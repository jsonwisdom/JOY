#!/usr/bin/env bash
set -euo pipefail
mkdir -p artifacts/github
OUT="artifacts/github/trigger_hunter_snapshot.txt"
NOW="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
{
echo "GITHUB_TRIGGER_HUNTER_SNAPSHOT"
echo "timestamp_utc=$NOW"
echo "branch=$(git branch --show-current)"
echo "head=$(git rev-parse HEAD)"
echo
echo "== STATUS =="
git status --short --branch
echo
echo "== WORKFLOWS =="
find .github/workflows -maxdepth 1 -type f 2>/dev/null | sort || true
echo
echo "== RECENT COMMITS =="
git log --oneline -5
echo
echo "== MACHINE REPLAY CHECK =="
if [ -x scripts/verify_base_tx_boundary.sh ] && [ -f artifacts/base/base_tx_8a642.normalized.json ]; then
  ./scripts/verify_base_tx_boundary.sh artifacts/base/base_tx_8a642.normalized.json
else
  echo "YELLOW: base tx replay harness or normalized receipt missing"
fi
echo
echo "== GITHUB RUNS =="
if command -v gh >/dev/null 2>&1 && gh auth status >/dev/null 2>&1; then
  gh run list --limit 10 || true
else
  echo "YELLOW: gh unavailable or unauthenticated"
fi
echo
echo "== RULING =="
echo "TRIGGER HUNTER = BOOTED"
echo "SNAP BACK FIXTURE = PRESERVED"
echo "SEMANTIC TRUTH = NOT CLAIMED"
echo "AUTHORITY = FALSE"
echo "NO_FAKE_GREEN = TRUE"
} | tee "$OUT"
sha256sum "$OUT" | tee artifacts/github/trigger_hunter_snapshot.sha256
