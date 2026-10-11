# Wisdom Family Play Graph v0.2

**Observed:** 2026-08-20 21:27 America/Chicago  
**Source:** user-declared semantic update for `TodayJayWithMay`  
**Authority created:** `false`

## Declared edges

```text
May CAN_PLAY_WITH Jay
Joy CAN_PLAY_WITH May
Jay CAN_PLAY_WITH Joy
```

These three edges are stored exactly as directed permissions in the StoryGrow graph.

## Graph

```text
May ─PLAY→ Jay ─PLAY→ Joy ─PLAY→ May
```

Machine set:

```text
E = {
  (May, PLAY, Jay),
  (Joy, PLAY, May),
  (Jay, PLAY, Joy)
}
```

## What may be derived

```text
NODES = {Jay, Joy, May}
NODE_COUNT = 3
DIRECTED_EDGE_COUNT = 3
DIRECTED_GRAPH = C3_DIRECTED_CYCLE
UNDERLYING_UNDIRECTED_GRAPH = K3
```

The undirected projection is K3 because each unordered pair has one directed edge between its members.

## What may NOT be derived

```text
Jay CAN_PLAY_WITH May      = HOLD_UNDECLARED
May CAN_PLAY_WITH Joy      = HOLD_UNDECLARED
Joy CAN_PLAY_WITH Jay      = HOLD_UNDECLARED
```

Therefore:

```text
MUTUAL_RECIPROCITY = HOLD
RECIPROCITY_INFERENCE = BLOCKED
DIRECTED_EDGE != BIDIRECTIONAL_EDGE
```

## Node/identity boundary

The graph establishes labeled semantic nodes and relations for this project receipt. It does not establish third-party identity.

```text
MAY_NODE_LABEL = DECLARED
MAY_PLAY_SEMANTICS = BOUND
MAY_IDENTITY_BINDING = FALSE
JOY_NODE_LABEL = DECLARED
JAY_NODE_LABEL = USER_SUPPLIED
PLAY_EDGE != IDENTITY_PROOF
```

## Consent boundary

This graph is a StoryGrow/project semantic graph. It does not create blanket real-world consent or authority.

```text
GRAPH_PERMISSION != REAL_WORLD_CONSENT
GRAPH_PERMISSION != LEGAL_PERMISSION
GRAPH_PERMISSION != PARENTAL_AUTHORITY
GRAPH_PERMISSION != ACCOUNT_PERMISSION
```

## AppleBlossomStoryGrow use

Each directed edge may seed one story-learning round. A story ring closes only from receipts:

```text
May → Jay receipt
+ Jay → Joy receipt
+ Joy → May receipt
= STORY_GROW_RING_1_COMPLETE
```

Without all three receipts:

```text
STORY_GROW_RING_1 = HOLD_INCOMPLETE
```

## Wisdom rule

**Edges may grow stories. Receipts may grow confidence. Neither may silently grow identity, reciprocity, consent, or authority.**
