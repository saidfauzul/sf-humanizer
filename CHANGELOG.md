# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

Version `0.1.0-alpha.2` was folded into `0.1.0-alpha.3`, because Tahap 2 did not bump the version.

### Added

- `scripts/metrics.py`: sentence, pattern and count metrics, `--compare` and `--check-locked`.
- `tools/build.py`: generated examples and preset metric profiles, with a `--check` mode used by CI.
- Acceptance inputs and run evidence in `tests/manual/`, a test report, and a manual test guide for claude.ai.
- Full presets for all 11 registers, and validator checks for preset files.
- `tools/package.py` and a release workflow that attaches the ZIP to a GitHub Release.
- Skill core in `SKILL.md`: invocation, presets, modes, workflow and core rules.
- Indonesian and English pattern catalogs.
- Locking rules and Indonesian and English glossaries.
- Validator checks for reference size, preset names in generic rules, internal links and stated counts.
- Wave 1 corpus: 24 synthetic samples for three presets, pending owner review.
- Wave 2 corpus: 64 synthetic samples for the remaining eight presets, pending owner review.
- Quality review of all 88 samples, recorded in `docs/review-samples-2026-11-08.md`.
- `docs/sources.md`, `docs/synthetic-prompts.md` and `docs/PLAN.md`.
- Sample validation for frontmatter, ids and pair sections.

### Changed

- Audit score bands calibrated on synthetic samples: low below 3, medium 3 to 6, high above 6.
- `SKILL.md` may carry a pre-release version newer than the top released changelog entry.
- Sample ids now use `<lang>-<register>-<good|pair>-NNN`.
- CI uses `actions/checkout@v5` and runs on `ubuntu-24.04`.

### Fixed

- `scripts/metrics.py` and `tools/validate.py` now read a count from any line ending in a colon, such as "three documents", and ignore numbers in dates, times, amounts and references.
- Core rules and the en-chat preset now say to rewrite, not remove, a line that a later turn responds to.
- Core rules and patterns ID-03 and EN-04 now state when a generic opener or closer may be removed.
- `scripts/metrics.py` now locks English dates in October.

## [0.0.1] - 2026-11-08

### Added

- Repository foundation: documentation, community files and CI.
- Skill skeleton in `skill/sf-humanizer/`.
- Sample folders for 5 Indonesian and 6 English registers.
- `tools/validate.py` repository structure checker with tests.
