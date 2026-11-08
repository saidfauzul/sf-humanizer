# sf-humanizer

[English](README.en.md) · **Bahasa Indonesia**

> **Status: pre-alpha.** Skill ini masih berupa kerangka; perilaku dan struktur preset masih bisa berubah.

sf-humanizer adalah Claude skill yang menulis ulang teks bernuansa AI agar terbaca seperti tulisan manusia, tanpa mengubah fakta di dalamnya. Skill ini mendukung bahasa Indonesia dan Inggris.

## Cara memakai

```text
sf-humanizer preset <bahasa>, <register> [mode cepat|lengkap|audit]
```

Contoh: `sf-humanizer preset id, formal mode lengkap`

| Mode | Kegunaan |
| --- | --- |
| `cepat` | Penulisan ulang langsung |
| `lengkap` | Penulisan ulang dengan pemeriksaan menyeluruh |
| `audit` | Menandai masalah tanpa menulis ulang |

## Preset

| Bahasa | Kode | Register |
| --- | --- | --- |
| Indonesia | `id` | `formal`, `semiformal`, `informal`, `standar`, `email` |
| Inggris | `en` | `formal`, `semiformal`, `informal`, `standard`, `email`, `chat` |

## Pemasangan

1. Buat berkas ZIP dari folder `skill/sf-humanizer` sehingga folder `sf-humanizer/` berada di akar arsip:

   ```bash
   cd skill && zip -r ../sf-humanizer.zip sf-humanizer
   ```

2. Unggah ZIP tersebut di claude.ai melalui **Settings > Skills**.

## Struktur repositori

```text
skill/sf-humanizer/   Skill: SKILL.md, references/, scripts/
samples/id/           Sampel bahasa Indonesia per register
samples/en/           Sampel bahasa Inggris per register
tools/validate.py     Pemeriksa struktur repositori
tests/                Pengujian pytest
docs/                 Dokumentasi
```

## Pengembangan

```bash
pip install ruff pytest
ruff check .
pytest
python tools/validate.py
```

Panduan kontribusi ada di [CONTRIBUTING.md](CONTRIBUTING.md).

## Lisensi

[MIT](LICENSE). Atribusi sampel pihak ketiga dicatat di [NOTICE.md](NOTICE.md).
