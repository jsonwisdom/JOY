#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-.}"
BASE="$ROOT/FAMILY/receipts"
MD="$BASE/WISDOM_FAMILY_PURPOSE_MAP_V0_1.md"
JSON="$BASE/WISDOM_FAMILY_PURPOSE_MAP_INDEX_V0_1.json"

fail() {
  echo "NO_FAKE_GREEN reason=$1" >&2
  exit 1
}

[[ -f "$MD" ]] || fail "missing_family_purpose_md"
[[ -f "$JSON" ]] || fail "missing_family_purpose_json"

grep -q "FAMILY_PURPOSE_MAP_INDEXED" "$MD" || fail "md_missing_indexed"
grep -q "PUBLIC_SAFE_SYMBOLIC_PURPOSE_ONLY" "$MD" || fail "md_missing_public_safe"
grep -q "PRIVATE_DETAILS_EXPOSED_FALSE" "$MD" || fail "md_missing_private_boundary"
grep -q "FAMILY_APPROVAL_NOT_CLAIMED" "$MD" || fail "md_missing_approval_boundary"
grep -q "AUTHORITY_FALSE" "$MD" || fail "md_missing_authority_false"
grep -q "NO_FAKE_GREEN_ACTIVE" "$MD" || fail "md_missing_no_fake_green"

grep -q '"status": "FAMILY_PURPOSE_MAP_INDEXED"' "$JSON" || fail "json_wrong_status"
grep -q '"family_members_added_with_purpose": "PASS"' "$JSON" || fail "json_members_not_pass"
grep -q '"private_details_exposed": false' "$JSON" || fail "json_private_details_not_false"
grep -q '"public_biography": false' "$JSON" || fail "json_public_biography_not_false"
grep -q '"family_approval_claimed": false' "$JSON" || fail "json_family_approval_not_false"
grep -q '"authority": false' "$JSON" || fail "json_authority_not_false"
grep -q '"family_gate": "SOVEREIGN"' "$JSON" || fail "json_family_gate_not_sovereign"
grep -q '"no_fake_green": true' "$JSON" || fail "json_no_fake_green_missing"

for lane in JAY_WISDOM DADDY_WISDOM MRS_WISDOM HEIDEE JAYCEE BREALEE BRIANNA BOSS_BRENDA_BOSS_BRE MARYDEE LEEANNE_LEANNE BEANNE GRAMMY GAGA AL LIBRARIAN; do
  grep -q "$lane" "$JSON" || fail "json_missing_lane_$lane"
done

grep -q "FAMILY_PURPOSE_MAP != FAMILY_APPROVAL" "$MD" || fail "md_missing_family_approval_boundary"
grep -q "FAMILY_PURPOSE_MAP != AUTHORITY_TRUE" "$MD" || fail "md_missing_authority_true_boundary"

echo "WISDOM_FAMILY_PURPOSE_MAP_OK"
echo "family_members_added_with_purpose=PASS"
echo "private_details_exposed=false"
echo "public_biography=false"
echo "family_approval_claimed=false"
echo "authority=false"
echo "truth_state=YELLOW_WITH_GREEN_SCOPED_CONTINUITY"
echo "family_gate=SOVEREIGN"
echo "no_fake_green=true"
