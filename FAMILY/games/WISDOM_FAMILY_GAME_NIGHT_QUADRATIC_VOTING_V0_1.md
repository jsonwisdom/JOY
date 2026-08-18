# Wisdom Family Game Night v0.1
## Quadratic Voting Edition — Quantum-Driven Rubric

## Status

```text
ARTIFACT_ID          = JOY-FAMILY-QV-001
STATUS               = FAMILY_GAME_DRAFT
EXECUTION_AUTHORITY  = FALSE
LEGAL_AUTHORITY      = FALSE
FINANCIAL_AUTHORITY  = FALSE
PROMOTION_ALLOWED    = FALSE
REPLAY_REQUIRED      = TRUE
QUANTUM_COMPUTING    = NOT_REQUIRED
QUANTUM_DRIVEN       = RUBRIC_AND_STATE_MODEL_ONLY
```

## Family rule

```text
FAMILY FIRST, EVERY TIME.
THE PERSON COMES BEFORE THE SCORE.
JOY WELCOMES.
LOGIC COUNTS.
REPLAY SETTLES DISPUTES.
NO RESULT OVERRIDES CONSENT.
```

## Purpose

This game gives the Wisdom family a repeatable way to make low-stakes group choices while teaching:

- quadratic cost;
- budget discipline;
- private preference intensity;
- public tally verification;
- replay receipts;
- consent boundaries;
- disagreement without accusation;
- the difference between arithmetic proof and decision authority.

Example decisions:

- movie choice;
- dinner choice;
- family activity;
- weekend project;
- music playlist;
- creative challenge;
- family archive task;
- charitable activity.

The game MUST NOT be used by itself for legal, medical, financial, custody, employment, disciplinary, or emergency decisions.

## Players

Recommended:

```text
MIN_PLAYERS = 3
MAX_PLAYERS = 8
```

Suggested family roles:

- Host — explains the round;
- Keeper — records frozen options and budgets;
- Verifier — checks arithmetic;
- Joy Witness — confirms everyone understood the choices;
- Players — allocate votes privately;
- Replay Reader — reconstructs the round after tally.

No role creates permanent authority.

## Core game model

Each player receives a budget of voice credits.

Default budget:

```text
BUDGET_PER_PLAYER = 25
```

Each vote allocation has quadratic cost:

```text
cost = votes^2
```

Examples:

| Votes on one option | Cost |
|---:|---:|
| 0 | 0 |
| 1 | 1 |
| 2 | 4 |
| 3 | 9 |
| 4 | 16 |
| 5 | 25 |

A player may split the budget across options.

Example:

```text
Option A = 3 votes → cost 9
Option B = 2 votes → cost 4
Option C = 3 votes → cost 9
Total cost = 22
Budget remaining = 3
```

## Why quadratic voting

Linear voting asks only which option a person prefers.

Quadratic voting also measures how strongly they prefer it while making concentrated influence increasingly expensive.

```text
ONE MORE VOTE COSTS MORE THAN THE LAST.
STRONG FEELINGS ARE ALLOWED.
DOMINATION IS EXPENSIVE.
```

## Quantum-driven rubric

“Quantum-driven” in this game means the family evaluates several possible states before collapsing to one accepted result.

It does not claim quantum hardware or quantum encryption.

### State model

```text
SUPERPOSITION = all valid family options remain possible
AMPLITUDE     = preference strength represented by vote allocation
INTERFERENCE  = competing preferences change the collective result
MEASUREMENT   = verified tally
COLLAPSE      = family accepts one game outcome
REPLAY        = round can be reconstructed from frozen inputs and receipts
```

### Rubric dimensions

Each option is evaluated across five dimensions:

| Dimension | Question | Score range |
|---|---|---:|
| JOY | Will this make the family feel connected? | 0–5 |
| LOVE | Does this respect each person? | 0–5 |
| LOGIC | Is it practical and understandable? | 0–5 |
| WISDOM | Does it support a good long-term pattern? | 0–5 |
| SAFETY | Is it appropriate and low risk? | 0–5 |

Rubric score:

```text
R[o] = JOY + LOVE + LOGIC + WISDOM + SAFETY
```

Maximum rubric score:

```text
MAX_RUBRIC_SCORE = 25
```

## Combined result

The family may use one of two modes.

### Mode A — Pure quadratic vote

```text
FINAL_SCORE[o] = TALLY[o]
```

### Mode B — Quantum-driven rubric

Default normalized form:

```text
FINAL_SCORE[o] = 0.70 * NORMALIZED_TALLY[o]
               + 0.30 * NORMALIZED_RUBRIC[o]
```

The weighting MUST be frozen before voting begins.

Recommended permitted weights:

```text
70/30
60/40
50/50
```

Weights MUST NOT be changed after private votes are submitted.

## Round procedure

### Step 1 — Freeze the question

Example:

```text
QUESTION = What should Wisdom Family Game Night do Saturday?
```

### Step 2 — Freeze the options

Example:

```text
A = movie and pizza
B = board-game tournament
C = family archive night
D = outdoor activity
```

### Step 3 — Confirm boundaries

Every player must understand:

- participation is voluntary;
- abstention is allowed;
- votes are private unless the player chooses otherwise;
- the result is advisory unless everyone agreed otherwise before the round;
- no one must justify a private vote.

### Step 4 — Freeze parameters

