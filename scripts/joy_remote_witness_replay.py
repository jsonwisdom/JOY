#!/usr/bin/env python3
import argparse, hashlib, json, pathlib, subprocess, sys

def sh(cmd):
    return subprocess.check_output(cmd, shell=True, text=True).strip()

def fail(msg):
    print(json.dumps({"result": "REJECTED", "reason": msg}, indent=2))
    sys.exit(1)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("receipt")
    args = ap.parse_args()

    receipt_path = pathlib.Path(args.receipt)
    if not receipt_path.exists():
        fail("receipt_missing")

    receipt = json.loads(receipt_path.read_text())

    asset_path_value = receipt.get("asset_path")
    if not asset_path_value:
        asset_id_for_path = receipt.get("asset_id") or receipt.get("badge_id")
        if not asset_id_for_path:
            fail("asset_path_missing")
        asset_path_value = f"assets/badges/{asset_id_for_path}.svg"

    asset_path = pathlib.Path(asset_path_value)
    if not asset_path.exists():
        fail("asset_missing")
    if asset_path.is_dir():
        fail("asset_path_is_directory")

    actual = hashlib.sha256(asset_path.read_bytes()).hexdigest()
    expected = receipt.get("sha256_restored") or receipt.get("asset_sha256")
    if actual != expected:
        fail("sha256_mismatch")

    if receipt.get("status") not in ["RESTORED_VERIFIED", "TEMPLATE_RECEIPT"]:
        fail("invalid_receipt_status")

    manifest = json.loads(pathlib.Path("badges/badge_manifest_v0_2.json").read_text())
    badge_id = receipt.get("asset_id") or receipt.get("badge_id")

    entry = next((b for b in manifest.get("badges", []) if b.get("badge_id") == badge_id), None)
    if not entry:
        fail("manifest_entry_missing")

    if entry.get("sha256_restored") != actual:
        fail("manifest_hash_mismatch")

    local = sh("git rev-parse HEAD")
    remote = sh("git ls-remote origin refs/heads/main | awk '{print $1}'")
    if local != remote:
        fail("remote_head_mismatch")

    print(json.dumps({
        "result": "VERIFIED",
        "asset_id": badge_id,
        "sha256": actual,
        "local_head": local,
        "remote_head": remote
    }, indent=2))

if __name__ == "__main__":
    main()
