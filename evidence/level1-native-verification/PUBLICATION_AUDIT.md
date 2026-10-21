# Complete Level 1 publication inclusion/exclusion audit

Audit date: 22 October 2026 (Africa/Cairo). Previous update head: `cca388daa3537030abdb7b6cf175d847f23b99ec`. New work is isolated on `codex/level1-native-verification`.

## Dependency and diff boundary

Team PR #5 is open and unmerged at preflight. It provides the initial literal lifecycle/native route and remains unchanged. The Level 1 update delta is measured against its final head `cca388d`, not attributed to upstream main. The new PR description records the explicitly selected destination/base. No merge, rebase, reset, cherry-pick or history rewrite is used.

## Initial complete working-tree inventory

The initial index was empty. There were three modified tracked files and 29 untracked files. All 25 relevant initial paths are included in full; the 7 raw generated-workspace paths below are preserved locally and excluded. Additional fresh checks, a curated successful output, scoped Git configuration and this audit/PR body were added during publication preparation.

| Initial path | Status | Decision | Reason |
|---|---|---|---|
| `hivo/requirements.py` | modified | Include entire file | Entire colon-delimited multiword literal recognition change. |
| `hivo/verification_routing.py` | modified | Include entire file | Entire refusal/native-proof versus executable-test classification fix. |
| `mini.py` | modified | Include entire file | Entire native guidance and bounded refused-verification implementation delta. |
| `AGENTS.md` | untracked | Include entire file | Permanent complete investigation/verification/documentation/publication workflow. |
| `evidence/level1-native-verification/README.md` | untracked | Include entire file | Evidence interpretation, progression and reproduction guidance. |
| `evidence/level1-native-verification/controlled-replay.log` | untracked | Include entire file | Sanitized retained suite/functional log; outcomes unchanged. |
| `evidence/level1-native-verification/controlled-replay/result.json` | untracked | Include entire file | Preserved controlled functional success with source pins and final aggregation. |
| `evidence/level1-native-verification/live-completed-result.json` | untracked | Include entire file | Independent successful real Ollama record, byte proof, Falsifier read and final gates. |
| `evidence/level1-native-verification/live-result.json` | untracked | Include entire file | Preserved earlier partial/interrupted real run; not counted as success. |
| `evidence/level1-native-verification/manifest.json` | untracked | Include entire file | Original versus sanitized derivative hashes and transformations. |
| `evidence/level1-native-verification/original-run-summary.json` | untracked | Include entire file | Preserved first failed/rolled-back Level 1 trace/tool summary. |
| `evidence/level1-native-verification/test-results.json` | untracked | Include entire file | Commands and exact previous suite outcomes, distinct from fresh checks. |
| `evidence/level1-native-verification/test_adaptive_architecture.log` | untracked | Include entire file | Sanitized retained suite/functional log; outcomes unchanged. |
| `evidence/level1-native-verification/test_authorityall.log` | untracked | Include entire file | Sanitized retained suite/functional log; outcomes unchanged. |
| `evidence/level1-native-verification/test_context_sufficiency_gate.log` | untracked | Include entire file | Sanitized retained suite/functional log; outcomes unchanged. |
| `evidence/level1-native-verification/test_experimentall.log` | untracked | Include entire file | Sanitized retained suite/functional log; outcomes unchanged. |
| `evidence/level1-native-verification/test_greenfield_impact_lifecycle.log` | untracked | Include entire file | Sanitized retained suite/functional log; outcomes unchanged. |
| `evidence/level1-native-verification/test_level1_native_verification-final.log` | untracked | Include entire file | Sanitized retained suite/functional log; outcomes unchanged. |
| `evidence/level1-native-verification/test_pre_mutation_impact.log` | untracked | Include entire file | Sanitized retained suite/functional log; outcomes unchanged. |
| `evidence/level1-native-verification/test_verification_applicability.log` | untracked | Include entire file | Sanitized retained suite/functional log; outcomes unchanged. |
| `evidence/level1-native-verification/test_verification_policy.log` | untracked | Include entire file | Actual failed suite: six OK outcomes, two authentic missing-fixture errors. |
| `list/project-6/.agent_host_preflight.json` | untracked | Exclude; retain locally | Raw generated workspace artifact; selected safe evidence is published separately. |
| `list/project-7/.agent_host_preflight.json` | untracked | Exclude; retain locally | Raw generated workspace artifact; selected safe evidence is published separately. |
| `list/project-8/.agent_experiment.jsonl` | untracked | Exclude; retain locally | Raw generated workspace artifact; selected safe evidence is published separately. |
| `list/project-8/.agent_host_preflight.json` | untracked | Exclude; retain locally | Raw generated workspace artifact; selected safe evidence is published separately. |
| `list/project-9/.agent_experiment.jsonl` | untracked | Exclude; retain locally | Raw generated workspace artifact; selected safe evidence is published separately. |
| `list/project-9/.agent_host_preflight.json` | untracked | Exclude; retain locally | Raw generated workspace artifact; selected safe evidence is published separately. |
| `list/project-9/test_level_1.txt` | untracked | Exclude; retain locally | Raw generated workspace artifact; selected safe evidence is published separately. |
| `scripts/level1_native_verification_replay.py` | untracked | Include entire file | Complete provider-free persistent functional replay harness. |
| `tests/test_level1_native_verification.py` | untracked | Include entire file | Complete ten-test regression suite, including actual final-gate assertions. |
| `updates/R_UPDATE_002.md` | untracked | Include entire file | Complete Level 1 update report, delta from PR #5 and controlled/live limits. |
| `updates/UPDATE_TEMPLATE.md` | untracked | Include entire file | Reusable unnumbered A–M report template. |

