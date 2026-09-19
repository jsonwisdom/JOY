import unittest

from tools.apple_blossom_ai_naming_audit_v0_1 import (
    abbreviation_collision,
    answer_question,
    validate_states,
)


class AppleBlossomAINamingAuditTests(unittest.TestCase):
    def test_si_collision(self):
        self.assertTrue(
            abbreviation_collision(
                {
                    "Superior Intelligence": "SI",
                    "Extreme Intelligence": "EI",
                    "Supreme Intelligence": "SI",
                }
            )
        )

    def test_auto_advance_to_taxonomy_collision(self):
        result = answer_question(
            {
                "naming_event_observed": True,
                "white_house_uses_ai": True,
                "nist_uses_ai": True,
                "nist_published_asi_mentions": True,
            }
        )
        validate_states(result)
        self.assertEqual(result["legal_term_changed"], "NOT_OBSERVED")
        self.assertEqual(result["taxonomy_collision"], "OBSERVED")
        self.assertEqual(
            result["next_gate"], "SUPERINTELLIGENCE_TAXONOMY_COLLISION_V0_1"
        )

    def test_missing_official_term_holds(self):
        result = answer_question(
            {
                "naming_event_observed": True,
                "white_house_uses_ai": False,
                "nist_uses_ai": True,
                "nist_published_asi_mentions": True,
            }
        )
        self.assertEqual(result["legal_term_changed"], "HOLD")
        self.assertEqual(result["next_gate"], "RESOLVE_CURRENT_OPERATIVE_TERM")


if __name__ == "__main__":
    unittest.main()
