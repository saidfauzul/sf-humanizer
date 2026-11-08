---
name: id-formal
lang: id
register: formal
status: ready
metrics:
  mean_sentence_length: {median: 15.13, p25: 12.28, p75: 16.05}
  light_verbs_per_100_words: {median: 0.0, p25: 0.0, p75: 0.0}
  connectors_per_100_sentences: {median: 0.0, p25: 0.0, p75: 1.78}
  nominalizations_per_100_words: {median: 8.39, p25: 6.98, p75: 11.73}
  merupakan_per_100_words: {median: 0.0, p25: 0.0, p75: 0.0}
---

## Tujuan register

Naskah kedinasan dan regulasi: surat dinas, nota dinas, undangan resmi, pengumuman berformat resmi, SOP, peraturan, dan laporan pengadaan. Pembacanya pejabat, unit kerja, atau Penyedia yang memakai naskah itu sebagai dasar tindakan, sehingga ketepatan dan susunan naskah lebih diutamakan daripada kelancaran bunyi.

## Ciri yang dicari

- **Sapaan dan kata ganti:** "Saudara" untuk penerima, "kami" untuk instansi atau unit penulis. "Bapak/Ibu" dipertahankan bila sudah ada di naskah asal. Tidak memakai "kita", "Anda", atau "kamu". SOP dan peraturan menyebut pelaku dengan nama jabatan.
- **Panjang kalimat:** kalimat lengkap dalam rentang p25 sampai p75 `mean_sentence_length` pada blok metrics, dengan variasi mengikuti isi. Nilai `nominalizations_per_100_words` yang tinggi wajar di register ini.
- **Paragraf:** satu pokok per paragraf, umumnya dua sampai empat kalimat.
- **Istilah:** istilah glosarium dan nama jabatan utuh, termasuk huruf kapitalnya. Istilah pengadaan tidak perlu dijelaskan kepada pembaca naskah. Singkatan mengikuti naskah asal.
- **Tanda baca:** tanpa em dash. Butir bernomor hanya untuk langkah, syarat, lampiran, dan pasal. Rincian hari, waktu, dan tempat boleh disusun berkolom.
- **Pembuka dan penutup:** surat dan nota dinas mengikuti kepala naskah (Nomor, Yth., Dari, Hal, Tanggal), lalu "Dengan hormat," bila ada. Penutupnya "Demikian disampaikan" atau "Atas perhatian Saudara, kami ucapkan terima kasih", lalu jabatan dan nama. SOP, peraturan, dan laporan tidak memakai salam.

## Penyesuaian pola

| ID pola | Perlakuan | Alasan |
| --- | --- | --- |
| ID-03 | dikecualikan | "Dengan hormat", "Sehubungan dengan", dan "Demikian disampaikan" adalah bagian susunan tata naskah dinas bila berada pada tempatnya. Pembuka generik seperti "Di era" tetap ditindak. |
| ID-11 | dikecualikan | "Merupakan" dan "adalah" boleh dalam definisi. Di luar definisi, kata ini tetap ditindak. |
| ID-01 | lebih longgar | Pasif tunggal lazim dalam naskah resmi, terutama bila pelakunya sudah jelas. Pasif berlapis, "yang mana", dan "dalam rangka untuk" tetap ditindak. |
| ID-07 | lebih longgar | Nomina seperti "penyusunan RUP" wajar dalam gaya kedinasan. Yang dibongkar hanya rantai tiga nomina atau lebih. |
| ID-10 | lebih longgar | Rincian berkolom dan butir bernomor adalah bentuk baku naskah. |
| ID-06 | lebih ketat | Verba ringan hampir tidak ada dalam contoh baik. |
| ID-14 | lebih ketat | Penguat tanpa ukuran seperti "sangat krusial" ditindak walau berdiri sendiri, karena naskah resmi bersandar pada ketentuan dan angka. |
| ID-16 | lebih ketat | Em dash tidak lazim dalam naskah dinas dan selalu diganti. |

## Contoh kalimat

- "Perlu digarisbawahi bahwa data tersebut kami mohon dapat kami terima paling lambat 20 November 2026" → "Kami mohon data tersebut dapat kami terima paling lambat 20 November 2026"
- "PPK wajib melakukan pengembalian tagihan kepada Penyedia" → "PPK wajib mengembalikan tagihan kepada Penyedia"
- "Dalam rangka untuk menjaga akuntabilitas dan transparansi pengadaan, seluruh pegawai yang terlibat dalam kegiatan pengadaan barang/jasa wajib melakukan penandatanganan Pakta Integritas." → "Untuk menjaga akuntabilitas dan transparansi pengadaan, seluruh pegawai yang terlibat dalam kegiatan pengadaan barang/jasa wajib menandatangani Pakta Integritas."

## Batas

- Jangan menjadikan naskah bernada percakapan: tanpa kata tidak baku, sapaan akrab, atau kalimat pendek bergaya slogan.
- Jangan mengubah susunan kepala naskah, urutan bagian, atau blok tanda tangan.
- Jangan menambahkan formula yang tidak ada di naskah asal.
- Jangan mengubah pasif menjadi aktif bila pelakunya harus diterka.
- Preset ini menjaga susunan yang sudah ada. Preset ini tidak menilai kesesuaian naskah dengan aturan tata naskah dinas.

## Rujukan

- Peraturan ANRI No. 5 Tahun 2021 tentang tata naskah dinas, hanya untuk format naskah (https://peraturan.bpk.go.id/Details/173489/peraturan-anri-no-5-tahun-2021). Status lisensi: tidak ada Hak Cipta atas dasar UU 28/2014 Pasal 42 huruf b; halaman sumber tidak memuat lisensi, dan cakupan Pasal 42 untuk peraturan lembaga belum ditelaah secara hukum. Teksnya tidak disalin.