## Complete intended new-update file list

Every file below is included, regardless of whether it originally was tracked. Fresh-check logs are included even where the suite failed; no success-only evidence selection is used.

| Repository path | Inclusion rationale |
|---|---|
| `.gitattributes` | Scoped canonical LF policy for published evidence/workflow files. |
| `.gitignore` | Exclude only numbered raw generated workspaces 6–9, preserving them locally. |
| `AGENTS.md` | Permanent complete investigation/verification/documentation/publication workflow. |
| `evidence/level1-native-verification/PR_DESCRIPTION.md` | Professional complete-update PR title/body and dependency disclosure. |
| `evidence/level1-native-verification/PUBLICATION_AUDIT.md` | This complete file-by-file inclusion/exclusion and dependency audit. |
| `evidence/level1-native-verification/README.md` | Evidence interpretation, progression and reproduction guidance. |
| `evidence/level1-native-verification/artifacts/test_level_1.txt` | Byte-identical curated copy of the successful 15-byte real-model output. |
| `evidence/level1-native-verification/controlled-replay.log` | Sanitized retained suite/functional log; outcomes unchanged. |
| `evidence/level1-native-verification/controlled-replay/result.json` | Preserved controlled functional success with source pins and final aggregation. |
| `evidence/level1-native-verification/live-completed-result.json` | Independent successful real Ollama record, byte proof, Falsifier read and final gates. |
| `evidence/level1-native-verification/live-result.json` | Preserved earlier partial/interrupted real run; not counted as success. |
| `evidence/level1-native-verification/manifest.json` | Original versus sanitized derivative hashes and transformations. |
| `evidence/level1-native-verification/original-run-summary.json` | Preserved first failed/rolled-back Level 1 trace/tool summary. |
| `evidence/level1-native-verification/publication-checks/controlled-replay.log` | Fresh 22 October offline suite/controlled replay observation; failed policy log retained. |
| `evidence/level1-native-verification/publication-checks/controlled-result.json` | Fresh 22 October offline suite/controlled replay observation; failed policy log retained. |
| `evidence/level1-native-verification/publication-checks/results.json` | Fresh 22 October offline suite/controlled replay observation; failed policy log retained. |
| `evidence/level1-native-verification/publication-checks/test_adaptive_architecture.log` | Fresh 22 October offline suite/controlled replay observation; failed policy log retained. |
| `evidence/level1-native-verification/publication-checks/test_authorityall.log` | Fresh 22 October offline suite/controlled replay observation; failed policy log retained. |
| `evidence/level1-native-verification/publication-checks/test_context_sufficiency_gate.log` | Fresh 22 October offline suite/controlled replay observation; failed policy log retained. |
| `evidence/level1-native-verification/publication-checks/test_experimentall.log` | Fresh 22 October offline suite/controlled replay observation; failed policy log retained. |
| `evidence/level1-native-verification/publication-checks/test_greenfield_impact_lifecycle.log` | Fresh 22 October offline suite/controlled replay observation; failed policy log retained. |
| `evidence/level1-native-verification/publication-checks/test_level1_native_verification.log` | Fresh 22 October offline suite/controlled replay observation; failed policy log retained. |
| `evidence/level1-native-verification/publication-checks/test_model_policy.log` | Fresh 22 October offline suite/controlled replay observation; failed policy log retained. |
| `evidence/level1-native-verification/publication-checks/test_pre_mutation_impact.log` | Fresh 22 October offline suite/controlled replay observation; failed policy log retained. |
| `evidence/level1-native-verification/publication-checks/test_project_understanding.log` | Fresh 22 October offline suite/controlled replay observation; failed policy log retained. |
| `evidence/level1-native-verification/publication-checks/test_verification_applicability.log` | Fresh 22 October offline suite/controlled replay observation; failed policy log retained. |
| `evidence/level1-native-verification/publication-checks/test_verification_policy.log` | Fresh 22 October offline suite/controlled replay observation; failed policy log retained. |
| `evidence/level1-native-verification/test-results.json` | Commands and exact previous suite outcomes, distinct from fresh checks. |
| `evidence/level1-native-verification/test_adaptive_architecture.log` | Sanitized retained suite/functional log; outcomes unchanged. |
| `evidence/level1-native-verification/test_authorityall.log` | Sanitized retained suite/functional log; outcomes unchanged. |
| `evidence/level1-native-verification/test_context_sufficiency_gate.log` | Sanitized retained suite/functional log; outcomes unchanged. |
| `evidence/level1-native-verification/test_experimentall.log` | Sanitized retained suite/functional log; outcomes unchanged. |
| `evidence/level1-native-verification/test_greenfield_impact_lifecycle.log` | Sanitized retained suite/functional log; outcomes unchanged. |
| `evidence/level1-native-verification/test_level1_native_verification-final.log` | Sanitized retained suite/functional log; outcomes unchanged. |
| `evidence/level1-native-verification/test_pre_mutation_impact.log` | Sanitized retained suite/functional log; outcomes unchanged. |
| `evidence/level1-native-verification/test_verification_applicability.log` | Sanitized retained suite/functional log; outcomes unchanged. |
| `evidence/level1-native-verification/test_verification_policy.log` | Actual failed suite: six OK outcomes, two authentic missing-fixture errors. |
| `hivo/requirements.py` | Entire colon-delimited multiword literal recognition change. |
| `hivo/verification_routing.py` | Entire refusal/native-proof versus executable-test classification fix. |
| `mini.py` | Entire native guidance and bounded refused-verification implementation delta. |
| `scripts/level1_native_verification_replay.py` | Complete provider-free persistent functional replay harness. |
| `tests/test_level1_native_verification.py` | Complete ten-test regression suite, including actual final-gate assertions. |
| `updates/R_UPDATE_002.md` | Complete Level 1 update report, delta from PR #5 and controlled/live limits. |
| `updates/UPDATE_TEMPLATE.md` | Reusable unnumbered A–M report template. |

