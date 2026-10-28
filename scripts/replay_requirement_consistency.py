"""One explicitly requested bounded live CLI replay; preserve every outcome."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time

ROOT=Path(__file__).resolve().parents[1]
sys.path[:0]=[str(ROOT),str(ROOT/'tests')]
from test_requirement_consistency_flow import EMPLOYEE,EXPECTED,HTML,MARKUP
SOURCES=['mini.py','hivo/requirements.py','hivo/requirement_consistency.py','hivo/requirement_decisions.py',
         'hivo/literal_source.py','hivo/literal_clarification.py','hivo/project_understanding.py',
         'hivo/verification_routing.py','hivo/pre_mutation_impact.py','hivo/context_sufficiency.py',
         'hivo/artifact_progress.py','tests/test_requirement_consistency_flow.py']

def sha(data):return hashlib.sha256(data).hexdigest()

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--live',action='store_true',required=True)
    parser.add_argument('--case',choices=['employee','html'],required=True)
    parser.add_argument('--output-dir',type=Path,required=True)
    args=parser.parse_args();out=args.output_dir.resolve();out.mkdir(parents=True,exist_ok=False)
    workspace=out/'workspace';workspace.mkdir()
    request,values=(EMPLOYEE,{'employee.txt':EXPECTED}) if args.case=='employee' else (HTML,{'index.html':MARKUP})
    request_file=out/'request.txt';request_file.write_text(request,encoding='utf-8',newline='\n')
    sources={name:sha((ROOT/name).read_bytes()) for name in SOURCES}
    command=[sys.executable,'-u','-B','-X','utf8',str(ROOT/'mini.py'),'--no-bootstrap','--workspace',str(workspace),'--prompt-file',str(request_file)]
    started=time.monotonic();timed_out=False
    with (out/'console.log').open('w',encoding='utf-8',newline='\n') as log:
        try:code=subprocess.run(command,cwd=ROOT,stdout=log,stderr=subprocess.STDOUT,timeout=360,creationflags=subprocess.CREATE_NO_WINDOW).returncode
        except subprocess.TimeoutExpired:code=None;timed_out=True
    rows_file=workspace/'.agent_experiment.jsonl'
    rows=[json.loads(line) for line in rows_file.read_text(encoding='utf-8').splitlines()] if rows_file.exists() else []
    row=rows[-1] if rows else {}
    events=[]
    for trace in (workspace/'.agent_runs').glob('*.jsonl'):
        events.extend(json.loads(line) for line in trace.read_text(encoding='utf-8').splitlines())
    artifacts={name:{'expected_hex':content.encode().hex(),'expected_sha256':sha(content.encode()),
        'exists':(workspace/name).is_file(),'actual_sha256':sha((workspace/name).read_bytes()) if (workspace/name).is_file() else None,
        'exact_bytes':(workspace/name).is_file() and (workspace/name).read_bytes()==content.encode()} for name,content in values.items()}
    record={'verification_class':'LIVE_MODEL_ATTEMPT','case':args.case,'model':'gemma4:e4b','request':request,
        'source_sha256':sources,'source_unchanged':all(sha((ROOT/n).read_bytes())==d for n,d in sources.items()),
        'process_exit':code,'outer_timeout':timed_out,'wall_limit_seconds':360,'wall_seconds':round(time.monotonic()-started,2),
        'run_ids':list(dict.fromkeys(e.get('run_id') for e in events if e.get('run_id'))),
        'metrics':{k:row.get(k) for k in ['run_id','status','root_verified','model_calls','builder_calls','tool_calls','falsifier_calls','repairer_calls','impact_contract_authorizations','impact_contract_comparisons','elapsed_seconds','control_flow','project_mode']},
        'artifacts':artifacts,'no_false_source_conflict':(not any(e.get('kind')=='clarification_gate_evaluated' and e.get('conflict_count',0)>0 for e in events)
            if any(e.get('kind') in {'source_contract_ready','literal_source_compiled','clarification_gate_evaluated'} for e in events) else None),
        'source_compiled':any(e.get('kind')=='literal_source_compiled' for e in events),
        'terminal_record_available':bool(row),'note':'Inspect trace, actual tool results and every final gate before any end-to-end PASS claim; process exit alone is insufficient.'}
    (out/'result.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps({k:record[k] for k in ['case','process_exit','outer_timeout','run_ids','metrics','source_compiled']}),flush=True)
    return 0 if row.get('status')=='done' and row.get('root_verified') and all(x['exact_bytes'] for x in artifacts.values()) else 1

if __name__=='__main__':raise SystemExit(main())
