"""Controlled transport clocks; real ask/Worker/leaf gates and filesystem."""
import hashlib
import io
import json
import unittest
from unittest.mock import patch

import mini
from hivo.inference_transport import stream_chat, InferenceFailure
from hivo.http_client import JsonResponse
import test_greenfield_impact_lifecycle as lifecycle

REAL_ASK = mini.ask_ollama


def wire(message, done=True):
    return (json.dumps({'message': message, 'done': done, 'done_reason': 'stop'})+'\n').encode()


def fake_stream(steps, **kwargs):
    now=[0.];steps=iter(steps)
    class Response:
        def __enter__(self):return self
        def __exit__(self,*args):pass
        def read1(self,n):
            delay,data=next(steps,(0,b''));now[0]+=delay;return data
    return stream_chat('http://offline/api/chat',payload=kwargs.pop('payload',{}),
                       opener=lambda *a,**k:Response(),clock=lambda:now[0],**kwargs)


class FirstOutputTests(unittest.TestCase):
    def test_cold_first_output_can_exceed_old_deadline(self):
        reply=fake_stream([(180,wire({'content':'ready'}))],first_output_timeout_seconds=240)
        self.assertEqual(reply.json()['message']['content'],'ready')
        with self.assertRaises(InferenceFailure) as error:
            fake_stream([(180,wire({'content':'ready'}))])
        self.assertEqual(error.exception.kind,'INFERENCE_IDLE_TIMEOUT')

    def test_first_output_heartbeat_and_generation_limits_remain_bounded(self):
        cases=[([(241,wire({'content':'late'}))],'INFERENCE_FIRST_OUTPUT_TIMEOUT'),
               ([(100,wire({},False))]*3,'INFERENCE_FIRST_OUTPUT_TIMEOUT'),
               ([(180,wire({'content':'first'},False)),(121,wire({'content':'late'}))],'INFERENCE_IDLE_TIMEOUT'),
               ([(180,wire({'content':'first'},False)),(100,wire({'content':'next'},False)),
                 (81,wire({'content':'late'}))],'INFERENCE_DEADLINE')]
        for steps,kind in cases:
            with self.subTest(kind=kind),self.assertRaises(InferenceFailure) as error:
                fake_stream(steps,first_output_timeout_seconds=240)
            self.assertEqual(error.exception.kind,kind)

    def test_complete_tools_accumulate_but_partial_calls_never_return(self):
        call={'function':{'name':'write_file','arguments':{'path':'record.txt','content':'exact'}}}
        self.assertEqual(fake_stream([(150,wire({'tool_calls':[call]},False)),
            (1,wire({}))],first_output_timeout_seconds=240).json()['message']['tool_calls'],[call])
        for data in [wire({'tool_calls':[call]},False),wire({'tool_calls':{'bad':'shape'}})]:
            with self.subTest(data=data),self.assertRaises(InferenceFailure):
                fake_stream([(150,data)],first_output_timeout_seconds=240)

    def test_cancelled_cold_request_is_not_admitted(self):
        cancelled=[False]
        with self.assertRaises(InferenceFailure) as error:
            fake_stream([(150,wire({'content':'partial'},False)),(1,wire({'content':'done'}))],
                first_output_timeout_seconds=240,cancelled=lambda:cancelled[0],
                on_progress=lambda m:cancelled.__setitem__(0,True))
        self.assertEqual(error.exception.kind,'INFERENCE_CANCELLED')


