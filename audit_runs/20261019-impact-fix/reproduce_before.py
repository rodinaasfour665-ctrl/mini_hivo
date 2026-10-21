"""Replay the observed no-tool completion through the real pre-mutation gates."""
import hashlib
import json
import sys
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
import mini

workspace = Path(__file__).parent / 'before'
workspace.mkdir(exist_ok=False)
mini.WORKSPACE = workspace
mini.reset_run('baseline')
mini.RUN['project_mode'] = mini.NEW_PROJECT
goal = 'Create a text file named welcone containing exactly welcome.'
contract = {
    'goal': goal,
    'requirements': ['Create a text file.', "The file name must be 'welcone'.",
                     "The content of the file must be 'welcome'."],
    'constraints': [], 'success_criteria': ['welcone.txt contains exactly welcome'],
}
mini.RUN['source_contract'] = contract
task = mini.root_task_from_contract(contract)
candidate = mini._prepare_task_impact_contract(task, contract)
mini.ACTIVE_TOOL_CONTRACT = contract
with patch.object(mini, 'ask_ollama', return_value={'role': 'assistant', 'content': 'done', 'tool_calls': []}):
    result = mini.execute_agent_task(
        goal, {}, context_sufficiency_enabled=True,
        context_anchor={'root_goal': goal, 'local_task': goal, 'requirements': contract['requirements']},
        impact_contract=candidate, impact_contract_required=True,
    )
data = {key: result.get(key) for key in (
    'status', 'failure_type', 'summary', 'impact_validation', 'impact_authorized', 'context_sufficiency')}
data['metrics'] = {key: mini.RUN.get(key) for key in (
    'impact_contracts_created', 'impact_contracts_validated', 'impact_contract_authorizations', 'tool_calls')}
data['source_sha256'] = hashlib.sha256((ROOT / 'mini.py').read_bytes()).hexdigest()
(Path(__file__).parent / 'before-reproduction.json').write_text(json.dumps(data, indent=2), encoding='utf-8')
print(json.dumps({key: value for key, value in data.items() if key != 'context_sufficiency'}, indent=2))
