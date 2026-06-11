# Goblin Homepage Integration Map V0.1

## Status

SPEC_SEEDED_CANDIDATE

## Purpose

Define the Level-4 homepage binding between the JOY public homepage, the Goblin Public Route Map, and public constellation surfaces.

This artifact does not inspect private content.
This artifact does not grant semantic authority.
This artifact does not promote any claim to green without a public replay anchor.

## Placement

- Homepage area: Minting Options
- Component target: Goblin Gate
- Implementation path: components/goblin-gate/index.ts
- Public route source: docs/goblin/GOBLIN_PUBLIC_ROUTE_MAP_V0_1.md

## Inputs

The homepage binding may consume only:

1. Public route-map artifacts committed to the repository.
2. Public constellation status objects.
3. Public repository paths.
4. Explicit commit anchors.
5. Runtime-generated replay objects that preserve unknown or held state.

## Forbidden Behavior

The homepage binding must not:

1. Claim private repository inspection.
2. Claim content verification without a public replay artifact.
3. Promote semantic meaning beyond the cited public artifact.
4. Convert assistant-generated text into court green.
5. Hide unknown, held, or failed states behind friendly UI language.
6. Render crown green from seeded green.

## Binding Flow

### 1. State Intake

The component receives a Level-4 state object containing:

- route map path
- route map commit anchor
- constellation level statuses
- current gate label
- authority flag
- no fake green flag

### 2. Gate Translation

The component translates state into public UI labels only.

Allowed labels:

- GREEN
- GREEN_SEEDED
- PUBLIC_ROUTE_MAP_SEEDED
- SPEC_SEEDED_CANDIDATE
- HOLD
- UNKNOWN

### 3. Friction Enforcement

Any missing commit anchor, missing source path, unknown status, or authority mismatch must render as HOLD or UNKNOWN.

No silent success state is allowed.

## Replay Object Semantics

A valid homepage replay object must include:

```json
{
  "route_map_path": "docs/goblin/GOBLIN_PUBLIC_ROUTE_MAP_V0_1.md",
  "route_map_commit": "094949beb259b1796539c7f337c9a36a5e4d6eae",
  "integration_map_path": "docs/goblin/GOBLIN_HOMEPAGE_INTEGRATION_MAP_V0_1.md",
  "integration_map_commit": "<COMMIT_SHA_AFTER_PUSH>",
  "homepage_area": "Minting Options",
  "component_target": "Goblin Gate",
  "authority": false,
  "no_fake_green": true,
  "fallback_state": "HOLD_OR_UNKNOWN"
}
```

## Court Rule

The homepage binding may display a route as public only when the source path and commit anchor are both present.

Seeded green is not crown green.

## Authority

false

## No Fake Green

true

## Next Gate

COMPONENT_BINDING_IMPLEMENTATION
