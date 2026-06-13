# ALMSL_PLUS_JSONL_LINE_ITEM_MAPPING_LANES_V0_1

## STATUS: MAPPING_LANE_SPEC_DRAFT
## TRUTH_STATE: YELLOW
## NO_FAKE_GREEN: TRUE
## AUTHORITY: FALSE
## ANCHORED_TO: jaywisdom.eth
## ENGINE: jaywisdom.base.eth
## L1_ANCHOR_EXECUTED: FALSE

---

## 1. Correction

ALMSL+ is the missing bridge layer between CAV and ALMS.

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

ALMSL+ does not replace CAV.
ALMSL+ does not replace ALMS.
ALMSL+ maps verified spreadsheet rows into append-only JSONL ledger line items.

---

## 2. Core Law

```text
A spreadsheet row is a claim.
A JSONL line item is a mapped custody unit.
An ALMS receipt is archived truth only after witness pass.
A surface green badge requires ALMS receipt state, not raw CSV state.
```

No Fake Green remains active at every boundary.

---

## 3. Layer Duties

| Layer | Duty | Cannot Do |
| --- | --- | --- |
| MCP | Capture raw claim | Verify or render green |
| CAV | Verify CSV / Excel row | Archive truth |
| ALMSL+ | Map verified row to JSONL lane item | Invent verification |
| ALMS | Archive valid mapped line item as receipt | Invent rows |
| Surface | Render ALMS-backed state | Read raw MCP/CAV for green |

---

## 4. ALMSL+ Lane Types

Each JSONL line item must declare exactly one lane.

```text
lane_00_ingest_claim
lane_01_csv_row_claim
lane_02_cav_witness_result
lane_03_jsonl_mapping
lane_04_receipt_binding
lane_05_tombstone_or_supersession
lane_06_alms_archive
lane_07_surface_projection
```

### lane_00_ingest_claim
Raw MCP claim preserved. Never green.

### lane_01_csv_row_claim
Spreadsheet row extracted as canonical row data. Still a claim.

### lane_02_cav_witness_result
CAV witness output: human gate, shape witness, row hash witness, receipt link witness.

### lane_03_jsonl_mapping
ALMSL+ mapping event. This binds row hash, receipt reference, lane id, and parent line hash.

### lane_04_receipt_binding
External proof object or ALMS receipt reference attached.

### lane_05_tombstone_or_supersession
Correction lane. Any fixed row must point back to the old row hash or parent line hash.

### lane_06_alms_archive
ALMS accepts a mapped line item into append-only custody.

### lane_07_surface_projection
Dashboard/export row created from ALMS only. Never from raw CSV.

---

## 5. Required JSONL Line Item Fields

```json
{
  "schema_name": "ALMSL_PLUS_LINE_ITEM_V0_1",
  "line_id": "ALMSL-000001",
  "lane": "lane_03_jsonl_mapping",
  "truth_state": "YELLOW",
  "claim_state": "PARTIAL",
  "parent_line_sha256": null,
  "source_row_sha256": "<64 hex>",
  "line_sha256": "<64 hex>",
  "receipt_ref": null,
  "tombstone_ref": null,
  "render_green": false,
  "no_fake_green": true
}
```

---

## 6. Hash Rule

Every JSONL line is canonicalized before hashing.

```text
canonical_json = sorted_keys + no whitespace + UTF-8
line_sha256 = sha256(canonical_json_without_line_sha256)
```

If a line changes, it becomes a new line item.
Existing line items are never edited in place.

---

## 7. Promotion Rule

```text
CSV_ROW_CLAIM -> CAV_WITNESSED -> JSONL_MAPPED -> RECEIPT_BOUND -> ALMS_ARCHIVED -> SURFACE_GREEN
```

Failure to pass any step keeps the item YELLOW, RED, REJECTED, or TOMBSTONED.

---

## 8. Hard Blockers

```text
No green from raw CSV.
No green from MCP.
No green from lane_00 through lane_05.
No ALMS archive without JSONL mapping.
No JSONL mapping without row hash.
No correction without tombstone or supersession lane.
No L1 anchor claim without transaction hash and read-back proof.
```

---

## 9. Final Ruling

```text
ALMSL+ = ALMS JSONL+ Line Item Mapping Lanes
POSITION = between CAV and ALMS
STATUS = DRAFT
TRUTH_STATE = YELLOW
L1_ANCHOR_EXECUTED = FALSE
NO_FAKE_GREEN = ACTIVE
```
