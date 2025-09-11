# 📑 PDF Tools – Aplikasi Bantu Upload Skripsi ke Repository

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://pdf-tools-s.streamlit.app/)

🔗 **Coba langsung aplikasi di sini:** [PDF Tools Online](https://pdf-tools-s.streamlit.app/)

---

## 📝 Latar Belakang

Mahasiswa akhir biasanya diwajibkan **unggah mandiri skripsi/tugas akhir** ke repository perpustakaan kampus.
Namun sebelum upload, ada syarat yang harus dipenuhi, seperti:

* File harus dalam format PDF.
* Harus diberi **watermark logo kampus**.
* File tidak boleh melebihi ukuran tertentu.
* File harus sudah melewati cek plagiarisme < 25%.
* Dokumen dipecah menjadi beberapa bagian (Cover, Lembar Pengesahan, Abstrak, Bab I, Skripsi Full, dll).

Aplikasi **PDF Tools** ini dibuat untuk memudahkan mahasiswa mengolah file PDF mereka sesuai persyaratan kampus.

---

## ⚙️ Fitur Utama

1. 🗑️ **Kelola Halaman PDF**

   * Menghapus halaman yang tidak diperlukan.
   * Mengatur ulang posisi halaman.
   * Memilih halaman tertentu untuk disimpan.

2. 💧 **Tambah Watermark**

   * Menambahkan watermark (misalnya logo kampus) ke semua halaman PDF.

3. 📚 **Gabung PDF**

   * Menggabungkan beberapa file PDF menjadi satu dokumen.
   * Bisa mengatur urutan file sebelum digabungkan.

4. ✂️ **Hapus Watermark**

   * Menghapus watermark tertentu (misalnya watermark CamScanner).
   * Bisa juga melakukan crop bagian bawah dokumen untuk membersihkan tanda.

---

## 🚀 Cara Menjalankan (Lokal)

1. **Clone repository** ini atau unduh sebagai `.zip`.
2. Pastikan Python 3.8+ sudah terinstal.
3. Install dependencies dengan:

   ```bash
   pip install -r requirements.txt
   ```
4. Jalankan aplikasi dengan perintah:

   ```bash
   streamlit run main.py
   ```
5. Buka browser pada alamat: [http://localhost:8501](http://localhost:8501)

---

## 📂 Struktur File

```
📑 pdf-tools/
│── main.py                   # File utama (navigasi sidebar & UI)
│── app_kelola_halaman.py      # Fitur kelola halaman PDF
│── app_tambah_watermark.py    # Fitur tambah watermark
│── app_gabung_pdf.py          # Fitur gabung PDF
│── app_hapus_watermark.py     # Fitur hapus watermark
│── requirements.txt           # Daftar dependencies
│── README.md                  # Dokumentasi proyek
```

---

## 🎯 Contoh Alur Penggunaan

1. Scan dokumen skripsi kamu → hasilnya dalam bentuk PDF.
2. Gunakan **Kelola Halaman** untuk menghapus atau mengatur halaman.
3. Tambahkan watermark logo kampus menggunakan **Tambah Watermark**.
4. Jika file tersebar dalam beberapa dokumen (Cover, Abstrak, Bab I, dll) → gunakan **Gabung PDF**.
5. Jika ada watermark dari aplikasi scanner → hapus dengan **Hapus Watermark**.
6. Setelah selesai, file siap diunggah ke **repository kampus** sesuai persyaratan.

---

## 👨‍💻 Dibuat Oleh

**Sendhy Maula Ammarulloh – 2025**
Sebagai solusi praktis untuk mahasiswa akhir dalam menyiapkan file skripsi sebelum upload ke repository perpustakaan.
