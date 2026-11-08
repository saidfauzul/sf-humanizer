#!/usr/bin/env python3
"""Validate the repository structure. Standard library only."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

MAX_SKILL_BYTES = 20 * 1024
SKILL_PATH = Path("skill/sf-humanizer/SKILL.md")
CHANGELOG_PATH = Path("CHANGELOG.md")
SAMPLE_FOLDERS = tuple(
    f"id/{register}" for register in ("formal", "semiformal", "informal", "standar", "email")
) + tuple(
    f"en/{register}"
    for register in ("formal", "semiformal", "informal", "standard", "email", "chat")
)

FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\s*(?:\r?\n|\Z)", re.DOTALL)
VERSION_RE = re.compile(r"^version:\s*[\"']?([^\s\"']+)[\"']?\s*$", re.MULTILINE)
RELEASE_RE = re.compile(r"^## \[(?!Unreleased\])([^\]]+)\]", re.MULTILINE | re.IGNORECASE)


def frontmatter_version(text: str) -> str | None:
    """Return the version declared in YAML frontmatter, if any."""
    frontmatter = FRONTMATTER_RE.match(text)
    if frontmatter is None:
        return None
    version = VERSION_RE.search(frontmatter.group(1))
    return version.group(1) if version else None


def top_released_version(text: str) -> str | None:
    """Return the newest released version in a Keep a Changelog file."""
    release = RELEASE_RE.search(text)
    return release.group(1) if release else None


def check_skill(root: Path) -> list[str]:
    """Check SKILL.md size and that its version matches the changelog."""
    skill = root / SKILL_PATH
    if not skill.is_file():
        return [f"{SKILL_PATH} is missing"]

    errors = []
    size = skill.stat().st_size
    if size >= MAX_SKILL_BYTES:
        errors.append(f"{SKILL_PATH} is {size} bytes; it must be under {MAX_SKILL_BYTES}")

    version = frontmatter_version(skill.read_text(encoding="utf-8"))
    if version is None:
        errors.append(f"{SKILL_PATH} has no version in its frontmatter")

    changelog = root / CHANGELOG_PATH
    if not changelog.is_file():
        errors.append(f"{CHANGELOG_PATH} is missing")
        return errors

    released = top_released_version(changelog.read_text(encoding="utf-8"))
    if released is None:
        errors.append(f"{CHANGELOG_PATH} has no released version")
    elif version is not None and version != released:
        errors.append(
            f"{SKILL_PATH} version {version} does not match {CHANGELOG_PATH} version {released}"
        )
    return errors


def check_samples(root: Path) -> list[str]:
    """Check that every register folder exists and has a README."""
    errors = []
    for folder in SAMPLE_FOLDERS:
        path = Path("samples") / folder
        if not (root / path).is_dir():
            errors.append(f"{path} is missing")
        elif not (root / path / "README.md").is_file():
            errors.append(f"{path}/README.md is missing")
    return errors


def validate(root: Path) -> list[str]:
    """Run all checks and return the error messages."""
    return check_skill(root) + check_samples(root)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parent.parent,
        help="repository root (default: this repository)",
    )
    args = parser.parse_args(argv)

    errors = validate(args.root)
    for error in errors:
        print(f"error: {error}", file=sys.stderr)
    if errors:
        return 1
    print("validate: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
