#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-.}"
BASE="$ROOT/FAMILY/receipts"
MD="$BASE/COACHES_CORNER_MENU_SOURCE_BYTES_V0_1.md"
JSON="$BASE/COACHES_CORNER_MENU_SOURCE_BYTES_INDEX_V0_1.json"

fail() {
  echo "NO_FAKE_GREEN reason=$1" >&2
  exit 1
}

[[ -f "$MD" ]] || fail "missing_source_bytes_md"
[[ -f "$JSON" ]] || fail "missing_source_bytes_json"

grep -q "SOURCE_BYTES_GATE_INDEXED" "$MD" || fail "md_missing_source_bytes_gate"
grep -q "SOURCE_BYTES_NOT_ATTACHED" "$MD" || fail "md_missing_source_bytes_not_attached"
grep -q "CONTENT_HASH_NOT_COMPUTED" "$MD" || fail "md_missing_hash_not_computed"
grep -q "INDEPENDENT_VERIFICATION_FALSE" "$MD" || fail "md_missing_independent_false"
grep -q "TRUTH_STATE_YELLOW" "$MD" || fail "md_missing_truth_yellow"
grep -q "AUTHORITY_FALSE" "$MD" || fail "md_missing_authority_false"
grep -q "NO_FAKE_GREEN_ACTIVE" "$MD" || fail "md_missing_no_fake_green"

grep -q '"source_bytes_attached": false' "$JSON" || fail "json_source_bytes_not_false"
grep -q '"content_hash_sha256": null' "$JSON" || fail "json_hash_not_null"
grep -q '"content_hash_attached": false' "$JSON" || fail "json_hash_attached_not_false"
grep -q '"independent_public_verification": false' "$JSON" || fail "json_independent_not_false"
grep -q '"truth_state": "YELLOW"' "$JSON" || fail "json_truth_not_yellow"
grep -q '"field_state": "GOAL_LINE_REVIEW"' "$JSON" || fail "json_field_state_not_goal_line_review"
grep -q '"authority": false' "$JSON" || fail "json_authority_not_false"
grep -q '"family_gate": "SOVEREIGN"' "$JSON" || fail "json_family_gate_not_sovereign"
grep -q '"no_fake_green": true' "$JSON" || fail "json_no_fake_green_missing"

grep -q "SOURCE_BYTES_GATE != AUTHORITY_TRUE" "$MD" || fail "md_missing_authority_true_boundary"
grep -q "SOURCE_BYTES_GATE != INDEPENDENT_TOUCHDOWN_CONFIRMED" "$MD" || fail "md_missing_touchdown_boundary"

echo "COACHES_CORNER_MENU_SOURCE_BYTES_GATE_OK"
echo "source_bytes_attached=false"
echo "content_hash_attached=false"
echo "independent_public_verification=false"
echo "truth_state=YELLOW"
echo "field_state=GOAL_LINE_REVIEW"
echo "authority=false"
echo "family_gate=SOVEREIGN"
echo "no_fake_green=true"
echo "next_packet=EMS_WETUMPKA_OFFICIAL_SOURCE_PACKET"
