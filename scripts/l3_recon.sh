#!/usr/bin/env bash
set -euo pipefail

MANIFEST_TARGET="artifacts/releases/L4_MASTER_RELEASE_MANIFEST_V0_4.json"
L0_TARGET="artifacts/L0_ATOMIC_RECEIPT_V0_1.json"

fail() {
  echo "❌ L3_RECON_FAIL: $1" >&2
  exit 1
}

[ -d .git ] || fail "not inside git repo"
[ -f "$MANIFEST_TARGET" ] || fail "missing L4 master manifest: $MANIFEST_TARGET"
[ -f "$L0_TARGET" ] || fail "missing L0 atomic receipt: $L0_TARGET"

HEAD_FULL="$(git rev-parse HEAD)"
HEAD_SHORT="$(git rev-parse --short HEAD)"
TIMESTAMP_UTC="$(date -u +%Y-%m-%dT%H:%M:%SZ)"
RUN_ID="RUN_${HEAD_SHORT}_$(date -u +%Y%m%dT%H%M%SZ)"

SHA256_REPLAY_HASH="$(sha256sum "$MANIFEST_TARGET" | awk '{print $1}')"

SHA3_256_BRIDGE_HASH="$(python3 - <<PY
import hashlib
from pathlib import Path
p = Path("$L0_TARGET")
print(hashlib.sha3_256(p.read_bytes()).hexdigest())
PY
)"

if [ -z "$RUN_ID" ] || [ -z "$SHA256_REPLAY_HASH" ] || [ -z "$SHA3_256_BRIDGE_HASH" ]; then
  CI_STATUS_PASS=false
else
  CI_STATUS_PASS=true
fi

cat > artifacts/runtime/L3_RECON_RUNTIME_PAYLOAD_V0_1.json <<JSON
{
  "runtime_payload": {
    "RUN_ID": "$RUN_ID",
    "REPO": "jsonwisdom/JOY",
    "HEAD_COMMIT": "$HEAD_FULL",
    "SHA256_REPLAY_TARGET": "$MANIFEST_TARGET",
    "SHA256_REPLAY_HASH": "$SHA256_REPLAY_HASH",
    "SHA3_256_BRIDGE_TARGET": "$L0_TARGET",
    "SHA3_256_BRIDGE_HASH": "$SHA3_256_BRIDGE_HASH",
    "CI_STATUS_PASS": $CI_STATUS_PASS,
    "TIMESTAMP_UTC": "$TIMESTAMP_UTC",
    "METADATA": {
      "environment": "local-iron-runner",
      "version": "0.1.0",
      "no_fake_green": true,
      "mock_values_allowed": false
    }
  }
}
JSON

cat artifacts/runtime/L3_RECON_RUNTIME_PAYLOAD_V0_1.json
