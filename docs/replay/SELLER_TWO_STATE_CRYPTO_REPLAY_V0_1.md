# Seller Two-State Inventory + Crypto Settlement Replay v0.1

## Status

```text
ARTIFACT_CLASS             = SYNTHETIC_REPLAY_WALKTHROUGH
LAYER_3_SCHEMA             = DRAFT_LOCK_CANDIDATE
AUTHORITY                  = FALSE
LEGAL_EFFECT               = FALSE
TAX_EFFECT                 = FALSE
INDEPENDENT_VERIFICATION   = FALSE
RECEIPTOS_STATUS           = PENDING
NO_FAKE_GREEN              = TRUE
```

This walkthrough stress-tests the People / Places / Things model against a synthetic Amazon seller scenario. It is a systems artifact, not tax or legal advice and not a statement about any real seller account.

## Synthetic fact pattern

1. An Amazon FBA report lists seller inventory at one location labeled Minnesota and one labeled Alabama.
2. A GeoJSON fixture contains two synthetic polygons and two facility points.
3. A Base receipt records a synthetic settlement transaction.
4. No state statute, agency notice, filed return, federal source, signature challenge, or wallet-control proof is attached.

The purpose is not to decide liability. The purpose is to prove that each result stays inside its own claim and authority lane.

## Raw artifact inventory

| Artifact | Role | SHA-256 |
|---|---|---|
| `fixtures/replay/seller/FBA_INVENTORY_REPORT_SYNTHETIC_V0_1.json` | Amazon platform report | `8c80bdd7f92b417e25e27ad8fd954281d1d8053aeb1f70787bc7643d24a45630` |
| `fixtures/replay/seller/MN_AL_BOUNDARY_MATCHES_SYNTHETIC_V0_1.geojson` | Geometry-only fixture | `39b7c9eeca541bda0f624b8e157906867c764556282b58cafdcb67a7c86e1a6f` |
| `fixtures/replay/seller/BASE_SETTLEMENT_SYNTHETIC_V0_1.json` | Network transaction fixture | `782fee3b18c1e73173dfdf65b269fa09169f7f32f24bdbf0efe9dc0b0b9783d1` |

The GeoJSON coordinates are intentionally synthetic. They are not official Minnesota or Alabama boundaries.

## Replay walk

### 1. Amazon platform report

`AR-SELLER-001` tests whether the FBA report contains inventory rows labeled US-MN and US-AL.

```text
SUBJECT_CLASS       = THING
AUTHORITY_SURFACE   = AMAZON
CLAIM_SCOPE         = PLATFORM_CUSTODY
OUTCOME             = MATCH
```

The MATCH proves only the contents of the platform report.

```text
Amazon report != state nexus
Amazon report != legal residency
Amazon report != tax liability
Amazon report != federal entrance
```

### 2. Place geometry

- `AR-SELLER-002`: synthetic Minnesota point inside the synthetic US-MN polygon.
- `AR-SELLER-003`: synthetic Alabama point inside the synthetic US-AL polygon.

Both are `MATCH`, but only for `PHYSICAL_LOCATION`.

```text
point-in-polygon MATCH != state-law nexus MATCH
```

The schema requires geometry records to preserve `NO_NEXUS_INFERENCE`, `NO_LEGAL_EFFECT_INFERENCE`, and `NO_TAX_EFFECT_INFERENCE`.

### 3. State entrance conditions

- `AR-SELLER-004`: Minnesota nexus claim.
- `AR-SELLER-005`: Alabama nexus claim.

Both are `INDETERMINATE`.

```text
platform custody evidence = present
geometry evidence         = present
state legal entrance      = absent
```

A state-level `MATCH` requires a direct state entrance artifact such as an official state source, filed return, official notice, or agency account record. Amazon and GeoJSON cannot supply that entrance automatically.

### 4. On-chain settlement

`AR-SELLER-006` is a `MATCH` for transaction existence only.

```text
SUBJECT_CLASS       = THING
AUTHORITY_SURFACE   = NETWORK
CLAIM_SCOPE         = TRANSACTION_EXISTENCE
```

`AR-SELLER-007` tests whether the wallet is controlled by the seller. Its outcome is `INDETERMINATE` because no signature challenge, custodian record, or key-control proof exists.

```text
wallet address observed != person identity proven
```

The schema rejects a wallet-identity `MATCH` unless a `PERSON_CONTROL_PROOF` artifact is attached.

