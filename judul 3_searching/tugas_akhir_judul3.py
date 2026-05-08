def binary_search(arr, n, target):
    l = 0
    r = n - 1
    pos = -1
    while l <= r:
        m = l + (r - l) // 2
        print(f"Median: {m}, nilai: {arr[m]}")
        if arr[m] == target:
            pos = m
            break
        elif arr[m] < target:
            print("Mencari di kanan")
            l = m + 1
        else:
            print("Mencari di kiri")
            r = m - 1
    return pos


def main():
    print("--- Sistem Verifikasi ID Registrasi Seminar ---")
    try:
        n = int(input("Masukkan jumlah elemen (peserta): "))
    except ValueError:
        print("Input tidak valid!")
        return
    arr = []
    print("Masukkan elemen ID (urut menaik):")
    for i in range(n):
        while True:
            try:
                nilai = int(input())
                arr.append(nilai)
                break
            except ValueError:
                print("Input tidak valid, silakan masukkan angka!")
    print(f"Array: {arr}")
    while True:
        try:
            target = int(input("Masukkan ID peserta yang ingin dicari: "))
            break
        except ValueError:
            print("Input tidak valid, silakan masukkan angka!")
    pos = binary_search(arr, n, target)
    if pos != -1:
        print(f"ID Valid! Ditemukan pada indeks ke-{pos}")
    else:
        print("ID Tidak ditemukan dalam sistem")


if __name__ == "__main__":
    main()