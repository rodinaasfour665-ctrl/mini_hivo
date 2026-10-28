# R_UPDATE_004 — Verification, scoped repair and recursive literal integration

**WIP engineering checkpoint; Level 2 INCOMPLETE.** Investigation and evaluation: 25–28 October 2026. Development baseline: `6f0047ca27e979db10e338357f0fa6a22fe0bf93`. Publication branch: `wip/r-update-004-level2-hardening`. The containing commit is identified by branch history and the publication audit, not a fabricated self-referential hash. This report records bounded engineering improvements with outstanding genuine Recursive Parent/ROOT acceptance.

**Reading this report:** sections 1–15 and their appendices describe the initial 25 October checkpoint; later phases preserve the chronological R_UPDATE_004 investigation. Earlier labels such as current/final source, local-only or publication blocked apply to their recorded checkpoint. **Section U is the current engineering handoff and WIP publication decision**, superseding the prior requirement to withhold publication until genuine ROOT PASS. That authorization changes publication scope, not verification outcomes. Previous update reports are unchanged.

## 1. Executive Overview

R_UPDATE_003 established useful source-ingestion, context-progress and bounded-recovery mechanisms, but its published checkpoint retained a failed parent acceptance test and real classification/verification failures. This update corrects source-grounded classification, carries accepted literal verification evidence across role boundaries, restricts literal Falsifier/Repairer capabilities, and gives a parent a read-only way to integrate genuinely committed child outcomes.

The new 12-case suite passes. The previously failing parent functional suite now passes all four tests without changing its assertions. Eight retained controlled executions reach ROOT completion with exact artifacts: independent counts 1, 2, 3, 4, 5, 8 and 10, plus a dependent three-artifact chain. These use scripted model proposals and a fixture DAG, with real production gates, leaf execution, Falsifier, scheduler, parent integration and transactions.

No final-source genuine Ollama PASS was established. A preliminary baseline qualification failed memory preflight; the final-source inventory replay passed preflight, correctly compiled/classified the task, then timed out in Specifier before Builder. Historical broad-suite debt remains unchanged. No branch, index, commit, remote, PR or R_UPDATE_003 record was changed. All new work remains local.

Current evidence entry point: [CURRENT_REVIEW](../evidence/level2-verification-repair-integration/CURRENT_REVIEW.md). The original [25 October packet](../evidence/level2-verification-repair-integration/README.md) remains a historical checkpoint. Registries distinguish original source hashes, sanitized derivative hashes, controlled results and live failures.

## 2. R_UPDATE_003 Handoff

