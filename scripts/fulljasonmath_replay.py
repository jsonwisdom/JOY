#!/usr/bin/env python3
"""MarydeeBot's optional, read-only mathematics lane. No proof of external truth."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "docs/school-of-wisdom/marydeebot.v0.1.json"
NUM = re.compile(r"-?(?:0|[1-9][0-9]{0,63})(?:/[1-9][0-9]{0,63})?\Z")
HEX256 = re.compile(r"[0-9a-fA-F]{64}\Z")


def rational(value: object) -> Fraction:
    """Reject floats, expressions and unlimited integers; accept exact strings only."""
    if not isinstance(value, str) or NUM.fullmatch(value) is None:
        raise ValueError("expected bounded exact integer or rational string")
    return Fraction(value)


def render(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def replay(case: object) -> dict:
    """PASS_SCOPED only for reproducible math equality, never truth or authority."""
    result = {
        "schema": "FULLJASONMATHREPLAY_RESULT_V0_1",
        "verdict": "HOLD",
        "reason": "UNVALIDATED_INPUT",
        "scope": "MATHEMATICS_ONLY",
        "authority_created": False,
        "human_final_decision": "JASON",
        "historical_card_13": "HOLD",
        "entropy_impartiality": "NOT_CERTIFIED",
        "external_truth": "NOT_EVALUATED",
        "original_logo_modified": False,
    }
    if not isinstance(case, dict):
        result["reason"] = "CASE_MUST_BE_JSON_OBJECT"
        return result
    try:
        encoded = json.dumps(case, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
        if len(encoded) > 8192:
            raise ValueError("case exceeds 8192 bytes")
        result["input_sha256"] = hashlib.sha256(encoded).hexdigest()
        case_id = case.get("case_id")
        if not isinstance(case_id, str) or not (1 <= len(case_id) <= 128):
            raise ValueError("case_id must be a nonempty bounded string")
        result["case_id"] = case_id
        kind = case.get("kind", "arithmetic")
        if kind == "arithmetic":
            operation = case.get("operation")
            operands = case.get("operands")
            if not isinstance(operands, list) or not 2 <= len(operands) <= 8:
                raise ValueError("operands must contain 2..8 exact strings")
            values = [rational(v) for v in operands]
            if operation == "add":
                computed = sum(values, Fraction(0))
            elif operation == "multiply":
                computed = Fraction(1)
                for value in values:
                    computed *= value
            elif operation in ("subtract", "divide", "modulo"):
                if len(values) != 2:
                    raise ValueError("binary operation requires two operands")
                a, b = values
                if operation == "subtract":
                    computed = a - b
                elif operation == "divide":
                    computed = a / b
                else:
                    if a.denominator != 1 or b.denominator != 1:
                        raise ValueError("modulo requires integers")
                    computed = Fraction(a.numerator % b.numerator)
            else:
                raise ValueError("unsupported arithmetic operation")
            value = render(computed)
            result["computed"] = value
            result["method"] = "PYTHON_FRACTION_EXACT"
            expected = case.get("expected")
            if expected is None:
                result["reason"] = "EXPECTED_RESULT_MISSING"
                return result
            expected_math = rational(expected)
            matches = computed == expected_math
        elif kind == "rejection_sample_100":
            # One fixed, supplied 256-bit digest. Does not authenticate its preimage,
            # source of randomness, commitment timestamp, or actual historic use.
            digest = case.get("digest_sha256")
            if not isinstance(digest, str) or not HEX256.fullmatch(digest):
                raise ValueError("digest_sha256 must be 64 hex characters")
            integer = int(digest, 16)
            limit = (2**256 // 100) * 100
            if integer >= limit:
                result["reason"] = "COUNTER_ADVANCE_REQUIRED_NOT_PERFORMED"
                result["method"] = "REJECTION_SAMPLING_NOT_COMPLETED"
                return result
            value = str(integer % 100)
            result["computed"] = value
            result["method"] = "256_BIT_DIGEST_REJECTION_SAMPLE_0_99"
            result["rejections"] = 0
            expected = case.get("expected")
            if expected is None:
                result["reason"] = "EXPECTED_RESULT_MISSING"
                return result
            if not isinstance(expected, str) or not re.fullmatch(r"(?:0|[1-9][0-9]?)", expected):
                raise ValueError("expected roll must be a string from 0 to 99")
            matches = value == expected
        else:
            raise ValueError("unsupported replay kind")
        result["verdict"] = "PASS_SCOPED" if matches else "FAIL"
        result["reason"] = "EXACT_REPLAY_MATCH" if matches else "EXPECTED_RESULT_MISMATCH"
        return result
    except (ValueError, ZeroDivisionError, TypeError, OverflowError) as exc:
        result["verdict"] = "HOLD"
        result["reason"] = "INVALID_OR_INCOMPLETE_CASE"
        result["validation_detail"] = str(exc)
        return result


def main() -> int:
    parser = argparse.ArgumentParser(description="Read-only exact mathematics replay.")
    parser.add_argument("case_json", type=Path, help="Local JSON test case; never uploaded by this script")
    args = parser.parse_args()
    spec = json.loads(SPEC.read_text(encoding="utf-8"))
    if spec.get("math_replay", {}).get("module_id") != "FULLJASONMATHREPLAY_V0_1":
        print(json.dumps({"verdict": "HOLD", "reason": "MODULE_NOT_DECLARED"}))
        return 1
    case = json.loads(args.case_json.read_text(encoding="utf-8"))
    output = replay(case)
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0 if output["verdict"] == "PASS_SCOPED" else 1


if __name__ == "__main__":
    raise SystemExit(main())
