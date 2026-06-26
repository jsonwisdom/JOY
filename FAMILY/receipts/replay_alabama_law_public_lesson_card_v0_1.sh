#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-.}"
BASE="$ROOT/FAMILY/receipts"
MD="$BASE/ALABAMA_LAW_PUBLIC_LESSON_CARD_V0_1.md"
JSON="$BASE/ALABAMA_LAW_PUBLIC_LESSON_CARD_INDEX_V0_1.json"

fail() {
  echo "NO_FAKE_GREEN reason=$1" >&2
  exit 1
}

[[ -f "$MD" ]] || fail "missing_lesson_card_md"
[[ -f "$JSON" ]] || fail "missing_lesson_card_json"

grep -q "LESSON_CARD_LIVE" "$MD" || fail "md_missing_lesson_card_live"
grep -q "PUBLIC_SAFE_TRAINING_PAYLOAD" "$MD" || fail "md_missing_public_safe_training_payload"
grep -q "HEIDEE_JOY_SCAFFOLD" "$MD" || fail "md_missing_heidee_joy_scaffold"
grep -q "FAMILY_GATE_SOVEREIGN" "$MD" || fail "md_missing_family_gate_sovereign"
grep -q "LEGAL_ADVICE_FALSE" "$MD" || fail "md_missing_legal_advice_false"
grep -q "AUTHORITY_FALSE" "$MD" || fail "md_missing_authority_false"
grep -q "NO_FAKE_GREEN_ACTIVE" "$MD" || fail "md_missing_no_fake_green"

grep -q '"status": "LESSON_CARD_LIVE"' "$JSON" || fail "json_not_live"
grep -q '"legal_advice": false' "$JSON" || fail "json_legal_advice_not_false"
grep -q '"authority": false' "$JSON" || fail "json_authority_not_false"
grep -q '"private_family_data_publication": false' "$JSON" || fail "json_private_family_data_boundary_missing"
grep -q '"background_monitoring": false' "$JSON" || fail "json_background_monitoring_boundary_missing"
grep -q '"family_gate": "SOVEREIGN"' "$JSON" || fail "json_family_gate_not_sovereign"
grep -q '"no_fake_green": true' "$JSON" || fail "json_no_fake_green_missing"

grep -q "LESSON_CARD != LEGAL_ADVICE" "$MD" || fail "md_legal_advice_boundary_missing"
grep -q "LESSON_CARD != FAMILY_APPROVAL" "$MD" || fail "md_family_approval_boundary_missing"
grep -q "LESSON_CARD != AUTHORITY" "$MD" && fail "md_contains_forbidden_ambiguous_authority_boundary"

echo "ALABAMA_LAW_PUBLIC_LESSON_CARD_OK"
echo "lesson_card_ingestion=PASS"
echo "public_safe=true"
echo "legal_advice=false"
echo "authority=false"
echo "family_gate=SOVEREIGN"
echo "background_monitoring=false"
echo "no_fake_green=true"
echo "next_packet=COACHES_CORNER_MENU_HASH_PACKET"
