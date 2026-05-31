# JOYSPACE Proof Model V0.1

Status: ACTIVE
Authority: false
Family Barrier: INTACT
Layer: Proof Substrate

## Purpose

The Proof Model defines how evidence is represented in JOYSPACE.

It ensures consistency without creating authority.

It enables validation without judgment.

## Doctrine

- Badges invite.
- Evidence exists.
- Witnesses confirm existence.
- Authority remains false.
- No scoring, ranking, or grading.
- No quality metrics.
- No comparative evaluation.

## Accepted Proof Types

- reflection
- screenshot
- drawing
- commit
- trusted_witness
- photo
- journal_entry

These types are descriptive, not restrictive.

Any future proof type must preserve the doctrine.

## Verification Model

```yaml
exists: true
quality_scored: false
ranked: false
graded: false
```

Existence is the only requirement.

Interpretation belongs to the badge earner, not the system.

## Proof Object Structure V0.1

A proof object must contain:

```json
{
  "proof_id": "<uuid>",
  "badge_id": "<badge_id>",
  "type": "<proof_type>",
  "submitted_by": "<username>",
  "timestamp": "<iso8601>",
  "content": "<human-readable description or link>",
  "witness": {
    "name": "<optional>",
    "statement": "<optional>",
    "confirmed": "<true|false>"
  },
  "authority": false
}
```

## Notes

- `content` may be a description, link, or embedded text.
- `witness` is optional for most badges.
- Witnesses confirm existence, not quality.
- No field may imply authority, ranking, grading, or human worth.

## Proof Lifecycle

### 1. Invitation

Criteria invite the user to create evidence.

### 2. Creation

The user generates a proof object.

### 3. Witness Optional

A trusted witness may confirm existence.

### 4. Validation

Validation checks structure, not worth.

### 5. Celebration

The badge is awarded.

This lifecycle is intentionally gentle.

It mirrors growth, not judgment.

## Alignment With Lineage

- Self-Creation Path badges emphasize reflection, commits, drawings, and journals.
- Safety & Care Path badges emphasize checklists, screenshots, and witness confirmations.
- All badges accept all proof types.
- No badge may require a proof type that risks privacy or safety.

## Safety Notes

- No personal data required.
- No sensitive screenshots.
- No identifiable minors.
- No pressure to share publicly.
- Private proofs are valid.

## Lock Line

```text
Badges invite.
Evidence exists.
Witnesses confirm existence.
Celebration follows.
Authority remains false.
```
