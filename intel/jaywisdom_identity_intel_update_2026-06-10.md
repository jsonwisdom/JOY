# JayWisdom Identity Intel Update — 2026-06-10

## Purpose

Normalize fragmented intelligence from past conversation recall, external model output, and public-web style claims into a conservative project ledger.

This file does **not** crown unverified claims. It separates verified project memory, claimed external findings, conflicts, and next lawful verification actions.

## Operator Identity Lane

| Field | Value | Status |
|---|---|---|
| Root ENS | `jaywisdom.eth` | Known project identity |
| Base name | `jaywisdom.base.eth` | Known project identity |
| X handle | `@JayWisdom12` | Claimed social lane |
| GitHub | `jsonwisdom` | Active repo operator |
| Primary repo in this update | `jsonwisdom/JOY` | Active |
| Doctrine | `NO_FAKE_GREEN` | Active |

## Current Replay Evidence

### Independent Replay #2

| Field | Value |
|---|---|
| Canonical JSON | `{ "action": "verify", "operator": "jaywisdom.base.eth" }` compacted as `{"action":"verify","operator":"jaywisdom.base.eth"}` |
| Raw UTF-8 byte length | `51` |
| Hash domain | `SHA-256` via Python `hashlib` |
| Computed digest | `c1df26dd8432ce75739646fd7bae77ff9b67e20596924d0ef09f36165a2328f8` |
| Expected digest | `c1df26dd8432ce75739646fd7bae77ff9b67e20596924d0ef09f36165a2328f8` |
| Digest match | `TRUE` |
| Replay status | `COMPLETE` |

### Conservative Verdict

```txt
INDEPENDENT_REPLAY_2 = PASS
SHA256_REPRODUCIBLE = TRUE
DIGEST_MATCH = TRUE
BYTE_VERIFICATION = TRUE
ON_CHAIN_PROOF = PENDING
EXTERNAL_BINDING = PENDING
NO_FAKE_GREEN = ACTIVE
```

The replay proves deterministic bytes and digest reproduction for the named JSON payload. It does **not** by itself prove ENS ownership, EAS attestation, Zora deployment, GitHub custody, or any external object.

## Claimed External Intel — Not Yet Crowned

The following claims came from an external summarized search. They are recorded as leads, not proof.

| Claim | Value | Status |
|---|---|---|
| Farcaster profile | `cmptrwsdm` | Lead |
| Wallet attributed to Jay Wisdom | `0x38f52288dfd6184d3f516cc36521dd07faf6ef43` | Lead / requires direct verification |
| ENS active | `jaywisdom.eth` | Known identity lane, still verify current resolver when used |
| Base name | `jaywisdom.base.eth` | Known identity lane, still verify current resolver when used |
| Uniswap V4 / Base pool label | `node_state: alert coherence_anomaly: rising` | Lead / requires direct verification |
| Claimed pool ID/address | `0xf4640fb2b5546579b44abb6d52f94f57d1e2d37c9f053bee2e8f052d7c96a95b` | Lead / requires Base explorer or Uniswap verification |
| Claimed contract-like identifier | `0xefedc723a774ffcc9392d807393a21075292bec6fa95d70e5c9a4f3b918c7258` | Suspicious length for EVM address; likely not a normal 20-byte contract address |
| EAS attestations not found | `None found` | Conflicts with prior project memory; do not accept without direct EAS query |
| GitHub not found | No matching code confirmed by external search | False for current repo lane; `jsonwisdom/JOY` exists and is writable by operator |

## Known Conflict Flags

```txt
CLAIM_NO_EAS_FOUND = CONFLICTS_WITH_PRIOR_EAS_MEMORY
CLAIM_NO_GITHUB_FOUND = CONFLICTS_WITH_ACTIVE_REPO_ACCESS
CLAIM_SMART_CONTRACT_ADDRESS = FORMAT_SUSPICIOUS
CLAIM_POOL_ADDRESS = UNVERIFIED_LEAD
NO_FAKE_GREEN = ACTIVE
```

## Known Prior EAS Lane From Project Memory

The project memory contains prior EAS/Base references that must be verified directly before being used in a new public claim.

| Artifact | Value | Status |
|---|---|---|
| Base EAS contract | `0x4200000000000000000000000000000000000021` | Known Base EAS address; verify before execution |
| Base SchemaRegistry | `0x4200000000000000000000000000000000000020` | Known Base SchemaRegistry address; verify before execution |
| Prior live UID | `0x5a59e6b63c66057f71ee0bbe795a4d1eca98f22ee2b0bf811fa5b578ce2f6db7` | Prior memory; needs direct EAS lookup before reuse |
| Prior revoked/test UID | `0x805d1a372d3827e83a275981b207c9b8123e3270ee67a98d9d049f6ae417f92f` | Prior memory; needs direct EAS lookup before reuse |
| PR #315 UID | `0x499544987781f0797a6f3afa88108485e47fd3f3981ef52a71d5814514a07b4a` | Prior memory; needs direct EAS lookup before reuse |
| PR #315 tx | `0x677f8d1593eb0035784f05c37176b495708b37d75c9c9e19fc58ee5e37e0cfaf` | Prior memory; needs direct explorer lookup before reuse |
| PR #315 schema UID | `0x42670c7e031397a449248671b47902c1...` | Truncated in memory; must not reuse until complete UID is recovered |

## Open Gates

```txt
GATE_1_DIRECT_EAS_LOOKUP = PENDING
GATE_2_BASESCAN_WALLET_TRACE = PENDING
GATE_3_ENS_BASENAME_RESOLUTION_REFRESH = PENDING
GATE_4_GITHUB_ARTIFACT_INDEX = PENDING
GATE_5_ZORA_FACTORY_OBJECT_BINDING = PENDING
GATE_6_GPK_SECRET_FACTORY_OBJECT_BINDING = PENDING
GATE_7_ON_CHAIN_ATTESTATION_OF_REPLAY_2_DIGEST = PENDING
```

## Next Lawful Actions

1. Query EAS directly for known UIDs and wallet-linked attestations.
2. Resolve `jaywisdom.eth` and `jaywisdom.base.eth` fresh before public claims.
3. Check the claimed wallet `0x38f52288dfd6184d3f516cc36521dd07faf6ef43` on Base explorer.
4. Verify whether the claimed Uniswap V4 pool ID exists and what contract/token objects it references.
5. Build a GitHub artifact index for `jsonwisdom/JOY` covering PRs, commits, vectors, manifests, and replay receipts.
6. Bind Independent Replay #2 digest to a real object before any crown language.

## Current Factory State

```txt
L1_HYPOTHETICAL_GPK_SECRET_FACTORY = OPEN
L2_HYPOTHETICAL_ZORA_FACTORY = OPEN
INDEPENDENT_REPLAY_2 = PASS
REPLAY_DIGEST = c1df26dd8432ce75739646fd7bae77ff9b67e20596924d0ef09f36165a2328f8
EXTERNAL_BINDING = PENDING
ON_CHAIN_CLAIM = FALSE
NO_FAKE_GREEN = ACTIVE
```

## Operator Note

This update intentionally preserves uncertainty. The right move is not to erase conflicting intel, but to pin it in a reviewable file, mark the collision, and force direct lookup before public use.
