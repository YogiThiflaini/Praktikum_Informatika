# --- 6. UPDATE VARIABEL DINAMIS ---
# Mahasiswa mengambil 1 mata kuliah susulan
matkul_baru = "Jaringan Komputer"
nilai_matkul_baru_str = "88.0"
mutu_matkul_baru = 3.5  # Nilai AB

# A. Tambahkan mata kuliah ke List
daftar_matkul.append(matkul_baru)

# B. Tambahkan nilai mutu ke Dictionary
transkrip_nilai[matkul_baru] = mutu_matkul_baru

# C. Rekalkulasi total dan rata-rata nilai
nilai_jk = float(nilai_matkul_baru_str)
total_nilai = total_nilai + nilai_jk
jumlah_matkul = len(daftar_matkul)
rata_rata_terbaru = total_nilai / jumlah_matkul

# D. Hitung IPK sementara dari Dictionary nilai mutu
total_bobot_mutu = sum(transkrip_nilai.values())
ipk_sementara = total_bobot_mutu / jumlah_matkul

# Menampilkan hasil terbaru
print("\n--- HASIL REKALKULASI SETELAH PENAMBAHAN MATKUL ---")
print("Daftar Matkul Terbaru :", daftar_matkul)
print("Jumlah Matkul Total   :", jumlah_matkul)
print("Rata-Rata Angka Baru  :", round(rata_rata_terbaru, 2))
print("IPK Sementara (Skala 4):", round(ipk_sementara, 2))