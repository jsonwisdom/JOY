# Brenda Teacher Kids Killectible — IPFS / Local Byte Verification Receipt

Status: VERIFICATION_GREEN_SCOPED_AFTER_OPERATOR_OUTPUT
Truth State: GREEN_SCOPED
Authority: false
No Fake Green: true
Repo: jsonwisdom/JOY
Lane: docs/school-of-wisdom/receipts/
Date: 2026-06-15
Created For: Jay Wisdom / jaywisdom.eth

## 1. Artifact

Name: Brenda the Teacher — Kids Killectible First Draft
CID:

```text
bafkreihetgss4fqmrip2tjb6mra5wp5wchohmteefzn43hqdk7xxejcmq4
```

Prior CID receipt:

```text
docs/school-of-wisdom/receipts/BRENDA_TEACHER_KIDS_KILLECTIBLE_CID_RECEIPT_20260614.md
```

Cleanup commit for stray test file:

```text
fc33c37355b34070fac80c9f2163dab220592f46
```

## 2. Gateway Readback Results

Operator command output timestamp window:

```text
2026-06-15T01:20:53Z to 2026-06-15T01:20:54Z
```

Gateway 1:

```text
gateway_name: ipfs_io
gateway_url: https://ipfs.io/ipfs/bafkreihetgss4fqmrip2tjb6mra5wp5wchohmteefzn43hqdk7xxejcmq4
http_status: 200
downloaded_file: /home/jaywisdom44/brenda_ipfs_check_20260615T012053Z/ipfs_io.png
byte_size: 167072
sha256: e499a52e160c8a1fa9a43e6441db3fb611dc764c842e5bcd9e0357ef72244c87
timestamp_utc: 2026-06-15T01:20:53Z
```

Gateway 2:

```text
gateway_name: dweb_link
gateway_url: https://bafkreihetgss4fqmrip2tjb6mra5wp5wchohmteefzn43hqdk7xxejcmq4.ipfs.dweb.link/
http_status: 200
downloaded_file: /home/jaywisdom44/brenda_ipfs_check_20260615T012053Z/dweb_link.png
byte_size: 167072
sha256: e499a52e160c8a1fa9a43e6441db3fb611dc764c842e5bcd9e0357ef72244c87
timestamp_utc: 2026-06-15T01:20:54Z
```

Gateway comparison:

```text
GATEWAY_1_EQUALS_GATEWAY_2 = GREEN_SCOPED
Reason: both gateways returned HTTP 200, byte_size 167072, and identical SHA256 e499a52e160c8a1fa9a43e6441db3fb611dc764c842e5bcd9e0357ef72244c87
```

## 3. Local CID Verification

Local command output:

```text
ipfs CLI found
added bafkreihetgss4fqmrip2tjb6mra5wp5wchohmteefzn43hqdk7xxejcmq4 ipfs_io.png
163.16 KiB / 163.16 KiB 100.00%
```

Local CID comparison:

```text
LOCAL_CID_EQUALS_RECORDED_CID = GREEN_SCOPED
Reason: local ipfs add --only-hash output returned the same CID: bafkreihetgss4fqmrip2tjb6mra5wp5wchohmteefzn43hqdk7xxejcmq4
```

## 4. Evidence-Class Boundaries

This receipt proves:

```text
IPFS_GATEWAY_READBACK = GREEN_SCOPED
LOCAL_PNG_BYTE_MATCH = GREEN_SCOPED
CID_VALUE_RECORDED = GREEN
```

This receipt does not prove:

```text
ZORA_MINT_STATUS = YELLOW
ONCHAIN_ATTESTATION = YELLOW
PUBLIC_ROUTE_RENDERING = YELLOW
INVESTMENT_VALUE = FALSE
```

## 5. Final Ruling

```text
BRENDA_TEACHER_ART_CID = GREEN_AS_USER_PROVIDED_INPUT
CID_VALUE_RECORDED = GREEN
CID_RECEIPT_READBACK = GREEN
READBACK_NOTE = GREEN
STRAY_TEST_FILE_CREATED = RESOLVED_GREEN
IPFS_GATEWAY_READBACK = GREEN_SCOPED
GATEWAY_BYTE_MATCH = GREEN_SCOPED
LOCAL_PNG_BYTE_MATCH = GREEN_SCOPED
ZORA_MINT_STATUS = YELLOW
ONCHAIN_ATTESTATION = YELLOW
NO_FAKE_GREEN = ACTIVE
```
