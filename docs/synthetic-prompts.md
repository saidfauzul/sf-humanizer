# Prompt teks sintetis

Berkas ini mencatat prompt persis yang dipakai untuk membuat teks "sebelum" pada `samples/*/*/pairs/`, supaya bisa diulang. Semua nama, perusahaan, nomor surat, dan nilai kontrak dalam prompt adalah fiktif.

## Cara teks "sebelum" dibuat

Setiap prompt dikirim apa adanya ke model Claude, sebagai draf pertama, tanpa panduan gaya tambahan dan tanpa menyebut tujuan korpus ini. Hasil yang terlalu pendek dibuat ulang dari prompt yang sama. Teks dipakai tanpa suntingan, dengan satu pengecualian: pada `en-email-pair-001`, nama perusahaan yang keliru dibuat model (PT Maju Contoh) diganti dengan nama di prompt (Acme Sample Ltd). Karena model bersifat nondeterministik, pengulangan akan menghasilkan teks yang mirip, bukan sama.

## Cara teks "sesudah" dibuat

Teks "sesudah" ditulis ulang oleh Claude mengikuti katalog di `skill/sf-humanizer/references/patterns-*.md` dan aturan penguncian di `locking.md`. Teks itu lalu diperiksa terhadap fakta di prompt, segmen terkunci, dan jumlah butir.

Teks "sesudah" dan teks `good/` pada gelombang ini juga buatan model, bukan tulisan manusia. Karena itu semuanya ditandai `synthetic: true` dan `license: synthetic`, sesuai CONTRIBUTING.md. Setelah saya tinjau dan sunting sendiri, statusnya dapat diubah.

## Teks "sebelum" yang dibuat ulang

Setelah tinjauan kualitas, teks "sebelum" yang memuat kurang dari 4 pola katalog dibuat ulang oleh Claude. Teks barunya bukan hasil prompt per sampel di bawah, melainkan disusun dari teks "sesudah" dengan templat berikut. Prompt di bawah tetap dicatat sebagai asal skenario dan fakta.

```text
Rewrite the following text in the voice of a generic AI assistant. Use at least four of these catalog patterns, including at least two marked strong: <list of ids>. Keep every fact, number, date, name, reference and quotation exactly. Add no facts. Match the original length. Keep the document type. Text: <after text>
```

Teks hasil templat ini memuat pola yang sengaja disisipkan, jadi sebagian terasa lebih kaku atau dibuat-buat dibanding keluaran model yang sebenarnya.

Cara lain yang dicoba tanpa penyisipan dicatat di [laporan percobaan](experiments/2026-11-08-teks-sebelum.md).

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

### id-semiformal-pair-001

Tulis memo internal berbahasa Indonesia sekitar 220 kata kepada tim Divisi Pengadaan tentang hasil rapat evaluasi kinerja Penyedia jasa katering PT Rasa Contoh. Fakta: rapat 4 November 2026; 2 keterlambatan pengiriman pada Oktober; kontrak berakhir 31 Desember 2026; tim diminta mengumpulkan catatan kinerja paling lambat 16 November 2026. Tulis langsung teksnya saja.

### id-semiformal-pair-002

Tulis laporan progres singkat berbahasa Indonesia sekitar 220 kata untuk rapat mingguan Divisi Pengadaan. Fakta: dari 12 paket tahun 2026, 8 sudah berkontrak, 3 dalam proses Tender, dan 1 ditunda karena anggaran belum tersedia; target seluruh paket berkontrak 15 Desember 2026. Tulis langsung teksnya saja.

### id-informal-pair-001

Tulis pesan santai berbahasa Indonesia sekitar 200 kata kepada teman kantor, menceritakan rapat Pokja Pemilihan hari Senin yang molor sampai pukul 19.00 karena Spesifikasi Teknis berubah 3 kali, dan mengajak makan siang Rabu di kantin. Tulis langsung pesannya saja.

### id-informal-pair-002

Tulis unggahan santai berbahasa Indonesia sekitar 200 kata untuk grup kantor tentang pengalaman pertama memakai E-purchasing untuk membeli 10 kursi. Pesanan selesai dalam 2 hari, tetapi satu kursi datang dalam keadaan rusak dan sudah diganti Penyedia. Tulis langsung unggahannya saja.

### id-standar-pair-001

Tulis artikel penjelasan berbahasa Indonesia sekitar 220 kata untuk pembaca umum tentang apa itu Pengadaan Langsung dan apa bedanya dengan Tender. Tulis langsung teksnya saja.

### id-standar-pair-002

Tulis artikel penjelasan berbahasa Indonesia sekitar 220 kata untuk pembaca umum tentang fungsi Jaminan Pelaksanaan dalam kontrak pengadaan. Tulis langsung teksnya saja.

### en-formal-pair-001

