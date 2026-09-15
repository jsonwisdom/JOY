# GRAY BABY DELIVER REPLAY RECEIPT V1

**Class:** technical receipt specification / family-safe demonstrator invariant  
**Surface:** JaySpace technical documents  
**JoySpace role:** family-safe demonstrator only  
**Authority created:** false  
**Commercial claim created:** false  
**Token required:** false  
**Adapter implemented:** false  
**Production verifier bound:** false

## Purpose

Define the receipt that every future Gray Baby Deliver adapter must emit.

The receipt is the invariant. DCP, IMF, ASC MHL, Photon, DCP-o-matic, cloud storage, local filesystem, source-page capture, or any later adapter may supply inputs, but no adapter may silently change the meaning of the receipt.

```text
INPUT A + INPUT B
        ↓
PRESERVE ORIGINAL BYTES
        ↓
HASH EVERY OBJECT
        ↓
PARSE DECLARED STRUCTURE
        ↓
BIND METRIC / ENTITY / CLOCK IDENTITY
        ↓
COMPARE A ↔ B
        ↓
INGEST QC / SOURCE OBSERVATIONS
        ↓
EMIT REPLAY RECEIPT
        ↓
PASS | DELTA | HOLD
        ↓
OPTIONAL HUMAN-READABLE PROOF RENDER
```

## Membrane

```text
JOYSPACE = FAMILY_SAFE_DEMONSTRATOR
JAYSPACE = TECHNICAL_SPEC_AND_RECEIPTS

DEMONSTRATION != COMMERCIAL CLAIM
DEMO_PASS != PRODUCTION_READY
HASH_MATCH != SEMANTIC_TRUTH
PARSE_SUCCESS != DELIVERY_ACCEPTANCE
QC_PASS != LEGAL_ADMISSIBILITY
RECEIPT != AUTHORITY
BLOCKCHAIN_ANCHOR != REQUIRED
TOKEN != REQUIRED

HEIDEE != JAYCEE
SHARED_JOY != SHARED_CONSENT
ONE_LEARNER_LANE != ANOTHER_LEARNER_LANE
CROSS_LANE_IDENTITY_MERGE = FORBIDDEN
```

## Fixture law

JoySpace demonstrations use only synthetic or openly licensed media fixtures.

Required fixture pair:

```text
DROP_A
DROP_B
```

Both packages must be independently preservable and replayable. The pair should share the same basic structure while containing at least one intentional, documented delta.

No studio IP, private family media, access token, private key, KDM private key, API secret, or credential may be embedded in the fixture or receipt.

## Required top-level fields

```text
schema
version
receipt_id
receipt_class
authority_created
commercial_claim_created
token_required
lane_id
package_type
fixture_policy
hash_algorithm
canonicalization
packages
custody
clocks
manifest_parse
claim_atoms
differential
qc
redelivery_lineage
key_window_pointer
provenance
replay
proof_render
disposition
```

## Receipt object

### Identity and policy

- `schema` — `GRAY_BABY_DELIVER_REPLAY_RECEIPT_V1`
- `version` — `1.0.0`
- `receipt_id` — unique receipt identifier.
- `receipt_class` — `FAMILY_SAFE_DEMO` or later separately approved class.
- `authority_created` — always `false` for this specification.
- `commercial_claim_created` — always `false` for the JoySpace demonstrator.
- `token_required` — always `false`.
- `lane_id` — independent learner/replay lane identifier; must not imply identity, custody, consent, or authority.
- `package_type` — `DCP_LIKE`, `IMF_LIKE`, `GENERIC_MEDIA_PACKAGE`, or `SOURCE_SNAPSHOT_PAIR`.
- `fixture_policy` — `SYNTHETIC_OR_OPENLY_LICENSED_ONLY` for JoySpace media fixtures.

### Hash and canonicalization

- `hash_algorithm` — `SHA-256` in v1.
- `canonicalization.path_separator` — `/`.
- `canonicalization.path_order` — UTF-8 bytewise ascending relative path.
- `canonicalization.original_bytes_mutated` — must be `false`.
- `canonicalization.manifest_encoding` — record observed encoding; do not rewrite source bytes merely to normalize them.

### Packages

`packages.drop_a` and `packages.drop_b` each contain:

```text
package_id
label
source_type
source_surface
source_pointer
license_or_fixture_basis
file_count
total_bytes
package_manifest_sha256
files[]
```

