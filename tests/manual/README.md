# Uji manual sf-humanizer

## Tujuan

Folder ini berisi 11 masukan tetap, satu untuk setiap preset. Masukan dipakai untuk memeriksa secara manual bahwa skill menerapkan preset yang diminta, menjaga segmen terkunci, mengurangi pola tulisan AI tanpa menambah fakta, dan mengajukan titik konfirmasi bila naskah memuat masalah substantif.

Semua skenario, nama, perusahaan, nomor dokumen, dan nominal bersifat fiktif serta tidak diambil dari `samples/`. Setiap berkas hanya berisi teks masukan.

Cara pakai: jalankan setiap berkas dengan preset yang sesuai, misalnya `sf-humanizer preset id, formal mode lengkap`, lalu nilai hasilnya dengan daftar periksa di bagian akhir. Pemeriksaan otomatis memakai:

```text
python3 skill/sf-humanizer/scripts/metrics.py --check-locked tests/manual/<berkas>.md HASIL --lang <id|en>
python3 skill/sf-humanizer/scripts/metrics.py --compare tests/manual/<berkas>.md HASIL --lang <id|en>
```

Butir bernomor pada `id-semiformal.md`, `en-semiformal.md`, dan `en-standard.md` sengaja bersih dari pola. `--check-locked` memeriksa baris langkah secara utuh, jadi langkah-langkah itu harus keluar sama persis.

## Isi uji per berkas

Segmen terkunci di bawah ini harus muncul persis seperti tertulis pada teks akhir.

### id-formal.md

Menguji nota dinas soal Denda Keterlambatan, kutipan Pasal, dan penanganan rujukan pasal yang keliru. Pola: ID-01, ID-02, ID-03, ID-04, ID-05, ID-06, ID-07, ID-14 (kuat kecuali ID-14).

- Nomor dokumen: `077/ND-SPI/XI/2026`, `0419/KTR-PML/III/2026`, `58/PER-DIR/2025`
- Tanggal: `9 November 2026`, `12 Oktober 2026`, `30 September 2026`, `20 November 2026`
- Nominal dan angka: `Rp480.000.000`, `Rp5.760.000`, `12`, `1/1000`
- Pasal dan rujukan: `Pasal 31 ayat (1)`, `Pasal 13 ayat (1)`
- Kutipan: seluruh baris `Pasal 31 ayat (1) Peraturan Direksi Nomor 58/PER-DIR/2025 tentang Pengelolaan Kontrak berbunyi: "Penyedia yang terlambat menyelesaikan pekerjaan dikenai Denda Keterlambatan sebesar 1/1000 dari nilai Kontrak untuk setiap hari keterlambatan, dan denda tersebut dipotong oleh PPK dari pembayaran yang menjadi hak Penyedia."`
- Nama dan jabatan: `Lembaga Khayalan Nusantara`, `PT Lift Angkasa Khayalan`, `Kepala Divisi Pengadaan`, `Kepala Satuan Pengawas Internal`, `Divisi Pengadaan`, `Divisi Keuangan`, `Galih Khayalan`
- Glosarium: `PPK`, `Penyedia`, `Berita Acara`, `Serah Terima`, `Denda Keterlambatan`, `Peraturan Direksi`

### id-semiformal.md

Menguji memo internal hasil rapat Register Gratifikasi dan pelestarian butir keputusan. Pola: ID-02, ID-03, ID-04, ID-05, ID-06, ID-07, ID-09 (kuat), ID-11, ID-12, ID-13, ID-14.

- Nomor dokumen: `204/MM-TK/XI/2026`
- Tanggal: `3 November 2026`, `31 Oktober 2026`, `15 Desember 2026`, `20 November 2026`, `27 November 2026`, `8 Desember 2026`
- Nominal dan angka: `Rp750.000`, `14`, `9`, `5`
- Langkah bernomor, utuh:
  - `1. Seksi Administrasi Kontrak menelusuri 5 laporan yang belum ditetapkan statusnya, paling lambat 20 November 2026.`
  - `2. Seksi Hukum mengkaji batas nilai Rp750.000, paling lambat 27 November 2026.`
  - `3. Kirana Khayalan menyusun rekap akhir untuk Komite Etik Khayalan, paling lambat 8 Desember 2026.`
- Nama dan jabatan: `Kirana Khayalan`, `Koordinator Kepatuhan`, `Divisi Tata Kelola`, `Tim Kepatuhan`, `Register Gratifikasi`, `Komite Etik Khayalan`, `Seksi Administrasi Kontrak`, `Seksi Hukum`

### id-informal.md

Menguji pesan grup santai soal kotak P3K, dengan nada akrab yang tetap terjaga. Pola: ID-02, ID-03, ID-04, ID-05, ID-06, ID-08, ID-09 (kuat), ID-11, ID-14.

