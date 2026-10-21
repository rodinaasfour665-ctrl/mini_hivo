# R_UPDATE_001 — HIVO historical changes audit

Audit date: 21 October 2026 (Africa/Cairo). Scope: documentation only. This report reconstructs existing work; it does not implement or validate a new application change.

## 1. Historical change summary and evidence standard

The most strongly attributable implementation is the 19 October 2026 greenfield pre-mutation impact-contract correction: four production files were modified, one regression file was added, and one existing regression expectation was modified. The supporting evidence comprises the previous root-cause report, saved pre-fix reproduction, exact test commands/logs, production hashes, a final-source integration replay, failed live attempts, and proof checks. The current four production hashes match the archived final replay hashes (checked by reading/hashing files during this documentation audit, without importing or executing project code).

Earlier work is also present: the local coding-agent architecture, versioned authority/recovery machinery, and Experiments 1–18. Existing documentation describes a linear Git history through Experiment 17 and a later revision for Experiment 18. Those commit identifiers are documentary references, not locally verified commits. No .git directory exists in this exported checkout, and git status --short returns “fatal: not a git repository”. Staged, unstaged, untracked, branch, commit dates, rename detection, deleted-file history, and exact diffs cannot be recovered from Git here. No clean-tree claim is made.

Confidence labels used throughout:

- **A — Strong attribution:** earlier report names the change and current source/artifacts corroborate it. This is evidence-based reconstruction, not a Git diff.
- **B — Historical documentary attribution:** older report/timeline associates a component with research work; exact original patch, author, and commit content cannot be independently checked.
- **C — Present, origin unresolved:** current contents are observable, but neither their original addition nor later modification is reliably attributable to a particular session.
- **G — Generated evidence:** run IDs, paths, logs, manifests or reports identify an output of the historical work. This does not mean the underlying experiment passed.
- **D — New documentation:** only this report and, if absent, its containing updates/ directory are created by the current task.

“Previous state” below refers to recorded behavior unless an actual historical source excerpt is available. No complete pre-fix production source copy was found. A source hash or a reproduction result is not a recoverable source version. Before/after source patches cannot honestly be fabricated.

### 1.1 Project structure inspected before writing

| Path | Current purpose | Attribution boundary |
|---|---|---|
| mini.py | CLI, request interpretation, task-tree/leaf controller, tools, transactions and runtime wiring | Four production-change areas detailed below; most of this large file predates the identified fix |
| hivo/ | 69 module files: source requirements, planning/approval, execution, evidence, context, verification, recovery and project intelligence | Existing architecture; only three modules are specifically attributable to the October 19 correction |
| scripts/ | 38 experiment harness/report/probe files | Historical research tooling, not new work in this audit |
| tests/ | 90 Python test files | Existing regression suites plus the specifically identified lifecycle addition and diagnostic edit |
| reports/ | 87 archived narrative/JSON/runbook/protocol files | Experiments 1–18, with different completion boundaries |
| docs/ | PROJECT_STATUS.md and EXPERIMENT_HISTORY.md | Older architecture/status and reported commit timeline |
| audit_runs/ | 130 retained files outside cache/environment exclusions | October 19 execution and correction artifacts, including generated disposable workspaces |
| list/ | 18 retained files outside cache/environment exclusions | Numbered user/runtime workspace artifacts; not all attributable to the fix |
| .venv/ and __pycache__/ | Existing interpreter/dependencies and cached bytecode | Not source history; recursively excluded from content-hash inventory; neither changed nor executed by this audit |
| README.md, requirements.txt, .gitignore, .gitattributes, .agent_experiment.jsonl | Existing root documentation/configuration/event record | Present; no evidence that these were edited during the correction |

The initial non-environment/non-cache inventory contains 440 files. All are listed in Section 10 with initial byte lengths and SHA-256 hashes. No AGENTS.md appeared in the project file search. No updates/ report existed in that inventory; R_UPDATE_001.md was therefore selected without replacing a prior report.

## 2. Verified October 19 implementation: file-by-file audit

### 2.1 mini.py — modified (A)

**Previous state/evidence.** audit_runs/20261019-impact-fix/before-reproduction.json captures source SHA-256 b22b51b3ae71e21893385fc1f940ef834f1a83337124b004e1e0af34944ed43b. The historical project-4 run 20261019T061903-f5bb5918 had the same source hash according to ROOT-CAUSE-REPORT.md. It created one candidate, validated zero contracts, authorized zero writes and executed zero tools. Its context snapshot was PREPARING_CONTEXT, round 0, context_status null, mutation_allowed false. The final failure_type was CONTEXT_INSUFFICIENT and summary blamed an unaccepted impact contract. The evidence indicates validation was never reached, rather than that validation rejected the contract.

**Current state and exact affected surfaces.**

1. Import at line 100 consumes hivo.requirements.literal_file_request. The run_file tool description at line 1006 now includes verification of controller-bound literal bytes.
2. run_file (line 1748; digest branch around 1756–1770) looks for ACTIVE_IMPACT_CONTRACT, or an accepted impact_contract in ACTIVE_TOOL_CONTRACT. It retains safe_path and existence checks. For an accepted target with post_state_sha256 it reads bytes, computes SHA-256, and returns structured LITERAL_ARTIFACT evidence before dispatching by executable suffix. A text artifact explicitly called proof.py is checked, not executed. Unrelated .py/.js/.cpp/HTML paths keep their pre-existing execution/verification routes.
3. _activate_impact_contract (2111) still invokes validate_pre_mutation_impact_contract and then accept_pre_mutation_impact_contract. It records invalid contracts and stops; it does not authorize a candidate merely because it exists. An accepted scope_required contract is also copied into ACTIVE_TOOL_CONTRACT at 2139 for the subsequent read-only verification context.
4. _impact_gate_mutation_guard (2168) still requires the earlier context gate. At 2199 it uses exact normalized-path membership for scope_required artifacts; ordinary contracts retain their existing allowed-path matcher. Rejections identify authorized targets. Thus welcone and welcone.txt do not become interchangeable write targets.
5. _prepare_task_impact_contract (2364) performs bounded compilation only in NEW_PROJECT, when there is no existing candidate and no execution contract. It parses original_goal when that key exists, otherwise goal. This avoids authorizing an abbreviated model interpretation that omitted additional original duties. For a recognized literal text-file request it preserves explicit suffixes, derives .txt for a bare basename, rejects unsafe/outside/existing/hidden-component targets, sets allowed_mutation_paths, expected_targets, scope_hint, and the expected UTF-8 digest. It binds source_requirements, scope_required, path_resolution and verification_obligations, refreshes the canonical contract hash, and records candidate metadata. The derived suffix is explicitly marked DERIVED; an explicit suffix retains USER_STATED provenance. Existing candidates are reused during repair so creation of the file does not destroy the original authority.
6. get_goal_contract (5522, reconciliation at 5553–5561) adapts a ready interpreted Goal Contract into an immutable source ledger when extraction yielded no records. It calls _record_source_ledger_metrics and establishes IDs before Stage 2, updates RUN.source_requirement_ledger, and records source_requirement_ledger_reconciled. Previously Project Brain's compatibility adapter created the IDs later, leaving Source Contract and Task Brain empty. _record_source_ledger_metrics (4947) is used here; its entire prior implementation is not claimed to be newly added.
7. _append_impact_contract_projection (13472) places the resolved literal plan first, followed by the bounded Worker packet and controller projection. It tells the Worker to use the resolved write_file/run_file path and explains exact-byte checking; the packet respects the existing node/mission bounds. The ordinary projection behavior remains for other contract classes.
8. execute_agent_task (13998; no-tool branch around 14603) gives one retry if the Worker has not submitted a context decision, state remains PREPARING_CONTEXT, and the existing step budget has room. It requests the structured context_sufficiency_check; it does not auto-pass it or increase budgets. Finalization around 15645–15758 distinguishes an unsubmitted decision (CONTEXT_SUFFICIENCY_REQUIRED) from an actual insufficient decision. Impact validation failures retain their precise reason rather than replacing the earlier context failure with an unrelated generic summary.
9. diagnose_failure (18721; branch at 18769) classifies CONTEXT_SUFFICIENCY_REQUIRED and IMPACT_CONTRACT_* failures as orchestration_failure with high confidence. It directs inspection to gate state/validation errors, avoiding an unsupported inference of missing repository context or bad implementation.
10. execute_leaf (19882; candidate preparation around 19911) passes the candidate and enabled context gate into the real Builder. It retains the accepted contract and propagates authorization failures before normal Falsifier/repair processing. The existing transaction, deterministic verification and post-state audit remain material boundaries.

**Recorded old versus current behavior.** A no-tool completion previously terminated with misleading insufficient-context/impact wording. Current code requests one bounded decision retry and preserves the actual missing-decision diagnosis if it still cannot authorize work. A source-defined single text file previously lacked a concrete named local scope and literal verifier; it now has exact target/digest obligations carried through authorization, Worker projection, readback and commit audit.

**Current excerpt (not a reconstructed historical diff):**

~~~python
literal = literal_file_request(source.get("original_goal", source.get("goal")))
relative = name if Path(name).suffix else name + ".txt"
~~~

The second line is inside the successful literal branch after name assignment; these are explanatory excerpts, not adjacent standalone runnable code.

**Dependencies.** hivo.requirements, context_sufficiency, pre_mutation_impact, verification_routing, safe_path, transaction capture, Source/Project/Task Brain projections, real Builder and Falsifier evidence.

**Verification.** Historical focused regressions and final-source replay are detailed in Sections 5–6. Current source SHA-256 is 07f08e30def31b9c05ca3574ee21d2582a88f82a612da9c35e6f6862c64f1401, matching controlled-final-result.json. No complete prior mini.py is available; precise changed line counts/import placement history and a literal before-code excerpt cannot be reconstructed.

### 2.2 hivo/requirements.py — modified (A)

**Previous state.** The original source extraction had an empty ledger for the short request; Goal Contract interpretation supplied three strings later. The earlier report separately reproduced a lexical coverage false negative between “file name … X” and “file named X”. The original per-ID coverage/specification payload is missing, so that reproduced defect cannot conclusively identify the original unmapped requirement.

**Current components.** literal_file_request at 387; deterministic_requirement_candidates at 403; specification_coverage at 1016 and its nested coverage_tokens. The recognizer uses re.fullmatch for create/make/write + text/txt file + named/called + one name + containing + optional exactly/the text + a quoted or single-token literal. It strips recognized quotes and terminal punctuation in its unquoted token handling. Arbitrary compound software requests are outside this bounded recognizer. A match emits creation, exact filename and exact-content requirements with functional category and source segment; the normal ledger builder assigns immutable IDs.

specification_coverage normalizes filename to “file name” and named to “name” before the existing conservative overlap threshold. It retains filename identifier tokens, so changing the actual filename still produces an unmapped obligation. It neither invents missing Specifier fields nor silently raises coverage to 100%.

**Current excerpt:**

~~~python
normalized = re.sub(r"\bfilename\b", "file name", str(value), flags=re.IGNORECASE)
normalized = re.sub(r"\bnamed\b", "name", normalized, flags=re.IGNORECASE)
return _overlap_tokens(normalized, normalized)[0]
~~~

**Purpose and behavior.** Give explicit single-file source facts a deterministic representation and avoid a narrow spelling-related mapping failure while preserving conservative omission detection. Consumers include get_goal_contract, source_contract_from_ledger, Brain creation and impact obligations. Historical tests cover three IDs, same-name mapping and different-name rejection. Current digest: 3845c4958d4f079f276d233d35d8ccdab133067a148c17032901e03ac0ccadf0. The historical full file is unavailable; older ledger immutability/conflict/clarification functions are not attributed wholesale to this fix.

### 2.3 hivo/pre_mutation_impact.py — modified (A)

**Previous state.** Existing contracts already had expected targets, provenance, validation, acceptance, mutation capture, semantic comparison and bounded projections. The prior generic target/verification surface did not enforce the exact literal-file post-state now required. ROOT-CAUSE-REPORT.md identifies the additions; no full old source is retained.

**Current components and mechanism.**

- _target_record (332; optional field at 347) preserves post_state_sha256 when provided.
- validate_pre_mutation_impact_contract (890; new requirements around 944–956) rejects scope_required contracts without an effective allowed path, checks every source requirement ID has a verification obligation, and rejects malformed expected digests unless they are 64 lowercase hex characters. Invalid schema/hash failures preserve IMPACT_INVALID rather than collapsing into incomplete.
- accept_pre_mutation_impact_contract (1063) remains the deterministic authority function used by the controller; it was not removed or replaced with a forced accepted flag.
- compare_pre_mutation_impact (1374; literal branch at 1412) finds the captured file's after record and requires existed is True and sha256 equals the expected digest. It emits literal_file_post_state / EXPECTED_AND_OBSERVED or EXPECTED_BUT_MISSING and adds a missing row on mismatch. Claimed verification PASS cannot substitute for actual post-state.
- project_impact_contract (1602; obligations around 1632) keeps bounded source/obligation IDs and authorized paths in the Worker-facing projection. No entire World Model is injected.

**Current excerpt:**

~~~python
matched = after.get("existed") is True and after.get("sha256") == digest
~~~

**Behavior impact and dependencies.** Contract construction now retains the literal digest, validation enforces source/scope completeness, and commit audit independently binds the filesystem state. It depends on existing canonical hashes, provenance checks, mutation snapshots and controller acceptance. Tests exercise invalid/missing/unaccepted contracts, wrong paths and wrong bytes despite claimed success. Current digest: 15804c02f44586aee7a936c01dcc80643f6697eafb0175024128c03f0b03ec6c. This does not prove general semantic verification for arbitrary new projects.

### 2.4 hivo/verification_routing.py — modified (A)

**Previous state.** A complete controlled replay exposed VERIFICATION_EVIDENCE_UNAVAILABLE: Stage 5A supplied only nonapplicable syntax/browser routes for the text artifact, so real readback could not satisfy required execution verification. Earlier replay setup failures are preserved and are not counted as successes.

**Current components.** LITERAL_ARTIFACT route constant; analyze_verification_applicability (969; branch at 1203–1214); _evidence_matches (1634). Only a scope_required impact contract with no impact_mutation_block_reason can emit the required literal route. Each concrete digest target supplies expected_sha256, impact_contract_hash and SOURCE_BOUND_LITERAL_POST_STATE.

Matching requires the tool to be run_file and both outer target and payload path to match the route. It parses string JSON when needed; requires verification_kind LITERAL_ARTIFACT, the accepted contract identity, expected digest, a 64-lowercase-hex observed digest, a real boolean passed value and matching PASS/FAIL status. It also requires the boolean to agree with observed==expected. A consistent native FAIL is matchable evidence of failure; matching is not synonymous with passing. Generic “PASS”, foreign authority, missing observation, contradictory status and unrelated tools/targets cannot satisfy the route.

**Dependencies and effect.** Reuses existing route aggregation, required verification sets and native tool evidence. Other browser/focused-test/direct-oracle/approved-authority branches remain separate in the current source. The previous report states their matching rules were retained; absent a full source diff, this audit cannot independently prove every unrelated line unchanged.

**Verification.** The final controller replay reaches route PASS, post-state PASS and root_verified true; native-proof-recheck.json records eleven positive/negative checks on retained actual native proof. Current digest: dbed610dcb219e9ca3aa3458aee73496388019c108024aef2bb3ebcef830f1ce. Full final regression rerun after the last matcher refinements was not executed historically.

### 2.5 tests/test_greenfield_impact_lifecycle.py — added (A)

GreenfieldImpactLifecycleTests begins at line 12. The file uses a temporary workspace and scripted model messages to exercise real controller and filesystem boundaries. It is a deterministic integration regression, not live Ollama reliability evidence. The historical report specifically identifies it as the new regression file; no Git creation event is available.

| Current method / line | Assertion boundary |
|---|---|
| test_a_simple_greenfield_file_verified_through_leaf / 68 | Real leaf, independent Falsifier, verification aggregation, commit and exact output |
| test_b_lifecycle_precedes_mutation / 85 | Candidate -> validator -> authorization before write |
| test_c_missing_invalid_rejected_and_out_of_scope_cannot_write / 98 | Missing/tampered/unaccepted/foreign-scope authority cannot mutate |
| test_d_requirement_ids_trace_to_source_brain_impact_and_worker / 113 | Source IDs retained across controller representations |
| test_e_existing_project_still_requires_plan_approval / 127 | Greenfield correction does not skip existing-repository approval |
| test_f_unsubmitted_context_is_not_reported_as_rejected_impact / 135 | Precise missing-decision diagnosis |
| test_rejected_candidate_is_diagnosed_and_stops_before_write / 143 | Invalid authorization terminates without mutation |
| test_wrong_content_cannot_pass_post_state_even_with_claimed_verification / 154 | Independent captured digest rejects false success |
| test_other_names_and_extensions_are_not_hardcoded / 160 | Generic name/suffix behavior |
| test_filename_mapping_requires_the_same_literal_name / 168 | Spelling normalization preserves identifier identity |
| test_legacy_goal_interpretation_populates_source_ledger_before_task_brain / 175 | Early ledger reconciliation and three stable IDs |
| test_unsafe_named_paths_never_authorize_creation / 188 | Traversal/metadata paths denied; compound original request not abbreviated into literal scope |
| test_rejection_is_not_generic_missing_context_diagnosis / 199 | Orchestration classification |
| test_resolved_path_is_mandatory_and_scope_errors_name_it / 203 | Worker sees derived .txt plan, packet bound and authorized-path error |
| test_literal_text_with_code_suffix_is_verified_without_execution / 220 | subprocess is patched to fail if literal verification executes code |
| test_reusing_candidate_after_creation_preserves_resolved_scope / 234 | Candidate survives in-progress artifact creation |
| test_literal_route_rejects_generic_or_foreign_proof / 241 | Typed proof rejects wrong identity/digest/missing/contradictory fields |

Current digest: 3344e113febe8b12116ca45e1bb447da080807aa22dc82c1d72a128930018704. Historical 17-test passing log precedes the last consistency/raw-source refinements; the final file has additional assertions and was not completely rerun after those refinements. This distinction prevents overstating the freshness of the suite result.

### 2.6 tests/test_context_sufficiency_gate.py — modified (A)

The identified change is in test_runtime_rejects_mutation_attempt_before_gate (227), at the expected failure_type assertion around line 255. The test still asserts mutation_calls==[] and mutation_authorized is false. It now expects CONTEXT_SUFFICIENCY_REQUIRED for a decision never submitted instead of generic CONTEXT_INSUFFICIENT. That previous expected value is recorded in the earlier change summary; the complete old test file is absent.

Current excerpt:

~~~python
self.assertEqual(mutation_calls, [])
self.assertEqual(result["failure_type"], "CONTEXT_SUFFICIENCY_REQUIRED")
self.assertFalse(result["mutation_authorized"])
~~~

The other eight current methods concern sufficient context, bounded completion, missing evidence, goal anchors, contradictions and disabled legacy behavior. They are pre-existing coverage, not all new changes. Historical nine-test suite passed. Current digest: ecdc62603c397d072c1e8f8f80fe212cc93912108a97afc2144a324df0444d54.

## 3. Why the correction was made: reconstructed failure chain

1. A literal-file request entered the normal source-understanding/NEW_PROJECT path. Stage 3 existing-repository impact planning is a different layer from local pre-mutation authorization.
2. The original Builder returned no tool calls. There was no context sufficiency decision, no write permission, and no validator invocation.
3. The candidate existed, but “created=1/validated=0/authorized=0” alone did not establish a rejected contract or validator exception.
4. Controller finalization obscured the true missing decision. Separately, requirement IDs were introduced too late for early Source/Task Brain artifacts.
5. Inspection identified downstream gaps: no exact named path, no literal readback, then no Stage 5A route for that readback.
6. The first corrected live diagnostic demonstrated context and impact authorization, but the model attempted the bare name three times; all were denied. The Worker packet was clarified to prioritize resolved path/provenance.
7. Controlled end-to-end replays exposed and then verified the routing integration. Final proof matching and original-source binding were tightened and checked.

The exact historical unmapped requirement is unresolved: only 2/3 counts survived, not the full original specification/per-ID coverage rows. No skipped rule or forced metric was introduced to claim coverage.

## 4. Earlier experiments and research changes

All outcomes below are historical reports, not trials performed by this audit. The named modules/harnesses are present and their current symbols are indexed in Section 9. Their experiment association is B unless noted. Historical “current” is the baseline of that particular cohort; it must not be assumed identical to today's source. Commit IDs come from docs/EXPERIMENT_HISTORY.md and are not locally resolvable.

### 4.1 Experiment 1 — Decomposition-first planning

- Reported history: e89e2e5, 5d56599.
- Files/components: hivo/decomposition_first.py; scripts/experiment1_report.py.
- Methodology/implementation: Early split validation, child-local contracts/brains and combined impact maps; compares current versus early decomposition.
- Recorded result and boundary: Two paired cases: current reached first Worker 1/2, early split 0/2; both first Child and final goal 0/2. Lower calls/time reflect different stopping points, not demonstrated efficiency.
- Evidence: [narrative](../reports/experiment1/final/report.md); [numeric/protocol record](../reports/experiment1/final/report.json). Supporting files under reports/experiment1/ are inventoried individually in Section 10.
- Historical source limitation: no original commit tree or complete before-version is available here; exact addition/modification status of each older component is unverified. No experiment was rerun in this audit.

### 4.2 Experiment 2 — Contract mission fallback

- Reported history: c697cc6, 19e877f.
- Files/components: mini.py; scripts/experiment2_report.py.
- Methodology/implementation: Fallback mission policy and paired reporting for one R-key case.
- Recorded result and boundary: Paired report exists; neither arm reports Child/Root verified. Exact historical implementation patch unavailable.
- Evidence: [narrative](../reports/experiment2/rkey_01/report.md); [numeric/protocol record](../reports/experiment2/rkey_01/report.json). Supporting files under reports/experiment2/ are inventoried individually in Section 10.
- Historical source limitation: no original commit tree or complete before-version is available here; exact addition/modification status of each older component is unverified. No experiment was rerun in this audit.

### 4.3 Experiment 3 — Progress-constrained Worker

- Reported history: d83876e.
- Files/components: hivo/worker_progress.py; scripts/experiment3_approved_run.py; scripts/experiment3_report.py.
- Methodology/implementation: WorkerProgress tracks attempted progress and enforces bounded progress_constrained behavior before/after first legal mutation.
- Recorded result and boundary: Paired report retains failed Child/Root outcomes; policy implementation is not proof of completion.
- Evidence: [narrative](../reports/experiment3/rkey_01/report.md); [numeric/protocol record](../reports/experiment3/rkey_01/report.json). Supporting files under reports/experiment3/ are inventoried individually in Section 10.
- Historical source limitation: no original commit tree or complete before-version is available here; exact addition/modification status of each older component is unverified. No experiment was rerun in this audit.

### 4.4 Experiment 4 — Evidence-grounded mutation

- Reported history: 7f2f4d3.
- Files/components: hivo/mutation_grounding.py; mini.py; scripts/experiment4_report.py.
- Methodology/implementation: Binds mutations to observed source; compares current and evidence_grounded. Prior rkey_02 output retained.
- Recorded result and boundary: Latest paired report reports no verified Child with committed edit and no Root success. Directory rkey_03 has heading rkey_01: preserve this documentary naming inconsistency.
- Evidence: [narrative](../reports/experiment4/rkey_03/report.md); [numeric/protocol record](../reports/experiment4/rkey_03/report.json). Supporting files under reports/experiment4/ are inventoried individually in Section 10.
- Historical source limitation: no original commit tree or complete before-version is available here; exact addition/modification status of each older component is unverified. No experiment was rerun in this audit.

### 4.5 Experiment 5 — Evidence-directed localization

- Reported history: fc21e38.
- Files/components: hivo/target_locator.py; scripts/experiment5_report.py.
- Methodology/implementation: TargetLocator ranks bounded candidate spans from goal/contract evidence under evidence_directed.
- Recorded result and boundary: Paired report exists; neither arm reports verified Child/Root. Later recovery tool-schema mismatch is documented under Experiment 18.
- Evidence: [narrative](../reports/experiment5/rkey_01/report.md); [numeric/protocol record](../reports/experiment5/rkey_01/report.json). Supporting files under reports/experiment5/ are inventoried individually in Section 10.
- Historical source limitation: no original commit tree or complete before-version is available here; exact addition/modification status of each older component is unverified. No experiment was rerun in this audit.

### 4.6 Experiment 6 — Verification environment classification

- Reported history: 7849040.
- Files/components: hivo/verification_environment.py; scripts/experiment6_report.py.
- Methodology/implementation: Preflights executable availability and distinguishes environment errors from behavior failures; retains earlier rkey_01.
- Recorded result and boundary: Paired current/resolved narrative and deterministic npm probe exist; neither paired arm reports Child/Root success.
- Evidence: [narrative](../reports/experiment6/rkey_02/report.md); [numeric/protocol record](../reports/experiment6/rkey_02/report.json). Supporting files under reports/experiment6/ are inventoried individually in Section 10.
- Historical source limitation: no original commit tree or complete before-version is available here; exact addition/modification status of each older component is unverified. No experiment was rerun in this audit.

### 4.7 Experiment 7 — Browser verification surface discovery

- Reported history: 0859b8a.
- Files/components: hivo/verification_surfaces.py; scripts/experiment7_candidate_probe.py; scripts/experiment7_report.py.
- Methodology/implementation: Discovers existing application hook __HOPLINE__ and executes game checks against same candidate plus original negative control.
- Recorded result and boundary: Same candidate: baseline VERIFIER_UNAVAILABLE, discovery PASS; original discovery TEST_FAILED. This isolates verifier reachability; live outcomes are separate.
- Evidence: [narrative](../reports/experiment7/rkey_01/report.md); [numeric/protocol record](../reports/experiment7/rkey_01/report.json). Supporting files under reports/experiment7/ are inventoried individually in Section 10.
- Historical source limitation: no original commit tree or complete before-version is available here; exact addition/modification status of each older component is unverified. No experiment was rerun in this audit.

### 4.8 Experiment 8 — Atomic verified child receipt

- Reported history: e31fe36.
- Files/components: hivo/atomic_child_receipt.py; scripts/experiment8_receipt_replay.py; scripts/experiment8_report.py.
- Methodology/implementation: Creates/validates/persists atomic evidence-bound child receipts and coverage.
- Recorded result and boundary: One same-patch replay: valid receipts 0/1 -> 1/1, integration NOT_READY -> READY. Live Child verified=1 but Root false because parent target unresolved; no general end-to-end success claim.
- Evidence: [narrative](../reports/experiment8/rkey_01/report.md); [numeric/protocol record](../reports/experiment8/rkey_01/report.json). Supporting files under reports/experiment8/ are inventoried individually in Section 10.
- Historical source limitation: no original commit tree or complete before-version is available here; exact addition/modification status of each older component is unverified. No experiment was rerun in this audit.

### 4.9 Experiment 9 — Integration target resolution

- Reported history: c367eae.
- Files/components: hivo/integration_targets.py; scripts/experiment9_parent_probe.py; scripts/experiment9_report.py.
- Methodology/implementation: Resolves parent targets/readiness and requires fresh parent proof rather than treating child evidence as parent proof.
- Recorded result and boundary: Parent probe and root_continuation comparison files retained. Full-run Root 0/2; isolated continuation evidence must not be substituted for full runs.
- Evidence: [narrative](../reports/experiment9/rkey_01/report.md); [numeric/protocol record](../reports/experiment9/rkey_01/report.json). Supporting files under reports/experiment9/ are inventoried individually in Section 10.
- Historical source limitation: no original commit tree or complete before-version is available here; exact addition/modification status of each older component is unverified. No experiment was rerun in this audit.

### 4.10 Experiment 10 — Child verification handoff diagnostics

- Reported history: 5c03694.
- Files/components: hivo/child_handoff_diagnostics.py; scripts/experiment10_capture.py; scripts/experiment10_handoff_probe.py; scripts/experiment10_report.py.
- Methodology/implementation: Captures full pre-browser handoff and audits route/evidence matching on the same state.
- Recorded result and boundary: Five frozen-boundary replays: target/applicability/start/behavior/evidence acceptance 5/5, behavior checks20/20, model/repairer0/0, receipts issued0. Worker, receipt commit and parent integration were not replayed.
- Evidence: [narrative](../reports/experiment10/rkey_01/report.md); [numeric/protocol record](../reports/experiment10/rkey_01/report.json). Supporting files under reports/experiment10/ are inventoried individually in Section 10.
- Historical source limitation: no original commit tree or complete before-version is available here; exact addition/modification status of each older component is unverified. No experiment was rerun in this audit.

### 4.11 Experiment 11 — Semantic evidence compatibility

- Reported history: 9db6907.
- Files/components: hivo/evidence_compatibility.py; hivo/atomic_child_receipt.py; scripts/experiment11_evidence_probe.py; scripts/experiment11_report.py.
- Methodology/implementation: Normalizes required claims/native evidence and validates compatible records; distinguishes invalid legacy receipt from real behavior PASS.
- Recorded result and boundary: Same historical state: current INVALID_RECEIPT versus compatible PASS. Report records four fresh Child/Root successes (4/4); one-case family limits apply; interim report retained.
- Evidence: [narrative](../reports/experiment11/rkey_01/report.md); [numeric/protocol record](../reports/experiment11/rkey_01/report.json). Supporting files under reports/experiment11/ are inventoried individually in Section 10.
- Historical source limitation: no original commit tree or complete before-version is available here; exact addition/modification status of each older component is unverified. No experiment was rerun in this audit.

### 4.12 Experiment 12 — Five-task generalization/reliability benchmark

- Reported history: 19f6317.
- Files/components: scripts/experiment12_fixtures.py; scripts/experiment12_run.py; scripts/experiment12_evidence_matrix.py; scripts/experiment12_handoff_probe.py; scripts/experiment12_report.py.
- Methodology/implementation: Frozen five-task fixtures, approved authorities, production pins, paired policies and three repeats (30-trial manifest). Planning is excluded from frozen-contract execution.
- Recorded result and boundary: Archived results set all_completed=true and planning_included=false. Earlier report notes current Node Root3/3, Timer/Python did not reach executable verification. October19 new Node pilot failed before Worker after120s; cohorts are not interchangeable.
- Evidence: [narrative](../reports/experiment12/experiment12-report.md); [numeric/protocol record](../reports/experiment12/experiment12-results.json). Supporting files under reports/experiment12/ are inventoried individually in Section 10.
- Historical source limitation: no original commit tree or complete before-version is available here; exact addition/modification status of each older component is unverified. No experiment was rerun in this audit.

### 4.13 Experiment 13 — Monotonic semantic compatibility

- Reported history: 85a57f7.
- Files/components: hivo/evidence_monotonic.py; scripts/experiment13_evidence_probe.py; scripts/experiment13_handoff_probe.py; scripts/experiment13_run.py; scripts/experiment13_report.py.
- Methodology/implementation: Retains supported semantic evidence while rejecting invalid bindings; proof_bindings/binding_errors and same-state handoffs.
- Recorded result and boundary: Fresh Root current3/9 versus monotonic8/9; valid receipts/actual PASS3/9 versus8/8; false rejection6/9 versus0/8. These have different denominators and must remain distinct.
- Evidence: [narrative](../reports/experiment13/experiment13-report.md); [numeric/protocol record](../reports/experiment13/experiment13-results.json). Supporting files under reports/experiment13/ are inventoried individually in Section 10.
- Historical source limitation: no original commit tree or complete before-version is available here; exact addition/modification status of each older component is unverified. No experiment was rerun in this audit.

### 4.14 Experiment 14 — Strict aggregation compatibility

- Reported history: b61c474.
- Files/components: hivo/evidence_strict.py; scripts/experiment14_evidence_probe.py; scripts/experiment14_handoff_probe.py; scripts/experiment14_run.py; scripts/experiment14_report.py.
- Methodology/implementation: Checks route/evidence identity and integrates strict aggregation while preserving valid evidence; v1/v2 supporting records retained.
- Recorded result and boundary: Fresh monotonic and strict arms each Child/Root9/9 and valid receipts9/9. This reports compatibility on the selected cohort, not superiority or universal reliability.
- Evidence: [narrative](../reports/experiment14/experiment14-report.md); [numeric/protocol record](../reports/experiment14/experiment14-results.json). Supporting files under reports/experiment14/ are inventoried individually in Section 10.
- Historical source limitation: no original commit tree or complete before-version is available here; exact addition/modification status of each older component is unverified. No experiment was rerun in this audit.

### 4.15 Experiment 15 — Evidence-to-edit mutation binding

