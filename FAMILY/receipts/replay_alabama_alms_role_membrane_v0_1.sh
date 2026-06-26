#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-.}"
BASE="$ROOT/FAMILY/receipts"
MD="$BASE/ALABAMA_ALMS_BOSS_BRE_LIBRARIAN_HEIDEE_MERGE_V0_1.md"
JSON="$BASE/ALABAMA_ALMS_BOSS_BRE_LIBRARIAN_HEIDEE_MERGE_INDEX_V0_1.json"

fail() {
  echo "NO_FAKE_GREEN reason=$1" >&2
  exit 1
}

[[ -f "$MD" ]] || fail "missing_md_receipt"
[[ -f "$JSON" ]] || fail "missing_json_index"

grep -q "MERGE_BRIDGE_ACTIVE" "$MD" || fail "md_missing_merge_bridge_active"
grep -q "ALABAMA_ALMS_REPLAY_ENGINE_LINKED" "$MD" || fail "md_missing_alabama_alms_link"
grep -q "BOSS_BRE_FAMILY_SIDE_LINKED" "$MD" || fail "md_missing_boss_bre_link"
grep -q "LIBRARIAN_SUGGESTION_LAYER_LINKED" "$MD" || fail "md_missing_librarian_link"
grep -q "HEIDEE_JOY_TRAINING_PURPOSE_LINKED" "$MD" || fail "md_missing_heidee_joy_link"
grep -q "FAMILY_GATE_SOVEREIGN" "$MD" || fail "md_missing_family_gate_sovereign"
grep -q "AUTHORITY_FALSE" "$MD" || fail "md_missing_authority_false"
grep -q "NO_FAKE_GREEN_ACTIVE" "$MD" || fail "md_missing_no_fake_green"

grep -q '"status": "V0_1_LIVE"' "$JSON" || fail "json_not_v0_1_live"
grep -q '"merge_bridge": "ACTIVE"' "$JSON" || fail "json_missing_active_bridge"
grep -q '"family_gate": "SOVEREIGN"' "$JSON" || fail "json_missing_family_gate_sovereign"
grep -q '"authority": false' "$JSON" || fail "json_authority_not_false"
grep -q '"private_child_data_publication": false' "$JSON" || fail "json_private_child_data_boundary_missing"
grep -q '"background_monitoring": false' "$JSON" || fail "json_background_monitoring_boundary_missing"
grep -q '"no_fake_green": true' "$JSON" || fail "json_no_fake_green_missing"

grep -q "MERGE != FAMILY_APPROVAL" "$MD" || fail "md_family_approval_boundary_missing"
grep -q "MERGE != CHILD_CONSENT" "$MD" || fail "md_child_consent_boundary_missing"
grep -q "MERGE != AUTHORITY_TRUE" "$MD" || fail "md_authority_boundary_missing"
grep -q "MERGE != BACKGROUND_MONITORING" "$MD" || fail "md_background_boundary_missing"

echo "ROLE_MEMBRANE_REPLAY_OK"
echo "merge_bridge=ACTIVE"
echo "family_gate=SOVEREIGN"
echo "authority=false"
echo "private_child_data_publication=false"
echo "background_monitoring=false"
echo "no_fake_green=true"
