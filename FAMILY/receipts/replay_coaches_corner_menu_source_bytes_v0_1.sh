#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-.}"
BASE="$ROOT/FAMILY/receipts"
MD="$BASE/COACHES_CORNER_MENU_SOURCE_BYTES_V0_1.md"
JSON="$BASE/COACHES_CORNER_MENU_SOURCE_BYTES_INDEX_V0_1.json"
EXPECTED_HASH="ddbd52e96aaf865746232ec0b7220ce2f15e5ca4b4cc394a98652dbde11ca7a2"

fail() {
  echo "NO_FAKE_GREEN reason=$1" >&2
  exit 1
}

[[ -f "$MD" ]] || fail "missing_source_bytes_md"
[[ -f "$JSON" ]] || fail "missing_source_bytes_json"

grep -q "OFFICIAL_SITE_EXTRACTED_TEXT_PACKET_ATTACHED" "$MD" || fail "md_missing_extracted_packet_attached"
grep -q "EXTRACTED_TEXT_HASH_COMPUTED" "$MD" || fail "md_missing_extracted_hash_computed"
grep -q "RAW_HTML_BYTES_NOT_CLAIMED" "$MD" || fail "md_missing_raw_html_boundary"
grep -q "INDEPENDENT_VERIFICATION_FALSE" "$MD" || fail "md_missing_independent_false"
grep -q "TRUTH_STATE_YELLOW" "$MD" || fail "md_missing_truth_yellow"
grep -q "AUTHORITY_FALSE" "$MD" || fail "md_missing_authority_false"
grep -q "NO_FAKE_GREEN_ACTIVE" "$MD" || fail "md_missing_no_fake_green"
grep -q "$EXPECTED_HASH" "$MD" || fail "md_missing_expected_hash"

grep -q '"status": "OFFICIAL_SITE_EXTRACTED_TEXT_PACKET_ATTACHED"' "$JSON" || fail "json_wrong_status"
grep -q '"raw_html_bytes_attached": false' "$JSON" || fail "json_raw_html_boundary_missing"
grep -q '"source_packet_sha256": "ddbd52e96aaf865746232ec0b7220ce2f15e5ca4b4cc394a98652dbde11ca7a2"' "$JSON" || fail "json_hash_mismatch"
grep -q '"independent_public_verification": false' "$JSON" || fail "json_independent_not_false"
grep -q '"independent_touchdown_confirmed": false' "$JSON" || fail "json_touchdown_not_false"
grep -q '"truth_state": "YELLOW"' "$JSON" || fail "json_truth_not_yellow"
grep -q '"field_state": "GOAL_LINE_REVIEW"' "$JSON" || fail "json_field_state_not_goal_line_review"
grep -q '"authority": false' "$JSON" || fail "json_authority_not_false"
grep -q '"family_gate": "SOVEREIGN"' "$JSON" || fail "json_family_gate_not_sovereign"
grep -q '"no_fake_green": true' "$JSON" || fail "json_no_fake_green_missing"

grep -q "SOURCE_BYTES_GATE != RAW_HTML_BYTE_CUSTODY" "$MD" || fail "md_missing_raw_byte_boundary"
grep -q "SOURCE_BYTES_GATE != AUTHORITY_TRUE" "$MD" || fail "md_missing_authority_true_boundary"
grep -q "SOURCE_BYTES_GATE != INDEPENDENT_TOUCHDOWN_CONFIRMED" "$MD" || fail "md_missing_touchdown_boundary"

echo "COACHES_CORNER_MENU_SOURCE_BYTES_GATE_OK"
echo "source_packet_attached=true"
echo "raw_html_bytes_attached=false"
echo "source_packet_sha256=$EXPECTED_HASH"
echo "independent_public_verification=false"
echo "truth_state=YELLOW"
echo "field_state=GOAL_LINE_REVIEW"
echo "authority=false"
echo "family_gate=SOVEREIGN"
echo "no_fake_green=true"
echo "next_packet=EMS_WETUMPKA_OFFICIAL_SOURCE_PACKET"
