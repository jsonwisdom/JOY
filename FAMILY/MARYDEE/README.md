# MARYDEE

**Role:** external co-parent/reviewer lane  
**Authority:** false

MARYDEE is a protected family review surface inside JOY.

Its purpose is to receive an explicitly submitted payload, inspect what was actually sent, identify missing evidence or unsafe material, and return recommendations to a human decision point.

```text
INPUT  = exact payload / manifest / hashes / changed-file list
OUTPUT = PASS_FOR_HUMAN_REVIEW | DELTA | HOLD
WRITE_AUTHORITY = false
CONSENT_INFERRED = false
```

## Grok Review Prompt

Use:

`FAMILY/MARYDEE/GROK_REVIEW_PROMPT_V0_1.md`

The prompt is designed for a user-operated external model such as a Grok Mary D bot. Model output remains advisory.

## Family Flow

```text
MR_WISDOM
   ↓ payload + purpose + timestamp
HEIDEE / JOYSPACE
   ↓ optional human-directed observer review
MRS_WISDOM
   ↓
HUMAN DECISION POINT

MR_WISDOM / HUMAN OPERATOR
   ↓ exact review package
MARYDEE EXTERNAL REVIEW
   ↓ recommendation
HUMAN DECISION POINT
```

No family role is converted into technical authority by this directory.
