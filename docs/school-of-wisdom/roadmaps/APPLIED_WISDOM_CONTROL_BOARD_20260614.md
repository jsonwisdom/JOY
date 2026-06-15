# Applied Wisdom Control Board

**Date:** 2026-06-14  
**Repo:** jsonwisdom/JOY  
**Lane:** docs/school-of-wisdom/roadmaps/  
**Status:** CONTROL_BOARD_DRAFT  
**Authority:** false  
**No Fake Green:** true

---

## Purpose

This board connects the School of Wisdom, JoySpace, protected family replay, GitHub Gamified training, and on-chain boundaries into one operating map.

The goal is not to make bigger claims.

The goal is to keep proven states separate from drafted states.

---

## Current Green / Scoped Green Layer

| Layer | State | Evidence class |
|---|---|---|
| School of Wisdom schema | GREEN | committed schema + readback |
| Gatekeeper schema | GREEN | committed schema + readback |
| GitHub Gamified manual | GREEN | committed manual + readback |
| Run 001 sandbox loop | GREEN_SCOPED | sandbox marker + execution receipt |
| Run 002 workflow file | GREEN | workflow file + readback |
| Run 003 trigger receipt | GREEN_SCOPED | trigger receipt + readback |
| School evidence locker | GREEN | incident receipt + readback |
| Protected family replay | GREEN_SCOPED | replay receipt + protected boundaries |
| On-Chain Mind lesson | GREEN_SCOPED | lesson receipt + backup reference |

---

## Yellow Perimeter

| Item | State | Reason |
|---|---|---|
| GitHub Actions run success | YELLOW | run proof not captured |
| Full byte-by-byte repo certainty | YELLOW | requires local clone + hash replay |
| External chain readback | YELLOW | no live readback attached to this board |
| Public HTTP route certainty | YELLOW | repo path is not automatically a public route |

---

## Next Gates

### Gate 1 — Actions Proof Run

Goal: convert Actions from workflow-file GREEN to run GREEN_SCOPED.

Required evidence:
- workflow run id
- run URL
- head SHA
- conclusion
- safe proof log line

Do not claim run GREEN from the workflow file alone.

### Gate 2 — Local Byte Replay

Goal: convert local terminal execution from YELLOW to GREEN_SCOPED.

Required evidence:
- clean working tree
- HEAD commit
- selected file hashes
- receipt file readback

Do not claim full repo certainty unless the full tree is replayed.

### Gate 3 — Public Route Check

Goal: distinguish repo path from website route.

Required evidence:
- public HTTP status
- route checked
- response hash if captured

Do not treat docs/ path as a public URL by default.

### Gate 4 — On-Chain Readback

Goal: verify chain-facing claims without expanding protected family content.

Required evidence:
- exact transaction or UID
- network name
- readback source
- timestamp

Do not treat a repo receipt as external chain confirmation.

### Gate 5 — Applied Wisdom Lesson

Goal: turn the protected replay into a lesson for School of Wisdom.

Allowed themes:
- ancestry as continuity
- reputation as earned trust
- resilience as recovery after mistakes
- certainty as evidence discipline
- democracy math as public reasoning
- gamification as learning flow

---

## School Lesson

Applied Wisdom means the system learns from wins and mistakes.

JoySpace carries care and memory.

School of Wisdom teaches evidence classes and no fake green.

On-chain thinking teaches that anchoring proof is not the same as expanding public claims.

GitHub Gamified teaches that every level needs a receipt.

---

## Operating Rule

READ FIRST.  
CHECK SECOND.  
CHANGE THIRD.  
PROVE FOURTH.

If proof is missing, the state is YELLOW.

---

## Ruling

```text
APPLIED_WISDOM_CONTROL_BOARD = GREEN_SCOPED
PROTECTED_REPLAY_LINKED = GREEN_SCOPED
SCHOOL_NETWORK_LINKED = GREEN_SCOPED
ONCHAIN_BOUNDARY_DEFINED = GREEN_SCOPED
ACTIONS_RUN_STATUS = YELLOW
FULL_BYTE_BY_BYTE_REPO_CERTAINTY = YELLOW
PUBLIC_ROUTE_CERTAINTY = YELLOW
NO_FAKE_GREEN = ACTIVE
```
