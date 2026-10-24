# AppleBlossomAwesome — Evidence Class Registry + LEAF → TREE → FOREST v0.1

## Purpose

Bridge the existing JoySpace Epistemic Receipt v0.1 into a Merkle Forest without collapsing provenance classes.

```text
RECEIPT
  ↓
EVIDENCE CLASS REGISTRY
  ↓
ROUTE | HOLD
  ↓
LEAF HASH
  ↓
ONE DOMAIN TREE ONLY
  ↓
TREE ROOT
  ↓
FOREST MANIFEST HASH
```

## Forest invariant

`FOREST_SHARED != ROOT_SHARED`

A receipt may participate in the same discoverable forest without inheriting the semantics, privacy, or authority of another tree.

## Root classes

| Manifest root | Evidence class |
|---|---|
| `family` | `PRIVATE_OR_APPROVED` |
| `alabama` | `PUBLIC_LOCAL` |
| `apple_blossom` | `BOUNDARY_RECEIPT` |
| `leah_prime` | `CREATIVE` |
| `public_research` | `PUBLIC_SOURCE` |

## Registry correction

The original sketch used source type, operation, and output-key voting as if they were sufficient to mutate a tree. v0.1 keeps those mappings as **HINT_ONLY** because they are useful suggestions but are not strong enough to silently cross a provenance membrane.

Automatic routing requires exactly one explicit EvidenceClass label in the existing `classifications[]` array of `schemas/joy/epistemic_receipt_v0_1.schema.json`.

- zero explicit root classes → `HOLD`
- one explicit root class → `ROUTE`
- conflicting explicit root classes → `HOLD`

This means BoxDee can inspect the receipt and the Registry can route it without manufacturing a class from weak context.

## Two different weights

`routing_confidence` measures classification agreement only. It does **not** mean probability that a claim is true.

`evidence_weight` measures process completeness:

- `0 / UNBOUND` — receipt exists but no bound source + BIND move
- `1 / SOURCE_BOUND` — source pointer exists and BIND occurred
- `2 / REPLAYED` — source pointer exists and both BIND + REPLAY occurred

A replay that ends in `CONFLICT` can still have weight `REPLAYED`. Failure is evidence too.

## Hashing

All hashes are SHA-256 with explicit domain separation and length-prefixing.

- Receipt leaf: `JOY_LEAF_V0_1`
- Merkle pair: `JOY_MERKLE_NODE_V0_1`
- Odd-node promotion: `JOY_MERKLE_PROMOTE_V0_1`
- Empty body: `JOY_MERKLE_EMPTY_V0_1`
- Class-bound tree root: `JOY_TREE_ROOT_V0_1`
- Forest manifest: `JOY_FOREST_MANIFEST_V0_1`

The tree root binds the evidence class, leaf count, and Merkle body root. Odd nodes are promoted with a separate domain rather than duplicated, avoiding the common `[A,B,C]` vs `[A,B,C,C]` duplicate-last ambiguity.

The `forest_manifest_hash` is computed over canonical JSON of the manifest with the hash field removed.

## Mutation rule

A successful route is allowed to mutate exactly one domain root. The implementation snapshots every root before routing and raises if more than the selected root changes.

```text
ROOT_MUTATIONS_PER_RECEIPT <= 1
CROSS_TREE_INFERENCE       = FALSE
SHARED_AUTHORITY           = FALSE
AUTHORITY_CREATED          = FALSE
```

Duplicate leaf insertion is a no-op and does not increment `leaf_count`.

## Alabama Jamma Slamma test

The test suite routes a `BOUNDARY_RECEIPT` into `apple_blossom`, then a `PUBLIC_LOCAL` receipt into `alabama`, and proves the first tree root stays unchanged. A conflicting receipt is held with zero forest mutation.

Run:

```bash
python -m unittest tests/test_evidence_forest_v0_1.py -v
```

## Next gate

`Replay Collision Matrix` can now operate on classified roots. It should consume root classes and interaction rules; it must not rewrite receipt classification or merge roots.
