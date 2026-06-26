#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-.}"
BASE="$ROOT/FAMILY/receipts"
MD="$BASE/COACHES_CORNER_MENU_HASH_PACKET_V0_1.md"
JSON="$BASE/COACHES_CORNER_MENU_HASH_PACKET_INDEX_V0_1.json"

fail() {
  echo "NO_FAKE_GREEN reason=$1" >&2
  exit 1
}

[[ -f "$MD" ]] || fail "missing_menu_hash_packet_md"
[[ -f "$JSON" ]] || fail "missing_menu_hash_packet_json"

grep -q "MENU_HASH_PACKET_INDEXED" "$MD" || fail "md_missing_packet_indexed"
grep -q "WITNESS_GREEN_PACKET_STRUCTURE" "$MD" || fail "md_missing_witness_green_structure"
grep -q "CONTENT_HASH_PENDING" "$MD" || fail "md_missing_content_hash_pending"
grep -q "INDEPENDENT_TOUCHDOWN_BLOCKED" "$MD" || fail "md_missing_independent_touchdown_blocked"
grep -q "FAMILY_GATE_SOVEREIGN" "$MD" || fail "md_missing_family_gate_sovereign"
grep -q "AUTHORITY_FALSE" "$MD" || fail "md_missing_authority_false"
grep -q "NO_FAKE_GREEN_ACTIVE" "$MD" || fail "md_missing_no_fake_green"

grep -q '"status": "WITNESS_GREEN_PACKET_STRUCTURE"' "$JSON" || fail "json_wrong_status"
grep -q '"content_hash_attached": false' "$JSON" || fail "json_content_hash_not_false"
grep -q '"independent_public_verification": false' "$JSON" || fail "json_independent_public_verification_not_false"
grep -q '"independent_touchdown_confirmed": false' "$JSON" || fail "json_independent_touchdown_not_false"
grep -q '"field_state": "GOAL_LINE_REVIEW"' "$JSON" || fail "json_field_state_not_goal_line_review"
grep -q '"authority": false' "$JSON" || fail "json_authority_not_false"
grep -q '"family_gate": "SOVEREIGN"' "$JSON" || fail "json_family_gate_not_sovereign"
grep -q '"no_fake_green": true' "$JSON" || fail "json_no_fake_green_missing"

grep -q "COACHES_CORNER_MENU_HASH_PACKET != INDEPENDENT_TOUCHDOWN_CONFIRMED" "$MD" || fail "md_missing_touchdown_boundary"
grep -q "COACHES_CORNER_MENU_HASH_PACKET != AUTHORITY_TRUE" "$MD" || fail "md_missing_authority_boundary"

echo "COACHES_CORNER_MENU_HASH_PACKET_OK"
echo "packet_structure=PASS"
echo "content_hash_attached=false"
echo "independent_public_verification=false"
echo "field_state=GOAL_LINE_REVIEW"
echo "authority=false"
echo "family_gate=SOVEREIGN"
echo "no_fake_green=true"
echo "next_packet=COACHES_CORNER_MENU_SOURCE_BYTES_V0_1"
