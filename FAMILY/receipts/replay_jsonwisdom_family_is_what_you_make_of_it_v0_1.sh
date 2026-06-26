#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-.}"
BASE="$ROOT/FAMILY/receipts"
MD="$BASE/JSONWISDOM_FAMILY_IS_WHAT_YOU_MAKE_OF_IT_V0_1.md"
JSON="$BASE/JSONWISDOM_FAMILY_IS_WHAT_YOU_MAKE_OF_IT_INDEX_V0_1.json"

fail() {
  echo "NO_FAKE_GREEN reason=$1" >&2
  exit 1
}

[[ -f "$MD" ]] || fail "missing_family_doctrine_md"
[[ -f "$JSON" ]] || fail "missing_family_doctrine_json"

grep -q "FAMILY_DOCTRINE_RECEIPT_INDEXED" "$MD" || fail "md_missing_doctrine_indexed"
grep -q "FAMILY_IS_WHAT_YOU_MAKE_OF_IT" "$MD" || fail "md_missing_core_line"
grep -q "CARE_OVER_CLAIM" "$MD" || fail "md_missing_care_over_claim"
grep -q "REPAIR_OVER_ERASURE" "$MD" || fail "md_missing_repair_over_erasure"
grep -q "PRIVATE_DETAILS_EXPOSED_FALSE" "$MD" || fail "md_missing_private_boundary"
grep -q "FAMILY_APPROVAL_NOT_CLAIMED" "$MD" || fail "md_missing_approval_boundary"
grep -q "AUTHORITY_FALSE" "$MD" || fail "md_missing_authority_false"
grep -q "NO_FAKE_GREEN_ACTIVE" "$MD" || fail "md_missing_no_fake_green"

grep -q '"status": "FAMILY_DOCTRINE_RECEIPT_INDEXED"' "$JSON" || fail "json_wrong_status"
grep -q '"family_is_what_you_make_of_it": true' "$JSON" || fail "json_core_line_not_true"
grep -q '"private_details_exposed": false' "$JSON" || fail "json_private_details_not_false"
grep -q '"family_approval_claimed": false' "$JSON" || fail "json_approval_not_false"
grep -q '"authority": false' "$JSON" || fail "json_authority_not_false"
grep -q '"family_gate": "SOVEREIGN"' "$JSON" || fail "json_family_gate_not_sovereign"
grep -q '"no_fake_green": true' "$JSON" || fail "json_no_fake_green_missing"

grep -q "FAMILY_IS_WHAT_YOU_MAKE_OF_IT != FAMILY_APPROVAL" "$MD" || fail "md_missing_family_approval_boundary"
grep -q "FAMILY_IS_WHAT_YOU_MAKE_OF_IT != AUTHORITY_TRUE" "$MD" || fail "md_missing_authority_true_boundary"

echo "JSONWISDOM_FAMILY_DOCTRINE_OK"
echo "family_is_what_you_make_of_it=true"
echo "care_over_claim=true"
echo "repair_over_erasure=true"
echo "private_details_exposed=false"
echo "family_approval_claimed=false"
echo "authority=false"
echo "family_gate=SOVEREIGN"
echo "no_fake_green=true"
