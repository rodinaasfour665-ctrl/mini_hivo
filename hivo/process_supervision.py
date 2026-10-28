"""Absolute elapsed-time supervision; short waits survive Windows low-power gaps.

No process can enforce a deadline while the host is suspended. On resume this
controller checks its clock before accepting completion or allowing more work.
It owns only the explicitly launched process, never a shared provider service.
"""
import subprocess
import time


def supervise_process(args, *, seconds, cwd=None, stdout=None, cancelled=None,
                      on_event=None, clock=time.monotonic, pause=time.sleep,
                      factory=subprocess.Popen):
    started=clock();process=None;reason='completed';code=None;reaped=True
    def emit(kind,**fields):
        if on_event:on_event(dict(kind=kind,elapsed_seconds=clock()-started,**fields))
    emit('supervisor_started',limit_seconds=seconds)
    try:
        process=factory(args,cwd=cwd,stdout=stdout,stderr=subprocess.STDOUT,
                        creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
        emit('process_started',pid=process.pid)
        notice=clock()
        while True:
            # Check before poll: a late observed completion cannot become PASS.
            if cancelled and cancelled():reason='cancelled';break
            if clock()-started>=seconds:reason='deadline';break
            code=process.poll()
            if code is not None:break
            if clock()-notice>=15:
                emit('process_waiting');notice=clock()
            pause(min(.05,max(0,seconds-(clock()-started))))
    except KeyboardInterrupt:
        reason='interrupted'
    except Exception:
        reason='supervisor_error'
        raise
    finally:
        if process is not None and process.poll() is None:
            process.kill()
            # Bounded cleanup; an un-reaped owned process is an explicit failure.
            cleanup_started=clock()
            while process.poll() is None and clock()-cleanup_started<1:
                pause(.01)
            reaped=process.poll() is not None
        if process is not None:code=process.poll()
        emit('supervisor_finished',reason=reason,returncode=code,reaped=reaped)
    return dict(reason=reason,returncode=code,reaped=reaped,
                elapsed_seconds=clock()-started,limit_seconds=seconds)
