# GitHub Gamified by Jay — Manual V0.1

**Status:** `TRAINING_MANUAL_DRAFT`
**Repo:** `jsonwisdom/JOY`
**Lane:** `docs/school-of-wisdom/`
**Authority:** `false`
**No Fake Green:** `true`

> A tiny-human-safe guide for using GitHub, terminal, and AI helpers without burning the repo down.

## 0. The Game

GitHub is the map.
The terminal is the controller.
AI is the helper goblin.
Receipts are the score.
Green means proven.
Yellow means not proven yet.
Red means stop.

## 1. Jay Is 6 With Terminal Access

Pretend the operator is brilliant, fast, curious, and dangerous because the buttons are real.

Rule:

```text
READ FIRST.
CHECK SECOND.
CHANGE THIRD.
PROVE FOURTH.
```

No guessing. No panic clicking. No fake green.

## 2. First Command Every Time

```bash
git status --short
```

If files appear, do not ignore them. They are toys on the floor. Step on them and you cry.

## 3. Safe Commands

Use these for looking around:

```bash
pwd
ls
git status --short
git branch --show-current
git log --oneline -5
git diff --stat
git diff -- path/to/file
cat path/to/file
sed -n '1,120p' path/to/file
```

## 4. Red-Button Commands

Some commands delete files, erase history, force-push branches, change permissions everywhere, or move big folders.

Those are red-button commands.

Before any red-button command, AI must explain:

```text
WHAT changes
WHY it is needed
WHAT could be lost
HOW to recover
WHETHER a backup exists
```

If the answer is fuzzy, do not press the button.

## 5. The Green Check Game

A claim can be GREEN only if it has evidence.

| Claim | Evidence needed |
|---|---|
| File exists | fetched file or directory listing |
| File changed | diff output |
| File committed | commit SHA |
| File hash proven | SHA256 line |
| Workflow passed | workflow run status |
| On-chain anchor exists | external chain readback |
| Full repo certainty | local clone plus sha256 replay |

If evidence is missing, the answer is YELLOW.

## 6. AI Helper Rules

AI must:

1. Search first.
2. Speak second.
3. Separate evidence classes.
4. Never call a draft executed.
5. Never call a repo receipt external verification.
6. Never call a workflow file a workflow run.
7. Never treat Git blob SHA as SHA256.
8. Keep family-safe boundaries.
9. Prefer one copy-paste block when giving terminal steps.
10. Stop before red-button commands.

## 7. The Baby Goblin Checklist

Before commit:

```bash
git status --short
git diff --stat
git diff -- docs/school-of-wisdom/
```

After commit:

```bash
git log --oneline -1
git status --short
```

After push:

```bash
git rev-parse HEAD
git status --short
```

## 8. The Joke Detector

Something happened.
Something else did not.
Humans treated them as the same thing.
That substitution is the joke.

Examples:

```text
File exists does not mean workflow passed.
Draft exists does not mean system executed.
Repo receipt does not mean external chain readback.
Blob SHA does not mean SHA256 receipt.
Screenshot does not mean byte proof.
```

## 9. Scoreboard

```text
GREEN = proven by the right evidence class
YELLOW = plausible but not proven
RED = contradicted, unsafe, or missing required boundary
```

## 10. Final Rule

When Jay moves fast, the system moves slower on purpose.

Not to block Jay.
To protect Jay's proof.

**School voice:** GitHub first. Evidence classes separate. Speak second.
