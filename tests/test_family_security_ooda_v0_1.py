import copy
import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(HERE / "tools"))
from family_security_ooda_v0_1 import CATALOG_SHA256, REQUEST_SCHEMA, canonical, load_catalog, run

CATALOG = (HERE / "drills/FAMILY_SECURITY_OODA_SCENARIOS_V0_1.json").read_bytes()

def request(scenario_id="PHISHING_LINK", choice="PAUSE_AND_VERIFY_OFFLINE"):
    return {"schema": REQUEST_SCHEMA, "scenario_id": scenario_id, "choice": choice,
            "simulation": True, "authority": False, "family_gate": "SOVEREIGN_UNVERIFIED",
            "human_approval": "NOT_ASSERTED", "private_data": False,
            "external_actions": False, "signals": ["SYNTHETIC"]}

def replay(doc, catalog=CATALOG):
    return run(canonical(doc), catalog)

class OodaTests(unittest.TestCase):
    def test_catalog_pin(self):
        self.assertEqual(hashlib.sha256(CATALOG).hexdigest(), CATALOG_SHA256)
        self.assertEqual(len(load_catalog(CATALOG)), 6)

    def test_phishing_pass_but_effective_hold(self):
        r = replay(request())
        self.assertEqual((r["simulation_verdict"], r["effective_decision"]), ("PASS", "HOLD"))
        self.assertFalse(r["authority"])

    def test_private_info_pass(self):
        self.assertEqual(replay(request("PRIVATE_INFO", "DO_NOT_SHARE_AND_ASK_ADULT"))["simulation_verdict"], "PASS")

    def test_missing_receipt_pass(self):
        self.assertEqual(replay(request("MISSING_RECEIPT", "HOLD_UNTIL_VERIFIED"))["simulation_verdict"], "PASS")

    def test_rest_voluntary_pass(self):
        self.assertEqual(replay(request("PRESSURE_AND_PAUSE", "STOP_WITHOUT_PENALTY"))["simulation_verdict"], "PASS")

    def test_account_recovery_hold(self):
        self.assertEqual(replay(request("ACCOUNT_RECOVERY", "STOP_AND_ASK_ACCOUNT_OWNER"))["simulation_verdict"], "HOLD")

    def test_emergency_hold(self):
        self.assertEqual(replay(request("REAL_EMERGENCY", "STOP_DRILL_FOLLOW_LOCAL_PLAN"))["simulation_verdict"], "HOLD")

    def test_unsafe_click_reject(self):
        self.assertEqual(replay(request(choice="CLICK_THE_LINK"))["effective_decision"], "REJECT")

    def test_real_event_signal_conflict(self):
        r = request(); r["signals"] = ["SYNTHETIC", "REAL_EVENT_PRESENT"]
        self.assertEqual(replay(r)["effective_decision"], "CONFLICT")

    def test_unverified_alert_hold(self):
        r = request(); r["signals"] = ["SYNTHETIC", "UNVERIFIED_ALERT"]
        self.assertEqual(replay(r)["effective_decision"], "HOLD")

    def test_no_synthetic_signal_reject(self):
        r = request(); r["signals"] = ["REAL_EVENT_PRESENT"]
        self.assertEqual(replay(r)["effective_decision"], "REJECT")

    def test_duplicate_signals_reject(self):
        r = request(); r["signals"] = ["SYNTHETIC", "SYNTHETIC"]
        self.assertEqual(replay(r)["effective_decision"], "REJECT")

    def test_unknown_signal_reject(self):
        r = request(); r["signals"] = ["SYNTHETIC", "AUTHORITY_GRANT"]
        self.assertEqual(replay(r)["effective_decision"], "REJECT")

    def test_true_authority_reject(self):
        r = request(); r["authority"] = True
        self.assertEqual(replay(r)["effective_decision"], "REJECT")

    def test_string_authority_reject(self):
        r = request(); r["authority"] = "false"
        self.assertEqual(replay(r)["effective_decision"], "REJECT")

    def test_family_gate_forgery_reject(self):
        r = request(); r["family_gate"] = "APPROVED"
        self.assertEqual(replay(r)["effective_decision"], "REJECT")

    def test_consent_forgery_reject(self):
        r = request(); r["human_approval"] = "GRANTED"
        self.assertEqual(replay(r)["effective_decision"], "REJECT")

    def test_private_data_reject(self):
        r = request(); r["private_data"] = True
        self.assertEqual(replay(r)["effective_decision"], "REJECT")

    def test_external_action_reject(self):
        r = request(); r["external_actions"] = True
        self.assertEqual(replay(r)["effective_decision"], "REJECT")

    def test_extra_personal_field_reject_and_not_leak(self):
        r = request(); r["child_name"] = "PRIVATE_SAMPLE"
        o = replay(r)
        self.assertEqual(o["effective_decision"], "REJECT")
        self.assertNotIn("PRIVATE_SAMPLE", json.dumps(o))

    def test_unknown_scenario_reject(self):
        self.assertEqual(replay(request("FAMILY_MEMBER_FOLLOW", "TRACK"))["effective_decision"], "REJECT")

    def test_missing_field_reject(self):
        r = request(); del r["signals"]
        self.assertEqual(replay(r)["effective_decision"], "REJECT")

    def test_duplicate_json_keys_reject(self):
        self.assertEqual(run(b'{"schema":"A","schema":"B"}', CATALOG)["reason"], "duplicate_json_key")

    def test_malformed_json_reject(self):
        self.assertEqual(run(b'{', CATALOG)["effective_decision"], "REJECT")

    def test_nonfinite_json_reject(self):
        self.assertEqual(run(b'{"x":NaN}', CATALOG)["effective_decision"], "REJECT")

    def test_request_too_large_reject(self):
        self.assertEqual(run(b'a'*2049, CATALOG)["effective_decision"], "REJECT")

    def test_catalog_tamper_reject(self):
        self.assertEqual(replay(request(), CATALOG+b' ')["reason"], "catalog_sha256_drift")

    def test_catalog_missing_reject(self):
        self.assertEqual(replay(request(), b'')["effective_decision"], "REJECT")

    def test_hash_deterministic(self):
        self.assertEqual(replay(request()), replay(request()))

    def test_receipt_no_raw_personal_text(self):
        r = request(); r["nickname"]="SECRET_TEXT_1234"
        o = replay(r)
        self.assertNotIn("SECRET_TEXT_1234", json.dumps(o))
        self.assertEqual(o["contacts"], "NONE")

    def test_receipt_flags_never_promoted(self):
        for sid, scenario in load_catalog(CATALOG).items():
            o = replay(request(sid, scenario["safe_choice"]))
            self.assertEqual(o["effective_decision"], "HOLD")
            self.assertFalse(o["authority"])
            self.assertFalse(o["external_actions"])
            self.assertEqual(o["heidee_consent"], "NOT_INFERRED")

    def test_cli_reject_and_write_new_only(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td); inp=root/"input.json";out=root/"receipt.json"
            inp.write_bytes(canonical(request(choice="CLICK_THE_LINK")))
            cmd=[sys.executable,str(HERE/"tools/family_security_ooda_v0_1.py"),
                 "--request",str(inp),"--catalog",str(HERE/"drills/FAMILY_SECURITY_OODA_SCENARIOS_V0_1.json"),
                 "--receipt",str(out)]
            first=subprocess.run(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            self.assertEqual(first.returncode,2)
            self.assertEqual(json.loads(out.read_text())["effective_decision"],"REJECT")
            second=subprocess.run(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            self.assertEqual(second.returncode,2)
            self.assertIn(b"RECEIPT_WRITE_REJECTED",second.stderr)

if __name__ == '__main__':
    unittest.main()
