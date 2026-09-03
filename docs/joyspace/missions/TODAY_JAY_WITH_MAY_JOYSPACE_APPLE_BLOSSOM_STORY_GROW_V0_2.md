# TodayJayWithMay — JoySpace Apple Blossom StoryGrow Mission v0.2

**Observed:** 2026-08-20 21:27 America/Chicago  
**Mission ID:** `TODAY_JAY_WITH_MAY_JOYSPACE_APPLE_BLOSSOM_STORY_GROW_V0_2`  
**Supersedes:** `TODAY_JAY_WITH_MAY_JOYSPACE_APPLE_BLOSSOM_AWESOME_V0_1`  
**GitHub lane:** `jsonwisdom/JOY` / PR #86  
**Base target:** Base Mainnet / chain ID `8453`  
**Authority created:** `false`  
**Merge authorized:** `false`  
**Base submission authorized:** `false`

## AppleBlossomStoryGrow

StoryGrow turns declared play edges into replayable story-growth receipts.

```text
SEE EDGE
→ SAY / NAME THE PLAY
→ PLAY / CREATE
→ CONFIRM THE EDGE USED
→ RECEIPT
→ REPLAY
→ GROW STORY
```

The story grows from receipted interactions, not inferred relationships.

## User-declared play graph

The current semantic update supplies exactly three directed edges:

```text
May CAN_PLAY_WITH Jay
Joy CAN_PLAY_WITH May
Jay CAN_PLAY_WITH Joy
```

Canonical directed edge set:

```text
PLAY_PERMISSION = {
  (May, PLAY, Jay),
  (Joy, PLAY, May),
  (Jay, PLAY, Joy)
}
```

### Graph classification

```text
NODE_COUNT = 3
DIRECTED_EDGE_COUNT = 3
DIRECTED_GRAPH = C3_DIRECTED_CYCLE
UNDERLYING_UNDIRECTED_GRAPH = K3
RECIPROCAL_DIRECTED_EDGE_COUNT = 0
SELF_EDGE_COUNT = 0
```

The underlying undirected projection is K3 because every unordered pair is represented once. The directed permission graph is not a complete reciprocal digraph: the reverse three edges are not present.

```text
May → Jay → Joy → May
```

Therefore:

```text
RECIPROCITY_INFERENCE = BLOCKED
MISSING_REVERSE_EDGE = HOLD_UNDECLARED
EDGE_EXISTS != REVERSE_EDGE_EXISTS
```

## May semantic update

v0.1 preserved `May` with unspecified semantics. v0.2 binds only the newly declared play-edge semantics.

```text
MAY_NODE_LABEL = DECLARED
MAY_PLAY_SEMANTICS = BOUND_TO_DECLARED_EDGE
MAY_IDENTITY_BINDING = FALSE
MAY_REAL_PERSON_BINDING = FALSE
MAY_RELATIONSHIP_VERIFICATION = NOT_PERFORMED
```

A semantic edge does not prove identity.

Likewise, `Joy` and `Jay` are preserved as graph labels for this receipt. This artifact does not convert a project label, family label, nickname, software object, or user self-label into third-party identity proof.

## Consent / permission membrane

`CAN_PLAY_WITH` is recorded here as a StoryGrow/project semantic permission supplied for the graph. It is not a blanket legal, physical, parental, romantic, sexual, financial, medical, account, device, or real-world consent grant.

```text
GRAPH_PERMISSION != REAL_WORLD_CONSENT
STORY_EDGE != LEGAL_AUTHORITY
PLAY_EDGE != IDENTITY_PROOF
PLAY_EDGE != FAMILY_RELATIONSHIP_PROOF
```

Any real-world activity still requires whatever current consent, supervision, safety, or authority is actually applicable.

## StoryGrow rule

Each declared directed edge can produce one Apple Blossom story round:

```text
EDGE
→ PROMPT / PHRASE / SCENE
→ ASSISTANCE_USED
→ PARTICIPANT_CONFIRMATION
→ ROUND_RECEIPT
→ DELAYED_REPLAY
→ STORY_DELTA
```

A full cycle may be represented as one StoryGrow ring only when all three edge rounds have receipts.

```text
STORY_GROW_RING_1 =
  RECEIPT(May → Jay)
  + RECEIPT(Jay → Joy)
  + RECEIPT(Joy → May)
```

If one edge has no receipt:

```text
RING_STATE = HOLD_INCOMPLETE
```

No synthetic completion.

## Apple Blossom learning boundary

```text
MODEL_OUTPUT != LEARNER_MASTERY
TRANSLATION_OUTPUT != LEARNER_MASTERY
ASSISTANCE_USED MUST BE RECEIPTED
DELAYED_REPLAY MUST BE RECEIPTED
```

