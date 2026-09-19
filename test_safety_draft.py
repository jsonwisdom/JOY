from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parent
DRAFT = ROOT / "SAFETY_DRAFT_V0_1.md"


class SafetyDraftContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = DRAFT.read_text(encoding="utf-8")

    def test_locked_requirements_are_exactly_present(self):
        required = (
            "HOW_WE_WILL_FAIL_SECTION          = REQUIRED",
            "LIVED_EXPERIENCE_YOUTH_REVIEWERS  = REQUIRED_AND_PAID",
            "ACCESSIBLE_ADULT_TESTING          = REQUIRED",
            "FAMILY_GAME_SAFETY_AUDIT          = SEPARATE",
            "MINOR_RECRUITMENT                 = BLOCKED",
            "PUBLIC_ACCESS                     = FALSE",
            "AUTHORITY_CREATED                 = FALSE",
        )
        for value in required:
            self.assertIn(value, self.text)

    def test_declaration_is_not_treated_as_storage_proof(self):
        self.assertIn("`what_was_not_shared` is a participant-facing declaration", self.text)
        for evidence in ("Data-flow tests", "Storage inspection", "Log audits", "Deletion tests"):
            self.assertIn(evidence, self.text)
        self.assertIn("NON_STORAGE_VERIFIED = FALSE", self.text)

    def test_satisfaction_is_not_the_only_metric(self):
        for metric in (
            "safety outcomes", "response time", "recurrence",
            "appeal availability and use", "independent-review outcomes",
        ):
            self.assertIn(metric, self.text)
        self.assertIn("cannot independently determine success", self.text)

    def test_completion_and_transition_remain_bounded(self):
        self.assertIn("SAFETY_DRAFT_COMPLETE = FALSE", self.text)
        self.assertIn("NEXT_TRANSITION       = VERIFY_COMMITTED_ARTIFACT", self.text)
        self.assertNotIn("SAFETY_DRAFT_COMPLETE = TRUE", self.text)

    def test_required_sections_exist(self):
        for heading in (
            "## Privacy verification boundary",
            "## Trial success metrics",
            "## How we will fail",
            "## Amendment history",
        ):
            self.assertIn(heading, self.text)


if __name__ == "__main__":
    unittest.main()
