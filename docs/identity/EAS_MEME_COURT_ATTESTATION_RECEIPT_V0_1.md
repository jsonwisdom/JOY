# EAS_MEME_COURT_ATTESTATION_RECEIPT_V0_1

## Status

```json
{
  "artifact": "EAS_MEME_COURT_ATTESTATION_RECEIPT_V0_1",
  "status": "ONCHAIN_ATTESTATION_RECORDED",
  "chain": "Base mainnet",
  "authority": false,
  "no_fake_green": true
}
```

## Summary

Goblin Court / Meme Court identity precedent has been attested on Base using EAS schema #1578.

The attestation records the precedent:

```text
IDENTITY_IS_NOT_SESSION
```

## Schema

```json
{
  "schema_number": 1578,
  "schema_uid": "0x79e6535156a3f4652649dff5e8ba5fd47f5d68cc7573203391ea688a0d15703b",
  "revocable": true
}
```

## Attestation

```json
{
  "uid": "0x2a4d436665af872f2a72adf08c112b1dd10b7333f5299f4048d96cd887fb6973",
  "transaction_id": "0x591f8c950f3f1e54b71b1dc2050baaabffded0e2021e347700c85268e8ef75b7",
  "created": "2026-06-11T20:56:53-05:00",
  "expiration": "Never",
  "revoked": false,
  "revocable": true,
  "from": "0x1dB2C056c7DeCD9f9fC574692b05F62aE34Fb8b5",
  "to": "No recipient",
  "referenced_attestation": "No reference"
}
```

## Decoded Data

```json
{
  "precedentId": "IDENTITY_REPETITION_PRECEDENT_001",
  "Court": "Goblin Court",
  "RootAnchor": "jaywisdom.base.eth",
  "lineageAnchor": "jaywisdom.eth",
  "receiptHash": "0x32f65c664328a641328812806c8d484c43c52d414c2e4338f65b14beaf374030",
  "githubCommit": "2517295ba986ea129fec39db2b376d179b725459",
  "ruling": "Identity is not session.",
  "authority": false
}
```

## Boundary

This attestation is a public surface-layer precedent. It does not grant platform access, ownership, legal authority, custody, or session authority.

It records a replayable distinction:

```json
{
  "identity": "public lineage claim",
  "authorization": "platform-specific permission",
  "session": "temporary login state"
}
```

## Court State

```json
{
  "transition": "EAS_ATTESTATION_EXECUTED",
  "schema_registered": true,
  "attestation_recorded": true,
  "identity_anchor": "jaywisdom.base.eth",
  "lineage_anchor": "jaywisdom.eth",
  "github_root": "2517295ba986ea129fec39db2b376d179b725459",
  "authority": false,
  "no_fake_green": true
}
```
