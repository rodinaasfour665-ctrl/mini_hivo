# Greenfield impact-contract lifecycle investigation

## Confirmed historical cause

The original `list/project-4` run `20261019T061903-f5bb5918` used source SHA-256 `b22b51b3ae71e21893385fc1f940ef834f1a83337124b004e1e0af34944ed43b`, identical to the source captured by the pre-fix deterministic reproduction.

Its Builder returned no tool calls. The context gate remained `PREPARING_CONTEXT`, with no sufficiency decision, round 0, and zero mutation permission. `_prepare_task_impact_contract()` created a candidate, but `_activate_impact_contract()` was never reached: impact validation intentionally waits for a passed context gate. Therefore zero validated/authorized contracts does **not** show a rejected contract, a validator exception, or proof that Stage 3 was incorrectly skipped.

The observed path was request understanding -> Stage 2 NEW_PROJECT bookkeeping/brains -> auto baseline selection -> shared `execute_leaf()` -> candidate creation -> gated Builder -> no tool response -> terminal result -> rollback. Baseline does not compile a separate recursive Worker Mission; its zero `worker_missions_executed` metric is not proof that the Builder tool-loop entrypoint was never entered.

The first pre-fix divergence was a model completion without a context decision. A second controller defect then obscured it: finalization replaced the context-required summary with an unaccepted-impact summary while returning generic `CONTEXT_INSUFFICIENT`. The deterministic replay in `before-reproduction.json` reproduces exactly those lifecycle counters and the misleading summary using the real runtime with only the model response scripted.

## Scope and verification gaps

Stage 3 existing-repository planning and the local pre-mutation impact contract are separate layers. Skipping Stage 3 in an empty workspace does not authorize writes and does not remove the local impact requirement.

The old baseline candidate had no concrete permitted path for this request and fell back to lexical identifiers. A generic identifier list is not a source-bound filename plan. In addition, `run_file` had no verification operation for a literal text artifact. These gaps would remain even after a successful context decision.

The change compiles an explicit single literal text-file request into one exact path and one expected UTF-8 content digest, retaining all source IDs as verification obligations. A bare name receives the `.txt` extension required by the interpreted text-file type; an explicit suffix is retained. No particular filename, content, model, or workspace is hardcoded. Unsafe paths, metadata targets, and initially existing outputs are not authorized. This bounded compiler handles the recognized literal-file request class, not every natural-language software request.

The first live diagnostic after this compilation passed the context and impact gates but retried the suffix-less source name three times. All three writes were rejected. The compiler now states the DERIVED path resolution first in the Worker packet, and a rejection lists the authorized targets. Reusing the already compiled candidate after file creation preserves its resolution and obligations instead of treating the in-progress artifact as an unrelated pre-existing file.

The existing context gate still runs first. The existing deterministic validator and acceptance function still run before any mutation. The runtime checks the exact named path, and the existing `run_file` tool can check the source-bound content digest without executing text. The post-mutation comparison independently checks the actual file digest before commit, even if a caller supplies a claimed passing verification result.

The complete controller replay exposed a further verification integration gap: Stage 5A emitted only nonapplicable syntax/browser routes and rejected real literal-file readback as `VERIFICATION_EVIDENCE_UNAVAILABLE`. It now emits a required `LITERAL_ARTIFACT` route from the accepted controller contract. The native `run_file` payload must bind the exact path, accepted contract hash, expected digest, and observed digest. Generic PASS text, another tool/target, foreign authority, or a claimed PASS with mismatching content cannot satisfy this route. Existing browser, focused-test, approved-authority and direct-oracle routes retain their matching rules.

## Requirement traceability

In the historical run, source extraction initially produced an empty ledger. The Goal Contract interpreter subsequently supplied three requirement strings. Project Brain's compatibility adapter created REQ-001..003 later, but the earlier Source Contract and Task Brain retained their empty ledgers. This is confirmed independently of the mutation failure.

The original leaf still received requirement strings in its task completion criteria. The missing IDs are a traceability defect, not evidence that the Worker lacked the filename/content facts or that the unmapped count caused the mutation stop.

