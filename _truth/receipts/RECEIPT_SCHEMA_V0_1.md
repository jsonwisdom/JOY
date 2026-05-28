# JOY Receipt Schema V0.1 🧾

## Status

CANONICAL_DRAFT

## Purpose

Define the minimal evidence grammar for JOY receipts.

Receipts are evidence objects. They bind artifacts, hashes, transitions, witnesses, and replay status.

This schema does not define courts, rituals, governance, or asset lifecycle rules.

## Core Rule

Receipts prove transitions. Receipts do not create authority.

## Required Fields

- receipt_id
- schema_version
- receipt_class
- artifact_id
- artifact_path
- artifact_sha256
- previous_state
- next_state
- transition
- canonicalization
- witness
- authority

## receipt_id

`sha256(jcs(receipt_without_receipt_id))`

## schema_version

`RECEIPT_SCHEMA_V0_1`

## receipt_class

Allowed values:

- RITUAL
- WITNESS
- ORACLE
- ASSET
- RECOVERY
- CLOSEOUT

## witness

A witness object must include:

- type
- status

Allowed witness types:

- LOCAL
- REMOTE
- ORACLE
- REPLAY
- RECOVERY

Allowed witness statuses:

- OBSERVED
- CONFIRMED
- REJECTED
- DRIFT_DETECTED
- RECOVERY_VERIFIED

## Canonicalization

Receipts use JCS canonicalization.

## Forbidden States

- authority_true
- missing_artifact_sha256
- receipt_without_class
- transition_without_previous_or_next_state
- canon_claim_without_witness_confirmation
- recovery_that_rewrites_history

## Boundary

A receipt may support canon.

A receipt does not decide canon alone.

Canon requires witness confirmation and repository adoption.

## Closing

JOY receipts are the evidence grammar future courts, rituals, and witnesses consume.
