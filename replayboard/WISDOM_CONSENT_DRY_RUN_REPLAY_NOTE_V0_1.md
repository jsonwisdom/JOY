# WISDOM_CONSENT_DRY_RUN_REPLAY_NOTE_V0_1

JOY ReplayBoard — Governance Rails v0.1

## Summary

This replay note documents the dry-run activation of the Mrs. Wisdom consent lane.

## Replay Inputs

- Ingress Receipt: `receipts/ingress/WISDOM_CONSENT_DRY_RUN_INGRESS_V0_1.json`
- Decision Receipt: `receipts/decisions/WISDOM_CONSENT_DRY_RUN_DECISION_V0_1.json`

## Replay Outcome

- Consent lane activated: YES
- Consent status: pending
- Public render allowed: NO
- Authority: false
- No Fake Green: true
- Governance rails: upheld
- Drift: none detected

## Governance Invariants

- JOY_AUTHORITY_FALSE
- JOY_NO_FAKE_GREEN
- JOY_CONSENT_REQUIRED_FOR_FAMILY_ARTIFACTS
- JOY_REPLAY_REQUIRED_FOR_PUBLIC_RENDER
- JOY_RECEIPT_REQUIRED_FOR_GOVERNED_MERGE
- JOY_EXTERNAL_ADAPTERS_ARE_NOT_SOURCES_OF_TRUTH

## Notes

This dry-run confirms that the Mrs. Wisdom membrane is functioning as a protective consent gate. It does not approve public render, does not claim authority, and does not imply green beyond this dry-run receipt.
