# Uji manual di claude.ai dan langkah rilis

## Memasang skill

1. Buka **Settings > Skills** di claude.ai.
2. Unggah `sf-humanizer-0.1.0.zip`.
3. Pastikan skill `sf-humanizer` aktif.

## Enam pemeriksaan

Tempel isi berkas dari `tests/manual/` setelah perintah berikut.

| Perintah | Berkas | Yang dilihat |
| --- | --- | --- |
| `sf-humanizer preset id, formal mode cepat` | `id-formal.md` | Kutipan pasal utuh, formula surat tetap ada, perbedaan Pasal 13 dan Pasal 31 dilaporkan sebagai poin konfirmasi |
| `sf-humanizer preset id, email mode lengkap` | `id-email.md` | Ada temuan, draf utuh, audit draf, teks akhir, poin konfirmasi, dan ringkasan metrik |
| `sf-humanizer preset id, informal mode audit` | `id-informal.md` | Hanya temuan dan skor, tanpa penulisan ulang |
| `sf-humanizer preset en, email mode cepat` | `en-email.md` | Tanpa kalimat pembuka, fakta di subjek tetap, tiga lawan empat lampiran dilaporkan |
| `sf-humanizer preset en, chat mode cepat` | `en-chat.md` | Terbaca seperti percakapan, label penutur tetap |
| `sf-humanizer preset en, formal mode lengkap` | `en-formal.md` | Kutipan Section utuh, "shall" tidak berubah |

Periksa juga bahwa angka, tanggal, nomor dokumen, dan nama tidak berubah. Di claude.ai, `metrics.py` hanya berjalan bila eksekusi kode tersedia. Bila tidak, skill harus menyebut bahwa angkanya perkiraan.

## Langkah rilis

1. Naikkan versi menjadi `0.1.0` di `SKILL.md` dan `pyproject.toml` (`0.1.0`), lalu pindahkan isi `Unreleased` di `CHANGELOG.md` ke `## [0.1.0] - <tanggal>`.
2. Jalankan `ruff check .`, `pytest`, `python tools/validate.py`, `python tools/build.py --check`, lalu merge ke `main`.
3. Dari `main`, buat tag yang memicu `release.yml`:

   ```bash
   git tag v0.1.0 && git push --tags
   ```

4. Pastikan GitHub Release berisi ZIP.
5. Ubah repo menjadi publik di **Settings > General**.
6. Nyalakan **Private vulnerability reporting** di **Settings > Advanced Security**.
