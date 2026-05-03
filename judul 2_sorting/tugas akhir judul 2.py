#PROGRAM PENGURUTAN STRUK BERDASARKAN TANGGAL TRANSAKSI MENGGUNAKAN INSERTION SORT

def insertion_sort_struk(arr, n):
    for i in range(1, n):
        temp = arr[i] 
        j = i - 1
        while j >= 0 and arr[j]['tanggal'] > temp['tanggal']:
            arr[j + 1] = arr[j]
            j -= 1 
        arr[j + 1] = temp
def main():
    try:
        n = int(input("Masukkan jumlah tumpukan struk/nota: "))
    except ValueError:
        print("Input tidak valid!")
        return
    arr = []
    print("Masukkan rincian struk:")
    for i in range(n):
        print(f"\n--- Struk ke-{i+1} ---")
        nama = input("Keterangan/Nama Struk (misal: Laundry, Makan): ")
        while True:
            try:
                tanggal = int(input("Tanggal transaksi (1-31): "))
                arr.append({'nama': nama, 'tanggal': tanggal})
                break
            except ValueError:
                print("Input tidak valid, silakan masukkan angka untuk tanggal!")
    print("\n=========================================")
    print("Kondisi Tumpukan Struk SEBELUM diurutkan:")
    for struk in arr:
        print(f"- {struk['nama']} (Tgl: {struk['tanggal']})")
    insertion_sort_struk(arr, n)
    print("\n=========================================")
    print("Kondisi Tumpukan Struk SETELAH diurutkan (Insertion Sort):")
    for struk in arr:
        print(f"- {struk['nama']} (Tgl: {struk['tanggal']})")
    print("=========================================\n")
if __name__ == "__main__":
    main()