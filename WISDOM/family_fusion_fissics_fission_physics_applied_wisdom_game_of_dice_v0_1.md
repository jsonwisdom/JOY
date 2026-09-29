# Family Fusion Fissics / Fission Physics — Applied Wisdom Game of Dice V0.1

Status: NEW_GAME_SPEC
Authority: false
Surface: WISDOM_FAMILY_GAME_NIGHT
Execution: NOT_RECORDED
No Fake Green: true
Append Only: true

## Lineage

This game extends the existing Wisdom Family Game Night dice lineage without rewriting the unbound family-story manuscript.

Repo-backed parents:

~~~text
WISDOM/wisdom_family_game_night_dice_game_v0_1.md
WISDOM/wisdom_family_game_night_v0_1.md
WISDOM/wisdom_game_night_expansion_pack_v0_2.md
docs/constitution/SPEED_IS_NOT_CERTAINTY_V0_1.md
docs/constitution/GENERATE_FAST_PROMOTE_SLOW_REPLAY_ALWAYS_V0_1.md
docs/goblin-courts/JASONS_MINNESOTA_EXPLORER_GAMBIT_TIMESTAMP_ACCOUNTABILITY_V0_1.md
~~~

New story labels:

~~~text
AMERICAN_TICK_MATH_PHYSICS_BY_JAYS_GAMBIT
CERTAINLY_ENTROPY_DEMON
FAMILY_FUSION_FISSICS_FISSION_PHYSICS
~~~

They are teaching / story labels, not physical findings, legal claims, government authority, or proof of identity.

## The kid rule

~~~text
SPLIT IT.
CHECK IT.
ROLL IT.
REPLAY IT.
JOIN ONLY WHAT SURVIVES.
~~~

## Six-sided Applied Wisdom die

One ordinary D6 chooses the operation, never the truth.

~~~text
1 = FISSION
2 = FUSION
3 = TICK
4 = ENTROPY
5 = RECEIPT
6 = REPLAY
~~~

Hard boundary:

~~~text
ROLL != TRUTH
RANDOM_SELECTION != AUTHORITY
GAME_OUTPUT != FACT
~~~

## Face 1 — FISSION

Take one sentence or harmless family/game claim and split it into the smallest checkable parts.

Example:

~~~text
"The red die rolled six twice."

FISSION:
A = a red die was used
B = roll 1 was six
C = roll 2 was six
D = both observations belong to the same recorded round
~~~

Fission rule:

~~~text
COMPOUND_CLAIM
→ ATOM_1 + ATOM_2 + ... + ATOM_n
~~~

No atom inherits proof from its neighbors.

~~~text
PROVED(A) != PROVED(B)
SHARED_SENTENCE != SHARED_RECEIPT
~~~

## Face 2 — FUSION

Fuse only receipt-bound atoms.

~~~text
A + B + RECEIPTS_FOR_A_AND_B
→ FUSION_CANDIDATE
~~~

If a required bridge is missing:

~~~text
FUSION = HOLD
~~~

Evidence conservation rule:

~~~text
FUSION DOES NOT CREATE NEW EVIDENCE.
~~~

Combining two proven atoms may support a larger claim only when the logical bridge is itself valid.

## Face 3 — AMERICAN TICK

A tick is a typed discrete time step:

~~~text
t_n = t_0 + n*Delta_t
~~~

For the game, one tick may be one roll, one replay step, or one timestamped receipt event.

Clock boundary:

~~~text
GAME_TICK != GITHUB_TIME
GAME_TICK != DRIVE_TIME
GAME_TICK != REAL_WORLD_EVENT_TIME
ORDERING != CAUSATION
~~~

Jay's Gambit rule:

~~~text
NAME THE CLOCK BEFORE COMPARING THE CLOCK.
~~~

## Face 4 — Certainly Entropy Demon

Certainly Entropy Demon is a fictional teaching character who attacks fake certainty.

Question:

> How uncertain were we before the roll, and what changed after observation?

For a fair six-sided die:

~~~text
H(D6) = log2(6) ~= 2.585 bits
~~~

For two independent fair six-sided dice:

~~~text
36 equally likely ordered outcomes
H(D6,D6) = log2(36) ~= 5.170 bits
~~~

After a particular roll is observed, uncertainty about that already-observed game variable is zero:

~~~text
H(observed_result | observed_result) = 0
~~~

That does NOT mean the physical entropy of the room, computer, dice, or universe became zero.

