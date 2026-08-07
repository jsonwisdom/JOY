#!/usr/bin/env python3
"""Read-only verifier for the sealed Atomic JOY v0.0.1 protocol.

Truth-state contract:
  GREEN  all required cryptographic, Git, schema, and immutability checks pass
  YELLOW verification completed but produced non-fatal warnings
  RED    a deterministic integrity check failed
  GRAY   verification could not be completed (missing source/dependency/runtime)

This module never writes to the repository.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path
from typing import Any

try:
    import rfc8785
except ImportError:  # handled as GRAY by verify_all()
    rfc8785 = None

try:
    from jsonschema import Draft7Validator
except ImportError:  # handled as GRAY by verify_all()
    Draft7Validator = None


PROTOCOL = "ATOMIC_JOY_REFLECTION_PROTOCOL"
VERSION = "0.0.1"
COMMIT_A = "39a026d9f5b09ea6d4d07c20608cb85835d37b6e"
COMMIT_B = "455e53bc67d78da9e903914d0b6d22fa82200f99"
COMMIT_C = "fa70b96676d22f75fc328c9b49a0599ae8377096"
EXPECTED_SEAL_SHA256 = "f422886213bf194be858f81c63414a563ccac72838255f26b9686ec98ab67da8"

MANIFEST_PATH = "reflections/SEAL_MANIFEST_v0.0.1.json"
INDEX_PATH = "reflections/index.json"
ANCHOR_PATH = "reflections/anchors/ANCHOR_v0.0.1.json"

ALLOWED_STATES = {"GREEN", "YELLOW", "RED", "GRAY"}


class VerificationUnavailable(RuntimeError):
    """Raised when verification cannot be completed from the local source."""


class JoyVerifier:
    def __init__(self, repo_root: Path | str | None = None) -> None:
        self.repo_root = Path(repo_root) if repo_root else Path(__file__).resolve().parents[1]
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.unavailable: list[str] = []
        self.checks: dict[str, bool] = {}
        self.details: dict[str, Any] = {
            "protocol": PROTOCOL,
            "version": VERSION,
            "commits": {"A": COMMIT_A, "B": COMMIT_B, "C": COMMIT_C},
        }

    @staticmethod
    def _sha256(data: bytes) -> str:
        return hashlib.sha256(data).hexdigest()

    def _git_bytes(self, *args: str, timeout: float = 10.0) -> bytes:
        try:
            proc = subprocess.run(
                ["git", *args],
                cwd=self.repo_root,
                capture_output=True,
                check=False,
                timeout=timeout,
            )
        except (OSError, subprocess.TimeoutExpired) as exc:
            raise VerificationUnavailable(f"git unavailable: {exc}") from exc
        if proc.returncode != 0:
            stderr = proc.stderr.decode("utf-8", errors="replace").strip()
            raise VerificationUnavailable(
                f"git {' '.join(args)} failed with code {proc.returncode}: {stderr or 'no stderr'}"
            )
        return proc.stdout

    def _git_text(self, *args: str, timeout: float = 10.0) -> str:
        return self._git_bytes(*args, timeout=timeout).decode("utf-8", errors="strict").strip()

    def _git_show(self, commit: str, path: str) -> bytes:
        return self._git_bytes("show", f"{commit}:{path}")

    def _commit_available(self, commit: str) -> bool:
        try:
            self._git_bytes("cat-file", "-e", f"{commit}^{{commit}}")
            return True
        except VerificationUnavailable:
            return False

    def _record(self, name: str, ok: bool, error: str | None = None) -> None:
        self.checks[name] = ok
        if not ok and error:
            self.errors.append(error)

    def _load_json(self, data: bytes, label: str) -> dict[str, Any]:
        try:
            value = json.loads(data.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise ValueError(f"{label} is not valid UTF-8 JSON: {exc}") from exc
        if not isinstance(value, dict):
            raise ValueError(f"{label} must be a JSON object")
        return value

    def _verify_git_chain(self) -> str:
        inside = self._git_text("rev-parse", "--is-inside-work-tree")
        if inside != "true":
            raise VerificationUnavailable("repo_root is not inside a Git work tree")

        head = self._git_text("rev-parse", "HEAD")
        self.details["head"] = head

        missing = [c for c in (COMMIT_A, COMMIT_B, COMMIT_C) if not self._commit_available(c)]
        if missing:
            raise VerificationUnavailable(
                "required sealed commit(s) unavailable in this checkout: " + ", ".join(missing)
            )

        parent_b = self._git_text("rev-parse", f"{COMMIT_B}^")
        parent_c = self._git_text("rev-parse", f"{COMMIT_C}^")
        self._record("commit_B_parent_is_A", parent_b == COMMIT_A, "Commit B is not a direct child of Commit A")
        self._record("commit_C_parent_is_B", parent_c == COMMIT_B, "Commit C is not a direct child of Commit B")

        try:
            self._git_bytes("merge-base", "--is-ancestor", COMMIT_C, head)
            ancestor = True
        except VerificationUnavailable:
            ancestor = False
        self._record("commit_C_in_HEAD_ancestry", ancestor, "Commit C is not in current HEAD ancestry")
        return head

    def _verify_manifest_and_schemas(self, head: str) -> tuple[bytes, dict[str, Any], list[str]]:
        manifest_bytes = self._git_show(COMMIT_A, MANIFEST_PATH)
        manifest = self._load_json(manifest_bytes, "seal manifest")

        self._record("manifest_protocol", manifest.get("protocol") == PROTOCOL, "Manifest protocol mismatch")
        self._record("manifest_version", manifest.get("protocol_version") == VERSION, "Manifest version mismatch")
        self._record(
            "manifest_frozen",
            manifest.get("schema_set_status") == "FROZEN",
            "Manifest schema_set_status is not FROZEN",
        )
        invariants = manifest.get("invariants", {})
        self._record(
            "no_fake_green",
            isinstance(invariants, dict) and invariants.get("NO_FAKE_GREEN") is True,
            "NO_FAKE_GREEN is not TRUE in the frozen manifest",
        )

        mark = manifest.get("author_design_signature", {})
        mark_ok = (
            isinstance(mark, dict)
            and mark.get("signed_by") == "JAY"
            and mark.get("design_sequence") == [3, 6, 9]
            and mark.get("signature_type") == "DECLARED_AUTHOR_MARK"
            and mark.get("cryptographic_signature") is False
        )
        self._record("declared_author_mark", mark_ok, "Declared JAY 3/6/9 author mark mismatch")

        schema_files = manifest.get("schema_files")
        if not isinstance(schema_files, list) or len(schema_files) != 5:
            self._record("schema_file_count", False, "Manifest must list exactly five sealed schema files")
            return manifest_bytes, manifest, []
        self._record("schema_file_count", True)

        schema_hashes: list[str] = []
        for item in schema_files:
            if not isinstance(item, dict) or not isinstance(item.get("path"), str) or not isinstance(item.get("sha256"), str):
                self.errors.append("Malformed schema_files entry in manifest")
                continue
            path = item["path"]
            expected = item["sha256"]
            sealed_bytes = self._git_show(COMMIT_A, path)
            actual = self._sha256(sealed_bytes)
            self._record(f"schema_hash:{path}", actual == expected, f"Schema SHA-256 mismatch: {path}")
            schema_hashes.append(expected)

            current_bytes = self._git_show(head, path)
            self._record(
                f"schema_immutable:{path}",
                current_bytes == sealed_bytes,
                f"Frozen schema changed after seal: {path}",
            )

            if Draft7Validator is not None:
                try:
                    Draft7Validator.check_schema(self._load_json(sealed_bytes, path))
                    self._record(f"schema_meta_valid:{path}", True)
                except Exception as exc:
                    self._record(f"schema_meta_valid:{path}", False, f"Draft-07 meta-validation failed for {path}: {exc}")

        current_manifest = self._git_show(head, MANIFEST_PATH)
        self._record(
            "manifest_immutable",
            current_manifest == manifest_bytes,
            "Frozen seal manifest changed after Commit A",
        )
        return manifest_bytes, manifest, schema_hashes

    def _verify_seal_and_anchor(
        self,
        head: str,
        manifest_bytes: bytes,
        manifest: dict[str, Any],
        schema_hashes: list[str],
    ) -> tuple[dict[str, Any], dict[str, Any]]:
        if rfc8785 is None:
            raise VerificationUnavailable("Python dependency 'rfc8785' is not installed")
        if Draft7Validator is None:
            raise VerificationUnavailable("Python dependency 'jsonschema' is not installed")

        index_b_bytes = self._git_show(COMMIT_B, INDEX_PATH)
        index_b = self._load_json(index_b_bytes, "Commit B reflection index")
        self._record("index_version", index_b.get("version") == VERSION, "Commit B index version mismatch")
        self._record("index_schema_sealed", index_b.get("schema_sealed") is True, "Commit B index is not schema_sealed=true")

        manifest_hash = self._sha256(manifest_bytes)
        seal_timestamp = index_b.get("seal_timestamp")
        if not isinstance(seal_timestamp, str):
            self._record("seal_timestamp_present", False, "Commit B index seal_timestamp missing")
            seal_timestamp = ""
        else:
            self._record("seal_timestamp_present", True)

        recipe = {
            "schemas": schema_hashes,
            "manifest": manifest_hash,
            "protocol_version": VERSION,
            "timestamp": seal_timestamp,
        }
        try:
            seal_bytes = rfc8785.dumps(recipe)
        except Exception as exc:
            raise VerificationUnavailable(f"RFC 8785 canonicalization failed: {exc}") from exc
        computed_seal = self._sha256(seal_bytes)
        recorded_seal = index_b.get("seal_hash")
        self.details["seal_recipe"] = recipe
        self.details["computed_seal_sha256"] = computed_seal
        self._record("seal_hash_matches_index", computed_seal == recorded_seal, "Recomputed seal hash does not match Commit B index")
        self._record("seal_hash_matches_frozen_constant", computed_seal == EXPECTED_SEAL_SHA256, "Recomputed seal hash does not match frozen v0.0.1 seal")

        anchor_bytes = self._git_show(COMMIT_C, ANCHOR_PATH)
        anchor = self._load_json(anchor_bytes, "Commit C anchor")
        self._record("anchor_points_to_commit_B", anchor.get("index_commit_sha") == COMMIT_B, "Anchor index_commit_sha mismatch")
        self._record(
            "anchor_index_content_hash",
            anchor.get("index_content_sha256") == self._sha256(index_b_bytes),
            "Anchor index_content_sha256 mismatch",
        )

        canonical_contract = manifest.get("canonical_state_contract", {})
        state = canonical_contract.get("shape") if isinstance(canonical_contract, dict) else None
        if not isinstance(state, dict):
            self._record("canonical_state_present", False, "Canonical state shape missing from manifest")
            computed_state_head = ""
        else:
            self._record("canonical_state_present", True)
            try:
                computed_state_head = self._sha256(rfc8785.dumps(state))
            except Exception as exc:
                raise VerificationUnavailable(f"Canonical state serialization failed: {exc}") from exc
        self.details["computed_state_head_hash"] = computed_state_head
        self._record(
            "anchor_state_head_hash",
            anchor.get("state_head_hash") == computed_state_head,
            "Anchor state_head_hash mismatch",
        )

        current_anchor = self._git_show(head, ANCHOR_PATH)
        self._record("anchor_immutable", current_anchor == anchor_bytes, "Anchor changed after Commit C")

        current_index = self._load_json(self._git_show(head, INDEX_PATH), "current reflection index")
        self._record("current_index_seal_retained", current_index.get("seal_hash") == EXPECTED_SEAL_SHA256, "Current index no longer retains the v0.0.1 seal hash")
        self._record("current_index_schema_sealed", current_index.get("schema_sealed") is True, "Current index no longer reports schema_sealed=true")

        return current_index, anchor

    def _verify_reflection_immutability(self, current_index: dict[str, Any], head: str) -> tuple[str, str]:
        entries = current_index.get("entries")
        if not isinstance(entries, list):
            self._record("reflection_entries_present", False, "Current index entries are missing")
            return "unknown", "unknown"

        entry = next((x for x in entries if isinstance(x, dict) and x.get("uid") == "REFLECTION_0001"), None)
        if not isinstance(entry, dict):
            self._record("reflection_0001_present", False, "REFLECTION_0001 missing from current index")
            return "unknown", "unknown"
        self._record("reflection_0001_present", True)

        status = str(entry.get("status", "unknown"))
        path = entry.get("path")
        content_commit = entry.get("content_commit_sha")
        expected_hash_field = entry.get("content_hash")
        receipt_path = entry.get("receipt_path")
        receipt_commit = entry.get("receipt_commit_sha")

        if not all(isinstance(v, str) for v in (path, content_commit, expected_hash_field, receipt_path, receipt_commit)):
            self._record("reflection_0001_receipt_fields", False, "REFLECTION_0001 anchoring fields malformed")
            return status, "unknown"
        self._record("reflection_0001_receipt_fields", True)

        expected_hash = expected_hash_field.removeprefix("sha256:")
        original_content = self._git_show(content_commit, path)
        self._record(
            "reflection_0001_content_hash",
            self._sha256(original_content) == expected_hash,
            "REFLECTION_0001 content SHA-256 mismatch",
        )
        current_content = self._git_show(head, path)
        self._record(
            "reflection_0001_content_immutable",
            current_content == original_content,
            "REFLECTION_0001 content changed after its content commit",
        )

        original_receipt = self._git_show(receipt_commit, receipt_path)
        current_receipt = self._git_show(head, receipt_path)
        self._record(
            "reflection_0001_receipt_immutable",
            current_receipt == original_receipt,
            "REFLECTION_0001 receipt changed after its receipt commit",
        )
        return status, expected_hash

    def verify_all(self) -> dict[str, Any]:
        try:
            head = self._verify_git_chain()
            manifest_bytes, manifest, schema_hashes = self._verify_manifest_and_schemas(head)
            current_index, anchor = self._verify_seal_and_anchor(
                head, manifest_bytes, manifest, schema_hashes
            )
            reflection_status, reflection_hash = self._verify_reflection_immutability(current_index, head)
            self.details["reflection_0001"] = {
                "status": reflection_status,
                "content_sha256": reflection_hash,
            }
            self.details["anchor"] = anchor
        except VerificationUnavailable as exc:
            self.unavailable.append(str(exc))
        except (ValueError, UnicodeError) as exc:
            self.errors.append(str(exc))
        except Exception as exc:
            self.unavailable.append(f"unexpected verifier failure: {type(exc).__name__}: {exc}")

        if self.errors:
            state = "RED"
        elif self.unavailable:
            state = "GRAY"
        elif self.warnings:
            state = "YELLOW"
        else:
            state = "GREEN"

        self.details["checks"] = self.checks
        if self.unavailable:
            self.details["unavailable"] = self.unavailable
        if self.warnings:
            self.details["warnings"] = self.warnings

        issues = [*self.errors, *self.unavailable, *self.warnings]
        return {
            "state": state,
            "protocol": PROTOCOL,
            "version": VERSION,
            "schema_sealed": bool(
                self.checks.get("index_schema_sealed", False)
                and self.checks.get("seal_hash_matches_index", False)
                and self.checks.get("seal_hash_matches_frozen_constant", False)
            ),
            "seal_sha256": self.details.get("computed_seal_sha256", "unknown"),
            "reflection_id": "REFLECTION_0001",
            "reflection_status": self.details.get("reflection_0001", {}).get("status", "unknown"),
            "no_fake_green": True,
            "errors": issues,
            "details": self.details,
        }


def _exit_code(state: str) -> int:
    return {"GREEN": 0, "RED": 1, "YELLOW": 2, "GRAY": 3}.get(state, 3)


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify sealed Atomic JOY v0.0.1 receipts")
    parser.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    parser.add_argument("--repo", type=Path, default=None, help="path to the JOY Git checkout")
    args = parser.parse_args()

    result = JoyVerifier(args.repo).verify_all()
    state = result.get("state", "GRAY")
    if state not in ALLOWED_STATES:
        state = "GRAY"
        result["state"] = state
        result.setdefault("errors", []).append("Verifier returned an invalid truth state")

    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print(f"Atomic JOY {result.get('version', VERSION)}: {state}")
        print(f"Seal SHA-256: {result.get('seal_sha256', 'unknown')}")
        print(f"REFLECTION_0001: {result.get('reflection_status', 'unknown')}")
        for issue in result.get("errors", []):
            print(f"- {issue}")

    return _exit_code(state)


if __name__ == "__main__":
    raise SystemExit(main())
