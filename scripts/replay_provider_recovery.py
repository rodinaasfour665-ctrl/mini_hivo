"""Bounded real-model CLI with ONE disclosed, pre-dispatch transport fault.

No model response or tool result is fabricated. The first Builder inference
attempt raises a controlled transport timeout; the existing retry must call
real Ollama. This is mixed fault-injection/genuine-model evidence, not a
spontaneous provider outage or an unmodified live end-to-end benchmark.
"""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]


def child():
    sys.path.insert(0, str(ROOT))
    import mini
    from hivo.http_client import HttpTransportError
    original_ask, original_post, original_stream = mini.ask_ollama, mini.http_post_json, mini.stream_chat
    state = {'armed': False, 'injected': False}

    def inject_once():
        if state['armed'] and not state['injected']:
            state['injected'] = True
            mini.record_run_event('controlled_inference_fault_injected', role='Builder',
                                  boundary='before_http_request', count=1)
            raise HttpTransportError('controlled test injection: timed out before HTTP dispatch')

    def post(*args, **kwargs):
        inject_once()
        return original_post(*args, **kwargs)

    def stream(*args, **kwargs):
        inject_once()
        return original_stream(*args, **kwargs)

    def ask(*args, **kwargs):
        state['armed'] = kwargs.get('role') == 'Builder'
        try:
            return original_ask(*args, **kwargs)
        finally:
            state['armed'] = False

    mini.http_post_json, mini.stream_chat, mini.ask_ollama = post, stream, ask
    sys.argv = [str(ROOT / 'mini.py'), *sys.argv[2:]]
    mini.main()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path, required=True)
    args = parser.parse_args()
    out = args.output_dir.resolve()
    out.mkdir(parents=True, exist_ok=False)
    workspace = out / 'workspace'
    workspace.mkdir()
    request = json.loads((ROOT / 'tests/fixtures/post_repair_requests.json').read_text(encoding='utf-8'))['employee']['request']
    prompt = out / 'request.txt'
    prompt.write_text(request, encoding='utf-8', newline='\n')
    files = ['mini.py', 'hivo/requirements.py', 'hivo/inference_transport.py', 'hivo/http_client.py',
             'hivo/verification.py', 'hivo/pre_mutation_impact.py', 'hivo/host_preflight.py',
             'hivo/project_understanding.py', 'hivo/verification_routing.py',
             'tests/fixtures/post_repair_requests.json', 'scripts/replay_provider_recovery.py']
    pins = {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest() for name in files}
    started = time.monotonic()
    timed_out = False
    with (out / 'console.log').open('w', encoding='utf-8') as log:
        try:
            code = subprocess.run([sys.executable, '-u', '-B', '-X', 'utf8', str(Path(__file__).resolve()),
                                   '--child', '--no-bootstrap', '--workspace', str(workspace),
                                   '--prompt-file', str(prompt)], cwd=ROOT, stdout=log, stderr=subprocess.STDOUT,
                                  timeout=900, creationflags=subprocess.CREATE_NO_WINDOW).returncode
        except subprocess.TimeoutExpired:
            code, timed_out = None, True
    metrics = workspace / '.agent_experiment.jsonl'
    rows = [json.loads(line) for line in metrics.read_text(encoding='utf-8').splitlines()] if metrics.exists() else []
    row = rows[-1] if rows else {}
    traces = list((workspace / '.agent_runs').glob('*.jsonl'))
    events = [json.loads(line) for line in traces[0].read_text(encoding='utf-8').splitlines()] if traces else []
    injected = sum(event['kind'] == 'controlled_inference_fault_injected' for event in events)
    expected = b'Name: Sara\nDepartment: Engineering\nStatus: Active'
    artifact = workspace / 'employee.txt'
    data = artifact.read_bytes() if artifact.exists() else None
    record = {'verification_class': 'CONTROLLED_TRANSPORT_FAULT_WITH_GENUINE_OLLAMA',
              'model': 'gemma4:e4b', 'request': request, 'process_exit': code,
              'outer_timeout': timed_out, 'outer_limit_seconds': 900, 'injected_transport_failures': injected,
              'source_sha256': pins, 'wall_seconds': time.monotonic() - started,
              'trace_run_id': traces[0].stem if traces else None,
              'metrics': {key: row.get(key) for key in ['run_id', 'status', 'root_verified', 'model_calls',
                  'tool_calls', 'builder_calls', 'falsifier_calls', 'repairer_calls', 'elapsed_seconds',
                  'ollama_timeout_failures', 'ollama_retry_count', 'verification_classification_policy']},
              'artifact_oracle': {'exists': data is not None, 'exact_source_bytes': data == expected,
                  'bytes': len(data) if data is not None else None,
                  'sha256': hashlib.sha256(data).hexdigest() if data is not None else None},
              'passed': injected == 1 and row.get('root_verified') is True and row.get('status') == 'done'
                        and data == expected,
              'limits': 'One simulated timeout before network dispatch. All admitted model replies are real Ollama; inspect gates/commit and actual tool counts independently.'}
    (out / 'result.json').write_text(json.dumps(record, indent=2) + '\n', encoding='utf-8', newline='\n')
    print(json.dumps(record), flush=True)
    return 0 if record['passed'] else 1


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--child':
        child()
    else:
        raise SystemExit(main())
