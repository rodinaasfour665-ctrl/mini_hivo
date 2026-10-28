# Post-repair live evaluation — local R_UPDATE_004 checkpoint

This packet follows the [false-conflict phase](../false-conflicts-20261027/README.md). It preserves the two historical genuine ROOT successes and the two historical HTML Specifier failures. It does not declare Level 2 complete.

Read the appended **Post-Repair Live Evaluation — Recursive Recovery, Ollama Inference Timeouts, HTML Generalization, and Engineering Hardening** phase in [R_UPDATE_004](../../../updates/R_UPDATE_004.md) for code paths, chronology, interpretation and Windows reproduction commands.

## Evidence boundaries

- [Historical run ledger](historical-run-ledger.json): exact selected metrics, role request metadata and trace counts from original local records. Historical traces do not self-pin source. The pre-edit source matched the user-provided checkpoint hash; that is a separate observation.
- [Original requests](original-requests.json): unchanged employee, inventory and HTML source requests copied to a reusable fixture. HTML in both historical workspaces was identical.
- [Role latency](historical-role-latency.json): matched completed-call client wall times only; failed request time is excluded. Do not interpret it as server prefill/decode decomposition.
- [Controlled functional](controlled-functional.json): real Worker/filesystem/native verification/impact/transactions and recursive scheduling, scripted model proposals. Exact artifact hex/digests remain inspectable. Internal recursive test asserts returned done/root true; its unfinalized RUN status can remain unknown.
- [Tests](test-registry.json): final offline cohort, per-suite counts, full failing/error IDs, excluded known-live test and source hashes. Counts overlap; no sum is meaningful. Driver exit 1. Verification-policy has 2 errors; V26 has 24 failure records, 2 errors and 3 skips. IDs match the preceding cohort.
- [Live attempts](live-run-registry.json): tiny availability smoke and bounded real Ollama attempts, each with pre-launch source hashes. A smoke is not a task PASS. Intermediate-source results are not relabeled final-source. A harness root-done flag requires independent artifact/gate inspection before accepting end-to-end completion.
- [Independent browser readback](independent-browser-readback.json): actual rendered title/body, heading/status, internal CSS and external-dependency negative check for the preserved 1411-byte page from the failed intermediate HTML attempt. This does not change that attempt's failed ROOT status.
- [Research](research.json): four primary scientific references, author-reported results, transfer limits, cost/safety tradeoffs and official implementation documents. Paper benchmark results are not our results.
- [Code manifest](code-change-manifest.json): phase-specific source/test/harness bytes. Earlier local edits remain preserved; hashes alone do not attribute all HEAD-relative changes to this phase.
- [Preservation](preservation.json), [provenance](provenance.json), [manifest](manifest.json): original source hashes, selected derivative hashes, original-run immutability, valid backup and historical report-prefix preservation. Current working-tree bytes, no staging or publication.

## Findings requiring careful interpretation

Historical child1 output was already correct. A refused sibling run_file was misclassified as an implementation failure. Repairer writes were rejected for caller-propagated goal-anchor drift. The model's later “System Call” strategy label did not add capability: it used guarded write_file again. ROOT's attempted write was refused by read-only integration; impact comparison recorded no parent changes. Zero optional Stage-5 counters do not negate the active literal child-receipt path.

The historical HTML failure was active inference interrupted by the configured 120-second blocking client operation. It was not proof Ollama was stopped or out of memory. CPU selection was corroborated by server policy dropping the integrated device; GPU acceleration was not enabled or benchmarked. The new Specifier streaming path has explicit total/inactivity bounds and admits no partial response.

The intermediate live replay passed specification and wrote HTML, then failed browser availability. Installed-browser discovery/fallback and installer-command rejection were repaired afterward. Chrome rendered the preserved page successfully; Edge's failed launch is retained in private diagnostics. No browser/model/driver package was installed.

## Privacy and preservation

Raw transcripts, SQLite databases, screenshots, host inventories, full server logs and detailed launch logs remain in a private ignored audit directory. Selected derivatives omit personal paths, host identity and credentials. No original evidence is edited. This packet is a **local candidate**, not a published record. Prior manifests intentionally refer to their historical report prefix; this packet pins the appended report. Removing content from a new packet would not erase any previously published history.

## Independent retest

Use the root-relative commands in the update report and `scripts/replay_post_repair.py`. Choose a fresh output directory every time, run sequentially, retain preflight and source pins, and inspect actual artifacts plus all applicable gates. Do not infer success from process exit, generated prose or a tiny health probe. No Level 3 experiment is included.

## Superseding child-binding checkpoint

The authoritative offline cohort is now `offline-source-binding-reviewed`, with 34 focused hardening passes and the same disclosed verification-policy/V26 debt. The retained controlled evidence includes the public recursive orchestration with Project Brain, MissionCompiler normalization and empty planner hints, in addition to the narrower prebuilt-child case. Each row states exactly which model/specification/decomposition boundaries are scripted.

The genuine HTML and mixed controlled-fault/genuine-model recovery successes on mini.py hash `37a118499df6dd824b0fcc7998e540e6b972c9c613992331f46c178b932f2591` remain historical. [The subsequent inventory failure](recursive-scope-regression.json) exposed dropped literal child ownership and incorrect CRLF bytes before interruption. Its exact planner hints were not recorded, and no finalized ROOT status is invented.

The repaired source binds children to root literal values, preserves the frozen root goal, projects explicit derived obligations and narrows advisory Worker missions. Its mini.py raw hash is `4ff3c7eb18cbc5c0a565e3c2fb16665428f1e722a99d809b6c4096551970d5e8`. The user approved exactly two sequential final-source genuine attempts: 35-minute inventory and 15-minute original HTML. The live registry records their actual outcomes when available; absence of a completed record is not PASS. No additional costly replay is authorized. Publication requires both complete independent acceptance checks.

The [independent final-source recursive inspection](genuine-recursive-acceptance.json) records the approved 35-minute replay's incomplete outcome. Two children passed exact bytes/native readback/Falsifier/impact and committed receipts; shipment.txt was absent and parent/ROOT gates were not reached. There were eight recorded inference timeouts and nine actual tool records. Final application metrics are null after the outer interruption. Publication is blocked; correct partial files do not satisfy complete task acceptance. The separate HTML outcome cannot discharge this missing recursive proof.

Final-source original HTML run **20261027T214528-8dfdcb28** passed independent file/DOM, native/Falsifier browser, impact and transaction checks: done/root_verified=true, 651.2 task seconds, 11 model attempts, five tools, one recovered timeout. See [current acceptance](genuine-html-acceptance.json). Both approved replays have ended; no further costly run or Git publication was performed. The missing recursive acceptance keeps R_UPDATE_004 and Level 2 incomplete.
