# PROGRAM PENCATATAN PENGELUARAN HARIAN

def menu():
    print("1. Masukkan keterangan dan nominal pengeluaran")
    print("2. Tampilkan catatan pengeluaran")
    print("3. Edit keterangan dan nominal pengeluaran")
    print("4. Keluar")

def main():
    pengeluaran = []
    running = True
    while running:
        menu()
        try:
            choice = int(input("Pilihan: "))
        except ValueError:
            print("Masukkan angka yang valid.")
            continue
        if choice == 1:
            keterangan = input("Keterangan pengeluaran: ")
            while True:
                try:
                    nominal = int(input("Nominal pengeluaran: "))
                    break
                except ValueError:
                    print("Input tidak valid, silakan masukkan angka!")
            pengeluaran.append((keterangan, nominal))
        elif choice == 2:
            if not pengeluaran:
                print("Belum ada data pengeluaran, silakan input terlebih dahulu.")
            else:
                print("Menampilkan Catatan Pengeluaran:")
                print("-------------------------")
                for i, (keterangan, nominal) in enumerate(pengeluaran):
                    print(f"{i + 1}. {keterangan}: {nominal}")
                print("-------------------------")
        elif choice == 3:
            if not pengeluaran:
                print("Belum ada data pengeluaran, silakan input terlebih dahulu")
            else:
                try:
                    index = int(input("Masukkan nomor pengeluaran yang ingin diedit: ")) - 1
                    if 0 <= index < len(pengeluaran):
                        keterangan_baru = input("Keterangan baru: ")
                        while True:
                            try:
                                nominal_baru = int(input("Nominal baru: "))
                                break
                            except ValueError:
                                print("Input tidak valid, silakan masukkan angka!")
                        pengeluaran[index] = (keterangan_baru, nominal_baru)
                    else:
                        print("Nomor pengeluaran tidak valid.")
                except ValueError:
                    print("Input tidak valid, silakan masukkan angka!")
        elif choice == 4:
            running = False
            print("Program selesai.")
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()