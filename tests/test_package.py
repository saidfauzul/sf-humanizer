from __future__ import annotations

import importlib.util
import sys
import zipfile
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent

sys.path.insert(0, str(REPO_ROOT / "tools"))
spec = importlib.util.spec_from_file_location("package", REPO_ROOT / "tools" / "package.py")
package = importlib.util.module_from_spec(spec)
sys.modules["package"] = package
spec.loader.exec_module(package)

CHANGELOG = "# Changelog\n\n## [Unreleased]\n\n## [0.0.1] - 2026-11-08\n\n### Added\n\n- First.\n"


@pytest.fixture
def root(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    skill = tmp_path / "skill" / "sf-humanizer"
    (skill / "references").mkdir(parents=True)
    (skill / "scripts" / "__pycache__").mkdir(parents=True)
    (skill / "SKILL.md").write_text("---\nversion: 0.1.0-alpha.3\n---\n\nBody\n", "utf-8")
    (skill / "references" / "a.md").write_text("A\n", "utf-8")
    (skill / "references" / ".gitkeep").touch()
    (skill / "references" / ".DS_Store").touch()
    (skill / "scripts" / "metrics.py").write_text("x = 1\n", "utf-8")
    (skill / "scripts" / "__pycache__" / "metrics.pyc").touch()
    (tmp_path / "CHANGELOG.md").write_text(CHANGELOG, "utf-8")
    monkeypatch.setattr(package, "run_checks", lambda _: [])
    return tmp_path


def names(path: Path) -> list[str]:
    with zipfile.ZipFile(path) as archive:
        return sorted(archive.namelist())


def test_zip_has_skill_at_root_and_excludes_junk(root: Path) -> None:
    output = package.package(root)
    assert output.name == "sf-humanizer-0.1.0-alpha.3.zip"
    assert names(output) == [
        "sf-humanizer/SKILL.md",
        "sf-humanizer/references/a.md",
        "sf-humanizer/scripts/metrics.py",
    ]


def test_refuses_when_changelog_is_newer(root: Path) -> None:
    text = CHANGELOG.replace("0.0.1", "0.1.0")
    (root / "CHANGELOG.md").write_text(text, "utf-8")
    with pytest.raises(package.PackageError, match="newer"):
        package.package(root)


def test_prerelease_sorts_before_release() -> None:
    assert package.version_key("0.1.0-alpha.3") < package.version_key("0.1.0")
    assert package.version_key("0.0.1") < package.version_key("0.1.0-alpha.3")


def test_refuses_failed_checks(root: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(package, "run_checks", lambda _: ["broken"])
    with pytest.raises(package.PackageError, match="broken"):
        package.package(root)


def test_refuses_wrong_tag(root: Path) -> None:
    with pytest.raises(package.PackageError, match="does not match"):
        package.package(root, "v9.9.9")
    assert package.package(root, "v0.1.0-alpha.3").is_file()


def test_main_exit_codes(root: Path) -> None:
    assert package.main(["--root", str(root)]) == 0
    assert package.main(["--root", str(root), "--tag", "v1.0.0"]) == 1


def test_release_notes(root: Path) -> None:
    assert "First." in package.release_notes(root, "0.0.1")
    assert "See CHANGELOG" in package.release_notes(root, "9.9.9")