The adapter now establishes the immutable IDs before Stage 2 when goal interpretation supplies the requirements. Explicit literal-file requests also have deterministic extraction of the creation, filename, and content obligations. IDs/provenance are retained through Source Contract, Task Brain, local Impact Contract, and its bounded Worker projection. Literal post-state verification enforces the concrete output independently of Specifier wording.

The historical metrics retain only the 2/3 mapping counts. The full original specification and per-ID coverage rows are not archived in this checkout; a read-only inspection of the historical events database found no saved coverage/specification payload. Consequently the exact historical unmapped ID cannot be conclusively identified from available evidence. A separate reproducible lexical mapping defect is confirmed: "file name ... X" did not match "file named X" at the conservative token threshold. Coverage now normalizes only those filename spellings; a different literal filename remains UNMAPPED. No source omission is silently marked covered, and the ledger is not copied into an omitted derived specification to inflate its metrics.

## Engineering changes

- `hivo/requirements.py`: explicit literal-file recognition/extraction and conservative filename coverage normalization.
- `mini.py`: early source-ledger reconciliation; bounded named-artifact scope compilation; one bounded retry for an unsubmitted context decision; rejected-contract stop and precise diagnostics; exact-path guard; source-bound literal verification through `run_file`.
- `hivo/pre_mutation_impact.py`: optional expected content digest; required scope and source-obligation validation; invalid hash/schema status preservation; independent post-state digest check; source IDs in the bounded Worker projection.
- `hivo/verification_routing.py`: required source-bound literal artifact route and exact native-proof matching.
- `tests/test_greenfield_impact_lifecycle.py`: positive/negative lifecycle, real file writes/readback, exact-content rejection, traceability, mapping and existing-project approval regressions.
- `tests/test_context_sufficiency_gate.py`: retains the existing denied-mutation assertions and updates the expected diagnostic for a never-submitted context decision.

## Evidence and limits

All intermediate test logs are retained. `test-results-final.json` records exact commands and exit codes for the first focused batch; `greenfield-routing-complete.log` records the final 17-test focused run. The final positive leaf test scripts only model responses. It uses the real Falsifier function, applicability routing, context/impact gates, mutation tools, deterministic verification aggregation, post-state audit and commit. It is not a live-model reliability measurement.

No packages, model settings, memory thresholds, or historical artifacts were replaced. The repository still has no Git metadata, so no commit or clean-working-tree claim is made.

## Final runtime evidence

| Run | Outcome | Boundary actually verified |
|---|---|---|
| `live-auto`, run `20261019T063924-418790a4` | Interrupted diagnostic; no output file | Context and impact authorization passed; three bare-name writes rejected. No completed Root result. |
| `live-auto-final`, run `20261019T065255-5928c8e3` | Failed; task process exit 0 | Preflight passed; Specifier timed out before Worker, zero tool calls. Process exit 0 is not task success. |
| `live-baseline` | Blocked; process exit 2 | Native preflight stopped at `CRITICAL_MEMORY_HEADROOM`: 488,017,920 available bytes (465.4 MiB), below the configured 512 MiB minimum. Zero canary/model task calls. |
| `controlled-baseline-routed`, run `20261019T070259-88ba0efc` | Provider-free replay passed | Seven scripted model responses; real Builder/Falsifier file checks, required verification route, post-state audit, commit and `root_verified=true`. |
| `controlled-final`, run `20261019T071642-a38faf6a` | Final-source provider-free replay passed | Same complete real controller path, with all four final production source hashes captured in `controlled-final-result.json`. |

The successful controlled replay created `controlled-baseline-routed/welcone.txt` containing exactly seven bytes, `welcome`, with SHA-256 `280d44ab1e9f79b5cce2dd4f58f5fe91f0fbacdac9f7447dffc318ceb79f2d02`.

