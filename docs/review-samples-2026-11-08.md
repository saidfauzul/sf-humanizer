# Tinjauan kualitas sampel, 8 November 2026

Seluruh 88 sampel dibaca dan dinilai oleh peninjau Claude per bahasa dan register, lalu berkas yang berubah dibaca ulang oleh peninjau baru. Sebagian berkas diperiksa juga secara acak (11 berkas dari 11 preset). Belum ada penutur manusia yang meninjau korpus ini.

Hasil: 21 ok, 13 revised, 54 regenerated. Pada tinjauan kedua, 18 dari 67 berkas masih dikoreksi (5 Indonesia, 13 Inggris).

## Masalah yang berulang

- **Teks "sebelum" terlalu lemah.** Keluaran model untuk prompt polos hanya memuat sedikit pola katalog, jadi 54 teks dibuat ulang dengan minimal 4 pola, dan catatannya kini menyebut letak setiap pola.
- **Bahasa percakapan dalam register baku.** Contoh: "lebih dulu" dan "Begitu sanggah masuk" pada teks formal. Diganti bentuk baku.
- **Permintaan yang janggal atau terlalu ketus.** Contoh: "kami mohon pembahasannya teliti" dan "Cantumkan tanggal pengiriman" kepada direktur. Diperhalus sesuai hubungan.
- **Kalke dan subjek yang tidak logis.** Contoh: "setiap metode punya tempat sendiri" dan "Bila pemeriksaan menemukan". Disusun ulang.
- **Pola yang hanya ditukar, bukan diperbaiki.** Contoh: "merupakan" menjadi "adalah", dan verba ringan yang masih tersisa. Catatan disesuaikan dengan yang benar-benar diperbaiki.
- **Nada surel dalam chat.** Salam pembuka dan kalimat panjang pada utas chat dipangkas.
- **Nama dan pembuka yang berulang dalam satu preset.** Nama fiktif dan pembuka divariasikan.
- **Fakta yang muncul hanya di satu sisi.** Satu kalimat di `en-standard-pair-003` dihapus. Kalimat melingkar di `en-formal-pair-004` juga dihapus, sehingga teks itu tidak lagi menyebut cara memperoleh dokumen tender.

## Keterbatasan yang masih ada

- Semua teks tetap buatan model dan bertanda `synthetic`. Penilaian kualitas ini juga dilakukan model.
- Teks "sebelum" yang dibuat ulang memuat pola yang sengaja disisipkan ke teks "sesudah". Sebagian terasa dibuat-buat, misalnya pembuka formula dalam pesan santai, dan polanya lebih mudah dikenali daripada keluaran model yang sebenarnya.
- `en-chat-pair-001` dan `en-chat-pair-002` masih panjang untuk chat, karena harus memuat semua fakta dan minimal 150 kata.
- `id-standar-pair-001` mendefinisikan Pengadaan Langsung dengan ciri yang lebih dekat ke Penunjukan Langsung (menunjuk satu penyedia, kebutuhan mendesak). Isinya dibiarkan karena fakta dikunci, dan perlu diperiksa pemilik repo.
- `en-standard-pair-001` memakai "Framework Agreement" dan "framework agreements" pada teks yang sama. Ini perlu dikonfirmasi.

## Per berkas

