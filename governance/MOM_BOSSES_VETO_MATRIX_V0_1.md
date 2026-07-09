# MOM_BOSSES_VETO_MATRIX_V0_1

Status: VETO_MATRIX_DRAFT

Parent Commit SHA: cc906c5f75f92bfcd69321f4212a0be30b25b12b

Depends On:

- PR #54: Registry algebra and HUMAN_SIGNATURES_V0_1 index
- PR #55: MR_WISDOM_CONSTRAINT_LEDGER_V0_1

## Purpose

Mom Bosses is the final family-context review and veto surface for JOY factory routing.

This matrix defines when a family-context artifact must stop even if logic, routing, witness templates, or receipts appear valid.

## Boundary

Mom Bosses may veto.

Mom Bosses may request more context.

Mom Bosses may block public family render.

Mom Bosses may override logic-green.

Mom Bosses does not grant global authority.

Mom Bosses does not activate production by itself.

Mom Bosses does not convert memory into truth.

## Authority

authority: scoped_family_review_only
global_authority: false
activation: false
public_render: false
no_fake_green: true

## Veto Outputs

| Output | Meaning | Production Effect |
|---|---|---|
| MOM_REVIEW_PASS | No family-context veto observed | Continue to receipt/render gate |
| MOM_REVIEW_VETO | Explicit veto or blocking condition observed | Stop path |
| MORE_CONTEXT_REQUIRED | Review cannot safely decide | Stop and request more context |
| HUMAN_WITNESS_REQUIRED | Human witness missing or incomplete | Route to human witness lane |
| FAMILY_SCOPE_TOO_BROAD | Claimed scope exceeds stated family context | Stop path |
| PUBLIC_RENDER_BLOCKED | Public release is not approved | Block render |
| SACRED_CONTEXT_PROTECTED | Sensitive or sacred context requires protection | Stop path |
| GOVERNANCE_GAP | Required evidence or prior gate missing | Stop path |

## Mandatory Veto Conditions

Mom Bosses must veto when any of the following are true:

- Logic-green is treated as family approval.
- Registry indexing is treated as family approval.
- A witness template is treated as an actual human signature.
- A family relationship is inferred without explicit scope.
- Public render is requested without final family review.
- Sensitive family context is being flattened into entertainment.
- Sacred context is being converted into production output without consent.
- A card, image, story, or artifact claims family truth without replay-bound witness.
- A render path tries to bypass Mom Bosses after Sister routing.
- Any lane claims global authority from scoped family review.

## Context Request Conditions

Mom Bosses must request more context when:

- The relationship scope is unclear.
- The witness statement is ambiguous.
- Consent appears partial, stale, or indirect.
- The render purpose is unclear.
- The artifact may affect living persons.
- The artifact may expose private family material.
- The artifact mixes parody with family memory.

## Routing Algebra

```text
FAMILY_RENDER_ELIGIBLE =
ROOT_AUDIT_PASS
+ REGISTRY_INDEXED
+ MR_WISDOM_CONSTRAINT_PASS
+ FAMILY_ALGORITHM_SISTER_CONTEXT_CHECK
+ MRS_WISDOM_SIGNATURE_CONSENT
+ MOM_REVIEW_PASS
+ REPLAY_RECEIPT_BOUND
```

## Non-Promotion Rules

```text
MOM_REVIEW_PASS != GLOBAL_AUTHORITY
MOM_REVIEW_PASS != AUTOMATIC_PUBLIC_RENDER
MOM_REVIEW_PASS != FAMILY_TRUTH
```

A Mom Bosses pass only clears the veto gate for the declared scope.

It does not approve anything outside that scope.

## Demotion Rules

- Missing Mr Wisdom constraint result: GOVERNANCE_GAP
- Missing Family Algorithm Sister routing: FAMILY_CONTEXT_REQUIRED
- Missing human signature: HUMAN_WITNESS_REQUIRED
- Missing Mom Bosses review: MOM_REVIEW_REQUIRED
- Missing replay receipt: RECEIPT_GAP
- Public render without Mom review: PUBLIC_RENDER_BLOCKED
- Scope expansion after approval: FAMILY_SCOPE_TOO_BROAD
- Sacred context conflict: SACRED_CONTEXT_PROTECTED

## Ledger Status

This veto matrix is a draft review surface.

It is safe for review and sequencing only.

It does not execute code, activate production, approve public render, or grant authority.