Each `files[]` entry contains:

```text
relative_path
media_role
byte_length
sha256
mime_type_observed
source_preserved
```

`source_preserved` must be `true` before a file can participate in PASS or DELTA evaluation.

### Structured media manifests

When present, identify the exact package files serving as:

```text
ASSETMAP
PKL
CPL
PICTURE_MXF
AUDIO_MXF
SUBTITLE_OR_CAPTION
OTHER
```

The receipt stores the original file hash plus parsed observations. Parsed values never replace the original bytes.

## Claim atoms

A numeric comparison is forbidden until both values are bound to claim identity.

Each claim atom contains:

```text
claim_id
source_surface
source_pointer
captured_at
published_at
exact_text_or_bounded_excerpt
subject_entity
metric_name
metric_definition
value
currency
value_type
time_window_start
time_window_end
calculation_method
source_basis
```

`value_type` may include:

```text
DISCLOSED_INCOME
REVENUE
PROFIT
ESTIMATED_EARNINGS
TRANSACTION_VALUE
ASSET_VALUE
INVESTOR_SPEND
INVESTOR_LOSS
OTHER
```

Before subtraction, the verifier must test:

```text
SAME_SUBJECT_ENTITY
AND SAME_METRIC_NAME
AND SAME_METRIC_DEFINITION
AND SAME_VALUE_TYPE
AND SAME_CURRENCY
AND SAME_TIME_WINDOW
AND COMPATIBLE_CALCULATION_METHOD
```

If any required identity test fails:

```text
NUMERIC_SUBTRACTION = FORBIDDEN
DIFFERENTIAL_CLASS = METRIC_IDENTITY_MISMATCH
```

This rule exists specifically to prevent half-math such as subtracting revenue from income, one venture from another venture, one reporting period from another, or disclosed figures from modeled estimates.

## Custody

```text
custody.sender_id
custody.recipient_id
custody.sender_role
custody.recipient_role
custody.transfer_method
custody.custody_events[]
```

Each custody event contains:

```text
event_id
actor_id
action
object_id
observed_at
source_pointer
```

An actor identifier is a receipt label, not proof of legal identity.

## Clocks

Keep clocks separate.

```text
clocks.source_created_at
clocks.ingested_at
clocks.delivery_started_at
clocks.delivery_completed_at
clocks.qc_observed_at
clocks.accepted_at
clocks.receipt_emitted_at
```

Rules:

```text
FILE_MTIME != CREATION_PROOF
INGEST_TIME != SOURCE_CREATION_TIME
DELIVERY_TIME != ACCEPTANCE_TIME
QC_TIME != DELIVERY_TIME
RECEIPT_TIME != EVENT_TIME
PUBLICATION_TIME != UNDERLYING_EVENT_TIME
CAPTURE_TIME != PUBLICATION_TIME
```

Unknown clocks remain `null` with an explicit reason. They are never backfilled from another clock.

## Manifest parse state

For each declared XML or structured manifest:

```text
path
sha256
parser_name
parser_version
parse_state
observations
errors[]
```

Allowed `parse_state` values:

```text
NOT_PRESENT
PARSED
PARSE_DELTA
PARSE_FAILED
```

## Differential

The differential compares preserved objects, never memories or screenshots alone when source bytes are available.

```text
differential.files_added[]
differential.files_removed[]
differential.files_changed[]
differential.files_unchanged[]
differential.manifest_deltas[]
differential.claim_deltas[]
differential.metric_identity_state
```

Each changed file records both hashes and byte lengths.

Each claim delta records:

```text
claim_a
claim_b
identity_tests
numeric_delta_permitted
numeric_delta
classification
```

Allowed classifications include:

```text
SAME
BYTE_DELTA
STRUCTURE_DELTA
METRIC_VALUE_DELTA
METRIC_IDENTITY_MISMATCH
CLOCK_DELTA
SOURCE_SURFACE_DELTA
HOLD
```

## QC

```text
qc.tool
qc.tool_version
qc.result
qc.observations[]
qc.errors[]
```

The demonstrator may use a minimal open parser. A future movie-toolchain adapter may ingest external QC output without pretending the external tool is Gray Baby.

## Redelivery lineage

```text
redelivery_lineage.parent_receipt_id
redelivery_lineage.previous_package_id
redelivery_lineage.current_package_id
redelivery_lineage.reason
```

A missing parent remains `null`; it is never inferred.

