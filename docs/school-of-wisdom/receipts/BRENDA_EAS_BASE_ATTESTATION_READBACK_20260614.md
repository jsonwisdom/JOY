# Brenda Teacher Kids — EAS Base Attestation Readback

Status: EAS_BASE_ATTESTATION_READBACK_GREEN_SCOPED
Truth State: GREEN_SCOPED
Authority: false
No Fake Green: true
Repo: jsonwisdom/JOY
Lane: docs/school-of-wisdom/receipts/
Date: 2026-06-14
Created For: Jay Wisdom / jaywisdom.eth

## 1. Evidence Class

Evidence class: USER_PROVIDED_EAS_BASE_READBACK

This receipt records the EAS Base attestation details provided by the operator from the EAS Base scan page.

Independent browser fetch by the assistant was not completed, so independent explorer readback remains a separate evidence class.

## 2. Attestation Summary

Network: Base mainnet
Attestation type: Onchain Attestation
Schema: #1597
Schema UID short: 0x70e30c...2ad1fb88
Recipient: No recipient
Referenced Attestation: No reference
Referencing Attestations: 0

UID:

```text
0xd62d02a443102ebebec5eba16809115bd38f28ce4037a90e9a2bf6c5c79b825f
```

Transaction ID:

```text
0xd2431dba40a1d93381c023aa02843238cdfdc7e410692070f72ece0d5a5bf142
```

Created:

```text
06/14/2026 8:35:03 pm
```

Expiration: Never
Revoked: No
Revocable: Yes

From / Attester:

```text
0x1dB2C056c7DeCD9f9fC574692b05F62aE34Fb8b5
```

## 3. Decoded Data

Docket_id:

```text
BRENDA_TEACHER_KIDS_KILLECTIBLE_20260615
```

Docket_sha256:

```text
0xe499a52e160c8a1fa9a43e6441db3fb611dc764c842e5bcd9e0357ef72244c87
```

Verifier_version:

```text
BRENDA_IPFS_LOCAL_VERIFY_V0_1
```

Verifier_sha256:

```text
EMPTY_BYTES32 / NOT PROVIDED
```

Receipt_sha256:

```text
EMPTY_BYTES32 / NOT PROVIDED
```

Receipt_uri:

```text
https://github.com/jsonwisdom/JOY/blob/main/docs/school-of-wisdom/receipts/BRENDA_TEACHER_KIDS_IPFS_LOCAL_VERIFICATION_RECEIPT_20260615.md
```

Verified_at:

```text
1781486454
```

Truth_state:

```text
GREEN_SCOPED
```

No_fake_green:

```text
True
```

## 4. Artifact Linkage

This attestation references the previously verified artifact bytes:

CID:

```text
bafkreihetgss4fqmrip2tjb6mra5wp5wchohmteefzn43hqdk7xxejcmq4
```

SHA256:

```text
e499a52e160c8a1fa9a43e6441db3fb611dc764c842e5bcd9e0357ef72244c87
```

Byte size:

```text
167072
```

## 5. Boundary Notes

The attestation proves an onchain EAS record exists as reported by the operator readback.

This receipt does not prove:

- Zora mint status
- Zora coin metadata match
- independent explorer fetch by assistant
- verifier file hash, because VERIFIER_SHA256 was intentionally left blank
- receipt file hash, because RECEIPT_SHA256 was intentionally left blank

Those remain separate evidence classes.

## 6. Ruling

```text
EAS_BASE_ATTESTATION_UID = GREEN_AS_OPERATOR_READBACK
EAS_BASE_TRANSACTION_ID = GREEN_AS_OPERATOR_READBACK
ONCHAIN_ATTESTATION = GREEN_SCOPED_BY_EAS_READBACK
ATTESTER_ADDRESS = GREEN_AS_OPERATOR_READBACK
DOCKET_SHA256 = GREEN_SCOPED_MATCHES_VERIFIED_ARTIFACT_SHA256
RECEIPT_URI = GREEN_AS_REPO_LINK
NO_FAKE_GREEN_FIELD = GREEN_TRUE
VERIFIER_SHA256 = YELLOW_EMPTY
RECEIPT_SHA256 = YELLOW_EMPTY
INDEPENDENT_EXPLORER_FETCH_BY_ASSISTANT = YELLOW
ZORA_MINT_STATUS = YELLOW
NO_FAKE_GREEN = ACTIVE
```
