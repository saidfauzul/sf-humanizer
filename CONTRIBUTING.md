# Contributing

Thanks for helping improve sf-humanizer. Code, comments and commit messages are in English. Samples are written in the language of their folder.

## Adding samples

Samples live in `samples/<language>/<register>/`:

- `good/` holds good human writing (`kind: good`).
- `pairs/` holds before-and-after rewrites (`kind: pair`).

Each sample is a Markdown file with YAML frontmatter:

```yaml
---
id: id-formal-good-001
kind: good            # good | pair
source: Peraturan contoh
source_url: https://example.org/doc
license: public-domain # public-domain | OGL-3.0 | CC-BY-4.0 | original | synthetic
synthetic: false
domain: pengadaan     # pengadaan | tata-kelola | sop | nota-dinas | surel | umum
notes: Short context for reviewers.
---
```

| Field | Description |
| --- | --- |
| `id` | Unique ID: `<language>-<register>-<good\|pair>-NNN`, matching the sample's folder |
| `kind` | `good` or `pair` |
| `source` | Name of the source document or author |
| `source_url` | Link to the source; leave empty if there is none |
| `license` | `public-domain`, `OGL-3.0`, `CC-BY-4.0`, `original` or `synthetic` |
| `synthetic` | `true` if the text was generated or invented |
| `domain` | `pengadaan`, `tata-kelola`, `sop`, `nota-dinas`, `surel` or `umum` |
| `notes` | Anything reviewers should know |

Pair files also need three sections: `## Sebelum`, `## Sesudah` and `## Catatan` in Indonesian, or `## Before`, `## After` and `## Notes` in English. List the pattern IDs that were fixed in the last section, and say where each one was fixed. The before text should contain at least four distinct patterns, including at least two strong ones.

After adding or changing samples, run `python tools/build.py` and commit the regenerated files in `skill/sf-humanizer/references/examples/` and `references/presets/`. CI runs `python tools/build.py --check` and fails if they are out of date.

### Rules for samples

- Only submit text whose license is one of the values above, and that you are allowed to share.
- **Anonymize real documents.** Remove or replace names, phone numbers, email addresses, ID and contract numbers, company names and values that could identify a person, organization or procurement.
- Do not submit confidential, classified or restricted documents, even anonymized.
- Mark anything model-generated as `synthetic: true` with `license: synthetic`, and nothing else.
- Add attribution to [NOTICE.md](NOTICE.md) for third-party text (`OGL-3.0`, `CC-BY-4.0`).

## Branches and commits

Name branches with one of these prefixes: `feat/`, `fix/`, `docs/`, `samples/`.

Use [Conventional Commits](https://www.conventionalcommits.org/), for example:

```text
feat: add audit mode to the English formal preset
feat(samples): add three Indonesian nota dinas pairs
```

## Before opening a pull request

```bash
pip install ruff pytest
ruff check .
pytest
python tools/validate.py
python tools/build.py --check
```

Update [CHANGELOG.md](CHANGELOG.md) for user-visible changes. The `version` in `SKILL.md` must match the top released entry in the changelog, or be a pre-release (such as `0.1.0-alpha.1`) of a newer version while the changelog has an `Unreleased` section.

By contributing, you agree to follow the [Code of Conduct](CODE_OF_CONDUCT.md).
