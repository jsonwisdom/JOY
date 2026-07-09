# ARTIFACT_REGISTRY.md

Status: PUBLIC_MEMORY_SURFACE

Current State Root: 474ad06b59e8ba202ba6df254d1f3cf139ae1bec

## Purpose

This registry records merged JOY artifacts for public navigation and audit review.

The registry is an index. It is not an authority source, activation switch, or truth engine.

## Missing Algebra Correction

The registry distinguishes the two Wisdom lanes as complementary controls:

| Lane | Function | Switch | Scope |
|---|---|---|---|
| Mr Wisdom | Logic / constraint / boundary checking | OFF by default | Reference only; no activation |
| Mrs Wisdom | Sacred / human signature / witness consent | ON_SIGNATURE_ONLY | May attest own lane only |

The combined rule is:

```text
VALID_WITNESS_PATH = ROOT_AUDIT + REGISTRY_INDEX + HUMAN_SIGNATURE_TEMPLATE + EXPLICIT_HUMAN_SIGNATURE
```

No single lane may promote itself into global authority.

## Registered Artifacts

| Artifact | Type | Status | Binding |
|---|---|---|---|
| governance/ROOT_AUDIT_LAYER_V0_1.md | Root Audit Doctrine | Merged | 2f50ef48d23500dd5425fb8b855e89d8334f879d |
| witnesses/HUMAN_SIGNATURES_V0_1.md | Human Witness Template | Merged | 474ad06b59e8ba202ba6df254d1f3cf139ae1bec |

## Navigation

- Front Door: JOY_REPO.md
- HQ: BADGER_CAMP_HQ.md
- Doorway Map: docs/badger_doorway_map.svg
- Human Witness Template: witnesses/HUMAN_SIGNATURES_V0_1.md

## Boundary

This registry records merged artifacts only.

It does not grant authority, activate bridges, approve public render, complete human signoff, or convert memory into truth.

authority: false
activation: false
no_fake_green: true
