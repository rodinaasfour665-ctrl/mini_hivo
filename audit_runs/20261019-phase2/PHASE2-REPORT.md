# HIVO Mini Phase 2 execution evidence

Date: 19 October 2026, Africa/Cairo. This directory contains fresh session evidence. Archived reports are historical and were not regenerated.

## Tests

| Invocation | Test process exit | Observed result |
|---|---:|---|
| Model policy | 0 | 4 tests, OK |
| Authority, initial sandboxed attempt | 1 | 23 errors caused by temporary-directory permission denial |
| Authority, approved unrestricted rerun | 0 | 23 tests, OK |
| Context sufficiency | 0 | 9 tests, OK |
| Experiment-focused tests | 0 | 122 tests, OK |
| Full discovery, first attempt | Interrupted | Stalled in an unexpected live-model test; no completed-suite result claimed |
| Regression with that live-model test excluded | 1 | 1,361 tests run; 24 failure records, 18 errors, 10 skips |

Focused counts overlap the regression suite and must not be added as unique coverage. Failure records include subtests; do not derive a passing-test count by simple subtraction. Discovery found 1,703 cases. One was explicitly excluded; class setup errors prevented additional cases from running. Static source counts in Phase 1 were not discovery counts.

Exact focused commands and outcomes: `execution-summary.json` and `test-executions.json`. Full failure details: `regression-excluding-live-test.log`; indexed failures: `regression-failure-index.json`.

### Regression selection

The completed regression used `unittest.defaultTestLoader.discover('tests')`, recursively flattened the discovered suite, excluded only:

`test_requirement_clarification.RequirementClarificationTests.test_root_brain_prompt_compacts_large_source_side_channel_without_dropping_ids`

and ran the selected cases with `unittest.TextTestRunner(verbosity=2)`. No production or test source was patched. The excluded test calls `get_goal_contract()` with a sufficiently long input to invoke actual requirement-extraction model calls. It cannot be described as an offline deterministic check in its current form.

### Failure investigation

- Fourteen class-setup errors require absent historical databases, plans, or live-run artifacts. Examples include the hardcoded `D:\projects\Ai\mini_hivo\output\hivo-v22-stage5c-fresh-receipts-live-1\.hivo\memory.sqlite3` and missing repository-local `output/hivo-v24-4-5-stage6b-planning-live-1`.
- Two verification-policy errors require the absent `output/gemma-only-rescue-recursive-v9-hard-prompt.txt`.
- Recovery tests depend on absent `output/hivo-v25-6-stage6c-b-verification-closure-live-3`. Their loaders yield incomplete evidence, followed by invalid-envelope assertions and downstream continuation failures. This establishes fixture dependence, not a production repair requirement. Two downstream tests also encounter `NoneType` errors.
- Browser tests skip because Chromium is absent; other skip reasons are retained verbatim in the log. Skips are not passes.
- The broad suite is not green on this checkout. No failing assertion was edited, suppressed, or reclassified as a pass.

## Runtime qualification

### Browser: blocked

`browser-runtime.json` records an actual Playwright driver and launch attempt, process exit 1. The driver identified missing Chromium/headless-shell executables for revision 1248. No browser was downloaded and no browser-dependent experiment was started.

### Host preflight: isolated run passed

The first preflight completed one canary, then the second timed out; `host-preflight-result.json` preserves this failure. Available RAM fell to about 0.9 GiB. This run overlapped the unexpected regression model call and is confounded; neither memory nor hardware is proven to be the cause.

The follow-up ran with no regression process active. `host-preflight-isolated-result.json` records PASS, all 3/3 native canaries completed, duration 26.945 seconds. Available RAM before the check was about 8.2 GiB. GPU telemetry remains unavailable. No timeouts, model options, packages, or environment settings were changed.

Diagnostic observation: the timeout text `timed out` was labelled `CANARY_PROVIDER_FAILURE`. In `hivo/host_preflight.py`, the exception classifier checks the substring `timeout`; that does not match `timed out`. This is a reporting discrepancy, not proof of an inference fault. No fix was applied.

## Experiment 12 preparation

Executed:

```powershell
.\.venv\Scripts\python.exe -B -X utf8 scripts/experiment12_run.py preregister --output-dir audit_runs/20261019-phase2/experiment12-suite
```

