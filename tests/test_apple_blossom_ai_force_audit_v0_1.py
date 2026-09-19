import unittest

from tools.apple_blossom_ai_force_audit_v0_1 import run


class AIForceAuditTests(unittest.TestCase):
    def test_announcement_without_instrument_advances_to_primary_bind_trigger(self):
        out = run({
            "reuters_announcement": True,
            "formal_instrument": False,
            "scope_defined": False,
            "girl_specific_edge": False,
        })
        self.assertEqual(out["announcement"], "OBSERVED")
        self.assertEqual(
            out["formal_instrument"],
            "NOT_OBSERVED_IN_CURRENT_SEARCH_SCOPE",
        )
        self.assertEqual(
            out["next_gate"],
            "AI_FORCE_PRIMARY_BIND_TRIGGER_V0_1",
        )
        self.assertFalse(out["authority_created"])


if __name__ == "__main__":
    unittest.main()
