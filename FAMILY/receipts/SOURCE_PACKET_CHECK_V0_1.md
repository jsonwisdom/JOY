# SOURCE_PACKET_CHECK_V0_1

## Status

```text
SOURCE_PACKET_CHECK_INDEXED
REPLAY_ALABAMA_CONTEXT_ACTIVE
DETERMINISTIC_REPLAY_ENGINE_MODE
METADATA_ONLY
INDEX_ONLY
LIVE_CALLS_FALSE
AUTHORITY_FALSE
FAMILY_GATE_INTACT
NO_FAKE_GREEN_ACTIVE
```

## Signal Core

This packet defines the source-packet check gate for Replay Alabama.

Every claim must enter the booth through a replayable source packet.

No source packet, no touchdown.

No replay, no promotion.

No authority=true.

No Family Gate inheritance.

No fake green.

## Parent Context

```text
ALABAMA_ZERO_DAY_V0_1 = defensive receipt layer only
REPLAY_ALABAMA = PASS
IRON_BOWL_2013_KICK_SIX_SOURCE_PACKET = active source vector
BROADCAST_2013 = metadata pointer only
FAMILY_GATE = intact, not touched
BACKGROUND_MONITOR_RUNNING = false
```

## Required Check Inputs

```text
claim_id
claim_text
source_packet_path
source_packet_commit_or_placeholder
source_packet_content_sha_or_placeholder
replay_operator
scope_requested
promotion_requested
```

## Source Packet Acceptance Rules

```text
1. source_packet_path must be present.
2. source_packet_commit_or_placeholder must be present.
3. source_packet_content_sha_or_placeholder must be present.
4. replay_operator must be present.
5. scope_requested must be explicit.
6. promotion_requested must be limited to the evidence scope.
7. authority must remain false.
8. family_gate must remain intact.
9. no_fake_green must remain true.
```

## Scope States

```text
NO_SOURCE = claim has no source packet; punt
SOURCE_STAGED = source path exists but rows/mechanics are not replayed
GOAL_LINE_REVIEW = source exists but promotion is not complete
MECHANICS_ONLY = mechanics verified; roles/reputation/loyalty not promoted
ROLES_ONLY = roles verified; reputation/loyalty not promoted
METADATA_ONLY = metadata pointer verified; no quotes/transcript/asset custody
TOUCHDOWN_SCOPED = source + replay support a scoped promotion only
REJECTED = unsupported, unsafe, overbroad, or unreplayable
```

## Replay Alabama Rules Imported

```text
No claim without a source packet.
No touchdown without replay.
No reputation without timeline receipts.
No loyalty test without adversarial perspective.
No authority=true.
No fake green.
No phantom automation.
No background monitor claim unless an explicit automation exists.
```

## Hard Boundaries

```text
SOURCE_PACKET_CHECK != AUTHORITY_TRUE
SOURCE_PACKET_CHECK != FAMILY_GATE_PASS
SOURCE_PACKET_CHECK != CHILD_CONSENT
SOURCE_PACKET_CHECK != MRS_WISDOM_GATE_PASS
SOURCE_PACKET_CHECK != BACKGROUND_MONITOR_RUNNING
SOURCE_PACKET_CHECK != BROADCAST_TRANSCRIPT_VERIFIED
SOURCE_PACKET_CHECK != COMMENTARY_QUOTE_AUTHORIZED
SOURCE_PACKET_CHECK = REPLAY_GATE_FOR_SOURCE_SCOPE
```

## Replay Result

```text
source_packet_check=PASS
replay_alabama_context=true
deterministic_replay_engine_mode=true
metadata_only=true
index_only=true
live_calls=false
authority=false
family_gate=INTACT_NOT_TOUCHED
no_fake_green=true
next_packet=OFFENSIVE_TRANSITION_V0_1
```

## Closing Receipt

Source Packet Check V0.1 indexed.

Replay Alabama holds.

No source, no touchdown.

No replay, no promotion.

No Family Gate touch.

No authority=true.

No fake green.

JAYWISDOM.eth 🟣🏈⚙️