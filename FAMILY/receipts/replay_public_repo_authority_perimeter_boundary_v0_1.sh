#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-.}"
BASE="$ROOT/FAMILY/receipts"
MD="$BASE/PUBLIC_REPO_AUTHORITY_PERIMETER_BOUNDARY_V0_1.md"
JSON="$BASE/PUBLIC_REPO_AUTHORITY_PERIMETER_BOUNDARY_INDEX_V0_1.json"

fail() {
  echo "NO_FAKE_GREEN reason=$1" >&2
  exit 1
}

[[ -f "$MD" ]] || fail "missing_perimeter_md"
[[ -f "$JSON" ]] || fail "missing_perimeter_json"

grep -q "PUBLIC_REPO_WITNESS_ONLY" "$MD" || fail "md_missing_public_repo_witness_only"
grep -q "FAMILY_AUTHORITY_NOT_PUBLIC_REPO_RESOLVED" "$MD" || fail "md_missing_family_authority_boundary"
grep -q "TRUTH_YELLOW_ALLOWED" "$MD" || fail "md_missing_truth_yellow_allowed"
grep -q "AUTHORITY_FALSE" "$MD" || fail "md_missing_authority_false"
grep -q "NO_FAKE_GREEN_ACTIVE" "$MD" || fail "md_missing_no_fake_green"

grep -q '"public_repo_witness_only": true' "$JSON" || fail "json_missing_public_repo_witness_only"
grep -q '"github_green_transport_only": true' "$JSON" || fail "json_missing_github_green_transport_only"
grep -q '"truth_yellow_allowed": true' "$JSON" || fail "json_missing_truth_yellow_allowed"
grep -q '"family_authority_public_repo_resolved": false' "$JSON" || fail "json_family_authority_boundary_missing"
grep -q '"authority": false' "$JSON" || fail "json_authority_not_false"
grep -q '"background_monitoring": false' "$JSON" || fail "json_background_monitoring_not_false"
grep -q '"no_fake_green": true' "$JSON" || fail "json_no_fake_green_missing"

grep -q "PUBLIC_REPO_PERIMETER != FAMILY_APPROVAL" "$MD" || fail "md_missing_family_approval_boundary"
grep -q "PUBLIC_REPO_PERIMETER != AUTHORITY_TRUE" "$MD" || fail "md_missing_authority_true_boundary"
grep -q "PUBLIC_REPO_PERIMETER != BACKGROUND_MONITORING" "$MD" || fail "md_missing_background_boundary"

echo "PUBLIC_REPO_AUTHORITY_PERIMETER_OK"
echo "public_repo_witness_only=true"
echo "github_green_transport_only=true"
echo "truth_yellow_allowed=true"
echo "family_authority_public_repo_resolved=false"
echo "authority=false"
echo "background_monitoring=false"
echo "no_fake_green=true"
echo "next_packet=COACHES_CORNER_MENU_HASH_PACKET"
