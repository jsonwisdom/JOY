# RCB_00001_00002_LOCAL_PARSE_HASH_WITNESS_V0_1

Status: LOCAL_PARSE_HASH_WITNESS_CAPTURED
Authority: false
Verified: local jq parse + raw byte sha256 witness
No Fake Green: true

## Source Commit

`5d6ed4f06a3f032f5a818901033e28edaa7fb78b`

## RCB-00001

Path: `artifacts/goblin_constellation_paths_v0_1.json`

```text
0901a84bdfa3eaa094004c5df12d9703e0dfea3f35fdf41af7301c00fe940e8b  receipts/zero_trust/chunks/rcb_00001_00002_step4/RCB-00001.json
3746795 receipts/zero_trust/chunks/rcb_00001_00002_step4/RCB-00001.json
jq type: "object"
required fields: true
```

## RCB-00002

Path: `artifacts/goblin_constellation_v0_1.json`

```text
3d8cf0121713ca8b69ee56f3436b0b6b9e4722acfc11742f6f330404ad493521  receipts/zero_trust/chunks/rcb_00001_00002_step4/RCB-00002.json
829614 receipts/zero_trust/chunks/rcb_00001_00002_step4/RCB-00002.json
jq type: "object"
required fields: true
```

## Boundary

```text
LOCAL_JQ_PARSE_SUCCESS != SEMANTIC_TRUTH
SHA256_RECORDED != AUTHORITY
BYTE_WITNESS != FINAL_TRUTH_RULING
NO_FAKE_GREEN_ACTIVE
```

## Ruling

Step 4 local full-content parse witness captured.
Step 5 raw-byte SHA256 witness captured.
No semantic truth ruling.
No authority implied.
No fake green.
