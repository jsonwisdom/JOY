#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-.}"
BASE="$ROOT/FAMILY/receipts"
MD="$BASE/FAMILY_JOURNAL_EXECUTION_RECEIPT_TEMPLATE_V0_1.md"
JSON="$BASE/FAMILY_JOURNAL_EXECUTION_RECEIPT_TEMPLATE_INDEX_V0_1.json"

fail() {
  echo "NO_FAKE_GREEN reason=$1" >&2
  exit 1
}

[[ -f "$MD" ]] || fail "missing_journal_template_md"
[[ -f "$JSON" ]] || fail "missing_journal_template_json"

grep -q "FAMILY_JOURNAL_TEMPLATE_INDEXED" "$MD" || fail "md_missing_template_indexed"
grep -q "OFFLINE_EXECUTION_RECEIPT_REQUIRED" "$MD" || fail "md_missing_offline_receipt_required"
grep -q "DIGITAL_SIDE_READ_ONLY" "$MD" || fail "md_missing_read_only"
grep -q "WITNESS_REQUIRED" "$MD" || fail "md_missing_witness_required"
grep -q "PHYSICAL_EXECUTION_HASH_REQUIRED" "$MD" || fail "md_missing_hash_required"
grep -q "GOLD_PENDING_REQUIRES_COOLDOWN" "$MD" || fail "md_missing_cooldown"
grep -q "PURPOSE_LAYER_REVIEW_REQUIRED" "$MD" || fail "md_missing_review_required"
grep -q "AUTHORITY_FALSE" "$MD" || fail "md_missing_authority_false"
grep -q "NO_FAKE_GREEN_ACTIVE" "$MD" || fail "md_missing_no_fake_green"

grep -q '"status": "FAMILY_JOURNAL_TEMPLATE_INDEXED"' "$JSON" || fail "json_wrong_status"
grep -q '"digital_side_read_only": true' "$JSON" || fail "json_read_only_missing"
grep -q '"witness_required": true' "$JSON" || fail "json_witness_missing"
grep -q '"physical_execution_hash_required": true' "$JSON" || fail "json_hash_missing"
grep -q '"cooldown_required_before_gold": true' "$JSON" || fail "json_cooldown_missing"
grep -q '"purpose_layer_required_before_gold": true' "$JSON" || fail "json_review_missing"
grep -q '"button_click_points": false' "$JSON" || fail "json_button_click_not_false"
grep -q '"authority": false' "$JSON" || fail "json_authority_not_false"
grep -q '"family_gate": "SOVEREIGN"' "$JSON" || fail "json_family_gate_not_sovereign"
grep -q '"no_fake_green": true' "$JSON" || fail "json_no_fake_green_missing"

grep -q "FAMILY_JOURNAL_TEMPLATE != AUTHORITY_TRUE" "$MD" || fail "md_missing_authority_boundary"

echo "FAMILY_JOURNAL_EXECUTION_RECEIPT_TEMPLATE_OK"
echo "digital_side_read_only=true"
echo "witness_required=true"
echo "physical_execution_hash_required=true"
echo "cooldown_required_before_gold=true"
echo "purpose_layer_required_before_gold=true"
echo "button_click_points=false"
echo "authority=false"
echo "family_gate=SOVEREIGN"
echo "no_fake_green=true"
echo "next_packet=DIGITAL_ABI_FAMILY_JOURNAL_READ_SPEC_V0_1"
