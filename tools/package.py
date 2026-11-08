#!/usr/bin/env python3
"""Package the skill as a ZIP with sf-humanizer/ at the archive root. Standard library only."""

from __future__ import annotations

import argparse
import re
import sys
import zipfile
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
REPO = TOOLS.parent
sys.path.insert(0, str(TOOLS))

import build  # noqa: E402
import validate  # noqa: E402

SKILL_DIR = Path("skill/sf-humanizer")
EXCLUDED_NAMES = {".gitkeep", ".DS_Store"}
EXCLUDED_DIRS = {"__pycache__"}
VERSION_RE = re.compile(r"^(\d+)\.(\d+)\.(\d+)(?:-(.+))?$")


class PackageError(Exception):
    """Raised when the skill must not be packaged."""


def version_key(version: str) -> tuple:
    """Return a sort key in which a pre-release sorts before its release."""
    match = VERSION_RE.match(version)
    if match is None:
        raise PackageError(f"invalid version: {version}")
    core = tuple(int(part) for part in match.groups()[:3])
    return (*core, 0 if match.group(4) else 1, match.group(4) or "")


def skill_version(root: Path) -> str:
    version = validate.frontmatter_version((root / validate.SKILL_PATH).read_text(encoding="utf-8"))
    if version is None:
        raise PackageError("SKILL.md has no version")
    return version


def check_version(root: Path) -> str:
    """Return the skill version, refusing one older than the top released entry."""
    version = skill_version(root)
    changelog = (root / validate.CHANGELOG_PATH).read_text(encoding="utf-8")
    released = validate.top_released_version(changelog)
    if released is not None and version_key(released) > version_key(version):
        raise PackageError(f"CHANGELOG release {released} is newer than SKILL.md {version}")
    return version


def run_checks(root: Path) -> list[str]:
    """Return the problems reported by the validator and the build check."""
    errors = validate.validate(root)
    errors += [f"{path} is out of date" for path in build.stale_files(root, build.build(root))]
    return errors


def included_files(root: Path) -> list[Path]:
    """Return the skill files that belong in the archive."""
    base = root / SKILL_DIR
    return [
        path
        for path in sorted(base.rglob("*"))
        if path.is_file()
        and path.name not in EXCLUDED_NAMES
        and not EXCLUDED_DIRS.intersection(path.relative_to(base).parts)
    ]


def build_zip(root: Path, version: str) -> Path:
    output = root / "dist" / f"sf-humanizer-{version}.zip"
    output.parent.mkdir(parents=True, exist_ok=True)
    base = root / SKILL_DIR
    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as archive:
        for path in included_files(root):
            archive.write(path, Path("sf-humanizer") / path.relative_to(base))
    return output


def package(root: Path, tag: str | None = None) -> Path:
    """Run the checks and build the ZIP."""
    version = check_version(root)
    if tag is not None and tag != f"v{version}":
        raise PackageError(f"tag {tag} does not match SKILL.md version {version}")
    errors = run_checks(root)
    if errors:
        raise PackageError("; ".join(errors))
    return build_zip(root, version)


def release_notes(root: Path, version: str) -> str:
    """Return the CHANGELOG section for a version, or a pointer to the file."""
    text = (root / validate.CHANGELOG_PATH).read_text(encoding="utf-8")
    match = re.search(
        rf"^## \[{re.escape(version)}\][^\n]*\n(.*?)(?=^## \[|\Z)",
        text,
        re.MULTILINE | re.DOTALL,
    )
    if match and match.group(1).strip():
        return match.group(1).strip() + "\n"
    return "See CHANGELOG.md for the changes in this version.\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Package the skill as a ZIP.")
    parser.add_argument("--root", type=Path, default=REPO, help="repository root")
    parser.add_argument("--tag", help="release tag that must match the skill version")
    parser.add_argument("--notes", metavar="VERSION", help="print release notes and exit")
    args = parser.parse_args(argv)

    if args.notes:
        print(release_notes(args.root, args.notes), end="")
        return 0
    try:
        output = package(args.root, args.tag)
    except PackageError as error:
        print(f"error: {error}", file=sys.stderr)
        return 1
    print(output)
    return 0


if __name__ == "__main__":
    sys.exit(main())
