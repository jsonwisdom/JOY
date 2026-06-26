#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-.}"
BASE="$ROOT/FAMILY/receipts"
MD="$BASE/EMS_WETUMPKA_OFFICIAL_SOURCE_PACKET_V0_1.md"
JSON="$BASE/EMS_WETUMPKA_OFFICIAL_SOURCE_PACKET_INDEX_V0_1.json"

fail() {
  echo "NO_FAKE_GREEN reason=$1" >&2
  exit 1
}

[[ -f "$MD" ]] || fail "missing_ems_md"
[[ -f "$JSON" ]] || fail "missing_ems_json"

grep -q "OFFICIAL_CITY_FIRE_EMS_SOURCE_ATTACHED" "$MD" || fail "md_missing_official_source"
grep -q "EXTERNAL_EMERGENCY_BOUNDARY_MAPPED" "$MD" || fail "md_missing_emergency_boundary"
grep -q "TRUTH_STATE_YELLOW" "$MD" || fail "md_missing_truth_yellow"
grep -q "PUBLIC_SERVICE_WITNESS_ONLY" "$MD" || fail "md_missing_public_witness"
grep -q "FAMILY_GATE_SOVEREIGN" "$MD" || fail "md_missing_family_gate"
grep -q "AUTHORITY_FALSE" "$MD" || fail "md_missing_authority_false"
grep -q "NO_FAKE_GREEN_ACTIVE" "$MD" || fail "md_missing_no_fake_green"

grep -q '"status": "OFFICIAL_CITY_FIRE_EMS_SOURCE_ATTACHED"' "$JSON" || fail "json_wrong_status"
grep -q '"official_city_source_attached": true' "$JSON" || fail "json_official_source_not_true"
grep -q '"emergency_phone_911_observed": true' "$JSON" || fail "json_911_not_observed"
grep -q '"trusted_adult_notification_delays_emergency_call": false' "$JSON" || fail "json_delay_boundary_missing"
grep -q '"medical_advice": false' "$JSON" || fail "json_medical_advice_not_false"
grep -q '"service_coverage_final": false' "$JSON" || fail "json_service_coverage_not_false"
grep -q '"truth_state": "YELLOW"' "$JSON" || fail "json_truth_not_yellow"
grep -q '"family_gate": "SOVEREIGN"' "$JSON" || fail "json_family_gate_not_sovereign"
grep -q '"authority": false' "$JSON" || fail "json_authority_not_false"
grep -q '"no_fake_green": true' "$JSON" || fail "json_no_fake_green_missing"

grep -q "EMS_PACKET != MEDICAL_ADVICE" "$MD" || fail "md_missing_medical_boundary"
grep -q "EMS_PACKET != AUTHORITY_TRUE" "$MD" || fail "md_missing_authority_boundary"

echo "EMS_WETUMPKA_OFFICIAL_SOURCE_PACKET_OK"
echo "official_city_source_attached=true"
echo "emergency_phone_911_observed=true"
echo "trusted_adult_notification_delays_emergency_call=false"
echo "medical_advice=false"
echo "service_coverage_final=false"
echo "truth_state=YELLOW"
echo "family_gate=SOVEREIGN"
echo "authority=false"
echo "no_fake_green=true"
echo "next_packet=EMERGENCY_MANAGER_PURPOSE_LAYER_REVIEW_MARY_V0_1"
