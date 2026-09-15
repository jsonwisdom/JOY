#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-.}"
BASE="$ROOT/FAMILY/receipts"
MD="$BASE/ALABAMA_STATE_REVERSE_REPLAY_BOUNDARY_COLLAPSE_V0_1.md"
JSON="$BASE/ALABAMA_STATE_REVERSE_REPLAY_BOUNDARY_COLLAPSE_INDEX_V0_1.json"

fail() {
  printf 'FAIL: %s\n' "$1" >&2
  exit 1
}

pass() {
  printf 'PASS: %s\n' "$1"
}

[[ -f "$MD" ]] || fail "missing markdown artifact: $MD"
[[ -f "$JSON" ]] || fail "missing json index: $JSON"

required_md=(
  'CONNECTED_GRAPH != COLLAPSED_GRAPH'
  'PARENT != UNIVERSITY'
  'UNIVERSITY != STATE_OF_ALABAMA'
  'STUDENT_ATTENDANCE != PARENTAL_AUTHORITY_TRANSFER'
  'AI_CLASSIFICATION != LEGAL_DETERMINATION'
  'FAMILY_RELATIONSHIP != LEGAL_AUTHORITY'
  'DAD_ROLE != PUBLIC_AUTHORITY'
  'COLLAPSED_JOIN = REJECTED'
  'AUTHORITY_CREATED = FALSE'
)

for token in "${required_md[@]}"; do
  grep -Fq "$token" "$MD" || fail "markdown invariant absent: $token"
done
pass "markdown boundary invariants present"

python3 - "$JSON" <<'PY'
import json
import sys

path = sys.argv[1]
with open(path, 'r', encoding='utf-8') as f:
    d = json.load(f)

assert d['repo'] == 'jsonwisdom/JOY'
assert d['authority_created'] is False
assert d['consent_created'] is False
assert d['legal_finding_created'] is False
assert d['no_fake_green'] is True
assert d['core_rule'] == 'CONNECTED_GRAPH != COLLAPSED_GRAPH'
assert d['collapse_test']['classification'] == 'BOUNDARY_COLLAPSE_REJECTED'

required_membranes = {
    'PARENT != UNIVERSITY',
    'UNIVERSITY != STATE_OF_ALABAMA',
    'STUDENT_ATTENDANCE != PARENTAL_AUTHORITY_TRANSFER',
    'AI_CLASSIFICATION != LEGAL_DETERMINATION',
    'FAMILY_RELATIONSHIP != LEGAL_AUTHORITY',
    'DAD_ROLE != PUBLIC_AUTHORITY',
}
assert required_membranes.issubset(set(d['membranes']))

assert len(d['prior_work_receipts']) >= 5
for receipt in d['prior_work_receipts']:
    sha = receipt['git_blob_sha']
    assert len(sha) == 40 and all(c in '0123456789abcdef' for c in sha)

join_required = set(d['join_policy']['required'])
assert join_required == {
    'independent_receipts',
    'matching_join_fields',
    'compatible_provenance',
    'no_scope_conflict',
}

assert d['drive_source_only']['write_performed'] is False
print('PASS: json index parses and authority/consent/join gates hold')
PY

# Git object SHA lanes are intentionally distinct from file SHA-256 lanes.
# This verifier reports local file SHA-256 values only; it does not claim they
# equal Git blob SHA, commit SHA, JCS SHA-256, or Merkle roots.
if command -v sha256sum >/dev/null 2>&1; then
  MD_SHA256="$(sha256sum "$MD" | awk '{print $1}')"
  JSON_SHA256="$(sha256sum "$JSON" | awk '{print $1}')"
elif command -v shasum >/dev/null 2>&1; then
  MD_SHA256="$(shasum -a 256 "$MD" | awk '{print $1}')"
  JSON_SHA256="$(shasum -a 256 "$JSON" | awk '{print $1}')"
else
  fail "no SHA-256 utility found"
fi

printf 'FILE_SHA256 markdown=%s\n' "$MD_SHA256"
printf 'FILE_SHA256 json=%s\n' "$JSON_SHA256"
printf '%s\n' 'PASS: BLOB_SHA != COMMIT_SHA != FILE_SHA256 unless separately proven under identical preimage rules'
printf '%s\n' 'RESULT: CONNECTED_GRAPH allowed; COLLAPSED_GRAPH rejected; AUTHORITY_CREATED=false'
