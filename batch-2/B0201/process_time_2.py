import time
from functools import wraps

def ukur_waktu(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        mulai = time.perf_counter()
        hasil = func(*args, **kwargs)
        selesai = time.perf_counter()
        durasi = selesai - mulai

        print(f"Fungsi '[{func.__name__}]' selesai dieksekusi dalam {durasi:.6f} detik")
        return hasil

    return wrapper

# Contoh Penggunaan Decorator:
@ukur_waktu
def hitung_kuadrat(n):
    return [i ** 2 for i in range(n)]

@ukur_waktu
def simulasi_proses():
    time.sleep(1.5)  # Simulasi proses jeda 1.5 detik

# Jalankan fungsi
hitung_kuadrat(5_000_000)
simulasi_proses()