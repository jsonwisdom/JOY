#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-.}"
BASE="$ROOT/FAMILY/receipts"
MD="$BASE/ELMORE_COUNTY_EMS_PUBLIC_SERVICE_WITNESS_V0_1.md"
JSON="$BASE/ELMORE_COUNTY_EMS_PUBLIC_SERVICE_WITNESS_INDEX_V0_1.json"

fail() {
  echo "NO_FAKE_GREEN reason=$1" >&2
  exit 1
}

[[ -f "$MD" ]] || fail "missing_elmore_ems_md"
[[ -f "$JSON" ]] || fail "missing_elmore_ems_json"

grep -q "ELMORE_COUNTY_EMS_REPLAY_INDEXED" "$MD" || fail "md_missing_elmore_indexed"
grep -q "PUBLIC_SERVICE_WITNESS_ONLY" "$MD" || fail "md_missing_public_witness"
grep -q "DIRECT_COUNTY_EMS_PAGE_NOT_FOUND_IN_THIS_RUN" "$MD" || fail "md_missing_direct_county_limit"
grep -q "TRUTH_STATE_YELLOW" "$MD" || fail "md_missing_truth_yellow"
grep -q "SERVICE_COVERAGE_FINAL_FALSE" "$MD" || fail "md_missing_service_coverage_limit"
grep -q "FAMILY_GATE_SOVEREIGN" "$MD" || fail "md_missing_family_gate"
grep -q "AUTHORITY_FALSE" "$MD" || fail "md_missing_authority_false"
grep -q "NO_FAKE_GREEN_ACTIVE" "$MD" || fail "md_missing_no_fake_green"

grep -q '"status": "PASS_WITH_LIMITS"' "$JSON" || fail "json_wrong_status"
grep -q '"direct_county_ems_page_found": false' "$JSON" || fail "json_direct_county_limit_missing"
grep -q '"official_municipal_source_reused": true' "$JSON" || fail "json_municipal_source_not_reused"
grep -q '"emergency_phone_911_observed": true' "$JSON" || fail "json_911_not_observed"
grep -q '"medical_advice": false' "$JSON" || fail "json_medical_advice_not_false"
grep -q '"county_service_coverage_final": false' "$JSON" || fail "json_county_coverage_not_false"
grep -q '"truth_state": "YELLOW"' "$JSON" || fail "json_truth_not_yellow"
grep -q '"family_gate": "SOVEREIGN"' "$JSON" || fail "json_family_gate_not_sovereign"
grep -q '"authority": false' "$JSON" || fail "json_authority_not_false"
grep -q '"no_fake_green": true' "$JSON" || fail "json_no_fake_green_missing"

grep -q "ELMORE_EMS_PACKET != MEDICAL_ADVICE" "$MD" || fail "md_missing_medical_boundary"
grep -q "ELMORE_EMS_PACKET != COUNTY_SERVICE_COVERAGE_FINAL" "$MD" || fail "md_missing_coverage_boundary"
grep -q "ELMORE_EMS_PACKET != AUTHORITY_TRUE" "$MD" || fail "md_missing_authority_boundary"

echo "ELMORE_COUNTY_EMS_PUBLIC_SERVICE_WITNESS_OK"
echo "elmore_county_ems_replay=PASS_WITH_LIMITS"
echo "direct_county_ems_page_found=false"
echo "official_municipal_source_reused=true"
echo "emergency_phone_911_observed=true"
echo "medical_advice=false"
echo "county_service_coverage_final=false"
echo "truth_state=YELLOW"
echo "family_gate=SOVEREIGN"
echo "authority=false"
echo "no_fake_green=true"
echo "next_packet=DIRECT_ELMORE_COUNTY_EMS_SOURCE_PACKET_IF_FOUND"