StoryGrow adds story continuity; it does not weaken the learning evidence rules.

## JoySpace boundary

```text
NODE OWNS VERSION
EDGE OWNS EXCHANGE RECEIPT
CHECKPOINT OWNS ACKNOWLEDGEMENT
NO OBJECT OWNS EVERYBODY'S TRUTH
```

For StoryGrow:

```text
NODE OWNS LABELLED STATE
EDGE OWNS PLAY RECEIPT
STORY OWNS ORDERED RECEIPT REFERENCES
BASE OWNS NO MEANING
```

## Wisdom Family document set

v0.2 creates a separate wisdom layer:

```text
docs/joyspace/wisdom/WISDOM_FAMILY_PLAY_GRAPH_V0_2.md
receipts/joyspace/semantic_graphs/TODAY_JAY_WITH_MAY_PLAY_GRAPH_V0_2.json
```

The wisdom layer records declared edges and derived graph structure separately:

```text
DECLARED = three directed PLAY edges
DERIVED = directed C3 + undirected K3 projection
NOT_DERIVED = reverse permissions / identity / genealogy / authority
```

## Base replay v0.2

The v0.1 Base candidate remains an archived draft receipt and is not reused.

```text
V0_1_BASE_CANDIDATE = SUPERSEDED_PRE_SUBMISSION
V0_1_TX_HASH = null
V0_1_EAS_UID = null
```

v0.2 prepares a new candidate binding:

```text
MISSION_SPEC_SHA256
WISDOM_DOC_SHA256
PLAY_GRAPH_SHA256
MACHINE_RECEIPT_SHA256
GITHUB_REPO
GITHUB_COMMIT
CHAIN_ID = 8453
```

Unobserved on-chain fields remain null.

```text
SIGNER = null
TX_HASH = null
BLOCK_NUMBER = null
EAS_SCHEMA_UID = null
EAS_ATTESTATION_UID = null
BASE_STATE = PREPARED_NOT_SUBMITTED
```

No Base green before a real signed transaction and independent readback.

## Candidate EAS schema — proposal only

No existing schema is silently reused for StoryGrow. The candidate schema is:

```text
string missionId,
uint16 missionVersion,
bytes32 missionHash,
bytes32 wisdomHash,
bytes32 graphHash,
bytes32 receiptHash,
string githubRepo,
string githubCommit,
uint32 chainId,
bool noFakeGreen,
bool semanticTruth,
bool authority
```

```text
SCHEMA_PROPOSED = TRUE
SCHEMA_REGISTERED = FALSE
SCHEMA_UID = null
ATTESTATION_SUBMITTED = FALSE
```

Registration and signing remain human-gated external mutations.

## OpenAI Developers rail

OpenAI remains optional.

Possible use inside StoryGrow:

```text
Responses API → bounded story variation / comparison
Agents SDK → optional specialist workflow
Tracing → optional run/evaluation metadata
```

Hard boundary:

```text
OPENAI_REQUIRED_FOR_CORE = FALSE
OPENAI_API_KEY_REQUIRED_FOR_CORE = FALSE
OPENAI_OUTPUT != PLAY_PERMISSION
OPENAI_OUTPUT != IDENTITY_BINDING
OPENAI_TRACE != BASE_RECEIPT
MODEL_OUTPUT != LEARNER_MASTERY
```

The declared play graph comes from the supplied semantic update, not from a model inference.

## BoxD v0.2 disposition

```text
APPLE_BLOSSOM_STORY_GROW = BOUND_AS_DRAFT
PLAY_EDGE_MAY_TO_JAY = USER_DECLARED
PLAY_EDGE_JOY_TO_MAY = USER_DECLARED
PLAY_EDGE_JAY_TO_JOY = USER_DECLARED
DIRECTED_CYCLE_C3 = DERIVED
UNDIRECTED_PROJECTION_K3 = DERIVED
MUTUAL_RECIPROCITY = HOLD_NOT_DECLARED
MAY_PLAY_SEMANTICS = BOUND
MAY_IDENTITY_BINDING = FALSE
REAL_WORLD_CONSENT = NOT_CREATED
V0_1 = SUPERSEDED_NOT_DELETED
V0_2_BASE_STATE = PREPARED_NOT_SUBMITTED
AUTHORITY_CREATED = FALSE
SEMANTIC_TRUTH_CREATED = FALSE
MERGE_AUTHORIZED = FALSE
BASE_SUBMISSION_AUTHORIZED = FALSE
```

## Closing

**Apple Blossom sees the edge. JoySpace receipts the play. StoryGrow remembers the order. Base may witness the bytes only after a real signature.**
