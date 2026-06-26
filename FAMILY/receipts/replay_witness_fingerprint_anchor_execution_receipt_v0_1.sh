#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-.}"
BASE="$ROOT/FAMILY/receipts"
MD="$BASE/WITNESS_FINGERPRINT_ANCHOR_EXECUTION_RECEIPT_V0_1.md"
JSON="$BASE/WITNESS_FINGERPRINT_ANCHOR_EXECUTION_RECEIPT_INDEX_V0_1.json"

fail() {
  echo "NO_FAKE_GREEN reason=$1" >&2
  exit 1
}

[[ -f "$MD" ]] || fail "missing_anchor_execution_md"
[[ -f "$JSON" ]] || fail "missing_anchor_execution_json"

grep -q "WITNESS_FINGERPRINT_ANCHOR_EXECUTION_RECEIPT_INDEXED" "$MD" || fail "md_missing_receipt_indexed"
grep -q "ANCHOR_READY" "$MD" || fail "md_missing_anchor_ready"
grep -q "ANCHOR_EXECUTION_FALSE" "$MD" || fail "md_missing_anchor_execution_false"
grep -q "BITCOIN_OP_RETURN_PRIMARY" "$MD" || fail "md_missing_op_return_primary"
grep -q "SIGNED_FEED_FALLBACK_COLD" "$MD" || fail "md_missing_signed_feed_cold"
grep -q "SOVEREIGN_PUBKEY_PLACEHOLDER_OFFLINE_INJECTION" "$MD" || fail "md_missing_pubkey_placeholder"
grep -q "EPOCH_SOURCE_UTC_UNIX" "$MD" || fail "md_missing_epoch_source"
grep -q "OP_RETURN_PAYLOAD_FORMAT_LOCKED" "$MD" || fail "md_missing_payload_format"
grep -q "AUTHORITY_FALSE" "$MD" || fail "md_missing_authority_false"
grep -q "NO_FAKE_GREEN_ACTIVE" "$MD" || fail "md_missing_no_fake_green"

grep -q '"status": "ANCHOR_READY_EXECUTION_SHAPE_LOCKED"' "$JSON" || fail "json_wrong_status"
grep -q '"anchor_medium_primary": "bitcoin_op_return"' "$JSON" || fail "json_anchor_primary_mismatch"
grep -q '"anchor_medium_fallback": "signed_append_only_feed"' "$JSON" || fail "json_fallback_mismatch"
grep -q '"signed_feed_pubkey": "pubkey_placeholder_offline_injection"' "$JSON" || fail "json_pubkey_placeholder_missing"
grep -q '"epoch_source": "UTC_unix"' "$JSON" || fail "json_epoch_source_mismatch"
grep -q '"anchor_execution": false' "$JSON" || fail "json_anchor_execution_not_false"
grep -q '"broadcast_txid": null' "$JSON" || fail "json_txid_not_null"
grep -q '"total_bytes": 40' "$JSON" || fail "json_payload_size_mismatch"
grep -q '"prefix_hex": "57545031"' "$JSON" || fail "json_prefix_mismatch"
grep -q '"commitment_bytes": 32' "$JSON" || fail "json_commitment_bytes_mismatch"
grep -q '"epoch_bytes": 4' "$JSON" || fail "json_epoch_bytes_mismatch"
grep -q '"can_prepare_payload": true' "$JSON" || fail "json_prepare_payload_missing"
grep -q '"can_execute_anchor_in_this_receipt": false' "$JSON" || fail "json_execute_anchor_not_false"
grep -q '"fallback_execution": false' "$JSON" || fail "json_fallback_execution_not_false"
grep -q '"authority": false' "$JSON" || fail "json_authority_not_false"
grep -q '"no_fake_green": true' "$JSON" || fail "json_no_fake_green_missing"

grep -q "ANCHOR_EXECUTION_RECEIPT != BITCOIN_TX_EXECUTED" "$MD" || fail "md_missing_btc_tx_boundary"
grep -q "ANCHOR_EXECUTION_RECEIPT != OP_RETURN_TXID" "$MD" || fail "md_missing_txid_boundary"
grep -q "ANCHOR_EXECUTION_RECEIPT != AUTHORITY_TRUE" "$MD" || fail "md_missing_authority_boundary"

echo "WITNESS_FINGERPRINT_ANCHOR_EXECUTION_RECEIPT_OK"
echo "anchor_ready=true"
echo "anchor_execution=false"
echo "anchor_medium_primary=bitcoin_op_return"
echo "op_return_payload_total_bytes=40"
echo "op_return_prefix_hex=57545031"
echo "epoch_source=UTC_unix"
echo "signed_feed_pubkey=pubkey_placeholder_offline_injection"
echo "signed_feed_fallback_status=COLD_BACKUP"
echo "physical_gold_source_of_truth=true"
echo "digital_reporter_only=true"
echo "authority=false"
echo "no_fake_green=true"
echo "next_packet=ANCHOR_EXECUTION_LIVE_RECEIPT_REQUIRES_EXPLICIT_COMMAND"
