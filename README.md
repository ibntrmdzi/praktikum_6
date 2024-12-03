# praktikum_6

Nama: Muhamad Rizki Wahyu Saputra

NIM: 312410534

Kelas: TI.24.A.5

## Penjelasan programnya

1. Daftar untuk menyimpan data mahasiswa:

```python
mahasiswa = []
```

Di sini, kita membuat sebuah list kosong bernama mahasiswa. List ini akan digunakan untuk menyimpan data mahasiswa dalam bentuk dictionary.

2.  Fungsi untuk menambah data mahasiswa:

```python
def tambah(nama, nilai):
    mahasiswa.append({'nama': nama, 'nilai': nilai})
```

Fungsi ini akan mencetak nama dan nilai dari setiap mahasiswa di dalam list.

3.  Fungsi untuk menghapus data mahasiswa berdasarkan nama:

```python
def tampilkan():
    for mhs in mahasiswa:
        print(f"Nama: {mhs['nama']}, Nilai: {mhs['nilai']}")
```

Fungsi tampilkan digunakan untuk mencetak semua data mahasiswa yang ada di dalam list mahasiswa. Fungsi ini akan mencetak nama dan nilai dari setiap mahasiswa di dalam list.

4.  Fungsi untuk menghapus data mahasiswa berdasarkan nama:

```python
def hapus(nama):
    global mahasiswa
    mahasiswa = [mhs for mhs in mahasiswa if mhs['nama'] != nama]
```

Fungsi hapus menerima satu parameter, yaitu nama. Fungsi ini menghapus data mahasiswa dari list mahasiswa berdasarkan nama yang diberikan. Menggunakan list comprehension, fungsi ini membuat list baru yang hanya berisi mahasiswa yang namanya tidak sama dengan nama yang diberikan.

5.  Fungsi untuk mengubah data mahasiswa berdasarkan nama:

```python
def ubah(nama, nilai_baru):
    for mhs in mahasiswa:
        if mhs['nama'] == nama:
            mhs['nilai'] = nilai_baru
            break
```

Fungsi ubah menerima dua parameter, yaitu nama dan nilai_baru. Fungsi ini mencari mahasiswa berdasarkan nama yang diberikan dan mengubah nilainya dengan nilai_baru.

6.  Contoh penggunaan fungsi:

```python
tambah("Ali", 90)
tambah("Rani", 87)
tambah("Budi", 85)
tambah("Gilang", 93)
tampilkan()
print("Setelah mengubah nilai Budi:")
ubah("Budi", 95)
tampilkan()
print("Setelah menghapus data Ali:")
hapus("Ali")
tampilkan()
```
Pertama, kita menambahkan beberapa data mahasiswa menggunakan fungsi tambah.

Kemudian, kita menampilkan semua data mahasiswa yang telah ditambahkan.

Setelah itu, kita mengubah nilai mahasiswa bernama Budi dan menampilkannya kembali untuk melihat perubahan.

Terakhir, kita menghapus data mahasiswa bernama Ali dan menampilkan data mahasiswa yang tersisa.

Program ini memperlihatkan bagaimana kita bisa menambah, menampilkan, mengubah, dan menghapus data mahasiswa menggunakan fungsi-fungsi yang telah dibuat.
