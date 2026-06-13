# ALMS_ARCHIVE_RECEIPT_CUSTODY_LEDGER_V0_1

## STATUS: ARCHIVE_LEDGER_SPEC_DRAFT
## TRUTH_STATE: YELLOW
## NO_FAKE_GREEN: TRUE
## AUTHORITY: FALSE
## ANCHORED_TO: jaywisdom.eth
## ENGINE: jaywisdom.base.eth
## L1_ANCHOR_EXECUTED: FALSE

---

## 1. Correction

ALMS is not the spreadsheet engine.
ALMS is not the JSONL mapping lane.
ALMS is the archive custody ledger.

```text
MCP -> CAV -> ALMSL+ -> ALMS -> Surface
```

Expanded:

```text
Model Context Protocol
-> CSV Audit Verification
-> ALMS JSONL+ Line Item Mapping Lanes
-> Automated Ledger of Minted Stories
-> Surface Render
```

ALMS accepts only valid mapped line items from ALMSL+.
ALMS never reads raw MCP for green.
ALMS never reads raw CSV for green.
ALMS never invents rows.

---

## 2. ALMS Definition

```text
ALMS = Automated Ledger of Minted Stories
```

ALMS stores verified, mapped, receipt-bound events as append-only custody entries.

A minted story is not a fantasy claim.
A minted story is a human-readable event backed by machine-verifiable custody.

---

## 3. Core Law

```text
No ALMS entry without ALMSL+ line mapping.
No ALMS green without CAV witness pass.
No ALMS archive without receipt binding.
No Surface green without ALMS custody.
```

If fewer events are verified than claimed, ALMS records the smaller number and sets `insufficient_events = true`.

---

## 4. Required Inputs

An ALMS archive entry requires:

```text
almsl_line_id
almsl_line_sha256
source_row_sha256
cav_witness_ref
receipt_ref
claim_state
truth_state
render_green
no_fake_green
```

---

## 5. ALMS Archive Entry Object

```json
{
  "schema_name": "ALMS_ARCHIVE_ENTRY_V0_1",
  "entry_id": "RCB-00001",
  "entry_type": "MINTED_STORY_RECEIPT",
  "truth_state": "GREEN",
  "claim_state": "VERIFIED",
  "almsl_line_id": "ALMSL-000001",
  "almsl_line_sha256": "<64 hex>",
  "source_row_sha256": "<64 hex>",
  "cav_witness_ref": "CAV-000001",
  "receipt_ref": "receipt://example",
  "render_green": true,
  "insufficient_events": false,
  "no_fake_green": "PASS"
}
```

---

## 6. Archive Promotion Rule

```text
ALMSL_MAPPED
-> RECEIPT_BOUND
-> CAV_WITNESS_CONFIRMED
-> ALMS_ARCHIVED
-> SURFACE_GREEN_ALLOWED
```

ALMS must reject archive attempts when:

```text
almsl_line_sha256 missing
receipt_ref missing
CAV witness is not PASS
claim_state is not VERIFIED
truth_state is not GREEN
render_green is true before archive custody
no_fake_green is not PASS
```

---

## 7. Insufficient Events Rule

If a CSV claims 50 rows but CAV verifies 2 rows:

```text
claimed_events = 50
verified_events = 2
archived_events = 2
insufficient_events = true
surface_summary = "2 verified events; 48 unverified claims preserved."
```

ALMS must never pad the ledger to match a target count.

---

## 8. Tombstone Rule

ALMS archive entries are never edited in place.

Corrections require:

```text
lane_05_tombstone_or_supersession
new ALMSL+ line item
new ALMS archive entry
parent archive entry preserved
```

A bad archived entry is not deleted.
It is terminated with lineage.

---

## 9. Surface Rule

Surface may render green only from ALMS archive entries where:

```text
truth_state = GREEN
claim_state = VERIFIED
render_green = true
no_fake_green = PASS
receipt_ref exists
almsl_line_sha256 exists
```

Surface may display yellow, red, rejected, pending, or tombstoned states from ALMS metadata.
Surface may not promote raw MCP, raw CAV, or raw ALMSL+ data to green.

---

## 10. Final Ruling

```text
ALMS = Automated Ledger of Minted Stories
POSITION = after ALMSL+ and before Surface
STATUS = DRAFT
TRUTH_STATE = YELLOW
L1_ANCHOR_EXECUTED = FALSE
NO_FAKE_GREEN = ACTIVE
```
