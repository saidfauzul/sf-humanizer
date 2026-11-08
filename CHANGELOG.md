# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

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

- `SKILL.md` may carry a pre-release version newer than the top released changelog entry.
- Sample ids now use `<lang>-<register>-<good|pair>-NNN`.
- CI uses `actions/checkout@v5` and runs on `ubuntu-24.04`.

## [0.0.1] - 2026-11-08

### Added

- Repository foundation: documentation, community files and CI.
- Skill skeleton in `skill/sf-humanizer/`.
- Sample folders for 5 Indonesian and 6 English registers.
- `tools/validate.py` repository structure checker with tests.
