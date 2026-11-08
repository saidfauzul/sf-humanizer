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


def test_main_exit_codes(repo: Path) -> None:
    assert validate.main(["--root", str(repo)]) == 0
    (repo / validate.SKILL_PATH).unlink()
    assert validate.main(["--root", str(repo)]) == 1
