# Independent Windows verification

Use the authoritative checkout, existing virtual environment and local gemma4:e4b. Run one live case at a time. Every output directory below is fresh and under the already ignored private audit root. Replace NEW with a unique suffix; existing directories are rejected. Normal preflight stays enabled.

```powershell
.\.venv\Scripts\python.exe -B -X utf8 scripts/verify_level2_offline.py --output-dir audit_runs/20261021-workspace-audit/r-update-004/manual-offline-NEW
```

Provider calls are forbidden by this offline driver. The historical verification-policy/V26 debt gives overall exit 1; inspect exact per-suite counts and IDs. The current hardening 34 and child-inference eight tests must pass.

```powershell
.\.venv\Scripts\python.exe -B -X utf8 scripts/replay_post_repair.py --case employee --outer-seconds 900 --output-dir audit_runs/20261021-workspace-audit/r-update-004/manual-employee-NEW
.\.venv\Scripts\python.exe -B -X utf8 scripts/replay_post_repair.py --case inventory --outer-seconds 3000 --output-dir audit_runs/20261021-workspace-audit/r-update-004/manual-inventory-NEW
.\.venv\Scripts\python.exe -B -X utf8 scripts/replay_post_repair.py --case html --outer-seconds 900 --output-dir audit_runs/20261021-workspace-audit/r-update-004/manual-html-NEW
```

These execute the unchanged original requests in tests/fixtures/post_repair_requests.json, not simplified prompts. They are manual commands, not authorization for another assistant live run. No GPU/browser package installation or preflight bypass is needed.

For employee, require exact UTF-8 LF/no-final-newline source bytes (49), native verification, Falsifier, impact and commit. For inventory, require products 41, supplier 46 and shipment 43 exact bytes and hashes, three independently verified committed child receipts, read-only Parent Integration, parent Falsifier, impact/transactions and status=done/root_verified=true/parent_integrations_passed=1. Correct partial files or completion prose do not establish success.

The inventory hashes are products 66d0f5c32b72d2edc9af209125f18346c828767b84af10304009cb8e6177516b; supplier 290e00c2af96732a9b48573cf9de857c75f11327855b62ee8223916abc3b27e4; shipment 80e258c1a18bda44c6bdb66b1aef8ef3c2c006a9aa1f2c7911527111fa74c48e. Independently read complete file bytes, not normalized text.

For HTML, inspect actual UTF-8 HTML5 structure, title Employee Profile, H1 Sara, Engineering Department paragraph, visible Active status, internal CSS, no external stylesheet/script and no additional task files. Require real native/browser and Falsifier results plus impact and commit. HTML has no exact LF/no-final-newline obligation.

Current replay is incomplete: all three children committed, parent/ROOT unverified. Configured request and outer limits were overrun in the retained trace; their enforcement needs diagnosis. Keep the host awake, retain process-lifecycle evidence, and do not assume the driver guarantees a hard wall-clock cutoff. A timeout or missing finalized metrics is not PASS. Preserve the whole private output directory and inspect role request times, first-output/idle/total limits, provider completion timing, actual tool effects and final gate evidence.

For the single-file baseline, run the actual CLI in a fresh workspace and enter the exact Level 1 request:

```powershell
.\.venv\Scripts\python.exe -B -X utf8 mini.py --no-bootstrap --workspace audit_runs/20261021-workspace-audit/r-update-004/manual-level1-NEW
```

Request: `Create a text file named test_level_1.txt containing exactly:Hello Mini Hivo`. Require exactly 15 bytes (`Hello Mini Hivo`), native readback, Falsifier, impact/commit and finalized ROOT PASS. This command is a manual reproduction, not a claim that a new Level 1 live replay was executed in this phase.
