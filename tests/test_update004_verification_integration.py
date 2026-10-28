"""R_UPDATE_004: real gates, files, scheduler/leaf/parent; model replies scripted."""
import copy
import hashlib
import io
import json
from pathlib import Path
import unittest
from unittest.mock import patch
import mini
from hivo import project_understanding as stage2
import test_greenfield_impact_lifecycle as lifecycle


class Update004VerificationTests(unittest.TestCase):
    setUp = lifecycle.GreenfieldImpactLifecycleTests.setUp
    call = staticmethod(lifecycle.GreenfieldImpactLifecycleTests.call)

    def recursive(self, count=3, dependencies=False, tamper=None, provider_adapter=None):
        values = {f'entry_{i}.txt': f'Identifier: {i}\nGroup: {count}\nStatus: exact' for i in range(count)}
        if dependencies:
            values={}
            for i in range(count):
                predecessor=f'entry_{i-1}.txt' if i else 'none'
                digest=hashlib.sha256(values[predecessor].encode()).hexdigest() if i else 'none'
                values[f'entry_{i}.txt']=f'Identifier: {i}\nInput: {predecessor}\nInputSHA256: {digest}'
        clauses = ['Create a text file named '+n+' containing exactly:'+json.dumps(v) for n,v in values.items()]
        mini.reset_run('recursive'); mini.RUN['project_mode'] = mini.NEW_PROJECT
        contract = mini.get_goal_contract('; '.join(clauses), interactive=False)
        parent = mini.root_task_from_contract(contract); mini.TASKS['ROOT'] = parent
        children = [mini.make_task(str(i+1), goal, 1, 'ROOT', [goal], [name]) for i,(name,goal) in enumerate(zip(values,clauses))]
        for i,c in enumerate(children):
            if dependencies and i:c['dependencies'] = [children[i-1]['id']]
            mini.TASKS[c['id']] = c
        parent['children'] = [c['id'] for c in children]
        replies = []
        for n,v in values.items():
            replies += [self.call('context_sufficiency_check', context_status='sufficient', reason='Authoritative exact child source is complete.')]
            replies += [self.call('write_file',path=n,content=v), self.call('read_file',path=n), {'role':'assistant','content':'Independent child check complete.','tool_calls':[]}]
        replies += [self.call('context_sufficiency_check',context_status='sufficient',reason='Current child receipts permit independent parent inspection.')]
        replies += [self.call('read_file',path=n) for n in values]
        replies += [{'role':'assistant','content':'Parent inspection complete.','tool_calls':[]}]
        iterator = iter(replies); surfaces=[]
        def respond(*args,**kwargs):
            surfaces.append((kwargs.get('role'),{x['function']['name'] for x in kwargs.get('tools',[])}))
            return next(iterator,{'role':'assistant','content':'No additional operation proposed.','tool_calls':[]})
        aggregate = mini.aggregate_task
        def parent_step(*args,**kwargs):
            if tamper:tamper(args[2])
            return aggregate(*args,**kwargs)
        with patch.object(mini,'ask_ollama',side_effect=provider_adapter(respond) if provider_adapter else respond), patch('sys.stdout',new_callable=io.StringIO):
            result=mini._execute_children(parent,children,0,contract,{}, {'files':[]},'',[],
                fit_decider=lambda *args:{'decision':'execute'},leaf_executor=None,aggregator=parent_step)
        return result,values,surfaces

    def test_literal_creation_preservation_is_not_existing_project_intent(self):
        retained=json.loads((Path(__file__).parents[1]/'evidence/level2-generalized-recovery/checkpoint/latest-run-registry.json').read_text(encoding='utf-8'))
        for run in retained:
            self.assertEqual(stage2.classify_project_mode(run['raw_user_request'],{'files':[]})['project_mode'],mini.NEW_PROJECT)
        cases=json.loads((Path(__file__).parent/'fixtures/clarification_user_turns.json').read_text(encoding='utf-8'))
        for case in cases[:2]:
            text=case['request']+'\nPreserve each filename. Complete parent integration checks.'
            self.assertEqual(stage2.classify_project_mode(text,{'files':[]})['project_mode'],mini.NEW_PROJECT)
        for text in ['Modify the existing app.py','Fix the current API','Preserve existing behavior in missing code']:
            self.assertEqual(stage2.classify_project_mode(text,{'files':[]})['project_mode'],mini.EXISTING_PROJECT)
        self.assertEqual(stage2.classify_project_mode(cases[0]['request'],{'files':['app.py']})['project_mode'],mini.EXISTING_PROJECT)

    def test_parent_and_falsifier_verify_without_mutation_authority(self):
        result,values,surfaces=self.recursive()
        self.assertEqual(result['status'],'done',result.get('summary'))
        for n,v in values.items():self.assertEqual((self.root/n).read_bytes(),v.encode())
        parent=result['impact_contract']
        self.assertTrue(parent['literal_verification_only'])
        self.assertEqual(parent['authorized_mutation_paths'],[])
        self.assertTrue(result['impact_comparison']['passed'])
        for role,tools in surfaces:
            if role=='Falsifier':self.assertFalse({'write_file','edit_file','run_command','verify_web_app'} & tools)
        mini.ACTIVE_IMPACT_CONTRACT=parent;mini.ACTIVE_IMPACT_REQUIRED=True
        try:
            self.assertIn('READ_ONLY_PARENT',mini.run_tool('write_file',{'path':'extra.txt','content':'forbidden'},role='Builder'))
            self.assertIn('READ_ONLY_PARENT',mini.run_tool('run_command',{'command':'echo unsafe > extra.txt'},role='Falsifier'))
            self.assertIn('outside inspection scope',mini.run_tool('run_file',{'path':'unrelated.py'},role='Falsifier'))
            self.assertFalse((self.root/'extra.txt').exists())
        finally:mini._clear_impact_attempt()

    def test_dependencies_preserve_child_and_parent_verification(self):
        result,values,_=self.recursive(3,dependencies=True)
        self.assertEqual(result['status'],'done',result.get('summary'))
        for n,v in values.items():self.assertEqual((self.root/n).read_bytes(),v.encode())
        for i in range(1,3):
            digest=hashlib.sha256((self.root/f'entry_{i-1}.txt').read_bytes()).hexdigest()
            self.assertIn('InputSHA256: '+digest,(self.root/f'entry_{i}.txt').read_text())

    def test_independent_recursive_counts_preserve_all_artifacts(self):
        original=self.root
        try:
            for count in [1,2,3,4,5,8,10]:
                with self.subTest(count=count):
                    self.root=original/str(count);self.root.mkdir();mini.WORKSPACE=self.root
                    result,values,_=self.recursive(count)
                    self.assertEqual(result['status'],'done',result.get('summary'))
                    self.assertTrue(result['gate']['passed'])
                    self.assertTrue(result['impact_comparison']['passed'])
                    for n,v in values.items():self.assertEqual((self.root/n).read_bytes(),v.encode())
        finally:self.root=original;mini.WORKSPACE=original

    def test_stale_child_bytes_do_not_authorize_parent_integration(self):
        def change(_): (self.root/'entry_0.txt').write_bytes(b'out-of-band modification')
        result,_,_=self.recursive(tamper=change)
        self.assertNotEqual(result['status'],'done')
        self.assertFalse((result.get('builder',{}).get('impact_contract') or {}).get('literal_verification_only',False))

    def test_forged_child_contract_is_rejected(self):
        def change(children):children[0]['result']['impact_contract']['contract_hash']='0'*64
        result,_,_=self.recursive(tamper=change)
        self.assertNotEqual(result['status'],'done')

    def test_missing_child_gate_is_not_a_verified_receipt(self):
        def change(children):children[0]['result']['gate']={}
        result,_,_=self.recursive(tamper=change)
        self.assertNotEqual(result['status'],'done')

    def test_missing_committed_receipt_is_rejected(self):
        def change(children):children[0]['result'].pop('literal_child_receipt',None)
        result,_,_=self.recursive(tamper=change)
        self.assertNotEqual(result['status'],'done')

    def test_old_run_receipt_cannot_be_replayed(self):
        def change(children):children[0]['result']['literal_child_receipt']['run_id']='previous-run'
        result,_,_=self.recursive(tamper=change)
        self.assertNotEqual(result['status'],'done')

    def test_literal_native_checks_use_current_exact_bytes(self):
        result,values,_=self.recursive()
        accepted=result['impact_contract'];name=next(iter(values));target=self.root/name
        mini.ACTIVE_IMPACT_CONTRACT=accepted
        try:
            good=target.read_bytes()
            self.assertTrue(json.loads(mini.run_file(name))['passed'])
            for incorrect in [b'wrong',b'\xef\xbb\xbf'+good,good.replace(b'\n',b'\r\n'),good+b'\n',good.decode().encode('utf-16')]:
                with self.subTest(bytes=incorrect[:12]):
                    target.write_bytes(incorrect)
                    self.assertFalse(json.loads(mini.run_file(name))['passed'])
            target.unlink()
            self.assertIn('does not exist',mini.run_file(name))
            self.assertIn('does not exist',mini.run_file('wrong-name.txt'))
        finally:mini._clear_impact_attempt()

    def test_readonly_parent_rejects_unexpected_new_file(self):
        original=mini._impact_post_mutation_check
        def compare(contract,**kwargs):
            if contract.get('literal_verification_only'):
                (self.root/'unexpected.txt').write_bytes(b'external fault injection')
            return original(contract,**kwargs)
        with patch.object(mini,'_impact_post_mutation_check',side_effect=compare):
            result,_,_=self.recursive()
        self.assertNotEqual(result['status'],'done')
        self.assertIn('IMPACT_CONTRACT',result['failure_type'])

    def test_repairer_corrects_owned_corrupted_literal_and_reverifies(self):
        name='owned_record.txt';expected='State: correct';wrong='State: damaged'
        request='Create a text file named '+name+' containing exactly:'+json.dumps(expected)
        original=mini.run_tool;injected=False;steps={}
        def tool(n,args,role='System'):
            nonlocal injected
            result=original(n,args,role=role)
            if role=='Builder' and n=='write_file' and not injected and not mini.tool_result_failed(result):
                (self.root/name).write_bytes(wrong.encode());injected=True
            return result
        def provider(messages,**kwargs):
            role=kwargs.get('role');steps[role]=steps.get(role,0)+1
            if role=='Builder':
                if steps[role]==1:return self.call('context_sufficiency_check',context_status='sufficient',reason='Exact source bytes define the owned artifact.')
                if steps[role]==2:return self.call('write_file',path=name,content=expected)
            if role=='Repairer':
                if steps[role]==1:return self.call('context_sufficiency_check',context_status='sufficient',reason='The current digest failure identifies the exact damaged owned target.')
                if steps[role]==2:return self.call('edit_file',path=name,old=wrong,new=expected)
                if steps[role]==3:return self.call('run_file',path=name)
            if role=='Falsifier' and not any(m.get('role')=='tool' for m in messages):return self.call('read_file',path=name)
            return {'role':'assistant','content':'Current inspection complete.','tool_calls':[]}
        with patch.object(mini,'run_tool',side_effect=tool),patch.object(mini,'ask_ollama',side_effect=provider),patch('sys.stdout',new_callable=io.StringIO):
            result,_=mini.run_baseline_request(request,{},repo_snapshot={'files':[]},finish=True)
        self.assertTrue(injected)
        self.assertGreater(steps.get('Repairer',0),0)
        self.assertEqual(result['status'],'done',result.get('summary'))
        self.assertEqual((self.root/name).read_bytes(),expected.encode())
        self.assertTrue(mini.RUN['root_verified'])


if __name__ == '__main__': unittest.main()
