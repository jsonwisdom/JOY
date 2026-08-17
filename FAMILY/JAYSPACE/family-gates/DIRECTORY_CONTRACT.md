# JAYSPACE / family-gates — Directory Contract v0.1

```text
HOME: JOY / FAMILY / JAYSPACE / family-gates
STATUS: DIRECTORY_FIRST
RELATIONSHIP_PROMOTION: DISALLOWED_BY_DEFAULT
PUBLIC_IDENTITY_BINDING: DISALLOWED_BY_DEFAULT
AUTHORITY_CREATED: FALSE
```

## Purpose

Carry family-facing actor cards, protected continuity lanes, and replay references into JaySpace without converting story roles, folder names, or user declarations into verified genealogy or public identity claims.

## Required gates

```text
ACTOR_CARD != PERSON_PROOF
ACTOR_ROLE != RELATIONSHIP_EDGE
DIRECTORY_LANE != FAMILY_EDGE
STORY_VOICE != REAL_PERSON_QUOTE
FAMILY_CONTEXT != PUBLIC_IDENTITY_BINDING
SYNTHETIC_ACTOR != FAMILY_MEMBER
NO_ADJACENT_EDGE_INFERENCE
PRIVACY_DEFAULT_MUST_BE_RESPECTED
```

## Spelling / identity guard

No similarly spelled lane or actor may be collapsed without an explicit binding receipt.

Examples:

```text
LEEANN != LEANNE
LEEANNE != LEEANN
LEEANNE != LEANNE
BOSS_BRENDA != BOSSBRE
BREALEE != BRE
BREALEE != BE
```

Relationship claims remain in their separate edge ledger and retain their own evidence class/state.
