from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent

spec = importlib.util.spec_from_file_location("validate", REPO_ROOT / "tools" / "validate.py")
validate = importlib.util.module_from_spec(spec)
sys.modules["validate"] = validate
spec.loader.exec_module(validate)


@pytest.fixture
def repo(tmp_path: Path) -> Path:
    skill = tmp_path / validate.SKILL_PATH
    skill.parent.mkdir(parents=True)
    skill.write_text("---\nname: x\nversion: 0.0.1\n---\n\nBody\n", encoding="utf-8")
    (tmp_path / validate.CHANGELOG_PATH).write_text(
        "# Changelog\n\n## [Unreleased]\n\n## [0.0.1] - 2026-11-08\n", encoding="utf-8"
    )
    for folder in validate.SAMPLE_FOLDERS:
        path = tmp_path / "samples" / folder
        path.mkdir(parents=True)
        (path / "README.md").write_text("# Register\n", encoding="utf-8")
    return tmp_path


def test_valid_repo_passes(repo: Path) -> None:
    assert validate.validate(repo) == []


def test_this_repository_passes() -> None:
    assert validate.validate(REPO_ROOT) == []


def test_there_are_eleven_sample_folders() -> None:
    assert len(validate.SAMPLE_FOLDERS) == 11


def test_missing_skill(repo: Path) -> None:
    (repo / validate.SKILL_PATH).unlink()
    assert any("SKILL.md is missing" in e for e in validate.validate(repo))


def test_skill_at_size_limit_fails(repo: Path) -> None:
    skill = repo / validate.SKILL_PATH
    header = "---\nversion: 0.0.1\n---\n"
    skill.write_text(header + "x" * (validate.MAX_SKILL_BYTES - len(header)), encoding="utf-8")
    assert any("must be under" in e for e in validate.validate(repo))


def test_version_mismatch(repo: Path) -> None:
    (repo / validate.SKILL_PATH).write_text("---\nversion: 0.0.2\n---\n", encoding="utf-8")
    assert any("does not match" in e for e in validate.validate(repo))


def test_version_outside_frontmatter_is_ignored(repo: Path) -> None:
    (repo / validate.SKILL_PATH).write_text("---\nname: x\n---\nversion: 0.0.1\n", encoding="utf-8")
    assert any("no version" in e for e in validate.validate(repo))


def test_unreleased_entry_is_not_a_release() -> None:
    assert validate.top_released_version("## [Unreleased]\n\n## [1.2.3] - 2026-01-01\n") == "1.2.3"


def test_changelog_without_release(repo: Path) -> None:
    (repo / validate.CHANGELOG_PATH).write_text("## [Unreleased]\n", encoding="utf-8")
    assert any("no released version" in e for e in validate.validate(repo))


def test_missing_sample_folder(repo: Path) -> None:
    (repo / "samples/en/chat/README.md").unlink()
    (repo / "samples/en/chat").rmdir()
    assert any("samples/en/chat is missing" in e for e in validate.validate(repo))


def test_missing_sample_readme(repo: Path) -> None:
    (repo / "samples/id/email/README.md").unlink()
    assert any("samples/id/email/README.md" in e for e in validate.validate(repo))


def write_reference(repo: Path, name: str, text: str) -> Path:
    path = repo / validate.REFERENCES_PATH / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


@pytest.mark.parametrize(
    ("version", "released", "has_unreleased", "allowed"),
    [
        ("0.0.1", "0.0.1", False, True),
        ("0.1.0-alpha.1", "0.0.1", True, True),
        ("0.1.0-alpha.1", "0.0.1", False, False),
        ("0.0.1-alpha.1", "0.0.1", True, False),
        ("0.0.2", "0.0.1", True, False),
        ("banana-1", "0.0.1", True, False),
    ],
)
def test_version_rule(version: str, released: str, has_unreleased: bool, allowed: bool) -> None:
    assert validate.version_allowed(version, released, has_unreleased) is allowed


def test_reference_at_size_limit_fails(repo: Path) -> None:
    write_reference(repo, "big.md", "x" * validate.MAX_REFERENCE_BYTES)
    assert any("must be under" in e for e in validate.validate(repo))


def test_nested_reference_is_size_checked(repo: Path) -> None:
    write_reference(repo, "presets/big.md", "x" * validate.MAX_REFERENCE_BYTES)
    assert any("big.md" in e for e in validate.validate(repo))


@pytest.mark.parametrize("name", ["id formal", "EN chat", "id, email", "en-semiformal"])
def test_preset_name_in_rule_fails(repo: Path, name: str) -> None:
    write_reference(repo, "patterns-id.md", f"# Title\n\nFor {name} do this.\n")
    assert any("names a preset" in e for e in validate.validate(repo))


def test_invalid_language_register_pair_is_allowed(repo: Path) -> None:
    write_reference(repo, "patterns-id.md", "# Title\n\nThe id chat combination.\n")
    assert validate.validate(repo) == []


