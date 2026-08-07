import importlib.util
import json
import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "src" / "qualification" / "eev_calculator.py"
SPEC = importlib.util.spec_from_file_location("eev_calculator", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)

OpportunityInputs = MODULE.OpportunityInputs
compute_eev_usd = MODULE.compute_eev_usd


class TestEEV(unittest.TestCase):
    fixtures_dir = pathlib.Path(__file__).parent / "fixtures"

    def _load(self, name):
        return json.loads((self.fixtures_dir / name).read_text())

    def _score(self, name):
        data = self._load(name)
        return compute_eev_usd(
            OpportunityInputs(**data),
            scored_at="2026-08-07T00:00:00+00:00",
        )

    def test_high_value_pass(self):
        result = self._score("score_high_pass.json")
        self.assertEqual(result["expected_value_usd"], 1960.0)
        self.assertTrue(result["threshold_pass"])
        self.assertEqual(result["reason"], "OK")

    def test_low_value_fail(self):
        result = self._score("score_low_fail.json")
        self.assertEqual(result["expected_value_usd"], -40.0)
        self.assertFalse(result["threshold_pass"])
        self.assertEqual(result["reason"], "LOW_EEV")

    def test_boundary_12_60_rejects(self):
        result = self._score("score_edge_12_6.json")
        self.assertEqual(result["expected_value_usd"], 12.6)
        self.assertFalse(result["threshold_pass"])

    def test_boundary_15_12_accepts(self):
        result = self._score("score_edge_15_12.json")
        self.assertEqual(result["expected_value_usd"], 15.12)
        self.assertTrue(result["threshold_pass"])

    def test_exact_threshold_accepts(self):
        data = OpportunityInputs(
            opportunity_id="opp_exact_threshold",
            payout_usd=150.0,
            acceptance_probability=0.6,
            estimated_agent_hours=2,
            agent_hour_cost_usd=30.0,
            estimated_human_minutes=15,
            human_minute_cost_usd=1.0,
        )
        result = compute_eev_usd(data, scored_at="2026-08-07T00:00:00+00:00")
        self.assertEqual(result["expected_value_usd"], 15.0)
        self.assertTrue(result["threshold_pass"])

    def test_invalid_probability_fails_closed(self):
        data = OpportunityInputs(
            opportunity_id="opp_bad_probability",
            payout_usd=100.0,
            acceptance_probability=1.1,
            estimated_agent_hours=1,
            agent_hour_cost_usd=1,
            estimated_human_minutes=1,
            human_minute_cost_usd=1,
        )
        with self.assertRaises(ValueError):
            compute_eev_usd(data)


if __name__ == "__main__":
    unittest.main()
