#!/usr/bin/env python3
"""
Zero Trust Civic Audit verifier for jsonwisdom/JOY.

This verifier is intentionally boring:
- standard library only
- no network calls
- no authority claims
- no fake green

It validates the repository's public metadata state, computes SHA-256
hashes for critical files, verifies required state lanes, parses JSON,
and emits a deterministic JSON report for GitHub Actions and auditors.

External systems such as IPFS, EAS, Zora, and Base are NOT verified here.
They remain pending unless explicit public receipts are later added.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
STATE_FILE = "JAYWISDOM_SIMPLE_STATE_V0_1.json"

DEFAULT_CRITICAL_FILES = [
    "README.md",
    "PUBLIC_AUDIT_LOCATOR_INDEX_V0_1.md",
    "VALIDATION_LAYER_START_HERE_V0_1.md",
    "SIGN_UP_AND_FEEDBACK_V0_1.md",
    "command-center/JAYWISDOM_GITHUB_COMMAND_CENTER_V0_1.md",
    "tools/verify-this-repo.py",
    ".github/workflows/zero-trust-audit.yml",
    "AUDIT_LOG.md",
    "metadata/operation-vcr/OPERATION_VCR_ALMS_KEEPUP_V0_1.json",
    "metadata/movies/BLOCKBUSTERS_IRL_GENZ_MOVIE_WATCHERS_V0_1.json",
    "schemas/retail/BLOCKBUSTER_RETAIL_2026_PACKAGE_SCHEMA_V0_1.json",
]

DEFAULT_REQUIRED_TEXT = {
    "README.md": ["PUBLIC START HERE", "jaywisdom.base.eth", "jsonwisdom/JOY"],
    "PUBLIC_AUDIT_LOCATOR_INDEX_V0_1.md": ["jsonwisdom/JOY", "jaywisdom.base.eth", "no_fake_green"],
}

DEFAULT_REQUIRED_STATE_LANES = ["MN", "AL", "UTAH"]
SKIP_DIRS = {".git", "node_modules", ".venv", "venv", "dist", "build", "__pycache__"}


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


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
    except Exception as exc:  # noqa: BLE001 - audit tool reports parse failures.
        return False, f"{type(exc).__name__}: {exc}"


def add_failure(failures: list[dict[str, str]], path: str, reason: str) -> None:
    failures.append({"path": path, "reason": reason})


def add_warning(warnings: list[dict[str, str]], path: str, reason: str) -> None:
    warnings.append({"path": path, "reason": reason})


def get_required_text(state: dict[str, Any]) -> dict[str, list[str]]:
    configured = state.get("verification", {}).get("required_text")
    if isinstance(configured, dict):
        out: dict[str, list[str]] = {}
        for path, needles in configured.items():
            if isinstance(path, str) and isinstance(needles, list):
                out[path] = [str(n) for n in needles]
        return out
    return DEFAULT_REQUIRED_TEXT


def get_critical_files(state: dict[str, Any]) -> list[dict[str, str | None]]:
    configured = state.get("verification", {}).get("critical_files")
    raw_items: list[Any] = configured if isinstance(configured, list) else DEFAULT_CRITICAL_FILES

    out: list[dict[str, str | None]] = []
    for item in raw_items:
        if isinstance(item, str):
            out.append({"path": item, "expected_sha256": None})
        elif isinstance(item, dict) and isinstance(item.get("path"), str):
            expected = item.get("expected_sha256")
            out.append({
                "path": item["path"],
                "expected_sha256": expected if isinstance(expected, str) else None,
            })
    return out


def verify_project_identity(state: dict[str, Any], failures: list[dict[str, str]]) -> None:
    identity = state.get("project_identity")
    if not isinstance(identity, dict):
        add_failure(failures, STATE_FILE, "project_identity_missing_or_invalid")
        return

    expected = {
        "ens": "jaywisdom.eth",
        "basename": "jaywisdom.base.eth",
        "github_root": "jsonwisdom/JOY",
        "authority_claimed": False,
    }
    for key, expected_value in expected.items():
        if identity.get(key) != expected_value:
            add_failure(failures, STATE_FILE, f"project_identity_mismatch:{key}")


def verify_rules(state: dict[str, Any], failures: list[dict[str, str]]) -> None:
    rules = state.get("rules")
    if not isinstance(rules, dict):
        add_failure(failures, STATE_FILE, "rules_missing_or_invalid")
        return

    required = {
        "public_metadata_only_by_default": True,
        "private_targeting": False,
        "secret_authority": False,
        "no_fake_green": True,
        "no_receipt_no_authority": True,
    }
    for key, expected_value in required.items():
        if rules.get(key) != expected_value:
            add_failure(failures, STATE_FILE, f"rule_mismatch:{key}")


def verify_state_lanes(
    state: dict[str, Any],
    failures: list[dict[str, str]],
    warnings: list[dict[str, str]],
) -> list[dict[str, Any]]:
    lanes = state.get("layers", {}).get("state_lanes")
    if not isinstance(lanes, dict):
        add_failure(failures, STATE_FILE, "layers.state_lanes_missing_or_invalid")
        return []

    configured = state.get("verification", {}).get("required_state_lanes")
    required = configured if isinstance(configured, list) else DEFAULT_REQUIRED_STATE_LANES

    results: list[dict[str, Any]] = []
    for lane in [str(x) for x in required]:
        present = lane in lanes
        value = lanes.get(lane)
        status = "PASS"

        if not present:
            status = "FAIL"
            add_failure(failures, STATE_FILE, f"state_lane_missing:{lane}")
        elif value == 0:
            status = "FAIL"
            add_failure(failures, STATE_FILE, f"state_lane_zero_invalid:{lane}")
        elif value is None:
            status = "WARN"
            add_warning(warnings, STATE_FILE, f"state_lane_declared_null:{lane}")
        elif value == "":
            status = "FAIL"
            add_failure(failures, STATE_FILE, f"state_lane_empty_invalid:{lane}")

        results.append({"lane": lane, "present": present, "status": status, "value_type": type(value).__name__})
    return results


def verify_external_anchor_policy(
    state: dict[str, Any],
    warnings: list[dict[str, str]],
) -> dict[str, Any]:
    anchors = state.get("layers", {}).get("optional_external_anchors")
    if not isinstance(anchors, dict):
        add_warning(warnings, STATE_FILE, "optional_external_anchors_missing_or_invalid")
        return {}

    results: dict[str, Any] = {}
    for name, value in anchors.items():
        text = str(value).upper()
        pending = "PENDING" in text
        results[str(name)] = {"value": value, "pending": pending}
        if not pending:
            add_warning(warnings, STATE_FILE, f"external_anchor_not_marked_pending:{name}")
    return results


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true", help="Emit machine JSON only")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as failures")
    args = parser.parse_args()

    failures: list[dict[str, str]] = []
    warnings: list[dict[str, str]] = []

    state_path = ROOT / STATE_FILE
    state_ok, state_value = load_json(state_path) if state_path.exists() else (False, "missing")
    state: dict[str, Any] = state_value if state_ok and isinstance(state_value, dict) else {}

    if not state_path.exists():
        add_failure(failures, STATE_FILE, "state_file_missing")
    elif not state_ok:
        add_failure(failures, STATE_FILE, "state_file_invalid_json")
    elif not isinstance(state_value, dict):
        add_failure(failures, STATE_FILE, "state_file_not_object")

    verify_project_identity(state, failures)
    verify_rules(state, failures)
    state_lane_results = verify_state_lanes(state, failures, warnings)
    external_anchor_results = verify_external_anchor_policy(state, warnings)

    critical_results = []
    for item in get_critical_files(state):
        path_text = str(item["path"])
        expected_sha = item.get("expected_sha256")
        path = ROOT / path_text
        exists = path.exists()
        actual_sha = sha256_file(path) if exists and path.is_file() else None

        record = {
            "path": path_text,
            "exists": exists,
            "sha256": actual_sha,
            "expected_sha256": expected_sha,
            "hash_status": "UNPINNED",
        }

        if not exists:
            record["hash_status"] = "MISSING"
            add_failure(failures, path_text, "critical_file_missing")
        elif expected_sha:
            if actual_sha == expected_sha:
                record["hash_status"] = "MATCH"
            else:
                record["hash_status"] = "MISMATCH"
                add_failure(failures, path_text, "critical_file_sha256_mismatch")
        else:
            add_warning(warnings, path_text, "critical_file_sha256_unpinned")

        critical_results.append(record)

    for path_text, needles in get_required_text(state).items():
        path = ROOT / path_text
        if not path.exists():
            add_failure(failures, path_text, "required_text_file_missing")
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for needle in needles:
            if needle not in text:
                add_failure(failures, path_text, f"missing_required_text:{needle}")

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
            add_failure(failures, rel(path), "invalid_json")
        elif isinstance(value, dict):
            if rel(path).startswith("schemas/") and "$schema" not in value:
                add_failure(failures, rel(path), "schema_file_missing_$schema")
            record["top_level_keys"] = sorted(value.keys())[:25]
        json_results.append(record)

    effective_failures = list(failures)
    if args.strict:
        for warning in warnings:
            effective_failures.append({"path": warning["path"], "reason": f"strict_warning:{warning['reason']}"})

    report = {
        "artifact": "ZERO_TRUST_CIVIC_AUDIT_DRILL_REPORT",
        "version": "0.2",
        "repo_root": "jsonwisdom/JOY",
        "project_identity": ["jaywisdom.base.eth", "jaywisdom.eth"],
        "mode": "public_metadata_validation",
        "authority": False,
        "green_implied": False,
        "no_fake_green": True,
        "state_file": {
            "path": STATE_FILE,
            "valid_json": state_ok,
            "sha256": sha256_file(state_path) if state_path.exists() and state_ok else None,
        },
        "state_lanes": state_lane_results,
        "critical_files": critical_results,
        "json_files_checked": len(json_results),
        "json_results": json_results,
        "external_anchors": external_anchor_results,
        "warnings": warnings,
        "failures": failures,
        "strict": args.strict,
        "status": "PASS" if not effective_failures else "FAIL",
    }

    if args.json:
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        print(f"Zero Trust Civic Audit Drill: {report['status']}")
        print(f"State lanes checked: {len(state_lane_results)}")
        print(f"Critical files checked: {len(critical_results)}")
        print(f"JSON files checked: {len(json_results)}")
        print(f"Failures: {len(failures)}")
        print(f"Warnings: {len(warnings)}")
        if warnings:
            print("Note: warnings do not fail unless --strict is used.")

    return 0 if not effective_failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
