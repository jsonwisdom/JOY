# MN CIVIC PACKET V1

## Purpose

This packet is the source artifact for Minnesota civic data verification under the ALMS six-proof invariant.

Primary identity: SHA256 of raw bytes.

CID is optional for distribution.

Witness is required for GREEN status.

## Included Records

- Sherco plant provenance: see `data/mn_civic/sherco_provenance.csv`

## Verification Instructions

1. Compute SHA256 of this file using raw bytes, no BOM, and LF line endings.
2. Compare the result against the hash recorded in `alms/claims/MN_CIVIC_PACKET_V1.json`.
3. Replay the claim path:

```text
source → hash → receipt → witness → verification
```

## Status

- [ ] Source bytes locked
- [ ] SHA256 recorded
- [ ] Claim JSON created
- [ ] Witness attested, such as EAS or equivalent
- [ ] NO_FAKE_GREEN: true

## Change Log

- 2026-06-13: Scaffold created.
