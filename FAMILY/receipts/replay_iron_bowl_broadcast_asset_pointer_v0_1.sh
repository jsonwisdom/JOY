#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-.}"
BASE="$ROOT/FAMILY/receipts"
MD="$BASE/IRON_BOWL_BROADCAST_ASSET_POINTER_V0_1.md"
JSON="$BASE/IRON_BOWL_BROADCAST_ASSET_POINTER_INDEX_V0_1.json"

fail() {
  echo "NO_FAKE_GREEN reason=$1" >&2
  exit 1
}

[[ -f "$MD" ]] || fail "missing_iron_bowl_pointer_md"
[[ -f "$JSON" ]] || fail "missing_iron_bowl_pointer_json"

grep -q "IRON_BOWL_BROADCAST_POINTER_INDEXED" "$MD" || fail "md_missing_pointer_indexed"
grep -q "WITNESS_GREEN_METADATA_POINTER" "$MD" || fail "md_missing_witness_green"
grep -q "TRUTH_YELLOW" "$MD" || fail "md_missing_truth_yellow"
grep -q "BROADCAST_ASSET_URL_NOT_ATTACHED" "$MD" || fail "md_missing_asset_url_boundary"
grep -q "TRANSCRIPT_NOT_VERIFIED" "$MD" || fail "md_missing_transcript_boundary"
grep -q "COMMENTARY_QUOTES_FORBIDDEN" "$MD" || fail "md_missing_quote_boundary"
grep -q "FAMILY_GATE_SOVEREIGN" "$MD" || fail "md_missing_family_gate"
grep -q "AUTHORITY_FALSE" "$MD" || fail "md_missing_authority_false"
grep -q "NO_FAKE_GREEN_ACTIVE" "$MD" || fail "md_missing_no_fake_green"

grep -q '"status": "WITNESS_GREEN_METADATA_POINTER"' "$JSON" || fail "json_wrong_status"
grep -q '"witness_green": true' "$JSON" || fail "json_witness_not_green"
grep -q '"truth_yellow": true' "$JSON" || fail "json_truth_yellow_missing"
grep -q '"broadcast_metadata_staged": true' "$JSON" || fail "json_metadata_not_staged"
grep -q '"broadcast_asset_url_attached": false' "$JSON" || fail "json_asset_url_not_false"
grep -q '"transcript_verified": false' "$JSON" || fail "json_transcript_not_false"
grep -q '"commentary_quotes_authorized": false' "$JSON" || fail "json_quotes_not_false"
grep -q '"asset_custody_final": false' "$JSON" || fail "json_asset_custody_not_false"
grep -q '"button_click_points": false' "$JSON" || fail "json_button_click_points_not_false"
grep -q '"offline_family_journal_receipts_required": true' "$JSON" || fail "json_journal_required_missing"
grep -q '"authority": false' "$JSON" || fail "json_authority_not_false"
grep -q '"family_gate": "SOVEREIGN"' "$JSON" || fail "json_family_gate_not_sovereign"
grep -q '"no_fake_green": true' "$JSON" || fail "json_no_fake_green_missing"

grep -q "BROADCAST_POINTER != AUTHORITY_TRUE" "$MD" || fail "md_missing_authority_boundary"

echo "IRON_BOWL_BROADCAST_ASSET_POINTER_OK"
echo "witness_green=true"
echo "truth_yellow=true"
echo "broadcast_metadata_staged=true"
echo "broadcast_asset_url_attached=false"
echo "transcript_verified=false"
echo "commentary_quotes_authorized=false"
echo "asset_custody_final=false"
echo "offline_family_journal_receipts_required=true"
echo "authority=false"
echo "family_gate=SOVEREIGN"
echo "no_fake_green=true"
echo "next_packet=FAMILY_JOURNAL_EXECUTION_RECEIPT_TEMPLATE_V0_1"
