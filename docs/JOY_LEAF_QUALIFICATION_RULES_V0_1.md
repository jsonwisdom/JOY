# JOY Leaf Qualification Rules v0.1

JOY is the semantic continuity layer for human-safe doctrine, receipts, and manifests.  
It records meaning, not cryptographic truth.  
Leaf qualification ensures that only stable, boundary-aligned artifacts enter `leaves.sha256` and later manifest root snapshots.

## Purpose of Leaf Qualification

Leaf qualification prevents drift, mutation, and accidental authority by defining what may become a JOY leaf.  
A leaf is the smallest canonical semantic unit eligible for hashing and inclusion in future manifest roots.

JOY does **not** verify cryptographic truth.  
ReceiptOS performs verification later.  
AL consumes verified artifacts downstream.

## What qualifies as a JOY leaf

A JOY leaf must:

- Be **semantic**, not executable.
- Be **stable**: no silent mutation, versioned, and replayable.
- Be **human-safe**: no automation triggers, no execution semantics.
- Be **boundary-explicit**:  
  - `authority=false`  
  - `execution=false`  
  - `verification=false`
- Preserve unknowns: **unknowns stay unknown**.
- Avoid false signals: **no fake green**.
- Be represented as a **canonical JSON manifest** or other explicitly declared leaf format.

Examples of valid leaves:

- Receipt Chain Link manifests  
- Family receipt manifests  
- JOY doctrine manifests  
- Future continuity manifests that meet all boundary rules

Invalid leaves:

- Runtime code  
- Automation triggers  
- Cryptographic claims  
- Anything asserting verification  
- Anything implying authority or execution  
- Anything that mutates silently or cannot be replayed

## Relationship to leaves.sha256

`leaves.sha256` is the digest ledger for qualified leaves.

JOY uses it to:

- Record canonical digests of leaf artifacts  
- Provide deterministic input for manifest root snapshots  
- Allow ReceiptOS to reconstruct and verify Merkle candidates later

JOY does **not** claim that digests are correct or verified.  
It only records them.

## Leaf participation in manifest roots

Qualified leaves may be included in:

- Manifest root snapshots  
- Family continuity snapshots  
- Future JOY semantic collections

A leaf’s inclusion means:

- “This artifact is part of the semantic continuity set.”

It does **not** mean:

- “This artifact is cryptographically verified.”  
- “This artifact is authoritative.”  
- “This artifact triggers execution.”

## Boundary statement

JOY records semantic continuity.  
ReceiptOS verifies canonical artifacts.  
AL consumes verified artifacts.

Leaf qualification ensures JOY stays within this boundary.
