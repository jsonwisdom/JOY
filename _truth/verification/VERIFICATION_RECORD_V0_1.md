# JOY Verification Record V0.1 🧾⚖️

## Status

CANONICAL_DRAFT

## Purpose

Define the output object produced by JOY Court evaluation.

A Verification Record references a receipt and records the Court's evaluation result.

It does not mutate receipts.
It does not create canon.
It does not perform repository adoption.

## Dependency Order

Verification Record V0.1 inherits from:

1. Witness Protocol V0.1
2. Receipt Schema V0.1
3. Court Spec V0.1

## Core Rule

Verification records evaluate receipts.

Verification records do not decide canon.

## Required Fields

- verification_record_id
- schema_version
- receipt_id
- court_version
- transition_integrity
- witness_claim
- adoption_required
- canon_pending
- verification_errors
- authority

## verification_record_id

`sha256(jcs(record_without_verification_record_id))`

## schema_version

`VERIFICATION_RECORD_V0_1`

## court_version

`COURT_SPEC_V0_1`

## witness_claim

A witness_claim records the witness status claimed by the receipt at receipt time.

It must include:

- claimed_status
- witness_id
- as_of_receipt_time

`as_of_receipt_time` must be true.

## allowed claimed_status values

- OBSERVED
- CONFIRMED
- REJECTED
- DRIFT_DETECTED
- RECOVERY_VERIFIED

## Verification Errors

`verification_errors` must be an array.

On success, it must be empty.

On failure, it must contain structured error labels.

## Invariants

- VERIFICATION_RECORD_DOES_NOT_MUTATE_RECEIPT
- VERIFICATION_RECORD_DOES_NOT_CREATE_CANON
- TEMPORAL_BINDING_REQUIRED
- COURT_OUTPUT_EXISTS_IN_SEPARATE_NAMESPACE
- REPOSITORY_ADOPTION_REQUIRED_FOR_CANON

## Forbidden States

- authority_true
- missing_receipt_id
- missing_witness_claim
- as_of_receipt_time_false
- canon_claim_inside_verification_record
- receipt_mutation_by_verification_record

## Boundary

A Verification Record may support repository adoption.

A Verification Record does not decide repository adoption.

Canon requires repository adoption.

## Closing

JOY Verification Records preserve the separation between evidence evaluation and canon adoption.
