# JOYSPACE Badge Award Record V0.1

Status: ACTIVE
Authority: false
Family Barrier: INTACT
Layer: Celebration Receipt
Depends On:
- badges/badge_manifest.json
- badges/proof/proof_model_v0_1.md
- badges/proof/witness_model_v0_1.md

## Purpose

The Badge Award Record defines how JOYSPACE records that a badge was earned and celebrated.

It is a receipt of participation, not a certificate of human worth.

It closes the badge flow gently:

```text
Badge -> Criteria -> Proof -> Witness -> Award Record -> Celebration
```

## Doctrine

- Badges invite.
- Evidence exists.
- Witnesses confirm existence.
- Award records preserve participation.
- Celebration follows.
- No badge grants authority.
- No badge creates rank.
- No badge measures human worth.
- Authority remains false.

## Award Record Object V0.1

```json
{
  "artifact": "JOYSPACE_BADGE_AWARD_RECORD_V0_1",
  "award_id": "<uuid>",
  "badge_id": "<badge_id>",
  "recipient": "<username_or_private_label>",
  "awarded_at": "<iso8601>",
  "proof_id": "<proof_id>",
  "witness": {
    "witness_type": "self | friend | mentor | family | teacher | guide | community",
    "confirmed": true,
    "quality_scored": false,
    "ranked": false,
    "authority": false
  },
  "celebration_note": "<short human note>",
  "privacy": "private | family-only | shareable",
  "authority": false
}
```

## Required Checks

Before an award record is created:

- badge_id exists in badge_manifest.json
- proof_id exists or is recorded with the award
- witness confirmation, if present, confirms existence only
- privacy is explicitly set
- authority is false
- no ranking or grading fields are present

## Celebration Rules

Celebration may include:

- a kind note
- a badge image
- a small ceremony
- a README update
- a private journal entry
- a family-only record
- a shareable gallery entry

Celebration may not include:

- ranking
- comparison
- public pressure
- forced disclosure
- authority claims
- permanent status claims

## Privacy Rules

Private awards are valid.

Family-only awards are valid.

Shareable awards require consent.

No award record must be public to count.

## Alignment With Lineage

Award records should reference the badge lineage arc when helpful, but must not imply hierarchy.

Examples:

```text
Seed Planter begins the Self-Creation Path.
Future Protector anchors the Safety & Care Path.
```

These are meanings, not ranks.

## Lock Line

```text
A badge award records participation.
Celebration stays gentle.
Privacy stays chosen.
No rank is created.
Authority remains false.
```
