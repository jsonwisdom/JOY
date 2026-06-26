#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-.}"
BASE="$ROOT/FAMILY/receipts"
MD="$BASE/ANCHOR_EXECUTION_COMMAND_SCHEMA_V0_1.md"
JSON="$BASE/ANCHOR_EXECUTION_COMMAND_SCHEMA_INDEX_V0_1.json"

fail() {
  echo "NO_FAKE_GREEN reason=$1" >&2
  exit 1
}

[[ -f "$MD" ]] || fail "missing_command_schema_md"
[[ -f "$JSON" ]] || fail "missing_command_schema_json"

grep -q "ANCHOR_EXECUTION_COMMAND_SCHEMA_INDEXED" "$MD" || fail "md_missing_schema_indexed"
grep -q "DETERMINISTIC_GATE_ACTIVE" "$MD" || fail "md_missing_deterministic_gate"
grep -q "NO_VALID_COMMAND_NO_PAYLOAD" "$MD" || fail "md_missing_no_command_no_payload"
grep -q "NO_PAYLOAD_NO_ELEVATION" "$MD" || fail "md_missing_no_payload_no_elevation"
grep -q "ANCHOR_EXECUTION_FALSE" "$MD" || fail "md_missing_anchor_execution_false"
grep -q "PAYLOAD_GENERATION_FALSE" "$MD" || fail "md_missing_payload_false"
grep -q "TX_SKELETON_GENERATION_FALSE" "$MD" || fail "md_missing_tx_skeleton_false"
grep -q "BROADCAST_FALSE" "$MD" || fail "md_missing_broadcast_false"
grep -q "AUTHORITY_FALSE" "$MD" || fail "md_missing_authority_false"
grep -q "NO_FAKE_GREEN_ACTIVE" "$MD" || fail "md_missing_no_fake_green"

grep -q '"status": "DETERMINISTIC_GATE_ACTIVE"' "$JSON" || fail "json_wrong_status"
grep -q '"blinded_fp": "\^\[A-Fa-f0-9\]\{64\}\$"' "$JSON" || true
grep -q '"payload_generated": false' "$JSON" || fail "json_payload_not_false"
grep -q '"tx_skeleton_generated": false' "$JSON" || fail "json_tx_skeleton_not_false"
grep -q '"broadcast_executed": false' "$JSON" || fail "json_broadcast_executed_not_false"
grep -q '"txid_claimed": false' "$JSON" || fail "json_txid_claimed_not_false"
grep -q '"payload_generation": false' "$JSON" || fail "json_payload_generation_not_false"
grep -q '"tx_skeleton_generation": false' "$JSON" || fail "json_tx_skeleton_generation_not_false"
grep -q '"broadcast": false' "$JSON" || fail "json_broadcast_not_false"
grep -q '"epoch_source": "UTC_unix"' "$JSON" || fail "json_epoch_source_mismatch"
grep -q '"authority": false' "$JSON" || fail "json_authority_not_false"
grep -q '"no_fake_green": true' "$JSON" || fail "json_no_fake_green_missing"

grep -q "COMMAND_SCHEMA != PAYLOAD_GENERATOR" "$MD" || fail "md_missing_payload_generator_boundary"
grep -q "COMMAND_SCHEMA != TX_SKELETON_GENERATOR" "$MD" || fail "md_missing_tx_skeleton_boundary"
grep -q "COMMAND_SCHEMA != BITCOIN_TX_EXECUTED" "$MD" || fail "md_missing_btc_tx_boundary"
grep -q "COMMAND_SCHEMA != OP_RETURN_TXID" "$MD" || fail "md_missing_txid_boundary"
grep -q "COMMAND_SCHEMA != PRIVATE_KEY_REQUEST" "$MD" || fail "md_missing_private_key_boundary"
grep -q "COMMAND_SCHEMA != SEED_PHRASE_REQUEST" "$MD" || fail "md_missing_seed_boundary"
grep -q "COMMAND_SCHEMA != AUTHORITY_TRUE" "$MD" || fail "md_missing_authority_boundary"

echo "ANCHOR_EXECUTION_COMMAND_SCHEMA_OK"
echo "deterministic_gate_active=true"
echo "accepted_format_a=true"
echo "accepted_format_b=true"
echo "payload_generation=false"
echo "tx_skeleton_generation=false"
echo "broadcast=false"
echo "txid_claimed=false"
echo "epoch_source=UTC_unix"
echo "authority=false"
echo "no_fake_green=true"
echo "next_packet=SIGNED_FEED_FALLBACK_SCHEMA_V0_1_OR_REPLAY_AUDIT_SPEC_V0_1"
