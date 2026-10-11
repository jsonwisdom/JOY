# MSE_C14N_CORPUS_V0_1

## Status

```text
STATUS = LOCAL_PIN_DRAFT
CANON = false
AUTHORITY_CREATED = false
ROUTE_TAXONOMY_CHANGE = NONE
```

This sidecar materializes today's Machine-Speed Evidence canonicalization work beside the School of Wisdom lane without promoting it into repository canon.

## Field classes

```text
IDENTIFIER_FIELDS
  CHARSET = ASCII
  CASE = lowercase
  GRAMMAR = [a-z0-9._:-]+
  NFC = APPLIED, NO-OP ON VALID INPUT
  NON_ASCII_INPUT = HOLD NON_ASCII_IDENTIFIER

FREE_TEXT_FIELDS
  NFC = APPLIED
  RECEIPT_FIELD = normalization_applied
  EXCLUDED_FROM = identifier hashes, routing refs,
                  SET membership, ORDERED_LIST membership
```

The earlier P001/N004 collision is dissolved by field class. Same bytes + same type + same version + same resolver must still produce the same verdict.

## Safe integer boundary

```text
SAFE_INTEGER_MAX = 9007199254740991
2^53             = exactly representable, outside safe range
2^53 + 1         = not exactly representable in binary64
```

## Received vs decision input

```text
received_hash =
  SHA256("MSE:RECEIVED:V0_1" || 0x00 || raw_bytes)

input_hash =
  SHA256("MSE:INPUT:V0_1" || 0x00 || canonical_bytes)
```

received_hash proves what arrived.
input_hash proves what the decision consumed.
normalization_applied binds the transformation.

## Exam before harness

```text
PIN
├── STUDENT_A  independent
├── REF_IMPL   third rail; does not define the pin
└── STUDENT_B  independent
```

Required:

```text
A == PIN
AND B == PIN
AND A == B
```

NON_COMPLIANT is a harness result about an implementation, not a receipt verdict.

## Fixture bytes

`input.bin` and `expected.bin` are authoritative bytes.
`manifest.json` is an expectation map only.

## Open pins

```text
FRACTIONAL_PRECISION = HOLD
VERSION_FORMAT = HOLD
IDENTIFIER_LENGTH_BOUND = HOLD
```

Dependent vectors are BLOCKED_BY_UNPINNED_PARAMETER and do not count toward PASS totals.

## Scale rule

One pinned corpus. Many local adapters. No silent copies.

No fake green.
