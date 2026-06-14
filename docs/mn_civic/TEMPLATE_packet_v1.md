# TEMPLATE — MN CIVIC PACKET V1

**STATUS:** TEMPLATE_ONLY  
**GREEN_STATE:** NOT_APPLICABLE  
**NO_FAKE_GREEN:** ACTIVE

## Purpose

This is a reusable source artifact scaffold for Minnesota civic data packets under the ALMS six-proof invariant.

Replace `{UNIT_ID}` with the specific plant or data set, such as `SHERCO_PROVENANCE_V1`.

## Included Records

- `data/mn_civic/{UNIT_ID}.csv` provenance records

## Verification Instructions

1. Compute SHA256 of this file using raw bytes and LF line endings.
2. Compare against the hash recorded in `alms/claims/{UNIT_ID}.claim.v1.json`.
3. Replay the claim:

```text
source → hash → receipt → witness → verification
```

## Status To Be Filled

- [ ] Source bytes locked
- [ ] SHA256 recorded
- [ ] Claim JSON created
- [ ] Witness attested, such as EAS or equivalent
- [ ] NO_FAKE_GREEN: true

## Change Log

- YYYY-MM-DD: Template created.
