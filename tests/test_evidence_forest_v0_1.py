import copy
import importlib.util
import sys
from pathlib import Path
import unittest

MODULE_PATH = Path(__file__).parents[1] / "tools" / "evidence_forest_v0_1.py"
spec = importlib.util.spec_from_file_location("evidence_forest_v0_1", MODULE_PATH)
mod = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = mod
assert spec.loader is not None
spec.loader.exec_module(mod)


def receipt(receipt_id, evidence_class):
    return {
        "schema_version": "0.1.0",
        "receipt_type": "epistemic_receipt_v0_1",
        "receipt_id": receipt_id,
        "timestamp": "2026-08-21T04:38:00Z",
        "moves": [
            {"code": "M1", "name": "DISCOVER"},
            {"code": "M2", "name": "CLASSIFY"},
            {"code": "M4", "name": "BIND"},
            {"code": "M7", "name": "REPLAY"},
            {"code": "M8", "name": "RECEIPT"},
        ],
        "sources": [{"pointer": f"user://{receipt_id}"}],
        "classifications": [{"label": evidence_class, "scope": None, "consent": None}],
        "genesis_status": "NOT_TESTED",
        "dissent_notes": [],
        "result_state": "PASS",
        "authority": False,
    }


class EvidenceForestTests(unittest.TestCase):
    def test_boundary_receipt_mutates_only_apple_blossom(self):
        state = mod.new_forest_state()
        before = copy.deepcopy(state["manifest"])
        out = mod.route_receipt(state, receipt("er_boundary_001", "BOUNDARY_RECEIPT"))
        self.assertEqual(out["status"], "ROUTED")
        self.assertEqual(out["root_mutated"], "apple_blossom")
        self.assertEqual(state["manifest"]["roots"]["apple_blossom"]["leaf_count"], 1)
        for name in ("family", "alabama", "leah_prime", "public_research"):
            self.assertEqual(state["manifest"]["roots"][name], before["roots"][name])
        self.assertNotEqual(out["forest_manifest_hash_before"], out["forest_manifest_hash_after"])
        self.assertFalse(out["authority_created"])

    def test_second_class_mutates_only_its_tree(self):
        state = mod.new_forest_state()
        mod.route_receipt(state, receipt("er_boundary_001", "BOUNDARY_RECEIPT"))
        apple_root = state["manifest"]["roots"]["apple_blossom"]["root"]
        out = mod.route_receipt(state, receipt("er_alabama_001", "PUBLIC_LOCAL"))
        self.assertEqual(out["root_mutated"], "alabama")
        self.assertEqual(state["manifest"]["roots"]["apple_blossom"]["root"], apple_root)
        self.assertEqual(state["manifest"]["roots"]["alabama"]["leaf_count"], 1)

    def test_conflicting_explicit_classes_hold_without_mutation(self):
        state = mod.new_forest_state()
        r = receipt("er_conflict_001", "PUBLIC_LOCAL")
        r["classifications"].append({"label": "PUBLIC_SOURCE", "scope": None, "consent": None})
        before = copy.deepcopy(state)
        out = mod.route_receipt(state, r)
        self.assertEqual(out["status"], "HOLD")
        self.assertEqual(out["classification"]["reason_codes"], ["CONFLICTING_EXPLICIT_CLASSES"])
        self.assertEqual(state, before)

    def test_missing_explicit_class_hold(self):
        state = mod.new_forest_state()
        r = receipt("er_missing_001", "PUBLIC_LOCAL")
        r["classifications"] = [{"label": "LOCAL_STORY", "scope": None, "consent": None}]
        out = mod.route_receipt(state, r)
        self.assertEqual(out["status"], "HOLD")
        self.assertIsNone(out["root_mutated"])

    def test_duplicate_is_noop(self):
        state = mod.new_forest_state()
        r = receipt("er_boundary_001", "BOUNDARY_RECEIPT")
        mod.route_receipt(state, r)
        before_hash = state["manifest"]["forest_manifest_hash"]
        out = mod.route_receipt(state, r)
        self.assertEqual(out["status"], "NOOP_DUPLICATE")
        self.assertEqual(state["manifest"]["roots"]["apple_blossom"]["leaf_count"], 1)
        self.assertEqual(state["manifest"]["forest_manifest_hash"], before_hash)

    def test_evidence_weight_is_process_completeness_not_truth(self):
        r = receipt("er_replayed_001", "PUBLIC_SOURCE")
        r["result_state"] = "CONFLICT"
        weight = mod.evidence_weight(r)
        self.assertEqual((weight.level, weight.label), (2, "REPLAYED"))

    def test_legacy_hints_do_not_mutate(self):
        hint = mod.legacy_hint_suggestion("method", "SAY", [])
        self.assertEqual(hint["decision"], "HINT_ONLY")
        self.assertEqual(hint["suggested_class"], "PRIVATE_OR_APPROVED")
        self.assertAlmostEqual(hint["routing_confidence"], 2 / 3, places=6)

    def test_manifest_hash_recomputes_deterministically(self):
        a = mod.new_forest_state()
        b = mod.new_forest_state()
        self.assertEqual(a["manifest"]["forest_manifest_hash"], b["manifest"]["forest_manifest_hash"])
        mod.route_receipt(a, receipt("er_same_001", "CREATIVE"))
        mod.route_receipt(b, receipt("er_same_001", "CREATIVE"))
        self.assertEqual(a["manifest"], b["manifest"])


if __name__ == "__main__":
    unittest.main()
