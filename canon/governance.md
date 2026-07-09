# JOY Governance Doctrine v0.1

## Purpose

JOY governance rails define what is allowed to enter `main`.  
They are protocol rules, not suggestions.

## Merge Classes

- **DOC_ONLY:** doctrine/docs only — must pass lint + invariant scan.
- **SCHEMA:** JSON schema change — schema validation required.
- **RECEIPT:** evidence packet — hash + replay check required.
- **MEMBRANE:** gate/rule change — stricter review, human witness required.
- **ADAPTER:** external bridge — no authority + replay receipt required.
- **PUBLIC_RENDER:** Zora/IPFS/art output — consent + receipt + hash required.

## Hard Blocks

A PR MUST fail if it contains:

- `authority: true`
- `green_implied: true`
- `load_verified: true` without a receipt
- `public_release_allowed: true` without consent
- private family data in public paths
- external links treated as proof without receipts

## Mrs. Wisdom Gate

Any PR touching:

- `family/` or `FAMILY/`
- `membranes/wisdom_membrane/`
- `receipts/decisions/`
- public render metadata

MUST declare:

- `wisdom_review_required: true`
- `consent_status: explicit | pending | not_applicable`
- `public_render_allowed: false` unless explicit consent exists.

## Governance Status

`JOY_GOVERNANCE_RAILS_V0_1_READY`
