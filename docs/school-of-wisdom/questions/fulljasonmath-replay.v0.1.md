# FullJasonMathReplay — Prove the Proof (Mathematics v0.1)

Status: DRAFT_FOR_PLAYTEST  
Authority: false  
No Fake Green: true  
MarydeeBot: bcbcca1d-8cf2-45a7-ac93-0f9fd9d2c347  
Tested With Real Family: false

## 1. Question

**When a number looks right, can I reproduce the calculation exactly?**

The learner owns the question. The answer may be **HOLD**.

## 2. Story

Jason's **FULL MATH — PROVE THE PROOF** logo names the lesson; artwork is preserved unchanged as a user-supplied design reference. A logo does not itself supply a calculation, timestamp, signature, or mathematical proof.

A new Card 13 dice demonstration reported a roll of 64. Replaying a supplied roll digest can test its numerical mapping, but cannot determine how impartially the original seed was chosen.

## 3. Lesson

```text
CALCULATION_MATCH != INPUT_TRUTH
HASH_MATCH != SEED_FAIRNESS
REPLAYED_DEMONSTRATION != HISTORICAL_CARD_13
LOGO != MATHEMATICAL_RECEIPT
PASS_SCOPED != HUMAN_AUTHORITY
```

Exact rational mathematics avoids binary floating-point approximation for these exercises. External facts and historical claims require independent evidence.

## 4. Game

Optional, local-only puzzles (no children's data, wallet access, or external uploads):

- `1/3 + 1/6` — is the exact answer `1/2`? (PASS_SCOPED)
- `478 + 478 = 957` — replay and flag the incorrect assertion. (FAIL; result 956)
- Given digest `afea6ad62370343a55aac86bd0967b6ef02ad3cf51fd76b46acda203ad9fc224`, use rejection sampling over 0..99. (64, zero rejections; **digest mapping only**)

An unverified input or missing expected result returns **HOLD**, not a fabricated pass.

## 5. Receipt

Read-only input example for `scripts/fulljasonmath_replay.py`:

```json
{
  "case_id": "fraction-example",
  "kind": "arithmetic",
  "operation": "add",
  "operands": ["1/3", "1/6"],
  "expected": "1/2"
}
```

Replay reports a SHA-256 digest of the supplied JSON and a bounded math verdict. This hash identifies the submitted bytes; it does not attest their historical truth or provenance.

## 6. Replay

MarydeeBot's existing Question Steward validates the seven-step curriculum shape. The **optional mathematics module** independently recomputes exact rational or 256-bit digest-mapping test cases. Passing either checker does not approve the other one, the School globally, or any historical Card 13 claim.

```text
MATH_REPLAY=SCOPED
ORIGINAL_CARD_13=HOLD
ENTROPY_IMPARTIALITY=NOT_CERTIFIED
FAMILY_TESTING=NOT_PERFORMED
CANON_PROMOTION=FALSE
AUTHORITY_CREATED=FALSE
JASON_FINAL_DECISION=REQUIRED
```

## 7. Your Turn

Optional. You may challenge the arithmetic, decline, keep notes private, or choose not to save anything. No scores are assigned to children.

## Family Gate

```text
FAMILY SAFETY OUTRANKS SYSTEM EXPANSION
NO PRIVATE CHILD DATA
NO CONSENT ASSUMED
NO PUBLIC FAMILY CLAIM WITHOUT PERMISSION
NO FAKE GREEN
```

## Draft Boundary

```text
FILE_EXISTS = TRUE_ON_REVIEW_BRANCH
CHAPTER_DRAFTED = TRUE
PLAYTESTED_WITH_REAL_FAMILY = false
SCHOOL_STANDARD_PASSED = false
HUMAN_APPROVED = false
```
