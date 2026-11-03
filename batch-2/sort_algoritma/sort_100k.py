import sys
import time

file_path = "random100k.txt"
output_file = "hasil_diurutkan.txt"

# Membaca data
try:
    with open(file_path, "r") as file:
        original_arr = [int(x) for x in file.read().split()]

    print(f"Total data: {len(original_arr)} angka")

except FileNotFoundError:
    print(f"File {file_path} tidak ditemukan.")
    sys.exit()


# Fungsi Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


# Fungsi Selection Sort
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


# Fungsi Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# Fungsi Shell Sort
def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr


# Fungsi Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Fungsi Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


# Daftar algoritma sorting
algorithms = [
    ("Bubble Sort", bubble_sort),
    ("Selection Sort", selection_sort),
    ("Insertion Sort", insertion_sort),
    ("Shell Sort", shell_sort),
    ("Merge Sort", merge_sort),
    ("Quick Sort", quick_sort)
]


# Mengukur waktu eksekusi setiap algoritma
print("\n" + "=" * 42)
print(f"{'Algoritma Sorting':<22} | {'Waktu (s)':>12}")
print("=" * 42)

final_sorted_result = []

for name, func in algorithms:
    test_arr = original_arr.copy()

    start_time = time.perf_counter()
    sorted_arr = func(test_arr)
    end_time = time.perf_counter()

    execution_time = (end_time - start_time)

    print(f"{name:<22} | {execution_time:>12.4f}")

    final_sorted_result = sorted_arr

print("=" * 42)


# Menyimpan hasil pengurutan
with open(output_file, "w") as file:
    file.write("\n".join(map(str, final_sorted_result)))

print(f"\nHasil pengurutan disimpan ke '{output_file}'.")