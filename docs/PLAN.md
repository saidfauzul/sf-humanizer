# Rencana pengembangan sf-humanizer

sf-humanizer adalah Claude skill yang menulis ulang teks bernuansa AI agar terbaca seperti tulisan manusia, tanpa mengubah fakta. Skill ini mendukung bahasa Indonesia dan Inggris, dengan preset per bahasa dan register. Rilis pertama yang dituju adalah v0.1.0, dan progresnya dipantau di [Roadmap v0.1.0 (#9)](https://github.com/saidfauzul/sf-humanizer/issues/9).

## Tahapan

| Tahap | Isi | Versi | Issue |
| --- | --- | --- | --- |
| 0 | Fondasi repo | v0.0.1 | [#3](https://github.com/saidfauzul/sf-humanizer/issues/3) |
| 1 | Inti skill dan katalog | v0.1.0-alpha.1 | [#4](https://github.com/saidfauzul/sf-humanizer/issues/4) |
| 2 | Sumber dan korpus gelombang 1 | v0.1.0-alpha.2 | [#5](https://github.com/saidfauzul/sf-humanizer/issues/5) |
| 3 | Metrik dan build | v0.1.0-alpha.3 | [#6](https://github.com/saidfauzul/sf-humanizer/issues/6) |
| 4 | Preset lengkap | v0.1.0-beta.1 | [#7](https://github.com/saidfauzul/sf-humanizer/issues/7) |
| 5 | Uji dan rilis | v0.1.0 | [#8](https://github.com/saidfauzul/sf-humanizer/issues/8) |

## Struktur

```text
skill/sf-humanizer/          Skill yang dipasang di claude.ai
  SKILL.md                   Pemanggilan, alur kerja, aturan inti
  references/patterns-*.md   Katalog pola per bahasa
  references/locking.md      Aturan segmen terkunci
  references/glossary-*.md   Istilah yang dipertahankan
  references/presets/        Aturan per preset (Tahap 4)
  references/examples/       Contoh per preset, hasil build (Tahap 3 dan 4)
  scripts/metrics.py         Metrik teks (Tahap 3)
samples/<bahasa>/<register>/ Korpus: good/ dan pairs/
tools/                       validate.py, build.py, package.py
docs/                        Rencana, sumber, prompt sintetis, laporan uji
```

## Preset dan mode

Preset adalah gabungan bahasa dan register. Bahasa Indonesia memiliki `formal`, `semiformal`, `informal`, `standar`, dan `email`. Bahasa Inggris memiliki `formal`, `semiformal`, `informal`, `standard`, `email`, dan `chat`. Jumlahnya 11 preset.

Skill dipanggil dengan `sf-humanizer preset <bahasa>, <register> [mode cepat|lengkap|audit]`.

- `cepat` memberikan teks akhir, catatan singkat, dan poin konfirmasi bila ada.
- `lengkap` memperlihatkan temuan, draf, audit draf, teks akhir, poin konfirmasi, dan ringkasan metrik.
- `audit` hanya memberikan temuan dan skor, tanpa menulis ulang.

Setiap penulisan ulang mengikuti tujuh langkah di `SKILL.md`. Fakta, angka, nama, rujukan, kutipan, dan istilah terkunci tidak berubah. Masalah substantif dilaporkan sebagai poin konfirmasi dan tidak diperbaiki diam-diam.

## Alur sampel

1. Lisensi sumber diverifikasi dan dicatat di `docs/sources.md`. Sumber yang lisensinya tidak jelas tidak dipakai.
2. Teks "sebelum" dibuat dari prompt yang dicatat di `docs/synthetic-prompts.md`.
3. Teks "sesudah" ditulis mengikuti katalog pola dan aturan penguncian.
4. Sampel diberi frontmatter sesuai `CONTRIBUTING.md` dan harus lulus `tools/validate.py`.
5. Pemilik repo meninjau sampel sebelum dipakai sebagai contoh.
6. Pada Tahap 3 dan 4, `tools/build.py` menyusun contoh dan profil metrik per preset dari korpus.

Dokumen nyata harus dianonimkan. Semua nama, perusahaan, nomor surat, dan nilai kontrak pada gelombang pertama bersifat fiktif. Teks buatan model ditandai `synthetic: true`.

## Alat

- `tools/validate.py` memeriksa ukuran berkas, versi, tautan, nama preset dalam aturan umum, kecocokan jumlah butir, dan format sampel.
- `scripts/metrics.py` (Tahap 3) mengukur panjang kalimat, verba ringan, nominalisasi, konektor, triplet, dan pemakaian merupakan/adalah, serta memeriksa segmen terkunci.
- `tools/build.py` (Tahap 3) menyusun contoh dan profil metrik ke preset.
- `tools/package.py` (Tahap 3) membuat ZIP dengan versi yang sinkron.

## Tata kelola

- Kode, komentar, dan pesan commit berbahasa Inggris. Dokumentasi pengguna berbahasa Indonesia, dengan README bahasa Inggris.
- Nama branch memakai awalan `feat/`, `fix/`, `docs/`, atau `samples/`, dan commit mengikuti Conventional Commits.
- Setiap perubahan masuk lewat pull request dengan CI hijau (ruff, pytest, validate), dan pemilik repo yang melakukan merge.
- Lisensi kode adalah MIT. Atribusi pihak ketiga dicatat di `NOTICE.md`.
- Repo dibuat publik pada Tahap 5, dan Private vulnerability reporting dinyalakan saat itu.