Write a formal policy notice of about 220 words requiring all staff involved in procurement to declare any Conflict of Interest. Facts: effective 1 December 2026; declarations go to Internal Audit within 3 working days of the conflict becoming known. Write only the notice.

### en-formal-pair-002

Write a formal report of about 220 words on a Contract Award for network equipment. Facts: the Evaluation Committee received 3 bids; Acme Sample Ltd was recommended at $125,000; the Independent Cost Estimate was $140,000; evaluation finished on 12 November 2026; the Bid Protest period is 5 working days. Write only the report.

### en-semiformal-pair-001

Write an internal memo of about 220 words to the Procurement team about a vendor performance review of Sample Catering Ltd. Facts: the meeting was on 4 November 2026; there were 2 late deliveries in October; the contract ends on 31 December 2026; the team must send performance notes by 16 November 2026. Write only the memo.

### en-semiformal-pair-002

Write a short progress briefing of about 220 words for a weekly Procurement meeting. Facts: of 12 packages for 2026, 8 are under contract, 3 are out to tender, and 1 is on hold because funding is not yet available; the target is all packages under contract by 15 December 2026. Write only the briefing.

### en-informal-pair-001

Write a casual message of about 200 words to a work friend about a Monday committee meeting that ran until 7 p.m. because the Technical Specifications changed 3 times, and suggest lunch on Wednesday in the cafeteria. Write only the message.

### en-informal-pair-002

Write a casual post of about 200 words for an office group about using the new online purchasing catalog for the first time to buy 10 chairs. The order took 2 days, but one chair arrived broken and the vendor has replaced it. Write only the post.

### en-standard-pair-001

Write an explanatory article of about 220 words for a general audience on what a Framework Agreement is and why organizations use one. Write only the article.

### en-standard-pair-002

Write an explanatory article of about 220 words for a general audience on what a Performance Bond does in a contract. Write only the article.

### en-chat-pair-001

Write a work chat thread of about 180 words, as one person's series of messages in a team channel, telling colleagues that the vendor portal will be down on Friday 13 November from 6 p.m. to 9 p.m., that bids due that evening are moved to Monday 16 November at noon, and that questions should go to Maya. Write only the messages.

### en-chat-pair-002

Write a work chat thread of about 180 words, as one person's series of messages to a colleague, asking for the signed Acceptance record for PO 3107, which Finance needs by 3 p.m. today, and explaining that payment is held until it arrives. Write only the messages.

### id-semiformal-pair-003

Tulis notulen rapat berbahasa Indonesia sekitar 220 kata tentang rapat koordinasi penyusunan RUP 2027 pada 3 November 2026. Fakta: dihadiri 6 unit kerja; 2 unit belum mengirim usulan; batas pengiriman usulan diundur ke 17 November 2026; Dewi Contoh menjadi penanggung jawab rekapitulasi. Tulis langsung teksnya saja.

### id-semiformal-pair-004

Tulis pengumuman internal berbahasa Indonesia sekitar 220 kata tentang pindahnya layanan Sekretariat Pengadaan ke lantai 4 Gedung Contoh A mulai 23 November 2026. Layanan tutup pada 20 November 2026 pukul 12.00 WIB untuk pengemasan. Tulis langsung teksnya saja.

### id-semiformal-pair-005

Tulis memo internal berbahasa Indonesia sekitar 220 kata tentang perubahan prosedur pengajuan permintaan pembelian. Mulai 1 Desember 2026 permintaan di bawah Rp10.000.000 cukup disetujui kepala bagian. Permintaan melewati tiga langkah bernomor: (1) unit mengisi formulir PP-01; (2) kepala bagian menyetujui paling lama 2 hari kerja; (3) Pejabat Pengadaan memproses. Tulis langsung teksnya saja.

### id-standar-pair-003

Tulis pengumuman publik berbahasa Indonesia sekitar 220 kata dari Badan Contoh Nasional tentang pembukaan pendaftaran calon Penyedia pada 1 sampai 15 Desember 2026, melalui laman yang tersedia, dengan syarat memiliki izin usaha dan NPWP. Tulis langsung teksnya saja.

### id-standar-pair-004

Tulis ringkasan kebijakan berbahasa Indonesia sekitar 220 kata tentang kebijakan Badan Contoh Nasional yang mengutamakan produk dalam negeri dalam pengadaan, dengan batas nilai komponen dalam negeri paling sedikit 40 persen, berlaku mulai 1 Januari 2027. Tulis langsung teksnya saja.

### id-standar-pair-005

Tulis bagian laporan umum berbahasa Indonesia sekitar 220 kata tentang kinerja pengadaan tahun 2025 Badan Contoh Nasional. Fakta: 142 paket selesai; nilai kontrak Rp86 miliar; penghematan Rp7,4 miliar terhadap pagu; rata-rata proses Tender 38 hari. Tulis langsung teksnya saja.

### id-informal-pair-003

