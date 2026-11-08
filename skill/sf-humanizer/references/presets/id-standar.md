---
name: id-standar
lang: id
register: standar
status: ready
metrics:
  mean_sentence_length: {median: 14.75, p25: 13.9, p75: 16.59}
  light_verbs_per_100_words: {median: 0.0, p25: 0.0, p75: 0.0}
  connectors_per_100_sentences: {median: 0.0, p25: 0.0, p75: 0.0}
  nominalizations_per_100_words: {median: 10.68, p25: 6.46, p75: 11.88}
  merupakan_per_100_words: {median: 0.0, p25: 0.0, p75: 0.0}
---

## Tujuan register

Bahasa Indonesia baku dan netral untuk pembaca umum: laporan untuk publik, artikel situs instansi, pengumuman publik, ringkasan kebijakan, penjelasan, dan dokumentasi. Pembacanya orang luar yang tidak tahu konteks internal penulis. Tulisan yang menyapa rekan sekantor masuk register semiformal.

## Ciri yang dicari

- **Sapaan dan kata ganti:** "kami" untuk lembaga penulis, "Anda" bila pembaca perlu disapa langsung, atau sebut kelompoknya, misalnya "pemohon" atau "pengendara". Tidak memakai "kita", "kamu", atau "Bapak/Ibu", dan tidak menyapa rekan kerja.
- **Panjang kalimat:** kalimat lengkap dengan panjang beragam, dalam rentang p25 sampai p75 `mean_sentence_length` pada blok metrics.
- **Paragraf:** dua sampai empat kalimat. Paragraf harus dapat dipahami tanpa pengetahuan orang dalam.
- **Istilah:** istilah glosarium utuh dan dipakai konsisten. Istilah teknis dijelaskan seperlunya saat pertama muncul, dan singkatan ditulis lengkap sekali bila naskah asal memuatnya. Penjelasan tidak boleh menambah fakta.
- **Tanda baca:** tanpa em dash. Bentuk utamanya paragraf. Daftar hanya untuk syarat, langkah, atau rincian.
- **Pembuka dan penutup:** judul menyatakan isi. Kalimat pertama langsung memuat pokok, misalnya apa yang berubah dan kapan. Penutupnya hal berikutnya atau tempat bertanya, bukan ringkasan. Tidak memakai salam atau formula surat.

## Penyesuaian pola

| ID pola | Perlakuan | Alasan |
| --- | --- | --- |
| ID-11 | lebih longgar | "Adalah" wajar saat menjelaskan istilah kepada pembaca umum, walau bukan dalam Ketentuan Umum. |
| ID-07 | lebih longgar | Nomina seperti "penetapan pemenang" lazim dalam teks kebijakan. Yang dibongkar hanya rantai yang menyulitkan pembaca. |
| ID-03 | lebih ketat | Formula surat dinas tidak berlaku di sini. Bila muncul, ganti dengan pembuka yang langsung ke pokok. |
| ID-05 | lebih ketat | Artikel dan laporan rawan ditutup dengan "Capaian ini menunjukkan" atau sejenisnya tanpa fakta baru. |
| ID-06 | lebih ketat | Verba ringan paling sering muncul pada kalimat pembuka pengumuman. |
| ID-08 | lebih ketat | Pembuka berpola seperti "Dari sisi X" atau "Bagi X" yang berulang membuat artikel terdengar seperti pidato. |
| ID-14 | lebih ketat | Klaim tanpa ukuran kepada publik perlu dibuang walau berdiri sendiri. |
| ID-16 | lebih ketat | Em dash tidak muncul dalam contoh baik register ini dan selalu diganti. |

## Contoh kalimat

- "Keduanya bertujuan memperoleh barang atau jasa yang tepat, tetapi memiliki perbedaan dalam hal cara dan tingkat persaingannya." → "Keduanya bertujuan memperoleh barang atau jasa yang tepat, tetapi cara dan tingkat persaingannya berbeda."
- "Badan Contoh Nasional melakukan pembukaan pendaftaran calon Penyedia pada 1 sampai 15 Desember 2026." → "Badan Contoh Nasional membuka pendaftaran calon Penyedia pada 1 sampai 15 Desember 2026."
- "Dari sisi waktu, rata-rata proses Tender berlangsung selama 38 hari" → "Rata-rata proses Tender berlangsung selama 38 hari"

## Batas

- Jangan bernada percakapan atau akrab, dan jangan bernada surat dinas.
- Jangan mengandaikan pembaca tahu nama unit, sistem, atau kebiasaan internal. Bila naskah tidak menjelaskannya, ajukan titik konfirmasi.
- Jangan menambahkan definisi, contoh, atau dasar hukum yang tidak ada di naskah asal.
- Jangan mengubah kata wajib, dapat, atau dianjurkan pada pengumuman dan kebijakan.
- Jangan menjadikan klaim lembaga lebih positif atau lebih tegas daripada aslinya.

## Rujukan

belum ada rujukan berlisensi jelas
