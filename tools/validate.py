#!/usr/bin/env python3
"""Validate the repository structure. Standard library only.

Version rule: SKILL.md either matches the newest released CHANGELOG entry, or is a
pre-release (such as 0.1.0-alpha.1) of a version newer than that entry while the
changelog has an Unreleased section. Pre-releases do not need their own entry.

Preset-name heuristic: generic rules must not name a preset. In SKILL.md and
patterns-*.md, a line must not contain a language followed by one of its registers
("id formal", "en, chat", "en-email"). Sections whose heading starts with "Preset"
are exempt, because that is where presets are defined.

Count heuristic: a non-list line ending in a colon that contains a number word from
one to ten (English or Indonesian) followed by another word, and that is immediately
followed by a list, must introduce exactly that many top-level items. Phrases such as
"one of", "salah satu" and "two or three" are not treated as counts.

Sample rule: every Markdown file in a register's good/ or pairs/ folder needs the
frontmatter fields from CONTRIBUTING.md. Its id must be unique and match its location
as <lang>-<register>-<good|pair>-NNN. A sample is synthetic exactly when its license
is synthetic. Pair files need the before, after and notes sections of their language.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

MAX_SKILL_BYTES = 20 * 1024
MAX_REFERENCE_BYTES = 15 * 1024
SKILL_PATH = Path("skill/sf-humanizer/SKILL.md")
REFERENCES_PATH = Path("skill/sf-humanizer/references")
CHANGELOG_PATH = Path("CHANGELOG.md")
REGISTERS = {
    "id": ("formal", "semiformal", "informal", "standar", "email"),
    "en": ("formal", "semiformal", "informal", "standard", "email", "chat"),
}
SAMPLE_FOLDERS = tuple(
    f"{language}/{register}" for language, registers in REGISTERS.items() for register in registers
)
NUMBER_WORDS = {
    **dict(
        zip(
            "one two three four five six seven eight nine ten".split(),
            range(1, 11),
        )
    ),
    **dict(
        zip(
            "satu dua tiga empat lima enam tujuh delapan sembilan sepuluh".split(),
            range(1, 11),
        )
    ),
}

SAMPLE_FIELDS = ("id", "kind", "source", "source_url", "license", "synthetic", "domain", "notes")
SAMPLE_LICENSES = ("public-domain", "OGL-3.0", "CC-BY-4.0", "original", "synthetic")
SAMPLE_DOMAINS = ("pengadaan", "tata-kelola", "sop", "nota-dinas", "surel", "umum")
SAMPLE_KINDS = {"good": "good", "pairs": "pair"}
PAIR_SECTIONS = {"id": ("Sebelum", "Sesudah", "Catatan"), "en": ("Before", "After", "Notes")}

FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\s*(?:\r?\n|\Z)", re.DOTALL)
VERSION_RE = re.compile(r"^version:\s*[\"']?([^\s\"']+)[\"']?\s*$", re.MULTILINE)
RELEASE_RE = re.compile(r"^## \[(?!Unreleased\])([^\]]+)\]", re.MULTILINE | re.IGNORECASE)
UNRELEASED_RE = re.compile(r"^## \[Unreleased\]", re.MULTILINE | re.IGNORECASE)
CORE_VERSION_RE = re.compile(r"^(\d+)\.(\d+)\.(\d+)(-.+)?$")
FENCE_RE = re.compile(r"^\s*(```|~~~)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")
PRESET_HEADING_RE = re.compile(r"^presets?\b", re.IGNORECASE)
PRESET_NAME_RE = re.compile(
    "|".join(
        rf"\b{language}[\s,-]+(?:{'|'.join(registers)})\b"
        for language, registers in REGISTERS.items()
    ),
    re.IGNORECASE,
)
INLINE_CODE_RE = re.compile(r"`[^`]*`")
LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)[^)]*\)")
URL_SCHEME_RE = re.compile(r"^[a-z][a-z0-9+.-]*:", re.IGNORECASE)
LIST_ITEM_RE = re.compile(r"^(\s*)(?:[-*+]|\d+[.)])\s+")
COUNT_RE = re.compile(
    r"(?<![\w-])(?<!salah )(?<!or )(?<!atau )(" + "|".join(NUMBER_WORDS) + r")\s+"
    r"(?!(?:of|dari|or|atau|per|to|sampai|hingga|more|lebih)\b)[^\W\d_]",
    re.IGNORECASE,
)


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


def version_allowed(version: str, released: str, has_unreleased: bool) -> bool:
    """Apply the version rule described in the module docstring."""
    if version == released:
        return True
    candidate = CORE_VERSION_RE.match(version)
    base = CORE_VERSION_RE.match(released)
    if candidate is None or base is None or candidate.group(4) is None or not has_unreleased:
        return False
    return tuple(map(int, candidate.groups()[:3])) > tuple(map(int, base.groups()[:3]))


def check_skill(root: Path) -> list[str]:
    """Check SKILL.md size and that its version agrees with the changelog."""
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

    text = changelog.read_text(encoding="utf-8")
    released = top_released_version(text)
    if released is None:
        errors.append(f"{CHANGELOG_PATH} has no released version")
    elif version is not None and not version_allowed(
        version, released, UNRELEASED_RE.search(text) is not None
    ):
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


def reference_files(root: Path) -> list[Path]:
    """Return the Markdown files under the skill's references directory."""
    return sorted((root / REFERENCES_PATH).rglob("*.md"))


