#!/usr/bin/env python3
"""Freeze or independently verify a deterministic family record set.

This tool hashes raw file bytes. It never normalizes source content.
The artifact root excludes observation time so an independent replay of the
same repository commit and scope can reproduce the same root.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

TOOL_ID = "freeze_family_records_v0_1.py"
TOOL_VERSION = "0.1.0"
SCHEMA_ID = "urn:jsonwisdom:schema:replay:family-frozen-artifact-manifest:v0.1"
LEAF_DOMAIN = b"JOY_FAMILY_FILE_V0_1"
ROOT_DOMAIN = b"JOY_FAMILY_MANIFEST_V0_1"
CANON_PROFILE = "JCS_SAFE_JSON_STRINGS_INTEGERS_BOOLEANS_NULL_V0_1"

RESERVED_PARTS = {".git", "__pycache__"}
DENIED_NAMES = {".DS_Store"}
DENIED_SUFFIXES = ("~", ".tmp", ".swp", ".swo")


class FreezeError(RuntimeError):
    """Fail-closed input or verification error."""


def sha256(data: bytes) -> bytes:
    return hashlib.sha256(data).digest()


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def reject_floats(value: Any, path: str = "$") -> None:
    if isinstance(value, float):
        raise FreezeError(f"float prohibited by canonical profile at {path}")
    if isinstance(value, dict):
        for key, item in value.items():
            reject_floats(item, f"{path}.{key}")
    elif isinstance(value, list):
        for index, item in enumerate(value):
            reject_floats(item, f"{path}[{index}]")


def canonical_json_bytes(value: Any) -> bytes:
    """Canonical JSON for this constrained manifest profile."""
    reject_floats(value)
    return json.dumps(
        value,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")


def safe_relative_path(root: Path, candidate: Path) -> str:
    try:
        relative = candidate.relative_to(root)
    except ValueError as exc:
        raise FreezeError(f"path escapes repository root: {candidate}") from exc

    posix = relative.as_posix()
    if not posix or posix.startswith("/") or "\\" in posix:
        raise FreezeError(f"invalid repository-relative path: {posix!r}")
    if any(part in {"", ".", ".."} for part in relative.parts):
        raise FreezeError(f"unsafe path component: {posix}")
    try:
        posix.encode("utf-8", errors="strict")
    except UnicodeEncodeError as exc:
        raise FreezeError(f"path is not valid UTF-8: {posix!r}") from exc
    return posix


def denied_path(path: Path) -> bool:
    if any(part in RESERVED_PARTS for part in path.parts):
        return True
    if path.name in DENIED_NAMES:
        return True
    return path.name.endswith(DENIED_SUFFIXES)


def iter_scope_files(root: Path, selected: Iterable[str]) -> list[tuple[str, Path]]:
    gathered: dict[str, Path] = {}

    for raw in selected:
        candidate = (root / raw).resolve(strict=False)
        if not candidate.exists():
            raise FreezeError(f"selected path does not exist: {raw}")
        if candidate.is_symlink():
            raise FreezeError(f"symlink denied: {raw}")

        paths: Iterable[Path]
        if candidate.is_dir():
            paths = candidate.rglob("*")
        elif candidate.is_file():
            paths = [candidate]
        else:
            raise FreezeError(f"unsupported filesystem object: {raw}")

        for path in paths:
            if denied_path(path):
                continue
            if path.is_symlink():
                raise FreezeError(f"symlink denied: {path}")
            if not path.is_file():
                continue
            relative = safe_relative_path(root, path.resolve())
            gathered.setdefault(relative, path)

    if not gathered:
        raise FreezeError("scope contains no files")

    casefold_seen: dict[str, str] = {}
    for relative in gathered:
        folded = relative.casefold()
        previous = casefold_seen.get(folded)
        if previous is not None and previous != relative:
            raise FreezeError(
                f"case-fold collision denied: {previous!r} vs {relative!r}"
            )
        casefold_seen[folded] = relative

    return sorted(gathered.items(), key=lambda item: item[0].encode("utf-8"))


def load_scope(scope_path: Path) -> dict[str, Any]:
    try:
        scope = json.loads(scope_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise FreezeError(f"cannot read scope file {scope_path}: {exc}") from exc

    required = {
        "scope_id",
        "repository",
        "source_ref",
        "source_commit_sha",
        "paths",
        "privacy_class",
    }
    missing = sorted(required - scope.keys())
    if missing:
        raise FreezeError(f"scope missing fields: {', '.join(missing)}")

    if not isinstance(scope["paths"], list) or not all(
        isinstance(item, str) and item for item in scope["paths"]
    ):
        raise FreezeError("scope.paths must be a non-empty string array")
    if not scope["paths"]:
        raise FreezeError("scope.paths must not be empty")

    sha = scope["source_commit_sha"]
    if not isinstance(sha, str) or len(sha) != 40 or any(
        ch not in "0123456789abcdef" for ch in sha
    ):
        raise FreezeError("source_commit_sha must be 40 lowercase hex characters")

    privacy = scope["privacy_class"]
    if privacy not in {"PUBLIC_SAFE", "FAMILY_PROTECTED", "REDACTED_DERIVATIVE"}:
        raise FreezeError(f"invalid privacy_class: {privacy!r}")

    return scope


def build_commitment(root: Path, scope: dict[str, Any]) -> dict[str, Any]:
    entries: list[dict[str, Any]] = []

    for relative, path in iter_scope_files(root, scope["paths"]):
        raw = path.read_bytes()
        raw_digest = sha256(raw)
        leaf = sha256(
            LEAF_DOMAIN
            + b"\x00"
            + relative.encode("utf-8")
            + b"\x00"
            + raw_digest
        )
        entries.append(
            {
                "path": relative,
                "size_bytes": len(raw),
                "raw_sha256": raw_digest.hex(),
                "leaf_commitment_sha256": leaf.hex(),
                "privacy_class": scope["privacy_class"],
            }
        )

    return {
        "scope_id": scope["scope_id"],
        "repository": scope["repository"],
        "source_ref": scope["source_ref"],
        "source_commit_sha": scope["source_commit_sha"],
        "path_order": "UTF8_BYTEWISE_ASCENDING",
        "bytes_policy": "RAW_EXACT_BYTES",
        "digest_algorithm": "SHA-256",
        "canonicalization_profile": CANON_PROFILE,
        "leaf_domain": LEAF_DOMAIN.decode("ascii"),
        "root_domain": ROOT_DOMAIN.decode("ascii"),
        "entries": entries,
    }


def artifact_root(commitment: dict[str, Any]) -> str:
    return sha256_hex(ROOT_DOMAIN + b"\x00" + canonical_json_bytes(commitment))


def manifest_without_file_hash(
    commitment: dict[str, Any], generated_at_utc: str
) -> dict[str, Any]:
    return {
        "$schema": SCHEMA_ID,
        "artifact": "FAMILY_FROZEN_ARTIFACT_MANIFEST",
        "version": "0.1.0",
        "state": "FROZEN_PENDING_INDEPENDENT_REPLAY",
        "authority_created": False,
        "canonized": False,
        "sealed": False,
        "commitment": commitment,
        "artifact_root_sha256": artifact_root(commitment),
        "observation": {
            "generated_at_utc": generated_at_utc,
            "tool_id": TOOL_ID,
            "tool_version": TOOL_VERSION,
            "independent_replay": False,
            "frozen_artifact_rail": "CANDIDATE",
            "verified_execution_rail": "NOT_RUN",
            "cross_rail_binding": "NOT_PROVEN",
        },
        "manifest_file_sha256": None,
    }


def encoded_manifest(manifest: dict[str, Any]) -> bytes:
    return (
        json.dumps(
            manifest,
            ensure_ascii=False,
            allow_nan=False,
            sort_keys=True,
            indent=2,
        )
        + "\n"
    ).encode("utf-8")


def write_manifest(output: Path, manifest: dict[str, Any]) -> str:
    # A file cannot contain its own exact digest without a recursive convention.
    # The in-file field remains null; the exact digest is written to a sidecar.
    final_bytes = encoded_manifest(manifest)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(final_bytes)
    exact_file_hash = sha256_hex(final_bytes)
    sidecar = output.with_suffix(output.suffix + ".sha256")
    sidecar.write_text(f"{exact_file_hash}  {output.name}\n", encoding="utf-8")
    return exact_file_hash


def freeze(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve(strict=True)
    if not root.is_dir():
        raise FreezeError(f"repository root is not a directory: {root}")

    scope = load_scope(Path(args.scope))
    commitment = build_commitment(root, scope)
    generated = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    manifest = manifest_without_file_hash(commitment, generated)
    exact_file_hash = write_manifest(Path(args.output), manifest)

    print(f"ARTIFACT_ROOT_SHA256={manifest['artifact_root_sha256']}")
    print(f"MANIFEST_EXACT_FILE_SHA256={exact_file_hash}")
    print("FROZEN_ARTIFACT_RAIL=CANDIDATE")
    print("VERIFIED_EXECUTION_RAIL=NOT_RUN")
    print("CROSS_RAIL_BINDING=NOT_PROVEN")
    return 0


def verify(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve(strict=True)
    manifest_path = Path(args.manifest)
    try:
        recorded = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise FreezeError(f"cannot read manifest {manifest_path}: {exc}") from exc

    commitment = recorded.get("commitment")
    if not isinstance(commitment, dict):
        raise FreezeError("manifest.commitment missing or invalid")

    recorded_entries = commitment.get("entries", [])
    if not isinstance(recorded_entries, list) or not recorded_entries:
        raise FreezeError("manifest contains no entries")

    privacy_values = {entry.get("privacy_class") for entry in recorded_entries}
    if len(privacy_values) != 1:
        raise FreezeError("v0.1 manifest requires one privacy class per scope")

    scope = {
        "scope_id": commitment.get("scope_id"),
        "repository": commitment.get("repository"),
        "source_ref": commitment.get("source_ref"),
        "source_commit_sha": commitment.get("source_commit_sha"),
        "paths": [entry.get("path") for entry in recorded_entries],
        "privacy_class": next(iter(privacy_values)),
    }

    rebuilt = build_commitment(root, scope)
    rebuilt_root = artifact_root(rebuilt)
    recorded_root = recorded.get("artifact_root_sha256")

    entries_match = rebuilt == commitment
    root_match = rebuilt_root == recorded_root

    print(f"RECORDED_ARTIFACT_ROOT_SHA256={recorded_root}")
    print(f"REBUILT_ARTIFACT_ROOT_SHA256={rebuilt_root}")
    print(f"ENTRIES_MATCH={str(entries_match).upper()}")
    print(f"ROOT_MATCH={str(root_match).upper()}")

    if entries_match and root_match:
        print("VERIFIED_EXECUTION_RAIL=PASSED")
        print("CROSS_RAIL_BINDING=PROVEN")
        return 0

    print("VERIFIED_EXECUTION_RAIL=FAILED")
    print("CROSS_RAIL_BINDING=MISMATCH")
    return 2


def parser() -> argparse.ArgumentParser:
    root = argparse.ArgumentParser(description=__doc__)
    sub = root.add_subparsers(dest="command", required=True)

    freeze_cmd = sub.add_parser("freeze", help="create a frozen artifact manifest")
    freeze_cmd.add_argument("--root", required=True, help="repository checkout root")
    freeze_cmd.add_argument("--scope", required=True, help="scope JSON path")
    freeze_cmd.add_argument("--output", required=True, help="manifest output path")
    freeze_cmd.set_defaults(func=freeze)

    verify_cmd = sub.add_parser(
        "verify", help="independently rebuild and compare an existing manifest"
    )
    verify_cmd.add_argument("--root", required=True, help="repository checkout root")
    verify_cmd.add_argument("--manifest", required=True, help="manifest JSON path")
    verify_cmd.set_defaults(func=verify)
    return root


def main() -> int:
    try:
        args = parser().parse_args()
        return int(args.func(args))
    except FreezeError as exc:
        print(f"DENIED: {exc}", file=sys.stderr)
        return 3
    except OSError as exc:
        print(f"DENIED: filesystem error: {exc}", file=sys.stderr)
        return 4


if __name__ == "__main__":
    raise SystemExit(main())
