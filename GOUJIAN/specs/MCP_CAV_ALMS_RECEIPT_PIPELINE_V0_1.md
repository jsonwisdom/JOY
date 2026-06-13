# MCP_CAV_ALMS_RECEIPT_PIPELINE_V0_2

## STATUS: PIPELINE_SPEC_DRAFT
## TRUTH_STATE: YELLOW
## NO_FAKE_GREEN: TRUE
## AUTHORITY: FALSE
## ANCHORED_TO: jaywisdom.eth
## ENGINE: jaywisdom.base.eth
## L1_ANCHOR_EXECUTED: FALSE

---

## 1. Purpose

This document defines Jay's corrected MCP CAV ALMS Receipt Pipeline:

```text
Model Context Protocol -> CSV Audit Verification -> Automated Ledger of Minted Stories
```

Correction from V0.1:

```text
CAV no longer means Content Authenticity Verification.
CAV now means CSV Audit Verification.
```

The pipeline turns messy human moments, wallet events, screenshots, CSV rows, and Microsoft Excel-style sheet entries into receipt-aware records without faking warmth, certainty, authority, or green status.

Core law:

```text
NO_FAKE_GREEN = TRUE
```

Every green pixel needs a witness.
Every green spreadsheet row needs a receipt.

---

## 2. Identity Binding

```text
jaywisdom.eth      = immutable L1 Seal
jaywisdom.base.eth = mutable L2 Engine
```

This spec is anchored by identity intent to `jaywisdom.eth`, but it does not claim that an L1 ENS text record or transaction has been executed.

Until transaction hash and read-back proof exist:

```text
L1_ANCHOR_EXECUTED = FALSE
TRUTH_STATE = YELLOW
```

---

## 3. Stage 1: MCP — Model Context Protocol

### Role

MCP is the ingest layer.

It records what entered the system.
It does not judge truth.
It does not approve.
It does not render green.
It does not create spreadsheet authority.

```text
MCP = microphone, not judge
```

### Input examples

- Mrs. Wisdom says yes to a badge.
- A transfer appears to hit `0x694cE46C64D9D1a5e9376A9feBcF85Ec05D72e9F`.
- Goblin Art Studio mints a link.
- A user claims a third transfer exists.
- A CSV row claims a transaction, approval, badge, kindness event, or receipt.
- A Microsoft Excel sheet contains 50 projected rows, but only 2 have receipts.

### Required MCP posture

```json
{
  "verified": false,
  "witnesses": [],
  "render_green": false,
  "claim_state": "PRESERVED"
}
```

### Boundary

MCP may capture and timestamp.
MCP may not approve, verify, archive as truth, or greenlight UI.

---

## 4. Stage 2: CAV — CSV Audit Verification

### Role

CAV is the CSV / Excel witness layer.

It checks preserved claims and spreadsheet rows against receipts. A row only advances when the witness chain passes.

```text
A row is not a receipt.
A row is a claim.
A green row requires a receipt.
```

### Spreadsheet object

CAV treats every CSV / Excel row as a claim object:

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

If the claim is on-chain, CAV also requires:

```text
tx_hash
block_number
chain_id
contract_or_address
```

If the claim requires human approval, CAV also requires:

```text
requires_human_approval
approved_by
approved_at
approval_signature
```

### Required witness chain

| Witness | JoySpace Name | Machine Function | Fails if |
|---|---|---|---|
| 1 | Mrs. Wisdom Gate | `check_human_approval()` | `approved_at == null`, missing signature, or human veto |
| 2 | CSV Shape Witness | `validate_csv_required_fields()` | Required spreadsheet fields missing or invalid |
| 3 | Row SHA Witness | `sha256_row_matches()` | Computed row hash does not match submitted row hash |
| 4 | Receipt Link Witness | `verify_receipt_ref()` | Row points to no receipt, fake tx, missing approval, or broken source |

### CAV output rule

If all required witnesses pass:

```text
verified_claim.json MAY be created
verified_csv_row.json MAY be created
```

If any required witness fails:

```text
rejected_claims/{claim_id}.json MUST be created
ALMS MUST NOT receive the claim
render_green MUST remain false
```

### Example rejection

```json
{
  "claim_id": "KKB-00003",
  "row_number": 3,
  "status": "REJECTED",
  "reason": "no_source_receipt_for_csv_row",
  "message": "Spreadsheet row exists, but the row has no valid source receipt.",
  "NO_FAKE_GREEN": "ACTIVE"
}
```

---

## 5. Stage 3: ALMS — Automated Ledger of Minted Stories

### Role

ALMS is the append-only archive of verified receipts and verified spreadsheet rows.

ALMS may archive verified truth.
ALMS may not invent rows.
ALMS may not backfill fake events.
ALMS may not turn MCP captures into green status.
ALMS may not treat Excel formulas as authority.

