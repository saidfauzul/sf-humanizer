# Prompt teks sintetis

Berkas ini mencatat prompt persis yang dipakai untuk membuat teks "sebelum" pada `samples/*/*/pairs/`, supaya bisa diulang. Semua nama, perusahaan, nomor surat, dan nilai kontrak dalam prompt adalah fiktif.

## Cara teks "sebelum" dibuat

Setiap prompt dikirim apa adanya ke model Claude, sebagai draf pertama, tanpa panduan gaya tambahan dan tanpa menyebut tujuan korpus ini. Hasil yang terlalu pendek dibuat ulang dari prompt yang sama. Teks dipakai tanpa suntingan, dengan satu pengecualian: pada `en-email-pair-001`, nama perusahaan yang keliru dibuat model (PT Maju Contoh) diganti dengan nama di prompt (Acme Sample Ltd). Karena model bersifat nondeterministik, pengulangan akan menghasilkan teks yang mirip, bukan sama.

## Cara teks "sesudah" dibuat

Teks "sesudah" ditulis ulang oleh Claude mengikuti katalog di `skill/sf-humanizer/references/patterns-*.md` dan aturan penguncian di `locking.md`. Teks itu lalu diperiksa terhadap fakta di prompt, segmen terkunci, dan jumlah butir.

Teks "sesudah" dan teks `good/` pada gelombang ini juga buatan model, bukan tulisan manusia. Karena itu semuanya ditandai `synthetic: true` dan `license: synthetic`, sesuai CONTRIBUTING.md. Setelah pemilik repo meninjau dan menyuntingnya sendiri, statusnya dapat diubah.

## Prompt

### id-formal-pair-001

Tulis laporan singkat berbahasa Indonesia formal sekitar 220 kata tentang hasil evaluasi penawaran Tender pengadaan perangkat jaringan. Fakta: Pokja Pemilihan menerima 3 penawaran; PT Maju Contoh menjadi calon pemenang dengan harga penawaran Rp1.250.000.000; HPS Rp1.400.000.000; evaluasi selesai 12 November 2026; masa sanggah 5 hari kerja. Tulis langsung teksnya saja.

### id-formal-pair-002

Tulis penjelasan berbahasa Indonesia formal sekitar 220 kata untuk pegawai tentang kewajiban menetapkan HPS tepat waktu. Teks harus memuat persis kutipan ini: Pasal 7 ayat (2) Peraturan Direksi Contoh Nomor 1 Tahun 2026 berbunyi "HPS ditetapkan paling lambat 14 (empat belas) hari kerja sebelum batas akhir pemasukan penawaran." Tulis langsung teksnya saja.

### id-formal-pair-003

Tulis bagian SOP verifikasi tagihan Penyedia dalam bahasa Indonesia formal sekitar 220 kata, terdiri atas satu paragraf pengantar dan lima langkah bernomor. Langkah: (1) Penyedia menyerahkan tagihan ke Sekretariat; (2) Sekretariat mencatat tagihan pada hari yang sama; (3) PPK memeriksa kesesuaian dengan Berita Acara Serah Terima paling lama 3 hari kerja; (4) Bagian Keuangan menghitung pajak; (5) Kepala Bagian Keuangan menyetujui pembayaran. Tulis langsung teksnya saja.

### id-formal-pair-004

Tulis nota dinas berbahasa Indonesia formal sekitar 220 kata. Nomor ND-001/XI/2026, dari Kepala Divisi Pengadaan kepada Kepala Divisi Keuangan, perihal permintaan data realisasi anggaran triwulan III. Data diperlukan untuk menyusun RUP tahun 2027 dan harus diterima paling lambat 20 November 2026. Tulis langsung teksnya saja.

### id-formal-pair-005

Tulis pengumuman internal berbahasa Indonesia formal sekitar 220 kata tentang kewajiban seluruh pegawai yang terlibat pengadaan menandatangani Pakta Integritas dan melaporkan Benturan Kepentingan. Fakta: berlaku sejak 1 Desember 2026; laporan disampaikan kepada Satuan Pengawas Internal paling lambat 3 hari kerja setelah benturan diketahui. Tulis langsung teksnya saja.

### id-email-pair-001

Tulis surel kerja berbahasa Indonesia sekitar 200 kata dari Rina Contoh (Pejabat Pengadaan) kepada PT Maju Contoh tentang keterlambatan pengiriman 20 unit laptop. Batas pengiriman 5 November 2026 sudah lewat, Denda Keterlambatan berlaku sesuai kontrak, dan Penyedia diminta mengirim jadwal baru paling lambat 10 November 2026. Tulis langsung surelnya saja.

### id-email-pair-002

Tulis surel kerja berbahasa Indonesia sekitar 200 kata dari Budi Contoh kepada atasannya, Ibu Sari Contoh, meminta persetujuan perpanjangan waktu penyusunan KAK jasa konsultansi dari 14 November menjadi 21 November 2026, karena data dari unit pengguna baru diterima 6 November 2026. Tulis langsung surelnya saja.

### id-email-pair-003

Tulis surel kerja berbahasa Indonesia sekitar 200 kata dari Dewi Contoh (Divisi Pengadaan) kepada Andi Contoh (Divisi Hukum) meminta reviu Rancangan Kontrak jasa kebersihan senilai Rp480.000.000 paling lambat 18 November 2026, khususnya klausul Jaminan Pelaksanaan dan pemutusan kontrak. Tulis langsung surelnya saja.

### id-email-pair-004

Tulis surel kerja berbahasa Indonesia sekitar 200 kata dari sekretariat Pokja Pemilihan yang mengundang seluruh anggota rapat pembahasan Spesifikasi Teknis pada Selasa, 17 November 2026, pukul 09.00 WIB, di Ruang Rapat Contoh 2. Anggota diminta membawa catatan reviu masing-masing. Tulis langsung surelnya saja.

### id-email-pair-005

Tulis surel kerja berbahasa Indonesia sekitar 200 kata dari Tono Contoh (Bagian Keuangan) kepada PT Sumber Fiktif, memberi tahu bahwa tagihan nomor INV-077/X/2026 belum dapat diproses karena Berita Acara Serah Terima belum dilampirkan. Penyedia diminta melengkapinya paling lambat 13 November 2026. Tulis langsung surelnya saja.

### en-email-pair-001

Write a work email of about 200 words from Maya Example (Procurement Officer) to Acme Sample Ltd about a late delivery of 20 laptops. The delivery date of 5 November 2026 has passed, liquidated damages apply under the contract, and the vendor must send a new schedule by 10 November 2026. Write only the email.

### en-email-pair-002

Write a work email of about 200 words from Ben Example to their manager, Sara Example, asking to extend the deadline for the Statement of Work from 14 November to 21 November 2026, because data from the requesting team only arrived on 6 November 2026. Write only the email.

### en-email-pair-003

Write a work email of about 200 words from Dana Example (Procurement) to Alex Example (Legal) asking for a review of a draft cleaning services contract worth $48,000 by 18 November 2026, especially the Performance Bond and termination clauses. Write only the email.

### en-email-pair-004

Write a work email of about 200 words inviting the Evaluation Committee to a meeting on the Technical Specifications on Tuesday 17 November 2026 at 9:00 a.m. in Sample Room 2. Members should bring their review notes. Write only the email.

### en-email-pair-005

Write a work email of about 200 words from Tom Example (Finance) to Fictional Supplies Inc. saying that invoice INV-077 cannot be processed because the signed Acceptance record was not attached. The vendor must supply it by 13 November 2026. Write only the email.