class ChildTransportTests(unittest.TestCase):
    setUp=lifecycle.GreenfieldImpactLifecycleTests.setUp
    call=staticmethod(lifecycle.GreenfieldImpactLifecycleTests.call)

    def child(self):
        request=json.loads((mini.Path(__file__).parent/'fixtures/post_repair_requests.json').read_text(encoding='utf-8'))['inventory']['request']
        contract=mini.get_goal_contract(request,interactive=False)
        mini.RUN['source_contract']={'root_goal':contract['goal']}
        values={'products.txt':b'Product: Keyboard\nQuantity: 12\nPrice: 250',
                'supplier.txt':b'Supplier: Nile Tech\nCity: Cairo\nStatus: Active'}
        for path,data in values.items():(self.root/path).write_bytes(data)
        goal='Create a text file named shipment.txt containing exactly:'+json.dumps('Shipment: SH-2026\nItems: 12\nStatus: Pending')
        task=mini.make_task('3',goal,1,'ROOT',[goal],[])
        mini.TASKS['3']=task
        return task,contract,values

    def execute(self, task, contract, transport, legacy_failure=False):
        with patch.object(mini,'ask_ollama',REAL_ASK),patch.object(mini,'stream_chat',side_effect=transport),\
             patch.object(mini,'http_post_json',side_effect=(mini.HttpTransportError('controlled offline provider unavailable')
                 if legacy_failure else AssertionError('unexpected network'))),\
             patch.object(mini.time,'sleep'),patch('sys.stdout',new_callable=io.StringIO):
            return mini.execute_leaf(task,contract,{}, {'files':[]})

    def test_third_child_cold_inference_reaches_exact_receipt_without_sibling_changes(self):
        task,contract,siblings=self.child()
        replies=iter([self.call('context_sufficiency_check',context_status='sufficient',reason='Exact root source and owned obligation supplied.'),
            self.call('write_file',path='shipment.txt',content='Shipment: SH-2026\nItems: 12\nStatus: Pending'),
            self.call('run_file',path='shipment.txt'),{'content':'Independent verification complete.','tool_calls':[]}])
        seen=[]
        def transport(url,**kwargs):
            seen.append(kwargs);return fake_stream([(180,wire(next(replies)))],**kwargs)
        result=self.execute(task,contract,transport)
        self.assertEqual(result['status'],'done',str(result)[:1400])
        data=(self.root/'shipment.txt').read_bytes()
        self.assertEqual(len(data),43)
        self.assertEqual(hashlib.sha256(data).hexdigest(),'80e258c1a18bda44c6bdb66b1aef8ef3c2c006a9aa1f2c7911527111fa74c48e')
        self.assertEqual(result['impact_contract']['authorized_mutation_paths'],['shipment.txt'])
        self.assertEqual(result['literal_child_receipt']['artifacts'],{'shipment.txt':hashlib.sha256(data).hexdigest()})
        self.assertTrue(result['gate']['passed']);self.assertTrue(result['impact_comparison']['passed'])
        for path,expected in siblings.items():self.assertEqual((self.root/path).read_bytes(),expected)
        self.assertTrue(all(k['first_output_timeout_seconds']==240 for k in seen))
        self.observations={'artifact_sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data),
            'receipt':result['literal_child_receipt'],'impact_status':result['impact_comparison']['status'],
            'scope':result['impact_contract']['authorized_mutation_paths'],'controlled_first_output_seconds':180}

    def test_partial_write_stream_cannot_mutate_or_commit(self):
        task,contract,siblings=self.child();calls=[0]
        def transport(url,**kwargs):
            calls[0]+=1
            if calls[0]==1:
                message=self.call('context_sufficiency_check',context_status='sufficient',reason='Source is supplied.')
                return fake_stream([(1,wire(message))],**kwargs)
            message=self.call('write_file',path='shipment.txt',content='must never dispatch')
            return fake_stream([(1,wire(message,False))],**kwargs)
        result=self.execute(task,contract,transport)
        self.assertNotEqual(result['status'],'done')
        self.assertFalse((self.root/'shipment.txt').exists())
        self.assertNotIn('3',mini.RUN.get('_verified_literal_receipts',{}))
        for path,expected in siblings.items():self.assertEqual((self.root/path).read_bytes(),expected)

    def test_role_policy_is_scoped_and_cancellation_has_no_retry(self):
        reply=JsonResponse(200,json.dumps({'message':{'content':'ready'},'done':True}))
        for role in ['Builder','Falsifier','Specifier','Repairer','Coordinator']:
            with self.subTest(role=role),patch.object(mini,'stream_chat',return_value=reply) as stream,\
                 patch.object(mini,'http_post_json',return_value=reply) as post:
                REAL_ASK([],tools=None,role=role,provider_retries=0)
                self.assertEqual(stream.call_count,int(role in {'Builder','Falsifier','Specifier'}))
                self.assertEqual(post.call_count,int(role in {'Repairer','Coordinator'}))
                if role in {'Builder','Falsifier'}:
                    self.assertEqual(stream.call_args.kwargs['first_output_timeout_seconds'],240)
                    self.assertEqual(stream.call_args.kwargs['total_seconds'],360)
        with patch.object(mini,'stream_chat',side_effect=InferenceFailure('INFERENCE_CANCELLED','prompt',1)) as stream:
            with self.assertRaises(mini.ProviderError):REAL_ASK([],role='Builder',provider_retries=4)
        self.assertEqual(stream.call_count,1)

    def test_sibling_scope_guard_remains_effective_with_worker_streaming(self):
        task,contract,siblings=self.child()
        candidate=mini._prepare_task_impact_contract(task,contract)
        self.assertEqual(candidate['authorized_mutation_paths'],['shipment.txt'])
        replies=iter([self.call('context_sufficiency_check',context_status='sufficient',reason='Exact source supplied.'),
            self.call('write_file',path='products.txt',content='unauthorized replacement'),
            {'content':'Stop after refusal.','tool_calls':[]}])
        result=self.execute(task,contract,lambda url,**kwargs:fake_stream([(1,wire(next(replies,{'content':'stop'})))],**kwargs),legacy_failure=True)
        self.assertNotEqual(result['status'],'done')
        self.assertNotIn('3',mini.RUN.get('_verified_literal_receipts',{}))
        for path,expected in siblings.items():self.assertEqual((self.root/path).read_bytes(),expected)


if __name__=='__main__':unittest.main()