def test_preset_name_allowed_in_preset_section(repo: Path) -> None:
    text = "# T\n\n## Presets\n\nid formal\n\n### Sub\n\nen chat\n\n## Other\n\nPlain.\n"
    write_reference(repo, "patterns-en.md", text)
    assert validate.validate(repo) == []


def test_preset_exemption_ends_with_section(repo: Path) -> None:
    text = "# T\n\n## Presets\n\nid formal\n\n## Rules\n\nen chat\n"
    write_reference(repo, "patterns-en.md", text)
    errors = validate.validate(repo)
    assert len(errors) == 1 and ":9 " in errors[0]


def test_preset_check_ignores_other_references(repo: Path) -> None:
    write_reference(repo, "locking.md", "Example for id formal.\n")
    assert validate.validate(repo) == []


def test_broken_link_fails(repo: Path) -> None:
    write_reference(repo, "a.md", "See [b](missing.md).\n")
    assert any("broken link missing.md" in e for e in validate.validate(repo))


def test_valid_links_pass(repo: Path) -> None:
    write_reference(repo, "b.md", "# B\n")
    text = "[b](b.md) [anchor](b.md#x) [top](#t) [web](https://example.org/nope.md)\n"
    write_reference(repo, "a.md", text)
    assert validate.validate(repo) == []


def test_links_in_code_are_ignored(repo: Path) -> None:
    write_reference(repo, "a.md", "`[x](no.md)`\n\n```text\n[y](no.md)\n```\n")
    assert validate.validate(repo) == []


@pytest.mark.parametrize(
    "intro", ["Ada tiga aturan:", "Three things:", "**Tiga hal:**", "Follow these three steps:"]
)
def test_count_match_passes(repo: Path, intro: str) -> None:
    write_reference(repo, "a.md", f"{intro}\n\n- a\n- b\n- c\n")
    assert validate.validate(repo) == []


@pytest.mark.parametrize("intro", ["Ada lima hal:", "Five things:", "Sepuluh butir:"])
def test_count_mismatch_fails(repo: Path, intro: str) -> None:
    write_reference(repo, "a.md", f"{intro}\n\n- a\n- b\n- c\n")
    assert any("but the list has 3" in e for e in validate.validate(repo))


def test_count_ignores_nested_items(repo: Path) -> None:
    write_reference(repo, "a.md", "Two things:\n\n1. a\n   - x\n   - y\n\n   more\n2. b\n")
    assert validate.validate(repo) == []


def test_count_stops_at_following_paragraph(repo: Path) -> None:
    write_reference(repo, "a.md", "Two things:\n\n- a\n- b\n\nAfter.\n\n- c\n")
    assert validate.validate(repo) == []


@pytest.mark.parametrize(
    "intro",
    ["Choose one of these:", "Pilih salah satu berikut:", "Two or three items:", "Three things"],
)
def test_non_counts_are_ignored(repo: Path, intro: str) -> None:
    write_reference(repo, "a.md", f"{intro}\n\n- a\n- b\n- c\n- d\n")
    assert validate.validate(repo) == []


def test_count_without_list_is_ignored(repo: Path) -> None:
    write_reference(repo, "a.md", "Three things:\n\nJust prose.\n")
    assert validate.validate(repo) == []


def write_sample(repo: Path, relative: str, **changes: str) -> Path:
    language, register, folder, name = relative.split("/")
    kind = "good" if folder == "good" else "pair"
    fields = {
        "id": f"{language}-{register}-{kind}-001",
        "kind": kind,
        "source": "Example",
        "source_url": "",
        "license": "original",
        "synthetic": "false",
        "domain": "umum",
        "notes": "Note",
        **changes,
    }
    frontmatter = "".join(f"{key}: {value}\n" for key, value in fields.items() if value != "DROP")
    sections = {"id": "## Sebelum\n\n## Sesudah\n\n## Catatan\n"}.get(
        language, "## Before\n\n## After\n\n## Notes\n"
    )
    path = repo / "samples" / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"---\n{frontmatter}---\n\n{sections}", encoding="utf-8")
    return path


@pytest.mark.parametrize("relative", ["id/formal/good/a.md", "en/chat/pairs/a.md"])
def test_valid_sample_passes(repo: Path, relative: str) -> None:
    write_sample(repo, relative)
    assert validate.validate(repo) == []


def test_synthetic_sample_passes(repo: Path) -> None:
    write_sample(repo, "id/email/pairs/a.md", license="synthetic", synthetic="true")
    assert validate.validate(repo) == []


def test_gitkeep_is_not_a_sample(repo: Path) -> None:
    path = repo / "samples/id/formal/good/.gitkeep"
    path.parent.mkdir(parents=True)
    path.touch()
    assert validate.validate(repo) == []


