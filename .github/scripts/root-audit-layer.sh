#!/usr/bin/env bash
set -euo pipefail

echo "ROOT_AUDIT_LAYER_V0_1"
echo "START_STATE=ZERO_STATE"

required_dirs=(
  "governance"
  ".github"
  ".github/scripts"
  ".github/workflows"
)

required_files=(
  "governance/ROOT_AUDIT_LAYER_V0_1.md"
  ".github/scripts/root-audit-layer.sh"
  ".github/workflows/root-audit-layer.yml"
)

for dir in "${required_dirs[@]}"; do
  if [ ! -d "$dir" ]; then
    echo "DEMOTION: missing directory: $dir"
    echo "STATE=ZERO_STATE"
    exit 1
  fi
done

echo "STATE=STRUCTURE_EXISTS"

for file in "${required_files[@]}"; do
  if [ ! -f "$file" ]; then
    echo "DEMOTION: missing file: $file"
    echo "STATE=STRUCTURE_EXISTS"
    exit 1
  fi
done

echo "STATE=FILES_EXIST"

if [ ! -s ".github/workflows/root-audit-layer.yml" ]; then
  echo "DEMOTION: workflow yaml empty"
  echo "STATE=FILES_EXIST"
  exit 1
fi

echo "STATE=YAML_DECLARED"
echo "ROOT_AUDIT_PASS=true"
echo "AUTHORITY=false"
echo "NO_FAKE_GREEN=true"
