#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-.}"
BASE="$ROOT/FAMILY/receipts"
MD="$BASE/WITNESS_FINGERPRINT_PROTOCOL_V0_1.md"
JSON="$BASE/WITNESS_FINGERPRINT_PROTOCOL_INDEX_V0_1.json"

fail() {
  echo "NO_FAKE_GREEN reason=$1" >&2
  exit 1
}

[[ -f "$MD" ]] || fail "missing_witness_fingerprint_md"
[[ -f "$JSON" ]] || fail "missing_witness_fingerprint_json"

grep -q "WITNESS_FINGERPRINT_PROTOCOL_INDEXED" "$MD" || fail "md_missing_protocol_indexed"
grep -q "OFFLINE_WITNESS_SOURCE_OF_TRUTH" "$MD" || fail "md_missing_offline_truth"
grep -q "DIGITAL_SIDE_OBSERVER_ONLY" "$MD" || fail "md_missing_observer_only"
grep -q "PHYSICAL_GOLD_ANCHOR_ONLY" "$MD" || fail "md_missing_physical_gold"
grep -q "COMMITMENT_BOUND_TO_PROTOCOL_VERSION" "$MD" || fail "md_missing_version_binding"
grep -q "PHASH_TOLERANCE_SET" "$MD" || fail "md_missing_phash_tolerance"
grep -q "QR_TRANSFER_COMPRESSED_AND_BLINDED" "$MD" || fail "md_missing_qr_rule"
grep -q "ANCHOR_EXECUTION_FALSE" "$MD" || fail "md_missing_anchor_execution_false"
grep -q "AUTHORITY_FALSE" "$MD" || fail "md_missing_authority_false"
grep -q "NO_FAKE_GREEN_ACTIVE" "$MD" || fail "md_missing_no_fake_green"

grep -q '"status": "WITNESS_FINGERPRINT_PROTOCOL_INDEXED"' "$JSON" || fail "json_wrong_status"
grep -q '"anchor_medium": "bitcoin_op_return_preferred"' "$JSON" || fail "json_anchor_medium_mismatch"
grep -q '"anchor_execution": false' "$JSON" || fail "json_anchor_execution_not_false"
grep -q '"pHash_hamming_distance_threshold": 5' "$JSON" || fail "json_phash_threshold_mismatch"
grep -q '"qr_payload_max_chars": 512' "$JSON" || fail "json_qr_max_mismatch"
grep -q '"minimum_scan_dpi": 300' "$JSON" || fail "json_dpi_mismatch"
grep -q '"commitment_bound_to_protocol_version": true' "$JSON" || fail "json_version_binding_missing"
grep -q '"blinded_payload_only": true' "$JSON" || fail "json_blinded_payload_missing"
grep -q '"manual_reanchor_required_for_review_or_reject": true' "$JSON" || fail "json_reanchor_missing"
grep -q '"digital_side_observer_only": true' "$JSON" || fail "json_observer_missing"
grep -q '"authority": false' "$JSON" || fail "json_authority_not_false"
grep -q '"no_fake_green": true' "$JSON" || fail "json_no_fake_green_missing"

grep -q "WITNESS_FINGERPRINT_PROTOCOL != BITCOIN_TX_EXECUTED" "$MD" || fail "md_missing_tx_boundary"
grep -q "WITNESS_FINGERPRINT_PROTOCOL != OP_RETURN_TXID" "$MD" || fail "md_missing_txid_boundary"
grep -q "WITNESS_FINGERPRINT_PROTOCOL != AUTHORITY_TRUE" "$MD" || fail "md_missing_authority_boundary"

echo "WITNESS_FINGERPRINT_PROTOCOL_OK"
echo "anchor_medium=bitcoin_op_return_preferred"
echo "anchor_execution=false"
echo "pHash_hamming_distance_threshold=5"
echo "qr_payload_max_chars=512"
echo "minimum_scan_dpi=300"
echo "commitment_bound_to_protocol_version=true"
echo "digital_side_observer_only=true"
echo "offline_receipt_source_of_truth=true"
echo "authority=false"
echo "no_fake_green=true"
echo "next_packet=WITNESS_FINGERPRINT_ANCHOR_EXECUTION_RECEIPT_V0_1_OR_SIGNED_FEED_FALLBACK"
