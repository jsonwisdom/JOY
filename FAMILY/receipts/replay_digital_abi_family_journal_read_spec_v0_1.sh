#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-.}"
BASE="$ROOT/FAMILY/receipts"
MD="$BASE/DIGITAL_ABI_FAMILY_JOURNAL_READ_SPEC_V0_1.md"
JSON="$BASE/DIGITAL_ABI_FAMILY_JOURNAL_READ_SPEC_INDEX_V0_1.json"

fail() {
  echo "NO_FAKE_GREEN reason=$1" >&2
  exit 1
}

[[ -f "$MD" ]] || fail "missing_digital_abi_md"
[[ -f "$JSON" ]] || fail "missing_digital_abi_json"

grep -q "DIGITAL_ABI_READ_SPEC_INDEXED" "$MD" || fail "md_missing_read_spec_indexed"
grep -q "READ_ONLY_MIRROR_ACTIVE" "$MD" || fail "md_missing_read_only_mirror"
grep -q "MUTATION_PATH_SEALED" "$MD" || fail "md_missing_mutation_sealed"
grep -q "OFFLINE_RECEIPT_SOURCE_OF_TRUTH" "$MD" || fail "md_missing_offline_source_truth"
grep -q "WITNESS_CREATION_FORBIDDEN" "$MD" || fail "md_missing_witness_forbidden"
grep -q "EXECUTION_HASH_CREATION_FORBIDDEN" "$MD" || fail "md_missing_hash_forbidden"
grep -q "GOLD_STATE_CREATION_FORBIDDEN" "$MD" || fail "md_missing_gold_forbidden"
grep -q "AUTHORITY_FALSE" "$MD" || fail "md_missing_authority_false"
grep -q "NO_FAKE_GREEN_ACTIVE" "$MD" || fail "md_missing_no_fake_green"

grep -q '"status": "DIGITAL_ABI_READ_SPEC_INDEXED"' "$JSON" || fail "json_wrong_status"
grep -q '"read_only_mirror": true' "$JSON" || fail "json_read_only_missing"
grep -q '"mutation_path_sealed": true' "$JSON" || fail "json_mutation_sealed_missing"
grep -q '"offline_receipt_source_of_truth": true' "$JSON" || fail "json_offline_source_missing"
grep -q '"witness_creation_forbidden": true' "$JSON" || fail "json_witness_forbidden_missing"
grep -q '"execution_hash_creation_forbidden": true' "$JSON" || fail "json_hash_forbidden_missing"
grep -q '"gold_state_creation_forbidden": true' "$JSON" || fail "json_gold_forbidden_missing"
grep -q '"authority": false' "$JSON" || fail "json_authority_not_false"
grep -q '"no_fake_green": true' "$JSON" || fail "json_no_fake_green_missing"
grep -q '"may_create": \[\]' "$JSON" || fail "json_may_create_not_empty"
grep -q '"next_packet": "WITNESS_FINGERPRINT_PROTOCOL_V0_1"' "$JSON" || fail "json_next_packet_missing"

grep -q "DIGITAL_ABI_READ_SPEC != AUTHORITY_TRUE" "$MD" || fail "md_missing_authority_boundary"

echo "DIGITAL_ABI_FAMILY_JOURNAL_READ_SPEC_OK"
echo "read_only_mirror=true"
echo "mutation_path_sealed=true"
echo "offline_receipt_source_of_truth=true"
echo "witness_creation_forbidden=true"
echo "execution_hash_creation_forbidden=true"
echo "gold_state_creation_forbidden=true"
echo "authority=false"
echo "no_fake_green=true"
echo "next_packet=WITNESS_FINGERPRINT_PROTOCOL_V0_1"
