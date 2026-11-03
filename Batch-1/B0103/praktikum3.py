# 1. Membuat variabel profil karakter
nama_hero = "Arthas"
level = 10
hp = 95.5
is_alive = True

inventory = ["Pedang", "Busur", "Perisai"]

atribut = {
    "kekuatan": 80,
    "kelincahan": 65
}

# 2. Menampilkan informasi awal karakter
print("===== PROFIL KARAKTER RPG =====")
print("Nama Hero :", nama_hero)
print("Level     :", level)
print("HP        :", hp)
print("Status Hidup:", is_alive)
print("Inventory :", inventory)
print("Atribut   :", atribut)

# 3. Menampilkan tipe data setiap variabel
print("\n===== TIPE DATA VARIABEL =====")
print("Tipe nama_hero :", type(nama_hero))
print("Tipe level     :", type(level))
print("Tipe hp        :", type(hp))
print("Tipe is_alive  :", type(is_alive))
print("Tipe inventory :", type(inventory))
print("Tipe atribut   :", type(atribut))

# 4A. Karakter mendapatkan item baru
inventory.append("Ramuan HP")

# 4B. Karakter naik level
level = float(level)
level = level + 0.5

# 5. Menampilkan informasi terbaru karakter
print("\n===== PROFIL KARAKTER TERBARU =====")
print("Nama Hero :", nama_hero)
print("Level     :", level)
print("HP        :", hp)
print("Status Hidup:", is_alive)
print("Inventory :", inventory)
print("Atribut   :", atribut)

print("\n===== TIPE DATA SETELAH UPDATE =====")
print("Tipe level     :", type(level))
print("Tipe inventory :", type(inventory))

print('\n ------------------------------------------- \n')