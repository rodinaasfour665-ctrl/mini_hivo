"""Bounded genuine local replay; exact stored user fixtures, fresh workspace."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from hivo.http_client import post_json,HttpTransportError
from hivo.process_supervision import supervise_process
from datetime import datetime,timezone


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--case',choices=['smoke','employee','html','inventory'],required=True)
    parser.add_argument('--output-dir',type=Path,required=True)
    parser.add_argument('--outer-seconds',type=int,default=900,
                        help='External replay wall limit, 1–3000 seconds; production budgets are unchanged.')
    args=parser.parse_args()
    if not 1<=args.outer_seconds<=3000:parser.error('--outer-seconds must be between 1 and 3000')
    out=args.output_dir.resolve();out.mkdir(parents=True,exist_ok=False)
    sources=['mini.py','hivo/inference_transport.py','hivo/process_supervision.py','hivo/http_client.py','hivo/host_preflight.py','hivo/project_understanding.py','hivo/verification.py','hivo/verification_routing.py','hivo/pre_mutation_impact.py','hivo/requirements.py','hivo/requirement_consistency.py','hivo/requirement_decisions.py','hivo/literal_source.py','tests/fixtures/post_repair_requests.json','scripts/replay_post_repair.py']
    pins={n:hashlib.sha256((ROOT/n).read_bytes()).hexdigest() for n in sources}
    started=time.monotonic()
    (out/'launch.json').write_text(json.dumps({'source_sha256':pins,'case':args.case,
        'configured_outer_seconds':args.outer_seconds,'started_at':datetime.now(timezone.utc).isoformat()},indent=2)+'\n',encoding='utf-8')
    if args.case=='smoke':
        try:
            response=post_json('http://127.0.0.1:11434/api/chat',timeout=120,payload={'model':'gemma4:e4b','messages':[{'role':'user','content':'Reply with exactly: HIVO_SMOKE_OK'}],'stream':False,'think':False,'options':{'num_predict':16,'num_ctx':4096,'temperature':0}})
            body=response.json();record={'case':'smoke','http_status':response.status_code,'content':(body.get('message') or {}).get('content'),'timing':{k:body.get(k) for k in ['total_duration','load_duration','prompt_eval_count','prompt_eval_duration','eval_count','eval_duration']}}
        except (HttpTransportError,ValueError) as exc:record={'case':'smoke','error':str(exc),'passed':False}
        record['passed']=record.get('http_status')==200 and 'HIVO_SMOKE_OK' in str(record.get('content'))
    else:
        request=json.loads((ROOT/'tests/fixtures/post_repair_requests.json').read_text(encoding='utf-8'))[args.case]['request']
        (out/'request.txt').write_text(request,encoding='utf-8',newline='\n');workspace=out/'workspace';workspace.mkdir()
        def supervision_event(row):
            with (out/'supervision.jsonl').open('a',encoding='utf-8',newline='\n') as evidence:
                evidence.write(json.dumps(dict(time=datetime.now(timezone.utc).isoformat(),**row))+'\n')
        with (out/'console.log').open('w',encoding='utf-8',newline='\n') as log:
            supervision=supervise_process([sys.executable,'-u','-B','-X','utf8',str(ROOT/'mini.py'),'--no-bootstrap','--workspace',str(workspace),'--prompt-file',str(out/'request.txt')],cwd=ROOT,stdout=log,seconds=max(0,args.outer_seconds-(time.monotonic()-started)),on_event=supervision_event)
        code=supervision['returncode'];timed_out=supervision['reason']=='deadline'
        rows_path=workspace/'.agent_experiment.jsonl';rows=[json.loads(x) for x in rows_path.read_text(encoding='utf-8').splitlines()] if rows_path.exists() else []
        row=rows[-1] if rows else {}
        record={'case':args.case,'request':request,'process_exit':code,'outer_timeout':timed_out,'outer_limit_seconds':args.outer_seconds,'supervision':supervision,'metrics':{k:row.get(k) for k in ['run_id','status','root_verified','model_calls','tool_calls','builder_calls','falsifier_calls','repairer_calls','elapsed_seconds','ollama_timeout_failures','ollama_retry_count','project_mode','control_flow','verification_classification_policy','browser_checks','impact_missing_targets','literal_child_receipts_committed','literal_parent_integrations_verified','parent_integrations_passed','verified_nodes','failed_nodes']},'passed':supervision['reason']=='completed' and supervision['reaped'] and code==0 and row.get('status')=='done' and row.get('root_verified') is True,'note':'No end-to-end claim until independent artifact, authorization, Falsifier, applicability/browser, impact and transaction inspection.'}
    record.update(verification_class='GENUINE_LOCAL_ATTEMPT',model='gemma4:e4b',source_sha256=pins,wall_seconds=time.monotonic()-started)
    (out/'result.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps(record),flush=True)
    return 0 if record['passed'] else 1
if __name__=='__main__':raise SystemExit(main())
