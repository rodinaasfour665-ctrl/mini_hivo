# Parent Integration deadline and supervision — local R_UPDATE_004 candidate

This phase continues [Child-3 recovery](../child3-inference-recovery-20261027/README.md) and [report section R](../../../updates/R_UPDATE_004.md). All historical evidence remains unchanged.

The [investigation](investigation.json) correlates Windows Modern Standby with the 1,070-second parent request, retained provider prefill/cancellation and the Windows process-wait semantics. It explicitly identifies the old trace's missing header/read phase and final kill attribution. The selected [provider excerpt](provider-excerpt.log) omits private model/runtime paths; [provenance](provenance.json) distinguishes source and derivative hashes.

The correction supervises blocked inference I/O with short absolute-deadline/cancellation checks, rejects late or partial results and prevents concurrent retry while cleanup is pending. The replay supervisor polls its own elapsed deadline, reaps its owned process and records launch/wait/terminal events. It cannot execute while the OS is suspended; post-resume rejection is the tested guarantee. No source/auth/context/impact/Falsifier/transaction boundary or model/tool budget is weakened.

[Controlled cases](controlled-results.json) and their individual records exercise real child and parent production code with scripted model proposals/NDJSON. Normal and recovered parent completion both reach ROOT=true/parent_integrations_passed=1. Permanent timeout and cancellation preserve all three child artifacts and cannot claim ROOT success. Independent inspections check actual bytes, tool roles, impact and the aggregate-ROOT transaction commit. These cases do not establish live-model reliability.

[Regressions](regression-comparison.json) retain exact per-suite results and baseline failure IDs. New parent/deadline 12, prior hardening 34 and prior child-inference eight pass separately. Verification-policy two errors and V26 24 failure records/two errors/three skips remain. The complete offline driver exits 1; do not add overlapping counts.

The [single genuine attempt](live-replay.json) stopped during host preflight with CRITICAL_MEMORY_HEADROOM after one of three canaries. There is no application run ID or task metrics. Normal process exit/reaping is not application success. No further live replay occurred. [Run registry](run-registry.json), [frozen source](frozen-source.json), [code changes](code-change-manifest.json), [preservation](preservation.json) and [manifest](manifest.json) record provenance and limits.

**R_UPDATE_004/Level 2 INCOMPLETE; publication blocked.** No stage, commit, push, new branch, PR modification, merge or Level 3. [Manual reproduction](REPRODUCE.md) requires fresh workspaces, adequate memory and sequential runs. No raw database, complete provider transcript, host inventory or runtime grant belongs in publication.
