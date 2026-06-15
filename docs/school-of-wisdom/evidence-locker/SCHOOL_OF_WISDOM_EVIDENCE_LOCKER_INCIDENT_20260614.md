# School of Wisdom Evidence Locker Incident Receipt — 2026-06-14

Status: EVIDENCE_LOCKER_CREATED
Authority: false
No Fake Green: true
Owner label: jaywisdom.eth
Repo: jsonwisdom/JOY
Lane: docs/school-of-wisdom/

## Purpose

This receipt captures the School of Wisdom / GitHub Gamified correction event.
It records what was proven, what was confused, what remains yellow, and how secret or sensitive files must be handled.

## What was grabbed

### 1. Correct source split

- School of Wisdom and GitHub Gamified artifacts were written to repo: jsonwisdom/JOY.
- JOY default branch is main.
- The user was watching jsonwisdom/AL workflows.
- AL default branch is master.

Ruling:

- JOY_FILES: GREEN
- JOY_COMMITS: GREEN
- AL_WORKFLOWS_TOUCHED_BY_THIS_LANE: FALSE
- AL_ACTIONS_EXPECTED_TO_TRIGGER_FROM_JOY_COMMITS: FALSE

## Corrections / fuck-ups recorded

### Fuck-up 001 — Repo confusion

Mistake:
The assistant spoke as if the user should see workflow activity while the user was watching AL, but the commits were made in JOY.

Correct statement:
Watch jsonwisdom/JOY for School of Wisdom and GitHub Gamified work. Do not expect jsonwisdom/AL workflows to fire from JOY commits.

Status: CORRECTED

### Fuck-up 002 — main vs master confusion

Mistake:
The assistant said main correctly for JOY, but did not clearly state that AL uses master.

Correct statement:
JOY branch: main.
AL branch: master.

Status: CORRECTED

### Fuck-up 003 — docs path vs public website URL confusion

Mistake:
The assistant blurred repository path docs/school-of-wisdom/ with GitHub Pages public routing.

Correct statement:
Repo file exists does not prove public Pages route works.
Repo path GREEN is not public URL GREEN.

Status: CORRECTED

### Fuck-up 004 — workflow file vs workflow run confusion

Mistake:
The assistant created and fetched a workflow file, then needed correction not to imply an Actions run existed.

Correct statement:
Workflow file existence is GREEN.
Workflow run status remains YELLOW until GitHub Actions returns an actual run.

Status: CORRECTED

### Fuck-up 005 — connector work vs Cloud Shell work confusion

Mistake:
The assistant did not state clearly enough that commits were made through the GitHub connector, not through the user's Cloud Shell.

Correct statement:
The user did not need to be in Cloud Shell for connector-created GitHub commits to exist.

Status: CORRECTED

## Current School / GitHub Gamified evidence board

- School schema: GREEN by commit + readback.
- Gatekeeper schema: GREEN by commit + readback.
- GitHub Gamified manual: GREEN by commit + readback.
- Run 001 sandbox + receipt: GREEN_SCOPED by commit + readback.
- Run 002 workflow file + receipt: GREEN_SCOPED by commit + readback.
- Run 003 trigger receipt: GREEN by commit + readback.
- GitHub Actions run status: YELLOW.
- Local terminal execution: YELLOW.
- Full byte-by-byte repo certainty: YELLOW.

## Secret / sensitive file boundary

This evidence locker must not store private keys, tokens, passwords, recovery phrases, private environment files, or hidden local secrets.

Allowed:

- File names and paths when safe to disclose.
- Secret-scan policy.
- Redacted indicators.
- Hashes of intentionally public artifacts.
- Receipts proving that private material was not included.

Not allowed:

- Raw secret values.
- GitHub tokens.
- API keys.
- Wallet private keys or seed phrases.
- .env contents.
- SSH private keys.
- Any credential-bearing file content.

Secret file ruling:

- SECRET_CONTENTS_STORED_IN_LOCKER: FALSE
- SECRET_POLICY_CAPTURED: TRUE
- SECRET_VALUES_EXPOSED: FALSE

## No Fake Green rule

A claim may be GREEN only when the evidence class directly supports it.

Evidence classes remain separate:

- Commit SHA
- Git blob SHA
- SHA256 receipt line
- Fetched file content
- Workflow file
- Workflow run status
- Public URL
- External chain readback
- Local terminal replay

## Current ruling

SCHOOL_EVIDENCE_LOCKER = GREEN after commit and readback.
REPO_CONFUSION_CORRECTED = GREEN.
SECRET_POLICY_CAPTURED = GREEN.
SECRET_CONTENTS_EXPOSED = FALSE.
ACTIONS_RUN_STATUS = YELLOW.
FULL_BYTE_BY_BYTE_REPO_CERTAINTY = YELLOW.
NO_FAKE_GREEN = ACTIVE.