~~~text
INFORMATION_ENTROPY != THERMODYNAMIC_ENTROPY
OBSERVING_A_ROLL != REVERSING_THE_SECOND_LAW
CERTAINTY_ABOUT_ONE_RECORDED_VALUE != UNIVERSAL_CERTAINTY
~~~

Certainly Entropy Demon's line:

> "You learned the roll. You did not learn the universe."

## Face 5 — RECEIPT

For a dice round, save only what is needed:

~~~text
round_id
die_sides
roll_sequence
operator
game_tick
prediction
observed_result
receipt_pointer
privacy_state
~~~

No private family detail is required.

~~~text
PERSONAL_DATA_REQUIRED = FALSE
AUTHORITY_CREATED = FALSE
~~~

## Face 6 — REPLAY

Run the bounded path again.

~~~text
CLAIM
→ FISSION
→ SOURCE / OBSERVATION
→ RECEIPT
→ REPLAY
→ FUSION_CANDIDATE
→ PASS | HOLD | CONFLICT
~~~

Replay does not guarantee the same random roll.

Replay checks whether the method and classification rules survive.

~~~text
SAME_METHOD != SAME_RANDOM_OUTCOME
DIFFERENT_ROLL != METHOD_FAILURE
REPLAY != REROLL_UNTIL_DESIRED
~~~

## Two-dice mode

Roll two dice.

First die chooses the operation.
Second die chooses the challenge:

~~~text
1 = Explain it to a six-year-old
2 = Write the equation
3 = Name the missing receipt
4 = State what is NOT proved
5 = Find a possible collision
6 = Replay from the beginning
~~~

Total ordered combinations:

~~~text
6 * 6 = 36
~~~

Each ordered pair has probability:

~~~text
1/36
~~~

if both dice are fair and independent.

## Fusion / fission scoreboard

Score the process, never the person.

One table point for each:

- compound claim successfully split
- missing bridge correctly held
- clock explicitly typed
- probability kept separate from observation
- information entropy kept separate from thermodynamic entropy
- receipt preserved
- replay completed without rerolling for a preferred answer
- private information protected

## Family physics membrane

This is applied teaching language, not a claim that family relationships obey nuclear physics.

~~~text
FAMILY_FUSION = STORY / COOPERATION METAPHOR
FAMILY_FISSION = CLAIM_DECOMPOSITION METAPHOR
NUCLEAR_FUSION != FAMILY_RELATION
NUCLEAR_FISSION != FAMILY_CONFLICT
PHYSICS_METAPHOR != PHYSICAL_FINDING
~~~

## Story expansion boundary

The existing repository shows that the family-story manuscript is still unbound and its story bind remains HOLD.

Therefore:

~~~text
THIS_GAME
!= FAMILY_STORY_MANUSCRIPT
!= STORY_BIND
!= REPLAY_RECEIPT_FOR_THE_MANUSCRIPT
~~~

This file expands the public teaching/game layer only.

## Canonical operators

~~~text
FISSION(x)
= decompose x into independently checkable atoms

CHECK(atom)
= test one atom against its own admissible receipt

FUSION(atoms)
= combine only atoms and bridges that passed

TICK(clock)
= advance one typed step without changing authority

ENTROPY(outcome_space)
= quantify uncertainty under stated assumptions

REPLAY(path)
= repeat the method while preserving prior state
~~~

## Conservation law for the audit game

~~~text
NO_RECEIPT_IN
→ NO_RECEIPT_OUT

SATIRE_IN
→ SATIRE_OUT

HOLD_IN
→ HOLD_PRESERVED

NEW_EVIDENCE
→ APPEND_NEW_RECEIPT
~~~

No operator may manufacture certainty.

## Receipt shape

~~~json
{
  "module": "FAMILY_FUSION_FISSICS_FISSION_PHYSICS_APPLIED_WISDOM_GAME_OF_DICE_V0_1",
  "round_id": null,
  "die_sides": 6,
  "operation_face": null,
  "challenge_face": null,
  "typed_clock": null,
  "claim_atoms": [],
  "receipt_pointers": [],
  "fusion_status": "HOLD",
  "entropy_model": "FAIR_D6_CLASSROOM_MODEL",
  "private_family_data_collected": false,
  "authority": false,
  "execution": false,
  "verification": false,
  "status": "NEW_GAME_SPEC"
}
~~~

## Lock line

~~~text
Fission splits the claim.
Receipts test the pieces.
Fusion joins only what survives.
The tick keeps time typed.
Entropy measures uncertainty, not human worth.
The dice choose the lesson, never the truth.
Replay keeps the story honest.
Authority remains false.
~~~
