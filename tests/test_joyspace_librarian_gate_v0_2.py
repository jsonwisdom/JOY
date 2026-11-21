import copy
import hashlib
import itertools
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tools'))
from joyspace_librarian_gate_v0_2 import (PINS, SHELVES, canonical, execute,
    git_blob_sha, precedence, receipt, verify_sources)

CATALOG = (ROOT / 'drills/FAMILY_SECURITY_OODA_SCENARIOS_V0_1.json').read_bytes()
GOOD = json.loads((ROOT / 'drills/FAMILY_SECURITY_OODA_EXAMPLE_V0_1.json').read_text())


def fake_verify(_joy, _heidee):
    return [{'repo': 'JOY', 'path': 'synthetic_test_only', 'git_blob_sha1': 'SYNTHETIC'}]


def call(data, cat=CATALOG, verify=fake_verify):
    return execute(canonical(data), cat, Path('.'), Path('.'), source_verifier=verify)


class LibrarianTests(unittest.TestCase):
    def test_256_state_combinations(self):
        values = ['REJECT', 'CONFLICT', 'HOLD', 'PASS']
        all_states = list(itertools.product(values, repeat=4))
        self.assertEqual(len(all_states), 256)
        for states in all_states:
            self.assertEqual(precedence(states), next(v for v in values if v in states))

    def test_single_all_pass(self):
        self.assertEqual(sum(all(v == 'PASS' for v in a)
                             for a in itertools.product(('REJECT', 'CONFLICT', 'HOLD', 'PASS'), repeat=4)), 1)

    def test_invalid_empty_states(self):
        with self.assertRaises(ValueError): precedence([])

    def test_invalid_unknown_state(self):
        with self.assertRaises(ValueError): precedence(['GREEN'])

    def test_good_choice_hold(self):
        r = call(GOOD)
        self.assertEqual(r['simulation_verdict'], 'PASS')
        self.assertEqual(r['effective_decision'], 'HOLD')
        self.assertEqual(r['shelf'], 'VERIFY_KNOWN_SOURCE')
        self.assertEqual(r['heidee_approval'], 'NOT_INFERRED')
        self.assertIs(r['authority'], False)

    def test_all_shelves_are_bounded(self):
        cat = json.loads(CATALOG)
        for x in cat['scenarios']:
            q = copy.deepcopy(GOOD)
            q['scenario_id'] = x['id']
            q['choice'] = x['safe_choice']
            r = call(q)
            self.assertEqual(r['shelf'] in SHELVES, False)  # shelf labels are not scenario IDs
            self.assertEqual(r['shelf'] in SHELVES.values(), r['simulation_verdict'] == 'PASS')
            self.assertIs(r['authority'], False)
            self.assertIs(r['family_enrollment'], False)
            self.assertIs(r['public_release'], False)

    def test_wrong_choice_rejects(self):
        q = copy.deepcopy(GOOD); q['choice'] = 'CLICK_THE_LINK'
        self.assertEqual(call(q)['effective_decision'], 'REJECT')

    def test_unauthorized_consent_rejects(self):
        q = copy.deepcopy(GOOD); q['human_approval'] = 'GRANTED'
        self.assertEqual(call(q)['effective_decision'], 'REJECT')

    def test_true_authority_rejects(self):
        q = copy.deepcopy(GOOD); q['authority'] = True
        self.assertEqual(call(q)['effective_decision'], 'REJECT')

    def test_private_field_rejects_and_does_not_leak(self):
        q = copy.deepcopy(GOOD); q['private_child_name'] = 'NEVER_PUBLISH_VALUE'
        r = call(q)
        self.assertEqual(r['effective_decision'], 'REJECT')
        self.assertNotIn('NEVER_PUBLISH_VALUE', json.dumps(r))

    def test_parent_gate_corruption_rejects(self):
        q = copy.deepcopy(GOOD); q['family_gate'] = 'BYPASSED'
        self.assertEqual(call(q)['effective_decision'], 'REJECT')

    def test_external_action_rejects(self):
        q = copy.deepcopy(GOOD); q['external_actions'] = True
        self.assertEqual(call(q)['effective_decision'], 'REJECT')

    def test_real_event_conflict(self):
        q = copy.deepcopy(GOOD); q['signals'] = ['SYNTHETIC', 'REAL_EVENT_PRESENT']
        self.assertEqual(call(q)['effective_decision'], 'CONFLICT')

    def test_unverified_signal_hold(self):
        q = copy.deepcopy(GOOD); q['signals'] = ['SYNTHETIC', 'UNVERIFIED_ALERT']
        self.assertEqual(call(q)['effective_decision'], 'HOLD')

    def test_deterministic_receipt(self):
        self.assertEqual(call(GOOD), call(GOOD))

    def test_source_verifier_failure_rejects(self):
        def fail(*_): raise ValueError('failed_pin')
        self.assertEqual(call(GOOD, verify=fail)['effective_decision'], 'REJECT')

    def test_source_verifier_cannot_leak_secret_error(self):
        def fail(*_): raise ValueError('SECRET_NOT_FOR_RECEIPT')
        self.assertNotIn('SECRET_NOT_FOR_RECEIPT', json.dumps(call(GOOD, verify=fail)))

    def test_empty_request_rejects(self):
        self.assertEqual(execute(b'', CATALOG, Path('.'), Path('.'), source_verifier=fake_verify)['effective_decision'], 'REJECT')

    def test_oversize_rejects(self):
        self.assertEqual(execute(b'x'*4096, CATALOG, Path('.'), Path('.'), source_verifier=fake_verify)['effective_decision'], 'REJECT')

    def test_duplicate_json_key_rejects(self):
        self.assertEqual(execute(b'{"schema":"X","schema":"Y"}', CATALOG, Path('.'), Path('.'), source_verifier=fake_verify)['effective_decision'], 'REJECT')

    def test_tampered_catalog_rejects(self):
        self.assertEqual(call(GOOD, cat=CATALOG+b' ' )['effective_decision'], 'REJECT')

    def test_git_blob_encoding(self):
        content=b'test\n'
        self.assertEqual(git_blob_sha(content), hashlib.sha1(b'blob 5\0test\n').hexdigest())

    def test_missing_sources_reject(self):
        with tempfile.TemporaryDirectory() as t:
            with self.assertRaisesRegex(ValueError,'missing'):
                verify_sources(Path(t), Path(t))

    def test_source_tamper_reject(self):
        with tempfile.TemporaryDirectory() as t:
            joy=Path(t)/'JOY'; heidee=Path(t)/'HEIDEE'
            for repo, rel, _sha in PINS:
                p=(joy if repo=='JOY' else heidee)/rel
                p.parent.mkdir(parents=True,exist_ok=True)
                p.write_bytes(b'wrong byte contents')
            with self.assertRaisesRegex(ValueError,'mismatch'):
                verify_sources(joy,heidee)

    def test_missing_heidee_reject(self):
        with tempfile.TemporaryDirectory() as t:
            r=execute(canonical(GOOD), CATALOG, Path(t), Path(t))
            self.assertEqual(r['effective_decision'], 'REJECT')

    def test_no_network_or_tracking_fields(self):
        r=call(GOOD)
        self.assertEqual(r['external_actions'],False)
        self.assertEqual(r['private_data_collected'],False)
        self.assertEqual(r['flywheel_maintenance'],'OFF')

    def test_suggestion_never_approval(self):
        for state in ('PASS','HOLD','CONFLICT','REJECT'):
            r=receipt(state,'synthetic', '0'*64)
            self.assertEqual(r['heidee_approval'],'NOT_INFERRED')
            self.assertEqual(r['family_gate'],'SOVEREIGN_UNVERIFIED')

if __name__ == '__main__': unittest.main()
