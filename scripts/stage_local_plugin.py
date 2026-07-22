#!/usr/bin/env python3
"""Create a disposable, installable staging copy of Prosa Viva."""

from __future__ import annotations

import argparse
import json
import shutil
import tempfile
from pathlib import Path
from uuid import uuid4


PLUGIN_NAME = "prosa-viva"
DIRECTORY_ALLOWLIST = (".codex-plugin", "skills")
FILE_ALLOWLIST = ("README.md", "LICENSE")
DEFAULT_SOURCE = Path(__file__).resolve().parents[1]
DEFAULT_DESTINATION = Path.home() / "plugins" / PLUGIN_NAME


def _validate_paths(source: Path, destination: Path) -> None:
    if source == destination:
        raise ValueError("source and destination must be different directories")
    if destination == Path(destination.anchor):
        raise ValueError("destination cannot be the filesystem root")
    if destination == Path.home().resolve():
        raise ValueError("destination cannot be the user home directory")
    if destination.name != PLUGIN_NAME:
        raise ValueError(f"destination directory must be named {PLUGIN_NAME}")
    if source in destination.parents or destination in source.parents:
        raise ValueError("source and destination cannot contain one another")


def _validate_source(source: Path) -> None:
    manifest_path = source / ".codex-plugin" / "plugin.json"
    if not manifest_path.is_file():
        raise FileNotFoundError(f"missing plugin manifest: {manifest_path}")
    if not (source / "skills").is_dir():
        raise FileNotFoundError(f"missing skills directory: {source / 'skills'}")

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if not isinstance(manifest, dict):
        raise ValueError(f"{manifest_path} must contain a JSON object")
    if manifest.get("name") != PLUGIN_NAME:
        raise ValueError(
            f"{manifest_path} must declare plugin name {PLUGIN_NAME!r}"
        )


def _copy_allowlist(source: Path, temporary: Path) -> tuple[str, ...]:
    copied: list[str] = []
    for name in DIRECTORY_ALLOWLIST:
        shutil.copytree(source / name, temporary / name)
        copied.append(name)
    for name in FILE_ALLOWLIST:
        source_file = source / name
        if source_file.is_file():
            shutil.copy2(source_file, temporary / name)
            copied.append(name)
    return tuple(copied)


def stage_plugin(source: Path, destination: Path) -> tuple[str, ...]:
    """Replace destination with a validated allowlisted copy of source."""
    source = source.expanduser().resolve()
    destination = destination.expanduser().resolve()
    _validate_paths(source, destination)
    _validate_source(source)

    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary = Path(
        tempfile.mkdtemp(prefix=f".{PLUGIN_NAME}-stage-", dir=destination.parent)
    )
    backup = destination.with_name(f".{PLUGIN_NAME}-backup-{uuid4().hex}")
    destination_moved = False

    try:
        copied = _copy_allowlist(source, temporary)
        if destination.exists():
            destination.replace(backup)
            destination_moved = True
        temporary.replace(destination)
    except Exception:
        if destination_moved and not destination.exists() and backup.exists():
            backup.replace(destination)
        raise
    finally:
        if temporary.exists():
            shutil.rmtree(temporary)

    if backup.exists():
        shutil.rmtree(backup)
    return copied


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create an installable staging copy of Prosa Viva."
    )
    parser.add_argument(
        "--source",
        type=Path,
        default=DEFAULT_SOURCE,
        help="Plugin checkout root (defaults to this repository).",
    )
    parser.add_argument(
        "--destination",
        type=Path,
        default=DEFAULT_DESTINATION,
        help="Staging directory (defaults to ~/plugins/prosa-viva).",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    copied = stage_plugin(args.source, args.destination)
    print(f"Source: {args.source.expanduser().resolve()}")
    print(f"Destination: {args.destination.expanduser().resolve()}")
    print("Copied: " + ", ".join(copied))


if __name__ == "__main__":
    main()
