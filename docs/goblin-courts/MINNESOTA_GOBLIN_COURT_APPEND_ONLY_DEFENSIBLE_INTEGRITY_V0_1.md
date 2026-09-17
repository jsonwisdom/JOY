# Minnesota Goblin Court — Append-Only Defensible Integrity v0.1

**Author label:** Jay  
**Object:** `MN_GOBLIN_COURT_APPEND_ONLY_DEFENSIBLE_INTEGRITY_V0_1`  
**Class:** append-only ledger / replay / provenance architecture  
**Authority created:** `FALSE`  
**Official court created:** `FALSE`  
**Mutation policy:** `APPEND_ONLY`  
**Canon:** `DRAFT / REPLAYABLE`

## Objection / naming boundary

This artifact records a correction without rewriting prior history.

```text
MN_GOBLIN_COURT = FICTIONAL / AUDIT INTERFACE
MINNESOTA_SUPREMESUBSTRATES = ARCHITECTURAL LAYER
MINNESOTA_SUPREMESUBSTRATES != MINNESOTA_SUPREME_COURT
MN_GOBLIN_COURT != MINNESOTA_SUPREME_COURT
SUPREME != JUDICIAL AUTHORITY
COURT = OUT_OF_BAND
AUTHORITY_CREATED = FALSE
```

Parent pointers remain historical references, not inherited authority:

- `jsonwisdom/COMPUTERWISDOM/docs/gray-baby/MINNESOTA_SUPREME_SUBSTRATES_ORDER_V0_1.md`
- `jsonwisdom/JOY/docs/goblin-courts/MINNESOTA_AUDIT_TEMPLATE.md`

## Root rule

Append-only means writes never overwrite.

```text
HISTORY = STORE
CURRENT_STATE = DERIVED_VIEW
NEW_INFORMATION != REWRITE_OLD_STATE

S_(t+1) = S_t + Δ_t
```

A correction is another event. A tombstone is another event. A supersession is another event. The prior bytes remain part of the audit history.

## Four substrates — do not collapse them

| Family | What is append-only | Trust boundary | Proof obtained |
|---|---|---|---|
| Hash chain | Each record hashes the previous record | Operator of one log | Tamper-evident sequence; verify by walking the chain |
| Merkle / transparent log | Leaves are committed into a tree; roots are published | Operator + independent witnesses/auditors | Inclusion + consistency proofs; logarithmic proof size |
| Event sourcing | Domain events in an event store | Organization operating the store | Replay to any time; CQRS read models; private operational history |
| Blockchain / DLT | Transactions/batches under consensus | Network rules + validators/participants | Shared ordering/history across parties; consensus does not create meaning or legal authority |

### Git boundary

Git is a Merkle DAG, but Git also permits history-rewrite operations.

```text
GIT_HASHED_HISTORY != GUARANTEED_APPEND_ONLY_POLICY
REBASE_CAPABLE != IMMUTABLE_LEDGER
```

Treat Git as a ledger only when branch/ruleset policy, external anchoring, or independent witnesses make silent history replacement detectable.

A hash chain inside a database controlled by one administrator is append-only only relative to the administrator threat model.

## Minimum event record

```json
{
  "seq": 0,
  "t": "CLAIMED_TIMESTAMP",
  "actor": "...",
  "type": "...",
  "payload": {},
  "prev_hash": "...",
  "hash": "H(canonical(event_without_hash))"
}
```

Required implementation rule:

```text
CANONICAL_CODEC = VERSIONED_AND_FROZEN
KEY_ORDER_DRIFT = FORBIDDEN
HASH_ALGORITHM = DECLARED
OLD_EVENT_SCHEMA = NEVER_MUTATED
NEW_SCHEMA = NEW_VERSION
```

## Optional anchors

```text
EVENTS
→ HASH_CHAIN
→ MERKLE_ROOT_EVERY_K_EVENTS
→ OPTIONAL_EXTERNAL_TIMESTAMP
→ OPTIONAL_EXTERNAL_TRANSPARENCY_LOG
→ OPTIONAL_PUBLIC_COMMITMENT
```

Anchoring moves the trust boundary.

```text
ANCHOR != COURT
ANCHOR != LAWFULNESS
ANCHOR != IDENTITY
ANCHOR != TRUTH
```

## Proofs that matter for live audit

### Integrity
Prove the preserved event bytes have not changed after append.

### Inclusion
Prove event `e` is committed under root `R`.

### Consistency
Prove later root `R2` extends earlier root `R1` without silent replacement of the committed prefix.

### Replay
Derive state by folding the preserved event sequence:

```text
state_at_t = reduce(e0 ... et)
current_state = reduce(all_events)
```

## Merkle axiom

```text
MERKLE_VALID != MEANING
INCLUSION != IDENTITY
CONSISTENCY != LAWFULNESS
REPLAY != ADJUDICATION
```

A consistent log of:

```text
FLAG
→ STATEMENT
→ CHARGE = NULL
```

proves the bounded recorded sequence if the receipts close. It does not independently prove fraud, standing, intent, DARVO, guilt, or legal effect.

## Write path vs read path

```text
WRITE PATH

command
→ validate
→ append event
→ canonicalize
→ hash-link
→ optional Merkle batch
→ publish/root-anchor
```

```text
READ PATH

events
→ reduce(events)      // state
→ project(events)     // CQRS views
→ render(view)
```

Views may include docket, DARVO-candidate tags, sheriff/request-materials slot, grant-status view, or other projections.