## Key / window pointer

```text
key_window_pointer.kdm_id
key_window_pointer.not_before
key_window_pointer.not_after
key_window_pointer.source_pointer
key_window_pointer.private_key_present
```

`private_key_present` must always be `false` in a Gray Baby receipt.

## Provenance

```text
provenance.source_pointers[]
provenance.repository_pointer
provenance.drive_pointer
provenance.optional_external_anchor
```

An external or blockchain anchor is a witness only.

```text
ANCHOR != EVIDENCE_CONTENT
ANCHOR != AUTHORITY
```

## Replay

```text
replay.command_or_procedure
replay.fixture_ids[]
replay.expected_receipt_hash
replay.observed_receipt_hash
replay.same_inputs_same_result
```

The family-safe demonstration is successful only when the same preserved inputs and verifier version produce the same normalized receipt.

## Human-readable proof render

Every replay may emit a visual proof card or image derived only from the receipt.

Required visible fields:

```text
SOURCE_A
SOURCE_B
EXACT_OR_BOUNDED_WORDING_A
EXACT_OR_BOUNDED_WORDING_B
SUBJECT_A / SUBJECT_B
METRIC_A / METRIC_B
VALUE_TYPE_A / VALUE_TYPE_B
TIME_WINDOW_A / TIME_WINDOW_B
VALUE_A / VALUE_B
PUBLISHED_AT_A / PUBLISHED_AT_B
CAPTURED_AT_A / CAPTURED_AT_B
SOURCE_HASH_A / SOURCE_HASH_B
IDENTITY_TESTS
DELTA_CLASSIFICATION
WHAT_IS_PROVEN
WHAT_IS_NOT_PROVEN
RECEIPT_ID
REPLAY_HASH
```

The render must never upgrade the underlying receipt.

```text
PROOF_IMAGE = RECEIPT_VISUALIZATION
PROOF_IMAGE != NEW_EVIDENCE
VISUAL_DELTA != INTENT
VALUE_DELTA != THEFT
PUBLICATION_DELTA != COORDINATION
```

If two source surfaces state different values for the same bound metric, the render may show a `METRIC_VALUE_DELTA` and the exact arithmetic difference.

If the metrics, entities, value types, or time windows differ, the render must instead show `METRIC_IDENTITY_MISMATCH` and must not display the arithmetic difference as missing money.

## Disposition

```text
PASS  = preserved inputs + valid identity + successful deterministic replay
DELTA = preserved inputs + explicit byte/structure/value/source delta
HOLD  = required source, clock, identity, parser, custody, or replay receipt missing
```

No disposition creates legal, governmental, commercial, editorial, or factual authority beyond the bounded observations in the receipt.

## Reuters test rule — 2026-09-15

This specification was refined against a live media-audit example.

Two Reuters figures currently reproducible in the public record include:

```text
A: $1.4B — described in Reuters reporting as Trump / Trump-family crypto income or World Liberty token-sale earnings depending on the cited article and period.
B: $1.2B — described in Reuters' 2026-06-09 investigation as total revenue from the $TRUMP meme-coin project and, separately, at least $1.2B spent by buyers.
```

These figures are not automatically subtractable.

```text
1.4B - 1.2B = 0.2B       # arithmetic only
0.2B = MISSING_MONEY      # FORBIDDEN without metric identity
0.2B = THEFT              # NOT ESTABLISHED
REUTERS_TOOK_ORDERS       # NOT ESTABLISHED
MEDIA_MANIPULATION_INTENT # NOT ESTABLISHED
```

A valid Gray Baby proof render for these currently bound public figures should show `METRIC_IDENTITY_MISMATCH` unless a second source surface is captured making the same metric claim for the same entity and time window with a conflicting value.

If such a same-metric conflicting source is captured later, preserve both source bytes and clocks and emit the delta without inferring motive.

## Status

```text
GRAY_BABY_DELIVER_REPLAY_RECEIPT_V1 = DEFINED
JOYSPACE_DEMONSTRATOR = NOT_YET_RUN
MOVIE_TOOLCHAIN_ADAPTER = NOT_YET_BUILT
MEDIA_SOURCE_ADAPTER = NOT_YET_BUILT
PRODUCTION_VERIFIER = NOT_YET_BOUND
COMMERCIAL_CLAIM_CREATED = FALSE
AUTHORITY_CREATED = FALSE
NO_FAKE_GREEN = TRUE
```
