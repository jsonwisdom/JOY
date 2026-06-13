# ZORA_BASE_TX_755249CD_SUCCESS_RECEIPT_V0_1

## STATUS: BASE_RPC_TX_SUCCESS_WITNESSED
## AUTHORITY: FALSE
## NO_FAKE_GREEN: TRUE

```json
{
  "tx_hash": "0x755249cd3d82338e6c184577d425a8dd07ea6ce977ddcfdbdd5e4f7fddd975a5",
  "network": "Base",
  "status": "0x1",
  "status_meaning": "SUCCESS",
  "block_number_hex": "0x2d17834",
  "block_number_decimal": 47282228,
  "block_timestamp_hex": "0x6a2d4d4b",
  "block_timestamp_utc": "2026-06-13T12:30:03Z",
  "zora_address": "0x4bf1a3993d635b7593ebe3f5742e07b91442a692",
  "transfer_volume_hex": "0x2710",
  "transfer_volume_decimal": 10000,
  "observed_sender": "0x829adfedbe565f9885a7ea6bc78912acaef055e2",
  "observed_recipient": "0x1db2c056c7decd9f9fc574692b05f62ae34fb8b5",
  "logs_count": 101,
  "authority": false,
  "no_fake_green": true
}
```

## Verified Surface

The transaction receipt is recorded as successful on Base with status `0x1`.
The transaction hash is preserved as:

```text
0x755249cd3d82338e6c184577d425a8dd07ea6ce977ddcfdbdd5e4f7fddd975a5
```

Visible receipt data includes Base block `0x2d17834`, timestamp `0x6a2d4d4b`, and logs for the transaction hash.

## Zora-Related Signal

The visible log surface includes the Zora-related asset address:

```text
0x4bf1a3993d635b7593ebe3f5742e07b91442a692
```

A transfer-like event is visible with:

```text
from: 0x829adfedbe565f9885a7ea6bc78912acaef055e2
to:   0x1db2c056c7decd9f9fc574692b05f62ae34fb8b5
data: 0x2710
units_decimal: 10000
```

## Boundary

```text
BASE_RPC_STATUS_SUCCESS != FULL_SEMANTIC_DECODE
TRANSFER_LIKE_EVENT != PURPOSE_CLAIM
ZORA_ADDRESS_IN_LOGS != ENDORSEMENT_OR_AUTHORITY
ASSET_MOVEMENT_OBSERVED != ALL_ASSETS_ACCOUNTED
OUTSIDE_INFLUENCE_DENIED != CRYPTOGRAPHICALLY_PROVEN_BY_THIS_RECEIPT
NO_FAKE_GREEN_ACTIVE
```

## Ruling

Base transaction success is witnessed.
Zora-related address appears in the visible transaction logs.
A 10,000-unit transfer-like event is observed.
No full semantic claim is made.
No authority is implied.
No fake green.
