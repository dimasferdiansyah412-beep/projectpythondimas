# Program Input Nilai Mahasiswa (Dictionary)
# Menu: (L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar
# Nilai akhir = 30% tugas + 35% UTS + 35% UAS

def hitung_nilai_akhir(tugas, uts, uas):
    return round((tugas * 0.30) + (uts * 0.35) + (uas * 0.35), 2)

def input_angka(prompt):
    while True:
        try:
            nilai = float(input(prompt).strip())
            if nilai < 0 or nilai > 100:
                print("Nilai harus 0–100.")
                continue
            return nilai
        except ValueError:
            print("Input harus angka yang valid.")

def lihat_data(data):
    print("\nDaftar Nilai")
    print("-" * 63)
    print("| NO | NIM     | NAMA           | TUGAS | UTS | UAS | AKHIR |")
    print("-" * 63)
    if not data:
        print("|{:^59}|".format("TIDAK ADA DATA"))
        print("-" * 63)
        return
    for i, (nim, mhs) in enumerate(data.items(), start=1):
        print(f"| {i:>2} | {nim:<7} | {mhs['nama']:<14} | "
              f"{mhs['tugas']:>5} | {mhs['uts']:>3} | {mhs['uas']:>3} | {mhs['akhir']:>5} |")
    print("-" * 63)

def tambah_data(data):
    print("\nTambah Data")
    nim = input("NIM         : ").strip()
    if nim in data:
        print("NIM sudah ada. Gunakan menu Ubah jika ingin mengubah.")
        return
    nama = input("Nama        : ").strip()
    uts = input_angka("Nilai UTS   : ")
    uas = input_angka("Nilai UAS   : ")
    tugas = input_angka("Nilai Tugas : ")

    akhir = hitung_nilai_akhir(tugas, uts, uas)
    data[nim] = {
        "nama": nama,
        "tugas": tugas,
        "uts": uts,
        "uas": uas,
        "akhir": akhir
    }
    print(f"Data untuk NIM {nim} ditambahkan.")

def ubah_data(data):
    print("\nUbah Data")
    nim = input("Masukkan NIM yang akan diubah: ").strip()
    if nim not in data:
        print("Data dengan NIM tersebut tidak ditemukan.")
        return

    mhs = data[nim]
    print(f"Data saat ini: Nama={mhs['nama']}, Tugas={mhs['tugas']}, UTS={mhs['uts']}, UAS={mhs['uas']}, Akhir={mhs['akhir']}")
    nama = input(f"Nama ({mhs['nama']})        : ").strip() or mhs['nama']

    def input_optional_angka(label, current):
        s = input(f"{label} ({current})   : ").strip()
        if s == "":
            return current
        try:
            v = float(s)
            if v < 0 or v > 100:
                print("Nilai harus 0–100. Diabaikan, gunakan nilai lama.")
                return current
            return v
        except ValueError:
            print("Input tidak valid. Diabaikan, gunakan nilai lama.")
            return current

    uts = input_optional_angka("Nilai UTS", mhs['uts'])
    uas = input_optional_angka("Nilai UAS", mhs['uas'])
    tugas = input_optional_angka("Nilai Tugas", mhs['tugas'])

    akhir = hitung_nilai_akhir(tugas, uts, uas)
    data[nim] = {"nama": nama, "tugas": tugas, "uts": uts, "uas": uas, "akhir": akhir}
    print(f"Data NIM {nim} berhasil diubah.")

def hapus_data(data):
    print("\nHapus Data")
    nim = input("Masukkan NIM yang akan dihapus: ").strip()
    if nim in data:
        del data[nim]
        print(f"Data NIM {nim} dihapus.")
    else:
        print("Data dengan NIM tersebut tidak ditemukan.")

def cari_data(data):
    print("\nCari Data")
    keyword = input("Masukkan NIM atau Nama: ").strip().lower()
    hasil = {}
    for nim, mhs in data.items():
        if keyword in nim.lower() or keyword in mhs['nama'].lower():
            hasil[nim] = mhs

    if not hasil:
        print("Data tidak ditemukan.")
        return

    print("\nHasil Pencarian")
    print("-" * 63)
    print("| NO | NIM     | NAMA           | TUGAS | UTS | UAS | AKHIR |")
    print("-" * 63)
    for i, (nim, mhs) in enumerate(hasil.items(), start=1):
        print(f"| {i:>2} | {nim:<7} | {mhs['nama']:<14} | "
              f"{mhs['tugas']:>5} | {mhs['uts']:>3} | {mhs['uas']:>3} | {mhs['akhir']:>5} |")
    print("-" * 63)

def main():
    data = {}  # Dictionary: key=NIM, value=info mahasiswa
    while True:
        print("\nProgram Input Nilai")
        print("=" * 19)
        pilihan = input("[(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari (K)eluar]: ").strip().lower()

        if pilihan == 'l':
            lihat_data(data)
        elif pilihan == 't':
            tambah_data(data)
        elif pilihan == 'u':
            ubah_data(data)
        elif pilihan == 'h':
            hapus_data(data)
        elif pilihan == 'c':
            cari_data(data)
        elif pilihan == 'k':
            print("Terima kasih. Keluar program.")
            break
        else:
            print("Pilihan tidak dikenal. Gunakan L/T/U/H/C/K.")

if __name__ == "__main__":
    main()
