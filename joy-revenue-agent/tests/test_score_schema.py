import importlib.util
import json
import pathlib
import unittest

import jsonschema


ROOT = pathlib.Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "src" / "qualification" / "eev_calculator.py"
SPEC = importlib.util.spec_from_file_location("eev_calculator", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)

OpportunityInputs = MODULE.OpportunityInputs
compute_eev_usd = MODULE.compute_eev_usd


class TestScoreSchema(unittest.TestCase):
    def setUp(self):
        self.schema = json.loads((ROOT / "schemas" / "score.schema.json").read_text())
        self.fixtures_dir = pathlib.Path(__file__).parent / "fixtures"

    def _validated_score(self, fixture_name):
        data = json.loads((self.fixtures_dir / fixture_name).read_text())
        score = compute_eev_usd(
            OpportunityInputs(**data),
            scored_at="2026-08-07T00:00:00+00:00",
        )
        jsonschema.validate(instance=score, schema=self.schema)
        return score

    def test_high_pass_output_valid(self):
        self.assertTrue(self._validated_score("score_high_pass.json")["threshold_pass"])

    def test_low_fail_output_valid(self):
        self.assertFalse(self._validated_score("score_low_fail.json")["threshold_pass"])

    def test_boundary_12_60_output_valid(self):
        self.assertEqual(
            self._validated_score("score_edge_12_6.json")["expected_value_usd"],
            12.6,
        )

    def test_boundary_15_12_output_valid(self):
        self.assertEqual(
            self._validated_score("score_edge_15_12.json")["expected_value_usd"],
            15.12,
        )

    def test_schema_rejects_false_green_reason(self):
        score = self._validated_score("score_low_fail.json")
        score["reason"] = "OK"
        with self.assertRaises(jsonschema.ValidationError):
            jsonschema.validate(instance=score, schema=self.schema)


if __name__ == "__main__":
    unittest.main()
