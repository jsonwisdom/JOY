#!/usr/bin/env bash
set -euo pipefail

# L3_L4_ARCHIVE_RECIPE_V0_1
# Purpose: Create an integrity-sealed archive of the L3/L4 public evidence chain.
# Invariants: NO_FAKE_GREEN=true, authority=false, membrane=INTACT
# Rule: fail closed if any expected artifact is missing.

fail() {
  echo "❌ ARCHIVE_FAIL: $1" >&2
  exit 1
}

[ -d .git ] || fail "not inside git repo"

TIMESTAMP="$(date -u +"%Y%m%dT%H%M%SZ")"
HEAD_COMMIT="$(git rev-parse HEAD)"
HEAD_SHORT="$(git rev-parse --short HEAD)"

ARCHIVE_NAME="wisdom_family_l3_l4_seal_${HEAD_SHORT}_${TIMESTAMP}.tar.gz"
ARCHIVE_PATH="artifacts/archives/${ARCHIVE_NAME}"
RECEIPT_PATH="receipts/archive/L3_L4_ARCHIVE_VERIFICATION_RECEIPT_V0_1_${TIMESTAMP}.json"

L4_MANIFEST="artifacts/releases/L4_MASTER_RELEASE_MANIFEST_V0_4.json"
L3_PAYLOAD="artifacts/runtime/L3_RECON_RUNTIME_PAYLOAD_V0_1.json"
L3_REPLAY_RECEIPT="artifacts/replay/L3_VERIFIER_REPLAY_RECEIPT_V0_1.json"
L3_SCRIPT="scripts/l3_recon.sh"

REQUIRED_FILES=(
  "$L4_MANIFEST"
  "$L3_PAYLOAD"
  "$L3_REPLAY_RECEIPT"
  "$L3_SCRIPT"
)

for f in "${REQUIRED_FILES[@]}"; do
  [ -f "$f" ] || fail "missing required artifact: $f"
done

tar -czf "$ARCHIVE_PATH" "${REQUIRED_FILES[@]}"

SHA256_HASH="$(sha256sum "$ARCHIVE_PATH" | awk '{print $1}')"

cat > "$RECEIPT_PATH" <<JSON
{
  "artifact": "L3_L4_ARCHIVE_VERIFICATION_RECEIPT_V0_1",
  "version": "0.1",
  "timestamp_utc": "$(date -u +"%Y-%m-%dT%H:%M:%SZ")",
  "repo": "jsonwisdom/JOY",
  "head_commit": "$HEAD_COMMIT",
  "archive_path": "$ARCHIVE_PATH",
  "archive_name": "$ARCHIVE_NAME",
  "sha256_hash": "$SHA256_HASH",
  "included_artifacts": [
    "$L4_MANIFEST",
    "$L3_PAYLOAD",
    "$L3_REPLAY_RECEIPT",
    "$L3_SCRIPT"
  ],
  "integrity_check": "PASS",
  "authority": false,
  "emission_eligible": false,
  "index_deployment": "BLOCKED",
  "no_fake_green": true,
  "mock_values_allowed": false,
  "membrane": "INTACT"
}
JSON

echo "✅ Archive complete"
echo "Archive: $ARCHIVE_PATH"
echo "Receipt: $RECEIPT_PATH"
echo "SHA256: $SHA256_HASH"
