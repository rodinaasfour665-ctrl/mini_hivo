# Child-3 inference recovery — R_UPDATE_004 current phase

This phase continues the [prior live evaluation](../post-repair-live-20261027/README.md) and [R_UPDATE_004 section Q](../../../updates/R_UPDATE_004.md). Earlier packets remain immutable historical checkpoints.

The complete original 35-minute trace establishes that Child 3 started, received one-target authority, completed context sufficiency and was interrupted during a model retry before mutation. [Timeline and eight timeout correlations](previous-recursive-timeline.json) separate observed cold prefill from unproven decode, scheduler transitions from provider waits, and committed children from absent ROOT verification. Server endpoint timestamps have one-second precision.

The new transport applies bounded streaming only to Builder/Falsifier: 240 seconds for first output, 120 seconds generation inactivity, 360 seconds configured total. Specifier and other-role policies, output/retry/tool budgets and all execution gates retain their documented behavior. Empty heartbeat chunks cannot extend deadlines; partial/cancelled/incomplete calls are not dispatched.

Evidence:

- [Before/after regressions](regression-results.json): exact counts, failure/error IDs, exclusions and source pins. The prior 34 hardening cases and eight new cases pass separately. Verification-policy/V26 debt remains; overall exit 1 and overlapping counts are explicit.
- [Controlled Child 3](controlled-child3.json): real production leaf/Worker/transport parser, gates, exact 43-byte artifact and committed receipt; scripted NDJSON and virtual 180-second first output. Siblings are seeded and preserved. No live model or parent integration is claimed.
- [Controlled HTML](controlled-html.json): actual browser/Falsifier/impact/commit with scripted models, on the new source. The older genuine HTML PASS remains in its original phase with its original source hash.
- [Frozen source](frozen-source.json), [code changes](code-change-manifest.json), [research](research.json), [preservation](preservation.json) and [manifest](manifest.json) distinguish tested raw source, original evidence and canonical LF candidate derivatives.
- [Live replay](live-replay.json): exactly one directly approved original-inventory attempt, cap 3,000 seconds, run 20261027T223818-f8bbcf6e. The process stopped without final metrics. All three children are verified/committed with exact artifacts, but parent completion and ROOT remain unverified. The [independent inspection](live-independent-acceptance.json) records accepted=false and unavailable metrics; [artifact provenance](live-artifact-provenance.json) identifies selected exact copies. A recorded 1,070-second request and trace span beyond 3,000 seconds mean hard deadline enforcement is not established. See report Q6–Q7. Publication is blocked.

No raw databases, full transcripts, host inventories or backups belong in publication. Receipt excerpts are evidence, not reusable runtime grants. No publication is inferred from this candidate packet. No Level 3 work is included.
