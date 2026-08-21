# FamilyReverseRePlay — Restore MrsWisdom / HonestJSONWisdom / Shared Merkle Root v0.1

**Local date:** 2026-08-20 (America/Chicago)  
**State:** DRAFT_RESTORE / REVIEW_REQUIRED  
**AUTHORITY_CREATED:** `FALSE`

## Restore Target

```text
MrsWisdom
  ↓
Family continuity / safety guardian
  ↓
HonestJSONWisdom
  ↓
Receipt ≠ Story ≠ Unknown
  ↓
Shared Family Merkle Boundary
```

## Identity Restore

`MRS_WISDOM` and `MS_WISDOM` are treated as name/role variants of one continuity identity in this restore rail, not as two separately inferred people.

The older registry statement `MRS_WISDOM != MS_WISDOM` is retained as a conflict receipt and is not silently deleted.

```json
{
  "canonical_role": "MRS_WISDOM",
  "variants": ["MRS_WISDOM", "MS_WISDOM"],
  "separate_identity_inference": false,
  "registry_conflict_present": true,
  "conflict_action": "HOLD_FOR_REPLAY"
}
```

## MrsWisdom Boundary

```json
{
  "role": "family_continuity_guardian",
  "people_are_assets": false,
  "receipts_own_people": false,
  "consent_over_convenience": true,
  "safety_over_work": true,
  "surveillance": false,
  "automatic_tracking": false,
  "private_stays_private": true,
  "pause_available": true,
  "authority_created": false
}
```

Existing approval gates remain gates. A committed file, pushed branch, index, hash, or root does not equal MrsWisdom consent.

## HonestJSONWisdom

```text
OBSERVED  = may be receipted
STORY     = may be preserved as story
UNKNOWN   = remains UNKNOWN
PRIVATE   = remains PRIVATE
INFERENCE = never silently promoted
REPLAY    = may preserve memory; may not create power
```

```json
{
  "organize": "!= control",
  "remember": "!= surveil",
  "replay": "!= rewrite",
  "hash": "!= ownership",
  "merkle_membership": "!= genealogy",
  "receipt": "!= consent",
  "authority_created": false
}
```

## Shared Merkle Root Posture

The shared root is a verification boundary for family-approved artifacts and continuity receipts. It is not a person, owner, genealogy oracle, consent token, or authority source.

```json
{
  "merkle_scope": "FAMILY_SHARED_CONTINUITY",
  "stewardship": "SHARED",
  "personal_ownership": false,
  "root_value": "UNKNOWN",
  "root_computed_and_verified": false,
  "root_promotion": "HOLD",
  "proves_artifact_membership_only_when_proof_valid": true,
  "proves_genealogy": false,
  "proves_identity": false,
  "proves_consent": false,
  "creates_authority": false
}
```

## Reverse Replay

```text
FAMILY MEMORY
    ↓
MRSWISDOM BOUNDARY
    ↓
QUESTION / STORY / RECEIPT / UNKNOWN
    ↓
HONESTJSONWISDOM
    ↓
APPROVED ARTIFACT BYTES
    ↓
HASHES
    ↓
MERKLE TREE
    ↓
SHARED ROOT CANDIDATE
    ↓
VERIFY
    ↓
HUMAN REVIEW
    ↓
PROMOTE | HOLD | REJECT
```

## Non-Negotiable Restore Rules

- No identity split by capitalization/title alone.
- No inferred family relationship becomes fact.
- No Merkle root is claimed until a replayable computation receipt exists.
- Shared means shared stewardship of the verification boundary, not control over a family member.
- Existing private material does not become a public leaf.
- PAUSE is always available.
- `AUTHORITY_CREATED = FALSE` throughout.

## Current Ruling

```text
MRS_WISDOM_VARIANT_RESTORE = ACTIVE_DRAFT
HONESTJSONWISDOM = ACTIVE
SHARED_MERKLE_SEMANTICS = RESTORED
NUMERIC_MERKLE_ROOT = UNKNOWN
ROOT_PROMOTION = HOLD
REGISTRY_CONFLICT = EXPLICIT
PUBLIC_AUTHORITY = FALSE
```
