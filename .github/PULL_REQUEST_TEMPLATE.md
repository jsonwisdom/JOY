# JOY Governance Rails v0.1 — Pull Request Template

## Artifact Classification

- Artifact type: (DOC_ONLY | SCHEMA | RECEIPT | MEMBRANE | ADAPTER | PUBLIC_RENDER)
- Affected membrane:
- External surfaces touched: (GitHub | Zora | IPFS | Chain | Other)

## Consent & Family Impact

- Consent impact: (none | new | updated | revoked)
- Family artifacts touched: (yes | no)
- Consent status: (explicit | pending | not_applicable)

## Replay & Receipts

- Replay evidence: (link/path to replay log or test)
- Receipt path: (receipts/... file(s))
- Public render allowed: (true | false)
- Hash / content identifier (if PUBLIC_RENDER):

## Authority & Invariants

- Authority claimed: false
- No fake green: true

Confirm invariants:

- JOY_AUTHORITY_FALSE
- JOY_NO_FAKE_GREEN
- JOY_CONSENT_REQUIRED_FOR_FAMILY_ARTIFACTS
- JOY_REPLAY_REQUIRED_FOR_PUBLIC_RENDER
- JOY_RECEIPT_REQUIRED_FOR_GOVERNED_MERGE
- JOY_EXTERNAL_ADAPTERS_ARE_NOT_SOURCES_OF_TRUTH

## Merge Class Justification

Explain why the chosen Artifact type and Merge Class are correct:

- Merge class reasoning:
- Risk assessment:
- Mrs. Wisdom review required: (true | false)