- Reported history: e768fda.
- Files/components: hivo/mutation_grounding.py; scripts/experiment15_binding_probe.py; scripts/experiment15_run.py; scripts/experiment15_report.py.
- Methodology/implementation: Bounded exact source-span/hash grounding, stale-anchor rejection and refresh recovery; grounded versus bound policies.
- Recorded result and boundary: Fresh grounded/bound arms each verification-after-mutation, Child and Root9/9. Later Colab positive control arena_q_restart records4/4 Child and4/4 Root checks; that is a separate control.
- Evidence: [narrative](../reports/experiment15/experiment15-report.md); [numeric/protocol record](../reports/experiment15/experiment15-results.json). Supporting files under reports/experiment15/ are inventoried individually in Section 10.
- Historical source limitation: no original commit tree or complete before-version is available here; exact addition/modification status of each older component is unverified. No experiment was rerun in this audit.

### 4.16 Experiment 16 — Timer/Python first-blocker isolation

- Reported history: 6eeca6c.
- Files/components: scripts/experiment16_run.py; scripts/experiment16_report.py; hivo/context_sufficiency.py; hivo/mutation_grounding.py; hivo/verification.py.
- Methodology/implementation: Three frozen runs each of Timer and Python under contract_fallback/strict/evidence_bound and28-step budget; records first reached boundary.
- Recorded result and boundary: Timer context/legal mutation3/3, formal child verifier2/3, Child0/3; Python context/legal mutation0/3. No shared first blocker established; two Timer verifier calls chose Game.
- Evidence: [narrative](../reports/experiment16/experiment16-report.md); [numeric/protocol record](../reports/experiment16/experiment16-results.json). Supporting files under reports/experiment16/ are inventoried individually in Section 10.
- Historical source limitation: no original commit tree or complete before-version is available here; exact addition/modification status of each older component is unverified. No experiment was rerun in this audit.

### 4.17 Experiment 17 — Opt-in field-scoped browser classification

- Reported history: cbed365.
- Files/components: hivo/verification.py; scripts/experiment17_run.py; scripts/experiment17_report.py; tests/test_experiment17_classification.py (only if present; see inventory for exact test names).
- Methodology/implementation: infer_web_profile supports field_scoped semantic inputs instead of whole-contract JSON/hash substrings; current remains default.
- Recorded result and boundary: Frozen Timer current0/3 versus field_scoped3/3; games retained6/6; identity invariance27/27. No completed fresh Worker outcome in this protocol; report/runbook existence does not mean nine live runs completed.
- Evidence: [narrative](../reports/experiment17/classification-protocol.md); [numeric/protocol record](../reports/experiment17/classification-protocol.json). Supporting files under reports/experiment17/ are inventoried individually in Section 10.
- Historical source limitation: no original commit tree or complete before-version is available here; exact addition/modification status of each older component is unverified. No experiment was rerun in this audit.

### 4.18 Experiment 18 — Context, mutation recovery and verifier follow-up

- Reported history: 4d1760b292d0ba9021b5e957a870053407bbee5c (reported baseline revision).
- Files/components: hivo/context_sufficiency.py; hivo/target_locator.py; hivo/mutation_grounding.py; hivo/verification.py; hivo/browser_checks.py; mini.py.
- Methodology/implementation: Diagnostics and controlled verification replay, documented in RESEARCH_HISTORY.md and EXPERIMENT18B_HANDOFF.md; no proven causal recovery fix.
- Recorded result and boundary: Windows2 eligible trials blocked before mutation. Colab current reached Game-profile failure; field_scoped retry applied1 edit then rejected2 stale edits,0 refreshes and Root false. Controls with read_file_range or read_file recover (2 applied/1 rejected/1 refresh), while no-refresh control terminates. Timer resume gap remains.
- Evidence: [narrative](../reports/experiment18/experiment18-report.md); [numeric/protocol record](../reports/experiment18/experiment18-findings.json). Supporting files under reports/experiment18/ are inventoried individually in Section 10.
- Historical source limitation: no original commit tree or complete before-version is available here; exact addition/modification status of each older component is unverified. No experiment was rerun in this audit.

### 4.19 Experiment 18 comparability and unresolved defects

The Windows18A reported model digest a3d2b95350da03ff9b1943a753bb6617c49a3ee462b632a758518ec817743986 (8.0B/~9.61GB) differs from Colab dc35e8d9c6061baa6f0fa870975ab6932e2542b579b13ea0f199fa4bb7300c9c (7.5B/~6.58GB). Hardware alone cannot explain differences.

The earlier handoff identifies (a) unconstrained needed_evidence.kind schema versus a21-element runtime whitelist; (b) a mutation error instructing read_file_range while evidence_directed omitted that tool; (c) stale candidate spans after edit; and (d) a Timer verifier that accepts clearInterval without interval=null, missing Start -> Pause -> Start. These are historical diagnostic findings, not bugs fixed by the October19 literal-file correction. The Worker attempted no alternative read even though read_file remained available, so the missing tool is not proven to be the sole failure cause. The reported temporary180s canary timeout belongs to18A, not the October19 sessions, whose reports explicitly say they did not change timeout settings.

### 4.20 October 19 Experiment 12 preparation and pilot (G)

Source: audit_runs/20261019-phase2/PHASE2-REPORT.md; suite under experiment12-suite/.

Recorded preregistration command:

~~~powershell
.\.venv\Scripts\python.exe -B -X utf8 scripts/experiment12_run.py preregister --output-dir audit_runs/20261019-phase2/experiment12-suite
~~~

Exit0 created five fixture seeds/authorities and a30-trial manifest. production-integrity.json records matching nine pinned source files at that time. Preregistration is not trial success.

Recorded pilot command:

~~~powershell
.\.venv\Scripts\python.exe -B -X utf8 scripts/experiment12_run.py trial --output-dir audit_runs/20261019-phase2/experiment12-suite --case-id node_unique --policy current --repeat 1
~~~

Run20261019T054959-87298d45: harness exit0, saved status failed,120.22s measured execution excluding preflight,1 model call,0 Worker/tool calls, Root false, seed source/protected tests unchanged. Trace places timeout in MissionCompiler; first-blocker artifact instead labels CHILD_VERIFICATION/ENVIRONMENT_ERROR. The report preserves this discrepancy. No full batch followed. Missing Chromium blocked browser pilots. October19 pilot and original benchmark conditions are not demonstrated identical.

### 4.21 October 19 literal-file diagnostic cohort (G, separate from numbered experiments)

| Run/workspace | Recorded outcome | What it establishes |
|---|---|---|
| Original project-4 /20261019T061903-f5bb5918 | Failed before tool call | Missing context decision, candidate1/validated0/authorized0 |
| live-auto /20261019T063924-418790a4 | Interrupted; no output | Context/impact passed; three bare-name writes denied |
| live-auto-final /20261019T065255-5928c8e3 | Task failed despite process0 | Preflight passed; Specifier timeout120s,2 model calls,0 tools |
| live-baseline | Preflight blocked, exit2 | CRITICAL_MEMORY_HEADROOM,488017920 bytes/465.4MiB available below512MiB minimum |
| controlled-baseline-routed /20261019T070259-88ba0efc | Provider-free full controller replay passed | Real authorization/readback/Falsifier/aggregation/commit; scripted provider only |
| controlled-final /20261019T071642-a38faf6a | Final-source controlled replay passed | All four current production hashes pinned; Root true |

Final output: audit_runs/20261019-impact-fix/controlled-final/welcone.txt, seven bytes welcome, SHA-256280d44ab1e9f79b5cce2dd4f58f5fe91f0fbacdac9f7447dffc318ceb79f2d02. Final counters created1/validated1/authorized1/tool4/model0; seven scripted provider messages; source extracted/retained3 and REQ-001..003. This is not live-model completion. Earlier failed replay directories/logs remain evidence, not deleted setup noise.

## 5. Tests and verification actually recorded

All execution results in this section are historical. This task only reads source/reports/logs and hashes files; it does not run unittest, import mini.py, call a model, start a browser, execute a harness, run the project, install dependencies or create runtime workspaces.

### 5.1 Exact historical focused command families

The interpreter in test-results-final.json is the project's absolute .venv/Scripts/python.exe. The common invocation is:

~~~powershell
.\.venv\Scripts\python.exe -B -X utf8 -m unittest discover -s tests -p '<pattern>' -v
~~~

| Pattern | Historical result | Purpose/source |
|---|---|---|
| test_greenfield_impact_lifecycle.py | First batch exit0; later greenfield-routing-complete.log reports17 tests OK before final refinements | New lifecycle tests, real IO/gates/Falsifier |
| test_pre_mutation_impact.py |27 tests, exit0 | Deterministic impact contract guards |
| test_context_sufficiency_gate.py |9 tests, exit0 | Context permission/diagnosis |
| test_authority*.py |23 tests, exit0 on unrestricted run | Approved authority preservation |
| test_project_understanding.py |32 tests, exit0 | Source/Brain/project interpretation |
| test_experiment*.py |122 tests, exit0 | Existing experiment harness regressions |
| test_adaptive_architecture.py |90 tests, exit0 | Existing adaptive controller behavior |
| test_model_policy.py |4 tests, exit0 (Phase2) | Pinned model policy |

Exact command arrays, exit codes and times are reproduced without executing them in Appendix A. Overlapping suites are not additive unique coverage. Phase2 authority sandbox attempt produced23 permission errors; approved rerun passed23. The initial failure is not silently removed.

### 5.2 Broader regression comparison

Phase2 discovered1703, executed1361, recorded24 failures/18 errors/10 skips. Impact-fix broader comparison discovered1718, executed1376, recorded24 failure records/18 errors/10 skips. regression-comparison.json reports42 baseline/current failure headers, same_failure_identities=true, no new/resolved identities. Class setup errors prevented many discovered tests from running; subtest failure records are not necessarily distinct tests. Do not compute passes by simple subtraction.

Both exclude exactly:
test_requirement_clarification.RequirementClarificationTests.test_root_brain_prompt_compacts_large_source_side_channel_without_dropping_ids

The completed regression command was a custom Python selection using unittest.defaultTestLoader.discover('tests'), flattening and excluding that ID, then unittest.TextTestRunner(verbosity=2). No standalone exact shell command is retained in the summaries inspected, so none is invented. The initial ordinary discovery command in Appendix A was interrupted after unexpectedly reaching a live-model extraction call. README's broad claim that tests require no model has this documented exception.

The broader measured comparison preceded final verification-route integration; final broader/focused reruns after last refinements were blocked by automatic review capacity/deadline failures and were not executed. No claim of a fully green or freshly rerun final suite is supported.

### 5.3 Other historical checks and their limits

- native-proof-recheck.json:11 checks true, including actual retained native proof, current observed hash, generic-PASS/missing-field/foreign-hash/wrong-digest/contradictory-flag/wrong-target/wrong-tool rejection. Provider-free, not live model.
- raw-source-check.json: original request with additional duties cannot gain literal scope merely from an abbreviated interpreted goal.
- final-source-integrity.json: all four production hashes matched final controlled replay; six source/test files parsed historically. This audit does not rerun syntax parsing.
- Phase2 browser-runtime.json: actual Playwright launch failed because revision1248 Chromium/headless shell was missing; no browser installed.
- Phase2 isolated preflight:3/3 canaries PASS in26.945s; first overlapping preflight timed out and was confounded by another model test. These are distinct outcomes.
- normal-cli-startup.log: native preflight3/3 PASS, prompt reached, exit0 after exit input; startup only, no implementation request.

Recorded startup command:

~~~powershell
'exit' | .\.venv\Scripts\python.exe -u -B -X utf8 mini.py --no-bootstrap --workspace audit_runs/20261019-phase2/normal-cli-workspace
~~~

Recorded live correction command shape (workspace varied, actual saved request file retained):

~~~powershell
.\.venv\Scripts\python.exe -u -B -X utf8 mini.py --no-bootstrap --workspace <fresh-audit-workspace> --prompt-file audit_runs/20261019-impact-fix/live-request.txt
~~~

Direct baseline added --mode baseline. These placeholder commands describe the recorded family; they are not asserted to be an exact original shell string. The existing controlled_replay.py accepts an output directory argument and scripts seven provider messages. Its original invocation is not explicitly saved in the inspected summaries; execution is established by result/log/ledger artifacts, not a newly invented command.

## 6. Historical timeline

| Date/order evidence | Event | Confidence/qualification |
|---|---|---|
| Older linear sequence, commit dates unavailable locally | Experiments1–16 progress through planning, mutation, verification, receipts, compatibility and domain blockers | B; timeline commit strings only |
| docs checkpoint2026-10-03 | Status documents Experiment17 deterministic checkpoint, fresh runs pending | B; a dated document, not a live status source |
| Experiment18 findings date2026-10-11; run20261011T084608-0769014d | Windows/Colab diagnostics, stale-anchor trace, recovery controls, verifier replay and Timer coverage gap | B/G; no original Git tree |
|2026-10-19T05:49:59 run ID | Phase2 Node pilot timed out before Worker | G; UTC-formatted run identifier; not converted to local clock |
|2026-10-19T06:19:03 run ID | Original project-4 literal-file failure | G |
| Before first correction replay, exact edit times not recorded | Reproduction, ledger/scope/diagnosis/readback corrections | A; causal order reconstructed from report, no exact per-file edit timestamps |
|2026-10-19T06:39:24 run ID | First live diagnostic passes gates, bare-name writes denied | G |
| Following diagnostic, before routed final replay | Mandatory resolved-path handoff and candidate reuse; Stage5A literal route integration | A, relative order from recorded investigation |
|2026-10-19T06:52:55 run ID | Final auto live attempt times out at Specifier | G |
|2026-10-19T07:02:59 run ID | Routed provider-free controller replay passes | G |
|2026-10-19T07:16:42 run ID | Final-source provider-free replay passes | G |
| Same historical session, precise review timestamps absent | RAM block, proof/raw-source checks; final regressions blocked by review service | G/A; exact placement of all interleaved checks not certain |
| Later launch requests in chat | Attempts to open updated PowerShell session; latest recorded launch review failed at capacity | Conversation evidence only; no claim app stayed running |
|2026-10-21 | This documentation-only reconstruction | D; no experiment/test rerun |

Run IDs provide reliable labels and ordering among those runs. Filesystem write times were not treated as authorship/commit evidence because extraction/copying can change them. No exact author, edit duration or commit date is reconstructed.

## 7. Architecture and behavior impact

**Verified current code structure:** source request -> immutable requirement IDs -> Source/Task/Project Brain -> bounded local impact candidate -> context sufficiency decision -> deterministic impact validation/acceptance -> exact guarded mutation -> native literal readback -> required route aggregation -> captured post-state digest -> commit/root result. The final scripted replay records this path on one literal-file task. Existing-repository approved execution remains a separate authority path.

**Technical interpretation:** the fix closes authority/traceability/verification representation gaps at several interfaces rather than relaxing mutation permission. Path and content identity are source-bound across the transaction; the Worker prompt supplies guidance while controller checks enforce it. The corrected diagnostic distinguishes orchestration failure from a proven evidence deficit. These interpretations follow directly from the inspected call sequence, but they do not establish reliability across arbitrary requests/models.

**Not established:** a fully integrated production policy promotion; live task completion under latest source; reliable general new-project synthesis; resolved Timer resume assertions; browser readiness; full final regression success. Opt-in field_scoped/current policy choice from earlier experiments is not changed by the literal artifact route.

## 8. Remaining issues, provenance gaps and preservation rules

1. No .git or authentic full historical source snapshots: no exact staged/unstaged diff, author, patch size, deletion/rename chronology or local commit verification.
2. Original per-ID coverage payload absent; exact unmapped requirement unknown.
3. Most69 modules,38 harnesses and90 tests are older current files. Their names/version suffixes do not prove they were added by the immediately preceding work. Section9 records observable contents and limits attribution.
4. Full live-model completion and final post-refinement regression rerun remain unverified; model timeouts and memory gate are historical blockers, not current machine measurements.
5. Missing historical databases/plans/output fixtures caused many broad-suite failures. Examples in Phase2 report include D:/projects/Ai/mini_hivo/output/hivo-v22-stage5c-fresh-receipts-live-1/.hivo/memory.sqlite3, output/hivo-v24-4-5-stage6b-planning-live-1, output/gemma-only-rescue-recursive-v9-hard-prompt.txt and output/hivo-v25-6-stage6c-b-verification-closure-live-3. No substitute evidence is created.
6. Missing Chromium and the unexpected live-model test remain documented. Phase2 notes host_preflight substring classifier checks timeout but can miss timed out; no fix is claimed.
7. No independently verified deleted or renamed files. Absence of a path in this exported copy does not prove historical deletion.
8. .venv and cache contents are excluded from recursive hash preservation proof, because they are environment artifacts rather than source; this audit never runs the interpreter/application or writes them.
9. Archived reports disagree in checkpoint freshness: October3 status says17 pending, whereas later18 findings include additional diagnostics. They are dated evidence, not overwritten to appear synchronized.
10. No old artifacts, dependencies, model settings, experiment configuration or source are changed by this documentation task. No commit/push is performed.

## 9. Additional current-file audit and historical artifact catalogue

This section supplies a separate path-level subsection for existing source/harness/test files outside the six specifically attributable files, and for top-level historical session artifacts. **C entries are not assertions of modification.** For each C file the previous state/change type cannot be reconstructed; the symbols listed are current observable contents, and no exact old/new comparison or session-specific reason is supported. Experiment links in Section4 describe associations, not entire-file authorship.

### hivo/__init__.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Runtime architecture module. Dependencies are determined by current imports; historical import changes and original addition date are unavailable. Current opening description: """Core policies for the Mini Hivo coding orchestrator. The executable remains ``mini.py`` for backwards compatibility.  This package contains policy and state-free components that can be tested without Ollama or a browser. """

Current top-level symbols/line references: No top-level function/class declarations. Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### hivo/approval_authority.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Runtime architecture module. Dependencies are determined by current imports; historical import changes and original addition date are unavailable. Current opening description: """Stage 6C-A approval-bound execution authorization. This module owns the small, deterministic boundary between a validated ``PLAN_APPROVAL_REQUIRED`` result and an execution-eligible Stage 4 graph. It deliberately has no model, Worker, repository-mutation, or Project Brain write path.  The persisted Stage 6B replay helper belo

Current top-level symbols/line references: `89: class ApprovalAuthorityError(ValueError):`; `98: class ApprovalRequestError(ApprovalAuthorityError):`; `102: class ApprovalReceiptError(ApprovalAuthorityError):`; `106: class ExecutionAuthorizationError(ApprovalAuthorityError):`; `110: def canonical_hash(value: Any) -> str:`; `121: def _copy(value: Any) -> Any:`; `125: def _without(value: Any, *keys: str) -> dict[str, Any]:`; `132: def _text(value: Any) -> str:`; `136: def _as_list(value: Any) -> list[Any]:`; `144: def _sorted_strings(values: Iterable[Any]) -> list[str]:`; 64 further top-level declarations exist; listing is an index, not a claimed change list. Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### hivo/approval_bound_execution.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Runtime architecture module. Dependencies are determined by current imports; historical import changes and original addition date are unavailable. Current opening description: """Deterministic Stage 6C-B execution lifecycle glue. This module deliberately does not own a Worker loop, a verifier, or a memory promotion implementation.  It validates the immutable V25 authority proof, captures the execution subject, dispatches through the existing Worker entrypoint supplied by ``mini.py``, and hands evidenc

Current top-level symbols/line references: `67: def _copy(value: Any) -> Any:`; `71: def _text(value: Any) -> str:`; `75: def _path(value: Any) -> str:`; `82: def _unique(values: Iterable[Any]) -> list[str]:`; `95: def _without(value: dict[str, Any], *keys: str) -> dict[str, Any]:`; `99: def _root(workspace: str | os.PathLike | None) -> Path | None:`; `109: def _relative(root: Path, candidate: Path) -> str | None:`; `116: def _is_ignored(path: Path, root: Path) -> bool:`; `126: def _file_state(root: Path, relative: str) -> dict[str, Any]:`; `148: def enumerate_execution_subject(workspace: str | os.PathLike | None) -> dict[str, Any]:`; 24 further top-level declarations exist; listing is an index, not a claimed change list. Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### hivo/atomic_child_receipt.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Runtime architecture module. Dependencies are determined by current imports; historical import changes and original addition date are unavailable. Current opening description: """Experiment 8: bind a verified child handoff to its existing evidence."""

