# projectpythondimas
🔹 Fungsi hitung_nilai_akhir(tugas, uts, uas)
Tujuan: Menghitung nilai akhir mahasiswa.

Rumus:

Nilai Akhir
=
(
30
%
⋅
Tugas
)
+
(
35
%
⋅
UTS
)
+
(
35
%
⋅
UAS
)
Output: Nilai akhir dibulatkan 2 angka desimal.

🔹 Fungsi input_angka(prompt)
Tujuan: Meminta input angka dari user dengan validasi.

Validasi:

Harus berupa angka (float).

Harus dalam rentang 0–100.

Looping: Jika salah, akan terus meminta input sampai benar.

🔹 Fungsi lihat_data(data)
Tujuan: Menampilkan seluruh data mahasiswa dalam bentuk tabel.

Format: Ada header tabel (NO, NIM, Nama, Tugas, UTS, UAS, Akhir).

Jika kosong: Menampilkan pesan "TIDAK ADA DATA".

🔹 Fungsi tambah_data(data)
Tujuan: Menambahkan data mahasiswa baru.

Langkah:

Input NIM → dicek apakah sudah ada.

Input Nama, Nilai UTS, UAS, Tugas.

Hitung nilai akhir dengan hitung_nilai_akhir.

Simpan ke dictionary data dengan key = NIM.

🔹 Fungsi ubah_data(data)
Tujuan: Mengubah data mahasiswa berdasarkan NIM.

Langkah:

Input NIM → dicek apakah ada.

Tampilkan data lama.

User bisa mengganti Nama, Tugas, UTS, UAS (atau biarkan kosong untuk tetap sama).

Hitung ulang nilai akhir.

Update dictionary.

🔹 Fungsi hapus_data(data)
Tujuan: Menghapus data mahasiswa berdasarkan NIM.

Langkah:

Input NIM.

Jika ada → hapus dari dictionary.

Jika tidak ada → tampilkan pesan error.

🔹 Fungsi cari_data(data)
Tujuan: Mencari data mahasiswa berdasarkan NIM atau Nama.

Langkah:

Input keyword.

Cocokkan dengan NIM atau Nama (case-insensitive).

Jika ada → tampilkan hasil pencarian dalam format tabel.

Jika tidak ada → tampilkan pesan "Data tidak ditemukan."

🔹 Fungsi main()
Tujuan: Menjalankan menu utama program.

Menu tersedia:

(L) → Lihat data

(T) → Tambah data

(U) → Ubah data

(H) → Hapus data

(C) → Cari data

(K) → Keluar

Looping: Program berjalan terus sampai user memilih K.

🔹 Struktur Data
Data disimpan dalam dictionary dengan format:

python
data = {
    "NIM001": {
        "nama": "Budi",
        "tugas": 80,
        "uts": 75,
        "uas": 85,
        "akhir": 80.5
    },
    "NIM002": {
        "nama": "Siti",
        "tugas": 90,
        "uts": 88,
        "uas": 92,
        "akhir": 90.1
    }
}
✨ Jadi, program ini adalah sistem CRUD (Create, Read, Update, Delete) sederhana untuk data nilai mahasiswa, dengan tambahan fitur pencarian.

Mau saya buatkan diagram alur (flowchart) supaya lebih mudah dipahami aliran programnya?
