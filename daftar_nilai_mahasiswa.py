# Daftar untuk menyimpan data mahasiswa
mahasiswa = []

# Fungsi untuk menambah data mahasiswa
def tambah(nama, nilai):
    mahasiswa.append({'nama': nama, 'nilai': nilai})

# Fungsi untuk menampilkan data mahasiswa
def tampilkan():
    for mhs in mahasiswa:
        print(f"Nama: {mhs['nama']}, Nilai: {mhs['nilai']}")

# Fungsi untuk menghapus data mahasiswa berdasarkan nama
def hapus(nama):
    global mahasiswa
    mahasiswa = [mhs for mhs in mahasiswa if mhs['nama'] != nama]

# Fungsi untuk mengubah data mahasiswa berdasarkan nama
def ubah(nama, nilai_baru):
    for mhs in mahasiswa:
        if mhs['nama'] == nama:
            mhs['nilai'] = nilai_baru
            break

# Contoh penggunaan fungsi
tambah("Ali", 90)
tambah("Rani", 87)
tambah("Budi", 85)
tambah("gilang", 93)
tampilkan()
print("Setelah mengubah nilai Budi:")
ubah("Budi", 95)
tampilkan()
print("Setelah menghapus data Ali:")
hapus("Ali")
tampilkan()
