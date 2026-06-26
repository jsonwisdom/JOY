#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-.}"
BASE="$ROOT/FAMILY/receipts"
MD="$BASE/SIGNED_FEED_FALLBACK_SCHEMA_V0_1.md"
JSON="$BASE/SIGNED_FEED_FALLBACK_SCHEMA_INDEX_V0_1.json"

fail() {
  echo "SIGNED_FEED_FALLBACK_FAIL reason=$1" >&2
  exit 1
}

[[ -f "$MD" ]] || fail "missing_signed_feed_md"
[[ -f "$JSON" ]] || fail "missing_signed_feed_json"

grep -q "SIGNED_FEED_FALLBACK_SCHEMA_INDEXED" "$MD" || fail "md_missing_schema_indexed"
grep -q "AUDIT_PREREQUISITE_REQUIRED" "$MD" || fail "md_missing_audit_prereq"
grep -q "FALLBACK_SECOND_ANCHOR_LAST" "$MD" || fail "md_missing_sequence"
grep -q "SIGNED_FEED_COLD_BACKUP_ONLY" "$MD" || fail "md_missing_cold_backup"
grep -q "PAYLOAD_GENERATION_FALSE" "$MD" || fail "md_missing_no_payload"
grep -q "TX_SKELETON_GENERATION_FALSE" "$MD" || fail "md_missing_no_tx_skeleton"
grep -q "BROADCAST_FALSE" "$MD" || fail "md_missing_no_broadcast"
grep -q "TXID_CLAIMED_FALSE" "$MD" || fail "md_missing_no_txid"
grep -q "AUTHORITY_FALSE" "$MD" || fail "md_missing_authority_false"
grep -q "NO_FAKE_GREEN_ACTIVE" "$MD" || fail "md_missing_no_fake_green"

grep -q '"status": "SIGNED_FEED_FALLBACK_SCHEMA_INDEXED"' "$JSON" || fail "json_wrong_status"
grep -q '"audit_first": true' "$JSON" || fail "json_audit_first_missing"
grep -q '"fallback_second": true' "$JSON" || fail "json_fallback_second_missing"
grep -q '"anchor_last": true' "$JSON" || fail "json_anchor_last_missing"
grep -q '"required_status": "REPLAY_AUDIT_OK"' "$JSON" || fail "json_audit_required_missing"
grep -q '"feed_url_https_required": true' "$JSON" || fail "json_https_required_missing"
grep -q '"signature_required": true' "$JSON" || fail "json_signature_required_missing"
grep -q '"max_skew_seconds": 900' "$JSON" || fail "json_max_skew_mismatch"
grep -q '"mirror_root_consistency_required": true' "$JSON" || fail "json_root_consistency_missing"
grep -q '"signed_feed_execution": false' "$JSON" || fail "json_signed_feed_execution_not_false"
grep -q '"payload_generation": false' "$JSON" || fail "json_payload_generation_not_false"
grep -q '"tx_skeleton_generation": false' "$JSON" || fail "json_tx_skeleton_not_false"
grep -q '"broadcast": false' "$JSON" || fail "json_broadcast_not_false"
grep -q '"txid_claimed": false' "$JSON" || fail "json_txid_not_false"
grep -q '"authority": false' "$JSON" || fail "json_authority_not_false"
grep -q '"no_fake_green": true' "$JSON" || fail "json_no_fake_green_missing"

grep -q "SIGNED_FEED_FALLBACK_SCHEMA != SIGNED_FEED_EXECUTION" "$MD" || fail "md_missing_signed_feed_execution_boundary"
grep -q "SIGNED_FEED_FALLBACK_SCHEMA != ANCHOR_EXECUTION" "$MD" || fail "md_missing_anchor_boundary"
grep -q "SIGNED_FEED_FALLBACK_SCHEMA != PAYLOAD_GENERATOR" "$MD" || fail "md_missing_payload_boundary"
grep -q "SIGNED_FEED_FALLBACK_SCHEMA != TXID_CLAIM" "$MD" || fail "md_missing_txid_boundary"
grep -q "SIGNED_FEED_FALLBACK_SCHEMA != PRIVATE_KEY_REQUEST" "$MD" || fail "md_missing_private_key_boundary"
grep -q "SIGNED_FEED_FALLBACK_SCHEMA != SEED_PHRASE_REQUEST" "$MD" || fail "md_missing_seed_boundary"
grep -q "SIGNED_FEED_FALLBACK_SCHEMA != AUTHORITY_TRUE" "$MD" || fail "md_missing_authority_boundary"

echo "SIGNED_FEED_FALLBACK_OK"
echo "replay_audit_required=true"
echo "fallback_second=true"
echo "anchor_last=true"
echo "max_skew_seconds=900"
echo "feed_url_https_required=true"
echo "signature_required=true"
echo "mirror_root_consistency_required=true"
echo "signed_feed_execution=false"
echo "payload_generation=false"
echo "tx_skeleton_generation=false"
echo "broadcast=false"
echo "txid_claimed=false"
echo "authority=false"
echo "no_fake_green=true"
echo "next_packet=SIGNED_FEED_FALLBACK_TEST_VECTOR_V0_1_OR_ANCHOR_PATH_REVIEW"