Exit 0. Created five fixture seeds and authorities and a manifest for 30 planned trials. Preregistration is not trial execution or experimental success. `production-integrity.json` records matching hashes for all nine production files pinned by that manifest at the time checked.

Chromium is missing, so the live pilot was selected from the bundled Node family instead of the browser family. Only the disposable audit fixture is authorized for mutation; its tests remain protected by the harness contract.

Pilot command:

```powershell
.\.venv\Scripts\python.exe -B -X utf8 scripts/experiment12_run.py trial --output-dir audit_runs/20261019-phase2/experiment12-suite --case-id node_unique --policy current --repeat 1
```

### Fresh pilot outcome: failed

`pilot-audit.json` cross-checks the metrics, result JSON, process exit, and source/test bytes.

| Field | Observed value |
|---|---|
| Run ID | `20261019T054959-87298d45` |
| Process exit | 0 |
| Saved experiment status | `failed` |
| Measured execution time | 120.22 seconds; excludes native preflight |
| Model calls | 1 |
| Worker / tool calls | 0 / 0 |
| Root verified | false |
| Source and protected tests unchanged from seed | true / true |

The event trace shows one MissionCompiler request with approximately 1,409 estimated input tokens and a 4,096-token context. It timed out at the configured 120-second transport boundary. No Worker or behavioral verification ran. The first-blocker artifact labels the stage `CHILD_VERIFICATION / ENVIRONMENT_ERROR`, while the trace places the actual failure earlier in Mission Compiler. Root `INTEGRATION_NOT_READY` is a downstream consequence.

Process exit 0 means the harness completed recording a failed result; it is not experiment success. The timeout's underlying cause is unresolved. Canary success does not prove that a larger structured Mission Compiler request will complete on this host. No timeout or model option was changed.

Historical Experiment 12 reports current Node Root success in 3/3 attempts; this new cohort has one failed Node pilot before Worker. The tasks belong to the same bundled family, but source/runtime conditions have not been demonstrated identical to the historical cohort. Do not pool these attempts, substitute this pilot for the original 30-trial benchmark, or infer general reliability.

The full batch was not started after this failed pilot. Browser-dependent trials remain blocked by missing Chromium. Existing historical suite/Git prerequisites remain unresolved for exact later-experiment reproduction.

### Normal CLI startup

The normal default-mode CLI was invoked separately with `--no-bootstrap`, a new existing disposable workspace, and `exit` on standard input. No implementation task was submitted. This measures startup/preflight and clean exit only; it cannot establish request-to-result validation.

```powershell
'exit' | .\.venv\Scripts\python.exe -u -B -X utf8 mini.py --no-bootstrap --workspace audit_runs/20261019-phase2/normal-cli-workspace
```

The final native outcome is retained in `normal-cli-startup.log`, `normal-cli-startup-exit.txt`, and the workspace preflight marker.

Observed result: native host preflight PASS (3/3 canaries), pinned model selected, input prompt reached, clean exit with process code 0. Available RAM before this check was about 1.3 GiB. This is verified startup, not verified implementation or default-mode task dispatch.

## Actions needed before continuing affected work

1. Browser execution requires explicit approval to download Playwright Chromium with `.\.venv\Scripts\python.exe -m playwright install chromium`. This installs browser binaries; it does not fix the model timeout or supply historical evidence.
2. Restore authentic missing historical artifacts/databases where available. Any proposal to replace historical dependencies with portable deterministic test fixtures needs separate code-review approval; preserve the original failed logs and scope of claims.
3. The long-input test should receive deterministic injected model responses if it is intended as an offline regression test. Proposed scope is only that test's provider boundary, retaining its requirement-ID/compaction assertions. No change has been applied.
4. Investigate Mission Compiler latency/provider behavior before another full batch. A longer timeout, model option change, or application fix is not authorized by these measurements alone. Preserve the failed pilot as an attempted execution.

No full request-to-result run, completed experimental batch, or Phase 3 success is claimed. The isolated canary and normal startup passes do not cancel the failed pilot or the broad regression failures.

## Scope and approval boundary

No production/test fixes, package installation, model/configuration changes, or historical report replacements were approved or performed. Do not fabricate absent historical fixtures to make tests pass. Restore authentic matching artifacts where available, or separately review portable deterministic fixture work.

Phase 3 full validation remains pending. Browser installation, any test or production fix, and promotion of an experimental policy require explicit approval before action.
