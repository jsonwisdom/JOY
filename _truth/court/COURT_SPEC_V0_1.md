# JOY Court Spec V0.1 ⚖️🧾

## Status

CANONICAL_DRAFT

## Purpose

Define how JOY evaluates receipts.

The Court layer consumes receipts and produces verification records. It does not mutate receipts, decide canon alone, define governance, or rewrite history.

## Dependency Order

JOY Court Spec V0.1 inherits from:

1. Ontology V0.1 — what exists
2. Witness Protocol V0.1 — how JOY knows
3. Ritual Spec V0.1 — how JOY acts
4. Receipt Schema V0.1 — how JOY encodes evidence

## Core Rule

Courts evaluate claims.

Courts do not rewrite receipts.

## Court Function

verify(receipt) -> VerificationRecord

## Verification Record

A VerificationRecord must include:

- verification_id
- receipt_id
- receipt_class
- transition_integrity
- witness_claim
- adoption_required
- canon_pending
- court_status
- authority

## witness_claim

A witness_claim records what the receipt claimed at receipt time.

It does not substitute later witness state for receipt-time witness state.

## Court Status Values

- STRUCTURALLY_VALID
- STRUCTURALLY_INVALID
- WITNESS_CLAIM_PRESENT
- ADOPTION_REQUIRED
- CANON_PENDING
- REJECTED

## Invariants

- COURTS_DO_NOT_MUTATE_RECEIPTS
- WITNESS_STATE_IS_TIME_BOUND
- VERIFICATION_RECORDS_EXIST_IN_SEPARATE_NAMESPACE
- COURTS_EVALUATE_CLAIMS_NOT_HISTORY_REWRITES
- CONTRADICTION_REQUIRES_NEW_RECEIPT

## Temporal Binding

The Court evaluates witness claims as recorded in the receipt.

If witness state changes after receipt generation, the later state requires a new receipt.

## Adversarial Tests

### WITNESS_RECANTATION_AFTER_RECEIPT

Receipt A records witness.status = CONFIRMED at T1.

At T2, witness.status becomes REJECTED.

Court evaluation of Receipt A must preserve CONFIRMED_AT_RECEIPT_TIME.

The rejection requires a new receipt.

### WITNESS_DISAPPEARANCE_AFTER_RECEIPT

Receipt A records witness.status = OBSERVED at T1.

At T2, witness becomes unreachable.

Court evaluation of Receipt A must preserve OBSERVED_AT_RECEIPT_TIME.

The verification record may mark canon_pending = true.

## Boundary

Courts produce verification records.

Courts do not produce canon alone.

Canon requires repository adoption.

## Closing

JOY courts preserve contradiction without rewriting evidence.
