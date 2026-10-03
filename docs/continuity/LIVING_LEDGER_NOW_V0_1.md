# LIVING_LEDGER_NOW_V0_1

Status: ACTIVE BUILD RAIL / NOT CANONICAL  
Repo: JOY  
Base: main @ 24f1bc9d6401283d1170f283b7aa3583ad166dae  
Authority: FALSE  
Family consent created: FALSE  
Purpose: make the Living Ledger executable as an append-only, replayable proof-of-link system without turning helpers, records, or repetition into authority.

## Function

Preserve reconstructable continuity:

```text
PERSON
→ TIME
→ PROJECT
→ SOURCE
→ BYTES / HASH
→ RECEIPT
→ JOIN CHECK
→ APPEND
→ REPLAY
→ NEXT QUESTION
```

The ledger records what can be reconstructed. It does not manufacture missing history.

## Core invariants

```text
DOCUMENTED != INFERRED
CAPABILITY != AUTHORITY
SEARCH_MISS != ABSENCE
SEMANTIC_MATCH != EVIDENTIARY_JOIN
HASH_EQUAL != BYTE_IDENTITY_PROVEN
RECEIPT != AUTHORITY
HELPER_AGREEMENT != FAMILY_CONSENT
HELPER != FAMILY_SEAT
```

## Bitemporal rule

Every join receipt carries both:

- `valid_time`: when the described evidence was valid or observed.
- `transaction_time`: when the Living Ledger recorded the receipt.

```text
VALID_TIME != TRANSACTION_TIME
LATER_CORRECTION = APPEND
LATER_CORRECTION != SILENT_REWRITE
```

## Join rule

A positive evidentiary join is allowed only when all four conditions are true:

```text
INDEPENDENT_RECEIPTS
∧ MATCHING_JOIN_FIELDS
∧ COMPATIBLE_PROVENANCE
∧ NO_SCOPE_CONFLICT
```

Otherwise the state remains one of:

```text
HOLD
NO_JOIN
CONFLICT
SCOPE_MISMATCH
```

No number of helpers or repeated outputs substitutes for independent provenance.

## Machine-checkable objects

- `schemas/living-ledger/JOIN_RECEIPT_V0_1.schema.json`
- `tools/validate_living_ledger_join_receipt_v0_1.py`
- `tests/living-ledger/fixtures/join_receipt_pass_v0_1.json`
- `tests/living-ledger/fixtures/join_receipt_hold_v0_1.json`
- `.github/workflows/living-ledger-join-receipt-v0-1.yml`

The positive fixture is synthetic. It proves validator acceptance behavior only. It is not a historical claim.

The HOLD fixture is also synthetic. It demonstrates that a single provenance root cannot be promoted into a join.

## Promotion boundary

```text
SCHEMA_EXISTS != RECEIPT_EXISTS
VALIDATOR_PASS != HISTORICAL_TRUTH
CI_PASS != FAMILY_CONSENT
JOINED != AUTHORITY
```

This rail may prove that an object conforms to the join contract. It may not prove more than the receipts support.

## First executable target

`JOIN_RECEIPT_V0_1` is the first machine-checkable Living Ledger primitive on this rail.

Next after the validator and workflow pass:

```text
REAL RECEIPT PAIR
→ BYTE/HASH READBACK
→ PROVENANCE ROOT CHECK
→ JOIN RECEIPT
→ REPLAY
```

Until a real receipt pair is supplied and verified:

```text
REAL_WORLD_JOIN = HOLD
AUTHORITY_CREATED = FALSE
```