Tulis pesan berbahasa Indonesia sekitar 200 kata untuk grup kerja Divisi Pengadaan, mengingatkan dengan santai bahwa laporan bulanan dikumpulkan paling lambat Jumat pukul 15.00, dan bahwa templat baru sudah ada di folder bersama. Tulis langsung pesannya saja.

### id-informal-pair-004

Tulis pengumuman santai berbahasa Indonesia sekitar 200 kata tentang acara makan bersama akhir tahun Divisi Pengadaan pada Jumat, 18 Desember 2026, pukul 12.00 di kantin Gedung Contoh A, dengan iuran Rp50.000 yang dibayar ke Lia paling lambat 11 Desember. Tulis langsung teksnya saja.

### id-informal-pair-005

Tulis unggahan media sosial berbahasa Indonesia sekitar 200 kata dari akun Badan Contoh Nasional, dengan nada santai, mengajak pelaku usaha kecil ikut sosialisasi E-purchasing pada Rabu, 25 November 2026, pukul 13.00 WIB secara daring dan gratis. Tulis langsung unggahannya saja.

### en-formal-pair-003

Write a formal letter of about 220 words from the Contracting Officer of the Sample Agency to Fictional Supplies Inc., reference CO-2026-114, giving notice that a Performance Bond of $12,500 must be lodged by 20 November 2026 or the Letter of Award may be withdrawn. Write only the letter.

### en-formal-pair-004

Write a formal procurement notice of about 220 words for an Open Tender, reference RFP-2026-09, for security services at the Sample Agency. Facts: bids close on 4 December 2026 at 2:00 p.m.; a Bid Bond of $5,000 is required; questions are accepted until 25 November 2026. Write only the notice.

### en-formal-pair-005

Write a formal explainer of about 220 words for staff on a rule about Delegation of Authority. It must include this quotation exactly: Section 12(3) of the Sample Agency Procurement Regulation 2026 states "A delegate shall not approve a purchase in which the delegate has a Conflict of Interest." Write only the explainer.

### en-semiformal-pair-003

Write meeting notes of about 220 words for a procurement planning meeting on 3 November 2026. Facts: 6 teams attended; 2 teams have not sent proposals; the deadline moved to 17 November 2026; Dana Example will compile the results. Write only the notes.

### en-semiformal-pair-004

Write a project update of about 220 words on moving contract files to a new records system. Facts: 1,800 of 2,400 files are migrated; 45 files have missing metadata; go-live moved from 30 November to 7 December 2026. Write only the update.

### en-semiformal-pair-005

Write an internal memo of about 220 words on a changed purchase request process. From 1 December 2026, requests under $1,000 need only a team lead's approval. It has three numbered steps: (1) the team completes form PR-01; (2) the team lead approves within 2 working days; (3) the Procurement Officer processes it. Write only the memo.

### en-standard-pair-003

Write a FAQ of about 220 words for a government web page on how small businesses can register as a Vendor with the Sample Agency. Facts: registration is free; it takes up to 10 working days; a business number is required. Write only the FAQ.

### en-standard-pair-004

Write a public announcement of about 220 words from the Sample Agency saying that its vendor portal will close for maintenance on 13 November 2026 from 6 p.m. to 9 p.m., and that bids due that evening move to 16 November 2026 at noon. Write only the announcement.

### en-standard-pair-005

Write a section of about 220 words for a public annual report on procurement in 2025 at the Sample Agency. Facts: 142 packages completed; total contract value $8.6 million; savings of $740,000 against budget; an average of 38 days per tender. Write only the section.

### en-informal-pair-003

Write a blog-style post of about 220 words by a procurement officer on what they learned in their first year writing Statements of Work. Include these facts: they wrote 14 of them, and the first had to be redone twice. Write only the post.

### en-informal-pair-004

Write an item of about 200 words for a team newsletter welcoming Priya Example to Procurement on 2 November 2026 and mentioning the team's end-of-year lunch on 18 December at noon. Write only the item.

### en-informal-pair-005

Write a friendly social media post of about 180 words from the Sample Agency inviting small businesses to a free online session on selling to government, on Wednesday 25 November 2026 at 1 p.m. Write only the post.

### en-chat-pair-003

Write a Slack thread of about 180 words between Maya Example and Priya, a vendor contact at Acme Sample Ltd, about a delivery of 20 laptops due 5 November 2026 that has not arrived. Maya needs a new date by 10 November 2026. Mark each turn with the speaker's name. Write only the thread.

### en-chat-pair-004

Write a Teams thread of about 180 words between Ben Example and his manager Sara about extending the Statement of Work deadline from 14 to 21 November 2026. Mark each turn with the speaker's name. Write only the thread.

### en-chat-pair-005

Write a Slack thread of about 180 words between two teammates, Lia and Sam, splitting up the review of 3 bids before a meeting on Tuesday 17 November 2026 at 9:00 a.m. Mark each turn with the speaker's name. Write only the thread.
