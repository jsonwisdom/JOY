# FULLMATHGITHUB → Public Site Sync V0.1

```text
CLASS = HUMAN_DEFENSIBLE_PUBLIC_SYNC_SCAFFOLD
STATE = YELLOW_BUILDABLE
AUTHORITY_CREATED = false
IDENTITY_COLLAPSE = false
PUBLIC_PROMOTION = blocked_until_public_proof
SOURCE_MUTATION = false
```

## Purpose

Make Jason's observable work fast for machines to inventory and easy for a human to defend.

FULLMATHGITHUB does not decide who a human is. It preserves source evidence, computes relationships, exposes what is proven, and leaves unresolved joins visible.

The public site is a projection of evidence. It is not the authority that created the evidence.

## Centered-of-Self rule

The human remains the decision center.

```text
HUMAN -> PURPOSE -> WORK -> SOURCE -> RECEIPT -> REPLAY -> PUBLIC PROJECTION
```

Machines may accelerate the path after PURPOSE. They may not replace the HUMAN node or manufacture PURPOSE.

## Functions

### F1 — INVENTORY

Discover allowed repositories, public pages, Zora objects, wallet-role records, receipts, commits, timestamps, images, and generated reports.

Output:

```text
object_id
source_system
source_repo
source_path
source_commit
source_timestamp
content_hash
purpose_hint
status
```

### F2 — NORMALIZE

Represent each object in a common envelope without rewriting the original bytes.

```text
NORMALIZED_OBJECT != SOURCE_OBJECT
NORMALIZATION != MUTATION
```

### F3 — PROVENANCE

Bind every public statement to the smallest available receipt.

Required fields where available:

- source URI/path
- source commit
- author timestamp
- committer timestamp
- source-created timestamp
- SHA-256
- receipt reference
- public URL

Missing evidence remains missing.

```text
MISSING != ZERO
UNKNOWN != FALSE
CORRELATION != CAUSATION
```

### F4 — PURPOSE GATE

Classify the observed role without collapsing wallet, signer, repo, or person.

Known project role classes may include:

- CONSTITUTIONAL / NAME / RECEIPT
- ZORA / CREATOR / PUBLICATION
- UNI / MARKET / ROUTING
- SIGNER / CONTROL
- JAYSPACE / TECHNICAL STORY
- JOYSPACE / PUBLIC-SAFE DEMONSTRATOR

Role classification is evidence metadata, not identity proof.

### F5 — FULLMATH

Compute reproducible quantities such as:

```text
COUNT
DISTINCT_COUNT
SUM
DIFFERENCE
RATIO
DENSITY
TIME_DELTA
PAIRWISE_MAX = n(n-1)/2
HASH
MERKLE_ROOT
```

Math results must expose their inputs.

```text
RESULT_WITHOUT_INPUTS = NOT_DEFENDABLE
```

### F6 — SPLIT

Any unresolved or restricted object becomes a child lane rather than disappearing.

Triggers include:

- HOLD
- MISSING_EVIDENCE
- CLOCK_CONFLICT
- AUTHORITY_CLAIM_CONFLICT
- IDENTITY_JOIN_UNRESOLVED
- PUBLIC_BYTE_MISMATCH

```text
SPLIT != DELETE
HOLD != FAILURE
REPORT_BACK != PROMOTION
```

### F7 — BUILD

Create a public-safe projection from normalized evidence.

Build may generate:

- timeline
- searchable inventory
- proof cards
- purpose maps
- wallet-role graph
- Zora inventory
- image gallery
- source receipts
- machine-readable JSON
- Merkle batch manifest

Build does not by itself make the public site GREEN.

### F8 — PUBLIC PROOF

For a public route to become GREEN:

```text
PUBLIC_GREEN =
    HTTP_200
  + REQUIRED_MARKER
  + SHA256_REPO_SOURCE_EQUALS_PUBLIC_BODY
  + PRIVACY_CHECK
  + HUMAN_VISUAL_CONFIRM
```

Where exact byte equality is structurally impossible because a build transforms source files, use a signed/hash-bound deployment manifest that binds input hashes to the exact built output hash. Never pretend transformed output is byte-identical source.

### F9 — REPORT BACK

Every sync run emits a receipt back to JaySpace.

```text
SOURCE -> NORMALIZED OBJECT -> BUILD -> PUBLIC CHECK -> RECEIPT -> JAYSPACE
```

The source rail remains sovereign.

### F10 — HUMAN APPROVAL

The human receives a compact review surface showing:

- what changed
- source evidence
- hashes
- HOLDs
- public status
- unresolved joins
- proposed next action

No wallet transaction, token approval, authority change, or identity promotion is implied by public-site synchronization.

## Machine-speed state model

```text
DISCOVERED
SOURCE_BOUND
HASHED
NORMALIZED
RECEIPT_BOUND
BUILT
HTTP_200
PUBLIC_HASH_BOUND
HUMAN_CONFIRMED
HOLD
```

State transitions are append-only observations. Later states do not rewrite earlier evidence.

## HisStory

HisStory is an append-only replay lane.

Each event may point backward to a prior event, but the timeline does not infer authorship or causation from timestamp proximity.

```text
SAME_DAY != SAME_EVENT
ORDERED_BY_TIME != CAUSED_BY
COMMIT_TIME != HUMAN_AUTHORED_AT
```

## Base anchoring

FULLMATHGITHUB may prepare Merkle batches of public-safe event hashes.

```text
event bytes -> SHA256 leaf
leaves -> Merkle root
Merkle root -> Base anchor candidate
```

Creating the candidate is machine work.

Submitting a transaction is a separate human-authorized operation.

```text
BUILD_ANCHOR_CANDIDATE = allowed
SUBMIT_BASE_TRANSACTION = human_gate
```

## Public sync contract

The public site consumes only generated public-safe outputs.

Recommended surface:

```text
public/fullmath/
  manifest.json
  inventory.json
  timeline.json
  holds.json
  purpose-map.json
  provenance.json
  latest-receipt.json
```

Each output carries:

```text
schema
generated_at
source_commit_set
source_hash_set
build_commit
content_hash
authority_created=false
identity_join=false
promotion
```

## Constitutional boundary

```text
HUMAN_DEFENDABLE = evidence can be replayed by a person
PROVABLE = claim has bounded source support
ASSESSABLE = state and uncertainty are machine-readable
MACHINE_SPEED = automation accelerates evidence handling

MACHINE_SPEED != MACHINE_AUTHORITY
PUBLIC_SITE != HUMAN_IDENTITY
WALLET != HUMAN
SIGNER != HUMAN
REPO != HUMAN
HASH != TRUTH
RECEIPT != AUTHORITY
```

## Stop gate

V0.1 stops after inventory, normalization, build, and public-proof assessment.

```text
AUTO_DEPLOY = false
AUTO_SIGN = false
AUTO_TRADE = false
AUTO_APPROVE = false
AUTO_PROMOTE_IDENTITY = false
```

Promotion and Base submission require explicit later gates.
