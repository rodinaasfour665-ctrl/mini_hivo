"""Bounded NDJSON chat inference. Partial/late output is never actionable."""
import json
import time
import queue
import socket
import threading
from urllib.request import Request, urlopen
from urllib.error import HTTPError, URLError
from .http_client import HttpTransportError, JsonResponse


class InferenceFailure(HttpTransportError):
    def __init__(self,kind,phase,elapsed):
        self.kind=kind;self.phase=phase;self.elapsed=elapsed
        super().__init__(f'{kind} during {phase} after {elapsed:.2f}s; no complete response admitted')


class _RequestIO:
    """One disposable I/O worker. Only the supervising caller admits responses.

    Short waits let the supervisor recheck absolute deadlines immediately after
    resume and cancel during a blocked open/read. The worker never runs tools.
    """
    def __init__(self):
        self.operations=queue.Queue();self.results=queue.Queue();self.response=None
        self.stopped=threading.Event()
        self.thread=threading.Thread(target=self._work,daemon=True,name='hivo-inference-io')
        self.thread.start()

    def _work(self):
        try:
            while not self.stopped.is_set():
                operation=self.operations.get()
                if operation is None:break
                try:self.results.put((True,operation()))
                except BaseException as exc:self.results.put((False,exc))
        finally:
            if self.response is not None:
                try:self.response.__exit__(None,None,None)
                except Exception:pass

    def call(self,operation,check,remaining,clock,on_wait,phase,started):
        check();self.operations.put(operation);last_notice=clock()-15
        while True:
            check()
            if on_wait and clock()-last_notice>=15:
                on_wait({'phase':phase,'elapsed_seconds':clock()-started,'event':'blocking_io_wait'})
                last_notice=clock()
            try:ok,value=self.results.get(timeout=max(.001,min(.05,remaining())))
            except queue.Empty:continue
            check()  # Reject buffered results after cancellation or host resume.
            if ok:return value
            raise value

    def stop(self):
        self.stopped.set();self.operations.put(None)
        sock=getattr(getattr(getattr(self.response,'fp',None),'raw',None),'_sock',None)
        if sock is not None:
            try:sock.shutdown(socket.SHUT_RDWR)
            except OSError:pass
        # Never block the controller on response.close() or an unresponsive opener.
        self.thread.join(.05)
        return not self.thread.is_alive()


