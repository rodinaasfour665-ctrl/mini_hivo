# Windows reproduction and acceptance

From the authoritative checkout, use the existing virtual environment. Replace NEW with a unique suffix; existing output directories are rejected. Preserve every prior run. Controlled/offline checks require no Ollama inference:

```powershell
.\.venv\Scripts\python.exe -B -X utf8 scripts/verify_level2_offline.py --output-dir audit_runs/20261021-workspace-audit/r-update-004/manual-parent-offline-NEW
```

Expect the 12 new parent/deadline tests, 34 hardening and eight child-inference tests to pass separately. The driver still exits 1 for disclosed verification-policy/V26 debt. It places temporary fixtures under its output and forbids live provider calls. Inspect per-suite logs/results and source pins; do not run broad discovery assuming all tests are offline.

For independent manual live tests, first make sufficient memory available and keep the PC awake. Do not bypass preflight or change power settings globally. Run sequentially:

```powershell
.\.venv\Scripts\python.exe -B -X utf8 mini.py --no-bootstrap --workspace audit_runs/20261021-workspace-audit/r-update-004/manual-level1-NEW
```

Enter: `Create a text file named test_level_1.txt containing exactly:Hello Mini Hivo`. Require exactly 15 UTF-8 bytes, native readback, Falsifier, impact/commit and finalized ROOT PASS.

```powershell
.\.venv\Scripts\python.exe -B -X utf8 scripts/replay_post_repair.py --case inventory --outer-seconds 3000 --output-dir audit_runs/20261021-workspace-audit/r-update-004/manual-parent-inventory-NEW
.\.venv\Scripts\python.exe -B -X utf8 scripts/replay_post_repair.py --case html --outer-seconds 900 --output-dir audit_runs/20261021-workspace-audit/r-update-004/manual-parent-html-NEW
```

The driver uses the original fixture requests. Inventory must produce products.txt (41 bytes), supplier.txt (46), shipment.txt (43), exactly LF/no final newline. Their expected SHA-256 values are respectively 66d0f5c32b72d2edc9af209125f18346c828767b84af10304009cb8e6177516b, 290e00c2af96732a9b48573cf9de857c75f11327855b62ee8223916abc3b27e4 and 80e258c1a18bda44c6bdb66b1aef8ef3c2c006a9aa1f2c7911527111fa74c48e. Require all child context/authorization/native/Falsifier/impact/commit/receipt gates, read-only parent native/Falsifier/impact/aggregate-ROOT commit, status=done, root_verified=true and parent_integrations_passed=1.

HTML must satisfy the original HTML5/title/heading/department/status/internal-CSS requirements, create no extra task files and pass actual browser, Falsifier, impact and commit gates. Prior HTML success belongs to its historical source, not this unverified live transport revision.

Inspect launch.json, supervision.jsonl, result.json, preflight marker and task trace. inference_wait events distinguish blocked headers/read phases. An expired result is rejected after host resume; nothing can enforce a deadline while the OS cannot schedule it. A normal supervised exit or missing/null metrics is not PASS. The latest approved attempt failed preflight before a task run; these commands are manual instructions, not authorization for another assistant replay.