```json
{
  "game_id": "JOY-FAMILY-QV-001-R001",
  "budget_per_player": 25,
  "vote_range": "0_TO_5",
  "mode": "QUANTUM_RUBRIC",
  "tally_weight": 0.70,
  "rubric_weight": 0.30,
  "tie_rule": "REPLAY_THEN_RUNOFF",
  "rules_version": "0.1.0"
}
```

### Step 5 — Private allocation

Each player allocates votes while satisfying:

```text
sum(vote[o]^2) <= budget
```

### Step 6 — Arithmetic verification

The Keeper or verifier checks:

- each vote is within range;
- each quadratic cost is correct;
- no budget is exceeded;
- each ballot is counted once;
- the tally matches accepted ballots.

Privacy-preserving cryptographic proofs are optional future work. Paper ballots and transparent arithmetic are sufficient for Game Night v0.1.

### Step 7 — Rubric scoring

Each player or the family as a group scores each option across the five rubric dimensions.

The selected scoring method must be frozen before use:

```text
INDIVIDUAL_AVERAGE
GROUP_CONSENSUS
ROTATING_JUDGE
```

### Step 8 — Calculate result

The verifier computes the combined score using the frozen mode and weights.

### Step 9 — Family consent gate

Before accepting the result:

```text
DID EVERYONE UNDERSTAND THE RESULT?
DID ANYONE IDENTIFY A SAFETY PROBLEM?
DOES THE RESULT REQUIRE CONSENT FROM A SPECIFIC PERSON?
WAS THE ARITHMETIC REPLAYED?
```

A high score cannot override a required individual consent boundary.

### Step 10 — Receipt and replay

The round ends with a receipt.

## Minimal replay receipt

```json
{
  "receipt_id": "JOY-QV-RC-001",
  "game_id": "JOY-FAMILY-QV-001-R001",
  "rules_version": "0.1.0",
  "question_hash": "sha256:<pending>",
  "options_hash": "sha256:<pending>",
  "parameters_hash": "sha256:<pending>",
  "accepted_ballot_count": 0,
  "rejected_ballot_count": 0,
  "tally": {},
  "rubric_scores": {},
  "final_scores": {},
  "winning_option": "PENDING",
  "consent_gate": "NOT_EVALUATED",
  "replay_status": "NOT_EXECUTED",
  "previous_receipt_hash": "sha256:<pending>",
  "timestamp": "PENDING"
}
```

`<pending>` values are placeholders and are not valid cryptographic claims.

## Replay rules

A replay succeeds only when another family member can reconstruct:

1. the exact question;
2. the exact options;
3. the frozen budget and weighting;
4. every accepted or rejected ballot decision;
5. the tally arithmetic;
6. the rubric arithmetic;
7. the consent gate;
8. the final result.

Replay result states:

```text
REPRODUCED
PARTIALLY_REPRODUCED
REPLAY_MISMATCH
INDETERMINATE
```

## Tie handling

Default tie sequence:

```text
1. Recheck arithmetic.
2. Replay frozen parameters.
3. Check whether rubric scoring broke the tie.
4. Hold one runoff between tied options.
5. If still tied, rotate choice or use a neutral random draw agreed in advance.
```

No host may secretly choose the winner.

## Kindness protocol

```text
NO MOCKING A PRIVATE PREFERENCE.
NO PRESSURE TO REVEAL A BALLOT.
NO CLAIM THAT A LOSING VOTE WAS WRONG.
NO ACCUSATION OF BAD INTENT FROM A SCORE.
NO FAMILY STATUS IS EARNED OR LOST BY WINNING.
```

Mrs. Wisdom's family-first advice applies:

> The game is successful when the family remains connected, not merely when the arithmetic produces a winner.

## Example round

Question:

```text
What should we do for Saturday Game Night?
```

Options:

```text
A = movie and pizza
B = strategy board game
C = family archive and storytelling
```

Three private ballots:

```text
Player 1: A=3, B=2, C=3 → cost 9+4+9 = 22
Player 2: A=1, B=4, C=2 → cost 1+16+4 = 21
Player 3: A=2, B=2, C=4 → cost 4+4+16 = 24
```

Tally:

```text
A = 6
B = 8
C = 9
```

Illustrative rubric totals:

```text
A = 18/25
B = 20/25
C = 24/25
```

In both the tally and rubric example, option C leads.

The result remains subject to the family consent and practicality gate.

## Future cryptographic lane

A later technical edition may add:

- committed private ballots;
- zero-knowledge range proofs;
- quadratic budget proofs;
- public tally proofs;
- replay receipts bound to frozen commitments.

That work belongs under:

```text
verification/QUADRATIC_PROOF_V0_1.md
```

The cryptographic proof verifies arithmetic. It does not replace kindness, consent, or family judgment.

## Repository relationship

```text
JOY            = family experience, language, game, and replay lesson
COMPUTERWISDOM = optional implementation, app, and reusable product build
AL             = Alabama operating context and any state-specific constraints
```

No repository creates a family obligation or business ownership transfer.

## Final family theorem

```text
LOVE WITHOUT LOGIC CAN LOSE THE RECORD.
LOGIC WITHOUT LOVE CAN LOSE THE PERSON.
JOY KEEPS THEM AT THE SAME TABLE.
REPLAY KEEPS THE MATH HONEST.
WISDOM KNOWS WHEN THE GAME MUST YIELD TO FAMILY.
```