Its counters are created=1, validated=1, authorized=1; retained source IDs are REQ-001, REQ-002, REQ-003; real model calls=0. See `controlled-replay-result.json` and the saved native run ledger. Two earlier replay setup attempts remain in separate directories/logs: the first exhausted scripted responses before the Falsifier; the second exposed the missing Stage 5A route and then exhausted responses at repair. Neither is counted as a success.

The final-source output is `controlled-final/welcone.txt`, with the same exact bytes and digest. `native-proof-recheck.json` records 11 passing checks against an actual retained native proof and deliberate invalid variants. `raw-source-check.json` confirms that an abbreviated model goal does not grant this typed literal scope when the original request includes other duties.

## Regression results and execution limitation

- **Passed:** 17 focused regressions in `greenfield-routing-complete.log`, including real Falsifier/applicability/aggregation/commit and false-proof rejection. The last matcher-consistency and original-request binding refinements were additionally verified by workspace-only native-proof checks, the raw-source check, and the final-source integration replay.
- **Passed earlier affected suites:** impact contracts 27, context 9, authority 23, project understanding 32, experiment-focused 122, adaptive architecture 90. Their exact commands/exit codes are in `test-results-final.json`; these counts overlap the broader suite and are not unique coverage totals.
- **Broader comparison before the final verification-route integration:** 1,376 tests run, 24 failure records, 18 errors, 10 skips. All 42 failure/error identities match the pre-change baseline (`regression-comparison.json`); no new failure identities appeared in that measured run. Class setup failures prevent some discovered cases from executing. One known live-model requirement test was explicitly excluded.
- **Blocked, not executed:** the final broader rerun and the final focused rerun after the last refinements. Automatic permission review failed because its reviewer model was at capacity, then timed out on the permitted retry. These were review-service failures, not determinations that the commands were unsafe. The temporary-directory tests were not rerun by bypassing that approval boundary.

Thus the latest code has a passing, retained full controller replay and current positive/negative proof checks, but a fully rerun final regression suite and completed live-model task remain unverified. A working permission reviewer and sufficient host RAM are needed to close those two limits.

## Implementation locations

- `mini.py`: `run_file`, `_prepare_task_impact_contract`, `_activate_impact_contract`, `_impact_gate_mutation_guard`, `get_goal_contract`, `_append_impact_contract_projection`, `execute_agent_task`, `diagnose_failure`, `execute_leaf`.
- `hivo/requirements.py`: `literal_file_request`, `deterministic_requirement_candidates`, `specification_coverage`.
- `hivo/pre_mutation_impact.py`: `_target_record`, `validate_pre_mutation_impact_contract`, `accept_pre_mutation_impact_contract`, `compare_pre_mutation_impact`, `project_impact_contract`.
- `hivo/verification_routing.py`: `analyze_verification_applicability`, `_evidence_matches`.
- Regression coverage: `tests/test_greenfield_impact_lifecycle.py`, with the context-diagnostic expectation updated in `tests/test_context_sufficiency_gate.py`.

The final live-source request was:

```text
Create a text file named welcone containing exactly welcome.
```

Live commands used the existing venv interpreter with `-u -B -X utf8 mini.py --no-bootstrap --workspace <fresh-audit-workspace> --prompt-file audit_runs/20261019-impact-fix/live-request.txt`, and additionally `--mode baseline` for the direct-baseline attempt. No timeout or environment setting was increased to force an outcome.

## Remaining limits

- Full live-model task completion is **unverified**. One model timeout and the native RAM gate prevented a completed final live trial; the first live diagnostic was explicitly interrupted.
- The deterministic scope compiler recognizes explicit single literal text-file requests. It does not claim support for every greenfield project or arbitrary prose. Unrecognized requests retain the existing architecture and safeguards.
- The exact historical unmapped requirement ID remains **unverified** because the per-ID specification coverage payload is absent. The independent filename mapping regression and full ID propagation are tested without inflating missing specification coverage.
- Historical-fixture-dependent regressions and missing browser binaries identified in Phase 2 remain unresolved; no replacement historical evidence was invented.
- A currently running PowerShell/Python process must be restarted to load the edited source.
