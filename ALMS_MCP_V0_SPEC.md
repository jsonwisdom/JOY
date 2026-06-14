# ALMS MCP V0 SPEC

**Status:** BASELINE_SPEC  
**Truth State:** YELLOW_UNTIL_IMPLEMENTED  
**NO_FAKE_GREEN:** ACTIVE  
**Directive:** PROTECT OUR ASSETS  
**Mode:** READ_ONLY_VERIFICATION_LAYER

## Purpose

ALMS_MCP_V0 defines a read-only Model Context Protocol surface for querying ALMS claims, witnesses, and GREEN/YELLOW state without giving agents authority to create, mutate, or promote claims.

This is the hardening layer before any ALMS_AGENT_V1 issuance system.

## Scope

V0 may answer verification questions.

V0 must not issue receipts.

V0 must not attest on EAS.

V0 must not flip GREEN state.

V0 must not create or mutate repo claims.

## Baseline Tools

```text
alms.lookup_claim
alms.lookup_witness
alms.check_green_state
```

## Tool Contracts

### alms.lookup_claim

Input:

```json
{
  "claim_id": "MN_CIVIC_PACKET_V1"
}
```

Output:

```json
{
  "claim_id": "MN_CIVIC_PACKET_V1",
  "state": "GREEN",
  "source_commit": "be73b5cf0b6f51de93da83d4bcee84fe57947f56",
  "source_hash": "aa85eeefb848f5e23db9c8797015c65d1f44c7a6b4a76afbb9c53712f36e595d",
  "receipt_id": "MN_CIVIC_PACKET_V1_SOURCE_HASH_RECEIPT",
  "witness_status": "PRESENT"
}
```

### alms.lookup_witness

Input:

```json
{
  "claim_id": "ZORA_SERIES_ALPHA"
}
```

Output:

```json
{
  "claim_id": "ZORA_SERIES_ALPHA",
  "witness_type": "ONCHAIN",
  "eas_uid": "0x63474b597a4fde557a23a9a71aa7e5b53fd197f78f04ee18a683a3d9e9f7a831",
  "tx_hash": "0x983fa4dd0c57fdfc92ba1124943a76b16256069411fb0bec65bc8caa1ea7873f",
  "schema_uid": "0x60b411ae490910a5c647b725969e425b9c4dfc4ffdc2e9bd591709e9614d21dd"
}
```

### alms.check_green_state

Input:

```json
{
  "claim_id": "ZORA_SERIES_ALPHA"
}
```

Output:

```json
{
  "claim_id": "ZORA_SERIES_ALPHA",
  "green_state": true,
  "reason": "PASS",
  "no_fake_green": true,
  "no_new_root": true
}
```

## Security Rules

```text
READ_ONLY_ONLY = TRUE
NO_CLAIM_MUTATION = TRUE
NO_EAS_ATTESTATION = TRUE
NO_GREEN_FLIP = TRUE
NO_PRIVATE_KEY_ACCESS = TRUE
NO_FAKE_GREEN = ACTIVE
```

## Authorized Auditor Boundary

ALMS_MCP_V0 is an auditor, not an issuer.

It can read source claims from GitHub.

It can report hashes, receipts, and witnesses.

It can detect missing proofs.

It cannot produce new authority.

## V1 Gate

ALMS_AGENT_V1 is not authorized until V0 is stable.

Before V1, require:

```text
1. MCP read-only endpoint works
2. Claim lookup deterministic
3. Green-state checker deterministic
4. Witness lookup deterministic
5. Human approval required for all claim mutation
6. Human approval required for EAS attestation
7. Kill switch documented
```

## Closing

Protect first.

Verify first.

Issue later.

Agents may query ALMS.

Agents may not become ALMS until proof-of-execution gates exist.
