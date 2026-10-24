# Quadratic Proof Specification v0.1

## Status

```text
ARTIFACT_ID          = JOY-QGP-001
STATUS               = QUARANTINED_DRAFT
EXECUTION            = PROHIBITED
AUTHORITY_CREATED    = FALSE
PROMOTION_ALLOWED    = FALSE
FABRICATED_HASHES    = PROHIBITED
MERGE_AUTHORIZATION  = FALSE
REPLAY_AUTHORITY     = FROZEN_SOURCE_BYTES
```

## Purpose

Define a replayable cryptographic proof system for quadratic voting arithmetic without revealing each participant's private vote allocation.

The proof must establish that:

1. each participant's quadratic cost remains within the authorized budget;
2. every vote value is within the allowed range;
3. the published tally is derived correctly from committed votes;
4. verification can be repeated from public commitments, public parameters, and the published proof;
5. successful verification creates confidence in arithmetic correctness but does not create execution authority.

## Mathematical model

Let:

- `n` identify a participant;
- `p` identify a proposal or option;
- `v[n,p]` be the participant's signed or unsigned vote allocation;
- `B[n]` be the participant's authorized budget;
- `T[p]` be the published tally.

Quadratic cost:

```text
cost[n] = sum_p(v[n,p]^2)
```

Required budget constraint:

```text
cost[n] <= B[n]
```

Required tally constraint:

```text
T[p] = sum_n(v[n,p])
```

Unsigned range profile:

```text
0 <= v[n,p] <= 15
```

Signed range profile, when explicitly enabled by the frozen ruleset:

```text
-15 <= v[n,p] <= 15
```

Unsigned and signed profiles MUST NOT be mixed inside one proof instance unless the circuit and public parameters explicitly distinguish them.

## Evidence boundary

The proof is a receipt for arithmetic integrity. It is not:

- the vote itself;
- permission to execute a result;
- evidence of voter identity beyond the committed authorization model;
- proof that the voting policy is fair;
- proof that participants were eligible;
- proof that coercion, collusion, or Sybil behavior did not occur;
- proof that a tally should be adopted.

Controlling rule:

```text
VERIFICATION IS PUBLIC.
EXECUTION IS AUTHORIZED SEPARATELY.
```

## Cryptographic architecture

### 1. Vote commitments

Each private value `v[n,p]` is committed before tally publication.

Permitted design candidates:

- Pedersen commitments over a documented prime-order group;
- hash commitments with independently sampled blinding values;
- circuit-native commitments compatible with the selected proof system.

Commitments MUST bind:

```text
fixture_id
rules_version
participant_pseudonym
proposal_id
vote_value
blinding_value
commitment_domain
```

The commitment domain MUST be separated from receipt hashes, identity hashes, and state roots.

### 2. Range proof

For the unsigned profile, prove:

```text
0 <= v[n,p] <= 15
```

A four-bit decomposition MAY be used:

```text
v[n,p] = x0 + 2*x1 + 4*x2 + 8*x3
x_i in {0,1}
```

For each bit, the circuit proves booleanity:

```text
x_i * (x_i - 1) = 0
```

The signed profile requires an explicit sign representation and range constraint. Negative values MUST NOT be inferred from modular field representation alone.

### 3. Quadratic cost proof

For every participant, prove the square relation:

```text
q[n,p] = v[n,p] * v[n,p]
```

Then prove:

```text
sum_p(q[n,p]) + slack[n] = B[n]
slack[n] >= 0
```

The slack value remains private unless the ruleset requires public disclosure.

The circuit MUST prevent field wraparound from making an over-budget value appear valid. Integer bounds and field capacity MUST be documented.

### 4. Tally proof

For every proposal, prove:

```text
T[p] = sum_n(v[n,p])
```

Where additive commitments are used, the verifier MAY check that aggregated commitments correspond to the committed tally, with a zero-knowledge opening proof for the aggregate blinding factor.

Tally proof requirements:

- no uncommitted vote may enter the sum;
- no committed vote may be counted twice;
- participant and proposal identifiers must be bound to commitment positions;
- ordering must be canonical or explicitly indexed;
- duplicate identifiers must fail closed.

### 5. Proof system candidates

Candidate families include:

- Bulletproofs for range and arithmetic relations;
- Groth16 for succinct verification with a circuit-specific trusted setup;
- PLONK-family systems for universal or updatable setup models;
- transparent proof systems where setup avoidance is a controlling requirement.

No proof system is selected by this draft.

A production decision MUST document:

```text
setup_model
curve_or_field
security_assumptions
circuit_version
verification_cost
proof_size
prover_memory
mobile_feasibility
audit_status
```

## Frozen public inputs

A proof instance MUST bind at minimum:

```json
{
  "artifact_id": "JOY-QGP-001",
  "fixture_id": "QGP-SYNTH-001",
  "rules_version": "0.1.0",
  "range_profile": "UNSIGNED_0_15",
  "commitments_root": "sha256:<pending>",
  "budget_root": "sha256:<pending>",
  "tally_root": "sha256:<pending>",
  "circuit_id": "QGP-CIRCUIT-001",
  "proof_system": "UNSELECTED"
}
```

`<pending>` is a placeholder and MUST NOT be promoted as a real digest.

## Private witness

The private witness may contain:

```text
vote_values
commitment_blinding_values
bit_decompositions
square_values
budget_slack_values
aggregate_blinding_values
```

Private witness data MUST NOT be logged in replay receipts, application telemetry, crash reports, or public build artifacts.

## Proof output

The prover emits:

