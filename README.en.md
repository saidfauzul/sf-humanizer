# sf-humanizer

**English** · [Bahasa Indonesia](README.md)

> **Status: pre-alpha.** The skill is still a skeleton; its behavior and preset structure may change.

sf-humanizer is a Claude skill that rewrites AI-sounding text so it reads as human-written, keeping the facts unchanged. It supports Indonesian and English.

## Usage

```text
sf-humanizer preset <bahasa>, <register> [mode cepat|lengkap|audit]
```

Example: `sf-humanizer preset en, formal mode lengkap`

| Mode | Purpose |
| --- | --- |
| `cepat` | Quick, direct rewrite |
| `lengkap` | Rewrite with a full review pass |
| `audit` | Flag problems without rewriting |

## Presets

| Language | Code | Registers |
| --- | --- | --- |
| Indonesian | `id` | `formal`, `semiformal`, `informal`, `standar`, `email` |
| English | `en` | `formal`, `semiformal`, `informal`, `standard`, `email`, `chat` |

## Installation

1. Create a ZIP of `skill/sf-humanizer` with the `sf-humanizer/` folder at the archive root:

   ```bash
   cd skill && zip -r ../sf-humanizer.zip sf-humanizer
   ```

2. Upload the ZIP in claude.ai under **Settings > Skills**.

## Repository layout

```text
skill/sf-humanizer/   The skill: SKILL.md, references/, scripts/
samples/id/           Indonesian samples by register
samples/en/           English samples by register
tools/validate.py     Repository structure checker
tests/                pytest tests
docs/                 Documentation
```

## Development

```bash
pip install ruff pytest
ruff check .
pytest
python tools/validate.py
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines.

## License

[MIT](LICENSE). Third-party sample attribution is recorded in [NOTICE.md](NOTICE.md).
