#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-.}"
BASE="$ROOT/FAMILY/receipts"
MD="$BASE/DOCTRINE_SPINE_V0_1.md"
JSON="$BASE/DOCTRINE_SPINE_INDEX_V0_1.json"

fail() {
  echo "NO_FAKE_GREEN reason=$1" >&2
  exit 1
}

[[ -f "$MD" ]] || fail "missing_doctrine_spine_md"
[[ -f "$JSON" ]] || fail "missing_doctrine_spine_json"

grep -q "DOCTRINE_SPINE_LOCKED" "$MD" || fail "md_missing_spine_locked"
grep -q "WITNESS_GREEN" "$MD" || fail "md_missing_witness_green"
grep -q "TRUTH_YELLOW" "$MD" || fail "md_missing_truth_yellow"
grep -q "AUTHORITY_FALSE" "$MD" || fail "md_missing_authority_false"
grep -q "CARE_OVER_CLAIM_ACTIVE" "$MD" || fail "md_missing_care_over_claim"
grep -q "REPAIR_OVER_ERASURE_ACTIVE" "$MD" || fail "md_missing_repair_over_erasure"
grep -q "PUBLIC_REPO_WITNESS_ONLY" "$MD" || fail "md_missing_public_repo_witness_only"
grep -q "FAMILY_GATE_SOVEREIGN" "$MD" || fail "md_missing_family_gate"
grep -q "NO_FAKE_GREEN_ACTIVE" "$MD" || fail "md_missing_no_fake_green"

grep -q '"status": "DOCTRINE_SPINE_LOCKED"' "$JSON" || fail "json_wrong_status"
grep -q '"witness_green": true' "$JSON" || fail "json_witness_not_green"
grep -q '"truth_yellow": true' "$JSON" || fail "json_truth_yellow_missing"
grep -q '"authority": false' "$JSON" || fail "json_authority_not_false"
grep -q '"care_over_claim": true' "$JSON" || fail "json_care_over_claim_missing"
grep -q '"repair_over_erasure": true' "$JSON" || fail "json_repair_over_erasure_missing"
grep -q '"public_repo_witness_only": true' "$JSON" || fail "json_public_repo_witness_missing"
grep -q '"family_gate": "SOVEREIGN"' "$JSON" || fail "json_family_gate_not_sovereign"
grep -q '"no_fake_green": true' "$JSON" || fail "json_no_fake_green_missing"
grep -q '"next_packet": "IRON_BOWL_BROADCAST_ASSET_POINTER_V0_1"' "$JSON" || fail "json_next_packet_missing"
grep -q '"broadcast_pointer_needed": true' "$JSON" || fail "json_pointer_needed_missing"
grep -q '"transcript_or_quote_not_claimed": true' "$JSON" || fail "json_quote_boundary_missing"

grep -q "DOCTRINE_SPINE != AUTHORITY_TRUE" "$MD" || fail "md_missing_authority_true_boundary"

echo "DOCTRINE_SPINE_OK"
echo "witness_green=true"
echo "truth_yellow=true"
echo "authority=false"
echo "care_over_claim=true"
echo "repair_over_erasure=true"
echo "public_repo_witness_only=true"
echo "family_gate=SOVEREIGN"
echo "broadcast_pointer_needed=true"
echo "transcript_or_quote_not_claimed=true"
echo "no_fake_green=true"
echo "next_packet=IRON_BOWL_BROADCAST_ASSET_POINTER_V0_1"
