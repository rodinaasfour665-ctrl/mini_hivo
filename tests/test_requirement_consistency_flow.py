"""Real source/CLI/persistence/gates; provider and terminal interaction scripted."""
import io
import json
from pathlib import Path
import unittest
from unittest.mock import patch
import mini
import test_greenfield_impact_lifecycle as lifecycle
import test_project12_clarification as project12
from hivo.literal_source import parse_literal_input
from hivo.requirement_decisions import RequirementDecisions

EMPLOYEE = '''Create exactly one UTF-8 text file named employee.txt in the workspace.

The exact content must be:
Name: Sara
Department: Engineering
Status: Active

The file must contain exactly three lines in the specified order.

Use LF line separators and no trailing newline at the end of the file.

Do not create any additional task files.

Verify that the file exists and that its content exactly matches the requested text before reporting completion.'''
EXPECTED='Name: Sara\nDepartment: Engineering\nStatus: Active'
HTML='''Create exactly one UTF-8 file named index.html in the workspace.

The exact content must be:
<!doctype html>
<html><head><title>Report</title></head><body style="color: navy">Ready</body></html>

Use LF line separators and no trailing newline. Keep the required title and inline styling. Do not create external CSS or additional task files. Verify exact contents.'''
MARKUP='<!doctype html>\n<html><head><title>Report</title></head><body style="color: navy">Ready</body></html>'