Current top-level symbols/line references: `18: def create_atomic_child_receipt(task, result, *, verification_aggregation=None,`; `73: def validate_atomic_child_receipt(receipt, *, workspace=None, expected_contract_hash=None,`; `154: def persist_atomic_child_receipt(receipt, workspace):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### hivo/browser_checks.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Runtime architecture module. Dependencies are determined by current imports; historical import changes and original addition date are unavailable. Current opening description: """Deterministic, profile-driven interactions for browser verification."""

Current top-level symbols/line references: `41: def _check(name: str, passed: bool, **evidence: Any) -> dict[str, Any]:`; `45: def _button(page, pattern: str):`; `50: def _clock(page) -> dict[str, Any] | None:`; `54: def _phase_text(page) -> str:`; `85: def _completed_count(text: str) -> int | None:`; `94: def _run_timer_checks(page, required: set[str]) -> list[dict[str, Any]]:`; `183: def _run_settings_persistence(page) -> dict[str, Any]:`; `213: def _run_duration_configuration(page) -> dict[str, Any]:`; `273: def _run_keyboard_activation(page) -> dict[str, Any]:`; `289: def _run_responsive_check(page) -> dict[str, Any]:`; 2 further top-level declarations exist; listing is an index, not a claimed change list. Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### hivo/change_impact.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Runtime architecture module. Dependencies are determined by current imports; historical import changes and original addition date are unavailable. Current opening description: """Bounded change-impact and change-island analysis for CORE-6 maintenance."""

Current top-level symbols/line references: `25: class ChangeImpact:`; `78: class ChangeIsland:`; `112: def _normalized_paths(values: Iterable[str]) -> tuple[str, ...]:`; `116: def _reverse_edges(repository_map: RepositoryMap) -> dict[str, set[str]]:`; `127: def analyze_change_impact(`; `222: def build_change_island(`; `249: def detect_contract_drift(`; `263: def detect_interface_drift(` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### hivo/child_handoff_diagnostics.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Runtime architecture module. Dependencies are determined by current imports; historical import changes and original addition date are unavailable. Current opening description: """Read-only Experiment 10 tracing. Decisions remain with existing gates."""

Current top-level symbols/line references: `9: def evidence_match_audit(artifact, evidence, browser_result):`; `27: def trace_handoff(snapshot, backend):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### hivo/context_sufficiency.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Runtime architecture module. Dependencies are determined by current imports; historical import changes and original addition date are unavailable. Current opening description: """Bounded worker context-sufficiency and evidence-completion gate. The Stage 4 worker packet remains the initial context.  This module adds only the small repair loop that lets a Worker identify a missing semantic fact and ask for that fact before it can mutate the workspace.  It is intentionally provider-agnostic: callers supp

Current top-level symbols/line references: `124: class ContextSufficiencyError(ValueError):`; `128: def _copy(value: Any) -> Any:`; `132: def _text(value: Any, limit: int) -> str:`; `138: def _list(value: Any) -> list[Any]:`; `146: def _unique(values: Iterable[Any], *, limit: int, text_limit: int) -> list[str]:`; `163: def _bounded_facts(value: Any) -> list[str]:`; `171: def _resolution_status(value: Any) -> str:`; `176: def _merge_resolution_status(current: Any, incoming: Any) -> str:`; `189: def _integer(value: Any, default: int = 0) -> int:`; `196: def canonical_hash(value: Any) -> str:`; 16 further top-level declarations exist; listing is an index, not a claimed change list. Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### hivo/context.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Runtime architecture module. Dependencies are determined by current imports; historical import changes and original addition date are unavailable. Current opening description: """Bounded conversation projection for local model calls.""" def _content_digest(content: str) -> str:

Current top-level symbols/line references: `8: def _content_digest(content: str) -> str:`; `12: def _compact_marker(content: str) -> str:`; `20: def projected_size(messages: list[dict]) -> int:`; `29: def _compact_argument_payload(value, threshold: int = 700):`; `42: def _compact_tool_arguments(message: dict) -> None:`; `63: def compact_messages(messages: list[dict], max_chars: int, keep_recent: int = 8) -> list[dict]:` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### hivo/core_execution.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Runtime architecture module. Dependencies are determined by current imports; historical import changes and original addition date are unavailable. Current opening description: """Provider-free execution state and budgets for the integrated Core pipeline. This module contains only integration bookkeeping.  It deliberately does not own approval, mutation, verification, Brain truth, or any Core algorithm. """

Current top-level symbols/line references: `93: def _plain(value: Any) -> Any:`; `109: def _freeze(value: Any) -> Any:`; `121: class CoreExecutionBudget:`; `191: class CoreExecutionState:`; `272: class CoreProviderRequest:`; `306: class CoreExecutionResult:`; `371: def new_core_metrics() -> dict[str, int]:`; `405: def core_autonomy_lift(*, naive_success: bool, integrated_success: bool, provider_requests: int = 0) -> dict[str, Any]:` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### hivo/core_orchestrator.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Runtime architecture module. Dependencies are determined by current imports; historical import changes and original addition date are unavailable. Current opening description: """Provider-free orchestration across HIVO CORE-1 through CORE-6. The coordinator is intentionally a composition layer.  It selects bounded Core components and records their evidence, but it never creates approval, widens authority, treats a candidate as verified, or calls a model directly. """

Current top-level symbols/line references: `81: def _generation_failure_category(error: Mapping[str, Any]) -> str:`; `101: def _map(value: Any) -> dict[str, Any]:`; `113: def _plain(value: Any) -> Any:`; `128: def _invoke(callback: Any, *args: Any, **kwargs: Any) -> Any:`; `154: def _bool_result(value: Any, *, default: bool = False) -> tuple[bool, dict[str, Any]]:`; `167: def _safe_root(value: str | Path) -> Path:`; `174: def _safe_relative(root: Path, value: str | Path) -> str:`; `186: def _clone_project(root: Path, destination: Path) -> None:`; `210: def _copy_changed_files(source_root: Path, target_root: Path, paths: Iterable[str]) -> tuple[str, ...]:`; `226: def classify_core_task(`; 6 further top-level declarations exist; listing is an index, not a claimed change list. Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### hivo/coverage_evidence.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Runtime architecture module. Dependencies are determined by current imports; historical import changes and original addition date are unavailable. Current opening description: """Optional, revision-bound coverage evidence for HIVO CORE-4. Coverage is deliberately an input adapter, not a test runner.  A provider may collect bounded coverage in a caller-owned sandbox, but CORE-4 never turns a coverage row into verification or mutation authority. """

Current top-level symbols/line references: `23: def _safe_path(value: Any) -> str | None:`; `33: def _string_tuple(values: Iterable[Any] = ()) -> tuple[str, ...]:`; `39: def _path_tuple(values: Iterable[Any] = ()) -> tuple[str, ...]:`; `46: class CoverageEvidence:`; `160: class CoverageEvidenceProvider(Protocol):`; `173: def collect_coverage_evidence(`; `232: def ochiai_suspiciousness(`; `249: def coverage_hit_counts(evidence: CoverageEvidence, key: str) -> tuple[int, int]:` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### hivo/decomposition_first.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Runtime architecture module. Dependencies are determined by current imports; historical import changes and original addition date are unavailable. Current opening description: """Small, authority-free responsibility split for Experiment 1. The split may assign existing requirement IDs to children. It cannot grant repository access or mutation scope; Stage 3 and approval do that later. """

Current top-level symbols/line references: `13: class EarlySplitError(ValueError):`; `24: def validate_split(candidate, requirements, max_children=4):`; `52: def local_contract(root_contract, child):`; `71: def local_task_brain(root_brain, child):`; `89: def combine_impact_maps(local_maps, root_goal, max_impacts=12):`; `164: def compact_attached_reuse(impact_map, id_maps):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### hivo/diagnostic_hypotheses.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Runtime architecture module. Dependencies are determined by current imports; historical import changes and original addition date are unavailable. Current opening description: """Deterministic diagnostic sessions and hypothesis evidence for CORE-3. The objects in this module are diagnostic projections.  They deliberately do not represent Project Brain truth, mutation authority, or verification. """

Current top-level symbols/line references: `65: class DiagnosticBudget:`; `107: def _reference(value: Any) -> TypedReference | None:`; `116: def _references(values: Iterable[Any]) -> tuple[TypedReference, ...]:`; `128: class DiagnosticFailureEvidence:`; `195: class DiagnosticHypothesis:`; `268: class DiagnosticSession:`; `328: def _candidate_reference(candidate: Any) -> TypedReference | None:`; `348: def _candidate_identity(candidate: Any) -> str:`; `354: def seed_hypotheses(`; `399: def _strength_delta(strength: str) -> int:`; 2 further top-level declarations exist; listing is an index, not a claimed change list. Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### hivo/evidence_compatibility.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Runtime architecture module. Dependencies are determined by current imports; historical import changes and original addition date are unavailable. Current opening description: """Experiment 11: controller evidence identity by obligation, subject and claim. Only executed structured browser observations can be normalized. Tool names are provenance; Worker prose and a page-load PASS cannot prove behavior. """

Current top-level symbols/line references: `16: def canonical_hash(value):`; `21: def target_identity(value):`; `28: def required_claims(requirements, *, contract_hash, child_id, target, subject_hash, subject_paths):`; `54: def _assertion(check):`; `65: def normalize_browser_result(payload, claims, *, tool, source, subject_before_hash, subject_after_hash):`; `102: def record_valid(record):`; `111: def compatible(claim, record):`; `123: def assess(claims, records, *, required_requirement_ids):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### hivo/evidence_monotonic.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Runtime architecture module. Dependencies are determined by current imports; historical import changes and original addition date are unavailable. Current opening description: """Experiment 13: optional semantic rescue, with independent receipt binding. Unknown metadata cannot defeat a successful legacy check. Explicit foreign identity is different: it cannot become authoritative proof via a legacy match. The focused-test aggregator is deliberately unchanged (Experiment 14). """

Current top-level symbols/line references: `17: def assess(claims, records, *, required_requirement_ids):`; `24: def fallback_assessments(legacy, assessments, browser_result):`; `43: def _payload(value):`; `53: def proof_bindings(routes, evidence, browser_result):`; `78: def _targets(value, workspace):`; `99: def binding_errors(bindings, requirements, *, workspace=None):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### hivo/evidence_strict.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Runtime architecture module. Dependencies are determined by current imports; historical import changes and original addition date are unavailable. Current opening description: """Experiment 14: exact suite binding or complete executed browser claims. An approved suite path identifies its obligation without invented semantic metadata. Generic test markers, path substrings and a page-load PASS do not. This module changes aggregation only; the independent receipt gate is intact. """

Current top-level symbols/line references: `15: def _path(value, workspace):`; `27: def target(value, tool, workspace=None):`; `47: def identity_errors(route, item, context, claims=()):`; `93: def matches(route, item, context):`; `100: def browser_assessments(artifact, evidence, browser, assessments, context):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### hivo/evidence.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Runtime architecture module. Dependencies are determined by current imports; historical import changes and original addition date are unavailable. Current opening description: """Deterministic interpretation of tool evidence.""" VERIFICATION_TOOLS = frozenset({"run_file", "run_command", "verify_web_app"}) MUTATION_TOOLS = frozenset({"write_file", "edit_file", "edit_file_range"})

Current top-level symbols/line references: `11: def result_not_applicable(result: object) -> bool:`; `15: def result_is_tool_rejection(result: object) -> bool:`; `27: def result_failed(result: object) -> bool:`; `55: def mutation_failure_record(tool: object, target: object, result: object, role: object = None) -> dict | None:`; `104: def latest_verification_evidence(evidence: list[dict]) -> list[dict]:`; `116: def unresolved_tool_failures(evidence: list[dict]) -> list[dict]:`; `131: def evidence_for_review(evidence: list[dict], limit: int = 8) -> list[dict]:` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### hivo/execution_contracts.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Runtime architecture module. Dependencies are determined by current imports; historical import changes and original addition date are unavailable. Current opening description: """Stage 4A approved-plan execution contracts. This module is deliberately deterministic.  Stage 3 owns the architectural decisions; this module only snapshots the approved result, compiles bounded worker responsibilities, validates their dependency graph, and projects one contract into a fresh model context.  It never reads the

Current top-level symbols/line references: `129: class ExecutionContractError(RuntimeError):`; `138: class ApprovedPlanSnapshotError(ExecutionContractError):`; `142: class ExecutionContractTooLargeError(ExecutionContractError):`; `146: class ExecutionGraphError(ExecutionContractError):`; `150: def _copy(value):`; `154: def _require_authority_list(value, limit, label):`; `167: def _require_authority_text(value, limit, label):`; `178: def _validate_plan_authority_bounds(plan, requirements, evidence, registry):`; `458: def _text(value, limit=MAX_TEXT_CHARS):`; `464: def _path(value):`; 101 further top-level declarations exist; listing is an index, not a claimed change list. Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### hivo/execution_invariants.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Runtime architecture module. Dependencies are determined by current imports; historical import changes and original addition date are unavailable. Current opening description: """Deterministic execution-time preservation invariants. This module is intentionally small and provider-free.  It turns already approved repository evidence into a bounded, immutable set of current interface facts.  The parser is conservative: unsupported or ambiguous JavaScript is an observation that cannot become Worker autho

Current top-level symbols/line references: `75: class ExecutionInvariantError(ValueError):`; `84: class _FrozenRecord(dict):`; `101: class ExecutionInvariantSet(_FrozenRecord):`; `105: class WorkerExecutionInvariantProjection(_FrozenRecord):`; `115: class PreCommitInvariantAudit(_FrozenRecord):`; `119: def canonical_hash(value: Any) -> str:`; `129: def _copy(value: Any) -> Any:`; `133: def _without(value: Any, *keys: str) -> dict[str, Any]:`; `140: def _text(value: Any, limit: int = MAX_TEXT) -> str:`; `144: def _path(value: Any) -> str:`; 67 further top-level declarations exist; listing is an index, not a claimed change list. Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### hivo/experiment_sandbox.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Runtime architecture module. Dependencies are determined by current imports; historical import changes and original addition date are unavailable. Current opening description: """Safe ephemeral sandboxes and anchored counterfactual probes for CORE-3."""

Current top-level symbols/line references: `35: class SandboxSecurityError(ValueError):`; `39: def _normalize_path(value: str | Path) -> str:`; `43: def _is_forbidden_relative(path: str) -> bool:`; `48: def _safe_subject_path(root: Path, value: str | Path) -> tuple[str, Path]:`; `63: def _authority_paths(authority: Mapping[str, Any] | None, keys: tuple[str, ...]) -> set[str]:`; `79: class ProbePermission:`; `102: def classify_probe_permission(`; `128: class CounterfactualMutationSpec:`; `187: class SyntaxValidation:`; `198: class SandboxMutationResult:`; 6 further top-level declarations exist; listing is an index, not a claimed change list. Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### hivo/experiment_selector.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Runtime architecture module. Dependencies are determined by current imports; historical import changes and original addition date are unavailable. Current opening description: """Deterministic experiment models and model-free selection for CORE-3."""

Current top-level symbols/line references: `42: def _refs(values: Iterable[Any]) -> tuple[TypedReference, ...]:`; `57: class DiagnosticExperiment:`; `137: class SelectionDecision:`; `156: def _cost_penalty(cost: str) -> int:`; `160: def _risk_penalty(risk: str) -> int:`; `164: class ExperimentSelector:` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### hivo/experimental_evidence.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Runtime architecture module. Dependencies are determined by current imports; historical import changes and original addition date are unavailable. Current opening description: """Provider-free experimental evidence engine for CORE-3. This module orchestrates bounded diagnostic probes.  It never commits, edits the canonical project, writes Project Brain, promotes a candidate, or claims formal root-cause proof. """

Current top-level symbols/line references: `76: def _as_outcome(value: Any) -> tuple[str, bool, dict[str, Any]]:`; `93: class VerificationResult:`; `131: class BaselineReceipt:`; `172: class ExperimentReceipt:`; `231: class EvidenceItem:`; `262: class ExperimentalEvidenceLedger:`; `285: class DiagnosticResult:`; `335: def new_core3_metrics() -> dict[str, int]:`; `353: def _metric(metrics: dict[str, int], key: str, amount: int = 1) -> None:`; `357: def _runner_result(`; 9 further top-level declarations exist; listing is an index, not a claimed change list. Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### hivo/fault_localization.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Runtime architecture module. Dependencies are determined by current imports; historical import changes and original addition date are unavailable. Current opening description: """Deterministic multi-signal fault localization for HIVO CORE-4. CORE-4 is a diagnostic projection.  It consumes current RepositoryMap and CORE-2 working-set evidence, optional coverage, Brain references, and the CORE-3 experimental ledger.  It never authorizes a mutation, promotes Brain truth, or replaces V25.5/V25.6 verificat

Current top-level symbols/line references: `122: def new_core4_metrics() -> dict[str, int]:`; `126: def _metric(metrics: dict[str, int], key: str, amount: int = 1) -> None:`; `130: def _string_tuple(values: Iterable[Any] = ()) -> tuple[str, ...]:`; `134: def _mapping(value: Any) -> dict[str, Any]:`; `146: def _safe_path(value: Any) -> str | None:`; `158: def _typed_reference(value: Any) -> TypedReference | None:`; `167: def _typed_references(values: Iterable[Any] = ()) -> tuple[TypedReference, ...]:`; `176: def _failure_type(value: Any) -> str:`; `182: class FaultFailureEvidence:`; `290: class LocalizationBudget:`; 46 further top-level declarations exist; listing is an index, not a claimed change list. Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### hivo/fault_ranking.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Runtime architecture module. Dependencies are determined by current imports; historical import changes and original addition date are unavailable. Current opening description: """CORE-4 ranking façade. The canonical implementation lives in :mod:`hivo.fault_localization`; this module keeps ranking-oriented imports discoverable without creating a second ranking model. """

Current top-level symbols/line references: No top-level function/class declarations. Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### hivo/generation_checkpoint.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Runtime architecture module. Dependencies are determined by current imports; historical import changes and original addition date are unavailable. Current opening description: """Deterministic resume checkpoints for verified CORE-6 generation work."""

Current top-level symbols/line references: `17: class GenerationCheckpoint:`; `94: def create_generation_checkpoint(`; `124: def validate_generation_checkpoint(`; `162: def resume_completed_units(` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### hivo/generation_dag.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Runtime architecture module. Dependencies are determined by current imports; historical import changes and original addition date are unavailable. Current opening description: """Deterministic module and GenerationUnit dependency DAG for CORE-6."""

Current top-level symbols/line references: `31: class DependencyEdge:`; `63: class DAGValidationResult:`; `89: class DependencyDAG:`; `179: def _as_units(units: Iterable[Any]) -> tuple[Any, ...]:`; `183: def _topological_order(nodes: Iterable[str], edges: Iterable[DependencyEdge]) -> tuple[str, ...]:`; `204: def _find_cycles(nodes: Iterable[str], edges: Iterable[DependencyEdge]) -> tuple[tuple[str, ...], ...]:`; `237: def validate_dependency_dag(dag: DependencyDAG) -> DAGValidationResult:`; `262: def build_dependency_dag(`; `355: def topological_sort_units(dag: DependencyDAG) -> tuple[str, ...]:`; `359: def ready_set(dag: DependencyDAG, completed: Iterable[str] = ()) -> tuple[str, ...]:` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### hivo/generation_units.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Runtime architecture module. Dependencies are determined by current imports; historical import changes and original addition date are unavailable. Current opening description: """Bounded generation units, evidence packets and candidate artifacts."""

Current top-level symbols/line references: `48: def _texts(values: Iterable[Any] | None, *, limit: int = 128) -> tuple[str, ...]:`; `61: def _maps(values: Iterable[Any] | None, *, limit: int = 128) -> tuple[dict[str, Any], ...]:`; `74: def _safe_paths(values: Iterable[Any] | None, *, limit: int = 128) -> tuple[str, ...]:`; `83: def _reject_body_keys(value: Any, *, depth: int = 0) -> None:`; `98: class GenerationUnit:`; `199: class GenerationEvidencePacket:`; `300: class GeneratedArtifactCandidate:`; `373: class ContractValidationResult:`; `403: class GenerationUnitReceipt:`; `429: class CodeGenerationProvider(Protocol):`; 1 further top-level declarations exist; listing is an index, not a claimed change list. Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### hivo/host_preflight.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Runtime architecture module. Dependencies are determined by current imports; historical import changes and original addition date are unavailable. Current opening description: """Lightweight host qualification for local HIVO runs. The preflight is deliberately separate from HIVO task execution.  It checks the local Ollama endpoint, performs a tiny repeated inference using the selected model, and persists enough state to identify a hard host restart on the next startup.  It does not import or call the 

Current top-level symbols/line references: `43: class HostPreflightProbeError(RuntimeError):`; `52: def _compact(value, limit=320):`; `57: def _timestamp():`; `61: def _is_local_ollama_url(url):`; `68: def _memory_snapshot():`; `119: def _number(value):`; `126: def _nvidia_gpu_snapshot():`; `162: def sample_resources():`; `169: def _safe_resource_snapshot(resource_sampler, phase, warnings):`; `199: def collect_host_inventory(model, workspace, before_snapshot):`; 18 further top-level declarations exist; listing is an index, not a claimed change list. Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### hivo/http_client.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Runtime architecture module. Dependencies are determined by current imports; historical import changes and original addition date are unavailable. Current opening description: """Small standard-library JSON HTTP client for the local Ollama API."""

Current top-level symbols/line references: `11: class HttpTransportError(OSError):`; `16: class JsonResponse:`; `24: def request_json(url: str, *, method: str, timeout: float, payload=None, headers=None) -> JsonResponse:`; `41: def get_json(url: str, *, timeout: float, headers=None) -> JsonResponse:`; `45: def post_json(url: str, *, timeout: float, payload, headers=None) -> JsonResponse:` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### hivo/impact_planning.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Runtime architecture module. Dependencies are determined by current imports; historical import changes and original addition date are unavailable. Current opening description: """Evidence-grounded impact planning for existing-project changes. Stage 3 sits between the temporary Task Brain and execution planning.  The module is deliberately model-agnostic: it defines bounded schemas, validates weak-model proposals against Stage 1/2 IDs, applies one deterministic reconciliation pass, and produces the imm

Current top-level symbols/line references: `275: def _compact_json(value):`; `280: def planning_role_limit(role):`; `289: def _role_item_id(item, index):`; `294: def _role_item_metadata(item, index):`; `312: def _role_payload_factory(mandatory_payload, selected_items):`; `377: def _role_packet_hash(material):`; `382: def build_planning_role_packet(`; `624: def _estimated_tokens(value):`; `630: def _list_value(value):`; `644: def _candidate_impact_items(candidate):`; 287 further top-level declarations exist; listing is an index, not a claimed change list. Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### hivo/integration_gate.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Runtime architecture module. Dependencies are determined by current imports; historical import changes and original addition date are unavailable. Current opening description: """Deterministic V21 verified-child integration gate. Stage 5B is deliberately separate from the model client, Worker transcripts, and the existing Stage 4 authority objects.  A child receipt is a derived evidence record, never a new authority record.  The readiness gate consumes only the validated child plan, terminal child sta

Current top-level symbols/line references: `73: def _without(value: dict[str, Any], key: str) -> dict[str, Any]:`; `77: def canonical_hash(value: Any) -> str:`; `88: def _compact(value: Any, limit: int = 700) -> str:`; `93: def _as_list(value: Any) -> list[Any]:`; `101: def _unique_strings(values: Iterable[Any], limit: int = 120) -> list[str]:`; `117: def _provenance_violation_counts(*sources: dict | None) -> dict[str, int]:`; `157: def _root_path(workspace: str | os.PathLike | None) -> Path | None:`; `167: def normalize_path(value: Any, workspace: str | os.PathLike | None = None) -> str:`; `187: def _file_record(root: Path | None, relative: str) -> dict[str, Any]:`; `202: def fingerprint_dependency_paths(`; 28 further top-level declarations exist; listing is an index, not a claimed change list. Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### hivo/integration_targets.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Runtime architecture module. Dependencies are determined by current imports; historical import changes and original addition date are unavailable. Current opening description: """Experiment 9: resolve parent execution locations without reusing child proof."""

Current top-level symbols/line references: `14: def _descriptor(workspace, value, *, explicit=False):`; `42: def _values(value):`; `55: def _choose(workspace, candidates):`; `72: def resolve_integration_targets(parent, contract, readiness, receipts, *, workspace, repository_snapshot=None):`; `137: def resolved_readiness(readiness, resolution):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### hivo/lexical_index.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Runtime architecture module. Dependencies are determined by current imports; historical import changes and original addition date are unavailable. Current opening description: """Deterministic incremental lexical retrieval for CORE-2. The index stores token postings and document metadata, never source bodies. It is deliberately independent of providers and can be rebuilt safely when its repository-map identity no longer matches the current subject. """

Current top-level symbols/line references: `27: def normalize_term(value: str) -> str:`; `31: def tokenize(value: str) -> tuple[str, ...]:`; `35: def _map_value(repository_map: RepositoryMap | Mapping[str, Any]) -> RepositoryMap:`; `39: def _document_metadata(repository_map: RepositoryMap, path: str) -> dict[str, Any]:`; `66: def _read_indexable_text(root: Path, path: str) -> str:`; `78: def _term_counts(repository_map: RepositoryMap, root: Path, path: str) -> Counter[str]:`; `85: class LexicalIndex:`; `219: def build_lexical_index(`; `242: def incremental_lexical_update(`; `286: def ensure_lexical_index(`; 1 further top-level declarations exist; listing is an index, not a claimed change list. Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### hivo/memory.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Runtime architecture module. Dependencies are determined by current imports; historical import changes and original addition date are unavailable. Current opening description: """Durable, bounded, disk-backed memory for the coding orchestrator. The database is an execution ledger, not an ever-growing prompt.  Callers ask for a small relevant projection and only verified notes or promoted facts are eligible for that projection by default. """

Current top-level symbols/line references: `31: def _now() -> str:`; `35: def _tokens(text: str) -> list[str]:`; `45: def _json(value: Any) -> str:`; `59: def _contains_promotion_private(value: Any) -> bool:`; `82: def _promotion_private_key(key: Any) -> bool:`; `96: class MemoryStore:` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### hivo/model_policy.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Runtime architecture module. Dependencies are determined by current imports; historical import changes and original addition date are unavailable. Current opening description: """Single-model policy. The experiment intentionally measures one installed model.  Model selection, role routing, and silent fallbacks would make the result impossible to attribute, so every model-backed role is pinned here. """

Current top-level symbols/line references: `15: class SingleModelPolicy:` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### hivo/mutation_grounding.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Runtime architecture module. Dependencies are determined by current imports; historical import changes and original addition date are unavailable. Current opening description: """Bind initial Worker mutations to source text observed in the current file."""

Current top-level symbols/line references: `17: def _hash(data: bytes) -> str:`; `21: def _source_text(data: bytes) -> str:`; `27: class SourceSpan:`; `37: class MutationGrounding:` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### hivo/mutation_strategy.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Runtime architecture module. Dependencies are determined by current imports; historical import changes and original addition date are unavailable. Current opening description: """Deterministic mutation-strategy routing for HIVO CORE-5. Routing is intentionally a small, explainable projection of CORE-4 evidence. It chooses *candidate-generation operators* only; it never authorizes a mutation, declares a diagnosis true, or replaces V25.5/V25.6. """

Current top-level symbols/line references: `37: def _mapping(value: Any) -> dict[str, Any]:`; `50: class StrategyDecision:`; `74: def _candidate_value(candidate: Any) -> dict[str, Any]:`; `78: def _failure_values(problem: Any) -> list[dict[str, Any]]:`; `85: class MutationStrategyRouter:`; `170: def route_mutation_strategies(problem: Any, candidate: Any, *, max_strategies: int = 4) -> StrategyDecision:` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### hivo/patch_candidates.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Runtime architecture module. Dependencies are determined by current imports; historical import changes and original addition date are unavailable. Current opening description: """Immutable patch representations and bounded deterministic candidate generation. The objects in this module are proposals for sandbox evaluation.  They are not writes, approvals, verification receipts, or Brain updates. """

Current top-level symbols/line references: `58: def _safe_path(path: Any) -> str:`; `68: def _text_hash(text: str) -> str:`; `72: def _map(value: Any) -> dict[str, Any]:`; `85: class PatchOperation:`; `163: class PatchRepresentation:`; `198: class PatchCandidate:`; `317: class PatchCandidateReceipt:`; `363: class CandidateFailureEvidence:`; `404: class ModelPatchCandidateProvider(Protocol):`; `410: def _read(root: Path, path: str) -> str:`; 7 further top-level declarations exist; listing is an index, not a claimed change list. Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### hivo/patch_search.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Runtime architecture module. Dependencies are determined by current imports; historical import changes and original addition date are unavailable. Current opening description: """Bounded, evidence-driven patch candidate search for HIVO CORE-5. Search operates exclusively in disposable sandboxes.  The only API that can write the canonical subject is :func:`apply_selected_patch_candidate`, an explicit caller action that rechecks all anchors and existing authority. """

Current top-level symbols/line references: `42: def _map(value: Any) -> dict[str, Any]:`; `54: def _bool_result(value: Any, *, default: bool = False) -> tuple[bool, dict[str, Any], str]:`; `72: def _invoke(callback: Any, *args: Any, **kwargs: Any) -> Any:`; `101: def _sha_bytes(value: bytes) -> str:`; `105: def _safe_target(root: Path, path: str) -> Path:`; `116: def _authority_label(problem: RepairProblem, path: str, candidate_label: str = "") -> tuple[str, str]:`; `141: def _candidate_authority_violations(problem: RepairProblem, candidate: PatchCandidate) -> tuple[str, ...]:`; `160: def _candidate_source_hash(problem: RepairProblem, root: Path) -> str:`; `165: def _apply_candidate_to_sandbox(candidate: PatchCandidate, sandbox_root: Path, canonical_root: Path) -> tuple[bool, dict[str, Any], list[str]]:`; `210: def _candidate_score_parts(candidate: PatchCandidate, decision: StrategyDecision, receipt: PatchCandidateReceipt) -> dict[str, float]:`; 8 further top-level declarations exist; listing is an index, not a claimed change list. Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### hivo/playbooks.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Runtime architecture module. Dependencies are determined by current imports; historical import changes and original addition date are unavailable. Current opening description: """Small deterministic project playbooks for low-capacity model execution."""

Current top-level symbols/line references: `50: def _contract_text(contract: dict[str, Any]) -> str:`; `58: def classify_project(contract: dict[str, Any]) -> str:`; `75: def playbook_context(contract: dict[str, Any]) -> str:`; `85: def _is_complex(contract: dict[str, Any], profile: str) -> bool:`; `94: def build_execution_stages(contract: dict[str, Any], max_stages: int = 6) -> list[dict[str, Any]]:`; `166: def compact_stage_plan(stages: list[dict[str, Any]], max_chars: int = 4000) -> str:` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### hivo/precommit_invariant_gate.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Runtime architecture module. Dependencies are determined by current imports; historical import changes and original addition date are unavailable. Current opening description: """Compatibility exports for deterministic pre-commit invariant enforcement."""     EXECUTION_INVARIANT_MUTATION_VIOLATION,     PRECOMMIT_ALLOWED,     PRECOMMIT_DNT_VIOLATION,     PRECOMMIT_SCHEMA_VERSION,     PreCommitExecutionInvariantGate,

Current top-level symbols/line references: No top-level function/class declarations. Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### hivo/project_blueprint.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Runtime architecture module. Dependencies are determined by current imports; historical import changes and original addition date are unavailable. Current opening description: """Contract-first project design primitives for HIVO CORE-6. The objects in this module describe a project before source is generated.  They are deliberately metadata-only: a blueprint can describe contracts, paths and invariants, but it can never contain source bodies or grant write authority. All identities are deterministic s

Current top-level symbols/line references: `27: def _texts(values: Iterable[Any] | None, *, limit: int = 256) -> tuple[str, ...]:`; `40: def _maps(values: Iterable[Any] | None, *, limit: int = 256) -> tuple[dict[str, Any], ...]:`; `53: def _safe_paths(values: Iterable[Any] | None, *, limit: int = 128) -> tuple[str, ...]:`; `62: def _reject_source_bodies(value: Any, *, depth: int = 0) -> None:`; `80: class ProjectRequirement:`; `145: class InterfaceSchema:`; `221: class ModuleContract:`; `328: class ProjectBlueprint:`; `464: def blueprint_identity(value: ProjectBlueprint | Mapping[str, Any]) -> str:`; `468: def contract_identity(value: ModuleContract | Mapping[str, Any]) -> str:`; 1 further top-level declarations exist; listing is an index, not a claimed change list. Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### hivo/project_brain_refs.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Runtime architecture module. Dependencies are determined by current imports; historical import changes and original addition date are unavailable. Current opening description: """Reference-based Project Brain entities for CORE-1. The pre-CORE Brain stores verified semantic facts.  This module adds a small, typed reference layer without turning that Brain into a source-code cache. Everything here is deterministic and deliberately independent of providers, workers, approval, and mutation code. """

Current top-level symbols/line references: `49: def new_core1_metrics() -> dict[str, int]:`; `54: def canonical_json(value: Any) -> str:`; `60: def canonical_hash(value: Any) -> str:`; `64: def _normalise_component(value: str, *, label: str) -> str:`; `73: def normalize_relative_path(value: str) -> str:`; `91: class TypedReference:`; `210: def _reject_source_duplication(value: Any, *, depth: int = 0) -> None:`; `227: class ProjectBrainEntity:`; `375: def validate_project_brain_entity(entity: ProjectBrainEntity | Mapping[str, Any]) -> dict[str, Any]:`; `395: def create_project_brain_entity(**kwargs: Any) -> ProjectBrainEntity:`; 3 further top-level declarations exist; listing is an index, not a claimed change list. Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### hivo/project_builder.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Runtime architecture module. Dependencies are determined by current imports; historical import changes and original addition date are unavailable. Current opening description: """Contract-first, bounded and incremental project generation for CORE-6. This module is intentionally provider-neutral.  A provider is an optional candidate source; it never receives the whole repository and never gains authority from producing a candidate.  The canonical repository is changed only by an explicit ``apply_verifi

Current top-level symbols/line references: `66: def _paths(value: Any) -> tuple[str, ...]:`; `74: def _authority_paths(authority: Mapping[str, Any] | None, keys: tuple[str, ...]) -> set[str]:`; `83: def _safe_target(root: Path, path: str) -> Path:`; `94: def _map(value: Any) -> dict[str, Any]:`; `104: class GenerationBudget:`; `152: class ProjectGenerationPlan:`; `224: class GenerationMetrics:`; `266: class GenerationResult:`; `309: class GenerationProvider(Protocol):`; `316: class DeterministicFakeProvider:`; 11 further top-level declarations exist; listing is an index, not a claimed change list. Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### hivo/project_understanding.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Runtime architecture module. Dependencies are determined by current imports; historical import changes and original addition date are unavailable. Current opening description: """Bounded project understanding and temporary Task Brain primitives. Stage 2 is intentionally deterministic-first.  This module may inventory, search, and read repository files, but it never mutates them and never calls a model.  The orchestration layer may optionally ask the pinned weak model to select candidate paths after de

Current top-level symbols/line references: `231: def _has_strong_persistence(value):`; `235: def _compact(value, limit=320):`; `241: def _json_size(value):`; `245: def _is_test_path(path):`; `253: def _file_kind(path):`; `267: def _inventory_fingerprint(files):`; `275: def inventory_repository(workspace, max_files=MAX_RECON_INVENTORY_FILES, max_depth=MAX_RECON_DEPTH):`; `345: def _snapshot_has_meaningful_files(snapshot):`; `357: def classify_project_mode(raw_goal, inventory=None):`; `381: def _search_term_variants(term):`; 48 further top-level declarations exist; listing is an index, not a claimed change list. Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### hivo/project_world_model.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Runtime architecture module. Dependencies are determined by current imports; historical import changes and original addition date are unavailable. Current opening description: """A bounded, provenance-backed semantic model for one HIVO project. The model is deliberately small.  It stores atomic repository facts and their source fingerprints; it does not store prompts, worker reasoning, or natural language project summaries.  The semantic evidence resolver is the authority for discovering facts.  This 

Current top-level symbols/line references: `122: def _clean(value: Any, limit: int = 300) -> str:`; `127: def _normalise_relation(value: Any) -> str:`; `132: def _normalise_state(value: Any) -> str:`; `137: def _source_identity_parts(value: Any) -> tuple[str, str]:`; `149: def _stable_project_identity(root: Path, project_id: Any = None) -> str:`; `156: def _fingerprint(path: Path) -> str | None:`; `178: def _fact_identifier(project_identity: str, subject: str, relation: str, object_value: str) -> str:`; `183: def _canonical_kind(value: Any) -> str:`; `212: class ProjectWorldFact:`; `242: class ProjectWorldModel:`; 1 further top-level declarations exist; listing is an index, not a claimed change list. Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### hivo/projects.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Runtime architecture module. Dependencies are determined by current imports; historical import changes and original addition date are unavailable. Current opening description: """Numbered project workspace management for the default ``list`` root."""

Current top-level symbols/line references: `13: class MigrationResult:`; `18: class ProjectStore:` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### hivo/promotion.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Runtime architecture module. Dependencies are determined by current imports; historical import changes and original addition date are unavailable. Current opening description: """Deterministic V22 Stage 5C verified-state promotion. This module is the boundary between execution evidence and durable project memory.  It deliberately consumes only the V21 parent receipt, the approved contract, and bounded integration evidence.  It never calls a model and it never stores a Worker transcript, planner advice

Current top-level symbols/line references: `116: class PromotionEligibilityError(ValueError):`; `125: def _without(value: dict[str, Any], key: str) -> dict[str, Any]:`; `129: def _compact(value: Any, limit: int = 700) -> str:`; `134: def _as_list(value: Any) -> list[Any]:`; `142: def _unique_strings(values: Iterable[Any], limit: int = 120, chars: int = 240) -> list[str]:`; `158: def _bounded_value(value: Any, limit: int = MAX_FACT_CHARS) -> Any:`; `172: def _private_key(key: Any) -> bool:`; `186: def contains_forbidden_transcript(value: Any) -> bool:`; `205: def _path_from_value(value: Any) -> list[str]:`; `220: def _subject_paths(receipt: dict) -> list[str]:`; 29 further top-level declarations exist; listing is an index, not a claimed change list. Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### hivo/recovery.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Runtime architecture module. Dependencies are determined by current imports; historical import changes and original addition date are unavailable. Current opening description: """Provider-free V26 autonomous-recovery foundations. This module is deliberately a narrow authority boundary.  It converts deterministic execution evidence into a bounded recovery decision and a fresh, clean mission.  It does not call a model, mutate the user's workspace, create approval, or implement a production-code fix. The

Current top-level symbols/line references: `240: class _FrozenRecord(dict):`; `257: class RecoveryFailureEnvelope(_FrozenRecord):`; `261: class RecoveryFailureEvidence(_FrozenRecord):`; `265: class VerificationFailureEvidence(RecoveryFailureEvidence):`; `269: class WorkerExecutionFailureEvidence(RecoveryFailureEvidence):`; `273: class RecoveryAuthorityDelta(_FrozenRecord):`; `277: class AuthorizedExecutionLineage(_FrozenRecord):`; `281: class ApprovedRecoveryAuthorization(_FrozenRecord):`; `285: class RecoveryMission(_FrozenRecord):`; `289: class RecoveryWorkerPacket(_FrozenRecord):`; 166 further top-level declarations exist; listing is an index, not a claimed change list. Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### hivo/reentry.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Runtime architecture module. Dependencies are determined by current imports; historical import changes and original addition date are unavailable. Current opening description: """V23 Stage 6A freshness-aware verified-state re-entry. This module is deliberately a read-only boundary between the V22 verified Project Brain and a new task.  It does not plan, execute, re-verify, promote, or call a model.  The Project Brain remains the durable source of previously verified state; the ReentryContext is a dete

Current top-level symbols/line references: `145: def _zero_model_call_accounting() -> dict[str, int]:`; `149: def _without(value: dict[str, Any], key: str) -> dict[str, Any]:`; `153: def _compact(value: Any, limit: int = 700) -> str:`; `158: def _json_size(value: Any) -> int:`; `162: def _tokens(value: Any) -> list[str]:`; `173: def _as_list(value: Any) -> list[Any]:`; `181: def _unique_strings(values: Iterable[Any], limit: int = 48, chars: int = 260) -> list[str]:`; `197: def _safe_value(value: Any, *, depth: int = 0, limit: int = 900) -> Any:`; `215: def _normalize_paths(values: Any, workspace: str | Path | None = None) -> list[str]:`; `233: def _normalize_authority(value: Any) -> str:`; 57 further top-level declarations exist; listing is an index, not a claimed change list. Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### hivo/reference_resolution.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Runtime architecture module. Dependencies are determined by current imports; historical import changes and original addition date are unavailable. Current opening description: """Lazy, progressive resolution of CORE-1 Project Brain references."""

Current top-level symbols/line references: `33: class EvidenceResolutionRequest:`; `62: class ResolvedEvidence:`; `102: def _file_metadata(entry: Mapping[str, Any]) -> dict[str, Any]:`; `113: class ProjectReferenceResolver:`; `404: def resolve_project_reference(`; `420: def request_project_evidence(` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### hivo/repair_problem.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Runtime architecture module. Dependencies are determined by current imports; historical import changes and original addition date are unavailable. Current opening description: """Immutable CORE-5 repair inputs and bounded search budgets. CORE-5 is deliberately a diagnostic/repair-candidate projection.  These records bind current evidence and authority, but they never become approval, verification, Brain truth, or a canonical mutation by themselves. """

Current top-level symbols/line references: `28: class PatchSearchBudget:`; `104: def _as_reference(value: Any) -> TypedReference | None:`; `111: def _references(values: Iterable[Any]) -> tuple[TypedReference, ...]:`; `120: def _candidate_record(candidate: FaultCandidate) -> dict[str, Any]:`; `125: class RepairTargetSet:`; `157: class RepairEvidencePacket:`; `207: class RepairProblem:` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### hivo/repo_intelligence.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Runtime architecture module. Dependencies are determined by current imports; historical import changes and original addition date are unavailable. Current opening description: """Deterministic hybrid repository intelligence for CORE-2. CORE-2 is a retrieval and context-construction layer.  It combines the verified reference Brain and mechanically-derived CORE-1 RepositoryMap with exact, lexical, graph, test, and optional semantic evidence.  Retrieval confidence never becomes mutation or verification a

Current top-level symbols/line references: `76: def new_core2_metrics() -> dict[str, int]:`; `92: def _unique(values: Iterable[Any], *, limit: int = 128) -> tuple[str, ...]:`; `105: def _normalise_path_signal(value: str) -> str:`; `109: def extract_query_signals(raw_task_text: str) -> dict[str, tuple[str, ...]]:`; `164: def classify_search_intents(raw_task_text: str, signals: Mapping[str, Iterable[str]] | None = None) -> tuple[str, ...]:`; `192: class RepoIntelligenceQuery:`; `290: class SearchCandidate:`; `328: class RepoIntelligenceResult:`; `365: class SemanticRetriever(Protocol):`; `375: def _map_value(repository_map: RepositoryMap | Mapping[str, Any]) -> RepositoryMap:`; 12 further top-level declarations exist; listing is an index, not a claimed change list. Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### hivo/repository_map.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Runtime architecture module. Dependencies are determined by current imports; historical import changes and original addition date are unavailable. Current opening description: """Deterministic, metadata-only repository navigation for CORE-1. The map is intentionally a compact index.  It stores paths, hashes, symbol locations/signatures, and structural edges; it never stores source bodies. The parser is deliberately modest and currently gives JavaScript first-class support because that is the project's

Current top-level symbols/line references: `37: def _metric(metrics: dict[str, int] | None, key: str, value: int = 1) -> None:`; `42: def _safe_root(root: str | Path) -> Path:`; `49: def _safe_relative(root: Path, path: str | Path) -> str:`; `59: def _safe_existing_file(root: Path, relative: str) -> Path | None:`; `68: def _language_for(path: str) -> str:`; `79: def _is_test_path(path: str) -> bool:`; `90: def _read_text(path: Path) -> str:`; `94: def _content_hash(path: Path) -> tuple[str, int]:`; `99: def _package_identity(root: Path, relative: str) -> str:`; `108: def _line_number(text: str, position: int) -> int:`; 18 further top-level declarations exist; listing is an index, not a claimed change list. Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### hivo/semantic_coupling.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Runtime architecture module. Dependencies are determined by current imports; historical import changes and original addition date are unavailable. Current opening description: """Bounded semantic validation for candidate task decompositions. The existing decomposer remains responsible for proposing child missions.  This module is the small deterministic refinement layer which decides whether those missions are independently verifiable or must travel as one semantic work group.  It consumes typed, prov

Current top-level symbols/line references: `155: def _text(value: Any, limit: int) -> str:`; `160: def _unique(values: Iterable[Any], *, limit: int, item_limit: int = 220) -> list[str]:`; `175: def _tokens(value: Any) -> list[str]:`; `188: def _alias_forms(value: Any) -> set[str]:`; `207: def _matches(value: Any, aliases: set[str]) -> bool:`; `213: def _normalise_relation(value: Any) -> str:`; `217: def _normalise_state(value: Any) -> str:`; `221: def _fact_dict(value: Any) -> dict[str, Any] | None:`; `234: def _fact_key(fact: Mapping[str, Any]) -> tuple[str, ...]:`; `244: def _fact_authority(fact: Mapping[str, Any]) -> int:`; 26 further top-level declarations exist; listing is an index, not a claimed change list. Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### hivo/semantic_evidence.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Runtime architecture module. Dependencies are determined by current imports; historical import changes and original addition date are unavailable. Current opening description: """Bounded semantic evidence completion for targeted Worker requests. This module sits behind the existing ContextSufficiencyGate provider seam. It does not create a repository memory or a second orchestration loop.  The gate still owns the completion budget and mutation authorization; this module only turns one narrow request i

Current top-level symbols/line references: `139: def _normalise(value: Any) -> str:`; `143: def canonical_request_kind(value: Any) -> str:`; `152: def gate_request_kind(value: Any) -> str:`; `158: def _text(value: Any, limit: int) -> str:`; `163: def _unique(values: Iterable[Any], limit: int = 16) -> list[str]:`; `177: def _is_test_path(path: str) -> bool:`; `189: def _is_comment(line: str) -> bool:`; `194: def _identifier_tokens(target: str) -> list[str]:`; `208: def _primary_symbol(target: str, kind: str) -> str:`; `224: class SemanticEvidenceResolver:`; 1 further top-level declarations exist; listing is an index, not a claimed change list. Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### hivo/target_locator.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Runtime architecture module. Dependencies are determined by current imports; historical import changes and original addition date are unavailable. Current opening description: """Deterministic lexical navigation within approved inspection paths."""

Current top-level symbols/line references: `26: def _terms(text):`; `38: def _query_terms(task_text, contract):`; `53: def _present(term, lower):`; `57: def _section_weights(path, lines):`; `77: class TargetLocator:` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### hivo/task_working_set.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Runtime architecture module. Dependencies are determined by current imports; historical import changes and original addition date are unavailable. Current opening description: """Bounded, progressive task context for CORE-2. The working set is a transient retrieval projection.  It is not Brain truth, not verification evidence, and not an authorization object. """

Current top-level symbols/line references: `31: class WorkingSetBudget:`; `81: class WorkingSetItem:`; `126: class TaskWorkingSet:`; `172: def _authority_paths(authority: Mapping[str, Any] | None, keys: tuple[str, ...]) -> set[str]:`; `187: def authority_label_for_path(path: str, authority: Mapping[str, Any] | None = None) -> str:`; `199: def _candidate_dict(candidate: Any) -> dict[str, Any]:`; `208: def _role_for_candidate(candidate: Mapping[str, Any], *, primary_count: int, budget: WorkingSetBudget) -> str | None:`; `223: def build_task_working_set(`; `362: def _reference_for_item(item: WorkingSetItem) -> TypedReference | None:`; `371: def expand_working_set(` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### hivo/verification_environment.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Runtime architecture module. Dependencies are determined by current imports; historical import changes and original addition date are unavailable. Current opening description: """Deterministic verifier preflight and failure attribution for Experiment 6."""

Current top-level symbols/line references: `16: def preflight_command(parts, workspace, *, platform=None, which=None):`; `53: def command_result(result, *, launch_error=None):`; `60: def _preexisting_bridge_missing(transaction, workspace, path):`; `70: def classify_observation(item, *, transaction=None, workspace=None):`; `100: def classify_browser_result(result, *, transaction=None, workspace=None):`; `124: def classify_failed_gate(gate, builder, falsifier, browser, *, transaction=None, workspace=None):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### hivo/verification_gap_remediation.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Runtime architecture module. Dependencies are determined by current imports; historical import changes and original addition date are unavailable. Current opening description: """Deterministic V25.4 remediation for an uncovered behavior obligation. The objects in this module are planning and verification authority, not execution authority.  A caller must provide the proposed observable and the direct oracle explicitly; this module never invents an API, a test, or a provider action.  The direct oracle 

Current top-level symbols/line references: `57: class VerificationGapRemediationError(ValueError):`; `66: class _FrozenRecord(dict):`; `83: class BehaviorObservableContract(_FrozenRecord):`; `87: class DirectBehaviorOracleSpec(_FrozenRecord):`; `91: class VerificationGapRemediationProposal(_FrozenRecord):`; `95: class RevisedPlanApprovalSummary(_FrozenRecord):`; `99: def canonical_hash(value: Any) -> str:`; `109: def _copy(value: Any) -> Any:`; `113: def _without(value: Any, *keys: str) -> dict[str, Any]:`; `120: def _freeze_record(record_type: type[_FrozenRecord], value: dict[str, Any]) -> _FrozenRecord:`; 44 further top-level declarations exist; listing is an index, not a claimed change list. Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### hivo/verification_obligation_coverage.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Runtime architecture module. Dependencies are determined by current imports; historical import changes and original addition date are unavailable. Current opening description: """Deterministic verification-obligation coverage for V25.3. This module owns the small piece of authority that was missing between the approved verification contracts and Stage 5.  It answers a deliberately narrow question: which exact atomic obligation does an already-approved verification oracle independently establish? It ne

Current top-level symbols/line references: `113: class VerificationObligationCoverageError(ValueError):`; `122: class _FrozenRecord(dict):`; `139: class VerificationObligationCoverage(_FrozenRecord):`; `143: def canonical_hash(value: Any) -> str:`; `153: def _copy(value: Any) -> Any:`; `157: def _without(value: Any, *keys: str) -> dict[str, Any]:`; `164: def _text(value: Any, limit: int = MAX_TEXT) -> str:`; `169: def _path(value: Any) -> str:`; `176: def _unique(values: Iterable[Any], limit: int | None = None) -> list[str]:`; `190: def _as_list(value: Any) -> list[Any]:`; 35 further top-level declarations exist; listing is an index, not a claimed change list. Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### hivo/verification_surfaces.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Runtime architecture module. Dependencies are determined by current imports; historical import changes and original addition date are unavailable. Current opening description: """Discover existing browser observables and exercise a game through real input. No source file, application global, or persistent test bridge is created here. """

Current top-level symbols/line references: `14: def requested_key(requirement):`; `22: def discover_game_surface(page):`; `71: def _invoke(page, name, method):`; `75: def _state(page, name):`; `79: def _status(state):`; `83: def _position_changed(before, after):`; `90: def _check(name, passed, **evidence):`; `94: def _dom_game_state(page):`; `118: def _dom_key_route(page, profile, requirement, surface):`; `189: def run_game_checks(page, profile, requirement):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### hivo/verification.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Runtime architecture module. Dependencies are determined by current imports; historical import changes and original addition date are unavailable. Current opening description: """Contract-aware browser verification policies.""" GAME_BRIDGE_NAME = "AGENT_GAME"

Current top-level symbols/line references: `13: class WebVerificationProfile:`; `41: def interaction_expectations(profile: WebVerificationProfile) -> tuple[str, ...]:`; `50: def _profile_semantic_text(task_text: str, contract: dict | None) -> str:`; `67: def infer_web_profile(task_text: str, contract: dict | None = None,`; `128: def _looks_like_source_dump(text: str) -> bool:`; `141: def evaluate_web_snapshot(snapshot: dict, profile: WebVerificationProfile) -> dict:` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### hivo/verified_planning.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Runtime architecture module. Dependencies are determined by current imports; historical import changes and original addition date are unavailable. Current opening description: """V24 Stage 6B verified-state-aware planning boundary. This module is deliberately a deterministic adapter between the V23 ``FreshTaskBrain`` and the existing Stage 3 planning implementation.  It does not create authority, refresh verification, write the Project Brain, or introduce another model role.  The returned planning con

Current top-level symbols/line references: `103: def _without(value: dict[str, Any], key: str) -> dict[str, Any]:`; `107: def _json_size(value: Any) -> int:`; `111: def _compact(value: Any, limit: int = 700) -> str:`; `117: def _list(value: Any) -> list[Any]:`; `125: def _unique_strings(values: Iterable[Any], limit: int = 24, chars: int = 260) -> list[str]:`; `136: def _safe(value: Any, *, depth: int = 0, limit: int = 900) -> Any:`; `156: def _contains_private(value: Any) -> bool:`; `167: def _fact_dict(item: dict) -> dict:`; `172: def _fact_text(item: dict) -> str:`; `183: def _structured_relation_names(item: Any) -> list[str]:`; 36 further top-level declarations exist; listing is an index, not a claimed change list. Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### hivo/worker_progress.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Runtime architecture module. Dependencies are determined by current imports; historical import changes and original addition date are unavailable. Current opening description: """Deterministic progress accounting for one approved initial Worker attempt."""

Current top-level symbols/line references: `14: def _fingerprint(value):`; `19: class WorkerProgress:` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### scripts/experiment1_report.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Experiment execution/probe/report tooling. Harness existence proves implementation availability, not trial execution. See matching numbered experiment in Section4. Current opening description: """Summarize paired Experiment 1 runs from subject workspace metrics files."""

Current top-level symbols/line references: `22: def event(run, kind):`; `27: def summarize_run(run):`; `68: def load_runs(paths):`; `83: def rate(count, total):`; `88: def report(runs):`; `156: def format_markdown(result):`; `209: def main():` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### scripts/experiment10_capture.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Experiment execution/probe/report tooling. Harness existence proves implementation availability, not trial execution. See matching numbered experiment in Section4. Current opening description: """Observe the approved runner and save its actual pre-browser handoff."""

Current top-level symbols/line references: `25: def capture(task, tool_contract, builder, falsifier):`; `49: def main():` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### scripts/experiment10_handoff_probe.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Experiment execution/probe/report tooling. Harness existence proves implementation availability, not trial execution. See matching numbered experiment in Section4. Current opening description: """Replay one frozen post-child projection through unchanged verification gates."""

Current top-level symbols/line references: `26: def read_run(path):`; `30: def events_for(path):`; `35: def historical_audit(path, child_id):`; `48: def historical_projection(path, child_id):`; `89: def materialize(path, saved, child_id, workspace):`; `115: def replay(saved, snapshot, workspace):`; `150: def main():` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### scripts/experiment10_report.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Experiment execution/probe/report tooling. Harness existence proves implementation availability, not trial execution. See matching numbered experiment in Section4. Current opening description: """Summarize stability at each unchanged child verification boundary.""" def rate(count, total):

Current top-level symbols/line references: `8: def rate(count, total):`; `12: def main():` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### scripts/experiment11_evidence_probe.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Experiment execution/probe/report tooling. Harness existence proves implementation availability, not trial execution. See matching numbered experiment in Section4. Current opening description: """Compare a frozen failed aggregation, then resume the real child receipt seam. The original archive has compact tool results. A missing accepted Impact Contract can be recovered from a complete capture only when its content hash matches the original authorization event, execution contract and context anchor. No Worker, Falsifi

Current top-level symbols/line references: `23: def digest(content):`; `27: def recover_input(run_file, capture_file, child_id):`; `70: def resume_receipt(saved, snapshot, result):`; `89: def main():` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### scripts/experiment11_report.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Experiment execution/probe/report tooling. Harness existence proves implementation availability, not trial execution. See matching numbered experiment in Section4. Current opening description: """Report frozen compatibility results and every fresh trial with denominators.""" sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

Current top-level symbols/line references: `12: def read(path):`; `16: def rate(numerator, denominator):`; `21: def show(value):`; `25: def summarize(path):`; `72: def main():` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### scripts/experiment12_evidence_matrix.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Experiment execution/probe/report tooling. Harness existence proves implementation availability, not trial execution. See matching numbered experiment in Section4. Current opening description: """Actual reference verification payloads plus declared incompatible evidence. This protocol matrix is separate from fresh model runs. Altered records are adversarial replay inputs, never Worker evidence or new application authority. """

Current top-level symbols/line references: `24: def reference_source(case):`; `38: def browser_records(payload,claims,subject,tool="verify_web_app"):`; `43: def evaluate(case,workspace,contract,artifact,raw,browser,records,policy,claims):`; `61: def scenario_inputs(case,contract,payload,raw,claims,subject,other_behavior=None,other_target=None):`; `101: def main():` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### scripts/experiment12_fixtures.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Experiment execution/probe/report tooling. Harness existence proves implementation availability, not trial execution. See matching numbered experiment in Section4. Current opening description: """Public, disposable regression tasks; no solutions enter Worker workspaces.""" ARENA = '''<!doctype html> <html><head><title>Grid Arena</title></head><body> <canvas width="320" height="200"></canvas><p id="state" aria-live="polite"></p> <button data-move="up">Up</button><button id="restart">Restart</button> <script> let state;

Current top-level symbols/line references: `57: class ClampBehavior(unittest.TestCase):`; `108: def get_case(case_id):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### scripts/experiment12_handoff_probe.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Experiment execution/probe/report tooling. Harness existence proves implementation availability, not trial execution. See matching numbered experiment in Section4. Current opening description: """Paired, fresh verification of actual captured child handoffs; zero model calls."""

Current top-level symbols/line references: `17: def save(path,data):`; `21: def replay(snapshot,workspace,policy):`; `70: def main():` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### scripts/experiment12_report.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Experiment execution/probe/report tooling. Harness existence proves implementation availability, not trial execution. See matching numbered experiment in Section4. Current opening description: """Audit Experiment 12 denominators without treating page load as behavior PASS."""

Current top-level symbols/line references: `15: def load(path):`; `19: def rate(numerator, denominator):`; `24: def browser_pass(case, payload):`; `63: def unit_pass(case, evidence):`; `79: def gate_passes(case, observation):`; `93: def audit_trial(suite, case, policy, repeat, *, expected_semantic_policy=None, expected_policies=None):`; `174: def summarize(trials):`; `201: def matrix_summary(data):`; `214: def compact_paired(data, source):`; `235: def pct(r):`; 2 further top-level declarations exist; listing is an index, not a claimed change list. Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### scripts/experiment12_run.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Experiment execution/probe/report tooling. Harness existence proves implementation availability, not trial execution. See matching numbered experiment in Section4. Current opening description: """Frozen approved fixture -> fresh production Worker/verification/parent runs. The public benchmark authorizes only declared source paths in disposable workspaces. Every plan passes the existing Stage 3 validator, snapshot and Stage 4 graph compiler. No production gate, prompt, result or tool is replaced. Planning is a fixed in

Current top-level symbols/line references: `33: def sha(data):`; `37: def save(path, value):`; `41: def materialize(case, workspace):`; `50: def authority(case, workspace):`; `110: def preregister(directory):`; `135: def check_pin(manifest):`; `143: def execute_trial(directory, case_id, policy, repeat):`; `226: def batch(directory):`; `247: def main():` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### scripts/experiment13_evidence_probe.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Experiment execution/probe/report tooling. Harness existence proves implementation availability, not trial execution. See matching numbered experiment in Section4. Current opening description: """Fresh native proofs and explicit negative identity replays, three policies.""" sys.path.insert(0,str(Path(__file__).resolve().parents[1]))

Current top-level symbols/line references: `20: def evaluate(case, workspace, contract, artifact, raw, browser, records, policy, claims):`; `40: def main():` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### scripts/experiment13_handoff_probe.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Experiment execution/probe/report tooling. Harness existence proves implementation availability, not trial execution. See matching numbered experiment in Section4. Current opening description: """Re-evaluate every eligible current handoff from Exp12, without PASS filtering.""" sys.path.insert(0,str(Path(__file__).resolve().parents[1]))

Current top-level symbols/line references: `15: def main():` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### scripts/experiment13_report.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Experiment execution/probe/report tooling. Harness existence proves implementation availability, not trial execution. See matching numbered experiment in Section4. Current opening description: """Report fresh runs, exact-state preservation and final identity negatives.""" sys.path.insert(0,str(Path(__file__).resolve().parents[1]))

Current top-level symbols/line references: `13: def main():` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### scripts/experiment13_run.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Experiment execution/probe/report tooling. Harness existence proves implementation availability, not trial execution. See matching numbered experiment in Section4. Current opening description: """Experiment 13: same three eligible tasks, frozen contracts, 18 fresh runs."""

Current top-level symbols/line references: `20: def preregister(directory, baseline):`; `49: def main():` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### scripts/experiment14_evidence_probe.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Experiment execution/probe/report tooling. Harness existence proves implementation availability, not trial execution. See matching numbered experiment in Section4. Current opening description: """Fresh native proofs and explicit negative identity replays, three policies.""" sys.path.insert(0,str(Path(__file__).resolve().parents[1]))

Current top-level symbols/line references: `20: def evaluate(case, workspace, contract, artifact, raw, browser, records, policy, claims):`; `41: def main():` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### scripts/experiment14_handoff_probe.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Experiment execution/probe/report tooling. Harness existence proves implementation availability, not trial execution. See matching numbered experiment in Section4. Current opening description: """Re-evaluate every eligible monotonic handoff from Exp13, without PASS filtering.""" sys.path.insert(0,str(Path(__file__).resolve().parents[1]))

Current top-level symbols/line references: `15: def main():` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### scripts/experiment14_report.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Experiment execution/probe/report tooling. Harness existence proves implementation availability, not trial execution. See matching numbered experiment in Section4. Current opening description: """Audit strict aggregation separately from the unchanged final receipt gate.""" sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

Current top-level symbols/line references: `13: def main():` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### scripts/experiment14_run.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Experiment execution/probe/report tooling. Harness existence proves implementation availability, not trial execution. See matching numbered experiment in Section4. Current opening description: """Experiment 14: same three eligible tasks, frozen contracts, 18 fresh runs."""

Current top-level symbols/line references: `20: def preregister(directory, baseline):`; `50: def main():` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### scripts/experiment15_binding_probe.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Experiment execution/probe/report tooling. Harness existence proves implementation availability, not trial execution. See matching numbered experiment in Section4. Current opening description: """Declared grounding challenges, real file tools and fresh native verification. These are deterministic protocol inputs, not new Worker or Root successes. The historical failing call arguments were not saved; no exact replay is claimed. """

Current top-level symbols/line references: `33: def historic(path):`; `43: def evaluate(case,workspace,scenario,policy,approved):`; `117: def main():` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### scripts/experiment15_report.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Experiment execution/probe/report tooling. Harness existence proves implementation availability, not trial execution. See matching numbered experiment in Section4. Current opening description: """Separate declared grounding challenge results from unforced fresh Workers."""

Current top-level symbols/line references: `16: def true_region(case,text):`; `27: def region_changed(case,item):`; `39: def audit(suite,case,policy,repeat):`; `79: def fresh_summary(rows):`; `95: def main():` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### scripts/experiment15_run.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Experiment execution/probe/report tooling. Harness existence proves implementation availability, not trial execution. See matching numbered experiment in Section4. Current opening description: """Experiment 15: same three eligible tasks, frozen contracts, 18 fresh runs."""

Current top-level symbols/line references: `22: def preregister(directory, baseline):`; `65: def execute_trial(directory, case_id, policy, repeat):`; `167: def main():` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### scripts/experiment16_report.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Experiment execution/probe/report tooling. Harness existence proves implementation availability, not trial execution. See matching numbered experiment in Section4. Current opening description: """Audit the first blocking boundary for the two cross-domain fresh runs."""

Current top-level symbols/line references: `23: def audit(suite, case, repeat):`; `197: def main():` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### scripts/experiment16_run.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Experiment execution/probe/report tooling. Harness existence proves implementation availability, not trial execution. See matching numbered experiment in Section4. Current opening description: """First-blocker diagnosis for the Timer and Python fixtures; no production changes."""

Current top-level symbols/line references: `22: def preregister(directory: Path, baseline: Path):`; `56: def trial(directory: Path, case_id: str, repeat: int):`; `90: def batch(directory: Path):`; `115: def main():` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### scripts/experiment17_report.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Experiment execution/probe/report tooling. Harness existence proves implementation availability, not trial execution. See matching numbered experiment in Section4. Current opening description: """Audit field-scoped profile isolation and fresh Timer/game execution."""

Current top-level symbols/line references: `15: def frozen_contracts():`; `30: def profile_protocol():`; `56: def fresh_trial(suite, case, repeat):`; `100: def main():` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### scripts/experiment17_run.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Experiment execution/probe/report tooling. Harness existence proves implementation availability, not trial execution. See matching numbered experiment in Section4. Current opening description: """Frozen Timer and game contracts under optional field-scoped classification."""

Current top-level symbols/line references: `20: def preregister(directory: Path, baseline: Path):`; `52: def batch(directory: Path):`; `75: def main():` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### scripts/experiment2_report.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Experiment execution/probe/report tooling. Harness existence proves implementation availability, not trial execution. See matching numbered experiment in Section4. Current opening description: """Compare paired strict and contract-fallback Mission Compiler runs."""

Current top-level symbols/line references: `13: def load_run(source):`; `23: def has_event(run, kind):`; `27: def summarize(run):`; `50: def report(strict, fallback):`; `79: def format_markdown(result):`; `112: def main():` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### scripts/experiment3_approved_run.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Experiment execution/probe/report tooling. Harness existence proves implementation availability, not trial execution. See matching numbered experiment in Section4. Current opening description: """Run one approved Experiment 3 case against an isolated workspace.""" sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

Current top-level symbols/line references: `11: def main():` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### scripts/experiment3_report.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Experiment execution/probe/report tooling. Harness existence proves implementation availability, not trial execution. See matching numbered experiment in Section4. Current opening description: """Compare paired current and progress-constrained Worker runs."""

Current top-level symbols/line references: `10: def load_run(source):`; `20: def _event(run, kind):`; `25: def summarize(run):`; `71: def report(current, constrained):`; `95: def format_markdown(result):`; `136: def main():` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### scripts/experiment4_report.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Experiment execution/probe/report tooling. Harness existence proves implementation availability, not trial execution. See matching numbered experiment in Section4. Current opening description: """Compare paired current and evidence-grounded mutation runs."""

Current top-level symbols/line references: `11: def load_run(source):`; `21: def _event(run, kind):`; `26: def summarize(run):`; `75: def report(current, grounded):`; `102: def format_markdown(result):`; `142: def main():` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### scripts/experiment5_report.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Experiment execution/probe/report tooling. Harness existence proves implementation availability, not trial execution. See matching numbered experiment in Section4. Current opening description: """Compare paired target-localizer runs against a declared expected source span."""

Current top-level symbols/line references: `10: def load_run(source):`; `20: def _event(run, kind):`; `25: def _overlaps(item, expected):`; `35: def summarize(run, expected):`; `85: def report(current, directed, expected):`; `115: def format_markdown(result):`; `157: def main():` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### scripts/experiment6_report.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Experiment execution/probe/report tooling. Harness existence proves implementation availability, not trial execution. See matching numbered experiment in Section4. Current opening description: """Compare paired Experiment 6 runs with the same approved R-key plan."""

Current top-level symbols/line references: `9: def load(workspace):`; `17: def tool_evidence(workspace):`; `45: def summary(run, workspace):`; `79: def compare(current, resolved, current_workspace, resolved_workspace):`; `105: def markdown(result):`; `146: def main():` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### scripts/experiment7_candidate_probe.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Experiment execution/probe/report tooling. Harness existence proves implementation availability, not trial execution. See matching numbered experiment in Section4. Current opening description: """Run the same browser requirement against one frozen candidate workspace."""

Current top-level symbols/line references: `14: def main():` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### scripts/experiment7_report.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Experiment execution/probe/report tooling. Harness existence proves implementation availability, not trial execution. See matching numbered experiment in Section4. Current opening description: """Summarize frozen candidate A/B verification and live controller follow-through."""

Current top-level symbols/line references: `9: def load(path):`; `13: def direct_summary(payload):`; `35: def live_summary(workspace):`; `81: def report(current, discovery, original, live_workspaces):`; `101: def markdown(data):`; `150: def main():` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### scripts/experiment8_receipt_replay.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Experiment execution/probe/report tooling. Harness existence proves implementation availability, not trial execution. See matching numbered experiment in Section4. Current opening description: """Compare only the receipt boundary using one saved, verified child and patch."""

Current top-level symbols/line references: `17: def main():` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### scripts/experiment8_report.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Experiment execution/probe/report tooling. Harness existence proves implementation availability, not trial execution. See matching numbered experiment in Section4. Current opening description: """Report Experiment 8 receipt percentages separately from live root results.""" sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

Current top-level symbols/line references: `13: def ratio(numerator, denominator):`; `18: def live_summary(workspace):`; `49: def report(replay, live=None):`; `66: def percentage(value):`; `71: def markdown(data):`; `102: def main():` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### scripts/experiment9_parent_probe.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Experiment execution/probe/report tooling. Harness existence proves implementation availability, not trial execution. See matching numbered experiment in Section4. Current opening description: """Compare parent integration routes on one frozen, previously verified patch."""

Current top-level symbols/line references: `15: def main():` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### scripts/experiment9_report.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Experiment execution/probe/report tooling. Harness existence proves implementation availability, not trial execution. See matching numbered experiment in Section4. Current opening description: """Report target resolution, new parent proof and independent live root success.""" sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

Current top-level symbols/line references: `13: def summary(value, requirement_ids, root_verified=None):`; `38: def live_value(workspace):`; `62: def main():` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_adaptive_architecture.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: No descriptive opening docstring.

Current top-level symbols/line references: `12: def expanded_specification(goal="Build a focused browser application"):`; `18: class AdaptiveArchitectureTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_authority_drift.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description:     AUTHORITY_IMPLEMENTATION_DRIFT,     CONFIRMED_CONSISTENT,     CONFIRMED_DRIFT,     NOT_EVALUABLE,

Current top-level symbols/line references: `14: def _authority(record_id="AUTH-001", relation="owner(PAUSE_STATE) = PauseController"):`; `26: def _evidence(`; `39: class AuthorityDriftClassificationTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_authority_fail_closed.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: No descriptive opening docstring.

Current top-level symbols/line references: `10: class AuthorityFailClosedTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_browser_checks.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: class BrowserProbeTests(unittest.TestCase):     def test_clock_probe_accepts_nested_split_visible_time(self):         try:

Current top-level symbols/line references: `6: class BrowserProbeTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_canonical_impact_surfaces.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: No descriptive opening docstring.

Current top-level symbols/line references: `11: class CanonicalImpactSurfaceTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_context_policy.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: class ContextPolicyTests(unittest.TestCase):     def test_old_tool_outputs_are_compacted_without_mutating_history(self):         from hivo.context import compact_messages         original = [{"role": "system", "content": "system"}]

Current top-level symbols/line references: `4: class ContextPolicyTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_core_integration.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: No descriptive opening docstring.

Current top-level symbols/line references: `28: class CoreIntegrationTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_core1_reference_brain_repo_map.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: No descriptive opening docstring.

Current top-level symbols/line references: `37: class Core1ReferenceBrainRepoMapTests(unittest.TestCase):`; `353: def verified_entity(anchor_hash=None, source_hash=None):`; `366: def speculative_entity():`; `373: def tree_digest(root):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_core2_hybrid_repo_intelligence.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: No descriptive opening docstring.

Current top-level symbols/line references: `36: class FakeSemanticRetriever:`; `46: class Core2HybridRepositoryIntelligenceTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_core3_experimental_evidence.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: No descriptive opening docstring.

Current top-level symbols/line references: `53: class Core3ExperimentalEvidenceTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_core4_fault_localization.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: No descriptive opening docstring.

Current top-level symbols/line references: `46: class _CoverageProvider:`; `56: class Core4FaultLocalizationTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_core5_patch_candidate_search.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: No descriptive opening docstring.

Current top-level symbols/line references: `27: class _FakeModel:`; `37: class Core5PatchCandidateSearchTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_core6_large_project_incremental_builder.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description:     CHANGE_PUBLIC_CONTRACT, CHANGE_PRIVATE, analyze_change_impact, build_change_island,

Current top-level symbols/line references: `32: class Core6LargeProjectIncrementalBuilderTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_decomposition_first_experiment.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: No descriptive opening docstring.

Current top-level symbols/line references: `9: class DecompositionFirstExperimentTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_dependency_aware_scheduler.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: class DependencyAwareSchedulerTests(unittest.TestCase):

Current top-level symbols/line references: `8: class DependencyAwareSchedulerTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_evidence_policy.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: class EvidencePolicyTests(unittest.TestCase):     def test_mutation_failure_record_classifies_deterministic_categories(self):         from hivo.evidence import mutation_failure_record         cases = [

Current top-level symbols/line references: `4: class EvidencePolicyTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_execution_contracts.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: No descriptive opening docstring.

Current top-level symbols/line references: `11: class ApprovedPlanExecutionContractTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_experiment1_report.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: class Experiment1ReportTests(unittest.TestCase):     def run_record(self, route, events, blocker=None):         return {

Current top-level symbols/line references: `6: class Experiment1ReportTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_experiment10_child_handoff.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: No descriptive opening docstring.

Current top-level symbols/line references: `10: class ChildHandoffDiagnosticTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_experiment11_evidence_compatibility.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: No descriptive opening docstring.

Current top-level symbols/line references: `15: class SemanticEvidenceCompatibilityTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_experiment12_harness.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: No descriptive opening docstring.

Current top-level symbols/line references: `13: class GeneralizationHarnessTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_experiment12_metrics.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: def trial(**changes):     record = {"completed":True, "verification_executed":False, "verification_pass":False,

Current top-level symbols/line references: `7: def trial(**changes):`; `19: class Experiment12MetricTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_experiment13_monotonic.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: No descriptive opening docstring.

Current top-level symbols/line references: `12: class MonotonicBrowserTests(unittest.TestCase):`; `81: class MonotonicUnitTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_experiment14_strict.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: No descriptive opening docstring.

Current top-level symbols/line references: `9: class StrictBrowserTests(unittest.TestCase):`; `75: class StrictSuiteTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_experiment15_evidence_edit.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: No descriptive opening docstring.

Current top-level symbols/line references: `9: class EvidenceEditBindingTests(unittest.TestCase):`; `114: class EvidenceEditControllerTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_experiment17_field_scoped_profile.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: class FieldScopedProfileTests(unittest.TestCase):     def test_hash_fragment_cannot_turn_timer_into_game(self):

Current top-level symbols/line references: `7: class FieldScopedProfileTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_experiment2_report.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: class Experiment2ReportTests(unittest.TestCase):     def run_record(self, policy, worker):         return {

Current top-level symbols/line references: `6: class Experiment2ReportTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_experiment3_report.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: def run(policy, mutation=None):     return {         "worker_progress_policy": policy,

Current top-level symbols/line references: `6: def run(policy, mutation=None):`; `32: class Experiment3ReportTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_experiment3_worker_progress.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: No descriptive opening docstring.

Current top-level symbols/line references: `11: def tool_call(name, arguments):`; `18: class WorkerProgressTests(unittest.TestCase):`; `49: class WorkerProgressControllerTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_experiment4_mutation_grounding.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: No descriptive opening docstring.

Current top-level symbols/line references: `11: def tool_call(name, arguments):`; `18: def range_result(path, first, last):`; `26: class MutationGroundingTests(unittest.TestCase):`; `123: class MutationGroundingControllerTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_experiment4_report.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: def run(policy, first_applied=None):     return {         "mutation_grounding_policy": policy,

Current top-level symbols/line references: `6: def run(policy, first_applied=None):`; `40: class Experiment4ReportTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_experiment5_report.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: EXPECTED = {"path": "index.html", "start_line": 406, "end_line": 411}

Current top-level symbols/line references: `9: def run(policy):`; `44: class Experiment5ReportTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_experiment5_target_locator.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: No descriptive opening docstring.

Current top-level symbols/line references: `11: def tool_call(name, args):`; `16: class TargetLocatorTests(unittest.TestCase):`; `59: class TargetLocatorControllerTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_experiment6_verification_environment.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: No descriptive opening docstring.

Current top-level symbols/line references: `12: class VerificationEnvironmentTests(unittest.TestCase):`; `88: class VerificationResolutionControllerTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_experiment7_verification_surfaces.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: class _Keyboard:

Current top-level symbols/line references: `8: class _Keyboard:`; `17: class _Page:`; `35: class _InstrumentedPage(_Page):`; `50: class VerificationSurfaceTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_experiment8_atomic_child_receipt.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: No descriptive opening docstring.

Current top-level symbols/line references: `13: class AtomicChildReceiptTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_experiment9_integration_targets.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: No descriptive opening docstring.

Current top-level symbols/line references: `12: class IntegrationTargetTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_game_artifact.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: ROOT = Path(__file__).resolve().parents[1] NUMBERED_GAME = ROOT / "list" / "project-1" / "index.html"

Current top-level symbols/line references: `12: class GameArtifactTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_host_preflight.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: No descriptive opening docstring.

Current top-level symbols/line references: `13: class HostPreflightTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_impact_map_contract.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: No descriptive opening docstring.

Current top-level symbols/line references: `11: class ImpactMapContractTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_impact_planning.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: No descriptive opening docstring.

Current top-level symbols/line references: `11: class ImpactPlanningTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_long_term_memory.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: No descriptive opening docstring.

Current top-level symbols/line references: `9: class LongTermMemoryTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_mini.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: No descriptive opening docstring.

Current top-level symbols/line references: `11: class MiniAgentRegressionTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_model_policy.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: class SingleModelPolicyTests(unittest.TestCase):     def test_every_role_is_pinned_to_gemma(self):         from hivo.model_policy import GEMMA_MODEL, SingleModelPolicy         roles = SingleModelPolicy().role_models()

Current top-level symbols/line references: `4: class SingleModelPolicyTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_obligation_aware_plan_closure.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: No descriptive opening docstring.

Current top-level symbols/line references: `11: class ObligationAwarePlanClosureTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_obligation_conserving_reconciliation.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: No descriptive opening docstring.

Current top-level symbols/line references: `10: class ObligationConservingReconciliationTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_planning_packet_budget.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: No descriptive opening docstring.

Current top-level symbols/line references: `11: class PlanningPacketBudgetTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_playbooks.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: class PlaybookTests(unittest.TestCase):     def test_project_type_is_general_and_not_game_specific(self):         game = {"goal": "Build a responsive 3D browser game", "requirements": ["collision"]}

Current top-level symbols/line references: `6: class PlaybookTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_pre_mutation_impact.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: No descriptive opening docstring.

Current top-level symbols/line references: `21: class PreMutationImpactContractTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_project_store.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: class ProjectStoreTests(unittest.TestCase):     def test_legacy_list_contents_become_project_one_and_next_is_incremented(self):

Current top-level symbols/line references: `7: class ProjectStoreTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_project_understanding.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: No descriptive opening docstring.

Current top-level symbols/line references: `12: def empty_specification(goal):`; `19: class ProjectUnderstandingTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_project_world_model.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: No descriptive opening docstring.

Current top-level symbols/line references: `33: class ProjectWorldModelTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_requirement_clarification.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: No descriptive opening docstring.

Current top-level symbols/line references: `9: class RequirementClarificationTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_semantic_coupling.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description:     ANALYSIS_CONFLICTING,     ANALYSIS_PARTIAL,     BLOCKED,     CONFIGURATION_COUPLING,

Current top-level symbols/line references: `29: class FakeWorldModel:`; `51: def fact(fact_id, subject, relation, object_value, *, state="VERIFIED", score=100, source=None):`; `64: class SemanticCouplingTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_semantic_evidence_resolver.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: No descriptive opening docstring.

Current top-level symbols/line references: `24: class SemanticEvidenceResolverTests(unittest.TestCase):`; `462: def stage7_semantic_hop_limit():` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_structural_decomposition.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: No descriptive opening docstring.

Current top-level symbols/line references: `11: class StructuralDecompositionTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_structured_worker_contract.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: No descriptive opening docstring.

Current top-level symbols/line references: `10: class _FakeHTTPResponse:`; `25: class StructuredWorkerContractTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_v24_2_canonical_mandatory_core.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: No descriptive opening docstring.

Current top-level symbols/line references: `10: class CanonicalMandatoryPlanningCoreTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_v24_3_impact_decision_frame.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: No descriptive opening docstring.

Current top-level symbols/line references: `12: class ImpactDecisionFrameTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_v24_4_2_current_surface_preservation_binding.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: No descriptive opening docstring.

Current top-level symbols/line references: `28: class _ReadOnlyProjectBrain:`; `52: class CurrentSurfacePreservationBindingTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_v24_4_3_decision_relevant_impact_choice_projection.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: No descriptive opening docstring.

Current top-level symbols/line references: `9: class DecisionRelevantImpactChoiceProjectionTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_v24_4_4_challenger_review_relevant_projection.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: No descriptive opening docstring.

Current top-level symbols/line references: `9: class ChallengerReviewRelevantProjectionTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_v24_4_5_canonical_final_plan_budget_closure.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: No descriptive opening docstring.

Current top-level symbols/line references: `13: class CanonicalFinalPlanBudgetClosureTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_v24_4_6_live_equivalent_final_plan_bound_closure.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: No descriptive opening docstring.

Current top-level symbols/line references: `14: class LiveEquivalentCanonicalFinalPlanBoundClosureTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_v24_4_obligation_anchored_impact_coverage.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: No descriptive opening docstring.

Current top-level symbols/line references: `9: class ObligationAnchoredImpactCoverageTests(ImpactDecisionFrameTests):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_v25_1_approval_bound_execution_lifecycle.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: """Provider-free V25.1 approval-bound execution lifecycle tests."""

Current top-level symbols/line references: `28: def _load(root: Path, name: str, fallback=None):`; `36: class ApprovalBoundExecutionLifecycleTests(unittest.TestCase):`; `420: def _load_text(path: Path) -> str:` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_v25_2_worker_execution_invariant_projection.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: """Provider-free V25.2 deterministic Worker-invariant projection tests."""

Current top-level symbols/line references: `28: def _load(path: Path, fallback=None):`; `35: class WorkerExecutionInvariantProjectionTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_v25_3_verification_obligation_coverage_gate.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: """Provider-free V25.3 verification-obligation coverage tests."""

Current top-level symbols/line references: `28: def _load(path: Path, fallback=None):`; `35: class VerificationObligationCoverageGateTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_v25_4_1_verification_coverage_artifact_propagation.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: """Provider-free V25.4.1 coverage-artifact propagation regressions."""

Current top-level symbols/line references: `44: def _load(name: str, field: str | None = None):`; `49: class VerificationCoverageArtifactPropagationTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_v25_4_2_approved_verification_exact_routing.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: """Provider-free V25.4.2 exact approved-verification routing regressions."""

Current top-level symbols/line references: `39: def _load(name: str, field: str | None = None):`; `44: class ApprovedVerificationExactRoutingTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_v25_4_verification_complete_plan_revision.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: """Provider-free V25.4 verification-complete plan revision tests."""

Current top-level symbols/line references: `28: def _load(path: Path):`; `32: class VerificationCompletePlanRevisionTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_v25_5_precommit_execution_invariant_gate.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: """Provider-free V25.5 pre-commit execution-invariant enforcement tests."""

Current top-level symbols/line references: `35: def _load(path: Path, fallback=None):`; `42: class PreCommitExecutionInvariantGateTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_v25_6_execution_verification_authority_closure.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: """Provider-free V25.6 execution-verification authority closure tests."""

Current top-level symbols/line references: `39: def _read_artifact(name: str, field: str | None = None):`; `44: class V256ExecutionVerificationAuthorityClosureTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_v25_approval_bound_execution_authorization.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: """Provider-free Stage 6C-A approval-boundary regression tests."""

Current top-level symbols/line references: `20: def _load(name, fallback=None):`; `28: class ApprovalBoundExecutionAuthorizationTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_v26_3_recovery_strategy.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: """Provider-free V26.3 bounded recovery-strategy tests."""

Current top-level symbols/line references: `15: class V263RecoveryStrategyTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_v26_4_tool_contract_recovery.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: """Provider-free V26.4 bounded tool-contract recovery tests."""

Current top-level symbols/line references: `15: class V264ToolContractRecoveryTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_v26_5_preverification_recovery.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: """Provider-free V26.5 pre-verification recovery eligibility tests."""

Current top-level symbols/line references: `18: class V265PreVerificationRecoveryTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_v26_6_2_active_schema_mutation_intent_reset.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: No descriptive opening docstring.

Current top-level symbols/line references: `13: class V2662ActiveSchemaMutationIntentTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_v26_6_no_mutation_recovery_search.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: """Provider-free V26.6 no-mutation recovery search closure tests."""

Current top-level symbols/line references: `15: class V266NoMutationRecoverySearchTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_v26_7_progress_aware_completion_recovery.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: No descriptive opening docstring.

Current top-level symbols/line references: `10: class V267ProgressAwareCompletionRecoveryTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_v26_recovery_foundation.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: """Provider-free V26 authority-bounded autonomous-recovery tests."""

Current top-level symbols/line references: `17: class V26RecoveryFoundationTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_verification_applicability.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: No descriptive opening docstring.

Current top-level symbols/line references: `19: class VerificationApplicabilityTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_verification_policy.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: No descriptive opening docstring.

Current top-level symbols/line references: `12: class VerificationPolicyTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_verified_child_integration.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: No descriptive opening docstring.

Current top-level symbols/line references: `28: class VerifiedChildIntegrationGateTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_verified_state_planning.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: No descriptive opening docstring.

Current top-level symbols/line references: `24: class VerifiedStatePlanningTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_verified_state_promotion.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: No descriptive opening docstring.

Current top-level symbols/line references: `41: class VerifiedStatePromotionTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### tests/test_verified_state_reentry.py

Change type: unresolved existing file (C); not attributed to the October19 correction. Regression coverage; a filename is not proof of historical execution. Results are limited to the logs in Section5. Current opening description: No descriptive opening docstring.

Current top-level symbols/line references: `37: class VerifiedStateReentryTests(unittest.TestCase):` Previous source is unavailable; behavior deltas and exact modified methods cannot be established for this file. Current byte identity is in Section10.

### audit_runs/20261019-impact-fix/adaptive-final.log

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Retained execution log/input/exit marker; opening observation: test_baseline_and_recursive_call_the_same_leaf_engine (test_adaptive_architecture.AdaptiveArchitectureTests.test_baseline_and_recursive_call_the_same_leaf_engine) ... ok test_behavioral_failure_after_repair_does_not_beco. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-impact-fix/authority-final.log

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Retained execution log/input/exit marker; opening observation: test_all_classification_paths_are_model_free (test_authority_drift.AuthorityDriftClassificationTests.test_all_classification_paths_are_model_free) ... ok test_different_confirmed_contradictions_remain_separate (test_auth. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-impact-fix/before-reproduction.json

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Structured record fields/type: status, failure_type, summary, impact_validation, impact_authorized, context_sufficiency, metrics, source_sha256. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-impact-fix/context-final.log

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Retained execution log/input/exit marker; opening observation: test_completion_budget_is_bounded_and_fails_closed (test_context_sufficiency_gate.ContextSufficiencyGateTests.test_completion_budget_is_bounded_and_fails_closed) ... ok test_contradictory_evidence_requires_authoritative_. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-impact-fix/context-regression.log

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Retained execution log/input/exit marker; opening observation: test_completion_budget_is_bounded_and_fails_closed (test_context_sufficiency_gate.ContextSufficiencyGateTests.test_completion_budget_is_bounded_and_fails_closed) ... ok test_contradictory_evidence_requires_authoritative_. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-impact-fix/controlled_replay.py

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Retained diagnostic harness; opening text: """Provider-free integration replay: only model responses are scripted.  This is not a live Ollama run and does not replace host qualification.. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-impact-fix/controlled-final-result.json

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Structured record fields/type: execution_kind, scripted_provider_responses, status, failure_type, file_exists, exact_bytes, run_id, source_sha256, production_source_sha256, metrics, source_requirement_ids, impact_comparison, verification_aggregation. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-impact-fix/controlled-final.log

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Retained execution log/input/exit marker; opening observation: [MODE] baseline [BUILDER] ROOT executing [TOOL] context_sufficiency_check -. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-impact-fix/controlled-replay-result.json

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Structured record fields/type: execution_kind, scripted_provider_responses, status, failure_type, file_exists, exact_bytes, run_id, source_sha256, metrics, source_requirement_ids, impact_comparison. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-impact-fix/controlled-replay-routed.log

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Retained execution log/input/exit marker; opening observation: [MODE] baseline [BUILDER] ROOT executing [TOOL] context_sufficiency_check -. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-impact-fix/controlled-replay-verified.log

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Retained execution log/input/exit marker; opening observation: [MODE] baseline [BUILDER] ROOT executing [TOOL] context_sufficiency_check -. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-impact-fix/controlled-replay.log

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Retained execution log/input/exit marker; opening observation: [MODE] baseline [BUILDER] ROOT executing [TOOL] context_sufficiency_check -. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-impact-fix/evidence-sha256.json

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Structured record fields/type: adaptive-final.log, authority-final.log, before-reproduction.json, context-final.log, context-regression.log, controlled-final-result.json, controlled-final.log, controlled-replay-result.json, controlled-replay-routed.log, controlled-replay-verified.log, controlled-replay.log, controlled_replay.py, experiments-final.log, final-source-integrity.json, full-regression-console.log, full-regression-result.json, full-regression.log, greenfield-complete.log, greenfield-final-verified.log, greenfield-final.log, greenfield-handoff-final.log, greenfield-regression.log, greenfield-routing-complete.log, historical-specification-events.json, impact-final.log, impact-regression.log, implementation-locations.json, live-auto-final-exit.txt, live-auto-final.log, live-auto-interrupted.json, live-auto.log, live-baseline-exit.txt, live-baseline.log, live-request.txt, live-results-summary.json, native-proof-recheck.json, new-tests-first.log, new-tests-fourth.log, new-tests-second.log, new-tests-third.log, raw-source-check.json, reentry-before.log, regression-comparison.json, reproduce_before.py, ROOT-CAUSE-REPORT.md, test-results-final.json, test-results.json, understanding-final.log, controlled-baseline/welcone.txt, controlled-baseline-routed/.agent_experiment.jsonl, controlled-baseline-routed/welcone.txt, controlled-baseline-verified/welcone.txt, controlled-final/.agent_experiment.jsonl, controlled-final/welcone.txt, live-auto/.agent_host_preflight.json, live-auto-final/.agent_experiment.jsonl, live-auto-final/.agent_host_preflight.json, live-baseline/.agent_host_preflight.json, raw-source-check/.agent_runs/20261019T071723-906594f8.jsonl, live-auto-final/.agent_runs/20261019T065255-5928c8e3.jsonl, live-auto-final/.hivo/memory.sqlite3, live-auto/.agent_runs/20261019T063924-418790a4.jsonl, live-auto/.hivo/memory.sqlite3, controlled-final/.agent_runs/20261019T071642-a38faf6a.jsonl, controlled-final/.hivo/memory.sqlite3, controlled-baseline-verified/.agent_runs/20261019T065917-8cd25e0d.jsonl, controlled-baseline-verified/.hivo/memory.sqlite3, controlled-baseline-verified/.hivo/memory.sqlite3-shm, controlled-baseline-verified/.hivo/memory.sqlite3-wal, controlled-baseline-routed/.agent_runs/20261019T070259-88ba0efc.jsonl, controlled-baseline-routed/.hivo/memory.sqlite3, controlled-baseline-routed/.hivo/memory.sqlite3-shm, controlled-baseline-routed/.hivo/memory.sqlite3-wal, controlled-baseline/.agent_runs/20261019T065900-91f2fa0a.jsonl, controlled-baseline/.hivo/memory.sqlite3, before/.agent_runs/20261019T063028-f66ce012.jsonl, before/.hivo/memory.sqlite3. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-impact-fix/experiments-final.log

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Retained execution log/input/exit marker; opening observation: test_existing_run_file_browser_mismatch_is_explained_without_fixing_it (test_experiment10_child_handoff.ChildHandoffDiagnosticTests.test_existing_run_file_browser_mismatch_is_explained_without_fixing_it) ... ok test_gate. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-impact-fix/final-source-integrity.json

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Structured record fields/type: matches_final_controlled_replay, all_match, syntax_parsed. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-impact-fix/full-regression-console.log

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Retained execution log/input/exit marker; opening observation: [MODE] baseline [ROOT] Build a difficult single-file browser application [FIT ROOT] EXECUTE. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-impact-fix/full-regression-result.json

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Structured record fields/type: discovered, excluded, tests_run, failure_records, errors, skipped, failure_tests, error_tests, skip_reasons, elapsed_seconds, exit_code. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-impact-fix/full-regression.log

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Retained execution log/input/exit marker; opening observation: test_baseline_and_recursive_call_the_same_leaf_engine (test_adaptive_architecture.AdaptiveArchitectureTests.test_baseline_and_recursive_call_the_same_leaf_engine) ... ok test_behavioral_failure_after_repair_does_not_beco. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-impact-fix/greenfield-complete.log

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Retained execution log/input/exit marker; opening observation: test_a_simple_greenfield_file_verified_through_leaf (test_greenfield_impact_lifecycle.GreenfieldImpactLifecycleTests.test_a_simple_greenfield_file_verified_through_leaf) ... ok test_b_lifecycle_precedes_mutation (test_gr. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-impact-fix/greenfield-final-verified.log

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Retained execution log/input/exit marker; opening observation: test_a_simple_greenfield_file_verified_through_leaf (test_greenfield_impact_lifecycle.GreenfieldImpactLifecycleTests.test_a_simple_greenfield_file_verified_through_leaf) ... ok test_b_lifecycle_precedes_mutation (test_gr. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-impact-fix/greenfield-final.log

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Retained execution log/input/exit marker; opening observation: test_a_simple_greenfield_file_verified_through_leaf (test_greenfield_impact_lifecycle.GreenfieldImpactLifecycleTests.test_a_simple_greenfield_file_verified_through_leaf) ... ok test_b_lifecycle_precedes_mutation (test_gr. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-impact-fix/greenfield-handoff-final.log

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Retained execution log/input/exit marker; opening observation: test_a_simple_greenfield_file_verified_through_leaf (test_greenfield_impact_lifecycle.GreenfieldImpactLifecycleTests.test_a_simple_greenfield_file_verified_through_leaf) ... ok test_b_lifecycle_precedes_mutation (test_gr. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-impact-fix/greenfield-regression.log

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Retained execution log/input/exit marker; opening observation: test_a_simple_greenfield_file_verified_through_leaf (test_greenfield_impact_lifecycle.GreenfieldImpactLifecycleTests.test_a_simple_greenfield_file_verified_through_leaf) ... ok test_b_lifecycle_precedes_mutation (test_gr. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-impact-fix/greenfield-routing-complete.log

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Retained execution log/input/exit marker; opening observation: test_a_simple_greenfield_file_verified_through_leaf (test_greenfield_impact_lifecycle.GreenfieldImpactLifecycleTests.test_a_simple_greenfield_file_verified_through_leaf) ... ok test_b_lifecycle_precedes_mutation (test_gr. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-impact-fix/historical-specification-events.json

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Retained execution log/input/exit marker; opening observation: . Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-impact-fix/impact-final.log

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Retained execution log/input/exit marker; opening observation: test_benchmark_reports_zero_incorrectly_allowed_mutations (test_pre_mutation_impact.PreMutationImpactContractTests.test_benchmark_reports_zero_incorrectly_allowed_mutations) ... ok test_configuration_relation_is_recorded. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-impact-fix/impact-regression.log

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Retained execution log/input/exit marker; opening observation: test_benchmark_reports_zero_incorrectly_allowed_mutations (test_pre_mutation_impact.PreMutationImpactContractTests.test_benchmark_reports_zero_incorrectly_allowed_mutations) ... ok test_configuration_relation_is_recorded. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-impact-fix/implementation-locations.json

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Structured record fields/type: mini.py, hivo/requirements.py, hivo/pre_mutation_impact.py, hivo/verification_routing.py, tests/test_greenfield_impact_lifecycle.py, tests/test_context_sufficiency_gate.py. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-impact-fix/live-auto-final-exit.txt

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Retained execution log/input/exit marker; opening observation: 0. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-impact-fix/live-auto-final.log

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Retained execution log/input/exit marker; opening observation: workspace set to: D:\ECU\grade_project\باذن الله يشتغل\mini_hivo-main (1)\mini_hivo-main\audit_runs\20261019-impact-fix\live-auto-final  HIVO HOST PREFLIGHT: PASS. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-impact-fix/live-auto-interrupted.json

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Structured record fields/type: status, reason, run_id, source_sha256, authorization_events, scope_blocks, bare_file_exists, resolved_file_exists, completed_root_result. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-impact-fix/live-auto.log

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Retained execution log/input/exit marker; opening observation: workspace set to: D:\ECU\grade_project\باذن الله يشتغل\mini_hivo-main (1)\mini_hivo-main\audit_runs\20261019-impact-fix\live-auto  HIVO HOST PREFLIGHT: PASS. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-impact-fix/live-baseline-exit.txt

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Retained execution log/input/exit marker; opening observation: 2. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-impact-fix/live-baseline.log

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Retained execution log/input/exit marker; opening observation: workspace set to: D:\ECU\grade_project\باذن الله يشتغل\mini_hivo-main (1)\mini_hivo-main\audit_runs\20261019-impact-fix\live-baseline  HIVO HOST PREFLIGHT: FAIL. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-impact-fix/live-request.txt

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Retained execution log/input/exit marker; opening observation: Create a text file named welcone containing exactly welcome.. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-impact-fix/live-results-summary.json

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Structured record fields/type: array. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-impact-fix/native-proof-recheck.json

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Structured record fields/type: checks, all_passed, routing_source_sha256, proof_origin. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-impact-fix/new-tests-first.log

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Retained execution log/input/exit marker; opening observation: . Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-impact-fix/new-tests-fourth.log

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Retained execution log/input/exit marker; opening observation: test_a_simple_greenfield_file_verified_through_leaf (test_greenfield_impact_lifecycle.GreenfieldImpactLifecycleTests.test_a_simple_greenfield_file_verified_through_leaf) ... ok test_b_lifecycle_precedes_mutation (test_gr. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-impact-fix/new-tests-second.log

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Retained execution log/input/exit marker; opening observation: test_a_simple_greenfield_file_verified_through_leaf (test_greenfield_impact_lifecycle.GreenfieldImpactLifecycleTests.test_a_simple_greenfield_file_verified_through_leaf) ... ERROR test_b_lifecycle_precedes_mutation (test. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-impact-fix/new-tests-third.log

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Retained execution log/input/exit marker; opening observation: test_a_simple_greenfield_file_verified_through_leaf (test_greenfield_impact_lifecycle.GreenfieldImpactLifecycleTests.test_a_simple_greenfield_file_verified_through_leaf) ... FAIL test_b_lifecycle_precedes_mutation (test_. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-impact-fix/raw-source-check.json

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Structured record fields/type: typed_literal_scope_not_granted_from_abbreviated_model_goal, mutation_tools_called. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-impact-fix/reentry-before.log

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Retained execution log/input/exit marker; opening observation: test_a_simple_greenfield_file_verified_through_leaf (test_greenfield_impact_lifecycle.GreenfieldImpactLifecycleTests.test_a_simple_greenfield_file_verified_through_leaf) ... ok test_b_lifecycle_precedes_mutation (test_gr. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-impact-fix/regression-comparison.json

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Structured record fields/type: baseline_failure_headers, current_failure_headers, new_failures, resolved_failures, same_failure_identities. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-impact-fix/reproduce_before.py

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Retained diagnostic harness; opening text: """Replay the observed no-tool completion through the real pre-mutation gates.""" import hashlib import json. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-impact-fix/ROOT-CAUSE-REPORT.md

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Historical narrative report, preserved as evidence. Its findings and limitations are summarized above. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-impact-fix/test-results-final.json

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Structured record fields/type: array. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-impact-fix/test-results.json

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Structured record fields/type: array. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-impact-fix/understanding-final.log

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Retained execution log/input/exit marker; opening observation: test_baseline_keeps_task_brain_architecture_out_of_worker_execution (test_project_understanding.ProjectUnderstandingTests.test_baseline_keeps_task_brain_architecture_out_of_worker_execution) ... ok test_compound_source_r. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-phase2/authority-unsandboxed.log

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Retained execution log/input/exit marker; opening observation: test_all_classification_paths_are_model_free (test_authority_drift.AuthorityDriftClassificationTests.test_all_classification_paths_are_model_free) ... ok test_different_confirmed_contradictions_remain_separate (test_auth. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-phase2/authority.log

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Retained execution log/input/exit marker; opening observation: test_all_classification_paths_are_model_free (test_authority_drift.AuthorityDriftClassificationTests.test_all_classification_paths_are_model_free) ... ok test_different_confirmed_contradictions_remain_separate (test_auth. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-phase2/browser-runtime.json

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Structured record fields/type: command, exit_code, stdout, stderr, elapsed_seconds. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-phase2/context.log

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Retained execution log/input/exit marker; opening observation: test_completion_budget_is_bounded_and_fails_closed (test_context_sufficiency_gate.ContextSufficiencyGateTests.test_completion_budget_is_bounded_and_fails_closed) ... ok test_contradictory_evidence_requires_authoritative_. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-phase2/evidence-sha256.json

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Structured record fields/type: authority-unsandboxed.log, authority.log, browser-runtime.json, context.log, execution-summary.json, experiment12-node-pilot-exit.txt, experiment12-node-pilot.log, experiment12-preregister.log, experiments.log, full-suite.log, host-preflight-isolated-result.json, host-preflight-isolated.log, host-preflight-result.json, host-preflight.log, model-policy.log, normal-cli-startup-exit.txt, normal-cli-startup.log, PHASE2-REPORT.md, pilot-audit.json, production-integrity-final.json, production-integrity.json, regression-console.log, regression-excluding-live-test.log, regression-failure-index.json, regression-result.json, test-executions.json, experiment12-suite/manifest.json, host-preflight/.agent_host_preflight.json, host-preflight-isolated/.agent_host_preflight.json, normal-cli-workspace/.agent_host_preflight.json, normal-cli-workspace/.hivo/memory.sqlite3, experiment12-suite/arena_arrow/authority.json, experiment12-suite/arena_q_restart/authority.json, experiment12-suite/node_unique/authority.json, experiment12-suite/node_unique/current-1-observations.json, experiment12-suite/node_unique/current-1-result.json, experiment12-suite/python_clamp/authority.json, experiment12-suite/timer_pause/authority.json, experiment12-suite/timer_pause/seed/timer.html, experiment12-suite/python_clamp/seed/numbers_api.py, experiment12-suite/python_clamp/seed/tests/test_clamp.py, experiment12-suite/node_unique/current-1/.agent_experiment.jsonl, experiment12-suite/node_unique/current-1/.agent_host_preflight.json, experiment12-suite/node_unique/current-1/values.js, experiment12-suite/node_unique/seed/values.js, experiment12-suite/node_unique/seed/tests/unique.test.js, experiment12-suite/node_unique/current-1/.agent_runs/20261019T054959-87298d45.jsonl, experiment12-suite/node_unique/current-1/.hivo/memory.sqlite3, experiment12-suite/node_unique/current-1/tests/unique.test.js, experiment12-suite/arena_q_restart/seed/arena.html, experiment12-suite/arena_arrow/seed/arena.html. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-phase2/execution-summary.json

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Structured record fields/type: array. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-phase2/experiment12-node-pilot-exit.txt

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Retained execution log/input/exit marker; opening observation: 0. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-phase2/experiment12-node-pilot.log

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Retained execution log/input/exit marker; opening observation: [MODEL] gemma4:e4b [PROVIDER] local Ollama only [CAPACITY] 1/4 (PARAMETER-SIZE HEURISTIC; NOT A BENCHMARK). Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-phase2/experiment12-preregister.log

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Retained execution log/input/exit marker; opening observation: preregistered 5 tasks; 30 fresh trials. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-phase2/experiments.log

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Retained execution log/input/exit marker; opening observation: test_existing_run_file_browser_mismatch_is_explained_without_fixing_it (test_experiment10_child_handoff.ChildHandoffDiagnosticTests.test_existing_run_file_browser_mismatch_is_explained_without_fixing_it) ... ok test_gate. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-phase2/full-suite.log

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Retained execution log/input/exit marker; opening observation: test_baseline_and_recursive_call_the_same_leaf_engine (test_adaptive_architecture.AdaptiveArchitectureTests.test_baseline_and_recursive_call_the_same_leaf_engine) ... ok test_behavioral_failure_after_repair_does_not_beco. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-phase2/host-preflight-isolated-result.json

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Structured record fields/type: passed, status, preflight_id, report, marker_path, persisted. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-phase2/host-preflight-isolated.log

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Retained execution log/input/exit marker; opening observation: HIVO HOST PREFLIGHT: PASS  Selected model: gemma4:e4b. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-phase2/host-preflight-result.json

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Structured record fields/type: passed, status, preflight_id, report, marker_path, persisted. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-phase2/host-preflight.log

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Retained execution log/input/exit marker; opening observation: HIVO HOST PREFLIGHT: FAIL  Selected model: gemma4:e4b. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-phase2/model-policy.log

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Retained execution log/input/exit marker; opening observation: test_any_other_requested_model_is_rejected (test_model_policy.SingleModelPolicyTests.test_any_other_requested_model_is_rejected) ... ok test_every_role_is_pinned_to_gemma (test_model_policy.SingleModelPolicyTests.test_ev. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-phase2/normal-cli-startup-exit.txt

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Retained execution log/input/exit marker; opening observation: 0. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-phase2/normal-cli-startup.log

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Retained execution log/input/exit marker; opening observation: workspace set to: D:\ECU\grade_project\باذن الله يشتغل\mini_hivo-main (1)\mini_hivo-main\audit_runs\20261019-phase2\normal-cli-workspace  HIVO HOST PREFLIGHT: PASS. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-phase2/PHASE2-REPORT.md

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Historical narrative report, preserved as evidence. Its findings and limitations are summarized above. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-phase2/pilot-audit.json

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Structured record fields/type: run_id, process_exit_code, result_status, metrics_status, elapsed_seconds, model_calls, builder_calls, tool_calls, root_verified, first_blocker, source_and_tests_match_seed. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-phase2/production-integrity-final.json

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Structured record fields/type: production_matches_preregistration, all_match, live_trials_started, live_trial_count, live_trial_status, normal_cli_startup_exit_code. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-phase2/production-integrity.json

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Structured record fields/type: production_matches_preregistration, all_match, live_trials_started. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-phase2/regression-console.log

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Retained execution log/input/exit marker; opening observation: [MODE] baseline [ROOT] Build a difficult single-file browser application [FIT ROOT] EXECUTE. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-phase2/regression-excluding-live-test.log

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Retained execution log/input/exit marker; opening observation: test_baseline_and_recursive_call_the_same_leaf_engine (test_adaptive_architecture.AdaptiveArchitectureTests.test_baseline_and_recursive_call_the_same_leaf_engine) ... ok test_behavioral_failure_after_repair_does_not_beco. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-phase2/regression-failure-index.json

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Structured record fields/type: array. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-phase2/regression-result.json

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Structured record fields/type: discovered, excluded, tests_run, failures, errors, skipped, successful, elapsed_seconds. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### audit_runs/20261019-phase2/test-executions.json

Change type: generated/retained historical audit artifact (G, directory/session attribution; exact creation event not available). Previous pre-session bytes are unavailable; current contents serve as evidence rather than an application feature. Structured record fields/type: array. Related controller/experiment and outcome are described in Sections3–6. Log existence alone is not a passing result. SHA-256 and length appear in Section10; file is preserved.

### Generated nested workspaces and older research documentation

The remaining audit_runs nested files are generated seeds, authorities, manifests, result/metric logs, .hivo run/memory artifacts, preflight markers or literal outputs. Each exact path is inventoried below as G. Their meaning derives from the parent experiment12-suite, normal-cli-workspace, live-* or controlled-* run, not from a claim that all runs passed. The eighteen list/ files are C: older user/runtime outputs whose session of origin is not established. The87 reports/ and2 docs/ files are B retained research documentation/result/supporting snapshots; their detailed experiment context is Section4 and their individual exact path/hash is Section10. Historical before-bytes for these generated/documentary files are unavailable. No deleted/renamed path is inferred.

## 10. Complete retained file inventory

This is a comprehensive initial inventory of all 440 project files outside .venv and any __pycache__ directory. Types are historical classifications, not Git status. “Present/C” explicitly means modification origin unknown. A/B/G levels follow Section1. SHA-256 values were independently read during this documentation task; they prove current byte identities, not historical authorship.

| Repository-relative path | Historical type / confidence | Bytes | Initial SHA-256 |
|---|---|---:|---|
| `.agent_experiment.jsonl` | Present; origin unresolved/C | 479 | `afe310ebd9afcc72b9cdf4b2bb67546d60687749741e7cfcba3624b2a7cd049e` |
| `.gitattributes` | Present; origin unresolved/C | 66 | `1a1dbe176bc233b499d35a57db7513f2941c99ab9759f177830c9149be99005b` |
| `.gitignore` | Present; origin unresolved/C | 160 | `c46e61fea3a7100bca6c0cac20897c17c842e685aa389a82cf4db6e742b4f691` |
| `audit_runs/20261019-impact-fix/adaptive-final.log` | Generated/G | 31789 | `3f2147803e494a7df6b04a3c8dd2ebd31e09ec56d4ae09d40e1166beed0d286b` |
| `audit_runs/20261019-impact-fix/authority-final.log` | Generated/G | 24089 | `a56c9ea8da43813ff9193792aa759bcd32902fbd33358a1be6bce6d4a765503f` |
| `audit_runs/20261019-impact-fix/before-reproduction.json` | Generated/G | 1570 | `78871f03e5650563cbab9517c003fe9a337302cfa9e744e69c1b84b980ace1d1` |
| `audit_runs/20261019-impact-fix/before/.agent_runs/20261019T063028-f66ce012.jsonl` | Generated/G | 2252 | `a2327a8990c29554fc02f61329c0b05a4583f3afbf471b0eaad3f00a0a284387` |
| `audit_runs/20261019-impact-fix/before/.hivo/memory.sqlite3` | Generated/G | 135168 | `cde222b7ca73c11d6cd077227bf3db7fd15e031918589d2e349e9e6e656eec3e` |
| `audit_runs/20261019-impact-fix/context-final.log` | Generated/G | 1973 | `25852eead379dc35d9a26362035e4aebc9660cece27de2ffb9ac70257bd52485` |
| `audit_runs/20261019-impact-fix/context-regression.log` | Generated/G | 2836 | `76e4b538483e36f3dbbc2690b7c2406bbed8d826c92acb329d898d5a313ec9e3` |
| `audit_runs/20261019-impact-fix/controlled_replay.py` | Generated/G | 3478 | `d065cf5575f989f7e66875b41e82622804a246e368910e674635eddcf7b92895` |
| `audit_runs/20261019-impact-fix/controlled-baseline-routed/.agent_experiment.jsonl` | Generated/G | 28400 | `7f14790b87f050594b10a1f43c2373435e77deffec411801ec910da0c748db97` |
| `audit_runs/20261019-impact-fix/controlled-baseline-routed/.agent_runs/20261019T070259-88ba0efc.jsonl` | Generated/G | 10576 | `be2c9069c9780707095520da2b77bb2b87af733867fb4d5caea0c37164b8f813` |
| `audit_runs/20261019-impact-fix/controlled-baseline-routed/.hivo/memory.sqlite3` | Generated/G | 143360 | `25b416a24078dfb9dbc124a59ceadd3f2b30e0056d05a566481779390b699c6a` |
| `audit_runs/20261019-impact-fix/controlled-baseline-routed/.hivo/memory.sqlite3-shm` | Generated/G | 32768 | `fd4c9fda9cd3f9ae7c962b0ddf37232294d55580e1aa165aa06129b8549389eb` |
| `audit_runs/20261019-impact-fix/controlled-baseline-routed/.hivo/memory.sqlite3-wal` | Generated/G | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `audit_runs/20261019-impact-fix/controlled-baseline-routed/welcone.txt` | Generated/G | 7 | `280d44ab1e9f79b5cce2dd4f58f5fe91f0fbacdac9f7447dffc318ceb79f2d02` |
| `audit_runs/20261019-impact-fix/controlled-baseline-verified/.agent_runs/20261019T065917-8cd25e0d.jsonl` | Generated/G | 9807 | `c38ccc707fdce28544ed094ee4f42616f1e65f627d7de2c02f8c46f63a282da1` |
| `audit_runs/20261019-impact-fix/controlled-baseline-verified/.hivo/memory.sqlite3` | Generated/G | 139264 | `992beaf2fc89177b49e5dbe8187f30456baca8481627a136ef14231b6e627207` |
| `audit_runs/20261019-impact-fix/controlled-baseline-verified/.hivo/memory.sqlite3-shm` | Generated/G | 32768 | `fd4c9fda9cd3f9ae7c962b0ddf37232294d55580e1aa165aa06129b8549389eb` |
| `audit_runs/20261019-impact-fix/controlled-baseline-verified/.hivo/memory.sqlite3-wal` | Generated/G | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `audit_runs/20261019-impact-fix/controlled-baseline-verified/welcone.txt` | Generated/G | 7 | `280d44ab1e9f79b5cce2dd4f58f5fe91f0fbacdac9f7447dffc318ceb79f2d02` |
| `audit_runs/20261019-impact-fix/controlled-baseline/.agent_runs/20261019T065900-91f2fa0a.jsonl` | Generated/G | 5342 | `a6c70b2220f623dc124b07dd153532d644aabbf23afd4b1bec7daecdfdd26f9f` |
| `audit_runs/20261019-impact-fix/controlled-baseline/.hivo/memory.sqlite3` | Generated/G | 139264 | `420585e30d2b2f2f8310154e43e1b7197a6ad91e5291ab4e7d48c54123380acd` |
| `audit_runs/20261019-impact-fix/controlled-baseline/welcone.txt` | Generated/G | 7 | `280d44ab1e9f79b5cce2dd4f58f5fe91f0fbacdac9f7447dffc318ceb79f2d02` |
| `audit_runs/20261019-impact-fix/controlled-final-result.json` | Generated/G | 10292 | `ef1c7df15e5390f236c34d3e4501e5be244236d4924566d4381993e77abf3776` |
| `audit_runs/20261019-impact-fix/controlled-final.log` | Generated/G | 37270 | `6f962bdd4e02ab0779b4e5da6d988ddfdc48495d1867316027935a806692149c` |
| `audit_runs/20261019-impact-fix/controlled-final/.agent_experiment.jsonl` | Generated/G | 28390 | `84ca02d38db1b6efa4d4ca2ae2dee31dac33e15e3db739131c966e8ac8403e82` |
| `audit_runs/20261019-impact-fix/controlled-final/.agent_runs/20261019T071642-a38faf6a.jsonl` | Generated/G | 10566 | `09a69c1971ea543fc15f41d3b52f15751e50f7c0de9954e973c01ee9194609d7` |
| `audit_runs/20261019-impact-fix/controlled-final/.hivo/memory.sqlite3` | Generated/G | 143360 | `a54aae44bd296b35a72ed4649a01fcf6a16bed2df190375478f550316f13086a` |
| `audit_runs/20261019-impact-fix/controlled-final/welcone.txt` | Generated/G | 7 | `280d44ab1e9f79b5cce2dd4f58f5fe91f0fbacdac9f7447dffc318ceb79f2d02` |
| `audit_runs/20261019-impact-fix/controlled-replay-result.json` | Generated/G | 4291 | `70d495e0e6d3dfa9e8e3301014cbc94b81fe22ca97c7023a60cb18363632826f` |
| `audit_runs/20261019-impact-fix/controlled-replay-routed.log` | Generated/G | 31269 | `8662be07657b7f59e421b07fb31d315cd432a90dd422eda82c50f9f7f9239cf7` |
| `audit_runs/20261019-impact-fix/controlled-replay-verified.log` | Generated/G | 2519 | `0e5e694406894ca86e4567cecc4ae6d8622f7375aa7040278f35a5c4afd41ced` |
| `audit_runs/20261019-impact-fix/controlled-replay.log` | Generated/G | 2268 | `12b4359a3ad47daa6ab2404a8eaa73d9c9d0c2277ded129c8b589a34bce58abb` |
| `audit_runs/20261019-impact-fix/evidence-sha256.json` | Generated/G | 8202 | `a8ed606d01d4145e69352d2e47339dceeefb8039da0f03a01f2fd932666bafe5` |
| `audit_runs/20261019-impact-fix/experiments-final.log` | Generated/G | 24378 | `c740ee2b023195e281c35525561f0eefbc45185efd02b2f8052a1e8e2ae07678` |
| `audit_runs/20261019-impact-fix/final-source-integrity.json` | Generated/G | 454 | `551d0c0dba7ddb8d8ce77ad8288b272bbbf488e5f2e9aa510b34ac41f72774b3` |
| `audit_runs/20261019-impact-fix/full-regression-console.log` | Generated/G | 48914 | `c50d7d2ca7fbdc9f37a23bc1e36b4bae8144621b30f90849aeebb1768bc6baea` |
| `audit_runs/20261019-impact-fix/full-regression-result.json` | Generated/G | 12710 | `a365b12a252bc7caa04a10251bcf49a581c73982d8e167ab84a68ac1cd9d0273` |
| `audit_runs/20261019-impact-fix/full-regression.log` | Generated/G | 311553 | `daf8cfaee5006fb7c9755a321a1cdc6fc8c3352de046dc1298c4f9d17c02d474` |
| `audit_runs/20261019-impact-fix/greenfield-complete.log` | Generated/G | 4061 | `b350087697d45a1469ba5a00b54cb3d6fd3d58539b8c945f97e30d4d463072f3` |
| `audit_runs/20261019-impact-fix/greenfield-final-verified.log` | Generated/G | 3861 | `2a2eabfdacbcc1d10e77bdb7758a6eb465010182bce6ecbfd555170a2814384d` |
| `audit_runs/20261019-impact-fix/greenfield-final.log` | Generated/G | 3347 | `603b8948fa25fe248f96c1a7126a797953c74051b2ddc386329a8fe836afd438` |
| `audit_runs/20261019-impact-fix/greenfield-handoff-final.log` | Generated/G | 3861 | `3c3907c8c728ac0fa9f6386250fbe730814daa5a5dd18f8228811b88f89e496d` |
| `audit_runs/20261019-impact-fix/greenfield-regression.log` | Generated/G | 3347 | `ad3725f4c7928812c89b4f32f66a8b349695d86c433c2e700480f1c6d9ff306b` |
| `audit_runs/20261019-impact-fix/greenfield-routing-complete.log` | Generated/G | 4434 | `ef722a5aa43e4a80de12d70a11b7b3113cc8954bb31944074181780d267c0cb4` |
| `audit_runs/20261019-impact-fix/historical-specification-events.json` | Generated/G | 2 | `4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945` |
| `audit_runs/20261019-impact-fix/impact-final.log` | Generated/G | 5528 | `d8072e7ecc005ee1e9de42e2b89ff86e1a16775654254bac8a7ceb8b9c905183` |
| `audit_runs/20261019-impact-fix/impact-regression.log` | Generated/G | 5528 | `a745ea63ca7e5b6aba23d7f5cebd390a8dfcd8e0eee41f3e33023136b3f5ed3f` |
| `audit_runs/20261019-impact-fix/implementation-locations.json` | Generated/G | 995 | `1fce7390d8d2b876dd1d2a2d0e27c44a6f7e855f5b75e18e172b9b38d7420b56` |
| `audit_runs/20261019-impact-fix/live-auto-final-exit.txt` | Generated/G | 3 | `13bf7b3039c63bf5a50491fa3cfd8eb4e699d1ba1436315aef9cbe5711530354` |
| `audit_runs/20261019-impact-fix/live-auto-final.log` | Generated/G | 23342 | `75bb2e86ffc1029ff17bf09e62ea1b7358f4eb8273bed80757bf489f08186848` |
| `audit_runs/20261019-impact-fix/live-auto-final/.agent_experiment.jsonl` | Generated/G | 22134 | `5d4e302b7a29ef129551e8146f27f0f052f4e36fd347b65a80a2fff9bea6e9d6` |
| `audit_runs/20261019-impact-fix/live-auto-final/.agent_host_preflight.json` | Generated/G | 2566 | `8141abd4ace89437498001c0e3c070f167830ea455b00bc941a38acb27d2e843` |
| `audit_runs/20261019-impact-fix/live-auto-final/.agent_runs/20261019T065255-5928c8e3.jsonl` | Generated/G | 2890 | `ed147499a8aa40cef6fd0d2877a3a796541177e3541cb8afe469891939d4f13d` |
| `audit_runs/20261019-impact-fix/live-auto-final/.hivo/memory.sqlite3` | Generated/G | 135168 | `cde222b7ca73c11d6cd077227bf3db7fd15e031918589d2e349e9e6e656eec3e` |
| `audit_runs/20261019-impact-fix/live-auto-interrupted.json` | Generated/G | 446 | `70535d829cb532a8eff37d85308e703f9667df98fe09d0b27da400398b2b7fa4` |
| `audit_runs/20261019-impact-fix/live-auto.log` | Generated/G | 4682 | `1906584d844e312ae50ab5536bf02eee274d2d072ffa19b9e43359891f782c95` |
| `audit_runs/20261019-impact-fix/live-auto/.agent_host_preflight.json` | Generated/G | 2567 | `6a32c9760006651b58b2a64a5c8e3f7bbe43def50b930561143f7886e6161fd3` |
| `audit_runs/20261019-impact-fix/live-auto/.agent_runs/20261019T063924-418790a4.jsonl` | Generated/G | 28244 | `7c84876fb9bcfe843f2de7aea93080edfb4db9acdb90400eff029b380c0e4a53` |
| `audit_runs/20261019-impact-fix/live-auto/.hivo/memory.sqlite3` | Generated/G | 147456 | `c3c8fe1b5d77432643f70abbdd958b347f2dff41cd18f7e027961a36aa071933` |
| `audit_runs/20261019-impact-fix/live-baseline-exit.txt` | Generated/G | 3 | `df4e26a04a444901b95afef44e4a96cfae34690fff2ad2c66389c70079cdff2b` |
| `audit_runs/20261019-impact-fix/live-baseline.log` | Generated/G | 553 | `4b7e2a6710b271543d3191dc5f6ac155dd4024aad08bc5742299d9069fccfc1d` |
| `audit_runs/20261019-impact-fix/live-baseline/.agent_host_preflight.json` | Generated/G | 1492 | `eb6f9cdbd09c95ea62089ab5deb51a5eb385109c20c4c60dd2045f076f1a3cda` |
| `audit_runs/20261019-impact-fix/live-request.txt` | Generated/G | 60 | `52a075b4509b5051e110825492d71b3aebb6780eb835a76fd4fb9b69a30c65d3` |
| `audit_runs/20261019-impact-fix/live-results-summary.json` | Generated/G | 871 | `058b124b31f94d9e330bf9231900a0b950d55b08654dbfd99de9342b3c744097` |
| `audit_runs/20261019-impact-fix/native-proof-recheck.json` | Generated/G | 686 | `3899fdc38b6bfb17b9c218404eb9ed0729bb16ff16d63fd616dd89f1e4267f3c` |
| `audit_runs/20261019-impact-fix/new-tests-first.log` | Generated/G | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `audit_runs/20261019-impact-fix/new-tests-fourth.log` | Generated/G | 2586 | `b50d051b08eda0a68e6f7a00dc09bb0ad9ce6293b335c39a3fa0eec71f6bef74` |
| `audit_runs/20261019-impact-fix/new-tests-second.log` | Generated/G | 6618 | `e235ec7ac59a340558f1b4e3042742c0e88c5c17deb0625d4eb42b74f01ead3c` |
| `audit_runs/20261019-impact-fix/new-tests-third.log` | Generated/G | 5618 | `6d8a13fa6e02b7d1b8ed0f21a2167db72d761be50f6be273ea939626fafbb3ad` |
| `audit_runs/20261019-impact-fix/raw-source-check.json` | Generated/G | 106 | `33082fed911aebc582a4764d989a663cd133f852d7add215a02c61666fa1c31d` |
| `audit_runs/20261019-impact-fix/raw-source-check/.agent_runs/20261019T071723-906594f8.jsonl` | Generated/G | 802 | `f10d17191486f27f19e8b5dc83832c6aaf88503887734c0ba0a9da24c3b3e6bf` |
| `audit_runs/20261019-impact-fix/reentry-before.log` | Generated/G | 5224 | `a3572ebe03633609e8c2b57f3c1aeb032a5ae4c0926e81704f20264d8f94af4a` |
| `audit_runs/20261019-impact-fix/regression-comparison.json` | Generated/G | 159 | `b92f8b54327692b50a59ffd5dafb295d448fdd722ba9703338d582ebe65db114` |
| `audit_runs/20261019-impact-fix/reproduce_before.py` | Generated/G | 1954 | `b709bc8a931144a7224a5f73adef47b55afb9b70fb51b5d77868b0ada8544cca` |
| `audit_runs/20261019-impact-fix/ROOT-CAUSE-REPORT.md` | Generated/G | 14216 | `d5cafac1a6d9c1eedf864c8898bea4aa24786829a1f40ef523c775f8c0971d3e` |
| `audit_runs/20261019-impact-fix/test-results-final.json` | Generated/G | 3285 | `b4350ab583671ed3e1f7d0462bfef4e2edfa46fe7c71fdaf222dfae3e916982a` |
| `audit_runs/20261019-impact-fix/test-results.json` | Generated/G | 1419 | `c1a8bd22ba0ccbbdd1b89b0343aec66759a6033a4790c2c92bd669a740e7181c` |
| `audit_runs/20261019-impact-fix/understanding-final.log` | Generated/G | 6586 | `3f5e8db35fab8e704379d91574dd1e49525ed2921d4a7efa9893f5be929d9b87` |
| `audit_runs/20261019-phase2/authority-unsandboxed.log` | Generated/G | 24089 | `aa472afa5defdd91092fa42a4b00425dc90acd8a9ce28e9d0967c38cb358df22` |
| `audit_runs/20261019-phase2/authority.log` | Generated/G | 60198 | `5adffd42b4bb609d002712a7241cadf57d724ab90317aa3473bcb1a7711ad0f4` |
| `audit_runs/20261019-phase2/browser-runtime.json` | Generated/G | 4715 | `4de36a0aee72fde598d14e256022d8e9a1cd065f557789d266f0db9128c38630` |
| `audit_runs/20261019-phase2/context.log` | Generated/G | 1973 | `050061fd0dc144c670ec379605e601e727933a35ea30fed4c1a30c6ce4bc66ca` |
| `audit_runs/20261019-phase2/evidence-sha256.json` | Generated/G | 5708 | `b1d9a6b3ebf89293e588efd7ab994bc616cf67f350b6b88d1ac1c2957aa3be41` |
| `audit_runs/20261019-phase2/execution-summary.json` | Generated/G | 2155 | `99f709d136ed81cbba713dfc6823faed5665878cd8741e43617934179faf2c3c` |
| `audit_runs/20261019-phase2/experiment12-node-pilot-exit.txt` | Generated/G | 3 | `13bf7b3039c63bf5a50491fa3cfd8eb4e699d1ba1436315aef9cbe5711530354` |
| `audit_runs/20261019-phase2/experiment12-node-pilot.log` | Generated/G | 52274 | `e9be3fd8b2d3ed673d930dd7d7a25800c7ff88750b08b8bd7df11e008585e283` |
| `audit_runs/20261019-phase2/experiment12-preregister.log` | Generated/G | 40 | `566634265c9da3db01a14a103f2dc8a9c27f3f9c368ce9a2ab9d4a29666e61ed` |
| `audit_runs/20261019-phase2/experiment12-suite/arena_arrow/authority.json` | Generated/G | 12775 | `b411ec3bd9012833ff4ea123b14fe81188ce4beb2e2a4cb03560d68eb466c8fe` |
| `audit_runs/20261019-phase2/experiment12-suite/arena_arrow/seed/arena.html` | Generated/G | 1229 | `929093c174dbbc7639b64ad71750bd75032d1e9e0f19d7b99f2c85ffebe53566` |
| `audit_runs/20261019-phase2/experiment12-suite/arena_q_restart/authority.json` | Generated/G | 12359 | `83061a9a744a82b3762b97b2f35e3c34afcafec4fd88314d58e72577b228e89c` |
| `audit_runs/20261019-phase2/experiment12-suite/arena_q_restart/seed/arena.html` | Generated/G | 1227 | `8bb33333e43d5611abfc915be87a7e25a4d2952e3aed0d45f4d8eddb2f063a3a` |
| `audit_runs/20261019-phase2/experiment12-suite/manifest.json` | Generated/G | 6383 | `3c80ee8fcabac322060f1e342efc7732aa1091e3a2918fe814b220de7b5ce23d` |
| `audit_runs/20261019-phase2/experiment12-suite/node_unique/authority.json` | Generated/G | 15045 | `e4a757fd4ecd5bd70feecdf1abf50a0f5e54ac722da477eaf8efae8a857c4405` |
| `audit_runs/20261019-phase2/experiment12-suite/node_unique/current-1-observations.json` | Generated/G | 2 | `4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945` |
| `audit_runs/20261019-phase2/experiment12-suite/node_unique/current-1-result.json` | Generated/G | 5041 | `886c41bf22c47af6a78318156aad133426c20c22246ca14ebe0c66b080948e27` |
| `audit_runs/20261019-phase2/experiment12-suite/node_unique/current-1/.agent_experiment.jsonl` | Generated/G | 59796 | `fedcc959566948208e98322e827a2e54d950ade6b56f70f8d52c1a4db0804a8a` |
| `audit_runs/20261019-phase2/experiment12-suite/node_unique/current-1/.agent_host_preflight.json` | Generated/G | 2568 | `11286576f99462be157cd254d3cbea370d788f7e0a93bb7f73c9493129682b72` |
| `audit_runs/20261019-phase2/experiment12-suite/node_unique/current-1/.agent_runs/20261019T054959-87298d45.jsonl` | Generated/G | 10434 | `03dfefce956cc0cd9ae786c0f7e78a9a515eea0426708567a5b4af83f3b06766` |
| `audit_runs/20261019-phase2/experiment12-suite/node_unique/current-1/.hivo/memory.sqlite3` | Generated/G | 135168 | `796bf3a21bfc357c3c64d5938e9b1a3ce38ec297a3809726c497510dbf01bcf8` |
| `audit_runs/20261019-phase2/experiment12-suite/node_unique/current-1/tests/unique.test.js` | Generated/G | 374 | `b98d24271038906c2f606658a6cf42652aeb362f79363f0cad29263a7d3dbe35` |
| `audit_runs/20261019-phase2/experiment12-suite/node_unique/current-1/values.js` | Generated/G | 174 | `6a16886e3d12391032e8d336c2855ea70b45712543617dc871231c0ed40a7908` |
| `audit_runs/20261019-phase2/experiment12-suite/node_unique/seed/tests/unique.test.js` | Generated/G | 374 | `b98d24271038906c2f606658a6cf42652aeb362f79363f0cad29263a7d3dbe35` |
| `audit_runs/20261019-phase2/experiment12-suite/node_unique/seed/values.js` | Generated/G | 174 | `6a16886e3d12391032e8d336c2855ea70b45712543617dc871231c0ed40a7908` |
| `audit_runs/20261019-phase2/experiment12-suite/python_clamp/authority.json` | Generated/G | 15085 | `08ae192b440da922fa00c0de172606c07f0eca60ad94f6488b7a7c64cd180459` |
| `audit_runs/20261019-phase2/experiment12-suite/python_clamp/seed/numbers_api.py` | Generated/G | 216 | `c4cc50eb84c001013791ebe87f5b83f4250ca55eba96e0b2ad43d850b9712a4a` |
| `audit_runs/20261019-phase2/experiment12-suite/python_clamp/seed/tests/test_clamp.py` | Generated/G | 654 | `672a11da462960c302e33922201c41977c6d0181cd4159908c180790f357edcb` |
| `audit_runs/20261019-phase2/experiment12-suite/timer_pause/authority.json` | Generated/G | 13298 | `e7745649d1aa3872575102617824cf6c580b5ead75fa0e863835016a017ff5f6` |
| `audit_runs/20261019-phase2/experiment12-suite/timer_pause/seed/timer.html` | Generated/G | 1034 | `84fa3f7e5ef89445b6628a5d1b4f37501e7f68cfe318c5ea3d28dd5ac67a371d` |
| `audit_runs/20261019-phase2/experiments.log` | Generated/G | 24378 | `cfce1c7723b9f55486616afc8557528d68ce3acf05f35bcbe077df40f20f3821` |
| `audit_runs/20261019-phase2/full-suite.log` | Generated/G | 199165 | `3c83cb21177f7dc376fcedccecd75b4b59c4030c1c5b45e206689e4cc16e1f59` |
| `audit_runs/20261019-phase2/host-preflight-isolated-result.json` | Generated/G | 3218 | `b77ee4a14660075559a1d73f61d2e599edb49581308b0b291872d62709181761` |
| `audit_runs/20261019-phase2/host-preflight-isolated.log` | Generated/G | 251 | `78f30bf344d8ad7f0526408f83480067be20d1c362d2ab0ed56ff58430c1e5af` |
| `audit_runs/20261019-phase2/host-preflight-isolated/.agent_host_preflight.json` | Generated/G | 2570 | `a712f34bfd6da0ec5fbcfec917b172d9aa635c16bbd9e890ec19f3b4b0b91e6d` |
| `audit_runs/20261019-phase2/host-preflight-result.json` | Generated/G | 2765 | `626ee6d898d1935854215e06bd56487ef0f475f0b55f31d40c741216cccf1f06` |
| `audit_runs/20261019-phase2/host-preflight.log` | Generated/G | 357 | `e9e5759e31e5bca2f3eafaa6be2d581646e59df54e86d2bb0f64284676fe68b7` |
| `audit_runs/20261019-phase2/host-preflight/.agent_host_preflight.json` | Generated/G | 2164 | `ea4f8734fb25c6701ba158ee7a5c322f6d5e37fd678998d1463e049aad3de902` |
| `audit_runs/20261019-phase2/model-policy.log` | Generated/G | 709 | `6f11598dfde6915e454c86cbe426d8951a56e856af047902cec9e4b98406fe7e` |
| `audit_runs/20261019-phase2/normal-cli-startup-exit.txt` | Generated/G | 3 | `13bf7b3039c63bf5a50491fa3cfd8eb4e699d1ba1436315aef9cbe5711530354` |
| `audit_runs/20261019-phase2/normal-cli-startup.log` | Generated/G | 521 | `69ae3e2307aab124be43cf74211e2f574a22c43e048051eb2cbcbc3562099656` |
| `audit_runs/20261019-phase2/normal-cli-workspace/.agent_host_preflight.json` | Generated/G | 2569 | `896f743bc686c077982ee0cb34956f51c7cdbacc786513b5f5d7234cf3789b0c` |
| `audit_runs/20261019-phase2/normal-cli-workspace/.hivo/memory.sqlite3` | Generated/G | 135168 | `cde222b7ca73c11d6cd077227bf3db7fd15e031918589d2e349e9e6e656eec3e` |
| `audit_runs/20261019-phase2/PHASE2-REPORT.md` | Generated/G | 9667 | `2616de67f70a294acbebced879403d0934ff4eb93d976e118c09ae5101b39c89` |
| `audit_runs/20261019-phase2/pilot-audit.json` | Generated/G | 539 | `dc6b8156b925dcd4ee59840c5af33394c888148967a154d42e39b14773962818` |
| `audit_runs/20261019-phase2/production-integrity-final.json` | Generated/G | 556 | `22f44c19adff834e0d129b17619895f0c6823fa0d1b5e3f96c30a7eb19dbaeeb` |
| `audit_runs/20261019-phase2/production-integrity.json` | Generated/G | 459 | `71f9da56fbaf0fed17bc99200a3879c280ef575c64d192f0c654c8ff1f7f729d` |
| `audit_runs/20261019-phase2/regression-console.log` | Generated/G | 47956 | `8b4f3ccfaaa9df6620b6bdb1a46c3e784045195700c315920bd9e4c6c3bc1edf` |
| `audit_runs/20261019-phase2/regression-excluding-live-test.log` | Generated/G | 308715 | `b0f9553c2fcae13b4056e8b13f9459775a7ed66432b1b442966ee000fc1ac430` |
| `audit_runs/20261019-phase2/regression-failure-index.json` | Generated/G | 17215 | `d63b7a9738f7d6c9e2052d321d5f624b7d9910d132548a17d1361d06ac1ffc90` |
| `audit_runs/20261019-phase2/regression-result.json` | Generated/G | 325 | `b6c0b4257064e2f8afec76c05e1f2c2d57f25a069995a30dad48b3c0867fc60d` |
| `audit_runs/20261019-phase2/test-executions.json` | Generated/G | 1069 | `a9abc3df811c8f009ee0d9132903b29a1e83c215cb49ccfa3d2f6f608f1d35b5` |
| `docs/EXPERIMENT_HISTORY.md` | Retained historical document/result/B | 2467 | `9961aaf49d3935d221e54b151f25c0ad2eced8fd26fd13f41ec93e79ffad7ed0` |
| `docs/PROJECT_STATUS.md` | Retained historical document/result/B | 4718 | `09a5bed72941acd8045114119767bfecc1c10164c6e3293d51ced7f3e386251f` |
| `hivo/__init__.py` | Present; origin unresolved/C | 22698 | `af399745bf3808adae415834f1a266e07400bbbe700b0f4c348ca196edbcfc4c` |
| `hivo/approval_authority.py` | Present; origin unresolved/C | 107312 | `6825d339c3bbbc78996732e3954971cffcf5b2943713069172fd979df8436e7e` |
| `hivo/approval_bound_execution.py` | Present; origin unresolved/C | 77887 | `2de7a14ce600f7639b99511340c1dc4045e2eb59d67e7c023459ccdee0d614a3` |
| `hivo/atomic_child_receipt.py` | Present; origin unresolved/C | 10920 | `21e9c0e197f00469da57e6f4c7a950698ed0111269fb4a0aaebf70202e3493bd` |
| `hivo/browser_checks.py` | Present; origin unresolved/C | 15329 | `b8be20dfe8078f5c43a84c3c329e1a7a6fc83a287cbeae4272d772c315bb889b` |
| `hivo/change_impact.py` | Present; origin unresolved/C | 12480 | `3907816fc5207b156b8487ca9c8bd02c7fc639114d9190de20d6dcba9a7a350e` |
| `hivo/child_handoff_diagnostics.py` | Present; origin unresolved/C | 6084 | `958c2c7f71f05e8b5720ce4048b92e769c0d313bb83875582de3564697a7cb9e` |
| `hivo/context_sufficiency.py` | Present; origin unresolved/C | 49649 | `114025917bae6fa3e692809f9e9c1ef721334e75d3e8dd02bfd9706b48ed4e28` |
| `hivo/context.py` | Present; origin unresolved/C | 5098 | `4e48797d74a123b191d16c158569d877c63468bc0b2684775adac296c79f57a7` |
| `hivo/core_execution.py` | Present; origin unresolved/C | 20006 | `ffdf8a8957c4f5891b1ada859fc80c68ee550f50ae84b6db5379e752dd7586e1` |
| `hivo/core_orchestrator.py` | Present; origin unresolved/C | 76025 | `4809ccdec5d08065b99a11bcfb6a67d75fb3d47e0267a190eaffb6b61408808f` |
| `hivo/coverage_evidence.py` | Present; origin unresolved/C | 10930 | `f6908a7b757fdc76509caf1145fd0c2599846a9dcb0198a1cf7386cd2dc33d2c` |
| `hivo/decomposition_first.py` | Present; origin unresolved/C | 9590 | `04ae02ebabf5149c694fc03fb40bf4abf6b95616c3797e56f42ba4ed03337bcf` |
| `hivo/diagnostic_hypotheses.py` | Present; origin unresolved/C | 20852 | `516c199a0b6e70eddf526d8b75f1319a1b58c40d022ba8292f6dc3b6164aebe3` |
| `hivo/evidence_compatibility.py` | Present; origin unresolved/C | 7277 | `9b1614721414c6326b6828053ac1cdbfd4ce9474a75f61640af5d120fd5ec67a` |
| `hivo/evidence_monotonic.py` | Present; origin unresolved/C | 5930 | `2525c66cc0fa5cf74b70a1eb1eb8d39784b985522c3826485c1213a7bf4312c2` |
| `hivo/evidence_strict.py` | Present; origin unresolved/C | 7923 | `aefb9e8168a1d6a83bfd930894f6bc9b0f0c22d753279f7a9872c838601cfcc8` |
| `hivo/evidence.py` | Present; origin unresolved/C | 5658 | `99ab1cc91210b65f69aac2391e289094cf3e94ffeae8a6aa7d03118330b5f6c2` |
| `hivo/execution_contracts.py` | Present; origin unresolved/C | 230369 | `a61a8511e8072757fe84a61eac04b58defa0bee2a4c78ef253ed7c42902b659a` |
| `hivo/execution_invariants.py` | Present; origin unresolved/C | 103777 | `372defeb9cb287d0e9d4bd5bf361ff88f307451918c2d6900ba2f3f3e8c21364` |
| `hivo/experiment_sandbox.py` | Present; origin unresolved/C | 19332 | `77f5d29e911ef2e21eeda864aa431e238b76aa158a7ac441babcaac63503472c` |
| `hivo/experiment_selector.py` | Present; origin unresolved/C | 10010 | `4eb4a01bd3fae1d21db7abd7973e8b90996dcd606357e50b22d2c1a06238338e` |
| `hivo/experimental_evidence.py` | Present; origin unresolved/C | 49687 | `68df38fe96a621ed47afca2da14e77a641b9e79522bd7df8ce70c049bcf1f566` |
| `hivo/fault_localization.py` | Present; origin unresolved/C | 104232 | `4c0bbfb5d33c3dc457581c2597276674de0fc2531c41fc3fb931e71902437338` |
| `hivo/fault_ranking.py` | Present; origin unresolved/C | 505 | `17907d36011d3605d58d4e79876999c3bc485b2a1cc7133dcc7b0cfc98738f57` |
| `hivo/generation_checkpoint.py` | Present; origin unresolved/C | 8187 | `a47f5581c2ab07c839809b92aba52cf40d9904d5a514c6636b14f152cfd53f6e` |
| `hivo/generation_dag.py` | Present; origin unresolved/C | 17045 | `0cb395ffb0b668067734f25a46a95750a272f410278573fcafcca98ed17165e3` |
| `hivo/generation_units.py` | Present; origin unresolved/C | 21950 | `33e4d39670b9503ae591d61c4abf5f4f88594c0fbbe83d8b8b759533bef95ddf` |
| `hivo/host_preflight.py` | Present; origin unresolved/C | 27328 | `60cce7fe6d149c25c582d9224ca1ebf8068192472c05363b2549229765d1c265` |
| `hivo/http_client.py` | Present; origin unresolved/C | 1712 | `71f48b5342e9a93a14c591bf28c57118142d8954e2245048b70e5fb33be5ac75` |
| `hivo/impact_planning.py` | Present; origin unresolved/C | 808094 | `085d19eb3f6fd518a1cec3dc2b47659fbe21a9e32dd168f4cd758afb82d4d4bf` |
| `hivo/integration_gate.py` | Present; origin unresolved/C | 64041 | `ac7698856c747b23f6ad63f971378d15b3cdbc6236ede3958c45c1c38ca010e2` |
| `hivo/integration_targets.py` | Present; origin unresolved/C | 7609 | `e5b8bde6682e162a60c302de798843c25bcdbfc63ea6a26c56146e26332c41a5` |
| `hivo/lexical_index.py` | Present; origin unresolved/C | 12746 | `4a245958688854fabc0c5f967a4905a091e72cebdcd74057e986e70454359976` |
| `hivo/memory.py` | Present; origin unresolved/C | 66589 | `9481c1d8eaa9ec6fe42ea67df809a85aa6bc152712d1bac20bcb1621d78fcd0c` |
| `hivo/model_policy.py` | Present; origin unresolved/C | 2875 | `17f5d0a1a3f1163200a3ab564ef3016fd0b31d009e25540fdd7ed83105cfef66` |
| `hivo/mutation_grounding.py` | Present; origin unresolved/C | 11637 | `11d318d175435ab05115d8c48a02da2b89143769bd71e0bdeea9331b790d4ac7` |
| `hivo/mutation_strategy.py` | Present; origin unresolved/C | 9208 | `b607ea2b0ca12cf23c956e0523104ab6de9643943096a1c1f73e1d668c3fb189` |
| `hivo/patch_candidates.py` | Present; origin unresolved/C | 33344 | `b3931a7c51012a3f75f19e57887e021890afa3b585590e662dd27f12e07c0882` |
| `hivo/patch_search.py` | Present; origin unresolved/C | 44657 | `89b83a94e880378c2d8be8f41f239107cd29e1595f04e45634170d952a94f771` |
| `hivo/playbooks.py` | Present; origin unresolved/C | 7536 | `2ac437dfbff60b9c4b403ecd42676e8f89b4ebe4bab70f84f79697c8476f88d9` |
| `hivo/pre_mutation_impact.py` | Modified/A | 92182 | `15804c02f44586aee7a936c01dcc80643f6697eafb0175024128c03f0b03ec6c` |
| `hivo/precommit_invariant_gate.py` | Present; origin unresolved/C | 728 | `8dcee35e32bef0e66a1f04ab682435365a7b9f46e937c65e05c46785c0f827ca` |
| `hivo/project_blueprint.py` | Present; origin unresolved/C | 22956 | `bcd44faf3fb308d700e2a5e3c05f850e47e16053c0883ad608c746b2c35138ca` |
| `hivo/project_brain_refs.py` | Present; origin unresolved/C | 20642 | `a644e26a6ee85b1db969fdabaaac7812d9e34ceffd55cc6c0336187baca75a83` |
| `hivo/project_builder.py` | Present; origin unresolved/C | 53277 | `426e5d71e1f1455fcfe35f0e7542ed481d965e0cee62747599962ddcc90d9b82` |
| `hivo/project_understanding.py` | Present; origin unresolved/C | 114937 | `1dffb1f654c68d88b8d5a94660f9287f644ebae6508d8077419423757c23b092` |
| `hivo/project_world_model.py` | Present; origin unresolved/C | 56464 | `fe47329c1ca31dbc17350efd019cbec7b01888ad3cc40c8d1fed7edb3c12b509` |
| `hivo/projects.py` | Present; origin unresolved/C | 2900 | `3ee29cfbc2322c7aa89a6986d68b7c7a8d7332fe69786a14ed32e8b8628d0145` |
| `hivo/promotion.py` | Present; origin unresolved/C | 70494 | `35fe6634863d70004aca56b6d156d90be8c5d06ed9730c39e02a31f5af4f276a` |
| `hivo/recovery.py` | Present; origin unresolved/C | 413875 | `4849198c167453952e7263676d2e2124a5c14d09f62e3d961111e42c6572968c` |
| `hivo/reentry.py` | Present; origin unresolved/C | 131429 | `b13d017d0987291438bf63198aaf8b6399fb6fc1d86e7440db1bcd1b8cd0ecb4` |
| `hivo/reference_resolution.py` | Present; origin unresolved/C | 20226 | `5e482243732c9cbcde93522b4dd45b13d5ffba6d3a46bd9790ca5cc456b9b43c` |
| `hivo/repair_problem.py` | Present; origin unresolved/C | 19566 | `797fbebd31af1b440d5a79f8684e3d7eef12f2622c0e7476cb51ef1e3519a2b4` |
| `hivo/repo_intelligence.py` | Present; origin unresolved/C | 46193 | `fb38366f6b2e6fd0879507e090e1eb9f7465d733ef4485b5580cc8c7fac0493a` |
| `hivo/repository_map.py` | Present; origin unresolved/C | 29133 | `5842dde814279529c32e76b74d6c7a38701568d35e70a8d562c49f13c7f93f4f` |
| `hivo/requirements.py` | Modified/A | 49443 | `3845c4958d4f079f276d233d35d8ccdab133067a148c17032901e03ac0ccadf0` |
| `hivo/semantic_coupling.py` | Present; origin unresolved/C | 64192 | `28722afbcd80a69142cf090c6499bf72453f6bee2d74c6bf4457174065f2c4fd` |
| `hivo/semantic_evidence.py` | Present; origin unresolved/C | 61929 | `d17ac36352bf8bb0a204bcf4d7feaec9dc974be2d37d856b50d9465c0127d169` |
| `hivo/target_locator.py` | Present; origin unresolved/C | 7231 | `a24f247899596042c8b777dc5f74cde990a4496f68de14b65d7c5b3bcadc48c3` |
| `hivo/task_working_set.py` | Present; origin unresolved/C | 19913 | `260e30f19edc14a597b742b549fc9116d86b3f1e9a24c2c29a481810ce7f06a9` |
| `hivo/verification_environment.py` | Present; origin unresolved/C | 7011 | `64b50b0589ca4a04acae9200c38f37a1c8ec0becd581c0a9a7ed299da2827f46` |
| `hivo/verification_gap_remediation.py` | Present; origin unresolved/C | 67856 | `b5633f227d0f03dbc74ec0ac894abaab27e296886854aa3925256736f229c9d5` |
| `hivo/verification_obligation_coverage.py` | Present; origin unresolved/C | 63941 | `45c9d6b77d12db8dad0b9846e8202bf950f2594f2fb47fcd35633f1dc4b59bba` |
| `hivo/verification_routing.py` | Modified/A | 109657 | `dbed610dcb219e9ca3aa3458aee73496388019c108024aef2bb3ebcef830f1ce` |
| `hivo/verification_surfaces.py` | Present; origin unresolved/C | 12879 | `6b9e251b8373d00ae3ad94012d967735a0c66efda9b0dbc13a5d9473c96378fd` |
| `hivo/verification.py` | Present; origin unresolved/C | 8771 | `488f845f693120ee02d77a8aa920778b035b265e282b921b7205de8202cc4229` |
| `hivo/verified_planning.py` | Present; origin unresolved/C | 81078 | `0e864b6e0e53c5c4b56d69a16f4cbcf883021e3b49d09440898c45191ea7700b` |
| `hivo/worker_progress.py` | Present; origin unresolved/C | 5624 | `422e1a0bf6a7084765d61b4928cb4ed3eb5db9aeddfa7a014b7d25e1e143fc45` |
| `list/project-1/.agent_experiment.jsonl` | Present; origin unresolved/C | 2581 | `0869bcc886c0174c75e071ed6ac07118f40f0b11f8ef6f415dedb2e0a551aae2` |
| `list/project-1/.agent_memory.json` | Present; origin unresolved/C | 61257 | `968335042ed893c1d34fd64dbc9cdd8906a178eaa05fb6994e1f2c0b376466cf` |
| `list/project-1/index.html` | Present; origin unresolved/C | 31361 | `3d031b1f28499a3bf0fc3f0f5bbac6521476e566373ad22ea75b2ab72293c661` |
| `list/project-2/.agent_host_preflight.json` | Present; origin unresolved/C | 1800 | `9a6afc4d211606e0b0c35521567a02aef54f076eed29a7dc16ffa6f07fa13852` |
| `list/project-3/.agent_experiment.jsonl` | Present; origin unresolved/C | 28912 | `dbf7cae043802012a6b19e7049f20c4dec4a27b57c9cb6e8b91f6822d3e708c4` |
| `list/project-3/.agent_host_preflight.json` | Present; origin unresolved/C | 2570 | `8c5fbe63cf17a9befb7b7cae9f0de97d667badf45813e7d16eeac66f82d07c34` |
| `list/project-3/.agent_runs/20261014T172228-b7b4fe68.jsonl` | Present; origin unresolved/C | 13801 | `286d953f7309ee2a29201a1ad39066931c849965750e88c2774256f1836a5b8a` |
| `list/project-3/.hivo/memory.sqlite3` | Present; origin unresolved/C | 135168 | `953ffd2e0933dd812084987716a21c0b71f6bb752106c756ca6374122d62ce19` |
| `list/project-4/.agent_experiment.jsonl` | Present; origin unresolved/C | 27642 | `5323fcba8fc226a661ee2767fd566fda8c223f039e3b60687c85b892bf9ec906` |
| `list/project-4/.agent_host_preflight.json` | Present; origin unresolved/C | 2566 | `b969d3f5b2b4d98e292d5b813b3a5a19ae6bc39d6852b69dea3e89211598bc6b` |
| `list/project-4/.agent_runs/20261019T061903-f5bb5918.jsonl` | Present; origin unresolved/C | 12792 | `636ab479193bbba08cd9caf8a9b03e0c58451181b009708254f6b5d27506bcf8` |
| `list/project-4/.hivo/memory.sqlite3` | Present; origin unresolved/C | 135168 | `fd12a0e345dd943a8074a9e794f72b600b9907f3a73246f4df3d52c4253af030` |
| `list/project-4/.hivo/memory.sqlite3-shm` | Present; origin unresolved/C | 32768 | `fd4c9fda9cd3f9ae7c962b0ddf37232294d55580e1aa165aa06129b8549389eb` |
| `list/project-4/.hivo/memory.sqlite3-wal` | Present; origin unresolved/C | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `list/project-5/.agent_experiment.jsonl` | Present; origin unresolved/C | 35780 | `344b19755df553bdcb920e1b72f730e162658b0e0c3de24d1ea114210a300ada` |
| `list/project-5/.agent_host_preflight.json` | Present; origin unresolved/C | 2570 | `c735996110955c585ed72ba9202478e63ac0bc69ed61f3ae9101be420659ff8e` |
| `list/project-5/.agent_runs/20261019T073847-95540b26.jsonl` | Present; origin unresolved/C | 63365 | `f6a4a3cb8421d29be6dfc91ef7e0d0574f0621c5b59d8195fd280e5e77b2e22d` |
| `list/project-5/.hivo/memory.sqlite3` | Present; origin unresolved/C | 143360 | `bec9ad7f1d7ddeeadbb6a35f14e9633f0e96090cfb209e82ab7027f617daa513` |
| `mini.py` | Modified/A | 1527467 | `07f08e30def31b9c05ca3574ee21d2582a88f82a612da9c35e6f6862c64f1401` |
| `README.md` | Present; origin unresolved/C | 44424 | `4b43dc22a5d7c8824d79f261755cb8b3b44775d547feeaf41a64e1ddfc785210` |
| `reports/experiment1/combined/report.json` | Retained historical document/result/B | 6401 | `add2f5512f68ebc8b1eeeddd8c6818541c95db79246e43bd9e5a0661f1238d67` |
| `reports/experiment1/combined/report.md` | Retained historical document/result/B | 1274 | `808e1bffdf1b29c7310002bf47af25e40405472683b4458f89258666f59bdfb7` |
| `reports/experiment1/final/report.json` | Retained historical document/result/B | 6818 | `a90397ce35a19021891685481d9b74ae0f0d1c551f564bd73c9c9a2625496294` |
| `reports/experiment1/final/report.md` | Retained historical document/result/B | 1867 | `42cbf18d3b1c1378e277fe44afe986ab2e3ea9c389052d6f5e35c9c838765521` |
| `reports/experiment1/pause_01/report.json` | Retained historical document/result/B | 3055 | `6da3011f56b30bca508d5e818d4e9a341e57ad3729db91d18421423197816742` |
| `reports/experiment1/restart_01/report.json` | Retained historical document/result/B | 2259 | `3ec1e1eb456cccea46bd92542ebea19d16ac5f3849125d3157e02efcf821b842` |
| `reports/experiment1/restart_exec_01/report.json` | Retained historical document/result/B | 4571 | `628b2886d3969c0114b5838e1de91a1a0c9741cd8846e842537fede6d9ccc2f6` |
| `reports/experiment1/restart_exec_01/report.md` | Retained historical document/result/B | 1323 | `ee220fb350caf8049210db631f53a4b0ea3f85abcaf0fae1f2e412b72718ddd1` |
| `reports/experiment10/rkey_01/frozen_handoff/comparison.json` | Retained historical document/result/B | 132708 | `ea3fc4974fae05d82b16c5a00a7600e74f44e10d484a0adbd6f60ff500de6da2` |
| `reports/experiment10/rkey_01/full_handoff/comparison.json` | Retained historical document/result/B | 123307 | `78ae2055dca7f1f6fe66b955d32e6a04f05555a28ff4fdb2eab091a62570580f` |
| `reports/experiment10/rkey_01/historical_report.md` | Retained historical document/result/B | 2321 | `f141fb3a4c295691cd2169e427f1247e5c6d9dacce37f3490ac03ca2f3185357` |
| `reports/experiment10/rkey_01/report.json` | Retained historical document/result/B | 280441 | `de0a8f14a9bdd0b1dd312b30497aaf1d22ecdb434dc0065ce71417513b2f0694` |
| `reports/experiment10/rkey_01/report.md` | Retained historical document/result/B | 3167 | `86b3ebd1ab407825d8dd492c085d42fbbd0cb4b577ac0ad9660bfc81585009bd` |
| `reports/experiment11/rkey_01/frozen-comparison/comparison.json` | Retained historical document/result/B | 116579 | `8bac6df2df8e427fcd94597a378123ef93a75aa6e9ecdd0a5a7192668c16fd9f` |
| `reports/experiment11/rkey_01/frozen-comparison/compatible/comparison.json` | Retained historical document/result/B | 81884 | `1fa63c0862610cc407ead240319c516c2f75bf62bd562541362df872d7203292` |
| `reports/experiment11/rkey_01/frozen-comparison/current/comparison.json` | Retained historical document/result/B | 22475 | `41991bbe4f39ab577685387989efb8db642b17242ac3d8113591859e61f81d68` |
| `reports/experiment11/rkey_01/interim-report.json` | Retained historical document/result/B | 130275 | `9e2365253380ea4c7eae7d558760b7bc7e380815ac96e0a10b9a48866b9d7c22` |
| `reports/experiment11/rkey_01/interim-report.md` | Retained historical document/result/B | 3364 | `8feeb6d732f23e7a8189306ae74134e48249a27374cf5813d965efedca5c32c8` |
| `reports/experiment11/rkey_01/report.json` | Retained historical document/result/B | 134591 | `e190611ea7c0cd225c81b243a8d25d47d4dfafb21cb0573e97f9b164ff782062` |
| `reports/experiment11/rkey_01/report.md` | Retained historical document/result/B | 4482 | `f54d07eaa596dd7d00eadaaa35546fdb8e8b62fb22a49e86b517ff378a7f3397` |
| `reports/experiment12/experiment12-report.md` | Retained historical document/result/B | 6991 | `04898059620f9b1bd26e833376867bda0ff9e8adfe3531d179f08136b6d7f100` |
| `reports/experiment12/experiment12-results.json` | Retained historical document/result/B | 98470 | `5cb43910e9599697acd86487061e9fe1d96d5282c45e93a9d8b8a975a5454945` |
| `reports/experiment12/manifest.json` | Retained historical document/result/B | 6261 | `d3f73d774140aa77a6ffe9f34c5ee8318ccdc5075b4d42a5604039912b7119d5` |
| `reports/experiment12/RUNBOOK.md` | Retained historical document/result/B | 4627 | `ec0e6655ecc930a4f5258ec8e3ed82351719f1a8dcbadd04c1f32351e533091f` |
| `reports/experiment12/supporting/evidence-matrix-v2/matrix.json` | Retained historical document/result/B | 41874 | `6f241560853f12b911f05eb57cf1683d381bfa8d2667a51b9aa3176b24e070fc` |
| `reports/experiment12/supporting/evidence-matrix-v4/matrix.json` | Retained historical document/result/B | 41874 | `7994f3e76675d581d5593a08232f7a036f8774e2869f6f701f689ba695cd275e` |
| `reports/experiment12/supporting/evidence-matrix-v5/matrix.json` | Retained historical document/result/B | 41874 | `7994f3e76675d581d5593a08232f7a036f8774e2869f6f701f689ba695cd275e` |
| `reports/experiment12/supporting/evidence-matrix-v6/matrix.json` | Retained historical document/result/B | 41874 | `7994f3e76675d581d5593a08232f7a036f8774e2869f6f701f689ba695cd275e` |
| `reports/experiment12/supporting/paired-handoffs/arena_arrow/comparison.json` | Retained historical document/result/B | 78732 | `a547c680f0bf6f3be1c74be86f8e0077fbed7412526ced62ae5c3346c67f0c46` |
| `reports/experiment12/supporting/paired-handoffs/arena_q_restart/comparison.json` | Retained historical document/result/B | 100510 | `34a24d4a7bedccd4dd80a3d31becf71e80a786f3b8df0cadf498303e405833e5` |
| `reports/experiment12/supporting/paired-handoffs/comparison.json` | Retained historical document/result/B | 267818 | `e731e61a82dde973b2e051c6646575ee804060da17f9a5d8b50f2df6320294bb` |
| `reports/experiment12/supporting/paired-handoffs/node_unique/comparison.json` | Retained historical document/result/B | 65080 | `cc476d96ab59880ef9786e4195d87fb85f2f8dce5b80141587af9ab5cf61f84b` |
| `reports/experiment13/experiment13-report.md` | Retained historical document/result/B | 4208 | `2898ad25b920ffbf98ec303aa3eead04931d39db645ff444c9ece67f84de55b7` |
| `reports/experiment13/experiment13-results.json` | Retained historical document/result/B | 49094 | `ecb628d3f54dcc1a2396370632bd7b5547f4ded047432fb53531fb5986d890b6` |
| `reports/experiment13/manifest.json` | Retained historical document/result/B | 5124 | `f365b2552f1393bdef6a82b59d5eeeb8469f56997be271f246c878d8a9238c9f` |
| `reports/experiment13/RUNBOOK.md` | Retained historical document/result/B | 3888 | `919789fc0b13d65eb1e7cb4bf80895efc93709fe26364f6d05493a494a2ac72d` |
| `reports/experiment13/supporting/evidence-v1/comparison.json` | Retained historical document/result/B | 31240 | `f7493a6748858ccfa707995bf4000c22df3c50d42a259815823146ab58029318` |
| `reports/experiment13/supporting/handoffs-v1/comparison.json` | Retained historical document/result/B | 17059 | `8eb8e9dfca83e66c345c37565ede8d2e653a1918fde6e59aae010c1e19e8f5d4` |
| `reports/experiment14/experiment14-report.md` | Retained historical document/result/B | 4229 | `7f88575039ad20165d52f164643f6ca743fb67967bb9ebba0b52927167238946` |
| `reports/experiment14/experiment14-results.json` | Retained historical document/result/B | 93044 | `5e5ef9599d3e36354d2626edab5cbf81f1820256ddd63427ecbcd091d0904ded` |
| `reports/experiment14/manifest.json` | Retained historical document/result/B | 5532 | `7a2d4b1ce26de6e2e14ab8db2c290c222f64508acb259f6e9ba7f86985d5ad2b` |
| `reports/experiment14/RUNBOOK.md` | Retained historical document/result/B | 4947 | `2373576986d045be576e87d9add84830dbceb45f6ddedf22795dd7a0269b37fa` |
| `reports/experiment14/supporting/evidence-v1/comparison.json` | Retained historical document/result/B | 45363 | `0d469f1e1d67e05578948536e92daede07ac9be43209e72dff12f9f0171e2069` |
| `reports/experiment14/supporting/evidence-v2/comparison.json` | Retained historical document/result/B | 45363 | `0d469f1e1d67e05578948536e92daede07ac9be43209e72dff12f9f0171e2069` |
| `reports/experiment14/supporting/handoffs-v1/comparison.json` | Retained historical document/result/B | 12516 | `6dbe5cc264670c16c34f6f89345a458e27178aee6e1c52b032a344151c9b0e37` |
| `reports/experiment14/supporting/handoffs-v2/comparison.json` | Retained historical document/result/B | 12036 | `7c7dd4c395b6eddd9129ab3803176788572a71bac7ca4e2dbdd36e650f1e1f43` |
| `reports/experiment15/experiment15-report.md` | Retained historical document/result/B | 4716 | `c353fda397973dbca5d2c0c61e57f0c72106503e5afeec1c94361be4f371980a` |
| `reports/experiment15/experiment15-results.json` | Retained historical document/result/B | 116182 | `6502372e7d9a7987798eb02d93b2b0b59ec444a8df16610203f6198ee2acf5a7` |
| `reports/experiment15/manifest.json` | Retained historical document/result/B | 6556 | `d1955bdc45aef7c0e638a3d2092dbd6d94a0d4b0ce0be2449bda36fbc68e610e` |
| `reports/experiment15/RUNBOOK.md` | Retained historical document/result/B | 5456 | `411b2a1ec3c102a1dc00973c142f478e8e39ea1b7f625be38f452b1721953314` |
| `reports/experiment15/supporting/binding-v1/comparison.json` | Retained historical document/result/B | 263294 | `4c44fa4de00df50808fefca05ad4a38a9ba04fb55ed90a6045284d22b7220d05` |
| `reports/experiment15/supporting/binding-v2/comparison.json` | Retained historical document/result/B | 262646 | `c1f86acfaecb69f7796f2cc6d8c32c4ee46f553031199502553238e7bce7b3e4` |
| `reports/experiment16/experiment16-report.md` | Retained historical document/result/B | 4158 | `4b05579b796c5ad775af38e449b620e53f21d012c3dba714fa78ab0b1efb32d3` |
| `reports/experiment16/experiment16-results.json` | Retained historical document/result/B | 42580 | `e06759e7cf53065456e80553abe3bd96249e42d407c11c3e46a96b4d02573dc9` |
| `reports/experiment16/manifest.json` | Retained historical document/result/B | 3683 | `30549af23782cf17c710e302329127e05213902da69cd90690936df4c595cfc4` |
| `reports/experiment16/RUNBOOK.md` | Retained historical document/result/B | 2707 | `3b8fe8534f382a2c5fda0f869426c8ad8214fe5165bda0b3692e43d2007f7a1f` |
| `reports/experiment17/classification-protocol.json` | Retained historical document/result/B | 3302 | `281869941eea5384f0516f955411482a7e39af301a92dce3f119579e69fb145b` |
| `reports/experiment17/classification-protocol.md` | Retained historical document/result/B | 978 | `8cde8bad8834072b0b5893206234abceffebab7f2e2cdbd57021e1240a28bd9a` |
| `reports/experiment17/RUNBOOK.md` | Retained historical document/result/B | 2360 | `7caa94d1f432b33a7c75a4ad4763f5689af2752f53377a41cb283b6cb5271597` |
| `reports/experiment18/experiment18-findings.json` | Retained historical document/result/B | 7914 | `29d758f606e1f43199f6f964fe96c826df851b60e31337a3391d07557ce0bbd4` |
| `reports/experiment18/experiment18-report.md` | Retained historical document/result/B | 17798 | `b7aebbc9926492b98da6d165b918af1428204b5fd3d3676b041de227500c5b05` |
| `reports/experiment18/EXPERIMENT18B_HANDOFF.md` | Retained historical document/result/B | 15787 | `ba09e7a7230db2a4047394d110bf818aab08b548d6a64f7a9efef49cc973caa6` |
| `reports/experiment18/RESEARCH_HISTORY.md` | Retained historical document/result/B | 25965 | `c32818b23b494e553cff3852474c620d496186e17d55818d50ed8f41c42ef30c` |
| `reports/experiment2/rkey_01/report.json` | Retained historical document/result/B | 1185 | `697fe540a3c9bf35ecf3f04e5d3fdadc50410f6aeb3f07466768d82a0487e1b3` |
| `reports/experiment2/rkey_01/report.md` | Retained historical document/result/B | 921 | `00769193dec0889f4614ea032036900daeed800eb6562e1db860733c25f6ea96` |
| `reports/experiment3/rkey_01/report.json` | Retained historical document/result/B | 2315 | `ea14a2958cf87f16692a48b2e4fdb381df7d04727e39d8cb7077d9eb4d69fdfa` |
| `reports/experiment3/rkey_01/report.md` | Retained historical document/result/B | 1605 | `5eb0937af33ac54dda05fefbd01cafc3fe2f204e996ef8bbe8dcbfaf785cce37` |
| `reports/experiment4/rkey_02/report.json` | Retained historical document/result/B | 1717 | `4129835aeec03fbe1c8d85325b4adc695b3478a7366d5c42e0dbcb7b373133c9` |
| `reports/experiment4/rkey_02/report.md` | Retained historical document/result/B | 1378 | `288243911afabf60e0dbaf78d53a6b4f5f65773f72f2625d275d2252cfaebeb5` |
| `reports/experiment4/rkey_03/report.json` | Retained historical document/result/B | 1838 | `a79ba2ec65f83402456c888441906d38a8e23f086c5d1b23fcccb18c74c41460` |
| `reports/experiment4/rkey_03/report.md` | Retained historical document/result/B | 1468 | `537addc5f5a856e8238859043170fc9e53d71f476db4b1f18cce50c2b24c76a1` |
| `reports/experiment5/rkey_01/report.json` | Retained historical document/result/B | 2218 | `0bdc00e5781d0b3133d224f2a21c15daf1e9bcf7adfd6546c7fa2b1bcf8f560f` |
| `reports/experiment5/rkey_01/report.md` | Retained historical document/result/B | 1603 | `0d008a8c18817b7e942e729af9c367df3560271ab1dbf4b4bcbf5855fd78ffaf` |
| `reports/experiment6/rkey_01/report.json` | Retained historical document/result/B | 4794 | `b95556a070e8cb153ee7e10a106216e67b0ca9202acd7b10f596a9c1400cf7aa` |
| `reports/experiment6/rkey_01/report.md` | Retained historical document/result/B | 1073 | `2c9722a63aec2552ebc11e4c1679e76f633317416f5cb931a9b67a0bf1510de3` |
| `reports/experiment6/rkey_02/report.json` | Retained historical document/result/B | 5788 | `d8c92fb08a0d9a3413c27847d987409ec7ad3d2a5e9f78fc29a4a4af89352d22` |
| `reports/experiment6/rkey_02/report.md` | Retained historical document/result/B | 2004 | `ef11a051bd4e1bf903454611822325f68538cbff5745a5dae10dc08734cdbef1` |
| `reports/experiment7/rkey_01/report.json` | Retained historical document/result/B | 5958 | `08815b08f76fec17098c58b3ba976b34d651f1ae927923abbf14aa7ef4b71900` |
| `reports/experiment7/rkey_01/report.md` | Retained historical document/result/B | 2441 | `4c5d63d12f5e6030eb88abb160ef6c77c82cff0e2a38633e1697e67b404088fa` |
| `reports/experiment8/rkey_01/receipt_replay/comparison.json` | Retained historical document/result/B | 57327 | `7bb5f2bbd2d550b69b0c5b70a206e473c72bbf46eda82ee2b570115b4d6a1606` |
| `reports/experiment8/rkey_01/report.json` | Retained historical document/result/B | 2872 | `abe7ec41d5b573eb46636fd2ac6bd41968e8fad9465c61eb31da12778eca618a` |
| `reports/experiment8/rkey_01/report.md` | Retained historical document/result/B | 1539 | `546bb97229c66f1b2bbc32a5dc307475d0882dc8568695686dacb46395644d18` |
| `reports/experiment9/rkey_01/parent_probe/comparison.json` | Retained historical document/result/B | 20468 | `be6c1f2cf0c3a618b6a3aeef6d5279e8fe033a2f280f5c97ee26c83983b5b7a8` |
| `reports/experiment9/rkey_01/report.json` | Retained historical document/result/B | 5333 | `a621de104ac0705ec43ef952fdc4da56850a24052c4f7373b22c0da4ce7eb9ca` |
| `reports/experiment9/rkey_01/report.md` | Retained historical document/result/B | 2432 | `59f1e986f69c90debc36c422c8fe22d979228d0579392d75d9a66d1e6171aa3a` |
| `reports/experiment9/rkey_01/root_continuation/comparison.json` | Retained historical document/result/B | 20727 | `bf96481a268628239e7a11be13edee22874dd35c3a769598301e336cf82108ff` |
| `reports/INDEX.md` | Retained historical document/result/B | 4772 | `0e296c0372a3208b996ea92870677046819cf86212b24e52feca1c5a0a823106` |
| `requirements.txt` | Present; origin unresolved/C | 61 | `3a398357ad24fb888830f7c4f8df5e693e0674e702f506f57513c91c9c512285` |
| `scripts/experiment1_report.py` | Present; origin unresolved/C | 10937 | `77924652e4025c9b0a53d17925ce56eb98d09ba99fd86b01b132c30eede999d6` |
| `scripts/experiment10_capture.py` | Present; origin unresolved/C | 3690 | `50f1aa3babdc77583f644768a0eac46200fc4e2d967d367cd9dd81b62ba2ddc1` |
| `scripts/experiment10_handoff_probe.py` | Present; origin unresolved/C | 12798 | `ca8fd2bd411ef5c04d74a4fbd5917573e760914ac94717284fde45d5c14d3b09` |
| `scripts/experiment10_report.py` | Present; origin unresolved/C | 8406 | `e4c43c8f5f746cecb6e02f0640b86fa66960b0b439603ad0c923350a9d1429c5` |
| `scripts/experiment11_evidence_probe.py` | Present; origin unresolved/C | 8087 | `5c625ab8572bed386435f45dedf9ff2d04af463f96f227c1a421e518ef63abc9` |
| `scripts/experiment11_report.py` | Present; origin unresolved/C | 11535 | `76cc385435e0893b4eb07268be1c889f135034c80da01807cffc1a54ebf6b729` |
| `scripts/experiment12_evidence_matrix.py` | Present; origin unresolved/C | 11749 | `b65511c0658be3442b6baf508f64d08e3f77b8d9902a1437a3fa58282928c6dd` |
| `scripts/experiment12_fixtures.py` | Present; origin unresolved/C | 6214 | `b436ada90b419c19d5d2398e1ee4cd02fb020fb0930c9102a0373dc1188a479e` |
| `scripts/experiment12_handoff_probe.py` | Present; origin unresolved/C | 6543 | `4bca36fcbb841b2edb88239a0ea299a58eeb4d372100bbeaddbfae245f70c93d` |
| `scripts/experiment12_report.py` | Present; origin unresolved/C | 26725 | `47ebb47b523716192ebf673f3fe4b5982d6c5b71bbe27416f369d1cb7191000a` |
| `scripts/experiment12_run.py` | Present; origin unresolved/C | 14971 | `41a99579bedc0e03e8e868bde9963481cc0486b1fe05c1fe41cd79739b45493a` |
| `scripts/experiment13_evidence_probe.py` | Present; origin unresolved/C | 6265 | `cd26b72c3311f717fa7171b08e9a42338e1611bc00e51597805b7c7edd0a4501` |
| `scripts/experiment13_handoff_probe.py` | Present; origin unresolved/C | 2981 | `9aa640146619a46263520de56378c5d2beef8c49d60533e1bd5ce3e25eada0a2` |
| `scripts/experiment13_report.py` | Present; origin unresolved/C | 8824 | `4064e753973a4ef77cbfce4ca27c697c39a06e63a0494ccfca460af704d997d1` |
| `scripts/experiment13_run.py` | Present; origin unresolved/C | 4431 | `2d260978d84a5ab13112c5edec78e96fe2df6a1b2aa91dec5125dcabf1d23ba4` |
| `scripts/experiment14_evidence_probe.py` | Present; origin unresolved/C | 6449 | `ccef35b902e755f0189e3b9b4f0f1593568ba7405a433d52e360fc8d3c7713ca` |
| `scripts/experiment14_handoff_probe.py` | Present; origin unresolved/C | 2973 | `74923608912043a27a9ae44fe4fb0ef0f1ecc22463f3584df6d1bc5c81ebeee4` |
| `scripts/experiment14_report.py` | Present; origin unresolved/C | 10374 | `53492033b8649331c1a0f4f0b9ce42749eb0d85480b0632873e1fdf757bd37cb` |
| `scripts/experiment14_run.py` | Present; origin unresolved/C | 4564 | `a98335fa76fe38f380670e8aa5a41e5f30c8ff7959830dcb39a5f2328a9e8ccc` |
| `scripts/experiment15_binding_probe.py` | Present; origin unresolved/C | 9178 | `1e065e25f44930a17b310e16c9b1b04b0e2a489bb4ef15b5cbc93f1684fcc4f3` |
| `scripts/experiment15_report.py` | Present; origin unresolved/C | 15201 | `0000f7e9e1ba38fb21af19820517e765bec7bf89f1d4087e8bc0d14d795c8256` |
| `scripts/experiment15_run.py` | Present; origin unresolved/C | 11922 | `c88fb7a8a3b49d9f64a94f6f2af762464c413cb655f8c0a4c6cdda4c943a346a` |
| `scripts/experiment16_report.py` | Present; origin unresolved/C | 18558 | `0e3854d17c854a9826a82a6da77bf63ca72684b53fb92e6b4e11f73bb4d4bc4c` |
| `scripts/experiment16_run.py` | Present; origin unresolved/C | 5999 | `3cd77164666d8ccc7a757b6318d1a3965b6c17cca36115526c86e711cee5621d` |
| `scripts/experiment17_report.py` | Present; origin unresolved/C | 10514 | `8922cfce9d60f21b5b3b37f26417fbf2d839e8e5cfcc3a6511701e08713afcae` |
| `scripts/experiment17_run.py` | Present; origin unresolved/C | 4262 | `7de2455ac56e4f6773f8c061717eb72d7325598516d8bfd56c865d569a47b08a` |
| `scripts/experiment2_report.py` | Present; origin unresolved/C | 5535 | `7ae26814353e74718b9f2f83822b097bbeb14aee3d1b409765822dc85e3f4b7b` |
| `scripts/experiment3_approved_run.py` | Present; origin unresolved/C | 4043 | `41b787245a2fc5f94ca48e6b17311f7227623f85ea8952203b3b1a4c17d67a82` |
| `scripts/experiment3_report.py` | Present; origin unresolved/C | 8004 | `05cc1421e93fda21605e9b831dfd4a997d67a6125004ec8425697f40eb8b5a39` |
| `scripts/experiment4_report.py` | Present; origin unresolved/C | 8203 | `6b940458d1051ab4f9cabf37b29a73594ab306c42bddda434ede73dc26981203` |
| `scripts/experiment5_report.py` | Present; origin unresolved/C | 9527 | `3f89f9cdcb68aac203c310f988c94d8c8b93d553ea9288266edb65776945c1ac` |
| `scripts/experiment6_report.py` | Present; origin unresolved/C | 8151 | `298114818e9f184fabda904016b550d23b44c0d98cbd57b0310fbd8ae39f6a30` |
| `scripts/experiment7_candidate_probe.py` | Present; origin unresolved/C | 2874 | `6762816f6935880244a80c100accff5cb91f8caf59dc25fec0c814002392b721` |
| `scripts/experiment7_report.py` | Present; origin unresolved/C | 8686 | `ca1ce321c1aef9ebd3214665538b01e3a6dc0d54d8b0fe0b9a1c1596f0d8be32` |
| `scripts/experiment8_receipt_replay.py` | Present; origin unresolved/C | 6165 | `eaefea5c9463cf8265bde034faed3bd3ef01e1ed3cff158fa35bd98e7608a377` |
| `scripts/experiment8_report.py` | Present; origin unresolved/C | 7450 | `54d2817ce6e6cc8c027f4b1a23e8e93d5c31e5ee33af51f6e8db8e351a3a9935` |
| `scripts/experiment9_parent_probe.py` | Present; origin unresolved/C | 8114 | `9290b97b7886e9fba93eb0d05ce963cd610bc6dbfe8ecf378c679b0d5910d724` |
| `scripts/experiment9_report.py` | Present; origin unresolved/C | 10645 | `2a840a355df28d558e63a6a1f3d20a54e13c3216cd7bbecfa9cbe6d91af17b9c` |
| `tests/prompts/gemma_staged_web_smoke.txt` | Present; origin unresolved/C | 733 | `717be99ed2a7ae2fdb9af732c9fe35db5ba9a3445c9f065f4e8fbd5f040e4f0a` |
| `tests/test_adaptive_architecture.py` | Present; origin unresolved/C | 148692 | `c080718e235617695fb3997ff001ef0422976c1ac8ed530ad3648df2bdf1032b` |
| `tests/test_authority_drift.py` | Present; origin unresolved/C | 7929 | `a9876c415fb8387e8e1fc6d5ddf5d10b5df69625f2f653b5b71fbd45549c827b` |
| `tests/test_authority_fail_closed.py` | Present; origin unresolved/C | 16722 | `161242ad55319673753e1bcd8c4c72d55895f6fa0962320aaeeb2780ae843f10` |
| `tests/test_browser_checks.py` | Present; origin unresolved/C | 2866 | `61fd0d19eaa08d6872d8a5b04bf7e3dc2a4ef98e5543fa7751d1da009b3a5917` |
| `tests/test_canonical_impact_surfaces.py` | Present; origin unresolved/C | 41647 | `a9c82e37a7bed50a5b19c69fdf3c1420f4ad55badccd4f5d8532319d0cde91f3` |
| `tests/test_context_policy.py` | Present; origin unresolved/C | 2831 | `3c1bf5647e41491713db002dcdbaad9f2d0eff4e17818f0e5c1583e20175fec1` |
| `tests/test_context_sufficiency_gate.py` | Modified/A | 13987 | `ecdc62603c397d072c1e8f8f80fe212cc93912108a97afc2144a324df0444d54` |
| `tests/test_core_integration.py` | Present; origin unresolved/C | 18819 | `b4e7e65725db8fe9ba11d2031e54d7a2c14a5b4dc090266b9ad5b83d9d0b4abb` |
| `tests/test_core1_reference_brain_repo_map.py` | Present; origin unresolved/C | 19482 | `9f39651fbcdcb6a39449af665893f320eb8408413d19ccacb8d444beb1185181` |
| `tests/test_core2_hybrid_repo_intelligence.py` | Present; origin unresolved/C | 17652 | `5b639fa3d57e1712dc46a1f427e5b307963ffdcd8425f44fab571550a435ef02` |
| `tests/test_core3_experimental_evidence.py` | Present; origin unresolved/C | 19157 | `e45ca547726f54d3f215ed49c10365cb9fe9ca04d221f1ceb52276c230656755` |
| `tests/test_core4_fault_localization.py` | Present; origin unresolved/C | 15455 | `834ca3fed476a17c19ebf40f1127f2d45ffa2d7bbda96f6e9e4414bb58a82bb9` |
| `tests/test_core5_patch_candidate_search.py` | Present; origin unresolved/C | 15327 | `5a705d2c06ef05023da0c679f65aeaa2074cdfe3201ed3138bd262b2ffbf4601` |
| `tests/test_core6_large_project_incremental_builder.py` | Present; origin unresolved/C | 23028 | `f84c4e0b9bc6c9caf8aa8b9c2981e3d52532784aab4b15bb3f778330c536ecf1` |
| `tests/test_decomposition_first_experiment.py` | Present; origin unresolved/C | 7462 | `d585d3f6735e1779252d73019f04155aea3cd1e83f74fb37f96ffed9d92ecace` |
| `tests/test_dependency_aware_scheduler.py` | Present; origin unresolved/C | 9978 | `b628ba7a4e364091adae81e2a4837910d47efca476fc50bc3b7f3a2e8fe798b8` |
| `tests/test_evidence_policy.py` | Present; origin unresolved/C | 4256 | `5b8b29d4cb6d60bd5f0b25c146230ff26c8ea0b525351811b14be69df9601c69` |
| `tests/test_execution_contracts.py` | Present; origin unresolved/C | 62423 | `fd16cf2d321eb0a2052c78c23ff2e8eee1e3731a7f2c638705d96f58c6190dbc` |
| `tests/test_experiment1_report.py` | Present; origin unresolved/C | 3154 | `9d6fd4425ee7321d66ca13429701872233a81cc1cfef981f262c65285f9ce800` |
| `tests/test_experiment10_child_handoff.py` | Present; origin unresolved/C | 6055 | `87cac2fb87bf729dec106b5d95dbff86a58b94b096d0f94a23b282d87247c862` |
| `tests/test_experiment11_evidence_compatibility.py` | Present; origin unresolved/C | 9172 | `ecdc07b833afddc7f9504b9ddd1ea1ea0e39d1ec5ff8a7b92e721f55f22431ef` |
| `tests/test_experiment12_harness.py` | Present; origin unresolved/C | 2483 | `040e42fc7abb0c8434f2ab453332e10a9f435a193d31f859e08d1a21278f00fe` |
| `tests/test_experiment12_metrics.py` | Present; origin unresolved/C | 4151 | `92fd0704b3f959eedab1f9004d842b79dbc99d5dcd33d67b4a2bdaed76c92458` |
| `tests/test_experiment13_monotonic.py` | Present; origin unresolved/C | 7433 | `86968a8f52f3c1c17cdbc0969f3fd8de6c05455f2f0244d1bf17f5767f323d94` |
| `tests/test_experiment14_strict.py` | Present; origin unresolved/C | 7146 | `79219fd6437231310eceff456b4716224a5bfa13aef89ba2ad9dc037321564fc` |
| `tests/test_experiment15_evidence_edit.py` | Present; origin unresolved/C | 8385 | `86e01f4c597d57a44228ba6fcfc124ae14dbe5c3e4803ce96444001a9265f4cd` |
| `tests/test_experiment17_field_scoped_profile.py` | Present; origin unresolved/C | 3291 | `7772ba108563abc2e72e84c78e7de48c775a552690ed4b9ed876518c8697c5a3` |
| `tests/test_experiment2_report.py` | Present; origin unresolved/C | 1827 | `012ca74792d6463567d41c44e35b89515697f9e281099bdcf4c10b19b8b5d7d5` |
| `tests/test_experiment3_report.py` | Present; origin unresolved/C | 2169 | `ec37312ae450caaa8c24aa8bb06cf4a0edd928b3006aebf8975629afa980db40` |
| `tests/test_experiment3_worker_progress.py` | Present; origin unresolved/C | 7781 | `966d566145adc99098ec48ca8c46cc755e251df0ac96d2bf12ca36894fcd2278` |
| `tests/test_experiment4_mutation_grounding.py` | Present; origin unresolved/C | 13195 | `13948a5969ec3ff092c9065fca8abeb90cbcc20c3fcea7d88653a2e50cd1a128` |
| `tests/test_experiment4_report.py` | Present; origin unresolved/C | 2660 | `d6ace3b754b5f6a62e9fa006cefc080e3dfbf81b4194ac3dc96d4471fedb3957` |
| `tests/test_experiment5_report.py` | Present; origin unresolved/C | 2927 | `bcdf6a3a1802b7e5ad03b5897d55dcf6159b2022995ad2514308342ee81b6d82` |
| `tests/test_experiment5_target_locator.py` | Present; origin unresolved/C | 5959 | `409e68ce2988c6b07448da591fe7653a0c7d8247aff0151fc81636ca69f36869` |
| `tests/test_experiment6_verification_environment.py` | Present; origin unresolved/C | 7594 | `6e03434d3049842bc27b4ba0a89e819c663197a6a733c1acc0dadf1ab8d60ab8` |
| `tests/test_experiment7_verification_surfaces.py` | Present; origin unresolved/C | 4276 | `27ae3a64637c0d08fa6ffa58899f512b07eb25cc5a435fdb86752a92484b0c0f` |
| `tests/test_experiment8_atomic_child_receipt.py` | Present; origin unresolved/C | 7456 | `7daa0f96f3066d42d14566b1c141f8c966b6e7998f8e66afa657815f4f96537c` |
| `tests/test_experiment9_integration_targets.py` | Present; origin unresolved/C | 10446 | `f3046a95a4bf48c19e6949c6fc5edca8fe97c56171e7dc26770f28bc88de7396` |
| `tests/test_game_artifact.py` | Present; origin unresolved/C | 1473 | `143840746df1405498583e331e90049529dfc3cbf0b5f58cf23b33b27e48e022` |
| `tests/test_greenfield_impact_lifecycle.py` | Added/A | 16699 | `3344e113febe8b12116ca45e1bb447da080807aa22dc82c1d72a128930018704` |
| `tests/test_host_preflight.py` | Present; origin unresolved/C | 16043 | `9a993d0866a1d3ca7b8898ed76060f27e1a4924b7188eb15b87a59c5f0a0d5d4` |
| `tests/test_impact_map_contract.py` | Present; origin unresolved/C | 15995 | `0e786412ea095140cfdf60a38ad1e36c87006f8f3511511f759f3f3bc3df1d75` |
| `tests/test_impact_planning.py` | Present; origin unresolved/C | 40247 | `ae4f9d40584afb57d5d260ac7ce4c9bad0bebb8a04aa47bf757d17c52a3ef36a` |
| `tests/test_long_term_memory.py` | Present; origin unresolved/C | 6947 | `0c03e0b055a0e2e560a60d2644e6e1bdd79eccf8920082d32477921f80336caf` |
| `tests/test_mini.py` | Present; origin unresolved/C | 80735 | `fb6d2e8ef6bdd1f5032331ad3155fc3f6e81927f5bb79e5be30794894db03c8a` |
| `tests/test_model_policy.py` | Present; origin unresolved/C | 1143 | `fd3ee227b294f8ae15624d62b53b2234c6163985e93918e5855c23bebccdf6a2` |
| `tests/test_obligation_aware_plan_closure.py` | Present; origin unresolved/C | 27733 | `1d3d74462852d2b54d6b14fbab20024415bd81ec6bfb269ed5b3b75a6c1d7c93` |
| `tests/test_obligation_conserving_reconciliation.py` | Present; origin unresolved/C | 25470 | `b0579a143b480b8ecd49df22f7dcb355def547ff2bd626e204c2829e85894c42` |
| `tests/test_planning_packet_budget.py` | Present; origin unresolved/C | 12999 | `80c9d3b8505c529ff8ab4410bcba2e77dc182d654943defaaad41b1946e19348` |
| `tests/test_playbooks.py` | Present; origin unresolved/C | 3017 | `718cedf00f9213ce838ad97dfb8c5b124b29da73063a15b6b96ffd651bc85065` |
| `tests/test_pre_mutation_impact.py` | Present; origin unresolved/C | 26897 | `db1577efe19d0faead4468d589379945c836d17075d3e53e27171a7049c48cf5` |
| `tests/test_project_store.py` | Present; origin unresolved/C | 2095 | `5eca1b206e99645e87ce940671a0f6c85535f5f7008ad58a9df25b1f48843c12` |
| `tests/test_project_understanding.py` | Present; origin unresolved/C | 41068 | `e9be59b2654954a3909ac595191e9a2ba58ca13fd9e79de33f26d50092c5da2a` |
| `tests/test_project_world_model.py` | Present; origin unresolved/C | 27697 | `84b3477e45ff2c8b48c0cecc4722ab7c2738d184b639ec79ae8639a8299f1b0b` |
| `tests/test_requirement_clarification.py` | Present; origin unresolved/C | 38933 | `fe58b0e546d851b5402383d1189797da48bb90e797e4b47d6ec9d64253adc74a` |
| `tests/test_semantic_coupling.py` | Present; origin unresolved/C | 36338 | `559633c63e08132d5b512a77c8d6e05ad0a3f29e5907ca49e143c75a6d573e66` |
| `tests/test_semantic_evidence_resolver.py` | Present; origin unresolved/C | 20796 | `e6813e1f0d864899d674b5a1ae3b94336b7a0f78d1839131f6ba34bac04046cf` |
| `tests/test_structural_decomposition.py` | Present; origin unresolved/C | 28519 | `4564c99c174edbdcc59b8686b90154dd90e0fe099e416bcf9e460ab0c915083c` |
| `tests/test_structured_worker_contract.py` | Present; origin unresolved/C | 6387 | `23a6889eb2daded1205206c51d82910c66f1900ead8f2cf786f1fb413d2aefd4` |
| `tests/test_v24_2_canonical_mandatory_core.py` | Present; origin unresolved/C | 16147 | `810f5e100e3bee39ce9d6e8eedf16ca8509a62f7a949b848180911538c1bde90` |
| `tests/test_v24_3_impact_decision_frame.py` | Present; origin unresolved/C | 20584 | `d3544583ee77f95036edc3733ff4ec0639b246a47f078ef50cc27b3282429890` |
| `tests/test_v24_4_2_current_surface_preservation_binding.py` | Present; origin unresolved/C | 42227 | `e206a0361d607c5582ca121bbc040cbc92f1ac7a5e7e817078560c5c20679b97` |
| `tests/test_v24_4_3_decision_relevant_impact_choice_projection.py` | Present; origin unresolved/C | 12934 | `188fc7eca9c59cc6540ee721fcfdea9512da8368d9657109c9d44a4415109f05` |
| `tests/test_v24_4_4_challenger_review_relevant_projection.py` | Present; origin unresolved/C | 18866 | `f5e1e0dff69034ab0641044eb15eef0db2de7555a342e9fe92b3fdd30604420a` |
| `tests/test_v24_4_5_canonical_final_plan_budget_closure.py` | Present; origin unresolved/C | 27230 | `0a0cebc78ca68866c02191c21ff84df58225ca832282d5730f6f558d65585616` |
| `tests/test_v24_4_6_live_equivalent_final_plan_bound_closure.py` | Present; origin unresolved/C | 29105 | `01fb5e76b76009bf277612059ab3c89f09306c11733c4e805e80a42578a55457` |
| `tests/test_v24_4_obligation_anchored_impact_coverage.py` | Present; origin unresolved/C | 39301 | `8da5c4ea82e31b036ec5ddf7bd225f4e890652d76c4c6589e22f0c4dfd846c7e` |
| `tests/test_v25_1_approval_bound_execution_lifecycle.py` | Present; origin unresolved/C | 21508 | `55f1aed9a3579c0f248c94a59f96b2a0cfb77ad34d43ff909634c73a74675f3c` |
| `tests/test_v25_2_worker_execution_invariant_projection.py` | Present; origin unresolved/C | 28883 | `3145902be73df9018486813f0fdd5b34f2058eeb87031ddcc5c8f3b14444546c` |
| `tests/test_v25_3_verification_obligation_coverage_gate.py` | Present; origin unresolved/C | 37738 | `f749815ce187a9773de330d9da3dfb392069a69c18f15d328c92b06df56d3f49` |
| `tests/test_v25_4_1_verification_coverage_artifact_propagation.py` | Present; origin unresolved/C | 24983 | `7925fa493550ba11a6fdeeab11e39faca0410df5154e55a1ab53f283a5d5a78f` |
| `tests/test_v25_4_2_approved_verification_exact_routing.py` | Present; origin unresolved/C | 19219 | `c70634998827400a1120e2a60abe899954f3e1991ddd5faef82ff18c74fafa64` |
| `tests/test_v25_4_verification_complete_plan_revision.py` | Present; origin unresolved/C | 23346 | `85dc31af51eecb46d52182c2700e2385fb88a2cc7785e671165f240092935b66` |
| `tests/test_v25_5_precommit_execution_invariant_gate.py` | Present; origin unresolved/C | 35806 | `60d0c317eedf89776d31488d3acccc9756fc1f2f3253c0acca16158abe2e846e` |
| `tests/test_v25_6_execution_verification_authority_closure.py` | Present; origin unresolved/C | 26038 | `3bb125e826835aa23fbd18a74f40fd66f910d39f907d8d3f9ac73759641963a2` |
| `tests/test_v25_approval_bound_execution_authorization.py` | Present; origin unresolved/C | 15291 | `666e287828df01be9cc27d80d03a63cd6384f8e65a3b495865bcc6605f5a35f2` |
| `tests/test_v26_3_recovery_strategy.py` | Present; origin unresolved/C | 24805 | `a2a2bf2f371ee30d71960ee9b83e65668bd00259b58e97a117b1663bdd813cf5` |
| `tests/test_v26_4_tool_contract_recovery.py` | Present; origin unresolved/C | 31648 | `2f23bc623b5a3dd23c9527c1d9a8b61af69898db8be802f66044d28b82939875` |
| `tests/test_v26_5_preverification_recovery.py` | Present; origin unresolved/C | 26856 | `bb547ff23f5d464c87a7627650d23f451e6c599fcec70b63d80887a0cb896c4c` |
| `tests/test_v26_6_2_active_schema_mutation_intent_reset.py` | Present; origin unresolved/C | 15338 | `7eb565efef54f32c1c5ae8615878f2c2058dc75686b6ebd651a0b0645fd4f3e0` |
| `tests/test_v26_6_no_mutation_recovery_search.py` | Present; origin unresolved/C | 39713 | `ed2265f5eefdcc62cc2ba7e9325713e970913bf688ea43412faee3fc46dbe941` |
| `tests/test_v26_7_progress_aware_completion_recovery.py` | Present; origin unresolved/C | 36207 | `7825c7ff74b5f4b857c7d658a381de08654e2dc35c9bbdaa80ddb403e0207ea0` |
| `tests/test_v26_recovery_foundation.py` | Present; origin unresolved/C | 21642 | `69f3aef3db6c231bcdf1df365bd3419d3c3d39fff85b600441e05f61ab978d57` |
| `tests/test_verification_applicability.py` | Present; origin unresolved/C | 19932 | `7af754f7430a5382479a5d879542c4702512b76ff18287041186800b637f13aa` |
| `tests/test_verification_policy.py` | Present; origin unresolved/C | 7896 | `4b3f23f83d3c8d9831151e50479c6e3b8341c149b7da336b2920469152118da9` |
| `tests/test_verified_child_integration.py` | Present; origin unresolved/C | 21106 | `4ce4f303b74e44b338cc428fecc3f9f6bfba46c39f9e92f8920ba2047e1ee6ce` |
| `tests/test_verified_state_planning.py` | Present; origin unresolved/C | 19593 | `d1a4f94683d1ee9ee3c192678a0edf7db66e1c8f77e9c7152c827b5456068532` |
| `tests/test_verified_state_promotion.py` | Present; origin unresolved/C | 29962 | `73b1a1ee4b47c0c5cd12d023684b44d4cdad0b19eeb1bfd20dcab4999bca10c1` |
| `tests/test_verified_state_reentry.py` | Present; origin unresolved/C | 35202 | `4463cf17bbacbc37026e81a6cdace54bc43d4c7f5f2f4e8cc3ecb9e5756c956f` |

New documentation inventory: updates/R_UPDATE_001.md (added/D); updates/ directory created only if needed. The report itself is intentionally absent from its initial-input hash inventory to avoid circular self-hashing.

## 11. Documentation audit: sources and reconstruction limits

Primary records used:
- audit_runs/20261019-impact-fix/ROOT-CAUSE-REPORT.md, before-reproduction.json, controlled-final-result.json, implementation-locations.json, final-source-integrity.json, native-proof-recheck.json, raw-source-check.json, test-results-final.json, full-regression-result.json, regression-comparison.json and retained logs.
- audit_runs/20261019-phase2/PHASE2-REPORT.md, execution-summary.json, test-executions.json, regression-result.json, production-integrity*.json and experiment12-suite records.
- README.md, docs/PROJECT_STATUS.md, docs/EXPERIMENT_HISTORY.md and reports/INDEX.md.
- Individual experiment narratives/protocol/results, especially Experiment17 classification and Experiment18 findings/handoff/research history.
- Read-only inspection of current implementation, test methods, file declarations, project structure and SHA-256 identities.
- Earlier conversation explains the request and launch attempt; runtime claims rely primarily on retained artifacts, not conversation memory.

No web search or external Git clone was used. There is no local Git history to inspect beyond its confirmed absence. Historical commit strings remain unverified pointers. No full old source means before/after excerpts are behavioral records plus labeled current excerpts, never invented old code. Archived SHA manifests are evidence of recorded checks; this report independently compares current source identities against final replay pins but does not rerun their underlying tests. A hash match does not independently reproduce a successful controller run.

## 12. Final documentation-only preservation check

The final audit compares every initially inventoried path's byte length and SHA-256 with the final filesystem, checks for missing/added paths, and repeats git status --short. Only the new updates/R_UPDATE_001.md is permitted as an added non-cache/environment file. The result is recorded here after writing the report. Source, tests, previous reports, logs, configurations and experiment artifacts must remain byte-identical. This audit does not claim a final Git diff because .git is unavailable.

FINAL_PRESERVATION_RESULT_PENDING

## Appendix A. Exact saved historical command records

These are verbatim JSON records of earlier commands/results, included for reproducibility and provenance. They were read, not executed, by this task.

### audit_runs/20261019-impact-fix/test-results-final.json

~~~json
[
  {
    "label": "greenfield",
    "command": [
      "D:\\ECU\\grade_project\\\u0628\u0627\u0630\u0646 \u0627\u0644\u0644\u0647 \u064a\u0634\u062a\u063a\u0644\\mini_hivo-main (1)\\mini_hivo-main\\.venv\\Scripts\\python.exe",
      "-B",
      "-X",
      "utf8",
      "-m",
      "unittest",
      "discover",
      "-s",
      "tests",
      "-p",
      "test_greenfield_impact_lifecycle.py",
      "-v"
    ],
    "exit_code": 0,
    "seconds": 1.3
  },
  {
    "label": "impact",
    "command": [
      "D:\\ECU\\grade_project\\\u0628\u0627\u0630\u0646 \u0627\u0644\u0644\u0647 \u064a\u0634\u062a\u063a\u0644\\mini_hivo-main (1)\\mini_hivo-main\\.venv\\Scripts\\python.exe",
      "-B",
      "-X",
      "utf8",
      "-m",
      "unittest",
      "discover",
      "-s",
      "tests",
      "-p",
      "test_pre_mutation_impact.py",
      "-v"
    ],
    "exit_code": 0,
    "seconds": 0.81
  },
  {
    "label": "context",
    "command": [
      "D:\\ECU\\grade_project\\\u0628\u0627\u0630\u0646 \u0627\u0644\u0644\u0647 \u064a\u0634\u062a\u063a\u0644\\mini_hivo-main (1)\\mini_hivo-main\\.venv\\Scripts\\python.exe",
      "-B",
      "-X",
      "utf8",
      "-m",
      "unittest",
      "discover",
      "-s",
      "tests",
      "-p",
      "test_context_sufficiency_gate.py",
      "-v"
    ],
    "exit_code": 0,
    "seconds": 0.87
  },
  {
    "label": "authority",
    "command": [
      "D:\\ECU\\grade_project\\\u0628\u0627\u0630\u0646 \u0627\u0644\u0644\u0647 \u064a\u0634\u062a\u063a\u0644\\mini_hivo-main (1)\\mini_hivo-main\\.venv\\Scripts\\python.exe",
      "-B",
      "-X",
      "utf8",
      "-m",
      "unittest",
      "discover",
      "-s",
      "tests",
      "-p",
      "test_authority*.py",
      "-v"
    ],
    "exit_code": 0,
    "seconds": 1.16
  },
  {
    "label": "understanding",
    "command": [
      "D:\\ECU\\grade_project\\\u0628\u0627\u0630\u0646 \u0627\u0644\u0644\u0647 \u064a\u0634\u062a\u063a\u0644\\mini_hivo-main (1)\\mini_hivo-main\\.venv\\Scripts\\python.exe",
      "-B",
      "-X",
      "utf8",
      "-m",
      "unittest",
      "discover",
      "-s",
      "tests",
      "-p",
      "test_project_understanding.py",
      "-v"
    ],
    "exit_code": 0,
    "seconds": 1.26
  },
  {
    "label": "experiments",
    "command": [
      "D:\\ECU\\grade_project\\\u0628\u0627\u0630\u0646 \u0627\u0644\u0644\u0647 \u064a\u0634\u062a\u063a\u0644\\mini_hivo-main (1)\\mini_hivo-main\\.venv\\Scripts\\python.exe",
      "-B",
      "-X",
      "utf8",
      "-m",
      "unittest",
      "discover",
      "-s",
      "tests",
      "-p",
      "test_experiment*.py",
      "-v"
    ],
    "exit_code": 0,
    "seconds": 2.2
  },
  {
    "label": "adaptive",
    "command": [
      "D:\\ECU\\grade_project\\\u0628\u0627\u0630\u0646 \u0627\u0644\u0644\u0647 \u064a\u0634\u062a\u063a\u0644\\mini_hivo-main (1)\\mini_hivo-main\\.venv\\Scripts\\python.exe",
      "-B",
      "-X",
      "utf8",
      "-m",
      "unittest",
      "discover",
      "-s",
      "tests",
      "-p",
      "test_adaptive_architecture.py",
      "-v"
    ],
    "exit_code": 0,
    "seconds": 4.89
  }
]
~~~

### audit_runs/20261019-phase2/execution-summary.json

~~~json
[
  {
    "label": "model-policy",
    "command": ".\\.venv\\Scripts\\python.exe -B -X utf8 -m unittest discover -s tests -p 'test_model_policy.py' -v",
    "test_exit_code": 0,
    "summary": [
      "Ran 4 tests in 0.143s",
      "OK"
    ],
    "sandboxed": true
  },
  {
    "label": "authority",
    "command": ".\\.venv\\Scripts\\python.exe -B -X utf8 -m unittest discover -s tests -p 'test_authority*.py' -v",
    "test_exit_code": 1,
    "summary": [
      "Ran 23 tests in 0.125s",
      "FAILED (errors=23)"
    ],
    "sandboxed": true
  },
  {
    "label": "authority-unsandboxed",
    "command": ".\\.venv\\Scripts\\python.exe -B -X utf8 -m unittest discover -s tests -p 'test_authority*.py' -v",
    "test_exit_code": 0,
    "summary": [
      "Ran 23 tests in 0.549s",
      "OK"
    ],
    "sandboxed": false
  },
  {
    "label": "context",
    "command": ".\\.venv\\Scripts\\python.exe -B -X utf8 -m unittest discover -s tests -p 'test_context_sufficiency_gate.py' -v",
    "test_exit_code": 0,
    "summary": [
      "Ran 9 tests in 0.208s",
      "OK"
    ],
    "sandboxed": false
  },
  {
    "label": "experiments",
    "command": ".\\.venv\\Scripts\\python.exe -B -X utf8 -m unittest discover -s tests -p 'test_experiment*.py' -v",
    "test_exit_code": 0,
    "summary": [
      "Ran 122 tests in 1.246s",
      "OK"
    ],
    "sandboxed": false
  },
  {
    "label": "full-suite",
    "command": ".\\.venv\\Scripts\\python.exe -B -X utf8 -m unittest discover -s tests -p test*.py -v",
    "status": "INTERRUPTED",
    "session_exit_code": 1,
    "reason": "Long-input requirement compaction test invoked live model; no completion claimed"
  },
  {
    "label": "regression-excluding-live-test",
    "test_exit_code": 1,
    "discovered": 1703,
    "excluded": [
      "test_requirement_clarification.RequirementClarificationTests.test_root_brain_prompt_compacts_large_source_side_channel_without_dropping_ids"
    ],
    "tests_run": 1361,
    "failures": 24,
    "errors": 18,
    "skipped": 10,
    "successful": false,
    "elapsed_seconds": 35.85
  }
]
~~~

### audit_runs/20261019-impact-fix/native-proof-recheck.json

~~~json
{
  "checks": {
    "native_proof_accepted": true,
    "observed_file_hash_current": true,
    "generic_pass_rejected": true,
    "missing_actual_sha256_rejected": true,
    "missing_passed_rejected": true,
    "foreign_contract_rejected": true,
    "wrong_digest_rejected": true,
    "contradictory_boolean_rejected": true,
    "contradictory_status_rejected": true,
    "wrong_target_rejected": true,
    "wrong_tool_rejected": true
  },
  "all_passed": true,
  "routing_source_sha256": "dbed610dcb219e9ca3aa3458aee73496388019c108024aef2bb3ebcef830f1ce",
  "proof_origin": "actual Builder run_file result read from controlled replay SQLite events in read-only mode"
}
~~~


