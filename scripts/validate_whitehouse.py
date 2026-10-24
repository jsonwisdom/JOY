#!/usr/bin/env python3
"""
White House Edition Validation Script (Bench Tester 4340 Core)
Validates schema compliance, boundary flags, and structural integrity.
"""

import json
import os
import sys

import yaml
from jsonschema import Draft202012Validator


def validate_receipt(schema_path: str, receipt_path: str) -> bool:
    print(f"[*] Validating Receipt: {receipt_path}")
    with open(schema_path, encoding="utf-8") as schema_file:
        schema = json.load(schema_file)
    with open(receipt_path, encoding="utf-8") as receipt_file:
        data = json.load(receipt_file)

    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(data), key=lambda error: list(error.path))

    if errors:
        print(f"[-] FAIL: Receipt validation failed. {len(errors)} errors.")
        for error in errors:
            location = ".".join(str(part) for part in error.path) or "<root>"
            print(f"    - {location}: {error.message}")
        return False

    print("[+] PASS: Receipt conforms to schema.")
    return True


def validate_scenario(scenario_path: str) -> bool:
    print(f"[*] Validating Scenario: {scenario_path}")
    with open(scenario_path, encoding="utf-8") as scenario_file:
        data = yaml.safe_load(scenario_file)

    if not isinstance(data, dict):
        print("[-] FAIL: Scenario root must be a mapping.")
        return False

    required_flags = {
        "simulation_only": True,
        "real_policy": False,
        "real_actors": False,
        "authority_created": False,
    }

    failed = False
    for key, expected in required_flags.items():
        actual = data.get(key)
        if actual != expected:
            print(f"[-] FAIL: Flag '{key}' is {actual!r}, expected {expected!r}.")
            failed = True
        else:
            print(f"[+] PASS: Flag '{key}' == {expected}")

    pipeline = data.get("pipeline")
    if not isinstance(pipeline, dict):
        print("[-] FAIL: Scenario missing mapping-valued 'pipeline'.")
        failed = True
    else:
        boundary_check = pipeline.get("boundary_check")
        if not isinstance(boundary_check, dict):
            print("[-] FAIL: Scenario missing mapping-valued 'boundary_check' stage.")
            failed = True
        elif boundary_check.get("status") != "PASS":
            print("[-] FAIL: Pipeline boundary check did not PASS.")
            failed = True

        simulated_result = pipeline.get("simulated_result")
        if not isinstance(simulated_result, dict):
            print("[-] FAIL: Scenario missing mapping-valued 'simulated_result' stage.")
            failed = True
        else:
            if simulated_result.get("action_taken") != "DROP_PACKET":
                print("[-] FAIL: Expected simulated action DROP_PACKET.")
                failed = True
            if simulated_result.get("state_change") != "NONE":
                print("[-] FAIL: Expected simulated state change NONE.")
                failed = True

    if not failed:
        print("[+] PASS: Scenario structure and flags valid.")
    return not failed


def run_validation() -> int:
    root = os.getcwd()
    module_path = os.path.join(root, "systems", "whitehouse")

    if not os.path.isdir(module_path):
        print("[-] FAIL: White House module directory not found.")
        return 1

    schema_dir = os.path.join(module_path, "schemas")
    scenarios_dir = os.path.join(module_path, "scenarios")
    receipts_dir = os.path.join(module_path, "receipts")
    receipt_schema = os.path.join(schema_dir, "receipt.schema.json")

    checks_passed = True

    if not os.path.isfile(receipt_schema):
        print("[-] FAIL: Receipt schema not found.")
        checks_passed = False
    elif not os.path.isdir(receipts_dir):
        print("[-] FAIL: Receipts directory not found.")
        checks_passed = False
    else:
        receipt_files = sorted(name for name in os.listdir(receipts_dir) if name.endswith(".json"))
        if not receipt_files:
            print("[-] FAIL: No receipt JSON files found.")
            checks_passed = False
        for name in receipt_files:
            if not validate_receipt(receipt_schema, os.path.join(receipts_dir, name)):
                checks_passed = False

    if not os.path.isdir(scenarios_dir):
        print("[-] FAIL: Scenarios directory not found.")
        checks_passed = False
    else:
        scenario_files = sorted(
            name for name in os.listdir(scenarios_dir) if name.endswith((".yaml", ".yml"))
        )
        if not scenario_files:
            print("[-] FAIL: No scenario YAML files found.")
            checks_passed = False
        for name in scenario_files:
            if not validate_scenario(os.path.join(scenarios_dir, name)):
                checks_passed = False

    if checks_passed:
        print("\n[!] RESULT: BENCH TESTER 4340 VALIDATION SUCCESSFUL.")
        return 0

    print("\n[-] RESULT: VALIDATION FAILED. MERGE BLOCKED.")
    return 1


if __name__ == "__main__":
    sys.exit(run_validation())
