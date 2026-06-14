# TRIGGER_HUNTER_QA_V0_1

## Q: What do we trigger?
A: Repo maintenance only: manual dispatch, push-path checks, daily drift check, and machine replay consistency.

## Q: What is valuable right now?
A: Knowing whether the repo changed, which workflows exist, whether replay still passes, and whether we can snap back to the current head.

## Q: What do we not trigger yet?
A: No EAS truth promotion, no Zora purpose claim, no wallet-control claim, no semantic finality.

## Q: What is the snap-back fixture?
A: A timestamped snapshot of branch, head, status, workflows, recent commits, replay result, and recent GitHub runs.

## Ruling
TRIGGER HUNTER = LIVE MAINTENANCE
MACHINE GREEN = CONSISTENCY ONLY
AUTHORITY = FALSE
NO_FAKE_GREEN = TRUE