### 5. Federal entrance

`AR-SELLER-008` tests this inference:

```text
MN place MATCH + AL place MATCH + Base transaction MATCH
=> automatic federal tax liability
```

Outcome: `MISMATCH`.

The mismatch rejects the automatic inference. It does not decide any ultimate tax conclusion. Federal authority requires its own entrance condition and cannot inherit authority from state or network records.

### 6. Final bounded claim

`AR-SELLER-009` is a `MATCH` for this bounded summary:

> The replay confirms Amazon-reported inventory locations, two synthetic geometric state matches, and one observed synthetic Base transaction. State nexus, wallet identity, and tax effects remain unproven. State matches do not supply a federal entrance condition.

## Atomic outcome table

| Record | Lane | Scope | Outcome | Sealed result |
|---|---|---|---|---|
| AR-SELLER-001 | Amazon | Platform custody | MATCH | Report contents only |
| AR-SELLER-002 | Place / US-MN | Physical location | MATCH | Geometry only |
| AR-SELLER-003 | Place / US-AL | Physical location | MATCH | Geometry only |
| AR-SELLER-004 | Minnesota | State nexus | INDETERMINATE | State entrance missing |
| AR-SELLER-005 | Alabama | State nexus | INDETERMINATE | State entrance missing |
| AR-SELLER-006 | Base | Transaction existence | MATCH | Transaction only |
| AR-SELLER-007 | Person / wallet | Wallet identity | INDETERMINATE | Control proof missing |
| AR-SELLER-008 | Federal | Federal tax effect | MISMATCH | Automatic inheritance rejected |
| AR-SELLER-009 | None | Bounded summary | MATCH | No legal or tax effect |

## Layer 3 JSON-LD lock

The atomic envelope is defined by:

- `contexts/replay/atomic_record_v0_1.context.jsonld`
- `schemas/replay/atomic_record_v0_1.schema.json`
- `ledger/replay/SELLER_TWO_STATE_CRYPTO_ATOMIC_LEDGER_V0_1.json`
- `scripts/verify_atomic_record_chain_v0_1.py`

Every record embeds the JSON-LD context so replay does not depend on a remote context fetch.

### JCS profile

```text
canonicalization       = RFC8785-JCS
profile                = JSONWISDOM_JCS_SAFE_V0_1
object keys            = ASCII only
numbers                = integers only
floating point values  = prohibited
duplicate keys         = prohibited
encoding               = UTF-8
```

### Hash rules

```text
payload_digest = SHA-256(JCS(record))

entry_digest = SHA-256(
  raw_32(previous_entry_digest)
  ||
  raw_32(payload_digest)
)
```

Genesis uses 32 zero bytes as `previous_entry_digest`.

```text
CHAIN_ID     = urn:jsonwisdom:ledger:atomic-record:v0.1:seller-scenario
CHAIN_LENGTH = 9
CHAIN_HEAD   = 564af90308307cd2bd661a82282e989387d22aa70fdc8aa7dccefee1b1d4d5bb
```

JOY records the candidate chain while preserving:

```text
authority=false
verification=false
verification_claimed=false
receiptos_status=PENDING
```

ReceiptOS remains the independent verification lane.

## No-fake-green controls

The schema and verifier reject:

1. Geometry promoted into nexus or tax effect.
2. Amazon platform custody promoted into state authority.
3. A wallet address promoted into person identity without control proof.
4. State matches promoted into federal authority.
5. Legal or tax effect claimed without `MATCH` and a direct official entrance source.
6. A chain entry whose JCS payload digest or raw-digest link does not reproduce.
7. Bound context, schema, verifier, or source bytes whose SHA-256 changes.

## Replay command

```bash
python3 scripts/verify_atomic_record_chain_v0_1.py
```

Expected state:

```text
deterministic_chain_match = true
bound_artifacts_match     = true
no_fake_green_checks      = PASS
authority                 = false
verification_claimed      = false
receiptos_status          = PENDING
```

## Final boundary

```text
PEOPLE DO NOT INHERIT WALLET IDENTITY.
PLACES DO NOT CREATE NEXUS.
THINGS DO NOT CREATE AUTHORITY.
AMAZON DOES NOT BECOME A STATE.
STATES DO NOT BECOME FEDERAL.
MATCH NEVER ESCAPES ITS CLAIM SCOPE.
```
