#!/usr/bin/env python3
"""JOYSPACE Librarian advisory membrane. Offline, review-only, fail-closed.

No real-family identity lookup, no consent or approval, no network, no deployment.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

from family_security_ooda_v0_1 import run as run_ooda

SCHEMA = 'joyspace/librarian-family-gate-receipt/0.2'
# Committed Git blob SHA1 values checked against bytes, not commit descriptions.
PINS = (
    ('JOY', 'docs/school-of-wisdom/LIBRARIAN_SUGGESTIONS_GAMEPLAY_ALMS_ON_V0_1.md', '95f216f6e23e5edf72937f03e7d0d7f579983f99'),
    ('JOY', 'FAMILY/receipts/ALABAMA_ALMS_BOSS_BRE_LIBRARIAN_HEIDEE_MERGE_V0_1.md', 'de6c243360ba289d71906421ff7b80342f6ca0c2'),
    ('JOY', 'FAMILY/receipts/PUBLIC_REPO_AUTHORITY_PERIMETER_BOUNDARY_V0_1.md', 'afe19d59a507fa47522280249e0d1645a8a039d4'),
    ('JOY', 'docs/BOSS_BRE_FAMILY_SIDE_ACTIVATION_V0_1.md', '2c66e091177c37b6156dae27ab8970be36caec7e'),
    ('HEIDEE', 'HEIDEE_COMPUTER_WISDOM_FAMILY_LEGACY_REPORT_2026-11-07.md', '79e66f3281f8cb6272a7ea03058d4f12026ddb36'),
    ('HEIDEE', 'artifacts/HEIDEE_FAMILY_LEARNING_RAIL_BIND_V0.md', 'd05fb243d44b05fef6be502cbaaf0ee4dded8285'),
)
SHELVES = {
    'PHISHING_LINK': 'VERIFY_KNOWN_SOURCE',
    'PRIVATE_INFO': 'PROTECT_PRIVATE_INFORMATION',
    'ACCOUNT_RECOVERY': 'CONSULT_ACCOUNT_OWNER',
    'REAL_EMERGENCY': 'STOP_DRILL_USE_HOUSEHOLD_PLAN',
    'MISSING_RECEIPT': 'REQUEST_PRIMARY_RECEIPT',
    'PRESSURE_AND_PAUSE': 'PAUSE_WITHOUT_PENALTY',
}
ORDER = {'REJECT': 0, 'CONFLICT': 1, 'HOLD': 2, 'PASS': 3}
MAX_REQUEST_BYTES = 2048


def git_blob_sha(data: bytes) -> str:
    return hashlib.sha1(b'blob ' + str(len(data)).encode('ascii') + b'\0' + data).hexdigest()


def verify_sources(joy_root: Path, heidee_root: Path) -> list[dict]:
    roots = {'JOY': joy_root, 'HEIDEE': heidee_root}
    result = []
    for repo, rel, expected in PINS:
        file = roots[repo] / rel
        try:
            data = file.read_bytes()
        except OSError as exc:
            raise ValueError('source_missing_or_unreadable') from exc
        if git_blob_sha(data) != expected:
            raise ValueError('source_blob_mismatch')
        result.append({'repo': repo, 'path': rel, 'git_blob_sha1': expected})
    return result


def precedence(states) -> str:
    states = list(states)
    if not states or any(x not in ORDER for x in states):
        raise ValueError('invalid_decision_state')
    return min(states, key=lambda x: ORDER[x])


def canonical(data) -> bytes:
    return json.dumps(data, sort_keys=True, separators=(',', ':'), ensure_ascii=True, allow_nan=False).encode('ascii')


def receipt(state: str, reason: str, request_hash: str, sources=None, shelf='NO_SUGGESTION') -> dict:
    if state not in ORDER:
        raise ValueError('invalid_result_state')
    content = {
        'schema': SCHEMA,
        'interface': 'CANDIDATE_LIBRARIAN_ADVISORY_ONLY',
        'simulation_verdict': state,
        'effective_decision': 'HOLD' if state == 'PASS' else state,
        'reason': reason,
        'shelf': shelf,
        'request_sha256': request_hash,
        'verified_public_sources': sources or [],
        'roles': {
            'librarian': 'SOURCE_SUGGESTIONS_ONLY',
            'boss_bre': 'VOLUNTARY_PAUSE_AND_PRIVACY',
            'joy': 'SHARED_EDUCATIONAL_PATTERN',
            'heidee': 'INDEPENDENT_OPTIONAL_PARTICIPATION',
            'alms': 'SOURCE_REPLAY_NO_AUTHORITY',
        },
        'family_gate': 'SOVEREIGN_UNVERIFIED',
        'heidee_approval': 'NOT_INFERRED',
        'human_approval': 'NOT_ASSERTED',
        'authority': False,
        'public_release': False,
        'family_enrollment': False,
        'private_data_collected': False,
        'external_actions': False,
        'flywheel_maintenance': 'OFF',
    }
    content['receipt_sha256'] = hashlib.sha256(canonical(content)).hexdigest()
    return content


def execute(request_raw: bytes, catalog_raw: bytes, joy_root: Path, heidee_root: Path, *, source_verifier=verify_sources) -> dict:
    request_hash = hashlib.sha256(request_raw).hexdigest()
    try:
        if len(request_raw) > MAX_REQUEST_BYTES:
            raise ValueError('oversized_request')
        sources = source_verifier(joy_root, heidee_root)
        prior = run_ooda(request_raw, catalog_raw)
        state = precedence([prior['simulation_verdict']])
        # A valid syntax/choice can be synthetic PASS, but never generates approval.
        if state == 'PASS':
            req = json.loads(request_raw)
            shelf = SHELVES.get(req['scenario_id'], 'NO_SUGGESTION')
            return receipt(state, 'synthetic_guidance_only', request_hash, sources, shelf)
        return receipt(state, prior.get('reason', 'underlying_ooda_rejected'), request_hash, sources)
    except (ValueError, TypeError, KeyError, json.JSONDecodeError):
        return receipt('REJECT', 'source_or_request_integrity_rejected', request_hash)


def main(argv=None):
    p = argparse.ArgumentParser(description='Offline JOYSPACE Librarian candidate — NO authority')
    p.add_argument('--request', required=True)
    p.add_argument('--catalog', default='drills/FAMILY_SECURITY_OODA_SCENARIOS_V0_1.json')
    p.add_argument('--joy-root', required=True)
    p.add_argument('--heidee-root', required=True)
    p.add_argument('--receipt', default=None)
    a = p.parse_args(argv)
    try:
        req = Path(a.request).read_bytes()
        cat = Path(a.catalog).read_bytes()
    except OSError:
        req, cat = b'', b''
    result = execute(req, cat, Path(a.joy_root), Path(a.heidee_root))
    print('LIBRARIAN_INTERFACE=' + result['interface'])
    print('SIMULATION_VERDICT=' + result['simulation_verdict'])
    print('EFFECTIVE_DECISION=' + result['effective_decision'])
    print('RECEIPT_SHA256=' + result['receipt_sha256'])
    if a.receipt:
        try:
            with Path(a.receipt).open('xb') as f:  # never overwrite
                f.write(canonical(result) + b'\n')
        except OSError:
            print('RECEIPT_WRITE_REJECTED', file=sys.stderr)
            return 2
    return {'REJECT': 2, 'CONFLICT': 3, 'HOLD': 0, 'PASS': 2}[result['effective_decision']]

if __name__ == '__main__':
    raise SystemExit(main())
