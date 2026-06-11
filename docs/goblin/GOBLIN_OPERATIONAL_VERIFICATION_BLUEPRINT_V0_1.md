# Goblin Operational Verification Blueprint V0.1

## Status

OPERATIONAL_VERIFICATION_BLUEPRINT_SEEDED

## Purpose

Define the deterministic system-level verification pass for the Goblin Gate after Level-4 component binding.

This artifact is not a Court ruling.
This artifact is not a production deployment receipt.
This artifact does not grant semantic authority.
This artifact does not promote any mint, route, or card to verified status.

## Anchored Inputs

- Level-3 Public Route Map: docs/goblin/GOBLIN_PUBLIC_ROUTE_MAP_V0_1.md
- Level-3 Public Route Map Commit: 094949beb259b1796539c7f337c9a36a5e4d6eae
- Level-4 Homepage Integration Map: docs/goblin/GOBLIN_HOMEPAGE_INTEGRATION_MAP_V0_1.md
- Level-4 Homepage Integration Map Commit: 803859cc67cfd9f90e4958199004d9e4e458a524
- Level-4 Component Binding: components/goblin-gate/index.ts
- Level-4 Component Binding Commit: 076334ae9023b3d3885b08cd2c69ea74c647d626

## Required Verification Pass

### 1. Load Constellation JSON

- Source: artifacts/goblin_constellation_v0_1.json
- The loader must not infer missing nodes.
- The loader must not mutate status labels.
- Missing source means operational state is HOLD.

### 2. Render Goblin Gate

- Homepage area: Minting Options
- Component target: Goblin Gate
- Function: bindGoblinRepoConstellation()
- Hook alias: useGoblinRepoConstellation()

### 3. Confirm Card Shape

Each rendered card must expose only:

- title
- repo
- path
- status
- link
- mintEnabled
- warning

No private content preview is allowed.
No semantic summary is allowed.
No court ruling is allowed inside the card.

### 4. Confirm Allowed Status Labels

Only the following labels are allowed:

- GREEN
- GREEN_SEEDED
- PUBLIC_ROUTE_MAP_SEEDED
- SPEC_SEEDED_CANDIDATE
- HOLD
- UNKNOWN

Any other label triggers BOUNDARY_VIOLATION.

### 5. Confirm Friction Enforcement

- mintEnabled must remain false for every card.
- Missing path collapses to HOLD.
- Missing commit or href collapses to HOLD.
- Unknown repo key collapses to HOLD.
- Unknown label collapses to HOLD.

### 6. Confirm Authority Boundary

The replay object must include:

```json
{
  "authority": false,
  "no_fake_green": true,
  "fallback_state": "HOLD_OR_UNKNOWN"
}
```

Any authority=true result triggers BOUNDARY_VIOLATION.

## Failure States

```json
{
  "BOUNDARY_VIOLATION": "AUTO_ESCALATE_TO_COURT",
  "MISSING_CONSTELLATION_JSON": "HOLD",
  "UNAUTHORIZED_STATUS_LABEL": "HOLD",
  "MINT_ENABLED_WITHOUT_EVIDENCE": "BOUNDARY_VIOLATION",
  "SEMANTIC_PROMOTION_DETECTED": "BOUNDARY_VIOLATION"
}
```

## Expected Output

A valid operational verification pass may produce only:

```json
{
  "system_mode": "GOBLIN_OPERATIONAL_MODE_V0_1",
  "verification_pass": "COMPLETE_OR_HOLD",
  "authority": false,
  "no_fake_green": true,
  "cards_checked": "<NUMBER>",
  "violations": []
}
```

## Court Rule

Operational verification checks runtime conformance.
It does not create canon.
It does not grant authority.
It does not verify content.

## Authority

false

## No Fake Green

true
