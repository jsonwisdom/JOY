#!/usr/bin/env python3
"""Fail-closed CMP-WH v0.1 conformance runner.

The runner reports test outcomes and eligibility only. It never authorizes
schema freeze, OpenAPI generation, or government action.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


PASS = "PASS"
FAIL = "FAIL"
BLOCKED = "BLOCKED"


@dataclass(frozen=True)
class Outcome:
    result: str
    error_code: str | None = None
    detail: str = ""


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate_manifest(test: dict[str, Any]) -> Outcome:
    required = {"test_id", "category", "description", "expected"}
    missing = sorted(required - test.keys())
    if missing:
        return Outcome(FAIL, "E_MISSING_REQUIRED", f"missing manifest fields: {missing}")
    if test["expected"] not in {PASS, FAIL, BLOCKED}:
        return Outcome(FAIL, "E_INVALID_EXPECTATION", "invalid expected result")
    return Outcome(PASS)


def run_test(test: dict[str, Any], fixtures_dir: Path) -> Outcome:
    manifest_check = validate_manifest(test)
    if manifest_check.result != PASS:
        return manifest_check

    fixture_name = test.get("fixture")
    if fixture_name:
        fixture_path = fixtures_dir / f"{fixture_name}.json"
        if not fixture_path.is_file():
            return Outcome(BLOCKED, "E_FIXTURE_MISSING", str(fixture_path))
        try:
            load_json(fixture_path)
        except (OSError, json.JSONDecodeError) as exc:
            return Outcome(FAIL, "E_FIXTURE_INVALID", str(exc))

    if test.get("mode") == "COMPARE_INDEPENDENT_IMPLEMENTATIONS":
        attestation = test.get("independence_attestation")
        if not attestation:
            return Outcome(BLOCKED, "E_INDEPENDENCE_ATTESTATION_MISSING")

    # Category engines are intentionally explicit. Unimplemented validation
    # classes block rather than silently passing.
    implemented = {"RUNNER_SELF_TEST"}
    if test["category"] not in implemented:
        return Outcome(BLOCKED, "E_VALIDATOR_NOT_IMPLEMENTED", test["category"])

    return Outcome(PASS)


def build_report(suite: dict[str, Any], outcomes: list[dict[str, Any]], suite_path: Path) -> dict[str, Any]:
    passed = sum(item["actual"] == PASS for item in outcomes)
    failed = sum(item["actual"] == FAIL for item in outcomes)
    blocked = sum(item["actual"] == BLOCKED for item in outcomes)
    total = len(outcomes)
    conformance_passed = total > 0 and passed == total and failed == 0 and blocked == 0
    metadata_complete = all(item.get("metadata_complete", True) for item in outcomes)

    return {
        "report_id": "CMP-WH-CONFORMANCE-REPORT-000001",
        "suite_id": suite.get("suite_id"),
        "suite_version": suite.get("suite_version"),
        "protocol_version": suite.get("protocol_version"),
        "schema_version": suite.get("schema_version"),
        "executed_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "runner": {
            "name": "cmp-reference-runner",
            "version": "0.1.0",
            "runtime_platform": platform.python_implementation() + " " + platform.python_version(),
            "operating_system": platform.platform(),
            "suite_sha256": sha256_file(suite_path),
        },
        "total_tests": total,
        "passed": passed,
        "failed": failed,
        "blocked": blocked,
        "result": PASS if conformance_passed else FAIL,
        "conformance_passed": conformance_passed,
        "metadata_complete": metadata_complete,
        "eligible_for_human_freeze": conformance_passed and metadata_complete,
        "eligible_for_openapi_build": conformance_passed and metadata_complete,
        "human_freeze_authorized": False,
        "human_openapi_authorization": False,
        "next_gate": "EXPLICIT_HUMAN_AUTHORIZATION" if conformance_passed else "IMPLEMENTATION_COMPLETION",
        "outcomes": outcomes,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--suite", type=Path, required=True)
    parser.add_argument("--fixtures", type=Path, required=True)
    parser.add_argument("--report", type=Path, required=True)
    args = parser.parse_args()

    try:
        suite = load_json(args.suite)
    except (OSError, json.JSONDecodeError) as exc:
        print(f"FAIL: cannot load suite: {exc}", file=sys.stderr)
        return 1

    tests = suite.get("tests")
    if not isinstance(tests, list) or not tests:
        print("FAIL: suite has no tests", file=sys.stderr)
        return 1

    outcomes: list[dict[str, Any]] = []
    for test in tests:
        outcome = run_test(test, args.fixtures)
        outcomes.append({
            "test_id": test.get("test_id", "UNKNOWN"),
            "expected": test.get("expected"),
            "actual": outcome.result,
            "error_code": outcome.error_code,
            "detail": outcome.detail,
            "metadata_complete": outcome.error_code != "E_INDEPENDENCE_ATTESTATION_MISSING",
        })

    report = build_report(suite, outcomes, args.suite)
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: report[k] for k in ("result", "passed", "failed", "blocked", "next_gate")}, indent=2))
    return 0 if report["conformance_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
