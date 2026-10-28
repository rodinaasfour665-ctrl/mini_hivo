# Independent Windows retest

Run from the authoritative checkout, one case at a time. Use a fresh output directory; existing output directories are rejected. Retain preflight, actual artifacts and source hashes. These are bounded experiments, not a promise of completion. Do not bypass preflight or install dependencies from Builder commands.

```powershell
.\.venv\Scripts\python.exe -B -X utf8 mini.py --no-bootstrap
```

Select a fresh workspace and paste one complete original request below. Alternatively use the exact stored fixture through the bounded driver.

## Offline regression checkpoint

```powershell
.\.venv\Scripts\python.exe -B -X utf8 scripts/verify_level2_offline.py --output-dir audit_runs/manual-offline-NEW
```

The driver forbids provider calls and excludes the known provider-invoking requirement test. The current cohort has 34 focused hardening passes. Its overall exit remains 1 because verification-policy retains two missing-fixture errors and V26 retains 24 failure records, two errors and three skips. Compare exact IDs in test-registry.json; do not reinterpret the nonzero overall exit as an all-pass result or add overlapping counts.

## Original employee request

```text
Create exactly one UTF-8 text file named employee.txt in the workspace.

The exact content must be:
Name: Sara
Department: Engineering
Status: Active

The file must contain exactly three lines in the specified order.

Use LF line separators and no trailing newline at the end of the file.

Do not create any additional task files.

Verify that the file exists and that its content exactly matches the requested text before reporting completion.
```

```powershell
.\.venv\Scripts\python.exe -B -X utf8 scripts/replay_post_repair.py --case employee --output-dir audit_runs/manual-employee-NEW
```

## Original inventory request

```text
Create a small inventory record using exactly three UTF-8 text files.

File 1: products.txt
The exact content must be:
Product: Keyboard
Quantity: 12
Price: 250

File 2: supplier.txt
The exact content must be:
Supplier: Nile Tech
City: Cairo
Status: Active

File 3: shipment.txt
The exact content must be:
Shipment: SH-2026
Items: 12
Status: Pending

Each file must contain exactly three lines, in the specified order.

Use LF line separators and no trailing newline at the end of any file.

Do not create any other files.

Verify that all three files exist and independently confirm their exact contents before reporting the task as complete.
```

```powershell
.\.venv\Scripts\python.exe -B -X utf8 scripts/replay_post_repair.py --case inventory --outer-seconds 2100 --output-dir audit_runs/manual-inventory-NEW
```

## Original html request

```text
Create a simple standalone HTML page named index.html for an employee profile.

The page must include:
- A valid HTML5 document structure.
- The page title "Employee Profile".
- An H1 heading containing "Sara".
- A paragraph containing "Engineering Department".
- A visible status label containing "Active".
- Internal CSS to give the page a clean professional layout.

Use UTF-8 encoding.

Keep all CSS inside the HTML file. Do not create any external CSS or JavaScript files.

Create exactly one HTML file and no additional task files.

Verify that the required text and HTML elements are present before reporting completion.
```

```powershell
.\.venv\Scripts\python.exe -B -X utf8 scripts/replay_post_repair.py --case html --outer-seconds 900 --output-dir audit_runs/manual-html-NEW
```

## Controlled transport failure with a genuine model

```powershell
.\.venv\Scripts\python.exe -B -X utf8 scripts/replay_provider_recovery.py --output-dir audit_runs/manual-provider-recovery-NEW
```

This deliberately fails the first Builder inference before HTTP dispatch, then calls real Ollama through the existing retry. It is mixed controlled-fault/genuine-model evidence. It does not demonstrate a spontaneous provider outage or Repairer recovery. No model reply or tool result is fabricated.

## Independent oracle

For employee/inventory, compare complete bytes to the exact source values, UTF-8 without BOM, LF separators, no terminal newline. Expected byte lengths: employee 49; products 41; supplier 46; shipment 43. For HTML, inspect the real UTF-8 file, doctype/head/body, title, H1, department paragraph, visible status, internal style and absence of external stylesheet/scripts/extra task files. HTML has no source LF constraint. Require real browser/Falsifier evidence, authorized paths, successful impact comparison and transaction commit plus done/root_verified=true. A browser screenshot or CLI exit alone is insufficient.

Normal verification classification now uses field_scoped semantics. The explicit `--verification-classification-policy current` option retains legacy full-JSON classification for historical comparison and can reproduce metadata pollution; do not present that as the recommended normal run.


## Run limits and independent byte inspection

Inventory uses a 35-minute external wall limit; HTML uses 15 minutes. These are replay-process limits, not enlarged production tool/model budgets. Run sequentially on the CPU-constrained provider. A timeout, preflight refusal or null final metrics is not PASS. Keep the whole fresh output directory after each run.

The latest approved inventory replay did **not** complete within 35 minutes: two exact verified children committed, shipment.txt was absent and Parent Integration was not reached. This command reproduces a bounded experiment, not a ready-to-publish success guarantee. Review the timing evidence and controlled regressions before spending more live inference time.

For a completed inventory replay, independently inspect its actual retained files (replace only the fresh directory name):

~~~powershell
@'
from pathlib import Path
import hashlib, json
out = Path("audit_runs/manual-inventory-NEW")
workspace = out / "workspace"
expected = {
    "products.txt": b"Product: Keyboard\nQuantity: 12\nPrice: 250",
    "supplier.txt": b"Supplier: Nile Tech\nCity: Cairo\nStatus: Active",
    "shipment.txt": b"Shipment: SH-2026\nItems: 12\nStatus: Pending",
}
for name, oracle in expected.items():
    actual = (workspace / name).read_bytes()
    print(name, len(actual), hashlib.sha256(actual).hexdigest(), actual == oracle)
    assert actual == oracle, name
assert {p.relative_to(workspace).as_posix() for p in workspace.rglob("*")
        if p.is_file() and not any(part.startswith(".") for part in p.relative_to(workspace).parts)} == set(expected)
result = json.loads((out / "result.json").read_text(encoding="utf-8"))
assert not result["outer_timeout"]
assert result["metrics"]["status"] == "done"
assert result["metrics"]["root_verified"] is True
print("Bytes and recorded final outcome match; inspect native/Falsifier/impact/transaction trace evidence separately.")
'@ | .\.venv\Scripts\python.exe -B -X utf8 -
~~~

Expected recursive milestones are three owned-path impact authorizations, exact native readback, independent child Falsifier outcomes and committed child receipts; then read-only Parent Integration, parent Falsifier, impact comparison with no unexpected mutation, transaction completion and ROOT VERIFIED. Do not accept correct files alone when these gates fail. Do not edit/copy a sanitized receipt back into runtime state.

For the one-file baseline, use the same independent method with employee.txt and the exact source bytes (49 bytes). For HTML, additionally open the real page and inspect its DOM/visible state; source text search alone does not prove visibility. The controlled transport-fault command is optional manual testing with genuine model costs; it does not authorize the assistant to launch another live attempt.
