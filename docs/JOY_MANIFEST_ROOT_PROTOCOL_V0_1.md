# JOY Manifest Root Protocol v0.1

JOY is the semantic memory and human continuity surface for the ReceiptOS universe. It records doctrine, receipts, and manifests without claiming cryptographic truth or performing verification.

This protocol defines how JOY collections become stable, Merkle-ready snapshots that ReceiptOS can later verify.

## Leaves and leaf qualification

In JOY, a **leaf** is a canonical, machine-readable artifact that represents a specific semantic unit of continuity. Examples include:

- A Receipt Chain Link manifest (such as `WISDOM/receipt_chain_link_v0_1.manifest.json`).
- Future family receipt manifests that describe human events, roles, and doctrine.
- Other JOY manifests that are explicitly declared as leaves.

A leaf must:

- Be stable and versioned (no silent mutation).
- Be semantically complete for its scope.
- Respect JOY’s authority boundary (`authority=false`, `execution=false`, `verification=false`).

Leaves are not cryptographic proofs; they are structured semantic records.

## Role of leaves.sha256

`leaves.sha256` is the JOY ledger of leaf digests. It records the SHA-256 hashes of leaf artifacts as they exist at a given point in time.

Within JOY:

- `leaves.sha256` is a **semantic index of digests**, not a claim of verification.
- It allows deterministic reconstruction of which leaf versions participated in a snapshot.
- It provides the input material that ReceiptOS can later use to compute and verify Merkle roots.

JOY records the digests; it does not assert that they are correct or verified. Any cryptographic meaning is deferred to ReceiptOS.

## Manifest snapshots

A **manifest snapshot** is a JOY-level description of a set of leaves and their digests at a specific moment. It represents:

- Which leaf manifests are included.
- How many leaves participate (`leaf_count`).
- The relationship between the snapshot and `leaves.sha256`.
- A candidate Merkle root value, if one has been computed.

The snapshot is **semantic**: it says “this is the set of artifacts we consider together,” not “this set is cryptographically verified.”

## Receipt Chain Link manifests as leaves

Receipt Chain Link manifests, such as `WISDOM/receipt_chain_link_v0_1.manifest.json`, participate as leaves when:

- They are included in `leaves.sha256`.
- They are referenced in a manifest root’s `leaf_manifest` collection.
- Their schema (for example, `schemas/joy/receipt_chain_link_v0_1.schema.json`) is satisfied.

This allows family game night receipts and similar doctrine to be part of a larger continuity snapshot without changing their semantic meaning or authority boundary.

## Future family receipts as leaves

Future family receipts can join the leaf set when they:

- Have a JOY manifest that captures roles, surfaces, and doctrine.
- Are hashed and recorded in `leaves.sha256`.
- Are referenced by a manifest root as part of `leaf_manifest`.

This keeps the family continuity model extensible: new events and receipts can be added as leaves without altering the existing chain.

## Candidate Merkle roots

From a manifest snapshot, ReceiptOS (or another cryptographic process) may compute a Merkle root over the leaf digests. JOY records this as a **candidate root**:

- The `candidate_root` field is informational only.
- It indicates a value that may later be verified by ReceiptOS.
- It does not, by itself, assert correctness, integrity, or trust.

A candidate root becomes meaningful only when ReceiptOS performs verification and records the result in its own domain.

## JOY’s non-verification boundary

JOY must not verify Merkle roots or any other cryptographic property. The boundary is explicit:

- JOY records semantic continuity.
- JOY organizes leaves and snapshots.
- JOY may store candidate root values.

But JOY:

- Does **not** claim that a candidate root is correct.
- Does **not** perform cryptographic verification.
- Does **not** upgrade semantic artifacts into “truth.”

## ReceiptOS verification role

ReceiptOS is responsible for:

- Computing Merkle roots from the digests recorded in `leaves.sha256`.
- Verifying those roots against canonical artifacts.
- Recording verification results and trust decisions.

The JOY Manifest Root Protocol exists so that ReceiptOS can:

- Reliably reconstruct the leaf set for a snapshot.
- Trust that JOY has not silently mutated the semantic artifacts.
- Apply its own cryptographic and procedural checks.

JOY organizes semantic continuity; ReceiptOS verifies canonical artifacts; AL consumes verified artifacts. Each layer stays within its authority boundary.
