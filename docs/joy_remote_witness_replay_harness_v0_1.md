# JOY Remote Witness Replay Harness V0.1 🧾

## Purpose

The JOY Remote Witness Replay Harness verifies that a ritual receipt matches the current repository state.

It does not mutate files.
It does not create authority.
It only reads and reports.

## Input

A ritual receipt JSON file.

## Output

- VERIFIED
- REJECTED

## Verification Checks

1. SVG exists.
2. SHA-256 of SVG matches receipt.
3. Receipt status is valid.
4. Manifest entry exists.
5. Manifest hash matches receipt.
6. Local HEAD exists.
7. Remote main matches local HEAD.

## Rule

Read only. No mutation.