- Nomor dokumen: `PO-7731`
- Tanggal dan waktu: `16 November 2026`, `24 November 2026`, `18 November 2026`, `09.00`
- Nominal dan angka: `Rp4.750.000`, `12`, `3`, `1`
- Nama: `Seksi Logistik`, `Mas Bayu Khayalan`, `Mbak Sekar Khayalan`, `Tim Khayalan Sehat`, `Mas Bayu`, `Mbak Sekar`

### id-standar.md

Menguji laporan publik pengadaan peralatan pemadam kebakaran dan pendeteksian jumlah yang tidak cocok. Pola: ID-02, ID-03, ID-04, ID-05, ID-06, ID-08, ID-09 (kuat), ID-11, ID-12, ID-14.

- Nomor dokumen: `31/PENG-DPK/XI/2026`
- Tanggal: `6 November 2026`, `2 Maret 2026`, `17 April 2026`, `28 Agustus 2026`, `31 Desember 2026`
- Nominal dan angka: `Rp212.500.000`, `Rp87.250.000`, `Rp45.000.000`, `Rp354.750.000`, `150`, `40`, `12`, `2026`
- Nama: `Kabupaten Khayalan Jaya`, `Dinas Pemadam Khayalan`, `CV Pelita Khayalan`
- Glosarium: `Tender`, `Penyedia`
- Surel: `info@dinaspemadam.khayalan.example`

### id-email.md

Menguji surel klarifikasi kepada Penyedia, termasuk baris subjek dan salam penutup. Pola: ID-02, ID-04, ID-05, ID-06 (kuat), ID-12, ID-14, ID-16.

- Nomor dokumen: `RFQ-8842`
- Tanggal dan waktu: `10 November 2026`, `30 Juni 2026`, `1 Desember 2026`, `17 November 2026`, `15.00`
- Nominal dan angka: `Rp136.400.000`, `4`
- Nama dan jabatan: `Bapak Tirta Khayalan`, `PT Timbang Khayalan`, `Lintang Khayalan`, `Gudang Khayalan Sentosa`
- Glosarium: `Dokumen Penawaran`, `Pejabat Pengadaan`, `Pemilihan`
- Surel: `pengadaan@gudangkhayalan.example`

### en-formal.md

Menguji surat resmi penangguhan Prequalification, kutipan Section, dan pelestarian kata "shall". Pola: EN-01, EN-02, EN-04, EN-05, EN-06, EN-07, EN-11, EN-12 (kuat), EN-13.

- Nomor dokumen: `2291/GOV-NTC/2026`, `SUP-60418`
- Tanggal: `9 November 2026`, `16 November 2026`, `2 September 2026`, `5 October 2026`, `30 November 2026`
- Nominal dan angka: `$312,000`, `2024`
- Pasal dan rujukan: `Section 14(2)`
- Kutipan: `"A Supplier shall notify the Authority in writing of any change in its ownership or control within 10 working days of that change."`
- Nama dan jabatan: `Quillon Harbour Authority (Fictional)`, `Zephyr Mockworks Ltd`, `Supplier Conduct Code 2024`, `Odalys Madeup`, `Head of Governance`
- Glosarium: `Supplier`, `Prequalification`, `Internal Audit`, `Open Tender`, `Purchase Order`, `Conflict of Interest`
- Surel: `governance@quillon.example`

### en-semiformal.md

Menguji memo bergaya SOP tentang perubahan rekening Supplier, dengan langkah bernomor dan pelaku bernama. Pola: EN-01, EN-02, EN-03, EN-04, EN-05, EN-06, EN-09, EN-11, EN-12 (kuat), EN-13.

- Nomor dokumen: `SOP-6620`, `BK-22`
- Tanggal: `1 December 2026`, `27 November 2026`
- Nominal dan angka: `$25,000`, `3`
- Langkah bernomor, utuh:
  - `1. The Accounts Payable Clerk records the request on Form BK-22 on the day it is received and checks the sender's email address against the Supplier file.`
  - `2. The Procurement Analyst telephones the Supplier on the number held in the Supplier file, within 2 working days.`
  - `3. The Accounts Payable Clerk updates the bank details in the system only after the Procurement Analyst has signed Form BK-22.`
  - `4. The Finance Controller decides on any change affecting payments above $25,000, within 1 working day of receiving Form BK-22.`
  - `5. The Internal Audit Lead reviews a sample of 10 completed forms every month.`
- Nama dan jabatan: `Tavi Madeup`, `Finance Controller`, `Nimbus Payables Sandbox`, `Accounts Payable Clerk`, `Procurement Analyst`, `Internal Audit Lead`
- Glosarium: `Supplier`, `Segregation of Duties`

