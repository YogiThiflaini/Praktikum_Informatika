# 1. LIST (Berurutan, bisa diubah / mutable)
hobi = ["Membaca", "Koding", "Berenang"]
print("List Hobi:", hobi)
print("Tipe:", type(hobi))

# 2. TUPLE (Berurutan, tidak bisa diubah / immutable)
koordinat = (-6.1751, 106.8650)
print("Tuple Koordinat:", koordinat)
print("Tipe:", type(koordinat))

# 3. DICTIONARY (Pasangan Key : Value)
mahasiswa = {
    "nama": "Siti",
    "nim": "123456",
    "ipk": 3.85
}
print("Dict Mahasiswa:", mahasiswa)
print("Nama Mahasiswa:", mahasiswa["nama"])
print("Tipe:", type(mahasiswa))

# 4. SET (Nilai unik, tidak menyimpan duplikat)
angka_unik = {1, 2, 2, 3, 4, 4, 5}
print("Set Angka Unik (otomatis menghapus duplikat):", angka_unik)
print("Tipe:", type(angka_unik))
