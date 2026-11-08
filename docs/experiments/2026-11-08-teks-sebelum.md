# Percobaan pembuatan teks "sebelum", 8 November 2026

## Tujuan

Pasangan sampel memerlukan teks "sebelum" yang memuat pola katalog, minimal 4 pola per teks (target percobaan: 3 untuk register informal dan chat), dengan fakta yang sama seperti teks "sesudah". Percobaan ini menguji apakah teks seperti itu bisa diperoleh dari model tanpa menyisipkan pola secara manual.

## Metode dan hasil

Jumlah pola dihitung oleh peninjau Claude terhadap katalog `patterns-*.md`. Angka ini penilaian model, bukan pengukuran pasti.

| Metode | Teks | Rata-rata pola | Penyimpangan fakta |
| --- | --- | --- | --- |
| Model kecil, prompt polos dengan daftar fakta lengkap | 54 | 0,28 | 19 dari 54 teks |
| Model kecil, tabel fakta, arahan menulis seperti asisten AI umum | 54 | 0,56 | 40 dari 54 teks |
| Model terkuat, tabel fakta, permintaan polos | 6 | 0,33 | Kecil, angka semuanya cocok |
| Model terkuat, permintaan satu baris dengan poin singkat | 6 | 0,17 | 5 dari 6 teks menambah isi |
| Penyisipan pola ke teks "sesudah" (dipakai) | 54 | minimal 4 | Fakta sama karena disusun dari teks "sesudah" |

Dorongan netral "buat lengkap dan profesional" juga dicoba pada 6 teks metode pertama. Empat teks yang dibaca tetap nyaris sama dengan teks "sesudah".

Sebagai pembanding, penilai yang sama menilai secara buta dua teks versi penyisipan dan dua teks model kecil dari tabel fakta. Versi penyisipan mendapat 5 dan 6 pola, sedangkan teks model kecil mendapat 0 dan 1 pola. Jadi penilaiannya tidak terlalu ketat sampai pola tidak terdeteksi.

Pada metode terkuat dengan permintaan singkat, semua teks di bawah 150 kata. Empat surel hanya 50 sampai 94 kata.

## Kesimpulan

Model yang diuji, bila diberi fakta yang jelas, menulis teks kerja yang bersih dan hampir tanpa pola katalog. Karena itu katalog belum tervalidasi terhadap teks AI yang benar-benar diterima pengguna. Bisa jadi pola ini lebih sering muncul pada model atau alat lain, atau pada permintaan yang berbeda.

Teks "sebelum" yang dipakai adalah versi penyisipan. Polanya sengaja dimasukkan, sehingga sebagian terasa dibuat-buat dan polanya lebih mudah dikenali daripada keluaran AI yang sebenarnya.

## Langkah berikutnya

Kumpulkan keluaran AI asli yang sudah dianonimkan, lalu validasi dan sesuaikan katalog berdasarkan pola yang benar-benar muncul.
