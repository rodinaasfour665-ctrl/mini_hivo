"""Real blocked I/O/processes and production parent gates; no Ollama calls."""
import io
import json
import subprocess
import sys
import threading
import time
import unittest
from unittest.mock import patch

import mini
from hivo.inference_transport import stream_chat,InferenceFailure
from hivo.process_supervision import supervise_process
import test_update004_verification_integration as integration
import test_greenfield_impact_lifecycle as lifecycle

REAL_ASK=mini.ask_ollama


class Response:
    def __init__(self,message=None):self.message=message or {'content':'complete'};self.closed=threading.Event()
    def __enter__(self):return self
    def __exit__(self,*args):self.closed.set()
    def read1(self,n):return (json.dumps({'message':self.message,'done':True})+'\n').encode()


class BlockedIOTests(unittest.TestCase):
    setUp=lifecycle.GreenfieldImpactLifecycleTests.setUp

    def test_headers_and_read_are_cancelled_while_blocked(self):
        for phase in ['headers','read']:
            with self.subTest(phase=phase):
                release=threading.Event();entered=threading.Event();cancel=threading.Event();response=Response()
                def block():entered.set();release.wait(3)
                def opener(*a,**k):
                    if phase=='headers':block()
                    return response
                if phase=='read':response.read1=lambda n:(block() or b'')
                timer=threading.Thread(target=lambda:(entered.wait(2),cancel.set()),daemon=True);timer.start()
                started=time.monotonic()
                try:
                    with self.assertRaises(InferenceFailure) as error:
                        stream_chat('http://offline',payload={},opener=opener,cancelled=cancel.is_set)
                    self.assertEqual(error.exception.kind,'INFERENCE_CANCELLED')
                    self.assertLess(time.monotonic()-started,1)
                    self.assertTrue(error.exception.cleanup_pending)
                finally:release.set();timer.join(1)
                self.assertTrue(response.closed.wait(1))

    def test_deadline_during_blocked_headers_and_read_has_no_late_admission(self):
        for phase in ['headers','read']:
            with self.subTest(phase=phase):
                release=threading.Event();response=Response();waits=[]
                def block():release.wait(3)
                def opener(*a,**k):
                    if phase=='headers':block()
                    return response
                if phase=='read':response.read1=lambda n:(block() or b'')
                started=time.monotonic()
                try:
                    with self.assertRaises(InferenceFailure) as error:
                        stream_chat('http://offline',payload={},opener=opener,total_seconds=.12,
                                    idle_seconds=2,on_wait=waits.append)
                    self.assertEqual(error.exception.kind,'INFERENCE_DEADLINE')
                    self.assertLess(time.monotonic()-started,1)
                    self.assertTrue(waits)
                finally:release.set()
                self.assertTrue(response.closed.wait(1))

    def test_suspend_jump_rejects_late_header_and_stream_result(self):
        for phase in ['headers','read']:
            with self.subTest(phase=phase):
                now=[0.];response=Response()
                def opener(*a,**k):
                    if phase=='headers':now[0]=1070.492
                    return response
                def read(n):now[0]=1070.492;return Response.read1(response,n)
                if phase=='read':response.read1=read
                with self.assertRaises(InferenceFailure) as error:
                    stream_chat('http://offline',payload={},opener=opener,clock=lambda:now[0],
                                first_output_timeout_seconds=240)
                self.assertEqual(error.exception.kind,'INFERENCE_DEADLINE')
                self.assertTrue(response.closed.wait(1))

    def test_uninterruptible_open_prevents_concurrent_provider_retry(self):
        release=threading.Event();response=Response();attempts=[]
        def transport(url,**kwargs):
            attempts.append(1)
            def opener(*a,**k):release.wait(3);return response
            kwargs.update(total_seconds=.12,idle_seconds=2,first_output_timeout_seconds=2)
            return stream_chat(url,opener=opener,**kwargs)
        try:
            with patch.object(mini,'stream_chat',side_effect=transport),self.assertRaises(mini.ProviderError) as error:
                REAL_ASK([],role='Builder',provider_retries=4)
            self.assertIn('cleanup pending',str(error.exception))
            self.assertEqual(len(attempts),1)
        finally:release.set()
        self.assertTrue(response.closed.wait(1))


