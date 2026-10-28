"""Production transport/Worker/gates with deterministic clocks and model proposals."""
import copy
import io
import json
import unittest
from types import SimpleNamespace
from urllib.error import HTTPError,URLError
from unittest.mock import patch
import mini
from hivo.inference_transport import stream_chat,InferenceFailure
from hivo.http_client import HttpTransportError,JsonResponse
from hivo import project_understanding
import test_greenfield_impact_lifecycle as lifecycle
import test_update004_verification_integration as integration
_REAL_ASK=mini.ask_ollama  # Boundary itself is tested with transport patched below.


class VerificationEnvironmentTests(unittest.TestCase):
    def test_normal_cli_selects_semantic_profile_and_legacy_remains_explicit(self):
        with patch('sys.argv',['mini.py']):
            self.assertEqual(mini.parse_args().verification_classification_policy,'field_scoped')
        with patch('sys.argv',['mini.py','--verification-classification-policy','current']):
            self.assertEqual(mini.parse_args().verification_classification_policy,'current')
        contract={'goal':'Create a simple profile page','impact_contract':{'contract_hash':'a'*20+'3d'+'b'*42}}
        self.assertEqual(mini.infer_web_profile(contract['goal'],contract,classification_policy='current').kind,'game')
        self.assertEqual(mini.infer_web_profile(contract['goal'],contract,classification_policy='field_scoped').kind,'web')
        self.assertEqual(mini.infer_web_profile('Create a 3D game',contract,classification_policy='field_scoped').kind,'game')

    def test_source_artifact_declarations_exclude_negative_and_literal_data(self):
        from hivo.requirements import named_artifact_declarations
        for name in ['view.html','data.json','src/check.py','./notes.md']:
            text=f'Create a standalone document named {name} with the requested behavior.'
            self.assertEqual([r['path'] for r in named_artifact_declarations(text)],[name])
        self.assertEqual(named_artifact_declarations('Do not create a file named extra.js.'),[])
        self.assertEqual(named_artifact_declarations('Create a text file named note.txt containing exactly: "Create a page named fake.html"'),[])

    def test_only_unrequested_loopback_favicon_404_is_optional(self):
        url='http://127.0.0.1:8080/index.html'
        icon='http://127.0.0.1:8080/favicon.ico'
        item={'url':icon,'text':'Failed to load resource: 404 (File not found)'}
        errors,optional=mini._classify_browser_console_errors([item],url)
        self.assertFalse(errors);self.assertEqual(optional[0]['url'],icon)
        for observation,explicit,requirement in [
            (item,[icon],''),(item,[],'A favicon is required'),
            (dict(item,url='http://127.0.0.1:8080/app.js'),[],''),
            (dict(item,text='Failed to load resource: 500'),[],''),
            (dict(item,url='http://other.test/favicon.ico'),[],''),
            (dict(item,text='application failed'),[],'')]:
            with self.subTest(observation=observation,explicit=explicit,requirement=requirement):
                errors,optional=mini._classify_browser_console_errors([observation],url,explicit,requirement)
                self.assertTrue(errors);self.assertFalse(optional)

    def test_discovered_browser_failure_tries_another_installed_channel(self):
        from unittest.mock import Mock
        browser_type=Mock(executable_path='missing-managed')
        browser_type.launch.side_effect=[RuntimeError('closed'), 'browser']
        with patch.object(mini,'browser_launch_kwargs',return_value={'headless':True,'channel':'msedge'}),patch.object(mini.Path,'is_file',return_value=True):
            self.assertEqual(mini.launch_verification_browser(browser_type),'browser')
        self.assertEqual(browser_type.launch.call_args.kwargs,{'headless':True,'channel':'chrome','timeout':15000})

    def test_installer_commands_are_refused_before_process_launch(self):
        with patch.object(mini.subprocess, 'run') as run:
            for command in ('npx playwright install', 'npx playwright install-deps',
                            'npx --yes playwright test', 'npx --package=playwright playwright test',
                            'npm install playwright'):
                with self.subTest(command=command):
                    self.assertIn('refused', mini.run_command(command))
            run.assert_not_called()

    def test_npx_verification_disables_implicit_package_acquisition(self):
        parts,error=mini._validated_command_parts('npx playwright test')
        self.assertIsNone(error)
        self.assertEqual(parts,['npx','--no-install','playwright','test'])
        self.assertIsNone(mini._validated_command_parts('npm test')[1])

    def test_managed_browser_precedes_system_discovery(self):
        with patch.object(mini.Path,'is_file',return_value=True), patch.object(mini.shutil,'which') as which:
            self.assertEqual(mini.browser_launch_kwargs(SimpleNamespace(executable_path='managed')),{'headless':True})
            which.assert_not_called()

    def test_installed_channel_fallback_and_missing_browser(self):
        # This test runs on Windows; patch platform explicitly without changing pathlib's class.
        with patch.object(mini.shutil,'which',return_value=None), patch.dict(mini.os.environ,{'PROGRAMFILES':'C:/Apps'}):
            with patch.object(mini.Path,'is_file',side_effect=lambda: False):
                self.assertEqual(mini.browser_launch_kwargs(),{'headless':True})
            with patch.object(mini.Path,'is_file',return_value=True):
                self.assertEqual(mini.browser_launch_kwargs(),{'headless':True,'channel':'msedge'})


