# ZORA SERIES ALPHA — JOY THESIS MIRROR

**STATUS:** MIRROR_SOURCE_DRAFT  
**GREEN_STATE:** FALSE  
**NO_NEW_ROOT:** TRUE  
**NO_FAKE_GREEN:** ACTIVE

## Purpose

ZORA_SERIES_ALPHA is a mirror surface for the verified MN_CIVIC_PACKET_V1 root.

This document is the Zora-side source artifact for a future on-chain mint mirror. It does not create a new root and does not reinterpret the civic packet.

It preserves provenance from the sovereign ALMS Unit 0 root and prepares an independent Zora replay path.

## Root Provenance

```text
ROOT_CLAIM:
MN_CIVIC_PACKET_V1

ROOT_STATE:
GREEN

SOURCE_COMMIT:
be73b5cf0b6f51de93da83d4bcee84fe57947f56

ROOT_HASH_SHA256_RAW_BYTES:
aa85eeefb848f5e23db9c8797015c65d1f44c7a6b4a76afbb9c53712f36e595d

ROOT_RECEIPT:
MN_CIVIC_PACKET_V1_SOURCE_HASH_RECEIPT

ROOT_REPLAY:
PASS

ROOT_WITNESS_TRACK:
Track019_MN_Civic_Provenance

ROOT_EAS_UID:
0x9e897d2acabc6133f481ebad69c5bbd9dadb5201cc7adce847cab5a00325f0c9

ROOT_TX_HASH:
0x3870fcd23e03e51f60c769d570c7896b7a9d0807bea455734bb618ba813d816c
```

## Mirror Rule

This Zora mirror inherits the verified root provenance of MN_CIVIC_PACKET_V1 but must earn its own GREEN state.

```text
Root provenance can be referenced.
Root authority cannot be copied.
Mirror source bytes must be committed.
Mirror hash must be computed from raw bytes.
Mirror replay must pass.
Mirror witness must be present before GREEN.
```

## Mint Framing

Working title:

```text
JOY Thesis Fragment — Source → Hash → Receipt → Witness → Verification
```

Core fragment:

```text
Verification is stronger than assertion.
Replay is stronger than memory.
Evidence is stronger than narrative.
```

## Verification Instructions

1. Compute SHA256 over raw bytes of this file.
2. Record the hash in `alms/claims/ZORA_SERIES_ALPHA.claim.v1.json`.
3. Confirm the root provenance still points to MN_CIVIC_PACKET_V1 GREEN.
4. Replay the mirror claim:

```text
make replay-zora-series-alpha
```

5. Do not mark ZORA_SERIES_ALPHA GREEN until its own replay and witness exist.

## Current State

```text
SOURCE_BYTES: PRESENT_AFTER_COMMIT
SOURCE_HASH: PENDING
CLAIM: MIRROR_DRAFT
REPLAY: PENDING
WITNESS: PENDING
GREEN_STATE: FALSE
NO_FAKE_GREEN: ACTIVE
```

## Closing

ZORA_SERIES_ALPHA is a mirror, not a new root.

The root remains MN_CIVIC_PACKET_V1.

The mirror exists to carry verified provenance across surfaces without narrative drift.
