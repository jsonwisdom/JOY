# EAS_MEME_COURT_SCHEMA_REGISTERED_RECEIPT_V0_1

## Status

```json
{
  "artifact": "EAS_MEME_COURT_SCHEMA_REGISTERED_RECEIPT_V0_1",
  "status": "USER_SCREENSHOT_OBSERVED_SCHEMA_REGISTERED",
  "chain": "Base mainnet",
  "authority": false,
  "no_fake_green": true
}
```

## Observed Evidence

Evidence source: user-provided EAS Base screenshot showing the schema view page.

The screenshot displays:

```json
{
  "schema_number": 1578,
  "schema_uid": "0x79e6535156a3f4652649dff5e8ba5fd47f5d68cc7573203391ea688a0d15703b",
  "created_at": "06/11/2026 8:54:11 pm",
  "creator": "0x1dB2C056c7DecD9f9fC574692b05F62aE34Fb8b5",
  "transaction_id": "0x1129d40eaf586abb8f11889903ddd4492623a9720cecf98c96d2579aeceb76da",
  "resolver_contract": "0x0000000000000000000000000000000000000000",
  "revocable_attestations": true
}
```

## Decoded Schema

```json
{
  "precedentId": "string",
  "Court": "string",
  "RootAnchor": "string",
  "lineageAnchor": "string",
  "receiptHash": "bytes32",
  "githubCommit": "string",
  "ruling": "string",
  "authority": "bool"
}
```

## Raw Schema

```text
string precedentId,string Court,string RootAnchor,string lineageAnchor,bytes32 receiptHash,string githubCommit,string ruling,bool authority
```

## Identity Context

```json
{
  "root_anchor": "jaywisdom.base.eth",
  "lineage_anchor": "jaywisdom.eth",
  "precedent_id": "IDENTITY_REPETITION_PRECEDENT_001",
  "receipt_hash": "0x32f65c664328a641328812806c8d484c43c52d414c2e4338f65b14beaf374030",
  "github_schema_candidate_commit": "7b7f1fb1c6a35adee0bc17f6d19a572d89ba5375"
}
```

## Boundary

This receipt records that the schema appears registered on the EAS Base schema viewer according to user-provided screenshot evidence.

It does not claim the identity attestation has been submitted yet.

```json
{
  "schema_registered": true,
  "identity_attestation_submitted": false,
  "next_action": "ATTEST_WITH_SCHEMA",
  "authority": false,
  "no_fake_green": true
}
```