| Berkas | Vonis | Perubahan |
| --- | --- | --- |
| `en/chat/good/en-chat-good-001.md` | ok | Tidak ada perubahan. |
| `en/chat/good/en-chat-good-002.md` | ok | Tidak ada perubahan. |
| `en/chat/good/en-chat-good-003.md` | ok | Tidak ada perubahan. |
| `en/chat/pairs/en-chat-pair-001.md` | regenerated | Teks sebelum dibuat ulang agar memuat minimal 4 pola; teks sesudah juga diperbaiki. Catatan diperinci. |
| `en/chat/pairs/en-chat-pair-002.md` | regenerated | Teks sebelum dibuat ulang agar memuat minimal 4 pola; teks sesudah juga diperbaiki. Catatan diperinci. |
| `en/chat/pairs/en-chat-pair-003.md` | regenerated | Teks sebelum dibuat ulang agar memuat minimal 4 pola; teks sesudah juga diperbaiki. Catatan diperinci. |
| `en/chat/pairs/en-chat-pair-004.md` | regenerated | Teks sebelum dibuat ulang agar memuat minimal 4 pola; teks sesudah juga diperbaiki. Catatan diperinci. |
| `en/chat/pairs/en-chat-pair-005.md` | regenerated | Teks sebelum dibuat ulang agar memuat minimal 4 pola; teks sesudah juga diperbaiki. Catatan diperinci. |
| `en/email/good/en-email-good-001.md` | ok | Tidak ada perubahan. |
| `en/email/good/en-email-good-002.md` | revised | Bahasa atau register diperbaiki. |
| `en/email/good/en-email-good-003.md` | ok | Tidak ada perubahan. |
| `en/email/pairs/en-email-pair-001.md` | regenerated | Teks sebelum dibuat ulang agar memuat minimal 4 pola; teks sesudah juga diperbaiki. Catatan diperinci. |
| `en/email/pairs/en-email-pair-002.md` | regenerated | Teks sebelum dibuat ulang agar memuat minimal 4 pola; teks sesudah tetap. Catatan diperinci. |
| `en/email/pairs/en-email-pair-003.md` | regenerated | Teks sebelum dibuat ulang agar memuat minimal 4 pola; teks sesudah juga diperbaiki. Catatan diperinci. |
| `en/email/pairs/en-email-pair-004.md` | regenerated | Teks sebelum dibuat ulang agar memuat minimal 4 pola; teks sesudah juga diperbaiki. Catatan diperinci. |
| `en/email/pairs/en-email-pair-005.md` | regenerated | Teks sebelum dibuat ulang agar memuat minimal 4 pola; teks sesudah juga diperbaiki. Catatan diperinci. |
| `en/formal/good/en-formal-good-001.md` | ok | Tidak ada perubahan. |
| `en/formal/good/en-formal-good-002.md` | ok | Tidak ada perubahan. |
| `en/formal/good/en-formal-good-003.md` | ok | Tidak ada perubahan. |
| `en/formal/pairs/en-formal-pair-001.md` | regenerated | Teks sebelum dibuat ulang agar memuat minimal 4 pola; teks sesudah tetap. Catatan diperinci. |
| `en/formal/pairs/en-formal-pair-002.md` | regenerated | Teks sebelum dibuat ulang agar memuat minimal 4 pola; teks sesudah tetap. Catatan diperinci. |
| `en/formal/pairs/en-formal-pair-003.md` | regenerated | Teks sebelum dibuat ulang agar memuat minimal 4 pola; teks sesudah tetap. Catatan diperinci. |
| `en/formal/pairs/en-formal-pair-004.md` | regenerated | Teks sebelum dibuat ulang agar memuat minimal 4 pola; teks sesudah juga diperbaiki. Catatan diperinci. |
| `en/formal/pairs/en-formal-pair-005.md` | regenerated | Teks sebelum dibuat ulang agar memuat minimal 4 pola; teks sesudah juga diperbaiki. Catatan diperinci. |
| `en/informal/good/en-informal-good-001.md` | ok | Tidak ada perubahan. |
| `en/informal/good/en-informal-good-002.md` | ok | Tidak ada perubahan. |
| `en/informal/good/en-informal-good-003.md` | ok | Tidak ada perubahan. |
| `en/informal/pairs/en-informal-pair-001.md` | regenerated | Teks sebelum dibuat ulang agar memuat minimal 4 pola; teks sesudah juga diperbaiki. Catatan diperinci. |
| `en/informal/pairs/en-informal-pair-002.md` | regenerated | Teks sebelum dibuat ulang agar memuat minimal 4 pola; teks sesudah juga diperbaiki. Catatan diperinci. |
| `en/informal/pairs/en-informal-pair-003.md` | regenerated | Teks sebelum dibuat ulang agar memuat minimal 4 pola; teks sesudah juga diperbaiki. Catatan diperinci. |
| `en/informal/pairs/en-informal-pair-004.md` | regenerated | Teks sebelum dibuat ulang agar memuat minimal 4 pola; teks sesudah juga diperbaiki. Catatan diperinci. |
| `en/informal/pairs/en-informal-pair-005.md` | regenerated | Teks sebelum dibuat ulang agar memuat minimal 4 pola; teks sesudah tetap. Catatan diperinci. |
| `en/semiformal/good/en-semiformal-good-001.md` | ok | Tidak ada perubahan. |
| `en/semiformal/good/en-semiformal-good-002.md` | ok | Tidak ada perubahan. |
| `en/semiformal/good/en-semiformal-good-003.md` | revised | Bahasa atau register diperbaiki. |
| `en/semiformal/pairs/en-semiformal-pair-001.md` | regenerated | Teks sebelum dibuat ulang agar memuat minimal 4 pola; teks sesudah tetap. Catatan diperinci. |
| `en/semiformal/pairs/en-semiformal-pair-002.md` | regenerated | Teks sebelum dibuat ulang agar memuat minimal 4 pola; teks sesudah tetap. Catatan diperinci. |
| `en/semiformal/pairs/en-semiformal-pair-003.md` | regenerated | Teks sebelum dibuat ulang agar memuat minimal 4 pola; teks sesudah tetap. Catatan diperinci. |
| `en/semiformal/pairs/en-semiformal-pair-004.md` | regenerated | Teks sebelum dibuat ulang agar memuat minimal 4 pola; teks sesudah juga diperbaiki. Catatan diperinci. |
| `en/semiformal/pairs/en-semiformal-pair-005.md` | regenerated | Teks sebelum dibuat ulang agar memuat minimal 4 pola; teks sesudah juga diperbaiki. Catatan diperinci. |
| `en/standard/good/en-standard-good-001.md` | ok | Tidak ada perubahan. |
| `en/standard/good/en-standard-good-002.md` | revised | Bahasa atau register diperbaiki. |
| `en/standard/good/en-standard-good-003.md` | revised | Bahasa atau register diperbaiki. |
| `en/standard/pairs/en-standard-pair-001.md` | regenerated | Teks sebelum dibuat ulang agar memuat minimal 4 pola; teks sesudah tetap. Catatan diperinci. |
| `en/standard/pairs/en-standard-pair-002.md` | regenerated | Teks sebelum dibuat ulang agar memuat minimal 4 pola; teks sesudah juga diperbaiki. Catatan diperinci. |
| `en/standard/pairs/en-standard-pair-003.md` | regenerated | Teks sebelum dibuat ulang agar memuat minimal 4 pola; teks sesudah juga diperbaiki. Catatan diperinci. |
| `en/standard/pairs/en-standard-pair-004.md` | regenerated | Teks sebelum dibuat ulang agar memuat minimal 4 pola; teks sesudah juga diperbaiki. Catatan diperinci. |
| `en/standard/pairs/en-standard-pair-005.md` | regenerated | Teks sebelum dibuat ulang agar memuat minimal 4 pola; teks sesudah juga diperbaiki. Catatan diperinci. |
| `id/email/good/id-email-good-001.md` | revised | Bahasa atau register diperbaiki. |
| `id/email/good/id-email-good-002.md` | revised | Bahasa atau register diperbaiki. |
| `id/email/good/id-email-good-003.md` | ok | Tidak ada perubahan. |
| `id/email/pairs/id-email-pair-001.md` | regenerated | Teks sebelum dibuat ulang agar memuat minimal 4 pola; teks sesudah juga diperbaiki. Catatan diperinci. |
| `id/email/pairs/id-email-pair-002.md` | regenerated | Teks sebelum dibuat ulang agar memuat minimal 4 pola; teks sesudah tetap. Catatan diperinci. |
| `id/email/pairs/id-email-pair-003.md` | regenerated | Teks sebelum dibuat ulang agar memuat minimal 4 pola; teks sesudah juga diperbaiki. Catatan diperinci. |
| `id/email/pairs/id-email-pair-004.md` | regenerated | Teks sebelum dibuat ulang agar memuat minimal 4 pola; teks sesudah juga diperbaiki. Catatan diperinci. |
| `id/email/pairs/id-email-pair-005.md` | regenerated | Teks sebelum dibuat ulang agar memuat minimal 4 pola; teks sesudah juga diperbaiki. Catatan diperinci. |
| `id/formal/good/id-formal-good-001.md` | revised | Bahasa atau register diperbaiki. |
| `id/formal/good/id-formal-good-002.md` | revised | Bahasa atau register diperbaiki. |
| `id/formal/good/id-formal-good-003.md` | revised | Bahasa atau register diperbaiki. |
| `id/formal/pairs/id-formal-pair-001.md` | regenerated | Teks sebelum dibuat ulang agar memuat minimal 4 pola; teks sesudah juga diperbaiki. Catatan diperinci. |
| `id/formal/pairs/id-formal-pair-002.md` | regenerated | Teks sebelum dibuat ulang agar memuat minimal 4 pola; teks sesudah juga diperbaiki. Catatan diperinci. |
| `id/formal/pairs/id-formal-pair-003.md` | regenerated | Teks sebelum dibuat ulang agar memuat minimal 4 pola; teks sesudah juga diperbaiki. Catatan diperinci. |
| `id/formal/pairs/id-formal-pair-004.md` | regenerated | Teks sebelum dibuat ulang agar memuat minimal 4 pola; teks sesudah juga diperbaiki. Catatan diperinci. |
| `id/formal/pairs/id-formal-pair-005.md` | regenerated | Teks sebelum dibuat ulang agar memuat minimal 4 pola; teks sesudah tetap. Catatan diperinci. |
| `id/informal/good/id-informal-good-001.md` | ok | Tidak ada perubahan. |
| `id/informal/good/id-informal-good-002.md` | revised | Bahasa atau register diperbaiki. |
| `id/informal/good/id-informal-good-003.md` | revised | Bahasa atau register diperbaiki. |
| `id/informal/pairs/id-informal-pair-001.md` | regenerated | Teks sebelum dibuat ulang agar memuat minimal 4 pola; teks sesudah juga diperbaiki. Catatan diperinci. |
| `id/informal/pairs/id-informal-pair-002.md` | regenerated | Teks sebelum dibuat ulang agar memuat minimal 4 pola; teks sesudah juga diperbaiki. Catatan diperinci. |
| `id/informal/pairs/id-informal-pair-003.md` | regenerated | Teks sebelum dibuat ulang agar memuat minimal 4 pola; teks sesudah tetap. Catatan diperinci. |
| `id/informal/pairs/id-informal-pair-004.md` | regenerated | Teks sebelum dibuat ulang agar memuat minimal 4 pola; teks sesudah juga diperbaiki. Catatan diperinci. |
| `id/informal/pairs/id-informal-pair-005.md` | regenerated | Teks sebelum dibuat ulang agar memuat minimal 4 pola; teks sesudah juga diperbaiki. Catatan diperinci. |
| `id/semiformal/good/id-semiformal-good-001.md` | ok | Tidak ada perubahan. |
| `id/semiformal/good/id-semiformal-good-002.md` | ok | Tidak ada perubahan. |
| `id/semiformal/good/id-semiformal-good-003.md` | revised | Bahasa atau register diperbaiki. |
| `id/semiformal/pairs/id-semiformal-pair-001.md` | regenerated | Teks sebelum dibuat ulang agar memuat minimal 4 pola; teks sesudah juga diperbaiki. Catatan diperinci. |
| `id/semiformal/pairs/id-semiformal-pair-002.md` | regenerated | Teks sebelum dibuat ulang agar memuat minimal 4 pola; teks sesudah tetap. Catatan diperinci. |
| `id/semiformal/pairs/id-semiformal-pair-003.md` | regenerated | Teks sebelum dibuat ulang agar memuat minimal 4 pola; teks sesudah tetap. Catatan diperinci. |
| `id/semiformal/pairs/id-semiformal-pair-004.md` | regenerated | Teks sebelum dibuat ulang agar memuat minimal 4 pola; teks sesudah juga diperbaiki. Catatan diperinci. |
| `id/semiformal/pairs/id-semiformal-pair-005.md` | regenerated | Teks sebelum dibuat ulang agar memuat minimal 4 pola; teks sesudah juga diperbaiki. Catatan diperinci. |
| `id/standar/good/id-standar-good-001.md` | ok | Tidak ada perubahan. |
| `id/standar/good/id-standar-good-002.md` | ok | Tidak ada perubahan. |
| `id/standar/good/id-standar-good-003.md` | ok | Tidak ada perubahan. |
| `id/standar/pairs/id-standar-pair-001.md` | regenerated | Teks sebelum dibuat ulang agar memuat minimal 4 pola; teks sesudah juga diperbaiki. Catatan diperinci. |
| `id/standar/pairs/id-standar-pair-002.md` | revised | Pembuka divariasikan pada kedua sisi, verba ringan diperbaiki, catatan diperinci. |
| `id/standar/pairs/id-standar-pair-003.md` | regenerated | Teks sebelum dibuat ulang agar memuat minimal 4 pola; teks sesudah tetap. Catatan diperinci. |
| `id/standar/pairs/id-standar-pair-004.md` | regenerated | Teks sebelum dibuat ulang agar memuat minimal 4 pola; teks sesudah juga diperbaiki. Catatan diperinci. |
| `id/standar/pairs/id-standar-pair-005.md` | regenerated | Teks sebelum dibuat ulang agar memuat minimal 4 pola; teks sesudah juga diperbaiki. Catatan diperinci. |