def test_sample_without_frontmatter(repo: Path) -> None:
    path = repo / "samples/id/formal/good/a.md"
    path.parent.mkdir(parents=True)
    path.write_text("No frontmatter\n", encoding="utf-8")
    assert any("has no frontmatter" in e for e in validate.validate(repo))


def test_sample_missing_field(repo: Path) -> None:
    write_sample(repo, "id/formal/good/a.md", domain="DROP")
    assert any("missing frontmatter fields: domain" in e for e in validate.validate(repo))


@pytest.mark.parametrize(
    ("changes", "message"),
    [
        ({"kind": "pair"}, "folder expects good"),
        ({"license": "MIT"}, "invalid license"),
        ({"domain": "hukum"}, "invalid domain"),
        ({"synthetic": "maybe"}, "invalid synthetic"),
        ({"synthetic": "true"}, "exactly when"),
        ({"license": "synthetic"}, "exactly when"),
        ({"id": "id-formal-001"}, "expected id-formal-good-NNN"),
        ({"id": "id-email-good-001"}, "expected id-formal-good-NNN"),
        ({"id": "id-formal-pair-001"}, "expected id-formal-good-NNN"),
    ],
)
def test_invalid_sample_fields(repo: Path, changes: dict[str, str], message: str) -> None:
    write_sample(repo, "id/formal/good/a.md", **changes)
    assert any(message in e for e in validate.validate(repo))


def test_duplicate_sample_id(repo: Path) -> None:
    write_sample(repo, "id/formal/good/a.md")
    write_sample(repo, "id/formal/good/b.md")
    assert any("repeats id" in e for e in validate.validate(repo))


@pytest.mark.parametrize(
    ("relative", "section"),
    [("id/formal/pairs/a.md", "Sesudah"), ("en/email/pairs/a.md", "Notes")],
)
def test_pair_missing_section(repo: Path, relative: str, section: str) -> None:
    path = write_sample(repo, relative)
    path.write_text(path.read_text(encoding="utf-8").replace(f"## {section}\n", ""), "utf-8")
    assert any(f"missing section {section}" in e for e in validate.validate(repo))


def write_preset(repo: Path, name: str, status: str, sections: tuple[str, ...]) -> Path:
    body = "".join(f"## {section}\n\nText.\n\n" for section in sections)
    text = f"---\nname: x\nstatus: {status}\nmetrics:\n  a: {{median: 1}}\n---\n\n{body}"
    return write_reference(repo, f"presets/{name}", text)


@pytest.mark.parametrize("language", ["id", "en"])
def test_ready_preset_passes(repo: Path, language: str) -> None:
    write_preset(repo, f"{language}-formal.md", "ready", validate.PRESET_SECTIONS[language])
    assert validate.validate(repo) == []


def test_stub_preset_needs_no_sections(repo: Path) -> None:
    write_preset(repo, "id-formal.md", "stub", ())
    assert validate.validate(repo) == []


def test_preset_missing_section(repo: Path) -> None:
    write_preset(repo, "id-formal.md", "ready", validate.PRESET_SECTIONS["id"][:-1])
    assert any("sections in order" in e for e in validate.validate(repo))


def test_preset_sections_out_of_order(repo: Path) -> None:
    sections = tuple(reversed(validate.PRESET_SECTIONS["en"]))
    write_preset(repo, "en-chat.md", "ready", sections)
    assert any("sections in order" in e for e in validate.validate(repo))


def test_preset_uses_sections_of_its_language(repo: Path) -> None:
    write_preset(repo, "en-chat.md", "ready", validate.PRESET_SECTIONS["id"])
    assert any("sections in order" in e for e in validate.validate(repo))


def test_preset_invalid_status(repo: Path) -> None:
    write_preset(repo, "id-formal.md", "draft", ())
    assert any("invalid status" in e for e in validate.validate(repo))


def test_preset_without_metrics(repo: Path) -> None:
    write_reference(repo, "presets/id-formal.md", "---\nname: x\nstatus: stub\n---\n\nX\n")
    assert any("no metrics block" in e for e in validate.validate(repo))


def test_preset_without_frontmatter(repo: Path) -> None:
    write_reference(repo, "presets/id-formal.md", "No frontmatter\n")
    assert any("has no frontmatter" in e for e in validate.validate(repo))


def test_preset_at_size_limit_fails(repo: Path) -> None:
    path = write_preset(repo, "id-formal.md", "stub", ())
    path.write_text(path.read_text("utf-8") + "x" * validate.MAX_PRESET_BYTES, "utf-8")
    assert any("must be under 6144" in e for e in validate.validate(repo))


def test_main_exit_codes(repo: Path) -> None:
    assert validate.main(["--root", str(repo)]) == 0
    (repo / validate.SKILL_PATH).unlink()
    assert validate.main(["--root", str(repo)]) == 1
