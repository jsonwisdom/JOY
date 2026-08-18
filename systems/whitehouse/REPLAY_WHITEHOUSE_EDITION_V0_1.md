# REPLAY_WHITEHOUSE_EDITION_V0_1

## Replay type

Hypothetical module replay.

```text
SIMULATION_ONLY           = TRUE
OFFICIAL_AFFILIATION      = FALSE
FEDERAL_AUTHORITY         = NONE
EXECUTION_AUTHORITY       = FALSE
RECEIPTS_CREATE_AUTHORITY = FALSE
```

## Purpose

A replay packet records how a White House Edition scenario was interpreted inside JOY. It is descriptive, not directive, and creates no official action.

## Required structure

1. Replay ID
2. Scenario ID
3. Timestamp
4. Assumptions
5. Inputs
6. Actors
7. Constraints
8. Events
9. Outputs
10. Receipts
11. Boundary-check result

## Example envelope

```yaml
replay_id: WH-REPLAY-0001
scenario_id: WH-SCENARIO-0001
timestamp: 2026-08-03T00:00:00Z
status: hypothetical
simulation_only: true
official_affiliation: false
federal_authority: none
execution_authority: false
receipts_create_authority: false

assumptions:
  - No real government authority is created.
  - JOY root identity remains unchanged.

events:
  - event_id: WH-EVENT-0001
    type: boundary_check
    result: pass

outputs:
  - module remains contained
  - no authority created

receipts:
  - receipt_id: WH-RECEIPT-0001
    type: replay
    authority_created: false
```

## Replay rule

```text
MEMORY    = TRUE
AUTHORITY = FALSE
```