def stream_chat(url,*,payload,total_seconds=360,idle_seconds=120,cancelled=None,
                on_progress=None,opener=urlopen,clock=time.monotonic,
                first_output_timeout_seconds=None,on_wait=None):
    started=last=clock();phase='prompt_or_headers';content=[];thinking=[];calls=[];buffer=b'';received=0;chunks=0;first=None
    first_limit=idle_seconds if first_output_timeout_seconds is None else first_output_timeout_seconds
    def inactivity_kind():
        return ('INFERENCE_FIRST_OUTPUT_TIMEOUT' if first is None and first_output_timeout_seconds is not None
                else 'INFERENCE_IDLE_TIMEOUT')
    def remaining_inactivity():
        return first_limit-(clock()-started) if first is None else idle_seconds-(clock()-last)
    def check():
        now=clock()
        if cancelled and cancelled():raise InferenceFailure('INFERENCE_CANCELLED',phase,now-started)
        if now-started>=total_seconds:raise InferenceFailure('INFERENCE_DEADLINE',phase,now-started)
        if remaining_inactivity()<=0:raise InferenceFailure(inactivity_kind(),phase,now-started)
    request=Request(url,data=json.dumps(dict(payload,stream=True),ensure_ascii=False).encode('utf-8'),
                    headers={'Content-Type':'application/json','Accept':'application/x-ndjson'},method='POST')
    io=None;failure=None
    try:
        check()
        io=_RequestIO()
        def remaining():return min(total_seconds-(clock()-started),remaining_inactivity())
        def blocking(operation):
            return io.call(operation,check,remaining,clock,on_wait,phase,started)
        def open_response():
            try:response=opener(request,timeout=min(total_seconds,first_limit))
            except HTTPError as exc:response=exc
            io.response=response
            return response.__enter__()
        response=blocking(open_response)
        if response is not None:
            status=getattr(response,'status',getattr(response,'code',200))
            if status!=200:
                phase='error_body'
                error=blocking(lambda:response.read(8*1024*1024+1))
                if len(error)>8*1024*1024:raise InferenceFailure('INFERENCE_RESPONSE_LIMIT',phase,clock()-started)
                return JsonResponse(status,error.decode('utf-8',errors='replace'))
            phase='prompt_or_first_token'
            while True:
                check()
                # Bound each blocking read by both remaining deadlines. read1
                # returns available bytes rather than waiting for an entire line.
                sock=getattr(getattr(getattr(response,'fp',None),'raw',None),'_sock',None)
                if sock is not None:sock.settimeout(max(.001,min(total_seconds-(clock()-started),remaining_inactivity())))
                data=blocking(lambda:response.read1(8192))
                check()  # A completed read after cancellation/deadline is discarded.
                if not data:raise InferenceFailure('INFERENCE_INCOMPLETE',phase,clock()-started)
                received+=len(data)
                if received>8*1024*1024:raise InferenceFailure('INFERENCE_RESPONSE_LIMIT',phase,clock()-started)
                buffer+=data
                while b'\n' in buffer:
                    line,buffer=buffer.split(b'\n',1)
                    if not line.strip():continue
                    value=json.loads(line.decode('utf-8'));chunks+=1
                    if not isinstance(value,dict):raise ValueError('stream chunk must be an object')
                    if value.get('error'):raise InferenceFailure('INFERENCE_SERVER_ERROR',phase,clock()-started)
                    message=value.get('message') or {}
                    if not isinstance(message,dict):raise ValueError('message must be an object')
                    c=message.get('content','');t=message.get('thinking','')
                    if c:content.append(c)
                    if t:thinking.append(t)
                    tool_calls=message.get('tool_calls') or []
                    if not isinstance(tool_calls,list):raise ValueError('tool_calls must be a list')
                    calls.extend(tool_calls)
                    if c or t or message.get('tool_calls'):
                        last=clock();phase='generation'
                        if first is None:first=last-started
                    if on_progress:on_progress({'elapsed_seconds':clock()-started,'phase':phase,'chunks':chunks,'content_chars':sum(map(len,content))})
                    check()
                    if value.get('done') is True:
                        body=dict(value,message={'role':'assistant','content':''.join(content),'thinking':''.join(thinking),'tool_calls':calls})
                        body['client_timing']={'wall_seconds':clock()-started,'first_output_seconds':first,'chunks':chunks,'total_limit_seconds':total_seconds,'idle_limit_seconds':idle_seconds,'first_output_limit_seconds':first_limit}
                        return JsonResponse(200,json.dumps(body,ensure_ascii=False))
    except InferenceFailure as exc:
        failure=exc
        raise
    except (TimeoutError, OSError, URLError) as exc:
        timed_out=isinstance(exc,TimeoutError) or 'timed out' in str(exc).lower()
        kind=('INFERENCE_DEADLINE' if clock()-started>=total_seconds else inactivity_kind()) if timed_out else 'INFERENCE_TRANSPORT_UNAVAILABLE'
        failure=InferenceFailure(kind,phase,clock()-started)
        raise failure from exc
    except (ValueError,TypeError,UnicodeError) as exc:
        failure=InferenceFailure('INFERENCE_PROTOCOL_ERROR',phase,clock()-started)
        raise failure from exc
    finally:
        if io is not None:
            stopped=io.stop()
            if failure is not None:
                failure.retry_safe=stopped
                failure.cleanup_pending=not stopped