def without_fences(text: str) -> list[str]:
    """Return the lines of text, with fenced code blocks blanked out."""
    lines = []
    in_fence = False
    for line in text.splitlines():
        if FENCE_RE.match(line):
            in_fence = not in_fence
            lines.append("")
        else:
            lines.append("" if in_fence else line)
    return lines


def check_reference_sizes(root: Path) -> list[str]:
    """Check that every reference file is under the size limit."""
    errors = []
    for path in reference_files(root):
        size = path.stat().st_size
        if size >= MAX_REFERENCE_BYTES:
            relative = path.relative_to(root)
            errors.append(f"{relative} is {size} bytes; it must be under {MAX_REFERENCE_BYTES}")
    return errors


def check_preset_names(root: Path) -> list[str]:
    """Check that generic rules do not name a preset."""
    errors = []
    paths = [root / SKILL_PATH, *sorted((root / REFERENCES_PATH).glob("patterns-*.md"))]
    for path in paths:
        if not path.is_file():
            continue
        exempt_level = None
        for number, line in enumerate(without_fences(path.read_text(encoding="utf-8")), start=1):
            heading = HEADING_RE.match(line)
            if heading:
                level = len(heading.group(1))
                if exempt_level is not None and level <= exempt_level:
                    exempt_level = None
                if exempt_level is None and PRESET_HEADING_RE.match(heading.group(2)):
                    exempt_level = level
            if exempt_level is None and PRESET_NAME_RE.search(line):
                errors.append(f"{path.relative_to(root)}:{number} names a preset in a generic rule")
    return errors


def check_links(root: Path) -> list[str]:
    """Check that relative links in the skill's Markdown files resolve."""
    errors = []
    skill = root / SKILL_PATH
    paths = ([skill] if skill.is_file() else []) + reference_files(root)
    for path in paths:
        for number, line in enumerate(without_fences(path.read_text(encoding="utf-8")), start=1):
            for target in LINK_RE.findall(INLINE_CODE_RE.sub("", line)):
                if URL_SCHEME_RE.match(target) or target.startswith("#"):
                    continue
                if not (path.parent / target.split("#")[0]).exists():
                    errors.append(f"{path.relative_to(root)}:{number} has broken link {target}")
    return errors


def count_list_items(lines: list[str], start: int) -> int:
    """Count top-level list items from start; return 0 if no list begins there."""
    count = 0
    indent = None
    for line in lines[start:]:
        if not line.strip():
            continue
        item = LIST_ITEM_RE.match(line)
        if item:
            width = len(item.group(1))
            if indent is None:
                indent = width
            if width < indent:
                break
            if width == indent:
                count += 1
        elif indent is None or len(line) - len(line.lstrip()) <= indent:
            break
    return count


