"""Persistent controlled R_UPDATE_004 composition replay; never calls a live provider."""
import argparse
from contextlib import redirect_stdout, redirect_stderr
import hashlib
import json
from pathlib import Path
import shutil
import sqlite3
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT), str(ROOT/'tests')]
import mini
from test_update004_verification_integration import Update004VerificationTests

SOURCES = ['mini.py','hivo/project_understanding.py','hivo/verification_routing.py',
           'hivo/pre_mutation_impact.py','hivo/context_sufficiency.py','hivo/artifact_progress.py',
           'hivo/literal_source.py','hivo/literal_clarification.py','hivo/requirements.py',
           'tests/test_update004_verification_integration.py']

def sha(data): return hashlib.sha256(data).hexdigest()

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir',required=True,type=Path)
    args=parser.parse_args();out=args.output_dir.resolve();out.mkdir(parents=True,exist_ok=False)
    temp=out/'temporary';temp.mkdir();tempfile.tempdir=str(temp)
    summary=[]
    for count,dependent in [(n,False) for n in [1,2,3,4,5,8,10]]+[(3,True)]:
        case=f'{count}-'+('dependent' if dependent else 'independent');run=out/case;run.mkdir()
        test=Update004VerificationTests('runTest')
        try:
            with (run/'console.log').open('w',encoding='utf-8',newline='\n') as console,redirect_stdout(console),redirect_stderr(console):
                test.setUp();result,values,_=test.recursive(count,dependencies=dependent)
                mini.finish_metrics(result['status'])
                metrics={k:mini.RUN.get(k) for k in ['status','root_verified','model_calls','tool_calls','falsifier_calls','verified_nodes','failed_nodes']}
                run_id=mini.RUN_ID
                shutil.copytree(test.root,run/'workspace')
            workspace=run/'workspace'
            trace=workspace/'.agent_runs'/f'{run_id}.jsonl'
            events=[json.loads(x) for x in trace.read_text(encoding='utf-8').splitlines()]
            db=workspace/'.hivo/memory.sqlite3'
            with sqlite3.connect(db.as_uri()+'?mode=ro&immutable=1',uri=True) as connection:
                rows=connection.execute('select id,task_id,role,tool,target,status,content from events where run_id=? order by id',(run_id,)).fetchall()
            native=set();falsifier=set()
            for _,task,role,tool,target,status,content in rows:
                if task!='ROOT':continue
                if role=='Builder' and tool=='run_file':
                    try:proof=json.loads(content)
                    except ValueError:proof={}
                    if proof.get('passed') is True and proof.get('actual_sha256')==sha(values.get(target,'').encode()):native.add(target)
                if role=='Falsifier' and tool=='read_file' and status=='succeeded' and target in values and content.encode()==values[target].encode():falsifier.add(target)
                if role=='Falsifier' and tool=='run_file':
                    try:proof=json.loads(content)
                    except ValueError:proof={}
                    if target in values and proof.get('passed') is True and proof.get('actual_sha256')==sha(values[target].encode()):falsifier.add(target)
            actual={p.relative_to(workspace).as_posix() for p in workspace.rglob('*') if p.is_file() and not any(x.startswith('.') for x in p.relative_to(workspace).parts)}
            exact={n:{'exact':(workspace/n).read_bytes()==v.encode(),'expected_hex':v.encode().hex(),'actual_sha256':sha((workspace/n).read_bytes())} for n,v in values.items()}
            checks={'status_done':result['status']=='done','root_verified':metrics['root_verified'] is True,
                'exact_current_bytes':all(v['exact'] for v in exact.values()),'no_extra_task_files':actual==set(values),
                'parent_builder_native_coverage':native==set(values),'parent_falsifier_coverage':falsifier==set(values),
                'parent_no_mutation':not any(task=='ROOT' and tool in {'write_file','edit_file','edit_file_range'} and status=='succeeded' for _,task,_,tool,_,status,_ in rows),
                'parent_impact_passed':result['impact_comparison']['passed'] is True,
                'parent_gate_passed':result['gate']['passed'] is True,
                'parent_transaction_commit':any(e['kind']=='transaction_commit' and e.get('task_id')=='aggregate-ROOT' for e in events),
                'no_failed_nodes':metrics['failed_nodes']==0}
            record={'verification_class':'CONTROLLED_FUNCTIONAL','case':case,'run_id':run_id,
                'provider':'scripted tool proposals; real source/context/impact/leaf/Falsifier/parent/transaction',
                'decomposition':'explicit fixture child DAG; production scheduler/leaf/parent, no mocked successful child receipts',
                'workspace_snapshot':'Exact retained copy of test execution files; original temporary path differs.',
                'source_sha256':{n:sha((ROOT/n).read_bytes()) for n in SOURCES},'metrics':metrics,'checks':checks,'artifacts':exact,'passed':all(checks.values())}
            (run/'inspection.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8',newline='\n')
            summary.append({'case':case,'run_id':run_id,'passed':record['passed']});print(json.dumps(summary[-1]),flush=True)
        finally:test.doCleanups()
    (out/'results.json').write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8',newline='\n')
    return 0 if all(x['passed'] for x in summary) else 1

if __name__=='__main__':raise SystemExit(main())
