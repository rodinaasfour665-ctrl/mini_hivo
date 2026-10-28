# Post-restart Host Preflight — qualification failed

This packet continues [R_UPDATE_004 section T](../../../updates/R_UPDATE_004.md). The unchanged source matches all 68 tested pins; previously passing suites were inspected rather than repeated. No production, harness or test changes were made.

After restart, no old Mini Hivo replay was running. Ollama's installed service was initially stopped and was started locally before qualification. The PC was on AC with a two-hour automatic sleep interval. Normal preflight was run exactly once with gemma4:e4b and unchanged thresholds.

**FAIL: CRITICAL_MEMORY_HEADROOM**, after one of three canaries. Available RAM fell from **6,594,793,472 bytes (6.14 GiB)** immediately before the canary to **157,323,264 bytes (150.0 MiB)**, below the existing **512 MiB** minimum. Duration: 18.471 seconds. No Recursive task, application run ID, children, Parent Integration or ROOT verification was started.

- [Qualification](qualification.json): selected measured results and nullable task state.
- [Frozen source](frozen-source.json): unchanged tested code and separate saved test cohorts.
- [Preservation](preservation.json), [provenance](provenance.json) and [manifest](manifest.json): byte integrity and original-versus-derivative hashes. Canonical text is UTF-8 LF; no staged-Git-blob validation is claimed.

The private process-memory snapshot and full service/runtime reports are excluded from publication candidates. No user application or healthy system process was terminated. Release idle model memory and manually close unneeded applications before another qualification; do not weaken the threshold or automatically retry. See report section T for the safe manual options.

**R_UPDATE_004/Level 2 INCOMPLETE; publication blocked.** No replay approval was requested after failed qualification. All project changes remain local and unstaged. No new branch, commit, push, PR change, merge, R_UPDATE_005 or Level 3.