def check_counts(root: Path) -> list[str]:
    """Check that stated counts match the lists they introduce."""
    errors = []
    skill = root / SKILL_PATH
    paths = ([skill] if skill.is_file() else []) + reference_files(root)
    for path in paths:
        lines = without_fences(path.read_text(encoding="utf-8"))
        for index, line in enumerate(lines):
            if LIST_ITEM_RE.match(line) or not line.rstrip().rstrip("*_").endswith(":"):
                continue
            stated = COUNT_RE.search(line)
            if stated is None:
                continue
            found = count_list_items(lines, index + 1)
            expected = NUMBER_WORDS[stated.group(1).lower()]
            if found and found != expected:
                errors.append(
                    f"{path.relative_to(root)}:{index + 1} states {expected} items "
                    f"but the list has {found}"
                )
    return errors


def parse_frontmatter(text: str) -> dict[str, str] | None:
    """Return simple key-value frontmatter, or None if the text has none."""
    frontmatter = FRONTMATTER_RE.match(text)
    if frontmatter is None:
        return None
    fields = {}
    for line in frontmatter.group(1).splitlines():
        key, separator, value = line.partition(":")
        if separator:
            fields[key.strip()] = value.strip().strip("\"'")
    return fields


def check_sample_file(path: Path, language: str, register: str, kind: str) -> list[str]:
    """Check one sample file against the sample rule."""
    text = path.read_text(encoding="utf-8")
    fields = parse_frontmatter(text)
    if fields is None:
        return ["has no frontmatter"]

    missing = [field for field in SAMPLE_FIELDS if field not in fields]
    if missing:
        return [f"is missing frontmatter fields: {', '.join(missing)}"]

    errors = []
    if fields["kind"] != kind:
        errors.append(f"has kind {fields['kind']} but its folder expects {kind}")
    if fields["license"] not in SAMPLE_LICENSES:
        errors.append(f"has invalid license {fields['license']}")
    if fields["domain"] not in SAMPLE_DOMAINS:
        errors.append(f"has invalid domain {fields['domain']}")
    if fields["synthetic"] not in ("true", "false"):
        errors.append(f"has invalid synthetic value {fields['synthetic']}")
    elif (fields["synthetic"] == "true") != (fields["license"] == "synthetic"):
        errors.append("must be synthetic exactly when its license is synthetic")
    if not re.fullmatch(rf"{language}-{register}-{kind}-\d{{3}}", fields["id"]):
        errors.append(f"has id {fields['id']}; expected {language}-{register}-{kind}-NNN")
    if kind == "pair":
        for section in PAIR_SECTIONS[language]:
            if not re.search(rf"^##\s+{section}\s*$", text, re.MULTILINE):
                errors.append(f"is missing section {section}")
    return errors


def check_sample_files(root: Path) -> list[str]:
    """Check the frontmatter, ids and sections of every sample."""
    errors = []
    seen: dict[str, Path] = {}
    for folder in SAMPLE_FOLDERS:
        language, register = folder.split("/")
        for subfolder, kind in SAMPLE_KINDS.items():
            for path in sorted((root / "samples" / folder / subfolder).glob("*.md")):
                relative = path.relative_to(root)
                errors += [
                    f"{relative} {error}"
                    for error in check_sample_file(path, language, register, kind)
                ]
                sample_id = (parse_frontmatter(path.read_text(encoding="utf-8")) or {}).get("id")
                if sample_id in seen:
                    errors.append(f"{relative} repeats id {sample_id} from {seen[sample_id]}")
                elif sample_id:
                    seen[sample_id] = relative
    return errors


def validate(root: Path) -> list[str]:
    """Run all checks and return the error messages."""
    return (
        check_skill(root)
        + check_samples(root)
        + check_sample_files(root)
        + check_reference_sizes(root)
        + check_preset_names(root)
        + check_links(root)
        + check_counts(root)
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate the repository structure.",
    )
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
