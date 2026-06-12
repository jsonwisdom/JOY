# EAS_SCHEMA_REGISTRATION_CANDIDATE_V0_1

## Status

```json
{
  "artifact": "EAS_SCHEMA_REGISTRATION_CANDIDATE_V0_1",
  "status": "TRANSACTION_CANDIDATE_NOT_SENT",
  "chain": "Base mainnet",
  "authority": false,
  "no_fake_green": true
}
```

## Purpose

This artifact records the corrected EAS schema-registration candidate for the Jay identity receipt precedent.

It is not an execution receipt. It does not claim the schema has been registered. It records the intended target, function, schema string, calldata, and safety correction before operator wallet execution.

## Identity Anchors

```json
{
  "root_anchor": "jaywisdom.base.eth",
  "lineage_anchor": "jaywisdom.eth",
  "github_commit_root": "0570c1f92cda2e3bc8a822a92866a6cc3d63a8a1",
  "precedent_id": "IDENTITY_REPETITION_PRECEDENT_001",
  "integrity_hash": "0x32f65c664328a641328812806c8d484c43c52d414c2e4338f65b14beaf374030"
}
```

## Corrected Contract Boundary

The initial draft incorrectly targeted the EAS attestation contract for schema registration.

Corrected boundary:

```json
{
  "wrong_target": "0x4200000000000000000000000000000000000021",
  "correct_target_schema_registry": "0x4200000000000000000000000000000000000020",
  "wrong_function": "registerSchema(string,address,bool)",
  "correct_function": "register(string,address,bool)"
}
```

## Schema String

```text
IdentityReceipt(string version,uint256 timestamp,bytes32 integrity_hash,string root_anchor,string github_commit,bytes operator_signature)
```

## Registration Parameters

```json
{
  "to": "0x4200000000000000000000000000000000000020",
  "function": "register(string,address,bool)",
  "resolver": "0x0000000000000000000000000000000000000000",
  "revocable": true,
  "value": "0"
}
```

## Cast Preflight Result

Cloud Shell / Foundry produced the authoritative calldata for this candidate.

```json
{
  "cast_version": "1.5.1-stable",
  "expected_selector_previous_draft": "0x7b1837de",
  "actual_selector_from_cast": "0x60d7a278",
  "contract_code_at_target": true,
  "gas_estimate": 215623
}
```

The previous `0x7b1837de...` calldata is superseded by the `0x60d7a278...` calldata below.

## Corrected Calldata Command

```bash
cast calldata "register(string,address,bool)" \
  "IdentityReceipt(string version,uint256 timestamp,bytes32 integrity_hash,string root_anchor,string github_commit,bytes operator_signature)" \
  "0x0000000000000000000000000000000000000000" \
  true
```

## Candidate Calldata

```text
0x60d7a27800000000000000000000000000000000000000000000000000000000000000600000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000894964656e746974795265636569707428737472696e672076657273696f6e2c75696e743235362074696d657374616d702c6279746573333220696e746567726974795f686173682c737472696e6720726f6f745f616e63686f722c737472696e67206769746875625f636f6d6d69742c6279746573206f70657261746f725f7369676e6174757265290000000000000000000000000000000000000000000000
```

## Operator Action Required

Send only if the wallet transaction displays:

```json
{
  "chain": "Base mainnet",
  "to": "0x4200000000000000000000000000000000000020",
  "value": "0",
  "function_intent": "EAS SchemaRegistry.register",
  "revocable": true
}
```

Reject if the wallet displays an unexpected target, value transfer, token approval, permit, swap, bridge, or unknown spending permission.

## Post-Execution Evidence Required

After execution, record:

```json
{
  "transaction_hash": "PENDING_OPERATOR_EXECUTION",
  "schema_uid": "PENDING_REGISTERED_EVENT",
  "status": "NOT_EXECUTED"
}
```

## Court State

```json
{
  "transition": "EAS_SCHEMA_REGISTRATION_CANDIDATE_CORRECTED_BY_CAST_PREFLIGHT",
  "execution_status": "NOT_SENT",
  "next_action": "OPERATOR_WALLET_TRANSACTION_IF_SAFE",
  "authority": false,
  "no_fake_green": true
}
```
