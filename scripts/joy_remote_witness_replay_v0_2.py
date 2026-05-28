#!/usr/bin/env python3
import json, hashlib, sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
BADGES_DIR = ROOT / "assets" / "badges"
RECEIPTS_DIR = ROOT / "receipts"
MANIFEST_PATH = ROOT / "badges" / "badge_manifest_v0_2.json"
ORACLE_PATH = ROOT / "receipts" / "joy_clean_era_oracle_v0_1.json"

errors = []
warnings = []
results = {}

def load_json(path):
    return json.loads(path.read_text())

def sha256_file(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def skip_system_receipt(path, receipt):
    name = path.name.lower()
    if not receipt.get("asset_id"):
        return True
    if "oracle" in name or "closeout" in name or "ritual" in name:
        return True
    return False

if not MANIFEST_PATH.exists():
    errors.append(f"manifest_missing:{MANIFEST_PATH}")
else:
    manifest = load_json(MANIFEST_PATH)
    badges = manifest.get("badges", [])

    seen = set()
    for b in badges:
        bid = b.get("badge_id")
        if not bid:
            errors.append("badge_missing_id")
        elif bid in seen:
            errors.append(f"duplicate_badge_id:{bid}")
        else:
            seen.add(bid)
    results["no_duplicate_badge_ids"] = "PASS" if not any(e.startswith("duplicate") or e == "badge_missing_id" for e in errors) else "FAIL"

    receipts = {}
    for rp in RECEIPTS_DIR.glob("*.json"):
        r = load_json(rp)
        aid = r.get("asset_id")
        if aid:
            receipts[aid] = r
        if not skip_system_receipt(rp, r):
            if aid not in seen:
                warnings.append(f"orphan_receipt_allowed_warning:{rp.name}:{aid}")

    missing = []
    for b in badges:
        bid = b.get("badge_id")
        if bid and bid not in receipts:
            missing.append(bid)
            errors.append(f"manifest_asset_missing_receipt:{bid}")
    results["manifest_all_assets_have_receipts"] = "PASS" if not missing else "FAIL"

    mismatches = []
    for b in badges:
        bid = b.get("badge_id")
        if not bid:
            continue
        ap = BADGES_DIR / f"{bid}.svg"
        if not ap.exists():
            errors.append(f"asset_missing:{bid}")
            mismatches.append(bid)
            continue
        actual = sha256_file(ap)
        receipt_hash = receipts.get(bid, {}).get("sha256_restored")
        manifest_hash = b.get("sha256_restored")
        if receipt_hash != actual:
            errors.append(f"receipt_hash_mismatch:{bid}")
            mismatches.append(bid)
        if manifest_hash != actual:
            errors.append(f"manifest_hash_mismatch:{bid}")
            mismatches.append(bid)
    results["manifest_all_hashes_match_assets"] = "PASS" if not mismatches else "FAIL"

    oracle_mismatches = []
    if ORACLE_PATH.exists():
        oracle = load_json(ORACLE_PATH)
        for aid, expected in oracle.get("verified_assets", {}).items():
            ap = BADGES_DIR / f"{aid}.svg"
            if not ap.exists():
                errors.append(f"oracle_asset_missing:{aid}")
                oracle_mismatches.append(aid)
                continue
            actual = sha256_file(ap)
            if actual != expected:
                errors.append(f"oracle_hash_mismatch:{aid}")
                oracle_mismatches.append(aid)
        post_oracle = sorted({p.stem for p in BADGES_DIR.glob("*.svg")} - set(oracle.get("verified_assets", {}).keys()))
        if post_oracle:
            warnings.append("post_oracle_assets_allowed:" + ",".join(post_oracle))
        warnings.append("oracle_baseline_head:" + str(oracle.get("head")))
        results["oracle_assets_match_current_files"] = "PASS" if not oracle_mismatches else "FAIL"
    else:
        warnings.append("oracle_missing")
        results["oracle_assets_match_current_files"] = "SKIP"

out = {
    "result": "VERIFIED" if not errors else "REJECTED",
    "checks": results,
    "errors": errors,
    "warnings": warnings
}
print(json.dumps(out, indent=2))
sys.exit(0 if not errors else 1)
