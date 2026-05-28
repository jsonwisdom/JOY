# JOY Repository Spec V0.1 🏛️🧾

## Status

CANONICAL_DRAFT

## Purpose

Define how JOY adopts canon.

The Repository layer consumes Verification Records and produces canonical state transitions.

It does not re-evaluate receipts.
It does not mutate Verification Records.
It does not rewrite history.

## Dependency Order

Repository Spec V0.1 inherits from:

1. Verification Record V0.1
2. Court Spec V0.1
3. Receipt Schema V0.1
4. Witness Protocol V0.1
5. Ontology V0.1

## Core Rule

Repository adoption is the only canon-producing operation.

## Repository Input

The Repository consumes Verification Records.

Required input fields:

- verification_record_id
- receipt_id
- transition_integrity
- witness_claim
- adoption_required
- canon_pending
- verification_errors
- authority

## Adoption Conditions

A Verification Record may be adopted only if:

- transition_integrity is true
- canon_pending is true
- verification_errors is empty
- authority is false
- witness_claim.as_of_receipt_time is true

## Repository Output

A repository adoption event must produce:

- adoption_id
- verification_record_id
- adopted_state
- previous_canon_state
- next_canon_state
- repository_head
- adoption_status
- authority

## adoption_id

`sha256(jcs(adoption_without_adoption_id))`

## Adoption Status Values

- ADOPTED
- DEFERRED
- REJECTED

## Invariants

- REPOSITORY_ADOPTION_CREATES_CANON
- REPOSITORY_DOES_NOT_REEVALUATE_RECEIPTS
- REPOSITORY_DOES_NOT_MUTATE_VERIFICATION_RECORDS
- CANON_REQUIRES_REPOSITORY_ADOPTION
- AUTHORITY_REMAINS_FALSE
- HISTORY_IS_APPEND_ONLY

## Forbidden States

- adoption_without_verification_record
- adoption_with_verification_errors
- adoption_with_authority_true
- receipt_reinterpretation_by_repository
- verification_record_mutation_by_repository
- retroactive_canon_rewrite

## Boundary

The Repository decides adoption.

The Repository does not decide truth.

Truth is evaluated by witnesses and courts before repository adoption.

## Closing

JOY canon is adopted through explicit repository transitions, not inferred from evidence alone.
