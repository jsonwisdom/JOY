# Brenda Teacher Visual V2 — IPFS Receipt Template

Status: IPFS_RECEIPT_TEMPLATE_PENDING_CID
Truth State: YELLOW
Authority: false
No Fake Green: true
Repo: jsonwisdom/JOY
Lane: docs/school-of-wisdom/receipts/
Date: 2026-06-15
Created For: Jay Wisdom / jaywisdom.eth

## 1. Artifact

Name: Brenda the Teacher — Visual V2 / Meta Render Readback
Role: School of Wisdom / Brenda Math Class visual artifact
Style Boundary: original classroom collectible-style render; not a real-person likeness; not investment framing

## 2. Master File Metrics

These metrics are reported for the intended source-of-truth master file:

```text
IMAGE_DIMENSIONS = 1672 x 941
FILE_BYTES = 3968567
LOCAL_SHA256 = b9367bafed1e3415fd0dca42148b92c2921b52c74f15212b501a5d1ed784afd2
```

## 3. IPFS Pin Result

Fill after pinning the exact master file above:

```text
IPFS_CID =
PINNING_SERVICE =
PIN_TIMESTAMP_UTC =
GATEWAY_URL_1 =
GATEWAY_URL_1_HTTP_STATUS =
GATEWAY_URL_1_SHA256 =
GATEWAY_URL_1_BYTES =

GATEWAY_URL_2 =
GATEWAY_URL_2_HTTP_STATUS =
GATEWAY_URL_2_SHA256 =
GATEWAY_URL_2_BYTES =
```

## 4. Visual Elements Verified

```text
BOSS_BRENDA = GREEN
BEIGE_BRENDA = GREEN
GIRL_MATH_SLOT = GREEN
NO_FAKE_GREEN_BADGE = GREEN
RECEIPT_BEFORE_RUSH = GREEN
KIDS_KILLECTIBLE_STYLE = GREEN
```

## 5. Boundary Notes

A second local copy was observed with different metrics:

```text
ALT_COPY_DIMENSIONS = 1440 x 816
ALT_COPY_BYTES = 882861
ALT_COPY_SHA256 = 4fb221f1081449ca178ecc5e0c1fb529785c07ffc78eccd5a7de2791f0054ecb
```

This means:

```text
LOCAL_FILE_ALIGNMENT = YELLOW
Reason: multiple copies exist; only the 1672 x 941 / 3968567-byte file should be treated as the master for this receipt.
```

## 6. Evidence-Class Boundaries

This receipt may prove:

```text
VISUAL_V2_MASTER_FILE_RECORDED
IPFS_CID_FOR_MASTER_FILE
GATEWAY_BYTE_MATCH
```

This receipt does not prove:

```text
ZORA_MINT_STATUS
ONCHAIN_ATTESTATION
INVESTMENT_VALUE
PUBLIC_ROUTE_RENDERING
```

## 7. Ruling

```text
BRENDA_VISUAL_V2_MASTER_METRICS = GREEN_AS_REPORTED_INPUT
VISUAL_ELEMENTS_VERIFIED = GREEN
LOCAL_FILE_ALIGNMENT = YELLOW
IPFS_CID = YELLOW
GATEWAY_READBACK = YELLOW
ZORA_STATUS = YELLOW
ONCHAIN_ATTESTATION = YELLOW
NO_FAKE_GREEN = ACTIVE
```

## 8. Upgrade Rule

Only flip after evidence:

```text
IPFS_CID = GREEN_SCOPED
Reason: exact master file pinned and CID recorded

GATEWAY_READBACK = GREEN_SCOPED
Reason: at least two gateways return HTTP 200 with byte size 3968567 and SHA256 b9367bafed1e3415fd0dca42148b92c2921b52c74f15212b501a5d1ed784afd2

LOCAL_FILE_ALIGNMENT = GREEN_SCOPED
Reason: active local master file matches 1672 x 941 / 3968567 bytes / SHA256 b9367bafed1e3415fd0dca42148b92c2921b52c74f15212b501a5d1ed784afd2
```
