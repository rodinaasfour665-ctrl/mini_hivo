# R_UPDATE_004 local evidence — Level 2 INCOMPLETE

This packet accompanies [R_UPDATE_004](../../updates/R_UPDATE_004.md). All files are local, unstaged and unpublished. Base commit: `6f0047ca27e979db10e338357f0fa6a22fe0bf93`; containing commit pending.

The eight `controlled/*.json` records inspect actual retained execution artifacts and production SQLite/trace results. Provider tool proposals and child DAGs are scripted; real production source/context/impact gates, filesystem mutation, leaf execution, Falsifier, scheduler, parent integration and transactions execute. Temporary workspaces were copied before cleanup; original temporary paths differ from retained copies. These are **controlled functional/integration** results, not live-model results.

Independent counts 1, 2, 3, 4, 5, 8 and 10 and a dependent three-artifact chain passed all eleven inspector checks. Exact expected hex and actual hashes are recorded per file. Dependency source content includes predecessor name and digest; DAG discovery itself is a fixture. New regression suite: 12 tests PASS. Previous parent suite: unchanged four tests now PASS. A separate controlled fault-injection regression performs a real authorized repair followed by independent verification.

`live/live-receipt-final.json` records genuine `gemma4:e4b` run `20261025T204437-4d483ccf`: preflight PASS, three source literals, NEW_PROJECT, then Specifier timeout; zero tools and `root_verified=false`. Process exit 0 did not mean success. `live/live-final.json` is an earlier-source baseline attempt blocked by memory preflight; it is not final-source baseline proof. No final-source genuine end-to-end PASS is claimed. Selected timing events are retained separately, with private service/path details omitted.

`test-registry.json` preserves per-suite counts, full failing/error IDs, source pins and the explicit excluded live-provider test. Verification-policy has two fixture errors; V26 recovery has 24 failure records, two errors and three skips. Failure/error IDs match the starting cohort. Counts overlap and must not be summed. Raw tracebacks remain private; their absence here does not convert failures to passes.

The complete original evidence is under the ignored local directory `audit_runs/20261021-workspace-audit/r-update-004/`. It includes failed development iterations, final raw cohorts, actual copied task files/databases, original hash inventory and byte-preserving ZIP backup. No raw runtime databases, authorization objects, complete model transcripts or host inventories are copied into this packet.

## Integrity and provenance

- [manifest.json](manifest.json): original source versus sanitized derivative SHA-256 and packet file hashes.
- [preservation.json](preservation.json): nine individually checked originals still match the initial hashes and ZIP bytes. This is a scoped preservation check, not every historical file.
- [code-change-manifest.json](code-change-manifest.json): baseline and current source/test/harness hashes, with new files explicit.
- [run-registry.json](run-registry.json): exact live requests, expected byte oracles, run IDs, outcomes and source pins.
- [test-registry.json](test-registry.json): final offline results and unchanged baseline debt.
- [research-references.json](research-references.json): original references and adaptation boundaries; detailed review is in the report.

Canonical packet text is UTF-8 with LF. Manifest excludes its own digest. Hash validation uses actual local bytes. No staged Git blob validation has occurred because staging is prohibited. Future publication needs a separate explicit path/privacy/staged-byte review. These sanitized records cannot be loaded as runtime authorization, and no historical public data has been erased.

## Reproduce safely

From the checkout root in Windows PowerShell, use fresh output names:

```powershell
.\.venv\Scripts\python.exe -B -X utf8 -m unittest discover -s tests -p test_update004_verification_integration.py -v
.\.venv\Scripts\python.exe -B -X utf8 scripts/update004_controlled_replay.py --output-dir audit_runs/manual-r4-controlled-01
.\.venv\Scripts\python.exe -B -X utf8 scripts/verify_level2_offline.py --output-dir audit_runs/manual-r4-offline-01
```

The broad driver is expected to exit unsuccessfully until disclosed debt is fixed. It forbids live provider calls and excludes the known live requirement test. Inspect actual `results.json` and artifacts.

Optional manual live checks, one at a time after provider qualification:

```powershell
.\.venv\Scripts\python.exe -B -X utf8 scripts/level2_clarification_replay.py --live --cases structured-blocks --output-dir audit_runs/manual-r4-live-baseline-01
.\.venv\Scripts\python.exe -B -X utf8 scripts/level2_clarification_replay.py --live --cases inventory --output-dir audit_runs/manual-r4-live-inventory-01
```

Do not substitute a script success field for inspection of all live child/parent gates, Falsifier, impact, transaction and current exact bytes. Avoid repeated expensive timeouts without diagnostics. Report sections 14–15 describe open issues and acceptance limits. Do not start Level 3 or publish this candidate automatically.
