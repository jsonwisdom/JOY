# MCP_CAV_ALMS_RECEIPT_PIPELINE_V0_1

## STATUS: PIPELINE_SPEC_DRAFT
## TRUTH_STATE: YELLOW
## NO_FAKE_GREEN: TRUE
## AUTHORITY: FALSE
## ANCHORED_TO: jaywisdom.eth
## ENGINE: jaywisdom.base.eth
## L1_ANCHOR_EXECUTED: FALSE

---

## 1. Purpose

This document defines Jay's MCP CAV ALMS Receipt Pipeline:

```text
Model Context Protocol -> Content Authenticity Verification -> Automated Ledger of Minted Stories
```

The pipeline turns messy human moments into verifiable, receipt-aware records without faking warmth, certainty, authority, or green status.

Core law:

```text
NO_FAKE_GREEN = TRUE
```

Every green pixel needs a witness.

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

```text
MCP = microphone, not judge
```

### Input examples

- Mrs. Wisdom says yes to a badge.
- A transfer appears to hit `0x694cE46C64D9D1a5e9376A9feBcF85Ec05D72e9F`.
- Goblin Art Studio mints a link.
- A user claims a third transfer exists.

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

## 4. Stage 2: CAV — Content Authenticity Verification

### Role

CAV is the witness layer.

It checks the preserved claim against gates. A claim only advances when the witness chain passes.

### Required witness chain

| Witness | JoySpace Name | Machine Function | Fails if |
|---|---|---|---|
| 1 | Mrs. Wisdom Gate | `check_human_approval()` | `approved_at == null`, missing signature, or human veto |
| 2 | jq Doctrine | `validate_schema()` | Required fields missing or invalid |
| 3 | SHA Witness | `sha256_matches()` | Byte hash does not match source hash |

### CAV output rule

If all required witnesses pass:

```text
verified_claim.json MAY be created
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
  "status": "REJECTED",
  "reason": "human_veto_or_missing_human_approval",
  "message": "Valid receipt shape, but awaiting Mrs. Wisdom approval.",
  "NO_FAKE_GREEN": "ACTIVE"
}
```

---

## 5. Stage 3: ALMS — Automated Ledger of Minted Stories

### Role

ALMS is the append-only archive of verified receipts.

ALMS may archive verified truth.
ALMS may not invent rows.
ALMS may not backfill fake events.
ALMS may not turn MCP captures into green status.

### Entry conditions

A claim may enter ALMS only if:

```text
MCP captured it
CAV checked it
all required witnesses passed
schema validation passed
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
```

Private proof:

```text
source SHA256
receipt SHA256
jq validation log
witness signatures
approval receipt
chain receipt when applicable
```

### Insufficient events rule

If the target surface requests 50 rows but CAV verifies only 2, ALMS writes 2 rows and emits:

```json
{
  "requested_events": 50,
  "verified_events": 2,
  "INSUFFICIENT_EVENTS": true,
  "NO_FAKE_GREEN": "ACTIVE"
}
```

---

## 6. Stage 4: Surface Render

### Role

The surface is display only.

The UI may only read from ALMS for green status.
It may render chaotic draft art from MCP, but it may not render verified badges from MCP.

### Surface law

```text
surface_may_read_mcp_for_draft_art = true
surface_may_read_mcp_for_green = false
surface_may_read_alms_for_green = true
```

### Display consequence

If ALMS has 2 verified receipts, the surface shows 2 verified receipts.
If a third claim exists only in MCP or rejected claims, the surface must not display a third green row.

---

## 7. Fake Third Transfer Attempt

### Flow

1. MCP ingests claim: `Transfer #3 exists`.
2. CAV checks chain evidence.
3. `find_event_by_hash` fails.
4. CAV writes rejection.
5. ALMS never receives it.
6. Surface stays at 2 verified transfers.

### Validator stdout

```text
ANCHOR_READY = false
REAL_EVENTS = 2
CLAIMED_EVENTS = 3
FORGERY_DETECTED = true
SUMMARY = 2 verified transfers.
          1 row(s) rejected: no source receipt.
          -> Row 3: no source receipt for tx_hash 0x123...
NO_FAKE_GREEN = ACTIVE
```

---

## 8. Teeth Table

| Layer | Cannot Do | Can Do |
|---|---|---|
| MCP | Approve, verify, render green | Capture, timestamp, preserve |
| CAV | Create ALMS receipts, invent truth | Verify, reject, explain blockers |
| ALMS | Invent rows, overwrite history | Archive verified truth append-only |
| Surface | Read unverified data for green | Display ALMS-backed state |

---

## 9. Promotion Rules

```text
MCP:PRESERVED -> CAV:PENDING requires schema visibility
CAV:PENDING -> CAV:REJECTED requires failed witness reason
CAV:PENDING -> CAV:VERIFIED requires all witnesses PASS
CAV:VERIFIED -> ALMS:ARCHIVED requires receipt_id assignment
ALMS:ARCHIVED -> SURFACE:GREEN requires render_green true
```

No direct promotion from MCP to Surface.
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

Required schema concepts:

```text
requires_human_approval
human_approval
witness_chain
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
L1 anchor executed by this file: FALSE
Runtime validator executed by this file: FALSE
No Fake Green: ACTIVE
```

This document is a custody specification, not a deployed contract, not an on-chain transaction, and not a runtime verification result.
