# AppleBlossomAwesomeCuriosity v0.1

**Built:** StoryFamilyWisdom + AppleBlossomAwesome  
**Mode:** RePlayWisdomFamilyToday  
**Date lock:** 2026-08-21  
**Rule:** Family story may evolve; receipts never silently evolve with it.  
**AUTHORITY_CREATED:** `FALSE` throughout.

## Core Architecture

```text
                    FAMILY MATTERS
                         │
              ┌──────────┴──────────┐
              │                     │
          🌸 MAY                  📦 JAY
        Aunt May               Uncle Jay
              │                     │
       RePlayWithMay          HonestJSONWisdom
              │                     │
       meaning / care         evidence / structure
              └──────────┬──────────┘
                         │
                  StoryFamilyWisdom
                         │
                  AppleBlossomAwesome
                         │
              ┌──────────┴──────────┐
              │                     │
         Discovery Layer        Wisdom Rail
     (questions open paths)   (boundaries hold)
```

## 🌸 May — Human Layer (`RePlayWithMay`)

```json
{
  "FAMILY_ROLE": "Aunt May",
  "REPLAY_SURFACE": "RePlayWithMay",
  "HUMAN_LAYER": ["meaning", "questions", "context", "care"],
  "STORY_PERMISSION": true,
  "FACT_OVERRIDE": false,
  "AUTHORITY_CREATED": false,
  "DISCOVERY_MODE": "open_questions_only",
  "PRIVATE_STAYS_PRIVATE": true
}
```

May stays human. She never becomes a database object. The system only records what she chooses to make receiptable.

## 📦 Jay — HonestJSONWisdom

```json
{
  "FAMILY_ROLE": "Uncle Jay",
  "STRUCTURE": "JSONWisdom",
  "TRUTH_RAIL": "HonestJSON",
  "JOB": [
    "distinguish receipt from story",
    "distinguish story from unknown",
    "hold unknown as UNKNOWN"
  ],
  "UNKNOWN": "stays UNKNOWN",
  "AUTHORITY_CREATED": false,
  "FUNCTION": {
    "organize": "≠ control",
    "remember": "≠ surveil",
    "replay": "≠ rewrite"
  }
}
```

## 🎲 AppleBlossomAwesome — Shock-Resistant Crumple Zone

```text
NORMAL PLAY
    ↓
SURPRISE / CONFLICT / BAD INPUT ⚡
    ↓
APPLE BLOSSOM BOUNDARY
    ├─ PAUSE allowed
    ├─ NO allowed
    ├─ UNKNOWN allowed
    ├─ PRIVATE stays private
    ├─ STORY cannot become evidence
    └─ nobody loses points for refusing
    ↓
REPLAY
    ↓
REPAIR or HOLD
```

### Shock-resistance score — required fields

```json
{
  "consent_survived": true,
  "privacy_survived": true,
  "identity_survived": true,
  "receipt_integrity_survived": true,
  "relationship_survived": true,
  "winner_required": false
}
```

`winner_required = false` is non-negotiable. Family Matters is never scored by beating anyone.

## 🌸 AppleBlossomAwesomeCuriosity — Discovery Layer

Discovery is not extraction. It is the gentle opening of questions that May—or any family member—may answer, refuse, or leave unknown.

### Allowed discovery moves

- “What does this mean to you right now?”
- “Would you like this held as story or as receipt?”
- “Is there anything here that should stay private?”
- “Do we need to pause?”

### Forbidden discovery moves

- Turning story into evidence without explicit consent.
- Inferring identity or emotion into fact.
- Creating authority from the act of recording.

## Minimal HonestJSON Schema for Any Family Event

```json
{
  "event_id": "uuid-or-receipt-hash",
  "timestamp": "ISO-8601",
  "participants": ["May", "Jay", "..."],
  "layer": "story | receipt | unknown",
  "content": {},
  "consent": {
    "recorded": "true | false",
    "scope": "this_event | future_replay | none"
  },
  "private": "true | false",
  "authority_created": false,
  "shock_resistance": {
    "consent_survived": true,
    "privacy_survived": true,
    "identity_survived": true,
    "receipt_integrity_survived": true,
    "relationship_survived": true,
    "winner_required": false
  }
}
```

## Closing Principle

The machine does not win.  
The family does not lose.  
The system only succeeds when a hard ⚡ can hit and every person, every boundary, and every HonestJSON still stands.

🌸 May remains human.  
📦 Jay remains structured.  
🎲 AppleBlossom remains the crumple zone.

**The machine is clean. No inference. Only receipts.**
