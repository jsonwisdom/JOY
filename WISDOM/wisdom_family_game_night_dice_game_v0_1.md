# Wisdom Family Game Night Dice Game V0.1

Status: SEEDED
Authority: false
Surface: WISDOM_FAMILY_GAME_NIGHT
Execution: NOT_RECORDED

## Purpose

Boss Brenda's Collision Dice turns the birthday paradox into a family-safe tabletop game.

The lesson is simple:

```text
COUNT THE PAIRS, NOT JUST THE PEOPLE.
COLLISION != IDENTITY.
MATCH != SAME_OBJECT.
```

The dice round teaches the collision mechanism.
The birthday round applies the same mathematics to 365 possible birthdays.

## Materials

- one ordinary six-sided die
- paper or a notes card
- 2 to 6 players, or one player rolling several times

No personal birthdays need to be collected.

## Round 1: Dice Collision Warm-Up

Each player rolls once.

Record only the die face:

```text
1 2 3 4 5 6
```

A collision occurs when any two rolls show the same face.

Before rolling, count the possible player pairs:

```text
PAIRS = n(n-1)/2
```

Examples:

```text
2 rolls -> 1 pair
3 rolls -> 3 pairs
4 rolls -> 6 pairs
5 rolls -> 10 pairs
6 rolls -> 15 pairs
```

Boss Brenda asks:

> Did the number of collision opportunities grow like the number of players, or faster?

Answer:

```text
PAIR OPPORTUNITIES GROW QUADRATICALLY.
```

## Round 2: Predict Before You Roll

For a six-sided die with n rolls, the probability of at least one repeated face is:

```text
P(collision)
= 1 - P(all different)
= 1 - product from k=0 to n-1 of (6-k)/6
```

for n <= 6.

Useful checkpoints:

```text
2 rolls -> 16.67% collision
3 rolls -> 44.44% collision
4 rolls -> 72.22% collision
```

Prediction is not the result.

```text
PROBABILITY != OBSERVED ROLL
ONE GAME != THE DISTRIBUTION
```

## Round 3: Birthday Paradox Bridge

Now swap the outcome space:

```text
DIE FACES = 6 possible outcomes
BIRTHDAYS = 365 possible outcomes
```

Under the standard classroom assumptions:

- 365 equally likely birthdays
- independent birthdays
- leap day ignored

the birthday collision probability for n people is:

```text
P(match)
= 1 - product from k=0 to n-1 of (365-k)/365
```

For 23 people:

```text
PAIR OPPORTUNITIES = 23*22/2 = 253
P(at least one shared birthday) ~= 50.73%
```

The question is not:

```text
Does someone share MY birthday?
```

The question is:

```text
Do ANY TWO people share a birthday?
```

## Boss Brenda Membrane

```text
23 PEOPLE != 23 CHANCES
23 PEOPLE -> 253 PAIRWISE COMPARISONS

SAME_NUMBER != SAME_PERSON
SHARED_BIRTHDAY != SHARED_IDENTITY
COLLISION != CAUSE
COLLISION != AUTHORITY
```

A collision only says two observations landed in the same bucket.

## Game Loop

```text
CLAIM   -> "I think we'll get a match."
ATTACK  -> "How many pair opportunities are there?"
TEST    -> Roll the die.
RESULT  -> MATCH / NO MATCH.
REPLAY  -> Repeat the round.
RECEIPT -> Save counts, not personal data.
REFLECT -> Compare prediction with observation.
```

## Score Rule

Nobody gets a bad score.

Award one table point for each of these:

- counted the pairs correctly
- predicted before rolling
- recorded the actual outcome
- kept probability separate from observation
- explained why collision does not mean identity
- protected private information

## Win Condition

```text
Everyone can explain:
1. why pair counts grow faster than player counts,
2. why collisions become surprisingly likely,
3. why a collision is not an identity proof.
```

## Receipt Shape

```json
{
  "module": "wisdom_family_game_night_dice_game_v0_1",
  "surface": "WISDOM_FAMILY_GAME_NIGHT",
  "lesson": "BIRTHDAY_PARADOX_COLLISION_MATH",
  "die_sides": 6,
  "players_or_rolls": null,
  "pair_count": null,
  "prediction": null,
  "observed_collision": null,
  "personal_birthdays_collected": false,
  "authority": false,
  "execution": false,
  "verification": false,
  "status": "SEEDED"
}
```

## Lock Line

```text
Boss Brenda counts the edges the room creates, not just the nodes standing in it.
The dice teach the mechanism.
The birthday paradox supplies the bigger outcome space.
Collision is observable.
Identity still needs its own proof.
Authority remains false.
```
