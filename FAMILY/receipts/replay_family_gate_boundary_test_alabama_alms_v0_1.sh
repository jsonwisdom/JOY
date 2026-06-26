#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-.}"
BASE="$ROOT/FAMILY/receipts"
RESULT_MD="$BASE/FAMILY_GATE_BOUNDARY_TEST_ALABAMA_ALMS_V0_1.md"
RESULT_JSON="$BASE/FAMILY_GATE_BOUNDARY_TEST_ALABAMA_ALMS_INDEX_V0_1.json"
MERGE_JSON="$BASE/ALABAMA_ALMS_BOSS_BRE_LIBRARIAN_HEIDEE_MERGE_INDEX_V0_1.json"

fail() {
  echo "NO_FAKE_GREEN reason=$1" >&2
  exit 1
}

[[ -f "$RESULT_MD" ]] || fail "missing_boundary_test_md"
[[ -f "$RESULT_JSON" ]] || fail "missing_boundary_test_json"
[[ -f "$MERGE_JSON" ]] || fail "missing_merge_json"

grep -q "STATIC_REPLAY_GATE_PASS" "$RESULT_MD" || fail "md_missing_static_pass"
grep -q "FAMILY_GATE_SOVEREIGN" "$RESULT_MD" || fail "md_missing_family_gate_sovereign"
grep -q "AUTHORITY_FALSE" "$RESULT_MD" || fail "md_missing_authority_false"
grep -q "BACKGROUND_MONITORING_FALSE" "$RESULT_MD" || fail "md_missing_background_false"
grep -q "NO_FAKE_GREEN_ACTIVE" "$RESULT_MD" || fail "md_missing_no_fake_green"

grep -q '"status": "STATIC_REPLAY_GATE_PASS"' "$RESULT_JSON" || fail "json_missing_static_pass"
grep -q '"family_gate": "SOVEREIGN"' "$RESULT_JSON" || fail "json_missing_family_gate_sovereign"
grep -q '"authority": false' "$RESULT_JSON" || fail "json_authority_not_false"
grep -q '"background_monitoring": false' "$RESULT_JSON" || fail "json_background_not_false"
grep -q '"no_fake_green": true' "$RESULT_JSON" || fail "json_no_fake_green_missing"

grep -q '"merge_bridge": "ACTIVE"' "$MERGE_JSON" || fail "merge_json_bridge_not_active"
grep -q '"family_gate": "SOVEREIGN"' "$MERGE_JSON" || fail "merge_json_family_gate_not_sovereign"

echo "FAMILY_GATE_BOUNDARY_TEST_OK"
echo "static_replay_gate=PASS"
echo "family_gate=SOVEREIGN"
echo "authority=false"
echo "background_monitoring=false"
echo "no_fake_green=true"
echo "next_packet=ALABAMA_LAW_PUBLIC_LESSON_CARD_V0_1"
