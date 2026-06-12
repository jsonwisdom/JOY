# EAS_SCHEMA_CREATION_OPERATOR_INSTRUCTIONS_V0_1

## Status

```json
{
  "artifact": "EAS_SCHEMA_CREATION_OPERATOR_INSTRUCTIONS_V0_1",
  "status": "OPERATOR_RUNBOOK_NOT_EXECUTION_RECEIPT",
  "repo": "jsonwisdom/JOY",
  "authority": false,
  "no_fake_green": true
}
```

## Purpose

This runbook gives Jay operator instructions for registering the `JAY_IDENTITY_RECEIPT_V0_1` schema through EAS on Base.

It does not claim that the schema has been registered. It defines the exact preflight checks, send rules, reject rules, and evidence required after execution.

## Required Context

```json
{
  "root_anchor": "jaywisdom.base.eth",
  "lineage_anchor": "jaywisdom.eth",
  "precedent_id": "IDENTITY_REPETITION_PRECEDENT_001",
  "identity_hash": "0x32f65c664328a641328812806c8d484c43c52d414c2e4338f65b14beaf374030",
  "schema_candidate_commit": "7b7f1fb1c6a35adee0bc17f6d19a572d89ba5375"
}
```

## Target Transaction

```json
{
  "chain": "Base mainnet",
  "to": "0x4200000000000000000000000000000000000020",
  "value": "0",
  "function": "register(string,address,bool)",
  "resolver": "0x0000000000000000000000000000000000000000",
  "revocable": true
}
```

## Schema String

```text
IdentityReceipt(string version,uint256 timestamp,bytes32 integrity_hash,string root_anchor,string github_commit,bytes operator_signature)
```

## Candidate Calldata

```text
0x7b1837de00000000000000000000000000000000000000000000000000000000000000600000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000100000000000000000000000000000000000000000000000000000000000000e44964656e746974795265636569707428737472696e672076657273696f6e2c75696e743235362074696d657374616d702c6279746573333220696e746567726974795f686173682c737472696e6720726f6f745f616e63686f722c737472696e67206769746875625f636f6d6d69742c6279746573206f70657261746f725f7369676e6174757265290000000000000000000000000000000000000000000000000000
```

## Operator Preflight

Before sending, verify all of the following:

```json
{
  "wallet_network": "Base mainnet",
  "transaction_to": "0x4200000000000000000000000000000000000020",
  "transaction_value": "0",
  "transaction_type": "contract interaction",
  "expected_intent": "EAS SchemaRegistry.register",
  "token_approval": false,
  "permit": false,
  "swap": false,
  "bridge": false,
  "spending_permission": false
}
```

If any check fails, reject the transaction.

## Safe Execution Path

1. Open the Base wallet or wallet capable of sending a custom contract transaction on Base.
2. Select Base mainnet.
3. Set the transaction target to:

```text
0x4200000000000000000000000000000000000020
```

4. Set value to:

```text
0
```

5. Use the candidate calldata exactly as recorded above.
6. Review the wallet confirmation screen.
7. Send only if the target, chain, and value match this runbook.
8. Wait for confirmation.

## Reject Rules

Reject immediately if the wallet shows any of the following:

```json
{
  "reject_if": [
    "different target address",
    "nonzero value transfer",
    "token approval",
    "permit signature",
    "swap",
    "bridge",
    "setApprovalForAll",
    "unknown spending permission",
    "wrong chain",
    "unclear transaction intent"
  ]
}
```

## Evidence To Return

After execution, return:

```text
SCHEMA_TX=0x...
SCHEMA_UID=0x...
```

If the transaction fails, return:

```text
SCHEMA_TX_FAILED=0x...
FAILURE_REASON=<wallet_or_explorer_message>
```

## Post-Execution Court Update

Only after `SCHEMA_TX` and `SCHEMA_UID` are provided may the court move from candidate to registered.

```json
{
  "candidate_status": "ROOTED",
  "execution_status": "PENDING_OPERATOR_TRANSACTION",
  "schema_registered": false,
  "attestation_ready": false,
  "authority": false,
  "no_fake_green": true
}
```

## Plain Operator Rule

Do not prove identity again. Do not repair Cloud Shell auth. Do not paste private keys or seed phrases.

This action is only schema creation. It does not transfer funds, approve tokens, or grant platform access.
