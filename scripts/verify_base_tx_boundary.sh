#!/usr/bin/env bash
# script: verify_base_tx_boundary.sh
# doctrine: No signal without execution. No execution claim without receipt.
# usage: ./scripts/verify_base_tx_boundary.sh <normalized_receipt.json>

set -euo pipefail

RECEIPT_FILE="${1:-}"

halt() {
  echo "HALT: $1"
  exit 1
}

pass() {
  echo "GREEN: $1"
}

[ -n "$RECEIPT_FILE" ] || halt "Missing receipt JSON file."
[ -f "$RECEIPT_FILE" ] || halt "Receipt file not found: $RECEIPT_FILE"
command -v jq >/dev/null 2>&1 || halt "jq is required."

echo "Initiating Base TX Boundary Verification..."

rpc_status="$(jq -r '.rpc_status // .tx_status // .execution_status // empty' "$RECEIPT_FILE")"
logs_count="$(jq -r '.logs_count // empty' "$RECEIPT_FILE")"
topic_mentions="$(jq -r '.topic_mentions_observed // empty' "$RECEIPT_FILE")"
direct_hit="$(jq -r '.direct_zora_coin_log_address_hit // empty' "$RECEIPT_FILE")"
semantic_final="$(jq -r '.semantic_truth_final // empty' "$RECEIPT_FILE")"
authority="$(jq -r '.authority // empty' "$RECEIPT_FILE")"
no_fake_green="$(jq -r '.no_fake_green // empty' "$RECEIPT_FILE")"

[ "$rpc_status" = "0x1" ] || halt "RPC status mismatch. Expected 0x1, got '${rpc_status:-MISSING}'."
[ "$logs_count" = "14" ] || halt "Log count mismatch. Expected 14, got '${logs_count:-MISSING}'."
[ "$topic_mentions" = "true" ] || halt "Topic mentions absent."
[ "$direct_hit" = "false" ] || halt "Direct Zora coin log address hit detected."
[ "$semantic_final" = "false" ] || halt "Semantic truth claimed prematurely."
[ "$authority" = "false" ] || halt "Authority flag active."
[ "$no_fake_green" = "true" ] || halt "No Fake Green guard missing."

pass "Receipt boundary verification passed. Machine replay authorized."
