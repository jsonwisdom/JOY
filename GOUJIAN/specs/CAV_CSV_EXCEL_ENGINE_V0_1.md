# CAV_CSV_EXCEL_ENGINE_V0_1

## STATUS: CSV_ENGINE_SPEC_DRAFT
## TRUTH_STATE: YELLOW
## NO_FAKE_GREEN: TRUE
## AUTHORITY: FALSE
## ANCHORED_TO: jaywisdom.eth
## ENGINE: jaywisdom.base.eth
## L1_ANCHOR_EXECUTED: FALSE

---

## 1. Ruling

CAV now means:

```text
CSV Audit Verification
```

CAV is the spreadsheet witness layer.

It is not a vague content-authenticity box.
It is not a green renderer.
It is not a receipt creator.

It is the machine that turns CSV / Microsoft Excel-style rows into auditable row claims before ALMS is allowed to archive them.

```text
MCP = captures messy event claims
CAV = checks spreadsheet rows against receipts
ALMS = archives only verified rows
Surface = displays only ALMS-backed green
```

---

## 2. Identity Binding

```text
jaywisdom.eth      = immutable Seal
jaywisdom.base.eth = mutable Engine
```

This file is anchored by identity intent only.
It does not claim that an L1 ENS text record or transaction has been executed.

Until transaction hash and read-back proof exist:

```text
L1_ANCHOR_EXECUTED = FALSE
TRUTH_STATE = YELLOW
```

---

## 3. Spreadsheet Law

```text
A row is not a receipt.
A row is a claim.
A green row requires a receipt.
```

Excel may organize claims.
CSV may export claims.
CAV may verify claims.
ALMS may archive verified claims.
The Surface may display archived claims.

No layer may skip the next layer.

---

## 4. Required CSV / Excel Fields

Every row submitted to CAV MUST resolve to these fields:

```text
claim_id
row_number
workbook_name
sheet_name
source_csv_sha256
row_sha256
actor
event_type
event_timestamp
receipt_ref
claim_state
render_green
```

If the event is on-chain, the row also requires:

```text
tx_hash
block_number
chain_id
contract_or_address
```

If the event requires human approval, the row also requires:

```text
requires_human_approval
approved_by
approved_at
approval_signature
```

---

## 5. Row Hash Rule

CAV computes the row hash from a canonical row string.

Canonical order:

```text
claim_id|row_number|sheet_name|actor|event_type|event_timestamp|receipt_ref|tx_hash|block_number|chain_id
```

Missing optional fields are represented as empty strings.
Whitespace is trimmed.
Line endings are normalized to LF.

Output:

```text
row_sha256 = sha256(canonical_row_string)
```

The row passes only if the computed row hash matches the submitted `row_sha256`.

---

## 6. Excel Formula Rule

Excel formulas are not evidence.

If a cell contains a formula, CAV must choose one policy and record it:

```text
FORMULA_POLICY_VALUES_ONLY
FORMULA_POLICY_REJECT_FORMULAS
FORMULA_POLICY_REQUIRE_SIGNED_EXPORT
```

Default policy:

```text
FORMULA_POLICY_VALUES_ONLY
```

The verified object must preserve the exported value, not silently trust the formula.

---

## 7. Witness Chain

CAV requires these witnesses for green eligibility:

| Witness | Function | Fails if |
|---|---|---|
| CSV Shape Witness | `validate_csv_required_fields()` | required spreadsheet fields missing |
| Row Hash Witness | `sha256_row_matches()` | computed row hash differs from submitted row hash |
| Receipt Link Witness | `verify_receipt_ref()` | row points to no receipt, fake tx, missing approval, or broken source |
| Human Gate | `check_human_approval()` | required approval missing, vetoed, or unsigned |

CAV may include additional witnesses, but these are the minimum for spreadsheet green.

---

## 8. Output Rule

If every required witness passes:

```text
CAV_ROW_STATE = VERIFIED
ALMS_MAY_ARCHIVE = TRUE
```

If any required witness fails:

```text
CAV_ROW_STATE = REJECTED
ALMS_MAY_ARCHIVE = FALSE
render_green = FALSE
```

---

## 9. Insufficient Events Rule

If a spreadsheet claims 50 rows but only 2 pass CAV:

```json
{
  "claimed_rows": 50,
  "verified_rows": 2,
  "rejected_rows": 48,
  "INSUFFICIENT_EVENTS": true,
  "NO_FAKE_GREEN": "ACTIVE"
}
```

ALMS writes 2 rows.
It does not invent the other 48.

---

## 10. Surface Rule

```text
Surface may display CSV draft rows.
Surface may not display CSV green rows.
Surface may display ALMS green rows only.
```

So the dashboard can show:

```text
CSV Rows Claimed: 50
Rows Verified by CAV: 2
Rows Archived by ALMS: 2
Green Rows Rendered: 2
Rejected Rows: 48
```

It may not show 50 green rows.

---

## 11. No Fake Green Rule

```text
LESS GREEN IS ALLOWED
SLOW GREEN IS ALLOWED
YELLOW IS ALLOWED
PENDING IS ALLOWED
FAKE GREEN IS FORBIDDEN
```

A Microsoft Excel sheet can become a command surface.
It cannot become an authority surface until CAV verifies each row and ALMS archives it.

---

## 12. Current Ruling

```text
GitHub custody: PREPARED
CAV meaning: CSV Audit Verification
Pipeline state: YELLOW
L1 anchor executed by this file: FALSE
Runtime validator executed by this file: FALSE
No Fake Green: ACTIVE
```
