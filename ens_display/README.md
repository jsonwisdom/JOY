# ENS Display-Only Discovery Surface V0.1

Status: DISPLAY_ONLY
Authority: false
Membrane: HOLDS

## Purpose

Define a read-only ENS discovery surface for JOYSPACE and the three-repo replay spine.

This surface displays identity anchors for discovery and routing. It does not write ENS records, connect wallets, sign messages, mutate custody, or claim authority.

## Identity Anchors

- jaywisdom.eth
- jaywisdom.base.eth
- jaywisdom.base

## Route

3 -> JOY protection
6 -> ENS identity discovery
9 -> ALMS replay memory

## Display Rules

Allowed:

- Show public identity anchors.
- Copy identity anchors.
- Link to public replay surfaces.
- Mark unknowns as UNKNOWN.
- Mark queued states as QUEUED.

Forbidden:

- No wallet connect.
- No chain write.
- No ENS record write.
- No custody mutation.
- No legal, medical, emergency, or official authority claim.
- No child identity exposure by default.

## Example Output

```json
{
  "surface": "ENS_DISPLAY_ONLY_DISCOVERY_V0_1",
  "anchors": [
    "jaywisdom.eth",
    "jaywisdom.base.eth",
    "jaywisdom.base"
  ],
  "state": "DISPLAY_ONLY",
  "authority": false,
  "membrane": "HOLDS"
}
```

## Compliance

- Replay is not judgment.
- Visibility is not authority.
- ENS routes identity but does not prove claims.
- Memory is allowed before merge.
- Promotion is blocked until receipt.

## Final Line

ENS discovers. It does not decide.