def chunk(content='',done=False,**extra):
    return (json.dumps(dict(message={'content':content},done=done,**extra))+'\n').encode()


class StreamTests(unittest.TestCase):
    def stream(self,steps,**kwargs):
        now=[0.];steps=iter(steps)
        class Response:
            closed=False
            def __enter__(s):return s
            def __exit__(s,*args):s.closed=True
            def read1(s,n):
                dt,data=next(steps,(0,b''));now[0]+=dt
                if isinstance(data,BaseException):raise data
                return data
        response=Response()
        return stream_chat('http://localhost/api/chat',payload={'model':'gemma4:e4b'},opener=lambda *a,**k:response,clock=lambda:now[0],**kwargs)

    def test_fast_and_utf8_fragmented_response(self):
        data=chunk('مرحبا',True)
        r=self.stream([(1,data[:20]),(1,data[20:])]);self.assertEqual(r.json()['message']['content'],'مرحبا')

    def test_slow_prefill_and_progressing_generation_beyond_old_deadline(self):
        r=self.stream([(71,chunk('A')),(70,chunk('B')),(70,chunk('C',True))])
        self.assertEqual(r.json()['message']['content'],'ABC')
        self.assertEqual(r.json()['client_timing']['wall_seconds'],211)

    def test_prompt_and_generation_idle_are_bounded(self):
        for steps in [[(121,chunk('late',True))],[(1,chunk('A')),(121,chunk('late',True))]]:
            with self.subTest(steps=steps),self.assertRaises(InferenceFailure) as e:self.stream(steps)
            self.assertEqual(e.exception.kind,'INFERENCE_IDLE_TIMEOUT')

    def test_progress_does_not_extend_total_deadline(self):
        with self.assertRaises(InferenceFailure) as e:self.stream([(100,chunk('a'))]*4)
        self.assertEqual(e.exception.kind,'INFERENCE_DEADLINE')

    def test_cancelled_partial_or_late_response_is_not_returned(self):
        cancel=[False]
        with self.assertRaises(InferenceFailure) as e:
            self.stream([(1,chunk('partial')),(1,chunk('late',True))],cancelled=lambda:cancel[0],on_progress=lambda m:cancel.__setitem__(0,True))
        self.assertEqual(e.exception.kind,'INFERENCE_CANCELLED')

    def test_pre_cancel_never_opens_connection(self):
        with self.assertRaises(InferenceFailure):
            stream_chat('http://localhost',payload={},cancelled=lambda:True,opener=lambda *a,**k:self.fail('connection after cancellation'))

    def test_unavailable_has_distinct_category(self):
        with self.assertRaises(InferenceFailure) as e:
            stream_chat('http://localhost',payload={},opener=lambda *a,**k:(_ for _ in ()).throw(URLError('connection refused')))
        self.assertEqual(e.exception.kind,'INFERENCE_TRANSPORT_UNAVAILABLE')

    def test_http_500_is_not_unreachable(self):
        def opener(*a,**k):raise HTTPError('http://localhost',500,'server error',{},io.BytesIO(b'busy'))
        self.assertEqual(stream_chat('http://localhost',payload={},opener=opener).status_code,500)

    def test_protocol_eof_and_server_error_do_not_admit_partial(self):
        for data in [b'not-json\n',b'[]\n',b'{"message":3}\n',chunk('partial'),b'{"error":"runner failed"}\n']:
            with self.subTest(data=data),self.assertRaises(InferenceFailure):self.stream([(1,data)])


