"""Positive, negative, and no-fake-green fixtures for FullJasonMathReplay."""
import unittest

from scripts.fulljasonmath_replay import replay


class FullJasonMathReplayTests(unittest.TestCase):
    def test_exact_fraction(self):
        r = replay({"case_id": "fractions", "operation": "add",
                    "operands": ["1/3", "1/6"], "expected": "1/2"})
        self.assertEqual(r["verdict"], "PASS_SCOPED")
        self.assertEqual(r["computed"], "1/2")
        self.assertEqual(r["external_truth"], "NOT_EVALUATED")

    def test_bad_card_arithmetic_fails(self):
        r = replay({"case_id": "math-error", "operation": "add",
                    "operands": ["478", "478"], "expected": "957"})
        self.assertEqual(r["computed"], "956")
        self.assertEqual(r["verdict"], "FAIL")

    def test_exact_modulo(self):
        r = replay({"case_id": "modulo", "operation": "modulo",
                    "operands": ["127", "100"], "expected": "27"})
        self.assertEqual(r["verdict"], "PASS_SCOPED")

    def test_rejection_sampling_demo_is_scoped(self):
        r = replay({
            "case_id": "fresh-demo-digest-only-not-seed-verification",
            "kind": "rejection_sample_100",
            "digest_sha256": "afea6ad62370343a55aac86bd0967b6ef02ad3cf51fd76b46acda203ad9fc224",
            "expected": "64"
        })
        self.assertEqual(r["computed"], "64")
        self.assertEqual(r["rejections"], 0)
        self.assertEqual(r["verdict"], "PASS_SCOPED")
        self.assertEqual(r["historical_card_13"], "HOLD")
        self.assertEqual(r["entropy_impartiality"], "NOT_CERTIFIED")
        self.assertFalse(r["authority_created"])

    def test_rejected_digest_does_not_silently_reroll(self):
        r = replay({"case_id": "reject", "kind": "rejection_sample_100",
                    "digest_sha256": "f" * 64, "expected": "99"})
        self.assertEqual(r["verdict"], "HOLD")
        self.assertEqual(r["reason"], "COUNTER_ADVANCE_REQUIRED_NOT_PERFORMED")

    def test_missing_expected_is_hold(self):
        r = replay({"case_id": "unknown", "operation": "multiply",
                    "operands": ["12", "12"]})
        self.assertEqual(r["verdict"], "HOLD")

    def test_float_is_not_exact_input(self):
        r = replay({"case_id": "float", "operation": "add",
                    "operands": [0.1, "1/10"], "expected": "1/5"})
        self.assertEqual(r["verdict"], "HOLD")

    def test_zero_denominator_is_hold(self):
        r = replay({"case_id": "zero", "operation": "divide",
                    "operands": ["1", "0"], "expected": "0"})
        self.assertEqual(r["verdict"], "HOLD")


if __name__ == "__main__":
    unittest.main()
