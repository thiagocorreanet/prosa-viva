#!/usr/bin/env python3
"""Validate the public Prosa Viva plugin package and release metadata."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


PLUGIN_NAME = "prosa-viva"
AUTHOR_NAME = "Thiago Corrêa"
AUTHOR_URL = "https://github.com/thiagocorreanet"
REPOSITORY_URL = "https://github.com/thiagocorreanet/prosa-viva"
SOURCE_URL = REPOSITORY_URL + ".git"
SEMVER = re.compile(
    r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-[0-9A-Za-z.-]+)?$"
)
REQUIRED_FILES = (
    "LICENSE",
    "README.md",
    "skills/refinar-prosa/SKILL.md",
    "skills/refinar-prosa/agents/openai.yaml",
)
FORBIDDEN_COMPONENTS = ("apps", "hooks", "mcpServers")
PLACEHOLDER = re.compile(r"\[TODO:[^\]]*\]", re.IGNORECASE)


def load_object(path: Path) -> dict[str, object]:
    if not path.is_file():
        raise ValueError(f"missing required file: {path.name}")
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise ValueError(f"invalid JSON in {path}: {error.msg}") from error
    if not isinstance(payload, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return payload


def require_string(
    payload: dict[str, object], field: str, source: Path
) -> str:
    value = payload.get(field)
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{source} field {field!r} must be a non-empty string")
    return value


def require_object(
    payload: dict[str, object], field: str, source: Path
) -> dict[str, object]:
    value = payload.get(field)
    if not isinstance(value, dict):
        raise ValueError(f"{source} field {field!r} must be an object")
    return value


def resolve_declared_path(root: Path, value: str) -> Path:
    if not value.startswith("./"):
        raise ValueError(
            f"declared path must start with './' and stay inside the plugin: {value}"
        )
    resolved = (root / value).resolve()
    if not resolved.is_relative_to(root):
        raise ValueError(f"declared path must stay inside the plugin: {value}")
    if not resolved.exists():
        raise ValueError(f"declared path does not exist: {value}")
    return resolved


def scan_forbidden_content(root: Path, release_notes: Path) -> None:
    if (root / ".claude-plugin").exists() or (root / "CLAUDE.md").exists():
        raise ValueError("Claude-specific manifests are forbidden in the public package")

    paths = [
        root / ".codex-plugin" / "plugin.json",
        root / ".agents" / "plugins" / "marketplace.json",
        root / "README.md",
        root / "LICENSE",
        root / "skills" / "refinar-prosa" / "SKILL.md",
        root / "skills" / "refinar-prosa" / "agents" / "openai.yaml",
        release_notes,
    ]
    for path in paths:
        if path.is_file() and PLACEHOLDER.search(path.read_text(encoding="utf-8")):
            raise ValueError(f"placeholder found in public content: {path}")


def _validate_manifest(root: Path) -> tuple[dict[str, object], str]:
    manifest_path = root / ".codex-plugin" / "plugin.json"
    manifest = load_object(manifest_path)
    if require_string(manifest, "name", manifest_path) != PLUGIN_NAME:
        raise ValueError(f"plugin name must be {PLUGIN_NAME}")

    version = require_string(manifest, "version", manifest_path)
    if "+" in version:
        raise ValueError("public version cannot contain a Codex cachebuster")
    if SEMVER.fullmatch(version) is None:
        raise ValueError(f"public version is not strict SemVer: {version}")

    require_string(manifest, "description", manifest_path)
    author = require_object(manifest, "author", manifest_path)
    if require_string(author, "name", manifest_path) != AUTHOR_NAME:
        raise ValueError(f"manifest author.name must be {AUTHOR_NAME}")
    if require_string(author, "url", manifest_path) != AUTHOR_URL:
        raise ValueError(f"manifest author.url must be {AUTHOR_URL}")
    if require_string(manifest, "homepage", manifest_path) != REPOSITORY_URL:
        raise ValueError(f"manifest homepage must be {REPOSITORY_URL}")
    if require_string(manifest, "repository", manifest_path) != REPOSITORY_URL:
        raise ValueError(f"manifest repository must be {REPOSITORY_URL}")
    if require_string(manifest, "license", manifest_path) != "MIT":
        raise ValueError("manifest license must be MIT")

    skills = require_string(manifest, "skills", manifest_path)
    if not resolve_declared_path(root, skills).is_dir():
        raise ValueError("manifest skills path must point to a directory")
    for component in FORBIDDEN_COMPONENTS:
        if component in manifest:
            raise ValueError(f"public v0.1.0 must not declare {component}")

    interface = require_object(manifest, "interface", manifest_path)
    expected_interface = {
        "displayName": "Prosa Viva",
        "developerName": AUTHOR_NAME,
        "category": "Productivity",
        "websiteURL": REPOSITORY_URL,
    }
    for field in ("shortDescription", "longDescription"):
        require_string(interface, field, manifest_path)
    for field, expected in expected_interface.items():
        if require_string(interface, field, manifest_path) != expected:
            raise ValueError(f"manifest interface.{field} must be {expected}")
    if not isinstance(interface.get("capabilities"), list):
        raise ValueError("manifest interface.capabilities must be an array")
    prompts = interface.get("defaultPrompt")
    if not isinstance(prompts, list) or not prompts or not all(
        isinstance(prompt, str) and prompt.strip() for prompt in prompts
    ):
        raise ValueError("manifest interface.defaultPrompt must contain prompts")
    return manifest, version


def _validate_marketplace(root: Path, expected_tag: str) -> None:
    marketplace_path = root / ".agents" / "plugins" / "marketplace.json"
    marketplace = load_object(marketplace_path)
    if require_string(marketplace, "name", marketplace_path) != PLUGIN_NAME:
        raise ValueError(f"marketplace name must be {PLUGIN_NAME}")
    interface = require_object(marketplace, "interface", marketplace_path)
    if require_string(interface, "displayName", marketplace_path) != "Prosa Viva":
        raise ValueError("marketplace interface.displayName must be Prosa Viva")

    plugins = marketplace.get("plugins")
    if not isinstance(plugins, list) or len(plugins) != 1:
        raise ValueError("marketplace must contain exactly one plugin")
    entry = plugins[0]
    if not isinstance(entry, dict):
        raise ValueError("marketplace plugin entry must be an object")
    if require_string(entry, "name", marketplace_path) != PLUGIN_NAME:
        raise ValueError(f"marketplace plugin name must be {PLUGIN_NAME}")
    source = require_object(entry, "source", marketplace_path)
    expected_source = {"source": "url", "url": SOURCE_URL, "ref": expected_tag}
    if source != expected_source:
        raise ValueError(
            f"marketplace source must point to {SOURCE_URL} at {expected_tag}"
        )
    policy = require_object(entry, "policy", marketplace_path)
    if policy != {"installation": "AVAILABLE", "authentication": "ON_INSTALL"}:
        raise ValueError("marketplace policy must be AVAILABLE and ON_INSTALL")
    if require_string(entry, "category", marketplace_path) != "Productivity":
        raise ValueError("marketplace category must be Productivity")


def validate_release(root: Path, tag: str | None = None) -> tuple[str, ...]:
    root = root.expanduser().resolve()
    if root.name != PLUGIN_NAME:
        raise ValueError(f"plugin root directory must be named {PLUGIN_NAME}")

    _, version = _validate_manifest(root)
    expected_tag = f"v{version}"
    if tag is not None and tag != expected_tag:
        raise ValueError(f"release tag must be {expected_tag}, got {tag}")
    _validate_marketplace(root, expected_tag)

    for relative_path in REQUIRED_FILES:
        if not (root / relative_path).is_file():
            raise ValueError(f"missing required file: {relative_path}")
    license_text = (root / "LICENSE").read_text(encoding="utf-8")
    if "MIT License" not in license_text:
        raise ValueError("LICENSE must contain the MIT License")
    if "Copyright (c) 2026 Thiago Corrêa" not in license_text:
        raise ValueError("LICENSE copyright must name Thiago Corrêa")

    release_notes = root / "docs" / "releases" / f"{expected_tag}.md"
    if not release_notes.is_file():
        raise ValueError(f"missing release notes: docs/releases/{expected_tag}.md")
    scan_forbidden_content(root, release_notes)
    return (
        f"plugin={PLUGIN_NAME}",
        f"version={version}",
        f"release={expected_tag}",
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="Plugin root (defaults to this repository).",
    )
    parser.add_argument("--tag", help="Release tag to compare with the manifest.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    for result in validate_release(args.root, args.tag):
        print(result)


if __name__ == "__main__":
    try:
        main()
    except Exception as error:  # noqa: BLE001 - CLI surfaces one concise failure.
        print(str(error), file=sys.stderr)
        raise SystemExit(1) from error