class WorkerHardeningTests(unittest.TestCase):
    def test_literal_child_scope_is_source_bound_when_planner_hints_are_absent(self):
        values={'first.txt':'one\ntwo','second.txt':'three\nfour'}
        goal='; '.join('Create a text file named '+p+' containing exactly:'+json.dumps(v) for p,v in values.items())
        contract=mini.get_goal_contract(goal,interactive=False)
        mini.RUN['source_contract']=contract
        local='Create a text file named first.txt containing exactly:'+json.dumps(values['first.txt'])
        for hints in [[],['text record'],['FIRST.TXT']]:
            child=mini.make_task('1',local,1,'ROOT',[local],hints)
            candidate=mini._prepare_task_impact_contract(child,contract)
            self.assertEqual(candidate['authorized_mutation_paths'],['first.txt'])
            self.assertTrue(candidate['expected_targets'][0].get('post_state_sha256'))
        for local_goal,hints in [(local,['second.txt']), (local,['../escape.txt']),
                                 (local.replace('one','invented'),[]), ('Unknown work',[])]:
            child=mini.make_task('1',local_goal,1,'ROOT',[local_goal],hints)
            candidate=mini._prepare_task_impact_contract(child,contract)
            self.assertFalse(mini.stage10_impact.accept_pre_mutation_impact_contract(candidate)['accepted'])
            self.assertFalse(candidate['authorized_mutation_paths'])

    def test_frozen_brain_root_goal_remains_the_actual_root_anchor(self):
        mini.RUN['source_contract']={'root_goal':'Authoritative whole-project source'}
        child=mini.make_task('1',self.goal,1,'ROOT',[self.goal],['welcone.txt'])
        candidate=mini._prepare_task_impact_contract(child,self.contract)
        self.assertEqual(candidate['root_goal'],'Authoritative whole-project source')
        self.assertFalse(mini.stage10_impact.validate_pre_mutation_impact_contract(
            candidate,root_goal='A different whole-project source')['valid'])

    def test_real_recursive_orchestration_with_brain_mission_compiler_and_empty_hints(self):
        request=json.loads((mini.Path(__file__).parent/'fixtures/post_repair_requests.json').read_text(encoding='utf-8'))['inventory']['request']
        values={'products.txt':'Product: Keyboard\nQuantity: 12\nPrice: 250',
                'supplier.txt':'Supplier: Nile Tech\nCity: Cairo\nStatus: Active',
                'shipment.txt':'Shipment: SH-2026\nItems: 12\nStatus: Pending'}
        clauses=['Create a text file named '+p+' containing exactly:'+json.dumps(v) for p,v in values.items()]
        contract=mini.get_goal_contract(request,interactive=False)
        counts={};compiled=[];projected={}
        original_context=mini.build_node_context
        def context(task,*args,**kwargs):
            mission=kwargs.get('worker_mission')
            if task.get('parent') and isinstance(mission,dict):projected[task['id']]=mission['targets']
            return original_context(task,*args,**kwargs)
        def structured(prompt,validator,label,schema,*args,**kwargs):
            if label=='decompose-task':
                data={'children':[{'goal':c,'done_when':[c],'scope_hint':[]} for c in clauses]}
            elif label=='task-fit':data={'decision':'execute'}
            elif label=='mission-compilation':
                context=json.loads(prompt.split('BOUNDED COMPILER CONTEXT:\n',1)[1])
                node=context['current_node'];compiled.append(node['id'])
                data={k:[] for k in mini._WORKER_MISSION_FIELDS}
                data.update(goal_anchor=contract['goal'],task=node['goal'],expected_outcome='Own source artifact verified',
                            targets=list(values),implementation_plan=['Follow the controller-owned node scope.'],
                            verification_plan=['Native exact source readback'],done_when=node['done_when'])
            else:raise mini.StructuredOutputError('offline model boundary: '+label)
            self.assertTrue(validator(data),label)
            return data
        def provider(*args,**kwargs):
            role=kwargs.get('role');node=str((mini.ACTIVE_TOOL_CONTRACT or {}).get('task_id','ROOT'))
            key=(role,node);counts[key]=counts.get(key,0)+1;n=counts[key]
            if role=='Builder':
                if n==1:return self.call('context_sufficiency_check',context_status='sufficient',reason='The owned source and exact artifact obligations are supplied.')
                if node!='ROOT' and n==2:
                    path=list(values)[int(node)-1];return self.call('write_file',path=path,content=values[path])
                if node=='ROOT' and n==2:return self.call('read_file',path=list(values)[0])
            if role=='Falsifier':
                paths=list(values) if node=='ROOT' else [list(values)[int(node)-1]]
                if n<=len(paths):return self.call('run_file',path=paths[n-1])
            return {'role':'assistant','content':'Current independent observations complete.','tool_calls':[]}
        with patch.object(mini,'structured_model_call',side_effect=structured),patch.object(mini,'ask_ollama',side_effect=provider),patch.object(mini,'build_node_context',side_effect=context),patch('sys.stdout',new_callable=io.StringIO):
            result,_=mini.run_recursive_request(request,{},contract_override=contract,repo_snapshot={'files':[]},
                initial_decision={'decision':'split'},specification_override=mini.specification_from_goal_contract(contract),finish=False)
        self.assertEqual(result['status'],'done',str(result)[:2500])
        self.assertTrue(mini.RUN['root_verified'])
        self.assertEqual(compiled,['1','2','3'])
        self.assertEqual(mini.RUN['literal_child_receipts_committed'],3)
        for name,value in values.items():self.assertEqual((self.root/name).read_bytes(),value.encode('utf-8'))
        for task_id,name in zip(['1','2','3'],values):
            self.assertEqual(mini.TASKS[task_id]['impact_contract']['authorized_mutation_paths'],[name])
            self.assertEqual(projected[task_id],[name])

    def test_named_nonliteral_invalid_or_overflow_sets_never_gain_partial_authority(self):
        cases=[['good.html','../escape.html'],['good.html','.hivo/private.html'],
               ['Alpha.html','alpha.html'],[f'page_{i}.html' for i in range(mini.stage10_impact.MAX_IMPACT_TARGETS+1)]]
        for paths in cases:
            goal='; '.join(f'Create a page named {path}' for path in paths)
            contract={'goal':goal,'original_goal':goal,'requirements':[goal],'constraints':[]}
            mini.RUN['source_contract']=contract
            candidate=mini._prepare_task_impact_contract(mini.root_task_from_contract(contract),contract)
            with self.subTest(paths=paths):
                self.assertFalse(candidate['authorized_mutation_paths'])
                self.assertFalse(mini.stage10_impact.accept_pre_mutation_impact_contract(candidate)['accepted'])

    def test_nonliteral_named_output_has_physical_targets_and_preserves_obligations(self):
        request='Create a standalone HTML page named profile.html. Include a heading and internal CSS. Do not create any other files.'
        self.goal=request
        self.contract=mini.get_goal_contract(request,interactive=False)
        mini.RUN['source_contract']=self.contract
        mini.ACTIVE_CONTRACT=self.contract;mini.ACTIVE_TOOL_CONTRACT=self.contract
        self.task=mini.root_task_from_contract(self.contract)
        candidate=mini._prepare_task_impact_contract(self.task,self.contract)
        self.assertEqual([r['target'] for r in candidate['expected_targets']],['profile.html'])
        self.assertEqual(candidate['authorized_mutation_paths'],['profile.html'])
        self.assertTrue(candidate['scope_required'])
        self.assertFalse(any('post_state_sha256' in t for t in candidate['expected_targets']))
        obligations=' '.join(r['meaning'] for r in candidate['verification_obligations'])
        self.assertIn('heading',obligations);self.assertIn('internal CSS',obligations)
        result=self.execute([self.call('context_sufficiency_check',context_status='sufficient',reason='The source declares this output and its requirements.'),
                             self.call('write_file',path='profile.html',content='<!doctype html><title>Profile</title><style>h1{color:blue}</style><h1>Profile</h1>'),
                             self.call('write_file',path='unrelated.txt',content='unauthorized'),
                             {'role':'assistant','content':'Stop for independent verification.','tool_calls':[]}])
        self.assertTrue((self.root/'profile.html').is_file())
        self.assertFalse((self.root/'unrelated.txt').exists())
        self.assertTrue(any('OUT_OF_SCOPE' in e['result'] for e in result['tool_evidence']))

    setUp=lifecycle.GreenfieldImpactLifecycleTests.setUp
    call=staticmethod(lifecycle.GreenfieldImpactLifecycleTests.call)
    execute=lifecycle.GreenfieldImpactLifecycleTests.execute
    responses=lifecycle.GreenfieldImpactLifecycleTests.responses

    def builder(self):
        result=self.execute(self.responses());self.task['impact_contract']=copy.deepcopy(result['impact_contract']);return result

    def test_refused_sibling_probe_recovers_without_repair_or_rewrite(self):
        builder=self.builder();before=(self.root/'welcone.txt').read_bytes()
        with patch.object(mini,'ask_ollama',side_effect=[self.call('run_file',path='sibling.txt')]):
            falsifier=mini.falsify_task(self.task,self.contract,{},builder,{'files':[]})
        self.assertEqual(falsifier['status'],'done')
        self.assertTrue(falsifier['policy_refusals'])
        self.assertEqual(mini._current_verification_failures(builder,falsifier),[])
        browser=mini.optional_browser_check(self.task,self.contract,execution_evidence=mini.merged_verification_evidence(builder,falsifier))
        gate=mini.evidence_gate(builder,falsifier,browser)
        self.assertTrue(gate['passed'],gate)
        self.assertEqual((self.root/'welcone.txt').read_bytes(),before)
        self.assertFalse((self.root/'sibling.txt').exists())
        self.assertEqual(mini.RUN['repairer_calls'],0)

    def test_wrong_bytes_are_not_dismissed_as_a_policy_failure(self):
        builder=self.builder();(self.root/'welcone.txt').write_bytes(b'wrong')
        with patch.object(mini,'ask_ollama',side_effect=[self.call('run_file',path='sibling.txt')]):
            f=mini.falsify_task(self.task,self.contract,{},builder,{'files':[]})
        self.assertEqual(f['status'],'failed');self.assertFalse(f['policy_refusals'])
        self.assertTrue(mini._current_verification_failures(builder,f))

    def test_scope_recovery_reaches_root_commit_without_repair_or_duplicate_write(self):
        steps={}
        def provider(*args,**kwargs):
            role=kwargs.get('role');steps[role]=steps.get(role,0)+1
            if role=='Builder':
                if steps[role]==1:return self.call('context_sufficiency_check',context_status='sufficient',reason='Exact source bytes and permitted target are supplied.')
                if steps[role]==2:return self.call('write_file',path='welcone.txt',content='welcome')
            if role=='Falsifier':return self.call('run_file',path='unrelated.txt')
            return {'role':'assistant','content':'Scoped inspection complete.','tool_calls':[]}
        with patch.object(mini,'ask_ollama',side_effect=provider),patch('sys.stdout',new_callable=io.StringIO):
            result,_=mini.run_baseline_request(self.goal,{},repo_snapshot={'files':[]},finish=True)
        self.assertEqual(result['status'],'done',result.get('summary'))
        self.assertTrue(mini.RUN['root_verified'])
        self.assertEqual(mini.RUN['repairer_calls'],0)
        self.assertEqual((self.root/'welcone.txt').read_bytes(),b'welcome')
        self.assertFalse((self.root/'unrelated.txt').exists())

    def test_stale_or_forged_native_proof_cannot_excuse_a_refusal(self):
        builder=self.builder();proof=json.loads(mini.run_file('welcone.txt')) if mini.ACTIVE_IMPACT_CONTRACT else None
        mini.ACTIVE_IMPACT_CONTRACT=builder['impact_contract']
        proof=json.loads(mini.run_file('welcone.txt'));mini._clear_impact_attempt()
        for field in ['impact_contract_hash','actual_sha256']:
            bad=dict(proof,**{field:'0'*64})
            f={'tool_evidence':[{'tool':'run_file','target':'sibling.txt','result':'error: literal verification is restricted to source-bound artifact paths'},
                                {'tool':'run_file','target':'welcone.txt','result':json.dumps(bad)}]}
            self.assertFalse(mini._safe_literal_policy_refusals(builder,f))

    def test_repair_anchor_uses_stable_parent_not_narrative_summary(self):
        builder=self.builder()
        with patch.object(mini,'ask_ollama',side_effect=[self.call('context_sufficiency_check',context_status='sufficient',reason='Owned exact target and its source are current.'),self.call('run_file',path='welcone.txt'),{'role':'assistant','content':'Current inspection complete.','tool_calls':[]}]):
            r=mini.repair_task(self.task,self.contract,[],{},'',parent_goal='Narrative parent summary is not a new goal anchor')
        self.assertEqual(r['status'],'done',r.get('summary'))
        self.assertEqual((self.root/'welcone.txt').read_bytes(),b'welcome')

    def test_genuine_anchor_change_is_still_rejected(self):
        self.builder();self.task['goal']='Change the source goal without approval'
        with patch.object(mini,'ask_ollama',side_effect=[self.call('context_sufficiency_check',context_status='sufficient',reason='Current context inspected.'),self.call('edit_file',path='welcone.txt',old='welcome',new='unsafe'),{'role':'assistant','content':'stop','tool_calls':[]}]):
            r=mini.repair_task(self.task,self.contract,[],{},'')
        self.assertNotEqual(r['status'],'done')
        self.assertEqual((self.root/'welcone.txt').read_bytes(),b'welcome')

    def test_inference_retry_success_exhaustion_and_no_tool_side_effects(self):
        message=JsonResponse(200,json.dumps({'message':{'content':'ok'},'done':True}))
        for replies,success in [([HttpTransportError('connection refused'),message],True),([HttpTransportError('timed out')]*2,False)]:
            mini.reset_run('baseline')
            with patch.object(mini,'stream_chat',side_effect=replies) as post,patch.object(mini.time,'sleep'):
                if success:self.assertEqual(_REAL_ASK([],tools=None,provider_retries=1)['content'],'ok')
                else:
                    with self.assertRaises(mini.ProviderError):_REAL_ASK([],tools=None,provider_retries=1)
            self.assertEqual(post.call_count,2);self.assertEqual(mini.RUN['tool_calls'],0)
            self.assertEqual(mini.RUN['ollama_retry_count'],1)

    def test_specifier_streams_but_cancel_is_not_retried(self):
        with patch.object(mini,'stream_chat',side_effect=InferenceFailure('INFERENCE_CANCELLED','generation',2)) as stream:
            with self.assertRaises(mini.ProviderError):_REAL_ASK([],tools=None,role='Specifier',provider_retries=4)
        self.assertEqual(stream.call_count,1)
        self.assertTrue(stream.call_args.kwargs['payload']['stream'])
        self.assertEqual(mini.RUN['tool_calls'],0)

    def test_complete_stream_and_typed_deadline_keep_provider_metrics_accurate(self):
        response=JsonResponse(200,json.dumps({'message':{'content':'{"ready":true}'},'done':True,'eval_count':12,'eval_duration':2000000000}))
        with patch.object(mini,'stream_chat',return_value=response) as stream:
            self.assertEqual(_REAL_ASK([],tools=None,role='Specifier',provider_retries=0)['content'],'{"ready":true}')
        self.assertEqual(stream.call_args.kwargs['total_seconds'],360)
        self.assertEqual(stream.call_args.kwargs['payload']['options']['num_predict'],1536)
        with patch.object(mini,'stream_chat',side_effect=InferenceFailure('INFERENCE_DEADLINE','generation',360)):
            with self.assertRaisesRegex(mini.ProviderError,'timed out'):_REAL_ASK([],tools=None,role='Specifier',provider_retries=0)
        self.assertEqual(mini.RUN['ollama_timeout_failures'],1)

    def test_physical_files_and_implementation_evidence_are_distinct(self):
        self.assertTrue(project_understanding.inventory_repository(self.root)['filesystem_empty'])
        (self.root/'prior.txt').write_text('preserved')
        inventory=project_understanding.inventory_repository(self.root)
        self.assertFalse(inventory['filesystem_empty']);self.assertTrue(inventory['implementation_empty'])
        (self.root/'app.py').write_text('print(1)')
        self.assertFalse(project_understanding.inventory_repository(self.root)['implementation_empty'])

    def test_nonliteral_falsifier_can_still_verify_an_authorized_script(self):
        (self.root/'check.py').write_text('print("SCRIPT_OK")',encoding='utf-8')
        mini.ACTIVE_TOOL_CONTRACT={'goal':'Verify the existing check.py script output'}
        mini.ACTIVE_IMPACT_CONTRACT=None
        result=mini.run_tool('run_file',{'path':'check.py'},role='Falsifier')
        self.assertIn('SCRIPT_OK',str(result))

    def test_real_recursive_receipt_counters_do_not_relabel_optional_stage5_metrics(self):
        result,values,_=integration.Update004VerificationTests.recursive(self,3)
        self.assertEqual(result['status'],'done')
        self.assertEqual(mini.RUN['literal_child_receipts_committed'],3)
        self.assertEqual(mini.RUN['literal_parent_integrations_verified'],1)
        for n,v in values.items():self.assertEqual((self.root/n).read_bytes(),v.encode())


if __name__=='__main__':unittest.main()