### Entry conditions

A claim or row may enter ALMS only if:

```text
MCP captured it
CAV checked it
all required witnesses passed
schema validation passed
row hash matched when spreadsheet-sourced
integrity hashes matched
human approval passed when required
```

### Receipt assignment

ALMS assigns an immutable receipt identifier:

```text
RCB-00001
RCB-00002
RCB-00003
```

### Public/private artifact split

Public surface:

```text
badge
chart row
CSV entry
dashboard card
Excel export row
```

Private proof:

```text
source CSV SHA256
row SHA256
source SHA256
receipt SHA256
jq validation log
CAV validation log
witness signatures
approval receipt
chain receipt when applicable
```

### Insufficient events rule

If the target spreadsheet requests 50 rows but CAV verifies only 2, ALMS writes 2 rows and emits:

```json
{
  "requested_events": 50,
  "verified_events": 2,
  "rejected_events": 48,
  "INSUFFICIENT_EVENTS": true,
  "NO_FAKE_GREEN": "ACTIVE"
}
```

---

## 6. Stage 4: Surface Render

### Role

The surface is display only.

The UI may only read from ALMS for green status.
It may render chaotic draft art from MCP.
It may preview draft CSV rows.
It may not render verified badges or green spreadsheet rows from MCP or raw CSV.

### Surface law

```text
surface_may_read_mcp_for_draft_art = true
surface_may_read_csv_for_draft_rows = true
surface_may_read_mcp_for_green = false
surface_may_read_csv_for_green = false
surface_may_read_alms_for_green = true
```

### Display consequence

If ALMS has 2 verified receipts, the surface shows 2 verified receipts.
If a spreadsheet contains 50 claimed rows but ALMS has 2 verified rows, the surface shows 2 green rows and 48 yellow/rejected rows.
If a third claim exists only in MCP, raw CSV, Excel, or rejected claims, the surface must not display a third green row.

---

## 7. Fake Third Transfer Attempt

### Flow

1. MCP ingests claim: `Transfer #3 exists`.
2. CSV row claims Transfer #3.
3. CAV checks row shape, row hash, and receipt link.
4. `find_event_by_hash` fails.
5. CAV writes rejection.
6. ALMS never receives it.
7. Surface stays at 2 verified transfers.

### Validator stdout

```text
ANCHOR_READY = false
CSV_ENGINE = CAV
REAL_EVENTS = 2
CLAIMED_ROWS = 3
VERIFIED_ROWS = 2
FORGERY_DETECTED = true
SUMMARY = 2 verified transfers.
          1 row rejected: no source receipt.
          -> Row 3: no source receipt for tx_hash 0x123...
NO_FAKE_GREEN = ACTIVE
```

---

## 8. Teeth Table

| Layer | Cannot Do | Can Do |
|---|---|---|
| MCP | Approve, verify, render green | Capture, timestamp, preserve |
| CAV | Create ALMS receipts, invent truth, greenlight formulas | Verify CSV/Excel rows, reject rows, explain blockers |
| ALMS | Invent rows, overwrite history | Archive verified truth append-only |
| Surface | Read unverified data for green | Display ALMS-backed state |

---

## 9. Promotion Rules

```text
MCP:PRESERVED -> CAV:PENDING requires schema visibility
CAV:PENDING -> CAV:REJECTED requires failed witness reason
CAV:PENDING -> CAV:VERIFIED requires CSV shape + row hash + receipt link + required approval
CAV:VERIFIED -> ALMS:ARCHIVED requires receipt_id assignment
ALMS:ARCHIVED -> SURFACE:GREEN requires render_green true
```

No direct promotion from MCP to Surface.
No direct promotion from raw CSV/Excel to Surface Green.
No direct promotion from MCP to ALMS.
No green without ALMS.
No ALMS without CAV.
No CAV pass without witnesses.

---

## 10. Required Schema

Receipts must conform to:

```text
GOUJIAN/schemas/ALMS_RECEIPT_SCHEMA_V1.json
```

Spreadsheet source rules are specified in:

```text
GOUJIAN/specs/CAV_CSV_EXCEL_ENGINE_V0_1.md
```

Required schema concepts:

```text
requires_human_approval
human_approval
witness_chain
csv_engine
identity_anchor
integrity
surface_rules
no_fake_green
```

---

## 11. Current Ruling

```text
GitHub custody: PREPARED
Pipeline spec: YELLOW
CAV meaning: CSV Audit Verification
L1 anchor executed by this file: FALSE
Runtime validator executed by this file: FALSE
No Fake Green: ACTIVE
```

This document is a custody specification, not a deployed contract, not an on-chain transaction, and not a runtime verification result.
