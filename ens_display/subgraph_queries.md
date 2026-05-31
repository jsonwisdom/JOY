# ENS Subgraph Discovery V0.1

Status: DISPLAY_ONLY
Authority: false
Membrane: HOLDS

## Purpose

Enable read-only ENS discovery using indexed data without chain writes, anchoring, custody mutation, or authority claims.

## Discovery Targets

- jaywisdom.eth
- jaywisdom.base.eth
- jaywisdom.base

## Allowed Queries

- forward resolve name to public records
- reverse lookup address to names
- batch discovery by public fragment

## Display Rules

- Parent identity surfaces may be displayed.
- Child identity surfaces are hidden by default.
- Emergency exceptions require explicit receipt and witness.
- Query results are display-only.
- No discovered name is promoted to verified by this module.

## Cache Rule

Ephemeral display cache only. No custody mutation. No chain write.

## Invariants

- no chain write
- no authority claim
- child identity hidden by default
- membrane HOLDS
- replay is not judgment

Final line: ENS discovers. It does not decide.
