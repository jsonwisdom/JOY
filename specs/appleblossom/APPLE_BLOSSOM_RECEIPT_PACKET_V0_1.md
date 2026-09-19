# APPLE BLOSSOM RECEIPT PACKET V0.1

Status: DRAFT / MACHINE-CHECKABLE / FAMILY-SAFE / NO_FAKE_GREEN

## Purpose

Define the smallest canonical packet that may move meaning between JoySpace, JaySpace, Apple Blossom, CrissCrossAppleSauce, and downstream family or institutional lanes without forcing a global merge or silently rewriting source language.

## Constitutional rules

```text
EXACT_WORDS_FIRST = TRUE
DOCUMENTS_FIRST = TRUE
OPENAI_MEMORY != CANON
MODEL_OUTPUT != AUTHORITY
PACKET != PERSON
PACKET != GENEALOGY
PACKET != CONSENT
PACKET != LEGAL_FINDING
PACKET != GLOBAL_TRUTH
MISSING_RECEIPT != ILLEGALITY_PROVEN
DIVERGENCE != ERROR
RECONCILIATION != OVERWRITE
AUTHORITY_CREATED = FALSE
```

## Packet identity

Every packet has its own immutable `packet_id` and a stable `packet_version`. A packet may reference a predecessor but never edits the predecessor's historical meaning in place.

```text
SOURCE OBJECT
→ EXACT WORDS / BYTES
→ SOURCE HASH
→ CONTEXT
→ CLAIM / QUESTION
→ EVIDENCE REFS
→ AUTHORITY REFS
→ DELTA STATE
→ PRIVACY / CONSENT BOUNDARY
→ REPLAY RESULT
→ SURFACE RECEIPTS
```

## Required fields

- `schema`: fixed identifier `APPLE_BLOSSOM_RECEIPT_PACKET_V0_1`
- `packet_version`: semantic packet version
- `packet_id`: UUID
- `created_at`: ISO-8601 timestamp
- `producer`: actor/system label that assembled the packet; not proof of identity
- `source_object`: source locator + media type + SHA-256 when bytes are available
- `exact_words`: literal human/source wording when wording is part of the claim
- `subject_scope`: privacy-preserving subject key; never name-only identity linkage
- `claim`: bounded proposition or question carried by the packet
- `evidence_refs`: zero or more source receipts supporting or contradicting the claim
- `authority_refs`: zero or more statutes/rules/orders/policies relevant to authority
- `delta`: prior/new state relationship, including HOLD and CONFLICT states
- `privacy`: publication and PII controls
- `consent`: explicit consent state when family sharing is implicated
- `replay`: deterministic replay status and unresolved requirements
- `surface_receipts`: GitHub/Drive/other durable-surface pointers
- `authority_created`: always `false`

## Exact-word law

If a human phrase is the retrieval key, preserve it byte-for-byte in `exact_words.original`. Assistant or system paraphrases belong only in `exact_words.derived_variants` and may never replace the original query key.

```text
HUMAN WORDS = PRIMARY QUERY
PARAPHRASE = SECONDARY SEARCH AID
SYSTEM LABEL != HUMAN SPEECH
AI SUMMARY != USER STATEMENT
```

## Delta states

Allowed packet delta states:

```text
NO_CHANGE
OBSERVED
HOLD
NOT_REPLAYABLE
DELTA_CONFLICT
CORRECTION
SUPERSEDED_BY_RECEIPT
```

`HOLD` means evidence is incomplete. It is not a legal conclusion.

`DELTA_CONFLICT` requires preservation of both competing receipts and a comparison of date, source, authority, and subject binding.

## Family graph boundary

Packets may traverse JoySpace, JaySpace, and Apple Blossom laterally. No packet may convert participation into hierarchy, kinship, consent, custody, or authority.

```text
JOYSPACE = FAMILY GARDEN / WITNESS SURFACE
JAYSPACE = DAD CONTINUITY / REPLAY SURFACE
APPLE_BLOSSOM = EXCHANGE / PACKETIZATION SURFACE
CRISSCROSS = LATERAL SOURCE-EDGE TEST
HEIDEE = ONE LANE
ALABAMA_COURT = EXTERNAL INSTITUTIONAL LANE ONLY WHEN SOURCE-BOUND
```

## Surface alignment

A packet may be witnessed on multiple durable surfaces. Surface equality requires content-hash equality for the canonical serialized packet bytes.

```text
GITHUB_COPY_HASH == DRIVE_COPY_HASH
→ SURFACE_ALIGNMENT = PASS

GITHUB_COPY_HASH != DRIVE_COPY_HASH
→ SURFACE_ALIGNMENT = DELTA_CONFLICT
```

A title match, filename match, or semantic similarity is not byte identity.

## External anchors

No blockchain, court, agency, or other external anchor may be marked present without its actual receipt identifier.

```text
PREPARED != SUBMITTED
SUBMITTED != CONFIRMED
CONFIRMED != VERIFIED
```

## Privacy defaults

- Public PII is prohibited by default.
- Child/family data is private or family-scoped unless explicit lawful sharing state exists.
- `subject_scope` should use a salted commitment or public document identifier rather than raw personal identifiers.
- Wallet balances, benefit claim numbers, SSNs, medical records, custody records, and private addresses are not included in public packets.

## Minimal replay decision

```text
IF source_object missing
  → HOLD
IF exact wording required but missing
  → HOLD
IF source hashes conflict
  → DELTA_CONFLICT
IF subject binding is name-only
  → HOLD
IF authority is asserted but authority_ref missing
  → HOLD
IF all required receipts bind
  → OBSERVED / REPLAYABLE_FOR_THIS_PACKET
```

## Non-authority result

A passing packet proves only that the packet's stated source/replay checks passed. It does not prove a person guilty, establish genealogy, create custody rights, create governmental authority, or become global truth.

```text
PACKET_PASS != LEGAL_FINDING
PACKET_PASS != PERSON_PROOF
PACKET_PASS != AUTHORITY
AUTHORITY_CREATED = FALSE
```