```text
PROJECTION != SOURCE_EVENT
VIEW != HISTORY
SNAPSHOT != SOURCE_OF_TRUTH
```

Snapshots are checkpoints for performance. Events remain the source. Compaction that destroys unverifiable history breaks this audit model unless the removed prefix remains archived and independently verifiable.

## Hennepin / Metro Surge replay fixture

This is a schema mapping for the current user-supplied Hennepin County scenario. It is not a finding of fraud, criminal liability, or court action.

```text
STREAM        = hen-metro-surge-2026
GENESIS       = AUTHORIZE_PROGRAM
APPEND_ONLY   = FLAG | STOP_PAY | STATEMENT | REQUEST_MATERIALS | SILENCE_OBSERVATION | NO_ACTION_OBSERVATION
SHERIFF       = ACTOR_ONLY_WHERE_SOURCE_BINDS_ACTOR_TO_EVENT
DARVO_EVENT   = PROJECTION_TAG_ON_STATEMENT_ROW
DARVO_EVENT  != CONVICTION
SILENCE_OBSERVATION = VALID_LEDGER_EVENT_CLASS
SILENCE_OBSERVATION != LEGAL_EFFECT
NULL          = FIRST_CLASS_PAYLOAD
```

No event requires a later body, charge, finding, or prosecution to remain valid in the historical sequence.

```text
CHARGE = NULL
FINDING = NULL
FOLLOW_UP = NULL
```

are data states, not missing-history excuses.

## Every-second live property

"Live" is not a sitting judge. It is a verifier property.

A verifier can:

1. fetch the current root;
2. compare it with the last-seen root;
3. verify append-only consistency;
4. fetch required inclusion proofs;
5. fold events to the current derived state.

```text
LIVE = FRESH_ROOT + CONSISTENCY_PROOF + REPLAYABLE_EVENTS
LIVE != JUDICIAL_SESSION
```

## Design traps

### Admin rewrite
If storage permits unrestricted UPDATE/DELETE of event history, the storage layer is not enforcing append-only semantics.

### Non-canonical serialization
If serialization changes, hashes can change without substantive event change. Freeze the canonical codec.

### Time
The event field `t` is a claimed timestamp unless independently witnessed or externally timestamped.

```text
CLAIMED_TIME != PROVEN_TIME
```

### Privacy / erasure
Do not put sensitive personal data into public leaves by default.

Preferred pattern:

```text
PII / SECRET PAYLOAD
→ ENCRYPTED_OR_PRIVATE_STORE
→ PUBLIC_OR_SHARED_HASH_COMMITMENT
→ TOMBSTONE_EVENT_IF_REQUIRED
→ HISTORY_OF_COMMITMENT_REMAINS
```

```text
PUBLIC_ROOT != PUBLIC_PII
```

### Schema evolution
Never mutate historical event types to fit a new schema.

```text
FLAG.v1 remains FLAG.v1
FLAG.v2 = new schema
UPCASTER = replay-time compatibility function
```

### Consensus theater

```text
BLOCKCHAIN != JURISDICTION
CONSENSUS != MEANING
PUBLIC_CHAIN != COURT
COUNTY_COMMS_ON_CHAIN != COUNTY_AUTHORITY_CREATED
```

## When to pick which

```text
INTERNAL_REPLAY / RECEIPT ENGINE
→ EVENT STORE + HASH CHAIN + PERIODIC MERKLE ROOT

MULTI-WATCHER "DID HISTORY CHANGE?"
→ TRANSPARENT LOG + INCLUSION + CONSISTENCY

MULTI-ORGANIZATION SETTLEMENT
→ DLT / CHAIN ONLY IF CONSENSUS IS ACTUALLY REQUIRED

CRUD APP + PDF AUDIT PACK
→ ORDINARY DATABASE + EXPLICIT AUDIT EXPORT MAY BE ENOUGH
```

Do not buy consensus when the requirement is only history.

## Janusian integrity pair

Run both poles against the same receipt set:

```text
H+ = APPEND_ONLY_PROOF ESTABLISHES THE MEANING / LAWFULNESS OF EVENTS
H- = APPEND_ONLY_PROOF ESTABLISHES ONLY BOUNDED HISTORY PROPERTIES
```

The architecture permits proofs of integrity, inclusion, consistency, and replay.

It does not silently promote those proofs into meaning, identity, lawfulness, guilt, standing, jurisdiction, or adjudication.

## Closing constants

```text
LEDGER_CLASS              = APPEND_ONLY_EVENT_STREAM
PROOFS                    = INTEGRITY + INCLUSION + CONSISTENCY + REPLAY
HISTORY                    = SOURCE
CURRENT_STATE              = DERIVED_VIEW
SNAPSHOT                   = DERIVED_CHECKPOINT
COURT                      = OUT_OF_BAND
SHERIFF_PURPOSE            = USER_DEFINED_PACKET_SLOT
DARVO                      = PROJECTION
SILENCE_OBSERVATION        = VALID_EVENT_CLASS
NULL                       = FIRST_CLASS_STATE
PUBLIC_PII                 = BLOCKED_BY_DEFAULT
AUTHORITY_CREATED          = FALSE
```

## Defensible integrity close

The ledger can prove bounded sequence, byte integrity, inclusion, append-only consistency, and replay when the required receipts exist.

It cannot by itself prove meaning, identity, causation, lawfulness, jurisdiction, or adjudication.

That boundary is the integrity feature, not a limitation to hide.