The checkout started clean on `wip/r-update-003-level2-checkpoint`, tracking the identically named fork branch at the base commit above. `origin` is the team repository; `myfork` is the personal fork. [Draft PR #8](https://github.com/kareem232003/mini_hivo/pull/8) remains the published reference; no GitHub mutation was made.

Historical runs remain historical:

| Run | Established outcome | Boundary |
|---|---|---|
| `20261023T004235-79109aeb` | Genuine two-file baseline PASS | Native reads, Falsifier, impact and transaction; not generalized recursive proof |
| `20261023T005124-a828f3dd` | Recursive failure | Completed context check repeated 28 times; no productive mutation |
| `20261023T002611-991b46bd` | Provider/Specifier failure | Separate from artifact verification |
| `20261023T012433-0023e35a` | Specifier timeout | Request estimated 1,350 context tokens, configured context 4,096, 120-second request boundary; no contemporaneous load/memory attribution |
| `20261023T160330-5a172f42` | Empty project misclassified EXISTING_PROJECT | Three source artifacts; zero task tools |
| `20261023T160636-e485f2be` | Recursive verification failure | Native write succeeded; text run route lost, shell actions refused, helper repairs unauthorized; parent not reached |

The last run recorded 50 model calls, 25 tool calls, one Falsifier call and nine provider timeouts. Retained trace/database inspection supports rollback and no remaining requested non-runtime files in project-21. A present-day empty directory alone would not prove historical rollback. Earlier Reflexion/ProgPrompt/controller research and progress-state repairs remain in R_UPDATE_003; this update neither replaces its history nor claims those mechanisms were newly introduced.

Before edits, nine historical/reference files were hashed and backed up in the ignored local audit directory. These include R_UPDATE_003, AGENTS.md and seven project-21 evidence files, including its SQLite database. Final preservation results are recorded in the manifest. These are nine specifically checked files, not a claim to have independently rehashed every historical experiment ever run.

## 3. Project Classification Investigation

**Problem → observation → evidence.** The exact first project-21 request asks for new artifacts in an empty workspace, but includes “Preserve each filename.” Replaying classification against the stored request reproduces the inconsistency. The subsequent differently worded request does not trigger it. Both exact requests are retained in the preceding checkpoint registry and exercised by the new regression.

**Confirmed cause.** `hivo/project_understanding.py::classify_project_mode` consulted `_MODIFICATION_RE`, which includes `preserve`. A preservation instruction was sufficient to select existing-project semantics without meaningful repository files. There is no need to invoke stale workspace state or model randomness to explain this deterministic result. The executed CLI imports this module; it is not an alternative unused classifier.

**Research search.** Targeted searches covered grounded task routing, language intent versus environmental affordances, and state-aware planning. SayCan [reference C1] separates a language proposal from feasibility grounded in the current world. Its robot value functions do not fit this local filesystem classifier, but the distinction supports explicitly considering source obligations and workspace inventory rather than one keyword.

**Candidates and decision.** A learned classifier adds calls and uncertainty; classifying every empty workspace as new would mishandle requests to fix missing existing code; simply removing `preserve` misses other literal-body action words. The selected deterministic correction removes literal-content spans from intent matching, respects real meaningful files first, recognizes explicit existing-resource actions, and then recognizes parsed source-bound creation obligations.

**Implementation.** `classify_project_mode` uses `literal_requests`, `action_text` and an explicit existing/current/legacy action match. Real meaningful inventory still selects existing-project behavior. An explicit request to modify missing existing resources remains existing/fail-closed. Literal values do not become routing instructions. No mode threshold, model budget or recursive selection policy changed.

**Tests and benefit.** Both historical requests now classify NEW_PROJECT in empty inventory. Reworded creation/preservation cases pass; missing-existing-resource and meaningful-existing-repository negatives pass. Existing project-understanding tests pass 32/32; clarification/session regressions remain separate evidence. The final genuine inventory run also selected NEW_PROJECT with an empty inventory. Ambiguous prose outside the recognized literal grammar is not proven universally classified correctly.

## 4. Behavioral Verification Investigation

**Problem and cause.** The successful child write did not establish usable independent proof. `execute_agent_task` clears active impact state across calls. `falsify_task` previously reconstructed literal scope from that cleared global or a root contract without the accepted child authority. Native `run_file` then fell through executable dispatch for a text artifact. These are controller evidence-lifetime defects; the subsequent unsupported execution/command attempts are downstream symptoms.

**Research search and comparison.** Searches for artifact-bound proof, proof-carrying execution and independently checked evidence led to Necula and Lee's original Proof-Carrying Code report [C2]. Its consumer checks evidence against policy before acceptance. Mini Hivo can adapt evidence binding and independent checking, but its digest checks are not formal proofs of arbitrary programs and its in-process registry is not a signed certificate system. Importing theorem-prover infrastructure would not solve this scoped runtime handoff.

**Selected implementation and complete lineage.** Raw input is compiled to the source ledger and literal byte obligations; child scope derives expected path/digest; a validated impact contract authorizes native mutation after context proof; tools record real effects; native readback hashes current bytes; applicability recognizes the literal route; Falsifier receives a temporary, task-matching copy of accepted verification evidence; evidence gate checks observations; impact comparison checks actual effects; commit precedes child receipt registration. Parent integration independently repeats current observations. A completion sentence is never substituted for a receipt.

`run_file` and `_literal_artifact_verification_paths` accept the scoped verification contract in `ACTIVE_TOOL_CONTRACT`. `falsify_task` validates task identity and accepted scope before installing it, restoring previous state in `finally`. `_falsify_task_body` copies it before the next agent loop clears mutable globals. The existing readback fallback uses actual `run_tool` calls, not fabricated responses. `hivo/verification_routing.py` recognizes accepted read-only literal composition as well as accepted literal mutation contracts.

**Oracle and results.** Tests compare actual UTF-8 bytes and hashes, not text-mode normalized reads. Wrong content, UTF-8 BOM, UTF-16, CRLF instead of LF, extra final newline, missing/wrong filename and post-verification modification are rejected. Current exact bytes pass. Stale/missing/forged child proof cannot authorize parent composition. Parent inspection does not execute arbitrary text or JSON. Applicability tests pass 15/15. This mechanism covers source-bound literal artifacts; it is not a verifier for arbitrary complex applications.

## 5. Falsifier Investigation

**Observed failure.** In project-21 the Falsifier attempted output-redirection shell commands. Existing restrictions refused them. That refusal is a correct safety boundary, not a shell allowlist defect. Advertising capabilities inappropriate to a fully literal verification task encouraged unproductive selection after the evidence handoff had already failed.

**Research search.** Searches on least privilege, complete mediation and safe tool-using verification led to Saltzer and Schroeder [C3]. The paper motivates reducing role capabilities and enforcing the policy on every dispatch. Its principles are not empirical evidence that our controller is secure.

**Alternatives and implementation.** Broadening shell commands would permit a verifier to alter what it claims to verify; removing command/browser tools from every kind of Falsifier would damage executable/web verification. Instead `tools_for_role` restricts an accepted literal-scoped Falsifier to read/list/native readback tools. `run_tool` independently rejects hidden write/command/browser/helper proposals and restricts read/native targets to accepted literal paths. Metadata and unrelated executable inspection cannot be smuggled into that scope. Nonliteral verification retains its existing capabilities and restrictions.

**Results and gaps.** Controlled scheduler runs retain independent Falsifier coverage of every parent artifact, verified from SQLite tool results rather than tool names. Direct prohibited mutation, redirection and unrelated executable attempts are refused with no extra file created. Verification-contract state is restored after the role returns. This is application-level capability mediation, not an OS sandbox or a proof against a compromised interpreter. Directory listing remains available for inspection; raw metadata is not a new publication artifact.

## 6. Repairer Investigation

**Observed failure and established cause.** The real failed run tried irrelevant helper artifacts and executable strategies while lacking the appropriate active evidence/scope. Impact guards correctly refused unauthorized helper creation. Sharing accepted literal verification evidence must not implicitly grant permission to rewrite existing protected resources.

**Research search.** Searches on localized software repair and independent patch validation led to Agentless [C4]. Its localization → focused repair → validation sequence fits this bounded problem. Adopting its entire repository-search pipeline or benchmark-specific model workflow would add unnecessary infrastructure. Its SWE-bench results are the authors' results, not Mini Hivo's.

**Selected correction.** `repair_task` installs validated task-matching literal inspection evidence temporarily. `tools_for_role` and `run_tool` constrain literal repair to source-bound inspection and focused edits. Context checking remains available. Helper creation, backups, shell/browser operations and unrelated paths are rejected. Existing repair context compilation, mutation grounding and impact authorization still decide whether any edit is legal; verification scope alone grants no mutation permission.

**Actual controlled recovery.** The new test creates a transaction-owned literal artifact through the real Builder, then fault-injects incorrect bytes after the authorized write. Real Falsifier/gates observe failure. Scripted Repairer proposals acquire fresh context, perform a focused `edit_file`, invoke native verification and complete. Independent actual bytes and final ROOT verification confirm recovery. The fault injection and model proposals are scripted; edits and verification are production behavior. This does not demonstrate repair of arbitrary existing files or live-model repair reliability.

**Failed development experiment.** The first repair fixture repeatedly proposed edits even after correction and exhausted its budget. The fixture was corrected to propose native readback and completion after the edit; production budgets and completion rules were not weakened. The earlier log remains preserved. There is still no automatic controller invention of arbitrary repair patches.

## 7. Recursive Execution and Parent Integration

**Problem and reproduction.** The unchanged prior parent acceptance test failed even when children had created the correct files. `_prepare_task_impact_contract` recompiled parent work as greenfield creation, correctly rejected already-existing targets under that write interpretation, and lost the useful distinction between observing child effects and introducing another mutation. Intermediate fixes that only changed the route still failed impact comparison because the comparison expected an observed post-state, not an empty mutation delta.

**Research search and limitations.** Searches covered hierarchical task outcomes, committed-step composition and transactional workflows. Sagas [C5] is relevant to retaining outcomes of completed steps without treating every later coordination step as a new write. Only its official abstract/metadata were accessible; the original technical-report download returned 403. No full-text benchmark claims are made. Full compensating transactions were rejected here: Mini Hivo already has child transactions, and this defect requires verified read-only composition rather than a new global rollback framework.

**Receipt mechanism.** `_record_verified_literal_receipt` runs after real leaf or aggregate success, gate, impact comparison and transaction commit. It rehashes current artifacts and binds run, child, parent, accepted contract hash and artifact hashes. A deep copy is registered in the current run's controller state and included in the result. `_current_literal_child_coverage` requires actual TASKS child identity, the complete expected child set, gate/impact success, a matching current-run registered receipt, valid accepted authority, exact source digest coverage and current file bytes. A public JSON object alone cannot create this trusted runtime record.

**Parent contract.** Only successful coverage selects `verification_only=True` in `_prepare_task_impact_contract`. The parent receives a newly validated inspection contract with source-derived expected targets, `literal_verification_only=true`, inspection paths and **empty authorized mutation paths**. It still passes context/impact acceptance, independently reads/verifies all targets and invokes Falsifier. Tool projection and dispatch reject mutation or unrelated execution. A read-only snapshot is captured before inspection; impact comparison records real current post-state observations and rejects changed task files or missing baseline. No fictitious write delta is created.

**Additional source preservation correction.** When a child owns the complete source artifact set, retain the source ledger's expanded records. The previous per-record literal filter accidentally removed the single-file ledger's split name/content obligations. The count-one scale test exposed this; set equality of source scope, not a hardcoded artifact count, selects the correct retention rule. Partial-child scoping still filters to that child's literals.

**Results.** Prior acceptance suite changes from 3 PASS/1 FAIL to 4 PASS with its tests unchanged. Controlled independent counts 1/2/3/4/5/8/10 and a dependency chain all reach done/root_verified with current exact bytes, native parent proof, Falsifier coverage, impact comparison and aggregate transaction commit. The dependency chain includes the predecessor file name and independently checked SHA-256 in each dependent artifact; the fixture supplies those source values and DAG edges. The production scheduler orders execution. It does not prove model-generated semantic dependency discovery.

**Negative results and limits.** Missing gate, missing receipt, altered accepted contract, previous-run receipt, changed bytes and unexpected parent-time files prevent completion. Existing-file protections are not globally relaxed. Parent authority is read-only; legitimate existing-file mutation still needs its ordinary independently authorized workflow. This is not whole-tree atomic rollback: children retain their existing committed transactions. The registry is process-local; restart/resume of committed-child receipts and deeply nested composition are not independently established. Snapshot cost is linear in inspected non-hidden file bytes, excludes hidden runtime state, and is not a hostile concurrent-filesystem lock.

## 8. Reliability and Recovery

Existing completed-context suppression, proof retention, bounded stall detection, dependency scheduling and authorization rules remain active. No timeout, inference budget, routing default or shell allowlist was increased. Current context/progress suites and dependency tests pass; negative stale-proof behavior remains fail-closed.

**Research search.** Searches on observation/action feedback and exception recovery identified ReAct [C6]. It supports preserving current observations before choosing another action. Adding unbounded reflection/model retries would increase local cost without proving progress, so no new inference loop was introduced. The selected work retains authoritative role evidence and uses explicit verified-state transitions, while leaving speculative automatic recovery out of scope.

The preliminary live baseline failed preflight with `CRITICAL_MEMORY_HEADROOM`, resource-monitoring failure and one completed canary out of three. The final-source inventory attempt later passed three canaries and entered Specifier. Its 1,350-token estimate and 4,096 configured context were not an oversized-context rejection. The trace records the Specifier request at 20:45:43.960 and timeout at 20:47:43.967; no Builder/tool activity occurred. Qualification success does not prove every subsequent request has adequate latency/resources. No model-loading or GPU telemetry establishes the physical cause. A failed `psutil` probe (module unavailable) and denied CIM inventory are diagnostic-access limitations, not evidence that Ollama was offline. Provider timeout attribution remains unresolved.

Material artifact changes invalidate composition by fresh byte checks; they do not automatically manufacture new authorization. General automatic context revalidation/replanning after all possible material changes remains unproven. Partial-child failure and provider handling have existing controlled scheduler coverage, but the full live failure/recovery matrix is not established by this update.

## 9. Research Review and Engineering Decisions

Sources searched were original arXiv papers, PMLR proceedings, author/university-hosted originals and SIGMOD's official record. Search families are recorded separately in sections 3–8. Selection required a mechanism matching an evidenced defect; an LLM/agent keyword alone was insufficient. No model training, new service, framework or dependency was added.

| Reference | Transfer and cost | Decision / deterministic measure |
|---|---|---|
| C1 SayCan | Ground interpretation in source and current inventory; local parsing, no inference | Adapt concept only; exact historical requests and existing-resource negatives |
| C2 Proof-Carrying Code | Bind accepted evidence to artifacts and consumer policy; O(file bytes) digest/read checks | Adapt evidence discipline, not formal proof system; stale/forged/missing checks |
| C3 Saltzer–Schroeder | Least privilege plus complete dispatch mediation; small local tool-filter/guard cost | Apply scoped capabilities; direct hidden-action refusal and unchanged artifacts |
| C4 Agentless | Localize permitted repair and revalidate; existing repair calls only | Adapt focused scope, not framework; fault-injected actual edit and final gate |
| C5 Sagas | Separate committed child outcomes from coordination; registry plus fresh reads | Conceptual comparison, no full saga implementation; parent success/rejection matrix |
| C6 ReAct | Preserve tool observations for subsequent action selection | Complement existing bounded controller; reject speculative budget increases |

These papers inform engineering choices; only our own tests support our implementation outcomes. Empirical results reported by authors are summarized with explicit attribution in Appendix C. Read-only checks add local I/O rather than model calls. Receipt trust assumes the controller's process state is not compromised. A different model or persistent distributed ledger is not required by these scoped corrections.

## 10. Implementation Change Log

| File / functions | Before → after | Safety / coverage |
|---|---|---|
| `hivo/project_understanding.py::classify_project_mode` | Keyword preservation could imply existing code → source/inventory-aware deterministic precedence | Explicit missing-existing work remains fail-closed; exact historical requests |
| `mini.py::run_file`, `_literal_artifact_verification_paths` | Role transition could lose literal route → validated task-scoped evidence survives | Current exact bytes, accepted hash and scope required |
| `mini.py::falsify_task`, `_falsify_task_body` | Cleared global used for verification → accepted child evidence copied across call and restored afterward | Real independent readback; no mutation authority |
| `mini.py::repair_task`, `_repair_task_body`, `tools_for_role`, `run_tool` | Generic literal repair proposals → source-bound focused operations | Dispatch guards supplement projected tools; original authorization remains |
| `mini.py::_prepare_task_impact_contract` | Parent tried to create already-created files → explicit read-only accepted composition; expanded full-source ledger retained | No broad existing-file write exception |
| `mini.py::_record_verified_literal_receipt`, `_current_literal_child_coverage` | Child status/manifest insufficient → committed current-run controller registry plus fresh byte coverage | Missing/forged/stale/replayed evidence refused |
| `mini.py::aggregate_task`, `_literal_parent_snapshot`, `_impact_post_mutation_check`, `_impact_tool_projection`, `_impact_gate_mutation_guard` | No valid read-only parent observation contract → validated inspection, independent proof and current state comparison | Empty mutation scope; unexpected task-file change refused |
| `hivo/verification_routing.py` | Literal route required mutation contract shape → also supports accepted inspection-only shape | No automatic unavailable-evidence PASS |
| `tests/test_update004_verification_integration.py` | New 12-case regression/controlled-functional module | Scripted model, real affected execution paths and filesystem |
| `scripts/update004_controlled_replay.py` | New persistent offline matrix/independent inspector | Retains copied actual workspaces privately; no live provider |
| `scripts/verify_level2_offline.py` | Adds new suite and classifier source pin | Rejects live provider calls; keeps known live test excluded |
| `scripts/level2_clarification_replay.py` | Adds complete relevant source pin set | Live behavior/budgets unchanged; fresh evidence directories |

No other production module, AGENTS.md, update template or previous numbered report was edited. Manifests list exact current file hashes and baseline hashes; this document cannot know a future containing commit.

## 11. Controlled Regression Testing

Commands are in Appendix F. The final offline cohort is `offline-receipt-final`; final persistent execution cohort is `controlled-receipt-final` under the ignored R4 audit root. All production/test pins used by those cohorts match current files at documentation validation.

| Suite pattern | Tests run | Failures | Errors | Skips | Outcome |
|---|---:|---:|---:|---:|---|
| level1_native_verification | 10 | 0 | 0 | 0 | PASS |
| level2_generalized_recovery | 20 | 0 | 0 | 0 | PASS |
| literal_clarification_lifecycle | 9 | 0 | 0 | 0 | PASS |
| project12_clarification | 9 | 0 | 0 | 0 | PASS |
| context_completed_progress | 11 | 0 | 0 | 0 | PASS |
| context_recovery_functional | 4 | 0 | 0 | 0 | PASS; previous parent failure resolved |
| update004_verification_integration | 12 | 0 | 0 | 0 | PASS |
| dependency_aware_scheduler | 9 | 0 | 0 | 0 | PASS |
| greenfield_impact_lifecycle | 17 | 0 | 0 | 0 | PASS |
| pre_mutation_impact | 27 | 0 | 0 | 0 | PASS |
| context_sufficiency_gate | 9 | 0 | 0 | 0 | PASS |
| verification_applicability | 15 | 0 | 0 | 0 | PASS |
| authority* | 23 | 0 | 0 | 0 | PASS |
| experiment* | 122 | 0 | 0 | 0 | PASS |
| adaptive_architecture | 90 | 0 | 0 | 0 | PASS |
| project_understanding | 32 | 0 | 0 | 0 | PASS |
| model_policy | 4 | 0 | 0 | 0 | PASS |
| requirement_clarification | 49 | 0 | 0 | 0 | PASS; one known live-provider test excluded |
| verification_policy | 8 | 0 | 2 | 0 | ERROR; missing benchmark fixtures |
| v26_* | 186 | 24 | 2 | 3 | FAIL/ERROR; historical recovery/fixture debt |

Do not sum these counts: inheritance and overlapping scope exist. Failure records can include subtests and are not a denominator for inferred pass counts. Offline driver exit is 1 because the two debt cohorts remain unsuccessful. The failing/error test IDs in both are identical to `offline-existing-first`; full IDs and tracebacks are retained. They are pre-existing at this update's starting source, not evidence of newly introduced failures. They still need separate engineering closure; they are not reclassified as successes or all dismissed as obsolete fixtures.

The known requirement test `test_root_brain_prompt_compacts_large_source_side_channel_without_dropping_ids` is excluded because it has historically invoked a live provider. The driver also forbids unintended live `ask_ollama` calls. This is focused discovery, not a claim that every repository test is offline or passing.

**Controlled functional proof.** Each of eight retained cases has 11 independently evaluated checks: status done, root_verified, exact current bytes, no extra task files, typed native parent coverage, Falsifier coverage, no parent mutation, parent impact and gate success, aggregate transaction commit, no failed nodes. Artifacts are copied byte-for-byte from actual execution before temporary cleanup; retained paths differ from original temporary paths and are labeled accordingly. Model proposal sequences and decomposition are fixtures. All eight independent inspection records passed; there is no live model reliability inference.

The final read-only review independently rechecked all 36 retained artifact files against expected hex and recorded digest, all cohort source pins, nine originals against both initial hashes and backup ZIP bytes, curated original/derivative hashes, Markdown links, privacy patterns and Git state. The working diff passes `git diff --check`; the index remains empty. Review output is preserved privately as `audit_runs/20261021-workspace-audit/r-update-004/review-validation.json`. Privacy checks and review cover this packet, not a claim that all repository history is free of private data.

**Development chronology.** Initial parent replay failed existing-target contract; route-only experiment then exposed absent post-state observation; adding read-only observations made the unchanged four tests pass. Initial new fixture indexed aggregate results as leaf results and errored; correcting diagnostic indexing fixed that harness issue. Repair fixture initially looped on edits; corrected scripted handoff retained its failure log. Count-one scale exposed genuine ledger filtering loss; general full-source scope handling fixed it. Receipt hardening added trusted commit-bound registration and missing/replay negatives. Final broad and persistent cohorts were rerun after those production changes. Intermediate cohorts remain private and are not relabeled final-source results.

## 12. Genuine Ollama Evaluation

No genuine PASS is claimed in R_UPDATE_004.

| Attempt | Source / model / result | Observed boundary |
|---|---|---|
| `live-final/structured-blocks` | Earlier R4 source, `gemma4:e4b`, process exit 2, 26.39 seconds, no task run ID | Preflight `CRITICAL_MEMORY_HEADROOM`; 1/3 canaries; no completed metrics/artifacts |
| `20261025T204437-4d483ccf`, `live-receipt-final/inventory` | Final production pins; `gemma4:e4b`; process exit 0, task status failed, root_verified false | Preflight PASS 3/3; NEW_PROJECT; three literal sources; Specifier timeout; no tools |

The final inventory process lasted 219.53 seconds; task metrics elapsed 186.29 seconds, two model calls, zero tool/Falsifier calls, zero impact authorizations/comparisons and no execution budget exhaustion. No artifacts were created. No decomposition, Builder, Falsifier, Repairer, parent integration or transaction completion was reached. Exit 0 is a CLI process outcome, not task success. The run trace records Stage 2 provider failure and a 120-second Specifier request timeout. No code change or timeout increase was made to conceal this failure.

Exact prompts, expected byte hex/digests, source pins and sanitized selected events are in the live/run registry. The inventory request asks for three UTF-8 files with LF and no trailing newline:

```text
products.txt: Product: Keyboard\nQuantity: 12\nPrice: 250
supplier.txt: Supplier: Nile Tech\nCity: Cairo\nStatus: Active
shipment.txt: Shipment: SH-2026\nItems: 12\nStatus: Pending
```

The registry stores the full original block request, not just this compact oracle. Workspaces are fresh under the ignored R4 audit directory. Source pins prove which files were used; the earlier baseline attempt has different pins and is not called final-source baseline verification.

Live scenarios A (final-source baseline), C (different recursive task), D (dependency), E (live recovery) and F (live existing-project counterpart) remain unverified. E has direct controlled recovery proof; F has direct deterministic classification proof and the live new-project observation. Further expensive task attempts were deferred after the final Specifier failure rather than repeating a failure without new diagnostic value. Provider/load attribution and eventual final-source live completion remain required.

## 13. Complete Before/After Comparison

| Mechanism | Before | Current evidence | Limit |
|---|---|---|---|
| Empty-project intent | “Preserve” could route to existing | Exact historical requests now NEW; live inventory NEW | Arbitrary prose not universally resolved |
| Literal proof handoff | Accepted child evidence lost between roles | Native current digest and independent Falsifier coverage | Source-bound literal scope |
| Falsifier capability | Generic shell proposals attempted/refused | Literal projection and dispatch restrict inspection | Not an OS sandbox |
| Repair strategy | Helper/executable attempts refused | Actual owned-file corruption repaired and reverified | Model and fault scripted |
| Parent acceptance | 3/4 prior functional tests passed | Unchanged suite 4/4; eight retained ROOT passes | Fixture DAG; process-local receipts |
| Provenance | Status/manifest insufficient for safe composition | Trusted current-run commit receipts + fresh hashes | No restart/distributed trust proof |
| Broad regression | Policy errors and recovery debt | Same failure/error IDs retained | Broad suites not all green |
| Live runtime | Prior historical baseline PASS; recursive failures | Final new classification succeeds, Specifier times out | No final-source live completion |

No success-rate or performance improvement is inferred from these heterogeneous samples. The measurable acceptance improvement is one previously failing controlled parent test now passing with unchanged assertions, plus explicitly scoped new behavior and negative checks.

## 14. Open Issues and Risks

| ID / severity | Component / status / evidence | Impact, next action and closure test |
|---|---|---|
| R4-01 High | Final-source live execution unverified; confirmed timeout `20261025T204437-4d483ccf` | Diagnose provider timing/loading/resource conditions without changing budgets speculatively; close with genuine A–D workflows and all final gates |
| R4-02 Medium | Provider root cause unknown; preflight outcome varied | Capture request-level Ollama service/load telemetry on a diagnostic run; distinguish latency, service/resource and request construction causes |
| R4-03 Medium | Verification-policy fixture errors, confirmed | Restore/identify sanctioned benchmark fixtures independently; rerun eight tests without fabricated data |
| R4-04 Medium | V26 recovery suite 24 failure records, two errors, three skips, confirmed baseline | Investigate retained IDs by ownership/path; rerun affected recovery suites; do not infer safe generalized recovery from new passes |
| R4-05 Medium | Process-local child receipt registry, confirmed design limit | Specify persistence/restart semantics before loading receipts across processes; closure requires forged/stale/restart tests |
| R4-06 Medium | Deep nesting/model-generated dependency discovery not independently proven | Extend real scheduler integration scenarios and live decomposition with independent oracles |
| R4-07 Medium | Automatic general material-change revalidation is partial | Current literal hashes reject stale proof; closure requires context changes followed by authorized safe replan/recovery, not only rejection |
| R4-08 Medium | Parent snapshot excludes hidden runtime state and is not a concurrent filesystem lock | Bound scanning for large workspaces; test concurrent/symlink/resource failures under stated threat model before broader claims |
| R4-09 Medium | Complex application/existing-file repair not established by literal tests | Use appropriate executable/browser oracles and approved existing-file contracts; keep text scope separate |
| R4-10 Low | Current files unstaged, line-ending conversion warnings possible | Future publication needs explicit path audit, canonical byte policy and staged-blob integrity checks; no staging is authorized now |

Receipt hashing is tamper detection within trusted controller state, not an adversarial signature. Child commits are not rolled back as a single global atomic transaction by this change. Runtime traces and private backup remain local; public Git history is unchanged and nothing previously published has been erased.

## 15. Level 2 Readiness Assessment

| Requirement | Assessment |
|---|---|
| Source preservation/classification | Controlled coverage and final live new-project classification; general prose remains bounded |
| Context Sufficiency / Mutation Grounding / impact authorization | Focused and existing suites pass; actual controlled gates exercised; stale and hidden actions rejected |
| Builder / Falsifier / exact literal verification | Direct controlled functional proof; no final-source live Builder reached |
| Repairer | Controlled actual mutation and independent re-verification; live repair unverified |
| Recursive scheduling / Parent Integration | Controlled real scheduler, real children and parent PASS; fixture decomposition; live recursive completion unverified |
| Transaction correctness | Actual child/aggregate commit evidence within tested scope; no whole-tree atomicity claim |
| Recovery / material-change handling | Bounded rejection and owned repair proven; general revalidation/restart recovery incomplete |
| Real-model reliability / generalized applications | Unverified on final source |
| Auditability | Source hashes, original preservation, failed cohorts, curated records and exact commands retained |

**Level 2 remains INCOMPLETE.** The checkout is available for bounded independent manual tests after successful provider qualification. It is not ready for a completion claim, Level 3, publication or a claim of generalized application reliability. All changes are local, unstaged and uncommitted. Previous PRs remain untouched.

## Appendix A. Run Registry

See [run-registry.json](../evidence/level2-verification-repair-integration/run-registry.json) for exact controlled IDs, checks, expected byte oracles and live request/result records. Independent cases: `20261025T204216-ee434e6f` (1), `20261025T204216-c764dba8` (2), `20261025T204217-3c595f50` (3), `20261025T204219-ce7031e4` (4), `20261025T204221-5298b881` (5), `20261025T204224-2c54d11a` (8), `20261025T204229-c39ea2d8` (10). Dependency case: `20261025T204235-a8befced`. Final live failed run: `20261025T204437-4d483ccf`.

## Appendix B. Evidence Manifest

[manifest.json](../evidence/level2-verification-repair-integration/manifest.json) distinguishes original source SHA-256 from sanitized derivative SHA-256, records nine preserved original files and validates their ZIP bytes. Raw SQLite databases, transcripts, host telemetry and test workspaces stay under the ignored audit root. Curated records are inspection evidence, not reusable authorization. Manifest excludes its own hash to avoid circularity; current working-tree hashes are validated, with no claim to have checked staged blobs because staging is prohibited.

## Appendix C. Research References

**C1. Do As I Can, Not As I Say: Grounding Language in Robotic Affordances.** Brian Ichter et al., CoRL proceedings, PMLR 205:287–318, 2023; original preprint 2022, arXiv:2204.01691. [Official proceedings and complete author list](https://proceedings.mlr.press/v205/ichter23a.html), [original full text](https://arxiv.org/html/2204.01691v2). The preprint uses Michael Ahn et al. author ordering; the proceedings use Brian Ichter et al. The authors evaluate 101 robot instructions and report benefits from combining language with learned affordances. Robot skills/value functions and training assumptions differ substantially from local deterministic file intent. Adaptation: source/inventory precedence only.

**C2. Proof-Carrying Code.** George C. Necula and Peter Lee, CMU-CS-96-165, November 1996 technical report. [Author bibliography](https://people.eecs.berkeley.edu/~necula/papers.html), [accessible original-report copy](https://personal.utdallas.edu/~hamlen/Papers/necula96.pdf). This is distinguished from George C. Necula's POPL 1997 paper, DOI 10.1145/263699.263712; its linked PostScript could not be read through the research tool. The report studies consumer safety-policy checking with producer-supplied proof, including certified packet-filter examples. It assumes formal policies/checkers. Mini Hivo adapts artifact/evidence binding and independent checks, not formal verification of arbitrary code or the report's performance claims.

**C3. The Protection of Information in Computer Systems.** Jerome H. Saltzer and Michael D. Schroeder, Proceedings of the IEEE, 1975. [University-hosted original PDF](https://www.cs.cmu.edu/afs/cs.cmu.edu/academic/class/15712-s05/www/readings/Saltzer75.pdf), [university HTML](https://www.cs.virginia.edu/~evans/cs551/saltzer/). The paper develops protection principles including least privilege, complete mediation and fail-safe defaults. It is a systems design treatment, not an LLM experiment. Adaptation: scoped role tool surfaces plus mandatory dispatch checks. It does not establish protection against compromise of our Python process.

**C4. Agentless: Demystifying LLM-based Software Engineering Agents.** Chunqiu Steven Xia, Yinlin Deng, Soren Dunn and Lingming Zhang, 2024 preprint, arXiv:2407.01489v2. [Original paper](https://arxiv.org/abs/2407.01489), [reviewed full text](https://arxiv.org/html/2407.01489v2). Localization, repair and validation are separated. Authors report 96/300 (32%) SWE-bench Lite resolutions at approximately $0.70 per problem for their evaluated setup. Those benchmark/model assumptions differ from exact literal text repair. We adopt focused scope and revalidation, without importing the framework or transferring its success rate.

**C5. Sagas.** Hector Garcia-Molina and Kenneth Salem, ACM SIGMOD 1987, pp. 249–259, DOI [10.1145/38713.38742](https://doi.org/10.1145/38713.38742). [Official SIGMOD record](https://sigmodrecord.org/1987/12/09/sagas/). The official abstract/metadata describe decomposing long transactions into steps and handling failures through compensation. The original Princeton technical-report PDF was inaccessible (403), limiting review. No empirical throughput claim is imported. Comparison informs retaining committed child outcomes; Mini Hivo does not implement full saga compensation or global atomic rollback in R4.

**C6. ReAct: Synergizing Reasoning and Acting in Language Models.** Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan and Yuan Cao, ICLR 2023, arXiv:2210.03629. [Original paper](https://arxiv.org/abs/2210.03629), [PDF](https://arxiv.org/pdf/2210.03629). Interleaved observations and actions support exception handling; authors report absolute success improvements of 34% on ALFWorld and 10% on WebShop over specified baselines. These are not our workloads or results. We preserve authoritative feedback and bounded transitions; no unbounded reasoning loop or new chain-of-thought logging is introduced.

## Appendix D. Code Change Manifest

[code-change-manifest.json](../evidence/level2-verification-repair-integration/code-change-manifest.json) lists every changed production, test and harness file, base blob hash where available, current source hash and purpose. Documentation/evidence are additional local files. `git diff` against the base is the attribution boundary. Prior context/clarification machinery is not attributed to this update merely because it executes in the new tests.

## Appendix E. Test Registry

[test-registry.json](../evidence/level2-verification-repair-integration/test-registry.json) retains full suite IDs, outcomes, excluded live test, source pins and comparison of historical failure/error IDs. Selected test logs are sanitized derivatives; original logs remain private. Tests serve different scopes: isolated classifier negatives are unit/regression; scheduler/leaf/parent and repair are controlled functional/integration; none is a live-model PASS.

## Appendix F. Exact Reproduction Instructions

From the repository root in Windows PowerShell (use a **new output directory for every run**):

```powershell
.\.venv\Scripts\python.exe -B -X utf8 -m unittest discover -s tests -p test_update004_verification_integration.py -v
.\.venv\Scripts\python.exe -B -X utf8 scripts/update004_controlled_replay.py --output-dir audit_runs/manual-r4-controlled-01
.\.venv\Scripts\python.exe -B -X utf8 scripts/verify_level2_offline.py --output-dir audit_runs/manual-r4-offline-01
```

The broad command is expected to return unsuccessful until the disclosed baseline debt is resolved; inspect `results.json`, not only the exit code. The controlled script never calls a live model and independently checks retained real files/events.

For a single bounded genuine baseline or inventory replay, after ensuring Ollama is available and preflight succeeds:

```powershell
.\.venv\Scripts\python.exe -B -X utf8 scripts/level2_clarification_replay.py --live --cases structured-blocks --output-dir audit_runs/manual-r4-live-baseline-01
.\.venv\Scripts\python.exe -B -X utf8 scripts/level2_clarification_replay.py --live --cases inventory --output-dir audit_runs/manual-r4-live-inventory-01
```

Run these sequentially, inspecting the first outcome before starting the second. Each live subprocess has the existing 720-second outer bound; preflight and provider safeguards remain enabled. Do not repeat timeout batches without diagnostic value. A fresh final-source live pass must inspect trace/tool receipts, child and parent gates, impact/transaction records and actual artifacts; the script's `independent_pass` field alone is insufficient for that full claim.

For independent interactive testing:

```powershell
.\.venv\Scripts\python.exe -B -X utf8 mini.py --no-bootstrap
```

Choose a fresh workspace; do not reuse project-21. Start with: `Create a text file named test_level_1.txt containing exactly:Hello Mini Hivo`. Expected bytes are UTF-8 `Hello Mini Hivo`, length 15, no newline. Then in a separate fresh workspace paste the full `inventory` request from `run-registry.json`; do not type literal backslash-n characters in place of the block line breaks. A different recursive manual request can specify four new files:

```text
Create exactly four UTF-8 text files in this empty workspace.
File: north.txt
Exact content:
Region: North
Count: 4
State: Ready

File: south.txt
Exact content:
Region: South
Count: 7
State: Ready

File: east.txt
Exact content:
Region: East
Count: 2
State: Ready

File: west.txt
Exact content:
Region: West
Count: 9
State: Ready

Use exactly three lines per file, UTF-8, LF separators, no trailing newline.
Create no additional task files. Independently verify every exact file before completion.
```

This four-file live scenario has **not** been run in this update. Retain its new run ID and inspect every required gate. For existing-project classification, use a separate disposable workspace containing a meaningful existing file and request an explicitly scoped modification; expect EXISTING_PROJECT, not a forced greenfield write. Do not manually tamper with old experiments to test recovery; use the controlled repair regression above.

## Appendix G. Remaining Engineering Tasks

Resolve request-level provider latency attribution; qualify and run final-source live A–D with full independent artifact/gate inspection; extend nested/restart receipt semantics before claiming them; investigate baseline recovery debt and missing policy fixtures; measure larger workspace snapshot cost; test authorized existing-file repair with executable/application oracles; preserve R4 as incomplete until closure evidence exists. No Level 3 work is included.

## Appendix H. Known Environmental Limitations

Local model availability/preflight can change between attempts. An earlier memory-headroom rejection and later successful canaries coexist with a subsequent request timeout. GPU/load telemetry was unavailable; no causal physical diagnosis is established. Offline suites use scripted providers and do not benchmark real model throughput. Raw workspaces, databases, host inventories and backups remain ignored/private. No Git staging or blob normalization validation occurred; future publication requires separate explicit authorization and staged-byte privacy/integrity review.

## Local team summary (template A–M cross-reference)

Identification: sections 1–2; original problem/necessity/root cause: sections 3–8; changes/mechanism: sections 3–10; functional verification: sections 6–7/11–12; additional tests/compatibility: section 11; impact/limits: sections 13–15; evidence/reproduction: appendices A–H. Proposed future title: **Repair literal verification handoff and read-only recursive parent integration**. Proposed description: source-grounded classification and scoped evidence/repair fixes resolve the reproduced controlled parent failure; new exact-byte and provenance negatives pass, while broad historical debt and final-source live Specifier timeout remain disclosed. This is a local review summary, not authorization to publish or a claim that Level 2 is complete.

---

## False Requirement Conflicts and Clarification Flow

### Chronological addendum — 27 October 2026

This is additional local engineering within R_UPDATE_004, not R_UPDATE_005. Sections 1–15 and appendices above describe the 25 October checkpoint. Their source pins and results remain historical, unchanged evidence; they must not be read as a claim that today's source matches those pins. This addendum records the subsequent manual regression, repairs and final reviewed-source tests. **Level 2 remains INCOMPLETE.** No publication is authorized or performed.

### 1. Original observation and exact source

Genuine manual run `20261027T151126-fabceeb5`, project-22, selected `gemma4:e4b`. Retained metrics show `clarification_required`, six extracted source requirements, three blocking questions, zero task model/Builder/tool calls, `root_verified=false`, and control flow ending at REQUEST_CLARIFICATION. Host preflight passed three canaries; those qualification calls are outside task model-call counters. The original request was:

```text
Create exactly one UTF-8 text file named employee.txt in the workspace.

The exact content must be:
Name: Sara
Department: Engineering
Status: Active

The file must contain exactly three lines in the specified order.

Use LF line separators and no trailing newline at the end of the file.

Do not create any additional task files.

Verify that the file exists and that its content exactly matches the requested text before reporting completion.
```

Source SHA-256: `df6e34ce860f792f6bb466feb28fccfae0f88b992f6b286990655fbee3147cdd`. Before modifications, this run's files, the second project-22 trace `20261027T151514-6fea1b5f`, database, preflight record, relevant source files and the previous R4 report were preserved in a fresh byte-preserving backup. Originals in project-22 were never used as replay workspaces.

The three actual questions compared REQ-001 with REQ-004, REQ-001 with REQ-005, and REQ-003 with REQ-004. Their options respectively offered creation versus newline policy, creation versus no additional files, and three lines versus no trailing newline. The shared reason was: “The requirements explicitly prescribe opposite behavior for the same target.” All three pairs are compatible.

### 2. Pre-model trace and confirmed causes

The actual path was `get_goal_contract` → literal preparation (no recognized block) → source segmentation/candidates → immutable ledger → `clarify_request` → `detect_explicit_conflicts` → `_conflict_evidence` → `conflict_questions` → terminal selection/resolution. No Ollama task request participated in these decisions.

The deterministic ledger retained six statements: creation; the exact-content heading; three-line requirement; LF/no final newline; prohibition on additional files; final acceptance. The three content lines were present in `raw_user_request`, but the block parser did not bind them to an authoritative literal obligation for this natural declaration format. Thus the evidence proves **an extraction/representation gap**, not total loss of the raw text. The earlier parser recognized `File: name / Exact content:` and JSON maps, not `Create … file named … / The exact content must be:` separated by paragraphs.

The precise false-conflict mechanism was `_positive_target_tokens` intersected with `_negative_target_tokens`. Negative spans included ordinary words such as `file`, `files`, `additional`, `trailing` and `newline`; positive sentences included `file` or `files`. Any intersecting token was treated as proof of opposite behavior. The algorithm did not bind a predicate, property, scope or condition. It therefore confused prohibiting **additional** artifacts with prohibiting requested artifacts, and a final-newline policy with a file/line-count action. All three historical pairs were reproduced with the untouched ledger and zero model calls before selecting a repair.

Final adversarial checking also verified that instruction words inside exact content are data. Proven payload spans are now masked before policy segmentation; quoted exact values are extracted separately before policy/legacy lifecycle matching. This prevents the same false-conflict mechanism from reappearing through content such as “Use only CRLF” or “restart erases data.” Filename identity is normalized separately from case-sensitive content.

A further source-normalization problem was exposed by negative tests: generated single-literal name/content records lacked explicit artifact association, and case-folded merging could collapse exact content `A` and `a`. This was corrected in the same source/provenance layer, not hidden by reducing clarification questions.

### 3. UI and continuation findings

The old `select_clarification_option` put source choices directly into `radiolist_dialog`, with the first choice selected initially. The full-screen dialog text contained only navigation instructions; the actual question/reason were printed outside it. Its cancellation label said “Skip / use default” even for blocking decisions. The Windows fallback also initialized index zero. This amplified the detector error; it did not cause the original false conflicts.

Previously, selecting a choice appended a USER_CONFIRMED record and did not delete the original ledger. However, the execution representation still carried both unresolved original statements, and generic conflict decisions had no workspace-bound continuation state comparable to literal-boundary clarification. Thus preservation of raw records alone did not establish a resolved, unambiguous execution contract. Project-22 contains no accepted clarification answer; no claim is made that its original menu actually discarded a requirement.

### 4. Focused research search and original references

Searches were performed after reproducing the code defect and before selecting the repair. Search families included natural-language contradiction/event alignment, scoped negation, requirement consistency and provenance, NLI neutral versus contradiction, and formal requirements/specification relations. Primary ACL publications were accessible; an original requirements-engineering PDF could not be fetched fully. Research results are not proof of Mini Hivo correctness.

**C7 — Finding Contradictions in Text.** Marie-Catherine de Marneffe, Anna N. Rafferty and Christopher D. Manning, ACL-08: HLT, 2008, pp. 1039–1047. [Original record](https://aclanthology.org/P08-1118/), [reviewed paper](https://aclanthology.org/P08-1118.pdf). The method aligns events/entities and scopes polarity, numerical and other mismatch features before contradiction classification. Its reported RTE3 development comparison improves precision from 55.10 without filtering to 61.90 with root/topic filtering, with recall 32.93 versus 31.71. This demonstrates an alignment tradeoff in that dataset, not our performance. Adapted idea: require aligned target/property/conditions and a positive incompatibility witness. We do not import its parser, hand-weighted classifier or assume unrestricted semantic coverage.

**C8 — A large annotated corpus for learning natural language inference.** Samuel R. Bowman, Gabor Angeli, Christopher Potts and Christopher D. Manning, EMNLP 2015, pp. 632–642, DOI `10.18653/v1/D15-1075`. [Original record](https://aclanthology.org/D15-1075/), [reviewed paper](https://aclanthology.org/D15-1075.pdf). SNLI provides 570,152 human-written sentence pairs with entailment, contradiction and neutral/semantic-independence labels; authors report lexicalized and neural baseline evaluations. Caption-derived data and grounding assumptions differ from imperative software requirements. Adapted distinction: failure to prove entailment is not proof of contradiction. A trained NLI model was rejected as the sole authorization/clarification gate because domain calibration, model availability and added inference latency are unproven here.

**C9 — Four Dark Corners of Requirements Engineering.** Pamela Zave and Michael Jackson, ACM TOSEM 6(1), January 1997, pp. 1–30. [Original-paper university-hosted copy](https://www.cse.msu.edu/~chengb/RE-491/Papers/dark-corners-re-zave-jackson.pdf). Search extraction exposed its title, authors, abstract and publication details; full fetch timed out twice. Only that limited material was considered. Its distinction between requirements, specifications, domain knowledge and control information motivates preserving authoritative statements separately from decisions. It was not reviewed as an implemented contradiction algorithm; no empirical result or formal guarantee is imported.

### 5. Architectural comparison and selected approach

| Candidate | Fit, cost and risk | Decision |
|---|---|---|
| Disable conflict detection | Removes false positives but misses incompatible exact values/authority | Rejected |
| More keyword exceptions | Cheap but repeats the observed failure mechanism under new wording | Rejected |
| LLM/NLI decides every contradiction | General language coverage is attractive; adds calls, latency, calibration and uncertain authorization semantics | Not used as sole gate; existing eligible Clarifier path remains |
| Full unrestricted SAT/SMT semantics from prose | Solver is useful only after trustworthy formalization; no complete parser exists here | Not claimed or introduced |
| Typed bounded constraints plus conservative witnessed conflicts | Fits pure source layer, no additional model/service dependency; deterministic positive/negative tests | Selected |

Each fact binds target, property, value and condition. Artifact count, exact content, line ending, final newline, mutation/preservation, inclusion and creation obligations are separate properties. Independent properties compose rather than compete. Compatible negative constraints are retained. A conflict needs unequal mutually exclusive values under aligned scope/conditions, with both source IDs and a structured witness. Artifact association is explicit for expanded literal records. Original source and confirmed decisions remain distinct from effective execution input.

Unknown semantics are **not** certified compatible or discarded. Requirements remain present for specification, context, impact and authorization checks. The existing eligible, decision-critical Clarifier can still request an unresolved authorization choice; a controlled test exercises that path. The new deterministic grammar is bounded, not an NLI or arbitrary satisfiability solver. Lexical variants, complex temporal conditions and model-originated clarification continuation outside the new explicit-conflict store remain limits.

The worst-case pair scan is bounded by the existing 64-requirement limit. Parsing and comparison add local CPU/I/O only; no new model calls, model, dependency, timeout or budget was added. Existing command security, literal artifact limits, context, impact and verification gates are unchanged.

### 6. Exact production changes

| File / function | Implemented correction |
|---|---|
| `hivo/requirement_consistency.py::facts`, `targets`, `condition`, `contradiction` | New pure scoped constraint comparison and explicit mismatch witnesses; no broad token-overlap proof |
| `hivo/requirements.py::_conflict_evidence`, `detect_explicit_conflicts` | Use typed evidence; preserve existing lifecycle/resource checks with explicit target/condition separation |
| `hivo/requirements.py::_can_merge`, `deterministic_requirement_candidates`, `build_source_requirement_ledger`, `extract_source_requirements` | Preserve case-sensitive literal content, artifact path and original clause; avoid merging across different literal targets |
| `hivo/literal_source.py::parse_literal_input`, `policies`, `policy_text` | Mask proven literal bodies before policy extraction; support natural named-artifact content blocks with original spans; recognize singular file counts without rewriting literal values |
| `mini.py::extract_source_requirement_ledger` | Retain complete parsed literal obligations, original offsets/content and exact UTF-8 digest alongside normal source statements |
| `mini.py::get_goal_contract`, `_get_goal_contract_body` | Evaluate explicit conflicts before canonicalization; continue original workspace-bound decisions; preserve original ledger and record explicit supersession separately from effective execution ledger |
| `hivo/requirement_decisions.py::RequirementDecisions` | Workspace identity, pending state, append-only history, validated choice/Other answers, bounded multi-question continuation, explicit cancellation and independent-task handling |
| `mini.py::_source_ledger_for_contract` | Use controller-produced effective execution ledger when a recorded source decision exists, retaining original source in provenance |
| `mini.py::select_clarification_option`, `resolve_clarification_questions` | Display actual question/reason; blocking default is unresolved; skip/cancel do not choose a source statement; invalid index and interrupted Other are safe |
| `tests/test_requirement_consistency_flow.py` | New 18-case unit/integration/controlled-functional suite, including exact original prompt and negative decisions |
| `scripts/verify_level2_offline.py` | Add new suite and new source-module pins; preserve live-test exclusion/provider prohibition |
| `scripts/replay_requirement_consistency.py` | Fresh one-case genuine CLI replay with source pins, actual artifact observations, preserved failures and 360-second outer bound |

No filename, employee prompt, artifact count or run ID is hardcoded in production repairs. They appear only in tests, replay fixtures and documentation. Existing R4 classification/verification changes remain intact. `literal_clarification.py` was inspected but did not need modification for this phase.

### 7. Decision semantics and retention

For a real conflict, the menu now starts with **Leave unresolved — keep all requirements**. The dialog itself contains the question and reason. Enter without navigation, Escape, Skip, cancelled Other, blank/unresolving Other and invalid selection cannot select an incompatible outcome. Explicit selections and sufficiently resolving Other answers are source-bound USER_CONFIRMED decisions.

`RequirementDecisions` persists original request, original ledger, questions and accepted answers under a workspace identity. Partial answers leave only unresolved question IDs pending. A new independent creation request does not become an answer or consume the pending decision. A copied state from another workspace cannot load. Explicit task cancellation archives the source and decisions without treating any requirement as selected.

Once the required choices are complete, only explicitly superseded source clauses are removed from **effective execution input**. Original source records remain immutable and visible in provenance; unaffected clauses remain in execution input. If mapping a decision back to source or mutually consistent selections cannot be established, execution remains blocked. This is an auditable change authorized by the user's decision, not silent requirement deletion. It does not grant mutation authorization; ordinary downstream gates still apply.

### 8. Controlled tests and actual artifacts

Final reviewed cohort: `audit_runs/20261021-workspace-audit/r-update-004/false-conflicts-20261027/offline-verified-final/`. The new suite runs **18 tests, zero failures/errors/skips**. Counts below are scoped and not summed with overlapping suites.

- Compatible-property subtests cover exact text/LF, three lines/no final newline, one file/no extras, HTML title/structure/inline style, no external CSS, JSON keys/indentation, Python side-effect restrictions, unrelated-file preservation, independent targets, equivalent wording and different per-file conditions/formats. These are source-consistency checks, not execution proof for every programming language.
- Genuine-conflict subtests cover LF versus CRLF for the same target, incompatible exact content including case, artifact counts, positive/negative modification, unchanged preservation versus update, required versus prohibited lines, and negative modal variants.
- UI/state coverage includes no UI for the original compatible request; real question construction; unresolved default; dialog content; explicit selection; Other resolution/rejection/cancellation; invalid indexes; task cancellation; partial multi-question answers; no repeated resolved question within continuation; original requirement retention; workspace/reset binding and independent new tasks.
- An injected eligible Clarifier response confirms that unresolved authorization can still block. This exercises production question validation/resolution with the model answer scripted, not real NLI or model reliability.

The retained reviewed controlled CLI executions use scripted model/environment proposals and **real baseline CLI orchestration**, source/context/impact gates, mutation, Falsifier, evidence/transaction handling. Baseline mode is explicitly selected by the test harness; automatic decomposition/classification is not thereby proven. Actual artifacts were copied before test cleanup and independently compared:

| Case / run ID | Actual evidence / scope |
|---|---|
| Employee `20261027T155815-d6bf8902` | Exact original prompt, exact UTF-8 content, Falsifier, done/root_verified true |
| Content decision `20261027T155815-4ab3ac07` | Two incompatible contents `A`/`a`; first turn blocks, next CLI turn explicitly selects; exact `A` file and done/root_verified true |
| Multiple artifacts `20261027T155815-08406a4a` | Exact JSON and Markdown artifacts; native proofs, impact and commit; done/root_verified true; existing low-risk policy skipped Falsifier |
| HTML boundary `20261027T155815-dc7db756` | Actual exact HTML, Builder and Falsifier reached; controlled stop before required browser verification; root_verified false, no final PASS |

The HTML browser boundary is deliberately not mocked as success. The first development suite attempted the real browser path and was interrupted while waiting there. The corrected offline fixture records only the source → Builder → Falsifier → browser-handoff scope. Raw failed/interrupted logs are preserved. It does not establish rendered page behavior or HTML ROOT completion.

Final independent inspection checked all five retained task-artifact files against expected byte hex and hashes, real SQLite tool-result content, native proof coverage and applicable commit/impact events. Employee and content-decision runs have actual Falsifier readbacks; the multiple-artifact run has zero Falsifier calls under the unchanged low-risk skip policy. No Falsifier evidence is invented for that case. HTML has actual readback but no commit/impact-completion claim.

Development failures also included a temporary-directory sandbox access error and a test-helper name collision with the lifecycle fixture's `contract` attribute. These are retained harness failures, not passing tests. Temp output was moved into the private checkout audit directory; the helper was renamed. Imported test-class discovery initially duplicated another suite; the import was changed to a module alias. Assertions were not weakened to hide a production failure. Subsequent negatives exposed case-sensitive literal binding and cancellation/index safety gaps, which were fixed in production and retested.

### 9. Broad regression and baseline debt

Final source passes the existing Level 1 (10), generalized Level 2 (20), literal clarification (9), project-12 continuation (9), requirement clarification (49), R4 verification/integration (12), prior parent functional (4), context-progress (11), dependency scheduler (9), greenfield impact (17), pre-mutation impact (27), context sufficiency (9), verification applicability (15), authority (23), experiment (122), architecture (90), project understanding (32) and model-policy (4) suite scopes. These counts overlap and must not be added.

Verification-policy still has two errors in eight tests. V26 recovery still has 24 failure records, two errors and three skips in 186 tests. Final failure/error IDs are compared against the preceding preserved cohort in the new registry. No new failure ID is concealed or reclassified as a pass. Final retained-artifact review also exposed missing first-turn source/ledger/control-flow metrics in the new decision wrapper; these fields and the source/question counters were restored before the final rerun and are asserted by the two-turn CLI regression. Offline driver exit is 1 because debt remains. The known live requirement test remains explicitly excluded, and offline provider calls are forbidden.

### 10. Genuine replay and environmental boundary

The exact employee prompt was submitted once in a fresh isolated audit workspace using `gemma4:e4b`, normal AUTO CLI routing and unchanged preflight/security. It was **blocked before task ingestion**: `HOST_PREFLIGHT_FAILED`, `CRITICAL_MEMORY_HEADROOM`, resource-monitoring stage, one of three canaries completed, process exit 2. There is no task run ID, source-compilation event, Builder, Falsifier, impact comparison, artifact or ROOT result. Private preflight evidence records falling available memory during qualification; no application conflict result can be inferred from this attempt.

This live attempt preceded the final small cancellation/index and prohibition-grammar hardening. Its source pins are retained as attempted-source evidence, not relabeled final-source. Final reviewed production behavior is established by the controlled tests only. The harness's original `no_false_source_conflict` value was vacuously true with no source events; the curated interpretation is explicitly **not applicable**, and the harness was corrected to emit null for future pre-ingestion failures. The original result file was preserved unchanged.

The separate HTML live replay was **not launched** after this critical headroom rejection. Repeating expensive qualification under the same known resource block offered no new application diagnostic. No preflight was bypassed, no model/service was terminated to free memory, and no timeout/budget was increased. Both exact employee and representative HTML final-source live ingestion/execution remain unverified until host qualification permits a fresh bounded attempt. Earlier genuine baseline runs remain historical and are not substitutes.

### 11. Before/after and generalization boundary

| Mechanism | Before | Reviewed controlled result |
|---|---|---|
| Original employee input | Three fabricated conflicts, zero task tools | No conflict UI; exact source literal retained; real controlled ROOT completion |
| Complementary constraints | Shared negative/positive word could imply contradiction | Different properties/targets/conditions do not create a witness |
| Real exact conflicts | Case folding/weak binding could conceal content differences | Same target different exact values block; explicit decision resumes through real CLI |
| Blocking menu | First source option preselected; question outside dialog | Unresolved default, question/reason inside dialog; cancel/Other failure keep blocked |
| Continuation | Generic decisions not durably associated with original source | Workspace-bound explicit-conflict state; partial answers retained, original ledger auditable |
| HTML | Could stop at false clarification | Real controlled Builder/Falsifier/browser handoff reached; browser success unverified |

Expected generalization follows from property/target comparison and source provenance rather than an employee-specific exception. Demonstrated coverage is the finite matrix above. The grammar is not complete for arbitrary natural language, event coreference, every negation construction or complex conditional requirement. Identical words inside literal payloads and complex policy scope still need broader adversarial coverage before a universal semantic claim. Existing model-originated or repository-phase clarification workflows retain their existing controllers; the new continuation store specifically covers explicit deterministic source conflicts. A newly resubmitted contradictory task can legitimately require a new decision; this is distinct from repeating resolved questions within its continuation.

### 12. Evidence, commands and exact files

Curated phase packet: [false-conflicts-20261027](../evidence/level2-verification-repair-integration/false-conflicts-20261027/README.md). It contains the original failure's selected source/questions, exact request, reviewed controlled records, final test registry, code manifest, source/derivative integrity manifest and explicit blocked live interpretation. Raw databases, prompts/transcripts, all intermediate logs, original hashes and ZIP backup remain privately under the ignored audit root. The 25 October packet and its manifest remain unchanged; its document digest identifies that earlier report snapshot, which is preserved in this phase's backup.

From checkout root, with a **fresh directory name**:

```powershell
.\.venv\Scripts\python.exe -B -X utf8 scripts/verify_level2_offline.py --output-dir audit_runs/manual-r4-conflicts-offline-01
```

This driver sets its temporary workspace under the output root, includes all 18 new tests, forbids live provider calls and reports disclosed debt. Direct unittest discovery may use a system temp directory unavailable in the desktop sandbox; prefer the driver here. Private retained-artifact reproduction code is preserved with the raw cohort and its pins.

After resolving the environmental limitation, independently run **one** live case and inspect it before the next:

```powershell
.\.venv\Scripts\python.exe -B -X utf8 scripts/replay_requirement_consistency.py --live --case employee --output-dir audit_runs/manual-r4-conflicts-employee-01
.\.venv\Scripts\python.exe -B -X utf8 scripts/replay_requirement_consistency.py --live --case html --output-dir audit_runs/manual-r4-conflicts-html-01
```

The replay uses the exact original employee request, not a reworded workaround, and the separate HTML title/inline-style/no-external-CSS fixture. Each has a 360-second outer process bound; underlying provider limits are unchanged. Preflight failure is not an application FAIL/PASS. For any live completion claim, independently inspect actual bytes, context/impact authorization, Falsifier, applicable syntax/browser evidence, transaction and final ROOT status.

The code manifest lists the exact new phase files and hashes: `hivo/requirement_consistency.py`, `hivo/requirement_decisions.py`, `hivo/requirements.py`, `hivo/literal_source.py`, `mini.py`, `tests/test_requirement_consistency_flow.py`, `scripts/verify_level2_offline.py`, `scripts/replay_requirement_consistency.py`, plus this appended report and new phase evidence. Earlier R4 files remain present; no untracked user work was discarded.

### 13. Readiness and remaining tasks

The false-conflict regression is repaired for the demonstrated controlled scope, genuine contradictions remain blocked, literal content is now source-bound, and explicit conflict continuation/UI semantics are exercised through production paths. Live final-source source ingestion and application completion remain blocked/unverified. HTML rendering/browser completion is unverified even in the bounded offline handoff test. General semantic reasoning, provider reliability and previously disclosed broad-suite failures remain open. **R_UPDATE_004 and Level 2 remain incomplete.**

Next evidence needed: restore safe host/model qualification; run the exact employee and separate HTML requests with current source pins; inspect every downstream gate and actual artifact; expand complex scope/condition and model-originated clarification continuation cases without losing authority/provenance; resolve the existing recovery/policy debt separately. No R_UPDATE_005 or Level 3 was started. Branch, HEAD, index and published PRs remain unchanged; all work is local, unstaged, uncommitted and unpushed.

Future local review summary, without publication approval: **Repair source consistency, clarification continuation and literal recursive verification.** Compatible source properties now compose; explicit incompatible values retain source-bound blocking decisions and auditable continuation. Controlled exact-byte and integration checks pass, with critical-memory-blocked live qualification, HTML browser completion and historical broad-suite debt explicitly unresolved. The final packet manifest pins this appended report; the previous report and candidate derivative checkpoints remain privately recoverable.


## Post-Repair Live Evaluation — Recursive Recovery, Ollama Inference Timeouts, HTML Generalization, and Engineering Hardening

Date: 27 October 2026. Status: **INCOMPLETE — local engineering checkpoint**. This phase appends to the preceding false-conflict investigation; its historical claims retain their original source scope. No earlier report phase or original experiment was replaced. The preceding statement that HTML was not launched describes that earlier checkpoint, not the new attempts below.

Evidence: [phase README](../evidence/level2-verification-repair-integration/post-repair-live-20261027/README.md), [historical ledger](../evidence/level2-verification-repair-integration/post-repair-live-20261027/historical-run-ledger.json), [research](../evidence/level2-verification-repair-integration/post-repair-live-20261027/research.json), [test registry](../evidence/level2-verification-repair-integration/post-repair-live-20261027/test-registry.json), [live registry](../evidence/level2-verification-repair-integration/post-repair-live-20261027/live-run-registry.json), [provenance](../evidence/level2-verification-repair-integration/post-repair-live-20261027/provenance.json). Raw private investigation records are retained separately; they are not publication candidates.

### A. Observe: four genuine runs and independent artifact inspection

| Run | Actual boundary/outcome | Metrics and interpretation |
|---|---|---|
| `20261027T160613-55469a33` | Genuine baseline ROOT PASS, done | 7 model calls, 4 tools, Builder 1, Falsifier 1, Repairer 0; 350.96 seconds. Employee file independently matches the source obligation. |
| `20261027T161357-1ee2c633` | Genuine recursive ROOT PASS, done; three children and parent | 72 model calls, 47 tools, Builder 5, Falsifier 5, Repairer 2; 13 timeouts/retries, 3623.58 seconds. Final success is real, intermediate recovery was inefficient and partly misdirected. |
| `20261027T172137-d9c5357c` | HTML Specifier inference timeout, failed/root false | 13 retained source requirements, no clarification; 2 model calls, 0 tools, no Builder/Falsifier/browser; 184.22 seconds. |
| `20261027T174632-342cd69a` | Same HTML request, clean workspace, same Specifier boundary | 13 retained requirements, no clarification; 2 model calls, 0 tools; 179.57 seconds, failed/root false. Preflight 3/3 is not sustained-inference proof. |

Read-only original JSONL traces, experiment metrics and SQLite tool-result rows were inspected. Current files were read as bytes, not inferred from completion text. Employee is 49 bytes, SHA-256 `91023bf45a8f10c835b228cf136b58612c69f618b0d563ca56a3995206761d9e`; products is 41 bytes, `66d0f5c32b72d2edc9af209125f18346c828767b84af10304009cb8e6177516b`; supplier is 46 bytes, `290e00c2af96732a9b48573cf9de857c75f11327855b62ee8223916abc3b27e4`; shipment is 43 bytes, `80e258c1a18bda44c6bdb66b1aef8ef3c2c006a9aa1f2c7911527111fa74c48e`. Exact source requests and source hashes are in the packet. The earlier employee artifact survived the later recursive task.

At investigation entry, mini.py SHA-256 was `f3f5a47461087a4ae9bbb9fe95b78a75dd35cb87b5533bbee874a425aa477428`, matching the user's supplied checkpoint. The historical traces do not themselves pin that file hash per run; temporal association is not cryptographic run-source proof. New replay records pin source bytes before launch. HEAD remains `6f0047ca27e979db10e338357f0fa6a22fe0bf93` with additional local work, so HEAD alone does not identify tested source.

### B. Confirmed timeout mechanism, provider and hardware evidence

The owner of the 120-second deadline is established in source: `OLLAMA_TIMEOUT_SECONDS = 120` flows through `ask_ollama` into `http_post_json`, then `hivo/http_client.py` uses `urlopen(..., timeout=timeout)`. Chat previously used `stream=false`, so slow prefill plus a complete generated response had to fit that blocking operation. The error's former “could not reach” wording conflated slow active inference with absent service.

For the fresh HTML failure, the first role request had approximately 1101 actual prompt tokens, 41.49 seconds prefill, about 0.80 seconds generation and 59.44 seconds HTTP wall time. The second had 1651 prompt tokens; cache mismatch forced full prompt processing, about 71.27 seconds prefill, then generation at approximately 6–7 tokens/second beyond 300 tokens. HTTP ended at two minutes, followed by cancellation of task 7. Subsequent health requests returned 200. This supports a client deadline interrupting active inference; it does not establish an out-of-memory event or a stopped server.

Role trace estimates (1072/1519 for Clarifier/Specifier) differ from actual server counts (1101/1651); they are estimates, not lost requirements. Context was 4096, Specifier output cap 1536, structured output requested, thinking off. The timeout occurred before output admission, not after a malformed Builder tool or browser operation. No mandatory requirements were removed, output cap reduced or retry count increased to obtain progress. Later measured Specifier output was 340 tokens; no evidence establishes that excessive completed output caused the original failure. Prompt slimming remains an experiment, not an established repair.

Read-only hardware and server inspection found integrated Intel graphics. The server explicitly logged dropping the integrated Vulkan GPU unless `OLLAMA_IGPU_ENABLE=1`, then selected CPU inference. This establishes the device-selection policy in that server session, not inability to accelerate, a guaranteed GPU speedup or a model defect. No host GPU settings, drivers, model, Ollama service or memory safeguards were changed. Preflight now explicitly qualifies its PASS: small canaries and sampled resources do not guarantee sustained task inference. Private detailed host inventory remains outside curated evidence.

Historical recursive role wall timings are retained separately. They cover matched completed calls only, omit failed-call duration, and must not be read as server prefill/decode measurements. Ten retry attempts were Builder calls and three Falsifier calls. Most avoidable extra calls came after a mistaken verification-failure classification, but a CPU/provider latency problem remains independent of that controller defect.

### C. Falsifier, Repairer and strategy: actual accepted operations

Child 1 wrote products correctly and native exact-content verification passed. The Falsifier successfully listed/read its local file, then requested sibling reads and `run_file supplier.txt`. These were **refused** by the source-bound literal-artifact scope guard. `run_file` is a native exact-byte route for these literal text artifacts, not shell execution. It selected the wrong child target; it did not execute a supplier script. Read refusals were not themselves output counterexamples, but the refused `run_file` entered generic unresolved-tool-failure handling and incorrectly triggered repair despite correct current local bytes.

Repairer then proposed two writes to products; both were **blocked**, with `IMPACT_CONTRACT_REQUIRED` and trace rejection `GOAL_ANCHOR_DRIFT`. Its narrative `parent_summary` had been supplied as `parent_goal`, while the accepted child contract had a different stable parent anchor. The validator correctly rejected the changed anchor. The caller's context propagation was wrong. Repairer's native run_file checks on products passed; no successful Repairer mutation occurred.

The later “Direct File Write via System Call” string was a model-selected strategy label. Actual accepted execution remained native `write_file` under the same guarded contract hash. It rewrote already correct bytes; the next Falsifier happened to inspect the owned file and passed. There is no evidence of a new system-call capability, permission bypass, content repair or higher strategy authority. We preserve the historical strategy-rescue metric without crediting its label as the causal mechanism.

Production correction projects literal Falsifier tool paths to owned accepted targets and supplies local-versus-parent scope guidance. Dispatch guards remain authoritative if a model ignores the offered enum. A refused out-of-scope probe invokes bounded native local readbacks through `run_tool`; raw refusal evidence is retained. It ceases to be an implementation counterexample only if every owned current file matches its expected digest and has fresh independent Falsifier coverage. Incorrect bytes, stale/forged binding, actual script failures and applicable browser failures still block. Nonliteral executable verification retains its ordinary controlled route. This narrow recovery does not grant arbitrary cross-file access or synthesize a PASS tool response.

`_prepare_task_impact_contract` now records the exact root/parent/local context used to construct authority. `repair_task` reuses the stable root/parent context instead of narrative text; actual changed task goals still fail validation. No anchor validator or mutation guard was weakened.

### D. Parent integration and inventory semantics

The historical ROOT `write_file products.txt` call was **refused** with `READ_ONLY_PARENT_INTEGRATION`; the call name in a console trace was not an accepted write. ROOT performed current native verification across all three files, followed by Falsifier coverage, impact comparison PASS with `changed_paths=[]`, then aggregate completion. Three actual `literal_child_receipt_committed` events exist. The four zero Stage-5 receipt/readiness counters describe a separate optional architecture, not the active literal-composition route. They cannot establish missing proof by themselves and are not relabeled as positive.

Parent instructions now state read-only composition explicitly. New `literal_child_receipts_committed` and `literal_parent_integrations_verified` counters describe actual successful events on this route. Existing optional counters retain their semantics. Controlled production recursive execution establishes three committed children, one verified parent and no Repairer. A test harness RUN status can remain `unknown` if it calls scheduler internals without CLI finalization: the returned scheduler status and root verification are separately asserted. That is not recorded as a genuine CLI done result.

NEW_PROJECT historically meant no detected implementation/source project, not necessarily no files. Four TXT artifacts in project-24 did not create a codebase. This is classification semantics, not cross-workspace leakage. Inventory now separately records `filesystem_empty` and `implementation_empty`; truncated/unknown inventory yields unknown rather than a false emptiness claim. Existing artifact preservation and source classification are unchanged.

### E. Research and architecture decision

The primary-source search and exact metadata are in research.json. Four targeted papers informed distinct decisions:

- Agrawal et al., **Taming Throughput-Latency Tradeoff in LLM Inference with Sarathi-Serve**, OSDI 2024: distinguish prefill/decode cost and measurement; adapt bounded progress-aware client handling, not the GPU scheduler. [Proceedings](https://www.usenix.org/conference/osdi24/presentation/agrawal).
- Shinn, Cassano, Gopinath, Narasimhan and Yao, **Reflexion: Language Agents with Verbal Reinforcement Learning**, NeurIPS 2023 proceedings: useful feedback must reflect the actual failure. Adapt deterministic feedback classification; decline extra model-reflection loops under local latency constraints. The proceedings has five authors; later preprint author lists are not substituted. [Original paper](https://papers.nips.cc/paper_files/paper/2023/file/1b44b878bb782e6954cd888628510e90-Paper-Conference.pdf).
- Saltzer and Schroeder, **The Protection of Information in Computer Systems**, Proceedings of the IEEE 1975: least privilege and complete mediation guide scoped Falsifier capability projection, preserved contract guards and installer rejection. This is design analysis, not an agent empirical benchmark. [Paper](https://www.cs.cmu.edu/afs/cs.cmu.edu/academic/class/15712-s05/www/readings/Saltzer75.pdf).
- Xia, Deng, Dunn and Zhang, **Agentless: Demystifying LLM-based Software Engineering Agents**, arXiv:2407.01489v2, 2024: localize before repair, then validate independently. Adapt the separation, not an entire replacement framework. Its SWE-bench results do not establish Mini Hivo reliability. [Original preprint](https://arxiv.org/html/2407.01489v2).

For each, the registry distinguishes problem, mechanism, author evidence, limitations, architectural fit, costs, safety and deterministic evaluation. No training, model replacement, additional service or framework dependency was needed. Conventional caller-identity propagation and browser dependency discovery do not require a novel academic algorithm. These repairs use existing architectural contracts. Existing R4 proof-binding and transaction research remains historical context, not newly claimed empirical validation.

### F. Production implementation and bounded recovery

`hivo/inference_transport.py::stream_chat` implements bounded NDJSON accumulation. Only Specifier currently uses it: 360 seconds total, 120 seconds inactivity, at most 8 MiB, terminal `done=true` required. First output, wall time and provider prefill/decode/load metadata are retained. Blank/protocol chunks do not indefinitely extend the deadline. Late, cancelled, malformed, incomplete and server-error responses are not admitted as actionable results. Cancellation is cooperative at read boundaries, bounded by the active socket timeout; this is not instantaneous cancellation while blocked. No background inference thread can later dispatch a tool. The client collects complete output before existing parsing/gates. Other roles retain the original bounded transport and retries; their slow calls remain a limitation rather than being silently granted global extra time.

`mini.py::ask_ollama` records role/deadline/stream/output-cap metadata, phase-aware completion timing and typed failure events; HTTP errors remain distinct from absent transport. Cancellation is not retried. Existing retries remain inference-only; no speculative tool action is replayed. Legacy transport-failure aggregates may still contain typed protocol/server inference failures; use the new category event for diagnosis.

Worker/Falsifier, `_safe_literal_policy_refusals`, `_current_verification_failures`, `_falsify_task_body`, contract preparation/Repairer, actual literal receipt registration and parent completion implement the scoped corrections above. Source provenance, requirement ledger, context sufficiency, authorization, Falsifier, syntax/browser applicability, impact comparison and transactions remain required.

Additional production files: `hivo/project_understanding.py::inventory_repository` separates inventory meanings; `hivo/host_preflight.py` qualifies PASS wording. `hivo/http_client.py`, `hivo/model_policy.py` and R_UPDATE_003 remain unchanged in this phase. Earlier local R4 edits to requirements, literal parsing, consistency/decision modules, verification routing and their tests were preserved, not reattributed to this phase.

### G. New HTML boundary and environment hardening

The first new genuine replay, `20261027T182805-227ed5b0`, passed preflight, retained all 13 source requirements, completed streaming Specifier and reached authorized Builder execution. It created index.html and reached real Falsifier/browser checks. It finished **failed/root false**, 727.81 seconds, 15 model calls, 11 tools, one Builder timeout and one retry. This is a new downstream boundary, not HTML completion.

The Specifier used 1651 actual input tokens, 340 output tokens, 47.57 seconds prefill and 41.79 seconds decode; first output was about 47.64 seconds, complete client time 89.43 seconds. It completed under 120 seconds in this attempt. Thus live evidence establishes streaming compatibility and downstream progress, but does not isolate the deadline increase as a speedup or prove that a >120-second live call now succeeds. Controlled clock tests establish the latter transport capability only.

Managed Playwright Chromium was missing. Installed Edge and Chrome were independently detected. Initial browser discovery searched Linux-style PATH names and missed supported Windows channels. A local Edge launch then exited; Chrome successfully rendered the page in an isolated headless profile. The production helper now prefers an available managed browser, then existing PATH/Windows supported browsers, tries another installed channel after launch failure, and bounds each launch at 15 seconds. It installs nothing and does not use a personal browser profile. Supported channels are documented by [Playwright](https://playwright.dev/python/docs/browsers). Multiple candidates can consume multiple bounded launch intervals; browser presence is not a compatibility guarantee.

The preserved 1411-byte intermediate page has SHA-256 `72dd07f40c90b2a8e0fe7361e5df95bdc267188566b20331f43c95ddc76643c0`. Independent DOM readback found title Employee Profile, H1 Sara, Engineering Department paragraph, visible Active status, one internal style and no external stylesheet/script. Mini Hivo's browser snapshot also passed with no console/page/network errors. This is functional browser evidence for the retained artifact, not retroactive ROOT promotion of its failed run.

That run also exposed `npx playwright install` passing command validation and failing only because npx was unavailable. It was **not** a security refusal. npm install and shell listings were refused. The production command validator now rejects npx installation/package-acquisition options and installer subcommands, and inserts `--no-install` for allowed verification tools. Tests assert refusal before process launch and preservation of legitimate verification. This narrows the verification surface; it is not a claim of a complete shell/package-manager security audit. No dependency was installed by these attempts.

### H. Controlled verification and regression outcomes

Behavioral oracles were defined before execution: current exact UTF-8 bytes and expected digests; fresh Falsifier proof under current contract; refused sibling untouched; zero unnecessary Repairer; completed child receipts; read-only parent; no action from cancelled/incomplete inference; no subprocess for installer requests; real browser DOM/text after launch.

Final focused hardening: **27 tests pass**. They cover fragmented UTF-8, fast/slow prefill and decode, total/idle limits, cancellation/late result, protocol/EOF/HTTP500/unavailable transport, bounded retries and exhaustion, scope recovery through actual Worker and ROOT gates, wrong bytes/stale/forged proofs, stable versus changed goal anchors, nonliteral script verification, inventory semantics, actual recursive counters, installer refusal, managed/system browser discovery, failed-channel fallback and narrow optional-resource classification with six negative variants. Scripted model proposals establish controller behavior, not gemma4 reliability.

Two retained controlled functional replays separately exercised actual filesystem and gates: baseline scope recovery returned done/root true with exactly `welcome`, no sibling artifact, no Repairer; three-artifact recursive execution returned done/root true with exact independent expected byte strings, three committed children and one verified parent. Retained copies are available privately; selected byte/hash oracles are in controlled-functional.json. They are not added to suite totals as independent extra passing test counts.

Controlled-boundary qualification from harness review: these fixtures also make structured specification unavailable to exercise the production deterministic contract fallback. The recursive fixture supplies child missions and a fixed execute-fit decision; it invokes the real scheduler, leaves, parent, filesystem and verification gates afterward. It does not test model decomposition/fit quality or reproduce the full interactive CLI. The original raw helper label “model proposals only” was too narrow; the curated derivative explicitly corrects that label and preserves the raw record. Genuine AUTO CLI runs below are the separate evidence for actual specification/routing/model behavior.

Final broad offline command:

```powershell
.\.venv\Scripts\python.exe -B -X utf8 scripts/verify_level2_offline.py --output-dir <fresh-local-output-directory>
```

The retained final cohort is `offline-http-final`, following earlier `offline-final-reviewed` (26 hardening cases) and earlier development cohorts. Passing suite scopes: L1 10; generalized L2 20; literal clarification 9; project-12 continuation 9; requirement consistency 18; new hardening 27; host preflight 20; completed context progress 11; original recovery functional 4; R4 integration 12; dependency scheduler 9; greenfield impact 17; pre-mutation impact 27; context sufficiency 9; verification applicability 15; authority 23; experiment 122; adaptive architecture 90; project understanding 32; model policy 4; requirement clarification 49. These overlap; do not sum them.

Verification policy: 8 run, **2 errors**. V26 recovery: 186 run, **24 failure records, 2 errors, 3 skips**. Driver exit **1**, not all passing. Exact failing/error IDs are preserved and compared with the preceding false-conflict packet; unchanged IDs establish disclosed baseline debt for these runs, not universal irrelevance. Failures in future affected paths still require investigation. The known live-provider requirement test is explicitly excluded; offline provider calls are forbidden. Transport boundary unit tests use fake transport and deterministic clocks, not Ollama.

Development attempts are retained: a direct unittest invocation used sandbox TEMP outside the checkout and produced permission errors; the authoritative offline driver redirects temp output inside the private audit root. Initial host-preflight suite exposed an existing SimpleNamespace fixture lacking `conversation_file`; adding `conversation_file=None` matches the current CLI argument schema and changes no assertions. Earlier uninitialized standalone browser probes reported package unavailable because `_load_optional_imports` had not run; initialized probes separated the real missing-managed-browser/Edge-launch/Chrome-success boundaries. Those harness errors are not counted as application passes.

### I. Remaining issues and readiness

Level 2 remains **INCOMPLETE**. Proven: historical baseline/recursive genuine successes; current controlled scoped recovery, stable contract identity, native proof and read-only parent behavior; real rendered verification of the preserved HTML artifact; final offline regression results above. Unverified until separately recorded: complete final-source HTML ROOT outcome, final-source genuine recursive reliability after these repairs, repeatability across unrelated projects and provider recovery under varied real workloads. Builder/Falsifier still use 120-second nonstreaming inference; the HTML intermediate retry succeeded but latency remains material. No measured evidence justifies blanket streaming/deadline expansion or a universal latency claim.

Critical safety boundaries remain enforced. Open broader-suite debt, finite literal grammar and semantic coverage, local provider memory/CPU variability, browser enterprise policy/version differences and long-running resource exposure remain disclosed. Preflight PASS cannot eliminate these. No Level 3, no new update number and no publication are authorized.

### J. Reproduction and review

Exact original requests are in original-requests.json and the source fixture; do not replace them with shorter paraphrases. Manual local commands, using a fresh output directory for every invocation:

```powershell
Set-Location '<your-mini-hivo-checkout>'
.\.venv\Scripts\python.exe -B -X utf8 scripts/replay_post_repair.py --case smoke --output-dir audit_runs/local-manual-smoke-NEW
.\.venv\Scripts\python.exe -B -X utf8 scripts/replay_post_repair.py --case employee --output-dir audit_runs/local-manual-employee-NEW
.\.venv\Scripts\python.exe -B -X utf8 scripts/replay_post_repair.py --case inventory --output-dir audit_runs/local-manual-inventory-NEW
.\.venv\Scripts\python.exe -B -X utf8 scripts/replay_post_repair.py --case html --output-dir audit_runs/local-manual-html-NEW
```

Run sequentially after qualification, not in parallel. Each task has a 900-second outer process bound and normal AUTO routing; smoke is a tiny availability probe, not task success. For interactive use run `.\.venv\Scripts\python.exe -B -X utf8 mini.py --no-bootstrap`, select a fresh workspace, then paste the exact original request. Check actual bytes/DOM, native/Falsifier evidence, impact comparison, transaction and final root result independently. A process exit 0 is insufficient. A timeout/interruption is not PASS.

Private preserved originals, valid ZIP backup and source/derivative hashes are recorded in preservation/provenance/manifest files. All original project-24/project-25 files and R_UPDATE_003 must remain byte-identical. Existing evidence packet manifests retain their historical report-prefix hashes; the new manifest pins this appended report. No prior packet is regenerated. Git remains on the original WIP branch, same HEAD, empty index, with all changes local. No branch creation/switch, staging, commit, push, PR action or merge occurred. Proposed review wording only: **Harden scoped verification recovery and bounded local inference; retain unresolved Level 2 limits.** This is not a request to publish.

### K. Broader failure classification and review limits

Both failing/error ID lists were compared and are identical to the preceding false-conflict cohort. The verification-policy errors are `FileNotFoundError` for the absent historical benchmark prompt under output/. The V26 foundation loads an absent historical live-3 packet; missing authority/execution identity produces blocked/uncertain classifications and downstream assertions expecting a particular historical identity. Other V26 cases expose invalid legacy failure-envelope fields, absent historical workspace assertions and failed promotion/parent closure (`stage5b` is None, so two tests error when indexing it). These are substantive limits on what can be verified in this checkout. They must not be classified en masse as obsolete assertions or claimed passing.

Current changes do not edit hivo/recovery.py, those V26 test expectations or the historical fixtures. The inspected packet loader is read-only; missing source is not regenerated, imported from the old workspace or fabricated. No new failure/error ID appeared in the final cohort. This supports “no newly observed regression in these suites,” not “all recovery behavior is proven sound.” Their missing-fixture/schema/downstream-closure paths share the general recovery subject area but are distinct from the observed child-local Falsifier refusal and Repairer narrative-anchor caller defect. Baseline debt remains a readiness blocker until authentic fixtures and independent Stage-5 closure are restored/verified in a separately scoped repair.

The [problem registry](../evidence/level2-verification-repair-integration/post-repair-live-20261027/problem-registry.json) records eight issue groups with run/stage identity, original-request reference, expected/actual behavior, exact accepted/refused action semantics, state and authority effects, verification outcome, confidence, source paths, research mapping, rejected alternatives, repair, tests and remaining limits. A safe refusal, model inefficiency, infrastructure failure and instrumentation semantics are kept separate from confirmed implementation defects.

### L. Subsequent HTTP-path defect and final-source retest

The next genuine attempt, `20261027T184821-5b294417`, used the installed-browser correction and created exactly the same 1411-byte page. Browser launch succeeded, rendered title/text matched, but both Builder run_file and Falsifier verify_web_app returned FAIL on a console resource 404. It entered Repairer, then the external 900-second bound interrupted execution. There is no finalized experiment row or ROOT status for this interrupted run. The original replay result has null summary metrics; its run identity and stopping stage come from the retained trace, not an invented final result. It is **not PASS** and the interruption is not reclassified as a completed application failure.

An independent real loopback HTTP reproduction established that the error source was the browser's automatic `/favicon.ico` request, with HTTP 404 and no explicit icon link. The existing response callback already omitted that resource from network errors but its console callback treated the same event as application failure. The earlier file-URL readback could not reveal this HTTP-only discrepancy. This is why real transport/application-path verification was necessary beyond DOM helper tests.

`_classify_browser_console_errors` now separates only an unrequested default-icon 404 on the same local verification origin. Raw console text/source URL and the optional-classification reason remain in the snapshot. Explicit URL references or a favicon requirement, foreign origins, other paths and different errors remain failures. The response callback now retains all error resources before applying the same narrow classification, so an explicitly referenced missing icon is no longer broadly excluded from network consideration. No file is added, CSS/HTML altered or browser gate skipped to satisfy the exactly-one-file task.

Final-source **real HTTP controlled functional** checks: unchanged copied page PASS; explicitly referenced missing icon FAIL; required missing script FAIL. These are real installed Chrome, real server and actual browser callbacks, not mocked browser results. The new unit test covers positive classification and six negatives. Final offline cohort has 27 focused passes and the unchanged broader debt. Retained baseline and three-child controlled replays were rerun with final source pins and again passed their exact-byte, independent verification and parent/transaction assertions. The next genuine original-prompt HTML attempt is recorded separately in the live registry; its final interpretation follows below when the bounded run ends.

### M. Final impact and semantic-profile corrections

The subsequent genuine run `20261027T190608-7757cfd2` completed without provider timeouts: 10 model calls, five tools, one Builder and one Falsifier, 715.04 seconds. Both native browser and Falsifier browser checks passed. Final impact comparison nevertheless failed with eight missing expected targets, and the transaction correctly rolled back index.html. This was a failed ROOT result, not a browser failure or completed task. The original readback remains in SQLite; a fresh derivative reconstructed that readback for diagnostics after rollback. It is not mislabeled as preserved original on-disk byte evidence.

Confirmed root cause: an unscoped nonliteral greenfield root entered `hivo/pre_mutation_impact.py::_identifier_candidates`, which tokenizes ordinary goal words as candidate symbols. With no authoritative physical path scope, these became required mutation targets. The source had explicitly named one output, while impact expected ten word/symbol targets. The comparator correctly rejected unmet expectations; the compiler had supplied the wrong expectations. No comparator or authorization rule was disabled.

`hivo/requirements.py::named_artifact_declarations` now extracts positive create/write/generate declarations for a file/page/document/script/module/component/stylesheet **named/called** a path. `_prepare_task_impact_contract` uses those source declarations for nonliteral NEW_PROJECT roots that lack a prior explicit/child scope. Required physical paths stay separate from semantic verification obligations. Explicit contracts, child authority and existing-project planning retain their prior routes. Source offsets/clauses remain attached; no source content value or target filename is invented. This is a bounded declaration grammar, not a general natural-language file planner.

The first implementation exposed two genuine safety regressions in the broader checks: malformed/overflowed literal requests could re-enter a weaker generic declaration fallback, and a compound literal request could acquire partial scope. Both are preserved in `offline-artifact-final`, then corrected: exact-content requests stay on their stronger literal parser; invalid declaration sets, Windows case collisions and sets exceeding the existing impact bound grant no partial authority. The existing literal limit is ten, while the nonliteral impact target bound is twelve. A new negative initially assumed eleven was overflow; the test was corrected to use the actual bound plus one. Neither production bound was changed. Required semantic obligations retain the pre-existing ten-obligation bound while the full source ledger is retained; independent functional oracles remain necessary, and universal per-requirement semantic proof is not claimed.

Full controlled HTTP testing then exposed another confirmed production issue: the attached authorization hash contained `3d`, and the legacy full-contract JSON substring classifier selected a game profile for a static page. Actual page rendering was correct but canvas/game-bridge assertions failed. The source contract itself had no game requirement. This demonstrates why the earlier helper-only/file-URL checks and literal tests did not reveal this failure.

The correction reuses existing `hivo/verification.py::_profile_semantic_text` via `field_scoped`, previously evaluated as a classification-only checkpoint in Experiment 17. Normal baseline, recursive and AUTO execution now select this policy; CLI choice is propagated explicitly. `--verification-classification-policy current` still selects the legacy comparison behavior. The profile's game assertions remain enforced for genuine game semantics. Only this evidenced classification default changed; context, impact, mutation, surface-discovery, receipt and transaction policies were not broadly altered. Tests cover hash pollution, real 3D-game semantics, CLI default and explicit legacy selection. The host-preflight orchestration test now strictly expects the propagated policy keyword; it was not loosened to accept arbitrary calls.

Research-to-design: source grounding and typed separation prevent authority metadata or English prose from becoming implementation semantics; least privilege narrows mutation capabilities to named outputs; focused failure localization avoids rewriting a correct page for a contract/compiler error. Existing field-scoped implementation was reused instead of introducing another classifier/framework. The actual new behavior is supported by our tests, not by academic benchmark results.

Final controlled HTML replay: `controlled-html-closure-final` reaches done/root true through actual context and impact authorization, write_file, native HTTP browser verification, independent Falsifier read/browser, impact comparison PASS and transaction commit. Its 1,619-byte UTF-8 artifact matches the scripted expected native text-writer bytes. The HTML source did not require LF; an earlier helper incorrectly compared Windows text output against an LF-only oracle. That helper assertion failed even though ROOT passed. Its record is retained, and the corrected oracle documents the user-required encoding and native newline policy rather than changing production output. Literal TXT exact-LF/no-final-newline tests retain their strict byte oracle.

### N. Recovered final-source genuine HTML acceptance

After the usage-limit interruption, the saved final result, trace, actual filesystem, SQLite tool rows and source pins were inspected before another HTML run. No duplicate HTML replay was launched. The completed run is **`20261027T194758-1ef7c59c`**, model **gemma4:e4b**, fresh private `live-html-closure-final/workspace`, using the exact original HTML request in original-requests.json.

| Acceptance item | Independently observed result |
|---|---|
| Tested mini.py source SHA-256 | `37a118499df6dd824b0fcc7998e540e6b972c9c613992331f46c178b932f2591` |
| All recorded source pins | Match the current working-tree source bytes |
| Host preflight | PASS before task execution; no bypass |
| Source and routing | 13 requirements retained, no unnecessary clarification, NEW_PROJECT/AUTO baseline |
| Context and impact | Context sufficient; one accepted/authorized impact contract |
| Builder | done; one accepted page write, native browser verification |
| Falsifier | done; actual read_file and verify_web_app |
| Browser | Three checks; applicable route PASS; field_scoped profile |
| Impact comparison | PASS; index.html changed, zero missing/unexpected/out-of-scope/preservation violations |
| Transaction | One actual transaction_commit; page retained |
| Final result | **done, root_verified=true** |
| Calls/time | 11 model attempts, five tools, Builder 1, Falsifier 1, Repairer 0; 651.05 seconds task elapsed |
| Provider recovery | One actual Builder timeout at 120.034 seconds, then successful bounded retry; one timeout/one retry |

Independent oracle reads the retained **1,507-byte** artifact, SHA-256 **`140fa931879c13e7ee16553258b9ee231bb00fee6495aa8e0e142a7c05112398`**. It decodes as UTF-8, has HTML5 doctype/head/body and UTF-8 charset, title Employee Profile, H1 Sara, Engineering Department paragraph, visible Active label, internal style and no external stylesheet/script. Exactly one task file exists. Browser observations were regenerated independently with an installed supported isolated browser. This is a genuine live-model end-to-end PASS for this request, including actual impact/transaction completion. It does not establish complex-application correctness, all future runs or complete Level 2 maturity.

The successful run also supplies genuine inference recovery evidence: the timed-out Builder request preceded the accepted write; retry did not duplicate mutation. Specifier streaming completed, but the observed successful Specifier duration still does not isolate the 360-second bound as the cause of lower wall time. No claim of a measured global throughput improvement or universal provider reliability is made.

### O. Final regression source and publication readiness boundary

The authoritative broad cohort is now **offline-reviewed-closure**, with **31 focused hardening tests passing**. Other passing suite counts remain those listed in H, with host-preflight 20 and new-hardening 31 replacing earlier checkpoint counts. Exact commands, test IDs, exclusions, source hashes and baseline comparison appear in the current phase test registry. Verification-policy still has two fixture errors in eight tests; V26 still has 24 failure records, two errors and three skips in 186 tests. Driver exit remains 1. Counts overlap and are not added. All final newly introduced hardening cases pass; no newly observed failure/error ID remains in the previously passing suites.

Final-source retained baseline and three-child controlled replays were rerun under the final source, preserving exact artifacts, native/Falsifier evidence, real scheduler/leaf/parent gates and read-only integration. Their prebuilt-child/fit/specification boundaries remain explicitly documented. Final-source genuine recursive completion across the full matrix is still unverified; historical genuine recursive success is retained separately. Keyword-based semantic interpretation and the named/called grammar remain finite. A legacy failure diagnosis can describe a post-impact mismatch as preauthorization failure; the actual authorization and post-comparison events above take precedence. This diagnostic wording remains an open observability limitation, not a reason to bypass the impact gate.

The resumed user instruction authorizes a **new** branch `wip/r-update-004-level2-hardening` only after engineering/publication acceptance; it supersedes the earlier local-only restriction for that final stage. It authorizes no PR action, merge, upstream-main push, history rewrite or change to the R_UPDATE_003 checkpoint. The base remains the existing checkpoint commit `6f0047ca27e979db10e338357f0fa6a22fe0bf93`. PR #8 is a draft depending on prior unmerged work; a new branch from this checkpoint preserves that dependency rather than rewriting it. A future upstream-main PR would include ancestor work until those dependencies merge. [Existing PR #8](https://github.com/kareem232003/mini_hivo/pull/8) was read only.

Publication is conditional on final evidence/integrity/privacy review and the required live-verification boundary, not on pretending all historical suites pass. The result of any extra qualification/recovery attempt and the final publication decision are recorded below. R_UPDATE_003, earlier packet files, original logs and experiment workspaces remain unchanged. **Level 2 remains INCOMPLETE.**


### P. Superseding checkpoint: recursive child source binding and final acceptance replays

Sections N and O describe the source checkpoint `37a118499df6dd824b0fcc7998e540e6b972c9c613992331f46c178b932f2591`. Its HTML PASS and later recovery PASS remain genuine historical results; their source pins no longer match the final repaired mini.py. References there to “current” and “final” apply to that checkpoint. They do not establish successful execution of the subsequent child-binding correction.

A provider-recovery qualification first stopped at HOST_PREFLIGHT with CRITICAL_MEMORY_HEADROOM, before task execution or fault injection. A later approved warm qualification reached run `20261027T202418-3cc93760`: done/root_verified=true, 420.83 seconds, eight model attempts, four tools, one Builder and one Falsifier. Exactly one controlled transport timeout was injected before HTTP dispatch; seven actual completed model responses came from genuine Ollama. The retained employee.txt is exactly 49 bytes, independently equal to the original LF/no-final-newline oracle. This is **controlled transport-fault recovery with genuine model execution**, not evidence of a spontaneous provider outage. Native verification, Falsifier, impact and transaction gates completed. Its source is the earlier checkpoint, not the final child-binding source.

#### P1. Newly exposed recursive failure and earliest established boundary

Run `20261027T203235-92306c8b` used the earlier checkpoint and the original inventory request. It interpreted three literal artifacts and decomposed ROOT into three child tasks. Child 1's goal named only products.txt. Nevertheless its impact candidate had eleven targets and one obligation, and that child accepted writes to supplier.txt and shipment.txt as well. Native run_file on products.txt returned unsupported .txt rather than the expected literal readback route. Independent bytes were wrong: products 43 instead of 41, supplier 48 instead of 46 and shipment 45 instead of 43, due to CRLF instead of source-required LF. The 900-second external bound interrupted execution before completed child receipts, Falsifier, parent integration or finalized ROOT metrics. Final task status/root_verified are null, not inferred failure metrics. The observed scope and byte violations independently block acceptance.

The exact Coordinator scope_hint values were not persisted. It would be unsupported to state that this particular model returned empty hints. Source inspection proves that `_prepare_task_impact_contract` previously selected root literals only through matching optional child hints. Empty or nonmatching hints reproduce loss of literal bindings and fallback to generic semantic targets. The new regressions exercise this mechanism directly. Another confirmed source-shape mismatch is that a frozen Project Brain source uses root_goal, while old call sites looked only for goal and could fall back to a child-local goal. These are controller/source propagation defects; no conclusion depends on attributing a particular unrecorded hint to the model.

#### P2. Production correction and protected boundaries

The final repaired mini.py SHA-256 is `4ff3c7eb18cbc5c0a565e3c2fb16665428f1e722a99d809b6c4096551970d5e8` (raw tested bytes; Git canonical newline bytes are separately reviewed before any publication).

- `_source_goal_anchor` consistently recovers the accepted NEW_PROJECT root_goal, including frozen source shapes, before falling back to task state. Existing-project semantics are retained.
- `_source_literal_child_paths` binds a legacy recursive child to authoritative root literals by validated child goal and/or canonical matching hints. It requires exact source names and contents; unrelated paths, contradictions and ungrounded selection fail closed. It does not infer content or grant sibling authority. Existing immutable Stage-4 child contracts retain their own route.
- `_prepare_task_impact_contract` preserves typed literal bindings and emits explicitly DERIVED source-literal projection obligations when the ledger stores literal rows separately from global policy requirements. Stable IDs, source offsets and digests preserve provenance. Global parent file-count obligations are not falsely marked child-verified. Scope errors leave no authorized paths/obligations and are rejected by the existing validator.
- `_literal_worker_mission_projection` narrows model-advisory legacy literal missions to the validated owned paths, before constructing Worker context. No controller-forced write, fabricated tool response, bypassed gate, increased production budget or broad shell permission was introduced.

The architectural mechanism is source-grounded capability projection: model planning advice cannot replace the accepted source or define mutation authority. This complements the preceding least-privilege/source-separation research decisions. It is not a claim that the cited papers prove this implementation.

#### P3. Why earlier controlled tests missed this path; expanded evaluation

Earlier recursive tests supplied prebuilt children with usable canonical hints and did not exercise the complete Project Brain/MissionCompiler route. Those fixtures proved narrower scheduler/leaf/parent behavior and missed this production source-shape/hint interaction. The new `test_real_recursive_orchestration_with_brain_mission_compiler_and_empty_hints` calls the actual public recursive orchestration, Project Brain/source freezing, mission normalization, scheduler, leaves and parent. Coordinator, MissionCompiler and Worker model replies are scripted; ROOT split/specification are supplied through the documented production builders. The MissionCompiler deliberately proposes overly broad sibling targets, and the controller must narrow each child. It asserts actual exact 41/46/43-byte files, three committed child receipts and read-only parent integration/root success. This is controlled functional evidence, not an interactive CLI or live-model PASS.

The authoritative broader cohort is now `offline-source-binding-reviewed`: **34 focused hardening tests PASS**, host preflight 20 PASS, with previously passing suite outcomes retained. Verification-policy still has two fixture errors among eight tests. V26 still has 24 failure records, two errors and three skips among 186 tests. Driver exit is 1; failure/error identities match the baseline. Counts overlap and are not added. The known provider-invoking requirement test is explicitly excluded. Exact commands, source hashes, counts and IDs are in the test registry.

Fresh retained controlled cases are `controlled-source-binding-reviewed` (baseline, prebuilt recursive and full Project Brain/MissionCompiler recursive paths) and `controlled-html-source-binding-reviewed` (real installed browser, native/Falsifier, impact and commit with scripted models). All passed their independent artifacts/gate oracles on the repaired source. The HTML artifact is 1,619 UTF-8 bytes under the documented Windows native newline policy; the strict TXT LF/no-final-newline oracle is unchanged.

#### P4. Approved final live validation and publication boundary

The user explicitly approved exactly two additional sequential genuine gemma4:e4b replays: original recursive inventory capped at 2,100 seconds, then original HTML capped at 900 seconds. Production budgets and security gates remain unchanged. The recursive replay is `20261027T210935-14cea8e4`, fresh `live-inventory-child-binding-final/workspace`, using the source pinned above. Its outcome must be read from finalized results and independently inspected artifacts/gates; an in-progress trace is not acceptance. The HTML replay will be recorded separately after the recursive process ends.

Publication remains blocked until both approved runs pass their complete independent oracles and final integrity/privacy review succeeds. No further costly live replay is authorized. No staging, branch creation, commit, push or PR action has occurred at this checkpoint. **Level 2 remains INCOMPLETE pending this evidence and the disclosed baseline debt.**


#### P5. Approved 35-minute final-source recursive replay: incomplete

Run **20261027T210935-14cea8e4** used the repaired mini.py hash above and unchanged production budgets/security policies. The driver reached its approved **2,100-second outer limit** (wall 2,100.076 seconds) and interrupted the process. Harness exit is 1; process_exit is null because of the external timeout. The application did not finalize its experiment row: run_id/status/root_verified and other final summary metrics remain null in result.json. The trace establishes identity and partial observations only. No terminal ROOT false/status failed is synthesized from an interrupted process.

Independent retained-artifact inspection:

| Artifact | Expected/actual bytes | Exact original source bytes | Final child state |
|---|---|---|---|
| products.txt | 41 / 41 | PASS; SHA-256 66d0f5c32b72d2edc9af209125f18346c828767b84af10304009cb8e6177516b | Native verification, Falsifier read, impact PASS and committed receipt |
| supplier.txt | 46 / 46 | PASS; SHA-256 290e00c2af96732a9b48573cf9de857c75f11327855b62ee8223916abc3b27e4 | Native verification, Falsifier read, impact PASS and committed receipt |
| shipment.txt | 43 / absent | NOT ESTABLISHED | Context sufficient; interrupted during Builder inference before mutation |

No unexpected task files exist. All three child scope-resolution events select exactly the appropriate own source path; each impact contract has one target and one obligation. There are three successful context-tool calls, two writes, two native run_file proofs and two Falsifier reads: **nine observed tool records**. No prohibited shell attempt, duplicate context-tool loop, sibling mutation or redundant correct-artifact rewrite appears in this trace. Both completed child impact comparisons have zero missing/unexpected/out-of-scope/preservation violations. Two transaction commits and two child receipts are present. Third-child Falsifier, Parent Integration, parent Falsifier, parent impact comparison and ROOT verification were not reached.

Observed trace counts are **28 model requests**, **19 completed provider requests**, **eight recorded inference timeouts** (six Builder, two Falsifier), and one in-flight final Builder retry at interruption. These are independently counted trace observations, not fabricated finalized metrics. The last trace event is Builder attempt 2 with an estimated 3,363 context tokens. Completed prerequisite checks now lead toward legal mutation; the previous eleven-target/unsupported-TXT failure does not recur in the completed children. This establishes a concrete improvement in child behavior, not successful final recursive acceptance.

The eight 120-second failures consumed approximately 960 seconds of recorded client wait before bounded retries. Server diagnostics retained in a fresh private snapshot show active CPU work, request cancellation and slot release. Builder input estimates increase across child histories; complete response latency and repeated role/context preparation remain important costs. This supports a latency/overall-bound stopping diagnosis for this run. It does not prove that environment alone explains all inefficiency, that prompt construction is optimal, or that a longer replay would necessarily succeed. No OOM conclusion or silent deadline increase is made. Improving the remaining cost requires a separately justified change and fresh approved live evaluation; merely granting larger production budgets is not an established repair.

**Acceptance FAILED / workflow INCOMPLETE:** only two of three child artifacts were produced and independently verified, and required parent/ROOT gates are absent. The request's publication condition (both approved replays pass) is therefore unsatisfied regardless of the HTML outcome. No new branch, staging, commit or push is performed. The second approved original HTML replay runs sequentially in a separate fresh workspace and is documented below when finished. No further costly live attempt is authorized.


#### P6. Approved final-source original HTML replay: independently accepted PASS

Run **20261027T214528-8dfdcb28**, genuine local **gemma4:e4b**, used fresh `live-html-child-binding-final/workspace` and the exact original HTML request. It ran after the recursive process ended and server slots were idle, not concurrently. All 14 recorded source/harness pins match the final repaired working tree, including mini.py `4ff3c7eb18cbc5c0a565e3c2fb16665428f1e722a99d809b6c4096551970d5e8`. Process exit 0, no outer timeout, wall 678.064 seconds within the 900-second cap; task elapsed **651.2 seconds**.

Observed final metrics: **status=done, root_verified=true; 11 model attempts, five tools, Builder 1, Falsifier 1, Repairer 0, three browser checks, one inference timeout and one bounded retry**. Ten provider requests completed. The timeout was a Builder request at 120.035 seconds before the accepted page write. No duplicate write occurred. Specifier streaming completed; normal classification was field_scoped, NEW_PROJECT/AUTO baseline.

Actual tools, independently read from SQLite: Builder context_sufficiency_check, write_file index.html, run_file index.html; Falsifier read_file index.html and verify_web_app index.html. Both browser tool results have passed=true. Builder finished with sufficient context and accepted impact authority; Falsifier remained read-only. The aggregated verification evidence passed. Final impact comparison is IMPACT_CONTRACT_PASSED, changed_paths=[index.html], with zero missing, unexpected-related, out-of-scope or preservation violations. Exactly one transaction_commit retained the file. No child/parent receipt counter is expected for this baseline case.

A separate installed-browser DOM inspection after completion independently verified the **actual retained 1,507-byte UTF-8 file**, SHA-256 `140fa931879c13e7ee16553258b9ee231bb00fee6495aa8e0e142a7c05112398`: HTML5 doctype, html/head/body, UTF-8 charset, title Employee Profile, H1 Sara, Engineering Department paragraph, visible Active label, one internal style block, no external stylesheet/script and no additional task files, including nested task paths. It is byte-identical to the private snapshot captured before Falsifier and to the earlier HTML checkpoint's artifact. Identity of bytes does not substitute for this run's own trace, actual write and final gates; those were inspected independently.

This is **live-model end-to-end functional verification for this original HTML request on the repaired source**, not a scripted test. [Current HTML acceptance](../evidence/level2-verification-repair-integration/post-repair-live-20261027/genuine-html-acceptance.json), the live registry, source manifest and artifact provenance distinguish it from the older source checkpoint. The earlier curated checkpoint records and artifact remain preserved separately; the current HTML derivative uses a run-specific filename. Original bytes remain private and unchanged; any LF-normalized publication derivative has its own SHA-256.

#### P7. Final review, preservation and LOCAL readiness decision

Both approved costly replays have ended. No additional live inference was launched. The final production/test source has not changed since the 34-test hardening and broader offline cohort. Rechecking **all 63 recorded offline source/test hashes found zero mismatches**; runtime implementation was frozen for both genuine runs. The current retained controlled baseline, prebuilt recursive, full Project Brain/MissionCompiler recursive and installed-browser HTML cases remain controlled functional evidence, not genuine-model reliability claims.

Regression outcomes remain as recorded in the current test registry: all 34 focused hardening cases pass, as do the separately listed Level 1 (10), generalized Level 2 (20), R4 verification integration (12), host preflight (20), context, impact, authority and scheduler cohorts. Verification-policy retains two missing-fixture errors among eight tests; V26 retains 24 failure records, two errors and three skips among 186 tests. Driver exit is 1; failing/error IDs are unchanged from baseline. Overlapping suite counts are not combined. These known failures are not repaired or reclassified as passes.

Preservation checks independently validate all **16 original experiment files** from the initial phase and unchanged R_UPDATE_003, valid original backup CRC, unchanged prior false-conflict packet and intact historical R4 report prefix. The later interrupted scope-failure run's **ten original files** also remain unchanged, with a valid separate backup. These are distinct preservation cohorts, not an assertion that every historical file in the repository was rehashed. New raw traces, SQLite/sidecars, server snapshots, private backups and generated workspaces remain ignored/local.

The reviewed file audit includes all relevant current R4 production, tests, harnesses, scoped Git configuration, report and curated evidence; no tracked/untracked change lies outside that reviewed scope. It explicitly excludes private original runtime files and the ignored audit tree. Candidate privacy review distinguishes the pre-existing synthetic C-project classifier paths and the synthetic Apps browser fixture from real machine paths. No actual credential or personal-path finding remains in the reviewed candidate. Canonical LF derivative/report hashes are checked locally. **No staging occurred, so actual staged Git-blob publication validation and a publication manifest are deliberately not claimed.** They remain conditional on a future accepted publication checkpoint.

**Publication decision: BLOCKED.** The latest instruction requires both final-source live replays to pass. The HTML replay passes; the recursive replay is incomplete, with a missing third file and absent parent/ROOT verification. Therefore the new branch `wip/r-update-004-level2-hardening` is not created; no staging, commit or push is performed. HEAD remains checkpoint `6f0047ca27e979db10e338357f0fa6a22fe0bf93` on the existing local branch, with R4 changes left available in the working tree. No existing PR, published checkpoint, upstream main or Git history is modified, and no PR/merge is performed.

**Level 2 remains INCOMPLETE.** The remaining acceptance blocker is successful genuine final-source recursive completion through the third child, independent verification, Parent Integration, parent Falsifier, impact and transaction/ROOT gates. Trace timing and input construction deserve further targeted investigation; additional costly live replays require new user authorization. This report does not assert that a larger timeout alone would establish correctness.

For independent Windows testing, use [REPRODUCE](../evidence/level2-verification-repair-integration/post-repair-live-20261027/REPRODUCE.md): baseline employee exact bytes, bounded original inventory, bounded original HTML and optional disclosed transport-fault scenario, each in a fresh directory and sequentially. Inspect the exact artifacts and full gate milestones, not final prose. The inventory command is a known incomplete bounded reproduction on this host, not a promised PASS.

Team review summary: the update addresses false requirement conflicts, source/authority separation, literal verification handoff, scoped Falsifier/Repairer behavior, read-only parent composition, browser/command security and source-bound impact/profile selection. The latest repair binds legacy child ownership to root values instead of optional planner hints and consistently preserves the frozen root goal. Controlled regressions and genuine HTML pass; genuine recursive partial progress is improved but full acceptance remains missing. A future review title may be **WIP R_UPDATE_004: harden source-grounded verification and recursive child scope**. No completed-publication claim or PR submission accompanies this local candidate.


## Q. Final Recursive Child-3 Investigation and Bounded Inference Recovery — 27 October 2026

This phase continues section P and preserves all prior evidence. References there to final source describe mini.py 4ff3c7eb18cbc5c0a565e3c2fb16665428f1e722a99d809b6c4096551970d5e8. The genuine HTML PASS 20261027T214528-8dfdcb28 remains historical acceptance on that source. The new transport source is independently pinned below; a scripted HTML check on it is not relabeled a fresh genuine HTML run.

### Q1. Observe and investigate the complete 35-minute execution

The entire trace, copied SQLite database/sidecars, all model request/completion/failure events, controller transitions, scope/authorization events, native proof and receipt events, and retained server snapshot were inspected. Analysis uses private copies; originals remain untouched. Trace/server times below are Africa/Cairo; SQLite retains explicit UTC offsets. Full per-request data and eight matched server-prefill excerpts appear in the current phase timeline evidence.

| Component | Start (Cairo) | End / interruption | Wall seconds | Model requests | Recorded timeouts |
|---|---|---|---:|---:|---:|
| Initial source/specification/root planning | 21:09:35.594 | 21:14:38.894 | 303.300 | 4 | 0 |
| Child 1: products.txt | 21:14:38.894 | 21:25:12.013, done | 633.119 | 9 | 3 |
| Child 2: supplier.txt | 21:25:12.029 | 21:36:24.415, done | 672.386 | 9 | 3 |
| Child 3: shipment.txt | 21:36:24.430 | about 21:43:59, outer cancellation | 454.570 | 6 | 2 |

Child 3 was not skipped, deadlocked or denied scope. Coordinator chose EXECUTE at 21:37:39.306; mission preparation finished and Builder began at 21:39:08.883. Its contract owned only shipment.txt. Context sufficiency and impact authorization completed before the context tool returned at 21:41:48.525. The following request was the write-generation model call, not a write_file tool operation. It timed out at 21:43:48.555 and immediately retried at 21:43:48.757. The external cap cancelled that retry approximately ten seconds later. No third file mutation, child verification or receipt occurred. SQLite correctly retains children 1/2 as done and ROOT/3 as running after external process interruption; it does not fabricate terminal failure or success.

Each completed child had one context check, one write, native exact readback, Falsifier read, impact comparison PASS with only its owned path changed and no violations, transaction commit and a valid receipt. The first two files remained exact 41/46-byte source outputs after later provider failures. The scheduler advanced only after those successful commits. No stale child authority, repeated completed-context loop, cross-child mutation, unnecessary Repairer cycle or parent re-entry is evidenced in this run. Parent Integration was not reached; its correctness cannot be inferred from two child passes.

### Q2. Where the 2,100 seconds went

Task-provider waits total approximately **2,060.398 seconds**, comprising 1,090.047 seconds for 19 completed requests, 960.108 seconds for eight timed-out requests, and about 10.243 seconds for the interrupted final retry. The 960 seconds are recorded failed-request waits, not a proven amount of removable overhead: partial prefill may be reused by the provider retry cache. No equivalent speedup or fully repeated-prefill cost is inferred. The remaining task-controller/tool gaps total about 3.008 seconds; host preflight and harness startup account for the approximately 36.670-second residual. Totals reconcile to the driver's 2,100.076-second wall measurement. Initial planning and child spans are subdivisions of this same budget, not additional time. Server cancellation timestamps have one-second precision, so residuals and interrupted duration are approximate.

All eight failures were Builder (six) or Falsifier (two), stream=false, think=false, with the same 120-second HTTP boundary. Builder num_predict remained 4096; Falsifier remained 1536. Every failure retried once with the same source-supported provider payload construction. No tool was dispatched from the timed-out response. The raw trace lacks full payload hashes, so byte-identical retry payloads are supported by code inspection rather than independently observed request-body digests.

The server snapshot matches each timeout's second to a cancelled POST and active **incomplete prompt processing**. Actual server input counts were 2,748–4,264 tokens, larger than client message estimates because tool/schema/template input is not fully represented in that estimate. Recorded partial-prefill rates were approximately 22–32 tokens/second. At cancellation, progress examples include 2,131/3,155, 2,901/3,925 and 3,240/4,264 tokens. None of the eight excerpts establishes completed prefill or token generation before the cutoff. The previous general phrase “active inference” is refined here to observed prefill, not asserted decode. The nonstreaming client had no progress events to distinguish cold work from a dead connection.

Confirmed mechanism: slow cold prefill plus an unsuitable fixed initial-response boundary for these Worker roles caused avoidable timeout classification and equivalent inference retries. Large prompts and role/context reloads contribute cost; no arbitrary prompt field has been proven dispensable. This is not evidence of model inability to create shipment.txt or a scheduler correctness defect. It does not establish environment-only causation or optimal prompt construction. Extending the outer wall limit alone would not correct the false timeout/retry mechanism.

### Q3. Research and design decision

The existing Sarathi-Serve analysis remains relevant for separating prefill from decode; its GPU scheduler is not imported. A focused primary-source follow-up reviewed Jeffrey Dean and Luiz Andre Barroso, **The Tail at Scale**, Communications of the ACM 56(2), 74–80 (2013), DOI 10.1145/2408776.2408794, https://research.google/pubs/the-tail-at-scale/ and the original https://barroso.org/publications/TheTailAtScale.pdf. The paper studies latency variability/amplification and reports distributed-service mitigation measurements. Measurement-driven latency handling transfers; hedged duplicate requests require spare replicas/resources and are rejected for this single CPU provider. Its workloads do not prove agent correctness or justify our timing constants.

Official Ollama tool-streaming documentation, https://docs.ollama.com/capabilities/tool-calling, specifies accumulation of content/thinking/tool-call fields. Mini Hivo keeps a stricter execution boundary: no partial tool call is actionable before the complete bounded response is admitted. No SDK, framework, training, GPU configuration, parallel inference, extra reflection model or package installation is added.

Chosen correction: reuse bounded NDJSON transport for **Builder and Falsifier only**, with a measured cold-first-output allowance, generation inactivity watchdog and fixed total deadline. The first-output allowance is 240 seconds: the observed largest 4.3k-token prompt at the slower measured rates plus loading/formatting overhead can exceed 120 seconds while remaining inside this explicit bound. It is not a measured optimum or universal model policy. Once meaningful output begins, the 120-second inactivity watchdog applies. Every request has a 360-second total cap; heartbeats do not extend first-output/total limits. Other roles retain their previous policies, including Repairer. Specifier retains its existing 360-total/120-initial/120-idle behavior. Output limits, retry counts, task budgets, source/authorization/context/grounding/Falsifier/impact/transaction gates remain unchanged.

### Q4. Implementation and controlled verification

Production changes are limited to `hivo/inference_transport.py::stream_chat` and `mini.py::ask_ollama`. Transport distinguishes optional first-output silence from generation inactivity, bounds headers and socket reads by the applicable remaining allowance, emits typed first-output timeout errors, records limits and rejects malformed tool-call containers. Completed chunks are accumulated but no partial, cancelled, incomplete, over-limit or late response is admitted. ask_ollama selects the policy only for the evidenced roles and logs first-output/idle/total limits plus tool-schema size. Retry-count/output-budget assertions remain intact.

The replay driver accepts an explicitly requested outer limit up to 3,000 seconds and records existing parent_integrations_passed/verified_nodes/failed_nodes metrics. Its default is still 900 seconds. The disclosed fault-injection harness now intercepts both HTTP and streaming boundaries so its one pre-dispatch Builder fault is not silently skipped after the transport change. No new live fault experiment was run.

The new `tests/test_child_inference_recovery.py` has **eight passing tests**: old-versus-new cold first-output behavior; bounded silence/heartbeats, generation idle and absolute total time; full versus incomplete/malformed tool-call streams; cancellation; scoped role policy; real production Child 3 execution; denied sibling mutation; and failed/partial responses with no mutation or committed receipt. Subcases are not added as separate tests. The child diagnostic uses real ask_ollama, parser, Worker/leaf gates, authorization, native/Falsifier verification, impact and transaction/receipt code. NDJSON model messages and the 180-second clock are scripted; sibling files are seeded from source. It does not exercise live inference, Project Brain/MissionCompiler or Parent Integration by itself.

Controlled Child 3 produced exactly 43 UTF-8 bytes, SHA-256 80e258c1a18bda44c6bdb66b1aef8ef3c2c006a9aa1f2c7911527111fa74c48e, authorized only shipment.txt, left both siblings unchanged, passed impact and committed a genuine controller-generated receipt. Separate full recursive orchestration remains covered by the source-matched hardening suite. The new source also passed the retained controlled original-HTML flow through an actual installed browser, Falsifier, impact and commit: done/root true, 1,619 bytes matching its explicitly scripted/native-newline oracle. This is controlled functional verification, not a fresh genuine HTML PASS.

Before/after broad offline cohorts retain **34 hardening passes**, Level 1 10, generalized Level 2 20, R4 integration 12 and all other previously passing suite outcomes. The new eight cases pass separately. Verification-policy still has two fixture errors in eight tests; V26 still has 24 failure records, two errors and three skips in 186 tests. Failure/error IDs are unchanged; driver exit remains 1. Counts overlap and are not combined. The known provider-invoking requirement test remains excluded. All final tested-source pins match the frozen working tree.

Development errors are preserved: running the new module directly first encountered sandbox temporary-directory permission/cleanup errors; the established offline driver uses a repository-local temp tree and resolves that harness boundary. A negative sibling test initially treated the legitimate subsequent Repairer request as an unexpected network call. Its fixture now explicitly simulates unavailable legacy transport there while preserving assertions that siblings remain unchanged, no child receipt is fabricated and the leaf is not done. No production gate was weakened to resolve that test failure.

### Q5. Final-source genuine replay and current publication boundary

Tested mini.py raw SHA-256: **128d021f8687497dfff16ac9c284093d69f69aa59232b4f447975c86751b1e7a**. Transport raw SHA-256: **83cc18cae05827d7f62f2a0f4b515ee8195cc4c1323a24293ff6409b069667e2**. No production edit is permitted during the replay without invalidating this source checkpoint.

The first launch was rejected before process creation by automatic approval review because the attached-file authorization was not accepted as trusted direct consent for another costly run. No output workspace, run ID or model call resulted. A direct chat confirmation was then obtained: **Approve one replay, up to 50 minutes**. The single approved full original-inventory replay is now **20261027T223818-f8bbcf6e**, fresh `live-inventory-final50/workspace`, outer cap 3,000 seconds. No older replay was running; read-only provider health showed the model installed and no loaded inference workload before preflight. Normal host preflight passed three canaries. It is an in-progress attempt, not acceptance.

The complete run must establish all three exact source artifacts, verified/committed child receipts, read-only parent integration, independent parent Falsifier, impact comparisons, transaction completion, status=done, root_verified=true and parent_integrations_passed=1. Missing, stale or partial evidence remains a failure. Publication remains conditional and no branch/index/commit/push/PR change has occurred at this checkpoint. The final result and publication decision are appended after inspection. **R_UPDATE_004 and Level 2 remain INCOMPLETE until that evidence exists.**


### Q6. Approved final-source replay: three children verified, parent incomplete — 28 October inspection

**Problem → Evidence.** The single directly approved replay, **20261027T223818-f8bbcf6e**, used genuine local gemma4:e4b and the frozen source in Q5. Inspection after the interrupted session found no remaining Python replay process, no final driver result.json and no finalized application metrics. Original logs were not filled in or modified. A fresh private ZIP and inspection copy preserve all ten original run files; their hashes remain unchanged and the ZIP CRC check passes. SQLite was read from the inspection copy.

All three children completed before parent integration:

| Child | Artifact | UTF-8 bytes | Exact source SHA-256 | Child completion (Cairo) |
|---|---|---:|---|---|
| 1 | products.txt | 41 | 66d0f5c32b72d2edc9af209125f18346c828767b84af10304009cb8e6177516b | 22:51:14.005 |
| 2 | supplier.txt | 46 | 290e00c2af96732a9b48573cf9de857c75f11327855b62ee8223916abc3b27e4 | 23:01:08.761 |
| 3 | shipment.txt | 43 | 80e258c1a18bda44c6bdb66b1aef8ef3c2c006a9aa1f2c7911527111fa74c48e | 23:11:42.499 |

Independent binary reads match every original literal oracle, with LF and no final newline. No extra task artifacts exist. Each child has sufficient context, scoped impact authorization, one write, passing native run_file readback, a successful independent Falsifier read, impact PASS changing only its owned path with zero missing/unexpected/out-of-scope/preservation violations, transaction commit and a distinct receipt-commit hash. The copied database records children 1/2/3 as done. These are genuine child-level results, not controlled model fixtures. The retained receipt-commit events establish controller issuance; they are not a claim that a serialized receipt was independently revalidated in a completed parent integration.

**Parent boundary.** Parent integration began at 23:11:42.547 with zero preflight conflicts/invariant violations. Its first context-generation request began at 23:11:42.626. A failure at 23:29:33.121 recorded INFERENCE_DEADLINE after **1,070.492 seconds**, despite a configured total limit of 360 seconds. The late response was not admitted. Retry 2 completed in 37.192 seconds and supplied a context-check tool call. Parent context sufficiency and impact authorization completed at 23:30:10.610–.617. The trace ends at the next parent Builder request at **23:30:10.631**. There is no parent Falsifier, parent impact comparison/commit, parent terminal PASS or ROOT verification event. SQLite retains ROOT/run as running with no finished_at. This persisted state is not a claim that a process is still active.

The trace contains 25 model requests, 23 completed provider requests, one recorded provider failure, one final request without an outcome, three child receipt-commit events and three commits. Its first-to-last timestamp span is **3,111.649 seconds**, already beyond the requested 3,000-second outer limit. That span is not the driver's unavailable total wall time. Do not report successful hard wall-cap enforcement, an outer_timeout=true result, an exit code, status=done, root_verified=false/true or a numeric parent_integrations_passed value without actual final metrics. Required completion checks are unestablished, not synthesized application failures.

**Root cause and limitations.** Child 3 now completed; the previous eight cold-prefill cutoff mechanism did not recur in the children. Several completed first-attempt Worker requests exceeded the former 120-second boundary; the first completed in 135.835 seconds. This supports the role-specific first-output correction, not a general speedup claim: both source and outer allowance changed, and caching/load vary. The new parent deadline overrun exposes a separate unverified timing boundary. Source inspection shows deadline checks before/after blocking reads and socket deadlines, plus subprocess timeout in the driver. These mechanisms reject late content once execution resumes; this run does not prove prompt interruption under host scheduling or suspension. Host sleep/resume, socket blocking and external process/session interruption remain hypotheses. System event-log access was unavailable. Neither host suspension nor a particular transport defect is established as the cause. No speculative production patch or further costly replay was applied.

**Results.** The replay is **INCOMPLETE**, not a full recursive PASS. The [independent inspection](../evidence/level2-verification-repair-integration/child3-inference-recovery-20261027/live-independent-acceptance.json) separates observed child evidence from unavailable final metrics. Its false acceptance checks mean required evidence is missing; three receipt events and successful child artifacts are explicitly retained. Exact nonprivate artifact copies and provenance are included in the current local candidate packet. Raw transcripts/databases remain private and unchanged.

### Q7. Final local review and publication decision

The Q4 final offline cohort is still source-matched: all 67 frozen source/test/harness pins match the current files. No implementation edits were made after launching the replay. The 34 hardening and eight new inference cases passed separately; the other previously passing relevant suites retained their outcomes. Verification-policy two fixture errors and V26 24 failure records/two errors/three skips remain disclosed. No broad all-tests-passing claim is made and overlapping counts are not added. No additional runtime suite was needed for the documentation-only inspection follow-up.

The genuine original HTML PASS 20261027T214528-8dfdcb28 (651.2 seconds, 1,507 bytes, browser/Falsifier/impact/commit) remains evidence for its earlier source only. The current-source HTML evidence is controlled with an actual browser and scripted model boundaries. Earlier packets and R_UPDATE_003 remain unchanged. The phase manifest records current canonical LF candidate hashes; no staged-Git-blob validation is claimed because the index remains empty.

**Publication is blocked. R_UPDATE_004 and Level 2 remain INCOMPLETE.** The required final-source parent/Falsifier/impact/transaction/ROOT acceptance was not established, and the observed deadline/outer-limit overrun needs diagnosis before relying on another bounded live attempt. No new branch, stage, commit, push, PR change or merge was performed. The working branch remains wip/r-update-003-level2-checkpoint at 6f0047ca27e979db10e338357f0fa6a22fe0bf93. The proposed new branch remains uncreated. No Level 3 work was started.

Future review wording must describe a WIP transport/verification hardening candidate, not completed Level 2. Next engineering work should isolate host scheduling and actual socket/driver timeout behavior with process-lifecycle/timing evidence, preserve the existing completed children, and obtain separate approval before any additional expensive replay. Do not resume the old task by modifying its evidence or treat it as completed. Independent Windows commands and exact oracles remain in [REPRODUCE](../evidence/level2-verification-repair-integration/child3-inference-recovery-20261027/REPRODUCE.md); keep the machine awake during a diagnostic run, execute sequentially in fresh workspaces and inspect final gates. Those manual instructions do not authorize another assistant run.

Final local documentation/integrity review: all 67 frozen pins match; all protected prior evidence and R_UPDATE_003 remain unchanged; the latest ten run originals match their preserved hashes and backup CRC. The explicit inclusion/exclusion audit remains a blocked candidate review. Scoped privacy scanning found no credential or private-machine-path findings after verifying pre-existing synthetic classifier fixtures against HEAD. git diff --check passes; the index is empty. This is local-candidate validation, not staged-blob validation or permission to publish.


## R. Parent Integration Deadline and Supervision Repair — 28 October 2026

This chronological phase resumes Q without replacing its historical observations. Q6 correctly recorded unknown suspension/termination causes with the evidence then accessible. Narrow read-only access to Windows power events now establishes the standby interval; the final process-termination cause remains unknown. Child 3 is no longer the observed blocker. R_UPDATE_003, PR #8 and all prior evidence remain unchanged.

### R1. Problem, evidence and confirmed causes

**Problem.** Genuine run 20261027T223818-f8bbcf6e committed all three exact child artifacts, then stopped before parent/ROOT verification. A Parent Builder request recorded 1,070.492 seconds despite configured total 360, first-output 240 and generation-idle 120 seconds. The original replay lacked a durable supervisor record and final result.json.

**Evidence.** Windows Kernel-Power event 506 reports entering Modern Standby at **23:13:25.6538323+03:00**; event 507 reports exit at **23:29:32.9204929+03:00**. The interval is **967.266660 seconds**. The parent request began at 23:11:42.626; the client recorded INFERENCE_DEADLINE at 23:29:33.121, approximately 0.201 seconds after resume. An earlier standby interval (23:09:03.843–23:09:57.469) occurred during Child 3; it still completed. Modern Standby may permit brief background activity, so its entire duration is not asserted to be measured CPU-off time.

The retained provider log shows parent model loading in 18.40 seconds, 4,326 prompt tokens, incomplete prefill progress at 1,024/2,048/3,072 tokens, then an HTTP 500/cancel at 23:29:32 with 3,302 tokens retained. The retry reused that prefix and completed in 37.192 seconds. No first-attempt stream chunk or tool call was admitted. The final parent request then processed a new 4,325-token prompt and disconnected at 23:31:50 during incomplete prefill. That server disconnect does not establish which external actor ended the client.

**Exact observability boundary.** The old trace locates the gap inside the synchronous inference transport, before recorded stream output. It did not record exception phase, header arrival or a stack sample; copied SQLite contains no fuller exception. It cannot conclusively distinguish urllib.open/header wait from the first read1 call. No stack or exact suboperation is invented. The new inference_wait events identify these boundaries for future runs. Provider prefill and the power events establish a host suspension overlap, not an authorization denial, scheduler deadlock or parent mutation defect.

**Confirmed software mechanisms.** The original stream transport evaluated controller cancellation/deadline predicates only before and after a synchronous opener/read. Such checks cannot run while that call is blocked or the host suspends. The existing after-read gate correctly rejected expired output after resume; it did not promise prompt cancellation during a blocked operation. Separately, installed Python 3.14.8 Popen._wait calls Windows WaitForSingleObject once with the entire process timeout. On Windows 8 and later that wait excludes low-power time, so subprocess.run(timeout=3000) was not the assumed suspend-inclusive elapsed supervisor. This explains why work could continue beyond the intended wall-clock deadline. No historical supervisor log exists to prove the ultimate kill cause or its exact elapsed limit. The absence of final driver output remains a separate provenance limitation.

### R2. Established engineering references and design decision

Primary reference: [Microsoft WaitForSingleObject](https://learn.microsoft.com/en-us/windows/win32/api/synchapi/nf-synchapi-waitforsingleobject), specifically its Windows 8+ low-power timeout semantics. [Microsoft system power states](https://learn.microsoft.com/en-us/windows/win32/power/system-power-states) describes Modern Standby. The installed Python Popen._wait source and QueryPerformanceCounter-backed monotonic clock were inspected locally, rather than assuming all operating systems implement subprocess timeout identically. These references explain the mechanism; our controlled tests establish the implemented behavior.

Choose an absolute elapsed deadline rechecked by a supervisor using short waits, with separate I/O ownership. No process can enforce a wall deadline while its CPU is suspended. The guarantee is rejection and cancellation on the next scheduled check after resume, within short polling/cleanup allowances under a responsive host. Do not increase limits, prevent manual sleep, change system power settings, replace recursive execution or skip the parent. The earlier prefill/decode and least-privilege research decisions remain applicable; no additional framework, dependency, model training or parallel inference is introduced.

### R3. Production and harness changes

- **hivo/inference_transport.py:** _RequestIO owns one disposable daemon I/O worker per request. Only the supervising caller parses/adopts output; the worker executes no tools and touches no controller state. Header acquisition and each read are submitted separately, preventing the worker from consuming the whole response ahead of admission. The supervisor rechecks first-output/idle/total deadlines and cancellation using short queue waits. It checks again before accepting buffered output after resume. Existing NDJSON accumulation, response-size bound, full done=true requirement and protocol validation remain. HTTP error-body reads also pass through the same bounded boundary. Cleanup requests socket shutdown and closes the response in the worker, with bounded joining. If an unresponsive opener has not exited, cleanup_pending/retry_safe prevents a concurrent retry; a stalled I/O worker cannot authorize a tool. A blocked native operation may remain until the OS releases it; it is not falsely reported reaped.
- **mini.py::ask_ollama:** accepts an optional cancellation predicate for streaming, records inference_wait phase/elapsed events and failure phase/cleanup status, and refuses retries while old I/O cleanup is pending. Existing retry and token/tool budgets are not raised. Cancellation is not retried. These changes do not grant tool capabilities or alter source/context/impact/transaction gates.
- **hivo/process_supervision.py:** supervises the explicitly launched child with a monotonic deadline, short polls, cancellation/KeyboardInterrupt handling, termination/reaping and terminal supervision events. It checks expiry before accepting a late observed exit. It never terminates a shared Ollama service. It owns the direct launched process; it does not claim general process-tree cleanup. Process creation and a completely suspended/unresponsive OS cannot be given an unconditional hard real-time guarantee.
- **scripts/replay_post_repair.py:** replaces the one long subprocess.run wait, preserves launch-time source hashes before startup and writes durable supervision.jsonl with timestamps and terminal reason. Final result separates process exit, supervisor reason, host/application outcome and actual nullable metrics. PASS additionally requires normal supervised completion, exit 0 and actual done/root_verified=true. Launch/setup time is deducted from the outer allowance.
- **tests/test_parent_deadline_recovery.py:** 12 new tests described below. **tests/test_update004_verification_integration.py** adds an optional provider adapter to its existing real scheduler/child/parent fixture; default behavior and existing assertions remain unchanged. **scripts/verify_level2_offline.py** includes the new tests and process supervisor source pin.

These seven source/test/harness files are the incremental changes in this phase. Earlier R_UPDATE_004 source, tests, documents and evidence remain part of the complete local candidate. Full hashes appear in the phase frozen-source and code-change manifest. Current raw mini.py SHA-256: **c372c9197e1c3d2f923b0e63623f176d71d799add844c8a7be0f8d309022a4d6**. Transport: **0017b2760c49a3868e556d328cd1b19a2258c300900a84e66fbf78516a8ed78c**. Process supervisor: **a1d3b7cd2a6aea5c05541a4125fa66841f88bf3b8f1bc55fcff2108038dd89aa**. No source edits followed the approved replay launch.

### R4. Focused deterministic and controlled functional verification

**Twelve new tests PASS.** These cover blocked header/read cancellation; blocked-I/O deadlines; a simulated 1,070.492-second resume jump rejecting late results; refusing concurrent retry when connection cleanup remains pending; process deadline checks after resume; process cancellation and KeyboardInterrupt cleanup; an actual sleeping Python subprocess terminated/reaped at a short deadline; normal real subprocess completion; and four production parent scenarios. Tests use real threads/processes and real elapsed short bounds where indicated. The suspension jump is deterministic, not a test that physically suspends the PC. No provider model is invoked.

**Four retained controlled functional runs** exercise the real scheduler, child leaf execution, source/context/authorization gates, exact filesystem mutations, controller-issued child receipts, parent Worker/ask_ollama/NDJSON boundary, native proof, Falsifier, impact and transactions. The child DAG/proposals and parent model responses are scripted. Children use distinct entry_N fixture artifacts, not production filename-specific logic. Parent timeout injection advances the transport clock; parent success is never supplied as a mocked successful result.

| Controlled case | Actual outcome | Parent passes | ROOT | Independently inspected state |
|---|---|---:|---|---|
| Normal parent from three committed children | done | 1 | true | Three exact artifacts, parent native/Falsifier/impact, read-only aggregate commit |
| Expired parent response followed by valid retry | done | 1 | true | Late response discarded; fresh response completes without child rewrites |
| Permanent parent deadline failures | failed | 0 | false | All three committed artifacts/receipts preserved; no parent Falsifier/commit |
| Parent cancellation before admission | failed | 0 | false | No proposal dispatched or retry; children preserved |

Retained run IDs: success **20261028T013526-13f8ef11**, retry **20261028T013528-8bf72845**, and the remaining cases in their inspection records. These are controlled identifiers, not live-model execution proof.

Independent inspection compares exact expected/actual hex and hashes, all three child receipt-commit events, actual role/tool events, parent impact PASS with changed_paths=[], parent terminal PASS and the transaction event. The parent transaction namespace is **aggregate-ROOT**, while its task/gate namespace is ROOT. The first private inspector incorrectly expected ROOT for transaction_commit and assumed one trace file despite fixture setup creating an extra initialization trace. The inspector was corrected to use the recorded run ID and actual production transaction namespace; raw evidence and production code were unchanged. This inspection correction does not waive a commit requirement.

The first focused development run had 12 tests with one error because its direct-ask test omitted RUN initialization. Fixture setup was corrected; the final 12 pass with production behavior unchanged by that fixture fix. These development records remain private and preserved.

### R5. Broader regression and compatibility

Command from repository root:

```powershell
.\.venv\Scripts\python.exe -B -X utf8 scripts/verify_level2_offline.py --output-dir audit_runs/20261021-workspace-audit/r-update-004/parent-deadline-20261028/offline-final
```

Actual driver exit: **1**, because disclosed baseline debt remains. Per-suite results: new parent/deadline 12 PASS; previous hardening 34 PASS; child inference 8 PASS; Level 1 10 PASS; generalized Level 2 20 PASS; R4 verification integration 12 PASS; literal clarification 9 PASS; project-12 clarification 9 PASS; consistency flow 18 PASS; host preflight 20 PASS; completed context 11 PASS; context recovery 4 PASS; scheduler 9 PASS; greenfield impact lifecycle 17 PASS; pre-mutation impact 27 PASS; context sufficiency 9 PASS; verification applicability 15 PASS; authority 23 PASS; experiment regressions 122 PASS; adaptive architecture 90 PASS; project understanding 32 PASS; model policy 4 PASS; requirement clarification 49 PASS. Counts overlap and are not summed. The known live-provider test remains excluded; the driver forbids live provider calls.

Verification-policy: eight tests, **two errors**. V26: 186 tests, **24 failure records, two errors, three skips**. Failure/error IDs match the previous cohort exactly. No assertion was removed to hide this debt. All frozen final-source pins match; controlled results and the genuine attempt use the same production source. The historical HTML PASS and earlier controlled browser evidence remain intact with their original hashes, not relabeled fresh live HTML verification.

### R6. Single approved genuine attempt: blocked by host preflight

After the controlled checks and regression review, direct chat authorization was obtained for exactly one fresh genuine inventory replay up to 50 minutes. Read-only health confirmed gemma4:e4b installed and no loaded model; no older Python replay was running. A sandbox socket denial during that read-only check was resolved through explicit escalation; it was not a model attempt. The approved launch used a new private **parent-deadline-20261028/live-inventory-final** directory, normal preflight and the frozen source. No further live replay was run.

**Actual result:** HOST_PREFLIGHT_FAILED / **CRITICAL_MEMORY_HEADROOM**, resource_monitoring, after one of three canary calls. Available RAM fell from 5,186,383,872 bytes before the canary to **263,299,072 bytes (about 251 MiB)** after it. These sampled values establish insufficient headroom, not which unrelated process caused memory use. No unrelated application was closed, no model/storage setting changed and the gate was not bypassed.

The new supervisor recorded normal process exit **2**, reaped=true, reason=completed, approximately **22.755 seconds** supervised time; driver total **22.757 seconds**, outer_timeout=false. Here completed describes the process wait, not successful application execution. The driver returned exit **1** and passed=false. There is **no application run ID** because startup failed before task execution. Every application metric, including root_verified and parent_integrations_passed, is null; do not manufacture zeros, a task-failure run ID or ROOT=false from those nulls. The startup marker, launch/source hashes, supervision events, console and final result are retained, byte-hashed and backed up.

This attempt proves the harness records a preflight failure and reaps the child; it exercises no new Parent Builder inference. It provides **no final-source genuine recursive ROOT verification**. Earlier genuine three-child success remains Q6 evidence on its earlier source. Controlled current-source parent completion is independent evidence with an explicitly scripted model boundary.

### R7. Readiness, preserved evidence and next action

**R_UPDATE_004 and Level 2 remain INCOMPLETE; publication is blocked.** The remaining acceptance requirement is a fresh approved genuine final-source inventory execution through parent native verification, Falsifier, impact, read-only commit and status=done/root_verified=true/parent_integrations_passed=1. The new attempt stopped before application execution because of insufficient memory. Host standby is now established for the old run; its exact network suboperation and external final termination remain unrecoverable from the old trace. New telemetry addresses those observability gaps. Tests establish cancellation and post-resume rejection under controlled conditions, not an ability to run while the OS is suspended.

All prior source/evidence snapshots, failed attempts and backups remain preserved. Source modifications are limited to the seven listed paths; report additions are chronological. Current review and the new [parent deadline evidence phase](../evidence/level2-verification-repair-integration/parent-deadline-20261028/README.md) distinguish research/OS facts, trace findings, scripted controlled results, regressions and the preflight-blocked genuine attempt. Privacy-reviewed derivatives omit raw runtime databases, full provider logs, user paths, host inventory and live authorization objects. No staged-blob validation is claimed while the index is empty.

No stage, commit, push, branch creation, PR modification or merge occurred. The existing branch remains wip/r-update-003-level2-checkpoint at 6f0047ca27e979db10e338357f0fa6a22fe0bf93. The conditionally authorized new branch wip/r-update-004-level2-hardening remains uncreated. R_UPDATE_003 and PR #8 are unchanged. No Level 3 work was started.

Before a further genuine test, restore adequate memory headroom and keep the host awake. A new assistant live attempt requires fresh authorization; the consumed approval is not reused automatically. The manual [reproduction instructions](../evidence/level2-verification-repair-integration/parent-deadline-20261028/REPRODUCE.md) use fresh outputs and preserve gates. Publication remains conditional on actual full acceptance and a fresh full diff/privacy/staged-integrity review; no completed-PR claim is prepared.

Final local review: all **68 frozen source/test/harness pins** match the tested source. The current phase manifest validates 25 selected files plus its own separate manifest, with report canonical-LF hash reconciliation. The explicit candidate review covers 153 existing intended files; the future staged publication manifest is intentionally absent. Scoped privacy/credential checks found no actual private-path findings; unchanged synthetic classifier fixture paths and the prior immutable review describing them were inspected as exceptions. Current-phase links/whitespace and git diff --check pass. All protected historical evidence, ten original prior-run files, six original new-attempt files and R_UPDATE_003 remain unchanged; both current backups pass CRC checks. The index remains empty. These are local-candidate checks, not staged-Git-blob validation or publication.

## S. Final Completion Mission: Requalification and Single Startup Attempt — 28 October 2026

This phase follows the user's final completion mission after they freed resources and adjusted power settings. It continues the saved source without restarting engineering, research or historical experiments. No production, test or harness code changed. All 68 source/test/harness hashes match the section R cohort, including 34 hardening, eight child-inference and 12 parent/deadline passes. Their results were inspected rather than rerun. Verification-policy two fixture errors and V26 24 failure records/two errors/three skips remain disclosed; overall offline exit remains 1 and overlapping counts are not summed.

### S1. Host and source readiness

The branch remained wip/r-update-003-level2-checkpoint at 6f0047ca27e979db10e338357f0fa6a22fe0bf93 with an empty index and expected origin/myfork remotes. No Python/Mini Hivo replay was running. Ollama was reachable, gemma4:e4b installed and no model loaded. The previous 22.757-second attempt had a completed/reaped preflight-failure result, not unfinished task execution.

Lightweight memory samples showed approximately 6.8–7.0 GiB available of 15.7 GiB total. This exceeded the existing 512 MiB floor before loading, but did not guarantee qualification under model load. Normal three-canary Host Preflight remained required. No threshold, model, hardware policy, output/tool budget or security gate changed.

The machine was on AC power. Read-only powercfg showed Sleep after 7,200 seconds on AC and 3,600 on battery, with AC hibernation disabled. Input idle time was about 94 seconds, so the configured AC interval exceeded the upcoming 3,000-second bound. Power events showed a prior Modern Standby interval at 01:49:17.399–01:50:00.468+03:00, before this attempt. Screen timeout was not substituted for sleep configuration. The user was informed that manual sleep remained possible and to keep the PC awake. No system-wide power policy was changed.

Current mini.py raw SHA-256 remains **c372c9197e1c3d2f923b0e63623f176d71d799add844c8a7be0f8d309022a4d6**; transport **0017b2760c49a3868e556d328cd1b19a2258c300900a84e66fbf78516a8ed78c**; supervisor **a1d3b7cd2a6aea5c05541a4125fa66841f88bf3b8f1bc55fcff2108038dd89aa**. A byte-preserving snapshot of 154 existing candidate/historical files preceded documentation changes. Sandbox denial of the Python launcher was resolved through approved execution outside the sandbox; it was not a model attempt or code change.

### S2. Exactly one authorized attempt

The attached mission authorized one new bounded original-inventory attempt conditional on readiness. The existing harness was launched once, with unchanged tested source, no concurrent inference, normal preflight and a fresh directory:

```powershell
.\.venv\Scripts\python.exe -B -X utf8 scripts/replay_post_repair.py --case inventory --outer-seconds 3000 --output-dir audit_runs/20261021-workspace-audit/r-update-004/completion-20261028/live-inventory
```

**Result: HOST_PREFLIGHT_FAILED / CRITICAL_MEMORY_HEADROOM**, at resource_monitoring after one of three canary calls. The inventory task did not start. There is no application run ID, child/parent execution, task artifact, receipt or task transaction. All application metrics are null, including status, root_verified, model/tool calls, retries and parent_integrations_passed. Null does not mean zero inference across startup: one genuine preflight canary completed. No ROOT boolean or failure run ID is fabricated.

Preflight ID: **baf2d1be8c354fdba59057cce423b42a**. Preflight began at **02:03:03.626+03:00** and ended at **02:03:21.438+03:00** on 28 October 2026; raw timestamps use UTC on 27 October. Duration: **17.812 seconds**. Before the canary, available RAM was **7,365,431,296 bytes** (about 6.86 GiB). After it: **446,787,584 bytes**, approximately **426.1 MiB**, below the unchanged **536,870,912-byte / 512 MiB** floor.

CLI exit was **2**, reaped=true, supervisor reason completed. Completed describes the process wait, not task success. Driver exit was **1**, passed=false, outer_timeout=false. Supervisor elapsed time was **19.4667 seconds** and driver wall time **19.4686 seconds**. Launch/source hashes, supervision events, final result, console and preflight marker are preserved. No extra preflight or replay was launched after failure. Task-level provider timeout/retry results remain unavailable because application execution never began.

### S3. Resource finding and independent acceptance inspection

After startup the relevant llama-server process had about **6.39 GiB resident working set** and **7.69 GiB private committed memory**. These overlapping measures are not summed. They identify substantial model-runner use during qualification, not the cause of every byte of machine memory pressure. No unrelated user application, healthy system process or provider service was terminated; no files, caches or model data were deleted.

Independent inspection reconciled launch/current source pins, read the actual failed marker and process result, confirmed null application metrics and absence of task artifacts/run traces, and preserved all six original attempt files with SHA-256 and a ZIP backup. The three inventory digests remain expected fixture oracles; **no actual inventory artifact hashes exist for this attempt**. Historical genuine three-child completion and HTML PASS retain their original source/provenance. Current-source controlled parent success remains section R evidence.

**Acceptance NOT ESTABLISHED. R_UPDATE_004 and Level 2 remain INCOMPLETE.** The blocker is insufficient post-load physical-memory headroom, not a new demonstrated Parent Integration failure. No additional production correction was indicated. Case B of the mission requires preserving this result and stopping without another costly retry or publication as complete.

Safe next action: restore adequate headroom under model load by saving work and manually closing additional nonessential memory-heavy applications, inspecting memory pressure, or allowing the idle model to unload before a newly authorized attempt. Passing the pre-load floor alone is insufficient. Do not lower the threshold, bypass preflight, change model/hardware policy or automatically retry. No new acceptance threshold is proposed.

### S4. Documentation, evidence and Git decision

The [completion packet](../evidence/level2-verification-repair-integration/completion-20261028/README.md) contains independent inspection, selected readiness/power observations, source pins, provenance and preservation checks. CURRENT_REVIEW points to this boundary; previous packets remain immutable. Raw inventories, full runtime markers and local process identifiers stay private. Selected diagnostic derivatives are reviewed separately. No staged-Git-blob validation is claimed with an empty index.

No branch creation, staging, commit, push, PR modification or merge occurred. The requested wip/r-update-004-level2-hardening branch remains uncreated. R_UPDATE_003 and PR #8 remain unchanged; no Level 3 or R_UPDATE_005. Publication remains conditional on future authorized current-source genuine children/parent/Falsifier/impact/transaction/ROOT acceptance and final staged review. The latest requested future commit message is `R_UPDATE_004: complete Level 2 recursive execution and verification hardening`.

The [manual reproduction guide](../evidence/level2-verification-repair-integration/parent-deadline-20261028/REPRODUCE.md) tests the local candidate, since no published R_UPDATE_004 branch exists. Use fresh outputs and sequential inference, retain normal preflight, and independently inspect bytes and final gates.

## T. Post-Restart Host Qualification — 28 October 2026

The user restarted Windows after closing unnecessary applications and disabling selected startup/background applications. They authorized exactly one Host Preflight qualification and required separate approval for a genuine 50-minute Recursive replay only if qualification succeeded. No full replay was authorized or launched in this phase.

### T1. Saved state and readiness

The repository remained on wip/r-update-003-level2-checkpoint at 6f0047ca27e979db10e338357f0fa6a22fe0bf93, with an empty index and the expected origin/myfork remotes. No old Python/Mini Hivo replay was found. All 68 source/test/harness hashes still match section R, including the separately recorded 34 hardening, eight child-inference and 12 parent/deadline passes. No engineering investigation or successful test was repeated; no production, harness or test source changed.

The first lightweight sample showed 7,391,703,040 bytes available of 16,849,293,312 total physical RAM, approximately 6.88 GiB available. The machine was on AC with automatic sleep after 7,200 seconds on AC and 3,600 on battery. Power policy was read, not changed. The user was reminded to keep the machine awake if a later replay is approved.

Ollama was initially unavailable after restart (connection refused); no service or loaded model was running. The already-installed local Ollama service was started hidden, with logs retained privately. The service was then reachable and /api/ps showed no loaded model before qualification. No model, driver, hardware policy, security feature or startup configuration was changed.

### T2. One actual model-load qualification: FAIL

The existing hivo.host_preflight.run_host_preflight function was invoked once, using its unchanged defaults, selected gemma4:e4b and a fresh private qualification-workspace under host-requalification-20261028. Its three-canary limit, normal resource sampling and 512 MiB minimum remained intact. No task request was supplied.

Preflight ID: **3901756e30e44780a25415de33dcdd38**. Start: **02:31:32.358+03:00**, finish: **02:31:50.829+03:00** on 28 October 2026. Raw reports use UTC on 27 October. Duration: **18.471 seconds**. Result: **FAIL / CRITICAL_MEMORY_HEADROOM**, stage resource_monitoring, after **one of three canary calls**.

| Resource sample | Available physical RAM |
|---|---:|
| Immediately before canary | 6,594,793,472 bytes, approximately 6.14 GiB |
| After canary 1 | **157,323,264 bytes, approximately 150.0 MiB** |
| Existing minimum | **536,870,912 bytes / 512 MiB** |

The difference between the earlier lightweight snapshot and the before-canary sample is real variation in machine memory; it is not attributed to one process without evidence. Qualification stopped at the first failed resource sample. No repeated preflight, new model, Recursive replay or task execution followed. There is no application run ID, child or Parent Integration result, artifact, receipt, task transaction or ROOT metric. Null/unavailable task data must not be reported as a new Parent Integration failure or a zero-call task success. Only one genuine startup canary was completed.

### T3. Resource observations and safe next action

Post-qualification observations showed a loaded gemma4:e4b runner with approximately 4.50 GiB resident working set and 7.69 GiB private committed memory. These are different, overlapping measures and are not summed; residency can change under memory pressure. The observed total leaves insufficient headroom for normal preflight. This is not evidence of a new Mini Hivo controller defect.

A private per-application snapshot identifies remaining memory consumers for the user; it is omitted from public-candidate evidence as unnecessary machine inventory. No unrelated process or healthy system service was killed. The installed Ollama CLI help confirms that an idle model can be stopped with `ollama stop gemma4:e4b`; that cleanup command was documented for the user, not executed here. No files/caches were removed and no threshold was lowered.

Safest next steps are to release the idle model if memory remains critically low, save work and manually close unused application windows, then qualify again only after resources are available. If the desktop chat application itself occupies substantial RAM, the user can save this checkpoint and perform manual qualification/testing from standalone PowerShell after closing it. Summed application working sets are not guaranteed recoverable RAM, and passing initial free-memory checks does not promise post-load qualification. Do not disable Windows memory compression or terminate system processes. No exact new free-RAM target or model/hardware change is prescribed.

### T4. Preservation and decision

The [post-restart qualification packet](../evidence/level2-verification-repair-integration/host-requalification-20261028/README.md) contains selected results, source pins, original/derivative hashes and integrity checks. Raw reports, process inventory and service logs remain private. Existing report sections and historical packets are preserved, R_UPDATE_003 and PR #8 remain unchanged, and CURRENT_REVIEW points to this newest boundary.

**Host not qualified; R_UPDATE_004 and Level 2 remain INCOMPLETE.** No approval for a full replay is requested while preflight fails. No branch creation, staging, commit, push, PR creation/modification or merge occurred. Publication remains conditional on an approved final-source genuine full children/parent/Falsifier/impact/transaction/ROOT PASS and final review. No Level 3 or R_UPDATE_005 was started.


## U. R_UPDATE_004 WIP Engineering Handoff and Publication Review — 28 October 2026

### U1. Scope, baseline and status

The user explicitly authorized publishing this **incomplete WIP checkpoint**, superseding the former genuine-ROOT prerequisite for publication. Full genuine final-source Recursive acceptance remains pending. No new Ollama test, code repair, model change, budget adjustment or broad research campaign accompanies this documentation/publication phase.

The reviewed delta is the complete current R_UPDATE_004 work relative to **6f0047ca27e979db10e338357f0fa6a22fe0bf93**. It includes tracked and previously untracked implementation, tests, harnesses and selected evidence. It is not a consolidation of earlier numbered updates. R_UPDATE_001/002/003 remain unchanged. PR #8 is still open, draft and unmerged, with that same head revision. The new branch therefore intentionally depends on its checkpoint; it is not represented as an independent upstream-main-only diff. No merge, rebase or cherry-pick is needed or authorized. The old branch/PR is not advanced.

### U2. R_UPDATE_004 improvement matrix

| Problem | Previous behavior | Implemented correction | New observed behavior | Evidence | Remaining limitation |
|---|---|---|---|---|---|
| Empty-workspace creation misclassified | Preservation words/literal data could imply existing-project work | Classify using inventory plus source creation obligations; mask literal payload from intent | Retained failing creation requests classify NEW_PROJECT; missing-existing-resource negatives remain protected | Sections 3/P; project-understanding and hardening tests | Bounded grammar; no universal intent accuracy claim |
| Compatible requirements treated as contradictory | Token/polarity overlap mixed different objects and literal values | Typed target/property/value/condition witness, artifact-aware ledger retention, workspace-bound explicit decisions | Compatible constraints proceed; genuine incompatible source choices still require answers | False Requirement Conflicts phase; 18 consistency-flow tests | Not a complete semantic satisfiability solver; unresolved semantics retain later gates |
| Child scope depended on optional model hints | A legacy child could inherit all root targets or fail with empty hints | Match child literal paths and values to immutable root source; narrow mission to owned authority | Three distinct children legally create their own exact artifact; sibling mutation remains refused | Section P; genuine 20261027T223818-f8bbcf6e; hardening tests | Deep nesting and durable restart of receipts are not independently established |
| Accepted literal verification scope lost across roles | Text readback could fall through executable routing after globals cleared | Task-matching accepted verification contract survives Falsifier/Repairer handoff; native proof rechecks current bytes | Controlled and genuine children verify their exact artifacts | Sections 4–6; R4 integration and child-inference tests | Native literal verifier existed before R4; this update repairs its use/evidence lifetime |
| Correct safety refusal triggered unnecessary repair | An unrelated refused probe could be treated as wrong artifact bytes | Discharge only nonexecuted out-of-scope read refusals with complete fresh local evidence; preserve real failures | Controlled recovery reaches ROOT without duplicate writes or unrelated repair | Post-repair C/F; hardening refusal/wrong-byte/stale-proof cases | No blanket suppression of Falsifier failures |
| Repair identity/scope drift | Narrative parent summary could replace the root anchor; helper artifacts proposed | Stable source anchor and task-bound inspection/edit scope, enforced at projection and dispatch | Controlled focused edit/reverification succeeds; real anchor changes and helper writes remain refused | Sections 6 and post-repair F; repair tests | Scripted repair proposals do not establish arbitrary live-model repair reliability |
| Parent repeated creation or lacked trusted child evidence | Already-created targets were evaluated as new writes; unbound completion prose could not establish coverage | Receipt registered after actual gate/impact/commit; complete current coverage selects newly validated read-only parent contract | Controlled parent independently verifies all outputs and commits without mutation | Sections 7/R; success and retry controlled records | Genuine final-source Parent/ROOT PASS still absent; in-process receipt registry is not a signed/resumable certificate service |
| Cold inference and blocked I/O obscured progress/cancellation | Fixed response wait cut off observed prefill; controller checks could wait behind blocking I/O | Role-scoped bounded streaming, complete-response admission, separate first-output/idle/total checks and supervised I/O | Controlled cold/partial/cancel/cleanup cases pass; genuine earlier-source children complete | Sections Q/R; eight child-inference and 12 parent/deadline tests | No speedup percentage; native I/O may outlive cancellation, in which case concurrent retry is refused |
| Browser/tool environment handling | Installed Windows browser could be missed; installer commands could reach execution; optional favicon error poisoned verification | Installed-channel fallback, narrow favicon classification, installer/package-acquisition refusal and no-install verification invocation | Genuine historical HTML browser/Falsifier/impact/commit PASS; relevant negatives pass | Post-repair G–P; genuine HTML acceptance | HTML PASS belongs to its recorded source, not every later transport revision |
| Windows timeout exceeded intended elapsed bound | One native process wait excluded low-power time; original run lacked supervisor provenance | Short elapsed-deadline polling, late-result rejection, direct-child termination/reaping and durable events | Controlled resume/cancel/process tests pass; genuine startup failures retain explicit terminal result | Section R; 12 parent/deadline tests | No controller can run while its OS is suspended; no general process-tree cleanup guarantee |

### U3. Exact production-change map and technical basis

The full [engineering audit](../evidence/level2-verification-repair-integration/wip-publication-20261028/engineering-audit.json) inventories changed files and actual changed top-level mini.py symbols against the baseline. These are source observations, not inferred feature claims. The detailed Problem → Evidence → Root Cause → Research → Design → Code → Verification → Limitations narratives remain in the cited sections; this index avoids duplicating them.

- **Requirement and intent layer:** hivo/project_understanding.py::inventory_repository/classify_project_mode, hivo/literal_source.py::policies/parse_literal_input/policy_text, hivo/requirements.py::_can_merge/deterministic_requirement_candidates/build_source_requirement_ledger/extract_source_requirements/named_artifact_declarations/_conflict_evidence/detect_explicit_conflicts; new hivo/requirement_consistency.py::facts/contradiction and hivo/requirement_decisions.py::RequirementDecisions. mini.py::extract_source_requirement_ledger/get_goal_contract/_get_goal_contract_body/select_clarification_option/resolve_clarification_questions/_source_ledger_for_contract connects those decisions to the actual CLI. Original source and explicitly superseded execution input remain distinct. See sections 3 and the False Requirement Conflicts phase.
- **Authority and child execution:** mini.py::_source_goal_anchor/_source_literal_child_paths/_prepare_task_impact_contract/_literal_worker_mission_projection, _context_anchor_for_worker, execute_leaf and execute_integration_leaf bind actual source values, local tasks and accepted authority. _impact_gate_mutation_guard/_impact_tool_projection/run_tool enforce the contract independently of model suggestions. Invalid paths, mismatched values, stale anchors and invalid whole artifact sets do not receive partial authority. See section P and source-bound negatives.
- **Verification, Falsifier and Repairer:** mini.py::run_file/_literal_artifact_verification_paths/falsify_task/_falsify_task_body/repair_task/_repair_task_body/tools_for_role/run_tool, plus hivo/verification_routing.py's accepted-literal route. These repair evidence propagation and local read/edit permissions; they do not introduce the original native tool, impact framework or context gate. _safe_literal_policy_refusals/_current_verification_failures separate narrowly proven policy refusals from actual failed output. Missing coverage is filled through real guarded native calls, not fabricated responses.
- **Receipt and parent composition:** mini.py::_record_verified_literal_receipt/_commit_verified_leaf/_current_literal_child_coverage/_literal_parent_snapshot/aggregate_task/_impact_post_mutation_check. The order is actual write → native/Falsifier gate → impact → commit → registered receipt → current coverage → new read-only parent contract → independent parent proof/Falsifier → impact → aggregate-ROOT commit. Existing parent metric helpers report these real boundaries; they are not newly invented counters or proof by metric alone.
- **Inference and supervision:** new hivo/inference_transport.py::stream_chat/_RequestIO/InferenceFailure, mini.py::ask_ollama and new hivo/process_supervision.py::supervise_process. Builder/Falsifier use first-output 240 seconds, generation idle 120, total 360; Specifier retains its recorded 120/120/360 policy; other roles retain their existing behavior. These evidence-based role changes are not a claim that no timeout policy changed during all of R4. Stream accumulation waits for complete admitted output. An unresolved worker cleanup prevents a simultaneous retry. The replay driver records existing parent/final metrics and durable launch/supervisor evidence; its outer maximum remains 3,000 seconds.
- **HTML and entrypoints:** mini.py::browser_launch_kwargs/launch_verification_browser/ensure_browser/_classify_browser_console_errors/browser_snapshot/optional_browser_check and _validated_command_parts. Only unrequested loopback favicon 404s are optional; other browser errors remain evidence. Named nonliteral output declarations define physical impact targets, not semantic content. Existing field_scoped classification is wired into normal parse_args/main and run_baseline_request/run_recursive_request defaults; the underlying pre-existing classification framework is not attributed as new R4 architecture. hivo/host_preflight.py::format_host_preflight_report adds a qualification-limit explanation; its 512 MiB threshold is unchanged.

Research adaptations are scoped, with full original references and access limits in Appendix C and the later research phases. **Do As I Can, Not As I Say** (Brian Ichter et al., CoRL 2023) informed source/environment grounding, not robot-value-function import. **Proof-Carrying Code** (George C. Necula and Peter Lee, 1996 technical report) informed evidence binding/consumer checking, not formal proof claims. **The Protection of Information in Computer Systems** (Jerome H. Saltzer and Michael D. Schroeder, 1975) informed least privilege/complete mediation. **Agentless** (Chunqiu Steven Xia, Yinlin Deng, Soren Dunn and Lingming Zhang, 2024 preprint v2) informed localization and independent validation, not framework adoption. **Sagas** (Hector Garcia-Molina and Kenneth Salem, 1987; abstract/metadata access only) informed the distinction between committed steps and later coordination; no saga engine was introduced. **Finding Contradictions in Text** (Marie-Catherine de Marneffe, Anna N. Rafferty and Christopher D. Manning, 2008) and the **SNLI corpus paper** (Samuel R. Bowman, Gabor Angeli, Christopher Potts and Christopher D. Manning, 2015) informed aligned incompatibility/neutrality; neither an unrestricted NLI classifier nor a solver is an authorization source. The previously recorded ReAct/Reflexion, Sarathi-Serve and **The Tail at Scale** comparisons motivate current feedback, prefill/decode distinction and latency measurement while rejecting additional costly reflection, GPU scheduling or hedged parallel inference. Windows native-wait and Ollama/Playwright primary documentation informed concrete platform handling. Paper results do not prove Mini Hivo results.

### U4. Actual verification ledger and limits

| Evidence class | Exact established result | Source/provenance boundary |
|---|---|---|
| REAL MODEL EXECUTION — HTML | 20261027T214528-8dfdcb28: done/root_verified=true, real browser/Falsifier/impact/commit; 1,507-byte HTML, 651.2 seconds | mini.py 4ff3c7eb18cbc5c0a565e3c2fb16665428f1e722a99d809b6c4096551970d5e8; historical source only |
| REAL MODEL EXECUTION — Recursive partial | 20261027T223818-f8bbcf6e: exact products 41/supplier 46/shipment 43 bytes, three distinct child receipt-commit events; parent started; no final ROOT outcome | mini.py 128d021f8687497dfff16ac9c284093d69f69aa59232b4f447975c86751b1e7a; incomplete historical run, no synthetic final metrics |
| CONTROLLED FUNCTIONAL — final source | 20261028T013526-13f8ef11 normal parent and 20261028T013528-8bf72845 recovered parent: done/root=true, parent_integrations_passed=1, verified_nodes=4; negative timeout/cancel preserve three children and refuse ROOT | Scripted DAG/proposals and parent NDJSON; real production gates, files, Falsifier/impact/commit, independently inspected |
| REGRESSION — final source | test_post_repair_hardening.py 34 PASS; test_child_inference_recovery.py 8 PASS; test_parent_deadline_recovery.py 12 PASS; additional suite results in the registry | Separate suite counts, not added; unchanged source pins inspected in this phase, no new execution claimed |
| HOST QUALIFICATION | Recorded 251 MiB, 426.1 MiB and latest 150.0 MiB post-load samples failed the unchanged 512 MiB minimum; last preflight 3901756e30e44780a25415de33dcdd38 stopped after 1/3 canaries | No application run ID/child/parent/ROOT metrics; resource qualification blocks, not demonstrated parent-code failures |
| OUTSTANDING TEST DEBT | Verification-policy: two fixture errors. V26: 24 failure records, two errors, three skips. Offline driver exit 1 | IDs unchanged from the retained baseline; no fully green repository claim |
| NOT YET VERIFIED | Genuine final-source full Recursive Parent/Falsifier/impact/transaction/ROOT acceptance | Must be established in a future appropriately provisioned, approved isolated run |

The current tested raw mini.py digest is **c372c9197e1c3d2f923b0e63623f176d71d799add844c8a7be0f8d309022a4d6**; the 68-file frozen record is in the parent-deadline packet. Git may canonicalize source CRLF to LF; the publication manifest separately records actual staged-blob and tested working-tree SHA-256, with Python AST equality and text-normalization checks. They must not be called byte-identical when different.

Legacy packet fields such as matches_current_production_source=true describe their original checkpoint. They do not claim the later c372 source is identical to the HTML source. Likewise old publication=BLOCKED and local-only statements retain their dated meaning. CURRENT_REVIEW, this section and the final publication manifest define the present WIP scope. Raw logs, databases, service state and authorization objects are preserved privately; sanitized receipts remain evidence, not reusable grants.

### Team Handoff — How to Continue and What to Expect

**Implemented and verified starting point.** Use the mechanisms in U2–U3 and the retained controller-functional evidence. Child 3 is no longer the observed blocker. Start at full genuine **Parent Integration and ROOT acceptance**, including its current contracts/evidence, not a new speculative child rewrite. Current controlled success proves controller behavior with scripted model boundaries; it cannot guarantee gemma4:e4b completion or performance. Receipt registry persistence across process restarts, arbitrary semantic tasks, broader model reliability and unrelated baseline fixtures remain outside demonstrated scope.

**Reproducible environment.** Use the existing virtual environment, recorded gemma4:e4b/Ollama Windows setup and source pins; record any version/model-digest difference on another machine. Ensure adequate available memory after model loading, keep the host awake and run one inference workload at a time. The unchanged 512 MiB check is a floor, not a guarantee of sustained capacity. Do not weaken it or change GPU/model policy to force acceptance. No live run is authorized by this document alone; follow the team's approval process.

**Focused offline regressions.** From the repository root, these discover only the named offline suites. Tests use real filesystem gates with scripted model responses and local short-lived child processes. In a restricted automation sandbox, place TEMP/TMP under a fresh ignored audit directory as the existing offline driver does.

```powershell
.\.venv\Scripts\python.exe -B -X utf8 -m unittest discover -s tests -p test_post_repair_hardening.py -v
.\.venv\Scripts\python.exe -B -X utf8 -m unittest discover -s tests -p test_child_inference_recovery.py -v
.\.venv\Scripts\python.exe -B -X utf8 -m unittest discover -s tests -p test_parent_deadline_recovery.py -v
```

Expect the separate 34/8/12 counts on this unchanged tested source. Do not sum them with overlapping controlled cohorts. For the recorded broader compatibility boundary, inspect parent-deadline-20261028/regression-results.json; if rerunning is justified by source/environment changes:

```powershell
.\.venv\Scripts\python.exe -B -X utf8 scripts/verify_level2_offline.py --output-dir audit_runs/manual-r4-offline-NEW
```

Expect overall exit 1 until disclosed fixture/recovery debt is resolved. The driver excludes the known provider-invoking requirement test and forbids live provider calls. Do not replace it with unrestricted broad discovery.

**Controlled Parent Integration.** The 12 parent/deadline tests above cover success, retry, permanent timeout and cancellation. A retained, independently inspectable controller replay across artifact counts/dependencies can be generated with:

```powershell
.\.venv\Scripts\python.exe -B -X utf8 scripts/update004_controlled_replay.py --output-dir audit_runs/manual-r4-controlled-NEW
```

This uses a fixture DAG/scripted providers with production scheduler, child execution, native/Falsifier, parent impact and transactions. Inspect per-case inspection.json and actual copied artifacts; script PASS is not genuine-model evidence.

**Host qualification only.** This creates a fresh directory and runs the existing bounded three-canary check; it does not start a task. Ensure local Ollama is already available.

```powershell
.\.venv\Scripts\python.exe -B -X utf8 -c "from pathlib import Path; from hivo.host_preflight import run_host_preflight,format_host_preflight_report; p=Path('audit_runs/manual-r4-host-NEW'); p.mkdir(parents=True); r=run_host_preflight(p,'gemma4:e4b','http://127.0.0.1:11434'); print(format_host_preflight_report(r)); raise SystemExit(0 if r['passed'] else 1)"
```

On failed memory/resource qualification, preserve the marker and stop; do not repeatedly retry. The marker is evidence, not a transferable authorization. The full CLI still performs its own normal startup checks in a fresh workspace.

**Future genuine inventory acceptance.** After host qualification and the appropriate run approval, use the original stored request, fresh output and 3,000-second supervisor:

```powershell
.\.venv\Scripts\python.exe -B -X utf8 scripts/replay_post_repair.py --case inventory --outer-seconds 3000 --output-dir audit_runs/manual-r4-inventory-NEW
```

Expected artifact oracles are products.txt 41 bytes/SHA-256 66d0f5c32b72d2edc9af209125f18346c828767b84af10304009cb8e6177516b, supplier.txt 46/290e00c2af96732a9b48573cf9de857c75f11327855b62ee8223916abc3b27e4 and shipment.txt 43/80e258c1a18bda44c6bdb66b1aef8ef3c2c006a9aa1f2c7911527111fa74c48e. All require UTF-8, LF and no final newline. Independently compare actual bytes, not normalized text:

```powershell
.\.venv\Scripts\python.exe -B -X utf8 -c "from pathlib import Path; import hashlib; w=Path('audit_runs/manual-r4-inventory-NEW/workspace'); e={'products.txt':b'Product: Keyboard\nQuantity: 12\nPrice: 250','supplier.txt':b'Supplier: Nile Tech\nCity: Cairo\nStatus: Active','shipment.txt':b'Shipment: SH-2026\nItems: 12\nStatus: Pending'}; a={n:(w/n).read_bytes() for n in e}; print({n:(len(v),hashlib.sha256(v).hexdigest(),v==e[n]) for n,v in a.items()}); assert all(a[n]==e[n] for n in e)"
```

Byte equality alone is insufficient. Require all three current child receipts accepted; native/Falsifier evidence for each child; scope-isolated impact and commits; no missing/stale/forged evidence; zero unresolved parent conflicts; read-only complete-set parent proof and Falsifier; parent impact PASS and **aggregate-ROOT transaction commit**; actual final metrics status=done, root_verified=true, parent_integrations_passed=1. These are pending acceptance criteria, not a prediction of success.

**Inspect a failure at its first boundary.** Keep launch.json, supervision.jsonl, result.json, console.log and workspace/.agent_host_preflight.json. After task startup inspect workspace/.agent_runs/<actual-run-id>.jsonl, .agent_experiment.jsonl and .hivo/memory.sqlite3 using a copy for database inspection. Match run IDs and source hashes. Look for inference_wait/provider_request_failed phase and cleanup fields, source_literal_child_scope_resolved, context_sufficiency_decision, impact_contract_authorized/compared, literal_child_receipt_committed, transaction_commit and parent_integration_started/finished. A parent task uses ROOT while its transaction uses aggregate-ROOT. A pending/running persisted row after interruption is not proof of an active process or a finalized failure. Missing metrics stay unavailable. Never promote completion prose, exit 0 or three files to ROOT PASS.

**Preserved baseline/HTML commands, if independently needed.** Avoid concurrent inference and do not rerun the costly historical HTML case without reason. Use a new workspace and enter the exact Level 1 request after the first command:

```powershell
.\.venv\Scripts\python.exe -B -X utf8 mini.py --no-bootstrap --workspace audit_runs/manual-r4-level1-NEW
# Request: Create a text file named test_level_1.txt containing exactly:Hello Mini Hivo
# Require 15 exact bytes plus native/Falsifier/impact/commit and final ROOT PASS; exit CLI before another run.
.\.venv\Scripts\python.exe -B -X utf8 scripts/replay_post_repair.py --case html --outer-seconds 900 --output-dir audit_runs/manual-r4-html-NEW
```

### U5. Publication boundaries and next developer decision

Publish only the reviewed complete R4 delta and curated evidence, with explicit file-by-file inclusion/exclusion audit, unchanged previous reports/raw originals, canonical artifact hashes checked against **actual staged Git blobs**, credential/private-path review and git diff --cached --check. Synthetic path classifier fixtures are documented exceptions, not actual user paths. Previously published raw history is not erased by this checkpoint; no history rewrite is performed.

The requested normal commit message is **R_UPDATE_004 (WIP): recursive verification, recovery and parent integration hardening**, on the new fork branch only. No PR, merge, release or main push is part of this handoff. The new branch inherits the unmerged PR #8 baseline without changing it. **Documentation is ready for WIP review; final-source genuine Recursive Parent/ROOT validation and complete Level 2 reliability remain unproven.** Continue from the recorded parent acceptance boundary in an appropriately provisioned environment, preserve failed attempts, and obtain a fresh run approval before another costly replay.

### U6. Staged review: faithful diagnostic-log whitespace

The actual staged whitespace gate found one trailing-space progress line (line 192) in each of child3-inference-recovery-20261027/test_v26_all.log and post-repair-live-20261027/regression-v26.log. Both record the existing V26 authority-change subtest failures; they are captured unittest output, not source formatting defects. The gate stopped publication until this was understood. Neither log nor its original/derivative digest was changed.

The narrowly scoped .gitattributes additions apply whitespace=-blank-at-eol only to those two exact evidence paths. Source-code whitespace rules and all authorization/security/verification behavior are unchanged. Their captured bytes, the sole affected line in each and immutable hashes are independently checked in the [exception record](../evidence/level2-verification-repair-integration/wip-publication-20261028/whitespace-exceptions.json). [Git's attributes documentation](https://git-scm.com/docs/gitattributes#_checking_whitespace_errors) supports per-path whitespace control. This is an explicit log-fidelity exception, not an undisclosed all-files check override. All other staged diagnostics must pass normally.