class RequirementConsistencyFlowTests(unittest.TestCase):
    setUp=lifecycle.GreenfieldImpactLifecycleTests.setUp
    call=staticmethod(lifecycle.GreenfieldImpactLifecycleTests.call)
    cli=project12.Project12ClarificationTests.cli

    def ledger(self,*texts):
        return mini.build_source_requirement_ledger([{'text':x,'source_segment':i+1} for i,x in enumerate(texts)])

    def read_contract(self,text,**kwargs):
        with patch.object(mini,'ask_ollama',side_effect=AssertionError('No provider during ingestion')):
            return mini.get_goal_contract(text,interactive=False,**kwargs)

    def test_exact_manual_request_preserves_content_and_opens_no_ui(self):
        with patch.object(mini,'select_clarification_option',side_effect=AssertionError('No clarification UI')):
            c=self.read_contract(EMPLOYEE)
        self.assertFalse(mini._contract_needs_clarification(c))
        self.assertEqual(parse_literal_input(EMPLOYEE).artifacts,{'employee.txt':EXPECTED})
        original=c['literal_clarification']['original_source_requirement_ledger']
        self.assertEqual(original['literal_obligations'][0]['content'],EXPECTED)
        self.assertEqual(c['literal_clarification']['original_request'],EMPLOYEE)

    def test_compatible_properties_generalize_across_artifact_types(self):
        cases=[
            ('Create exactly one text file named notes.txt.','Use LF separators and no trailing newline.'),
            ('The file must contain exactly three lines.','No final newline.'),
            ('Create exactly one task file.','Do not create any additional task files.'),
            ('Create page.html with a required title and structure.','Use inline styling.'),
            ('Create page.html.','Do not create external CSS.'),
            ('Create data.json with required keys.','Use two-space indentation.'),
            ('Create run.py.','The script must not delete files.'),
            ('Modify app.py.','Preserve unrelated.py unchanged.'),
            ('Use only LF for first.md.','Use only CRLF for second.css.'),
            ('Write an HTML page with inline CSS.','No external stylesheets.'),
            ('Include required content.','Do not include unrelated content.'),
            ('Use LF for app.js when exporting.','Use CRLF for app.js when importing.'),
        ]
        for pair in cases:
            with self.subTest(pair=pair):self.assertEqual(mini.detect_explicit_conflicts(self.ledger(*pair)),[])

    def test_literal_instruction_words_are_data_not_competing_policies(self):
        block='''Create exactly one UTF-8 file named example.md in the workspace.

The exact content must be:
Use only CRLF. Restart must erase all persisted data.

Use LF separators and no final newline. Preserve unrelated data.'''
        c=self.read_contract(block)
        self.assertFalse(mini._contract_needs_clarification(c))
        self.assertEqual(parse_literal_input(block).artifacts['example.md'],'Use only CRLF. Restart must erase all persisted data.')
        from hivo.requirement_consistency import contradiction
        self.assertIsNone(contradiction('Create a file named example.md containing exactly:"Use only CRLF"','Use only LF for example.md.'))
        from hivo.requirements import extract_source_requirements
        ledger=extract_source_requirements('Create a text file named Mixed.txt containing exactly:"A"\n\nCreate a text file named mixed.txt containing exactly:"a"')
        self.assertTrue(mini.detect_explicit_conflicts(ledger))

    def test_genuine_same_scope_conflicts_have_witnesses(self):
        cases=[('Use only LF for data.json.','Use only CRLF for data.json.'),
               ('Create a file named x.txt containing exactly:"A"','Create a file named x.txt containing exactly:"B"'),
               ('Create exactly one file.','Create exactly two files.'),
               ('Modify app.py.','Do not modify app.py.'),
               ('Preserve app.py unchanged.','Update app.py.'),
               ('Include line "Status: Active".','Do not include line "Status: Active".'),
               ('Include line "Ready".','Prohibit line "Ready".'),
               ('Include line "Ready".','The output should not include line "Ready".')]
        for pair in cases:
            with self.subTest(pair=pair):
                conflicts=mini.detect_explicit_conflicts(self.ledger(*pair));self.assertEqual(len(conflicts),1)
                self.assertIn('constraint_witness',conflicts[0])
                self.assertEqual(len(mini.conflict_questions(self.ledger(*pair),conflicts)),1)

    def test_enter_cancel_skip_do_not_select_a_blocking_default(self):
        c=self.read_contract('Build records.\n- Use only LF.\n- Use only CRLF.')
        q=c['questions'][0]
        self.assertIsNone(mini.select_clarification_option(q,key_sequence=['enter']))
        self.assertIsNone(mini.select_clarification_option(q,key_sequence=['esc']))
        r=mini.resolve_clarification_questions({'questions':[q]},terminal_available=True,selector=lambda *a,**k:None)
        self.assertEqual(r['status'],'clarification_required')
        self.assertEqual(r['answers'],[])

    def test_dialog_displays_actual_question_with_safe_initial_value(self):
        c=self.read_contract('Build records.\n- Use only LF.\n- Use only CRLF.');q=c['questions'][0]
        with patch.object(mini,'PROMPT_TOOLKIT_AVAILABLE',True),patch('prompt_toolkit.shortcuts.radiolist_dialog') as dialog:
            dialog.return_value.run.return_value=None
            self.assertIsNone(mini.select_clarification_option(q,terminal_available=True,output_fn=lambda *a:None))
        args=dialog.call_args.kwargs
        self.assertEqual(args['values'][0][0],None)
        self.assertIn(q['question'],args['text'])
        self.assertEqual(args['cancel_text'],'Leave unresolved')

    def test_pending_decision_survives_reset_and_preserves_original_requirements(self):
        raw='Build records.\n- Use only LF.\n- Use only CRLF.\n- Preserve audit history.'
        first=self.read_contract(raw);mini.reset_run('baseline')
        second=self.read_contract('Q-001: 1')
        self.assertFalse(mini._contract_needs_clarification(second))
        p=second['requirement_decisions']
        self.assertEqual(p['original_request'],raw)
        self.assertIn('Preserve audit history.',p['effective_request'])
        self.assertNotIn('CRLF',p['effective_request'])
        self.assertEqual(len(second['source_requirement_ledger']['requirements']),3)
        self.assertEqual(mini.detect_explicit_conflicts(mini._source_ledger_for_contract(second)),[])
        self.assertIsNone(RequirementDecisions(self.root).load())

    def test_other_requires_a_resolving_answer_and_keeps_unaffected_scope(self):
        raw='Build records.\n- Use only LF.\n- Use only CRLF.\n- Keep history.'
        self.read_contract(raw)
        invalid=self.read_contract('I do not know')
        self.assertTrue(mini._contract_needs_clarification(invalid))
        q=invalid['questions'][0]
        result=mini.get_goal_contract(raw,interactive=True,terminal_available=True,
            selector=lambda *a,**k:len(q['options']),answer_reader=lambda *a:'Use only LF.')
        self.assertFalse(mini._contract_needs_clarification(result))
        self.assertIn('Keep history.',result['requirement_decisions']['effective_request'])

    def test_multi_question_partial_answer_does_not_repeat_resolved_question(self):
        raw='Build records.\n- Use only LF for first.txt.\n- Use only CRLF for first.txt.\n- Modify app.py.\n- Preserve app.py unchanged.'
        first=self.read_contract(raw);self.assertEqual(len(first['questions']),2)
        mini.reset_run('baseline');partial=self.read_contract('Q-001: 1')
        self.assertTrue(mini._contract_needs_clarification(partial))
        self.assertEqual([q['question_id'] for q in partial['questions']],['Q-002'])
        done=self.read_contract('Q-002: 2');self.assertFalse(mini._contract_needs_clarification(done))
        self.assertEqual(len(done['clarification_answers']),2)

    def test_independent_task_and_workspace_do_not_consume_pending_decision(self):
        self.read_contract('Build records.\n- Use only LF.\n- Use only CRLF.')
        before=RequirementDecisions(self.root).load()
        fresh=self.read_contract(EMPLOYEE)
        self.assertFalse(mini._contract_needs_clarification(fresh))
        self.assertEqual(RequirementDecisions(self.root).load(),before)
        other=self.root/'separate';other.mkdir();mini.WORKSPACE=other
        self.assertIsNone(RequirementDecisions(other).load())
        self.assertFalse(mini._contract_needs_clarification(self.read_contract(HTML)))

    def test_cli_employee_reaches_real_verification_and_exact_bytes(self):
        rows=self.cli([EMPLOYEE],[{'employee.txt':EXPECTED}])
        self.assertEqual(rows[-1]['status'],'done');self.assertTrue(rows[-1]['root_verified'])
        self.assertEqual((self.root/'employee.txt').read_bytes(),EXPECTED.encode())
        self.assertGreater(rows[-1]['falsifier_calls'],0)

    def test_cli_exact_content_conflict_resumes_without_case_folding_or_deletion(self):
        raw='Create a text file named choice.txt containing exactly:"A"\n\nCreate a text file named choice.txt containing exactly:"a"'
        rows=self.cli([raw,'Q-001: 1'],[{'choice.txt':'A'}])
        self.assertEqual([r['status'] for r in rows],['clarification_required','done'])
        self.assertEqual(rows[0]['raw_user_request'],raw)
        self.assertTrue(rows[0]['source_requirement_ledger']['requirements'])
        self.assertIn('REQUEST_CLARIFICATION',rows[0]['control_flow'])
        self.assertEqual(rows[0]['source_requirements_extracted'],len(rows[0]['source_requirement_ledger']['requirements']))
        self.assertEqual(rows[0]['user_clarification_questions'],1)
        self.assertEqual((self.root/'choice.txt').read_bytes(),b'A')
        self.assertTrue(rows[-1]['root_verified'])

    def test_cancel_archives_original_without_selecting_a_requirement(self):
        raw='Build records.\n- Use only LF.\n- Use only CRLF.'
        self.read_contract(raw);c=self.read_contract('cancel task')
        self.assertTrue(mini._contract_needs_clarification(c))
        self.assertIsNone(RequirementDecisions(self.root).load())
        saved=json.loads((self.root/'.hivo/requirement-decisions.json').read_text())
        self.assertEqual(saved['status'],'cancelled');self.assertEqual(saved['original_request'],raw)
        self.assertEqual(saved['answers'],{})

    def test_other_cancellation_preserves_pending_source(self):
        raw='Build records.\n- Use only LF.\n- Use only CRLF.'
        result=mini.get_goal_contract(raw,interactive=True,terminal_available=True,
            selector=lambda *a,**k:2,answer_reader=lambda *a:(_ for _ in ()).throw(KeyboardInterrupt()))
        self.assertTrue(mini._contract_needs_clarification(result))
        self.assertEqual(RequirementDecisions(self.root).load()['answers'],{})

    def test_invalid_selection_is_not_clamped_to_a_source_option(self):
        raw='Build records.\n- Use only LF.\n- Use only CRLF.'
        result=mini.get_goal_contract(raw,interactive=True,terminal_available=True,selector=lambda *a,**k:-1)
        self.assertTrue(mini._contract_needs_clarification(result))
        self.assertEqual(RequirementDecisions(self.root).load()['answers'],{})

    def test_unresolved_authorization_can_still_require_targeted_clarification(self):
        raw='Update app.py only if modification is authorized; otherwise preserve it.'
        question={'question':'Is modification of app.py authorized for this task?',
            'reason':'The allowed mutation scope is unresolved.', 'affected_requirement_ids':['REQ-001'],
            'impact_if_unknown':'An incorrect choice could authorize a destructive change.',
            'options':['Preserve app.py unchanged.','Modify app.py.'],'recommended_option':'',
            'allow_other':True,'blocking':True}
        result=self.read_contract(raw,clarifier_call=lambda *a,**k:{'questions':[question]})
        self.assertTrue(mini._contract_needs_clarification(result))
        self.assertIn('authorized',result['questions'][0]['question'])

    def test_cli_html_reaches_browser_boundary_without_false_clarification(self):
        class BrowserBoundary(Exception):pass
        # Browser launch is a separately required gate, not a scripted PASS.
        # Inspect source -> real Builder/Falsifier handoff without installing
        # or launching a browser in the focused offline suite.
        with patch.object(mini,'optional_browser_check',side_effect=BrowserBoundary),self.assertRaises(BrowserBoundary):
            self.cli([HTML],[{'index.html':MARKUP}])
        self.assertEqual((self.root/'index.html').read_bytes(),MARKUP.encode())
        self.assertGreater(mini.RUN['falsifier_calls'],0)
        self.assertFalse(mini.RUN['root_verified'])

    def test_cli_multiple_artifacts_retain_independent_contents(self):
        raw='''Create exactly two UTF-8 files.
File: config.json
Exact content:
{"ready": true}

File: readme.md
Exact content:
# Ready

Use LF separators and no final newline. Do not create additional files. Verify exact contents.'''
        values={'config.json':'{"ready": true}','readme.md':'# Ready'}
        rows=self.cli([raw],[values]);self.assertEqual(rows[-1]['status'],'done')
        for n,v in values.items():self.assertEqual((self.root/n).read_bytes(),v.encode())


if __name__=='__main__':unittest.main()
