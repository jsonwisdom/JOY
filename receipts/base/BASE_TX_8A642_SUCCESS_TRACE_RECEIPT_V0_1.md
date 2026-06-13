# BASE_TX_8A642_SUCCESS_TRACE_RECEIPT_V0_1

## STATUS: BASE_RPC_TX_SUCCESS_WITNESSED
## AUTHORITY: FALSE
## NO_FAKE_GREEN: TRUE

```json
{
  "tx_hash": "0x8a642cb0e2129fb7b386aee865e421dc9c60a4a1f20120a9cb6feefd9322474b",
  "network": "Base",
  "rpc_method_receipt": "eth_getTransactionReceipt",
  "rpc_method_body": "eth_getTransactionByHash",
  "status": "0x1",
  "status_meaning": "SUCCESS",
  "block_number_hex": "0x2d17b84",
  "block_hash": "0x57d6b1caa9f58366df61ee673da725cf2657c6a398e2001419e1c1218ce05e11",
  "from": "0x8d47ba07ff9ccccf58c7e8810ee42c0dc8b8b123",
  "to": "0x5ff137d4b0fdcd49dca30c7cf57e578a026d2789",
  "gas_used_hex": "0x5ae04",
  "logs_count": 14,
  "known_address_direct_log_address_hits": false,
  "topic_address_mentions_observed": true,
  "authority": false,
  "no_fake_green": true
}
```

## Quick Receipt Summary

```text
tx_hash: 0x8a642cb0e2129fb7b386aee865e421dc9c60a4a1f20120a9cb6feefd9322474b
status: 0x1
blockNumber: 0x2d17b84
from: 0x8d47ba07ff9ccccf58c7e8810ee42c0dc8b8b123
to: 0x5ff137d4b0fdcd49dca30c7cf57e578a026d2789
gasUsed: 0x5ae04
logs_count: 14
```

## Unique Log Addresses Observed

```text
0x2faeb0760d4230ef2ac21496bb4f0b47d634fd4c
0x4200000000000000000000000000000000000006
0x5ff137d4b0fdcd49dca30c7cf57e578a026d2789
0x6d131e0d0750c5b418364d4949a6ee44c4a55ab8
0x833589fcd6edb6e08f4c7c32d4f71b54bda02913
0x88a43bbdf9d098eec7bceda4e2494615dfd9bb9c
```

## Known Address Check

The shell `ZORA / KNOWN ADDRESS CHECK` returned no direct log-address matches for the configured known-address filter.

Important nuance: the visible logs include watched addresses such as `0x829adfedbe565f9885a7ea6bc78912acaef055e2` and `0xa380552a27b0a5a2874ea7aa52cac09f542002e8` as indexed topic values, not as direct log-emitting contract addresses in the known-address filter output.

## Boundary

```text
BASE_RPC_STATUS_SUCCESS != SEMANTIC_TRUTH
DIRECT_LOG_ADDRESS_MISS != TOPIC_ADDRESS_ABSENCE
TOPIC_ADDRESS_MENTION != ASSET_PURPOSE_DECODED
NO_ZORA_COIN_ADDRESS_DIRECT_HIT_IN_FILTER_OUTPUT
NO_FAKE_GREEN_ACTIVE
```

## Ruling

Base RPC transaction success is witnessed.
The transaction emitted 14 logs.
The configured direct known-address filter returned no direct log-address matches.
Known wallet/topic mentions are visible in the trace, but no full semantic claim is made.
No authority implied.
No fake green.
