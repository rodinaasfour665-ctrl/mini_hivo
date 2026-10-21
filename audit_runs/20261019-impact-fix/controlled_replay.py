"""Provider-free integration replay: only model responses are scripted.

This is not a live Ollama run and does not replace host qualification.
"""
import hashlib
import json
import sys
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
import mini

output = Path(__file__).parent
workspace = output / (sys.argv[1] if len(sys.argv) > 1 else 'controlled-baseline-routed')
workspace.mkdir(exist_ok=False)
mini.WORKSPACE = workspace.resolve()
mini._load_optional_imports()
mini.reset_run('baseline')
goal = (output / 'live-request.txt').read_text(encoding='utf-8')

def call(name, **arguments):
    return {'role': 'assistant', 'content': '', 'tool_calls': [
        {'function': {'name': name, 'arguments': arguments}}]}

responses = [
    {'role': 'assistant', 'content': 'I will do that.', 'tool_calls': []},
    call('context_sufficiency_check', context_status='sufficient',
         reason='The source contract states the literal filename, text type and exact content in an empty workspace.'),
    call('write_file', path='welcone.txt', content='welcome'),
    call('run_file', path='welcone.txt'),
    {'role': 'assistant', 'content': 'Exact file bytes verified.', 'tool_calls': []},
    call('run_file', path='welcone.txt'),
    {'role': 'assistant', 'content': 'Independent read-only Falsifier byte check passed.', 'tool_calls': []},
]
with patch.object(mini, 'structured_model_call', side_effect=mini.StructuredOutputError('offline replay')):
    contract = mini.get_goal_contract(goal, interactive=False)
    mini.RUN['source_contract'] = contract
    with patch.object(mini, 'ask_ollama', side_effect=responses) as provider:
        result, _ = mini.run_baseline_request(goal, {}, contract_override=contract,
                                              reset=False, finish=True, interactive=False)
data = {
    'execution_kind': 'PROVIDER_FREE_SCRIPTED_RESPONSES_REAL_CONTROLLER_AND_FILESYSTEM',
    'scripted_provider_responses': provider.call_count,
    'status': result.get('status'), 'failure_type': result.get('failure_type'),
    'file_exists': (workspace / 'welcone.txt').is_file(),
    'exact_bytes': (workspace / 'welcone.txt').read_bytes() == b'welcome' if (workspace / 'welcone.txt').exists() else False,
    'run_id': mini.RUN_ID,
    'source_sha256': hashlib.sha256((ROOT / 'mini.py').read_bytes()).hexdigest(),
    'production_source_sha256': {name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest() for name in (
        'mini.py', 'hivo/requirements.py', 'hivo/pre_mutation_impact.py', 'hivo/verification_routing.py')},
    'metrics': {key: mini.RUN.get(key) for key in (
        'impact_contracts_created', 'impact_contracts_validated', 'impact_contract_authorizations',
        'tool_calls', 'model_calls', 'root_verified', 'source_requirements_extracted', 'source_requirements_retained')},
    'source_requirement_ids': [item['requirement_id'] for item in mini.ledger_requirements(contract['source_requirement_ledger'])],
    'impact_comparison': result.get('impact_comparison'),
    'verification_aggregation': result.get('gate', {}).get('verification_aggregation'),
}
result_path = output / (sys.argv[1] + '-result.json' if len(sys.argv) > 1 else 'controlled-replay-result.json')
result_path.write_text(json.dumps(data, indent=2), encoding='utf-8')
print(json.dumps(data, indent=2))
raise SystemExit(0 if data['status'] == 'done' and data['exact_bytes'] else 1)