class ProcessDeadlineTests(unittest.TestCase):
    def test_resume_jump_kills_before_accepting_late_exit(self):
        now=[0.];events=[]
        class Process:
            pid=123;code=None;killed=False
            def poll(self):return self.code
            def kill(self):self.killed=True;self.code=-9
        process=Process()
        def pause(seconds):now[0]+=1070.492
        result=supervise_process(['offline'],seconds=360,clock=lambda:now[0],pause=pause,
                                 factory=lambda *a,**k:process,on_event=events.append)
        self.assertEqual(result['reason'],'deadline');self.assertTrue(process.killed)
        self.assertTrue(result['reaped']);self.assertEqual(events[-1]['kind'],'supervisor_finished')

    def test_cancel_and_keyboard_interrupt_reap_owned_process(self):
        for interrupted in [False,True]:
            with self.subTest(interrupted=interrupted):
                now=[0.];cancel=[False]
                class Process:
                    pid=124;code=None
                    def poll(self):return self.code
                    def kill(self):self.code=-9
                def pause(seconds):
                    now[0]+=seconds;cancel[0]=True
                    if interrupted:raise KeyboardInterrupt
                result=supervise_process(['offline'],seconds=20,clock=lambda:now[0],pause=pause,
                    cancelled=lambda:cancel[0],factory=lambda *a,**k:Process())
                self.assertEqual(result['reason'],'interrupted' if interrupted else 'cancelled')
                self.assertTrue(result['reaped'])

    def test_real_sleeping_process_is_killed_at_short_outer_deadline(self):
        events=[];started=time.monotonic()
        result=supervise_process([sys.executable,'-B','-c','import time; time.sleep(30)'],
                                 seconds=.2,stdout=subprocess.DEVNULL,on_event=events.append)
        self.assertEqual(result['reason'],'deadline');self.assertTrue(result['reaped'])
        self.assertIsNotNone(result['returncode']);self.assertLess(time.monotonic()-started,2)

    def test_real_process_can_complete_before_deadline(self):
        result=supervise_process([sys.executable,'-B','-c','pass'],seconds=5,stdout=subprocess.DEVNULL)
        self.assertEqual(result['reason'],'completed');self.assertEqual(result['returncode'],0)


class ParentRecoveryTests(unittest.TestCase):
    setUp=lifecycle.GreenfieldImpactLifecycleTests.setUp
    call=staticmethod(lifecycle.GreenfieldImpactLifecycleTests.call)

    def execute(self,mode):
        seen=[];faulted=[False];parent_calls=[0]
        def adapter(propose):
            def provider(messages,*args,**kwargs):
                task=str((mini.ACTIVE_TOOL_CONTRACT or {}).get('task_id','ROOT'))
                if task!='ROOT':return propose(messages,*args,**kwargs)
                parent_calls[0]+=1
                proposal=propose(messages,*args,**kwargs)
                def transport(url,**options):
                    now=[0.];response=Response(proposal)
                    def read(n):
                        if mode=='permanent' or (mode=='retry' and not faulted[0]):
                            now[0]=1070.492;faulted[0]=True
                        return Response.read1(response,n)
                    response.read1=read;seen.append(kwargs.get('role'))
                    return stream_chat(url,opener=lambda *a,**k:response,clock=lambda:now[0],**options)
                with patch.object(mini,'stream_chat',side_effect=transport),patch.object(mini.time,'sleep'):
                    return REAL_ASK(messages,*args,**kwargs,provider_retries=1,
                                    cancelled=(lambda:True) if mode=='cancel' else None)
            return provider
        with patch.object(mini,'http_post_json',side_effect=AssertionError('live provider forbidden')):
            result,values,surfaces=integration.Update004VerificationTests.recursive(self,3,provider_adapter=adapter)
        for name,value in values.items():self.assertEqual((self.root/name).read_bytes(),value.encode('utf-8'))
        self.assertEqual(mini.RUN['literal_child_receipts_committed'],3)
        self.assertEqual(set(mini.RUN['_verified_literal_receipts']),{'1','2','3'})
        self.assertEqual(len(list(self.root.glob('*.txt'))),3)
        self.observations={'mode':mode,'result':result,'values':values,'parent_roles':seen,
                           'parent_model_invocations':parent_calls[0]}
        return result,seen

    def test_three_committed_children_reach_parent_falsifier_impact_and_commit(self):
        result,seen=self.execute('success')
        self.assertEqual(result['status'],'done',str(result)[:1000])
        self.assertTrue(result['gate']['passed']);self.assertTrue(result['impact_comparison']['passed'])
        self.assertEqual(result['impact_contract']['authorized_mutation_paths'],[])
        self.assertTrue(result['impact_contract']['literal_verification_only'])
        self.assertEqual(mini.RUN['parent_integrations_passed'],1)
        self.assertTrue(mini.RUN['root_verified']);self.assertIn('Falsifier',seen)

    def test_parent_deadline_retry_can_complete_without_rewriting_children(self):
        result,seen=self.execute('retry')
        self.assertEqual(result['status'],'done',str(result)[:1000])
        self.assertEqual(mini.RUN['parent_integrations_passed'],1)
        self.assertTrue(mini.RUN['root_verified']);self.assertIn('Falsifier',seen)

    def test_parent_timeout_keeps_children_and_cannot_claim_root_success(self):
        result,seen=self.execute('permanent')
        self.assertNotEqual(result['status'],'done')
        self.assertEqual(mini.RUN['parent_integrations_passed'],0)
        self.assertFalse(mini.RUN['root_verified']);self.assertNotIn('Falsifier',seen)

    def test_cancelled_parent_cannot_dispatch_a_proposal_or_retry(self):
        result,seen=self.execute('cancel')
        self.assertNotEqual(result['status'],'done')
        self.assertEqual(mini.RUN['parent_integrations_passed'],0)
        self.assertFalse(mini.RUN['root_verified']);self.assertEqual(seen,['Builder'])


if __name__=='__main__':unittest.main()
