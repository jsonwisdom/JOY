#!/usr/bin/env python3
"""
Zero Trust Civic Audit verifier for jsonwisdom/JOY.

Purpose:
- Parse all repo JSON artifacts.
- Check required public-entry files exist.
- Check key JSON schemas declare $schema or schema-like structure.
- Emit a deterministic JSON report for GitHub Actions and outside auditors.

This script does not verify IPFS, EAS, Zora, or Base externally.
Those remain pending unless explicit external receipts are present.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "PUBLIC_AUDIT_LOCATOR_INDEX_V0_1.md",
    "SIGN_UP_AND_FEEDBACK_V0_1.md",
    "metadata/operation-vcr/OPERATION_VCR_ALMS_KEEPUP_V0_1.json",
    "metadata/movies/BLOCKBUSTERS_IRL_GENZ_MOVIE_WATCHERS_V0_1.json",
    "schemas/retail/BLOCKBUSTER_RETAIL_2026_PACKAGE_SCHEMA_V0_1.json",
]

REQUIRED_TEXT = {
    "README.md": ["PUBLIC START HERE", "jaywisdom.base.eth", "jsonwisdom/JOY"],
    "PUBLIC_AUDIT_LOCATOR_INDEX_V0_1.md": ["jsonwisdom/JOY", "jaywisdom.base.eth", "no_fake_green"],
}

SKIP_DIRS = {".git", "node_modules", ".venv", "venv", "dist", "build"}


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def iter_json_files() -> list[Path]:
    out: list[Path] = []
    for base, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for name in files:
            if name.endswith(".json"):
                out.append(Path(base) / name)
    return sorted(out)


def load_json(path: Path) -> tuple[bool, Any | str]:
    try:
        return True, json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # noqa: BLE001 - verifier reports parse failures.
        return False, f"{type(exc).__name__}: {exc}"


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true", help="Emit machine JSON only")
    args = parser.parse_args()

    failures: list[dict[str, str]] = []
    warnings: list[dict[str, str]] = []

    required_results = []
    for item in REQUIRED_FILES:
        path = ROOT / item
        exists = path.exists()
        required_results.append({"path": item, "exists": exists})
        if not exists:
            failures.append({"path": item, "reason": "required_file_missing"})

    for item, needles in REQUIRED_TEXT.items():
        path = ROOT / item
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for needle in needles:
            if needle not in text:
                failures.append({"path": item, "reason": f"missing_required_text:{needle}"})

    json_results = []
    for path in iter_json_files():
        ok, value = load_json(path)
        record: dict[str, Any] = {
            "path": rel(path),
            "valid_json": ok,
            "sha256": sha256_file(path) if ok else None,
        }
        if not ok:
            record["error"] = value
            failures.append({"path": rel(path), "reason": "invalid_json"})
        elif isinstance(value, dict):
            if rel(path).startswith("schemas/") and "$schema" not in value:
                warnings.append({"path": rel(path), "reason": "schema_file_missing_$schema"})
            record["top_level_keys"] = sorted(value.keys())[:25]
        json_results.append(record)

    report = {
        "artifact": "ZERO_TRUST_CIVIC_AUDIT_DRILL_REPORT",
        "version": "0.1",
        "repo_root": "jsonwisdom/JOY",
        "project_identity": ["jaywisdom.base.eth", "jaywisdom.eth"],
        "mode": "public_metadata_validation",
        "authority": False,
        "green_implied": False,
        "no_fake_green": True,
        "required_files": required_results,
        "json_files_checked": len(json_results),
        "json_results": json_results,
        "warnings": warnings,
        "failures": failures,
        "status": "PASS" if not failures else "FAIL",
        "external_anchors": {
            "ipfs": "not_verified_by_this_script",
            "eas": "not_verified_by_this_script",
            "zora": "not_verified_by_this_script",
            "base": "not_verified_by_this_script",
        },
    }

    if args.json:
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        print(f"Zero Trust Civic Audit Drill: {report['status']}")
        print(f"JSON files checked: {len(json_results)}")
        print(f"Failures: {len(failures)}")
        print(f"Warnings: {len(warnings)}")

    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
