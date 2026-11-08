# Laporan uji v0.1

## Metode

Uji dijalankan pada 8 November 2026 lewat Claude Code (`claude -p`, model bawaan) sebagai pengganti claude.ai, dengan skill dimuat dari folder di luar repo. Unggahan ke claude.ai belum diuji. Masukan ada di `tests/manual/`, keluaran di `tests/manual/runs/2026-11-08/`.

Ada 33 kombinasi pada putaran pertama. Setelah perbaikan, sebagian dijalankan ulang, tetapi pemakaian habis di tengah jalan, jadi laporan ini memakai 17 kombinasi: 11 preset mode `cepat`, 3 `lengkap`, dan 3 `audit`. Kolom "Putaran" menunjukkan versi skill yang menghasilkan keluaran tersebut. Delapan keluaran berasal dari skill yang sudah diperbaiki.

Kriteria: (a) skill dan preset diterapkan, (b) bentuk sesuai mode, (c) `--check-locked` lulus, (d) `--compare` menunjukkan penurunan pola, (e) tidak ada fakta baru atau hilang, (f) sesuai register, (g) poin konfirmasi muncul untuk masalah yang ditanam. Kriteria (c) dan (d) dijalankan dengan `metrics.py`. Teks akhir mode `cepat` dibaca langsung, sedangkan (e) dan (f) pada kombinasi lain dinilai oleh agen peninjau dan diperiksa sebagian.

## Hasil

| Preset | Mode | Putaran | a | b | c | d | e | f | g | Catatan |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| id formal | cepat | ulang | P | P | P | P | P | P | P | Pasal 13 dan 31 dilaporkan, "perlu" tetap "perlu" |
| id semiformal | cepat | pertama | P | P | P | P | P | P | NA | Poin konfirmasi tambahan yang wajar |
| id informal | cepat | ulang | P | P | P | P | P | P | NA | Sedikit irama "bukan cuma ... tapi" tersisa |
| id standar | cepat | pertama | P | P | P | P | P | P | P | Selisih total Rp10.000.000 dilaporkan |
| id email | cepat | pertama | P | P | P | P | P | P | NA | Poin konfirmasi palsu soal tanggal; perbaikan belum diuji ulang |
| en formal | cepat | pertama | P | P | P | P | P | P | NA | Poin konfirmasi palsu soal tanggal; verba ringan 2 menjadi 1 |
| en semiformal | cepat | pertama | P | P | P | P | P | P | NA | Langkah bernomor utuh |
| en informal | cepat | ulang | P | P | P | P | P | P | NA | Pembuka tambahan sudah hilang |
| en standard | cepat | pertama | P | P | P | P | P | P | P | Klaim tanpa sumber dilaporkan; catatan masih berbahasa Indonesia, perbaikan belum diuji ulang |
| en email | cepat | ulang | P | P | P | P | P | P | P | Tiga lawan empat lampiran dilaporkan |
| en chat | cepat | pertama | P | P | P | P | P | P | NA | Satu klaim kosong tersisa di teks |
| id formal | lengkap | ulang | P | P | P | P | P | P | P | Draf kini ditulis utuh |
| id email | lengkap | ulang | P | P | P | P | P | P | NA | Draf kini ditulis utuh |
| en formal | lengkap | ulang | P | P | P | P | P | P | NA | Draf kini ditulis utuh |
| id informal | audit | ulang | P | P | NA | NA | P | P | NA | Skor 16,8, tinggi |
| en email | audit | pertama | P | F | NA | NA | P | P | P | Ada kalimat pembuka; perbaikan belum diuji ulang |
| en chat | audit | pertama | P | F | NA | NA | P | P | NA | Ada kalimat pembuka; perbaikan belum diuji ulang |

Jumlah lulus: a 17/17, b 15/17, c 14/14, d 14/14, e 17/17, f 17/17, g 6/6. Pada putaran pertama seluruh 33 kombinasi, kriteria b gagal pada 19 kombinasi dan e gagal pada 3 kombinasi.

## Kalibrasi skor audit

Skor dihitung dengan pendekatan metrik: (3 x temuan kuat + temuan lemah) x 100 / jumlah kata. Temuan kuat adalah verba ringan, konektor, rantai nominalisasi, dan pertanyaan retoris. Temuan lemah adalah triplet, kata intensif, em dash, dan "merupakan".

| Kelompok | Teks | P10 | Median | P90 |
| --- | --- | --- | --- | --- |
| Baik dan sesudah | 88 | 0,00 | 0,53 | 4,67 |
| Sebelum | 55 | 4,21 | 6,35 | 13,52 |
| Masukan uji | 11 | 9,12 | 10,04 | 15,42 |

Batas yang dipilih: rendah di bawah 3, sedang 3 sampai 6, tinggi di atas 6.

| Kelompok | Rendah | Sedang | Tinggi |
| --- | --- | --- | --- |
| Baik dan sesudah | 69 | 15 | 4 |
| Sebelum | 2 | 21 | 32 |
| Masukan uji | 0 | 0 | 11 |

Batas lama (3 dan 8) hanya menempatkan 19 teks "sebelum" pada tinggi. Skor yang ditulis skill pada mode `audit` berasal dari temuan yang dibaca model, jadi angkanya dapat berbeda dari pendekatan metrik ini. Kalibrasi dilakukan pada data sintetis.

## Perbaikan

- `SKILL.md`: keluaran langsung mulai dari isi tanpa kalimat pembuka, draf ditulis utuh, kekuatan kewajiban dipertahankan, poin konfirmasi tidak diangkat hanya karena tanggal lebih lambat dari hari ini, bahasa catatan mengikuti teks bila pesan hanya berisi perintah dan teks, serta total temuan harus cocok.
- `metrics.py`: nama tidak lagi melewati tanda kurung, salam tidak dianggap nama, verba ringan mengenali nomina pe-an dan "the conduct of", "document" tidak lagi dianggap nominalisasi, permintaan sopan tidak dihitung sebagai pertanyaan retoris, dan konektor tidak dihitung sebagai butir triplet.

## Keterbatasan

- Korpus sintetis, dan katalog belum tervalidasi pada teks AI asli ([#12](https://github.com/saidfauzul/sf-humanizer/issues/12)).
- Unggahan dan uji di claude.ai belum dilakukan.
- Lima kombinasi dengan temuan pada putaran pertama (`id email cepat`, `en formal cepat`, `en standard cepat`, dan dua `audit` berbahasa Inggris) belum dijalankan ulang setelah perbaikan.
- Masukan uji ditulis oleh model dengan pola yang sengaja dimasukkan, jadi keberhasilan penurunan pola tidak otomatis berlaku untuk teks nyata.