## Ignored/private material reviewed and excluded

| Category | Disposition / reason |
|---|---|
| `.venv/`, Python caches | Generated dependencies/bytecode; not source changes. Preserve/recreate locally. |
| Numbered workspaces 6–9, including `.hivo/`, `.agent_runs/`, preflight and experiment markers | Raw SQLite/sidecars, transcripts and machine inventories stay local. Original file hashes recorded privately before staging. |
| `audit_runs/20261021-workspace-audit/` | Private audits, backups, intermediate failed development logs, raw fresh test results and disposable replay outputs. Curated exports have separate provenance hashes. |
| Earlier ignored October 19 evidence and `updates/R_UPDATE_001.md` | Previous-update private historical records; immutable, unrelated to the new public delta. No restoration or rewriting. |
| Prior tracked source/tests/reports and `evidence/impact-lifecycle-publication/` | Dependency/base content retained unchanged; no deletion or new attribution. |

Raw state is not silently counted as uploaded evidence. For the original failed run the transient bytes are unavailable after rollback; the later successful file is independently inspected and copied byte-identically. Exclusions do not omit implementation, regression tests, the real-model completion record, the complete numbered report or persistent workflow instructions.

## Verification and publication gates

- Fresh source matches the previously verified Level 1 source pins; no new implementation change during packaging.
- Ten fresh offline suites pass; verification-policy has the same two missing historical prompt-fixture errors. Exact commands/outcomes are retained in `publication-checks/results.json`.
- Fresh controlled replay passes actual gates, Builder/Falsifier native readback, exact bytes, final aggregation and Root verification. No live-model rerun or Level 2 work.
- Completed real run `20261021T224333-21e91d97` is corroborated by stored trace/metrics and the exact 15-byte artifact. Real Falsifier used `read_file`; Builder supplied native proofs.
- Retain the refusal, repeated writes/readbacks and 375.51-second live runtime as inefficiencies. One pass is not a universal reliability or performance claim.
- Before commit: verify exact stage membership, originals, source/derivative hashes against staged blobs, source identity, JSON/links, privacy patterns and `git diff --cached --check`.
- Publish only to the personal fork; new PR dependency/base is explicit. Do not modify/merge #5 or start Level 2.
- Excluding raw files now does not erase previously public Git history.
