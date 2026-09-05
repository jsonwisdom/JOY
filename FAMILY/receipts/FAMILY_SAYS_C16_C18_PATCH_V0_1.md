# FAMILY_SAYS C16–C18 PATCH V0.1

```text
STATUS: DELTA_RECORDED
STORY_BIND: HOLD
FACTS_PROMOTED: 0
AUTHORITY_CREATED: FALSE
USAF_ENDORSEMENT: FALSE
OPERATOR_BYTES_PRESENT_HERE: FALSE
```

## Why this exists

Peer operator independently hashed attached draft files and reported:

```text
MANUSCRIPT_BYTES   = 8647
MANUSCRIPT_SHA256  = 1c9f70ac896ef6f6960a50d7b3b7adec79a94dfd1bd602d140ac105eda22aa9f
LEDGERS_BYTES      = 4952
LEDGERS_SHA256     = 07b7704d52c5f322bbe020afc710148af00692f37055100429d0a88aadcb99d0
PREFIX_MATCH       = PASS
```

Those hashes are **peer-declared**. This operator does not hold the 8647-byte or 4952-byte objects, so those digests are not recomputed here and are not a bind digest.

## Required classification patch

Jason-supplied family facts stay FAMILY_SAYS. They are not USAF facts. They are not public-verified facts. They must not be marked UNKNOWN/GAP merely because they lack external proof.

### C16

```text
CLAIM  = LeeAnn drives by Maxwell every day
SOURCE = FAMILY_SAYS / JASON_SAYS
STATUS = PRESERVED_AS_DECLARED
PUBLIC_VERIFICATION = NOT_ESTABLISHED
```

### C17

```text
CLAIM  = MaryDee drives by Maxwell every day
SOURCE = FAMILY_SAYS / JASON_SAYS
STATUS = PRESERVED_AS_DECLARED
PUBLIC_VERIFICATION = NOT_ESTABLISHED
```

### C18

```text
CLAIM  = LeeAnn and MaryDee are sisters
SOURCE = FAMILY_SAYS / JASON_SAYS
STATUS = PRESERVED_AS_DECLARED
GENEALOGICAL_EXTERNAL_BIND = NOT_ESTABLISHED
```

### C19

Colonel IRL stays unpromoted unless a current official effective-rank record is bound. Boundary correct. No change.

## Gate

```text
CONTENT_REVIEW              = DELTA
REQUIRED_PATCH              = FAMILY_SAYS classification only
STORY_DIGEST                = NOT_PROMOTED_TO_BIND_DIGEST
REPLAY_RECEIPT              = NOT_CREATED
STORY_BIND                  = HOLD
```

Regenerate manuscript + ledgers from the exact prior bytes after applying only this classification patch. The next SHA-256 of those patched bytes is the candidate bind digest. Do not bind the 1c9f70ac… draft.