```json
{
  "proof_id": "QGP-PROOF-001",
  "artifact_id": "JOY-QGP-001",
  "fixture_id": "QGP-SYNTH-001",
  "circuit_id": "QGP-CIRCUIT-001",
  "proof_system": "UNSELECTED",
  "proof_bytes_hash": "sha256:<pending>",
  "public_inputs_hash": "sha256:<pending>",
  "verification_key_hash": "sha256:<pending>",
  "status": "NOT_GENERATED"
}
```

## Verification procedure

A conforming verifier performs these steps:

1. Load exact frozen public-input bytes.
2. Verify canonical serialization rules.
3. Recompute the public-input digest.
4. Verify the circuit identifier and rules version.
5. Verify the verification-key digest against the accepted registry entry.
6. Verify proof bytes against the public inputs.
7. Produce a replay receipt.
8. Return only `PASS`, `FAIL`, or `INDETERMINATE`.

Verification pseudocode:

```text
verify_qgp(proof, public_inputs, verification_key):
    require canonical(public_inputs)
    require registered(circuit_id, rules_version, verification_key_hash)
    result = zk_verify(verification_key, proof, public_inputs)

    if result == true:
        return PASS
    if result == false:
        return FAIL
    return INDETERMINATE
```

A successful proof verification establishes only:

```text
RANGE_CONSTRAINTS_SATISFIED
QUADRATIC_COST_CONSTRAINTS_SATISFIED
TALLY_CONSTRAINTS_SATISFIED
FOR_THE_BOUND_PUBLIC_INPUTS
UNDER_THE_SELECTED_PROOF_SYSTEM
```

## Replay receipt

```json
{
  "receipt_id": "QGP-RC-001",
  "artifact_id": "JOY-QGP-001",
  "fixture_id": "QGP-SYNTH-001",
  "receipt_type": "QUADRATIC_PROOF_VERIFICATION",
  "circuit_id": "QGP-CIRCUIT-001",
  "rules_version": "0.1.0",
  "public_inputs_hash": "sha256:<pending>",
  "proof_bytes_hash": "sha256:<pending>",
  "verification_key_hash": "sha256:<pending>",
  "status": "NOT_EXECUTED",
  "previous_receipt_hash": "sha256:<pending>",
  "timestamp": "PENDING"
}
```

## Synthetic fixture design

Fixture identifier:

```text
QGP-SYNTH-001
```

Illustrative private allocation:

```text
Participant A: [2, 1, 0]
Participant B: [1, 0, 2]
Participant C: [0, 2, 1]
```

Illustrative budgets:

```text
B[A] = 5
B[B] = 5
B[C] = 5
```

Expected private costs:

```text
A: 2^2 + 1^2 + 0^2 = 5
B: 1^2 + 0^2 + 2^2 = 5
C: 0^2 + 2^2 + 1^2 = 5
```

Expected public tally:

```text
T = [3, 3, 3]
```

Required negative tests:

1. A vote value of `16` fails the unsigned range proof.
2. A participant cost of `6` against budget `5` fails.
3. A published tally of `[3, 3, 4]` fails.
4. A commitment reordered under a different participant identifier fails.
5. A proof bound to another `rules_version` fails.
6. A substituted verification key fails registry verification.
7. A malformed or noncanonical public-input document fails before proof verification.
8. A duplicate commitment fails closed.

## Privacy requirements

The implementation MUST NOT reveal:

- individual vote values;
- per-participant slack unless explicitly authorized;
- commitment blinding values;
- raw witness data;
- correlations created by unstable pseudonyms across unrelated elections.

The system SHOULD support election-specific pseudonyms and unlinkable commitments where policy permits.

## Mobile and iPhone feasibility

Verification may be practical on modern mobile devices, depending on proof system, curve, proof size, and circuit complexity.

Proving may be substantially more expensive than verification. Therefore:

```text
IPHONE_VERIFICATION = DESIGN_TARGET
IPHONE_PROVING       = BENCHMARK_REQUIRED
SECURE_ENCLAVE       = KEY_PROTECTION_ONLY
SECURE_ENCLAVE       != GENERAL_ZK_PROVER
```

No mobile-performance claim is accepted until measured on identified hardware and software versions.

## Public audit and voting relationship

Public participants may independently verify the proof and compare receipts. That collective check does not alter the proof result.

```text
PUBLIC_AUDIT    = MANY PEOPLE MAY VERIFY
PUBLIC_VOTE     = SEPARATE GOVERNANCE PROCESS
PROOF_RESULT    = CRYPTOGRAPHIC VERIFICATION RESULT
EXECUTION_RIGHT = SEPARATE AUTHORITY GRANT
```

A majority vote cannot convert an invalid proof into a valid proof. A valid proof cannot independently authorize execution.

## JOY relationship

JOY explains the proof in human language and preserves the learning experience.

JOY does not determine cryptographic validity.

```text
JOY WELCOMES.
THE VERIFIER CHECKS.
THE RECEIPT RECORDS.
AUTHORITY ACTS ONLY WHEN SEPARATELY GRANTED.
```

## Promotion gate

Promotion from quarantined draft requires all of the following:

1. exact circuit specification;
2. selected proof system and documented setup model;
3. deterministic public-input encoding;
4. independently reviewed integer and field bounds;
5. complete positive and negative test vectors;
6. reproducible verification implementation;
7. mobile benchmarks where mobile use is claimed;
8. independent cryptographic review;
9. exact frozen artifact hashes;
10. explicit human authorization for promotion.

Until then:

```text
SPECIFICATION_STATUS = DRAFT
PROOF_GENERATED       = FALSE
PROOF_VERIFIED        = FALSE
AUTHORITY_CREATED     = FALSE
PROMOTION_ALLOWED     = FALSE
```