### en-informal.md

Menguji catatan buletin tim soal rak sepeda, dengan suara penulis dan candaan yang harus tetap ada. Pola: EN-01, EN-02, EN-03, EN-04, EN-05, EN-06, EN-09, EN-12 (kuat), EN-15.

- Nomor dokumen: `RFP-5570`
- Tanggal: `5 October 2026`, `12 December 2026`, `30 November 2026`
- Nominal dan angka: `$48,200`, `7`
- Nama: `Pim Madeup`, `Pim`, `Wren`, `Spoke & Sprocket Fictional Co`

### en-standard.md

Menguji panduan publik pendaftaran Supplier kecil dan pendeteksian klaim tanpa dasar. Pola: EN-01, EN-02, EN-03, EN-04, EN-05, EN-06, EN-07, EN-12 (kuat), EN-15.

- Nomor dokumen: `7702/PUB/2026`
- Tanggal: `4 January 2027`, `26 February 2027`
- Nominal dan angka: `$40`, `50`, `15`, `10`, `2`
- Langkah bernomor, utuh:
  - `1. Create a business profile on the portal.`
  - `2. Upload your trade license and your most recent tax certificate.`
  - `3. Pay the fee of $40 by card.`
  - `4. Submit the application and keep the reference number that you receive.`
- Nama: `City of Larkspur Fictional`, `Larkspur`
- Glosarium: `Supplier`, `Request for Quotation`
- URL dan surel: `https://larkspur.example/suppliers`, `suppliers@larkspur.example`

### en-email.md

Menguji surel perpanjangan kontrak bus antar-jemput dan pendeteksian jumlah lampiran yang tidak cocok. Pola: EN-01, EN-02, EN-04, EN-05, EN-06, EN-11, EN-12 (kuat), EN-14, EN-15.

- Nomor dokumen: `SB-4409`, `Amendment No. 2`
- Tanggal: `31 December 2026`, `19 November 2026`, `4 December 2026`
- Nominal dan angka: `$86,500`, `$79,000`, `2027`
- Nama dan jabatan: `Ms. Fenwick`, `Orbit Shuttle Fictional Ltd`, `Ivo Madeup`, `Marlo Madeup`
- Glosarium: `Contract Manager`, `Procurement Officer`, `Vendor`, `Amendment`

### en-chat.md

Menguji utas obrolan kerja soal printer kartu, dengan label pembicara dan urutan giliran yang harus tetap. Pola: EN-01, EN-02, EN-03, EN-04, EN-05, EN-06, EN-09, EN-12 (kuat).

- Nomor dokumen: `Q-9130`
- Tanggal: `24 November 2026`, `20 November 2026`
- Nominal dan angka: `$3,740`, `$4,100`, `6`, `5120`, `10`
- Nama: `Plastikard Fictional`, `Noor Madeup`, `Noor`, `Juno`, `Bex`
- Label pembicara: `**Juno:**`, `**Bex:**`
- Glosarium: `Purchase Order`

## Berkas dengan masalah tertanam

Empat berkas berikut masing-masing memuat tepat satu masalah. Tujuh berkas lainnya tidak memuat masalah semacam ini.

| Berkas | Masalah |
| --- | --- |
| `id-standar.md` | Total tertulis `Rp354.750.000`, padahal Rp212.500.000 + Rp87.250.000 + Rp45.000.000 = Rp344.750.000. |
| `id-formal.md` | Teks merujuk `Pasal 13 ayat (1)` "yang dikutip di atas", padahal pasal yang dikutip adalah `Pasal 31 ayat (1)`. |
| `en-email.md` | Teks menyebut "three documents", padahal daftarnya berisi empat dokumen. |
| `en-standard.md` | Klaim "win three times as many public contracts" dan "the single most effective step" tanpa sumber atau dasar apa pun dalam teks. |

Segmen bermasalah tetap tidak boleh diubah. Skill harus membiarkannya dan mengajukan titik konfirmasi yang mengutip segmen tersebut.

## Daftar periksa penerimaan

- (a) Skill dan preset benar-benar diterapkan.
- (b) Bentuk keluaran sesuai mode. `cepat`: teks akhir, satu sampai tiga catatan, dan titik konfirmasi saja. `lengkap`: temuan, draf, audit, teks akhir, titik konfirmasi, dan metrik. `audit`: temuan dan skor, tanpa penulisan ulang.
- (c) `scripts/metrics.py --check-locked` lolos untuk teks akhir mode `cepat` dan `lengkap`.
- (d) `--compare` menunjukkan verba ringan, konektor, atau nominalisasi berkurang.
- (e) Tidak ada fakta baru.
- (f) Register sesuai.
- (g) Titik konfirmasi diajukan pada berkas yang memuat masalah tertanam.
