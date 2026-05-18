class StackArray:
    def __init__(self, max_size=100):
        self.MAX = max_size
        self.st = [None] * self.MAX
        self.top_idx = -1

    def is_empty(self):
        return self.top_idx == -1

    def is_full(self):
        return self.top_idx == self.MAX - 1

    def push(self, x):
        if self.is_full():
            print("Stack penuh: Botol ecobrick sudah penuh!")
            return
        self.top_idx += 1
        self.st[self.top_idx] = x
        print(f"Push: '{x}' berhasil dipadatkan ke dalam botol.")

    def pop(self):
        if self.is_empty():
            print("Stack kosong: Botol masih kosong, tidak ada yang bisa dikeluarkan.")
            return
        print(f"Pop: '{self.st[self.top_idx]}' berhasil dikeluarkan dari botol.")
        self.top_idx -= 1

    def peek(self):
        if self.is_empty():
            print("Stack kosong: Botol masih kosong.")
            return
        print(f"Elemen teratas (di bawah leher botol): {self.st[self.top_idx]}")

    def display(self):
        if self.is_empty():
            print("Stack kosong: Botol belum diisi.")
            return
        print("\nIsi botol ecobrick (atas ke bawah):")
        for i in range(self.top_idx, -1, -1):
            print(f"- Lapis {i+1}: {self.st[i]}")
        print()


def main():
    stack = StackArray(10)
    pilih = 0
    
    while pilih != 5:
        print("\n=== PEMBUATAN ECOBRICK (STACK) ===")
        print("1. Masukkan Sampah (Push)")
        print("2. Keluarkan Sampah Teratas (Pop)")
        print("3. Cek Sampah Paling Atas (Peek)")
        print("4. Tampilkan Isi Botol")
        print("5. Keluar")
        
        try:
            pilih = int(input("Pilih: "))
        except ValueError:
            print("Input tidak valid! Masukkan angka menu.")
            continue
            
        if pilih == 1:
            val = input("Masukkan jenis sampah plastik: ")
            stack.push(val)
        elif pilih == 2:
            stack.pop()
        elif pilih == 3:
            stack.peek()
        elif pilih == 4:
            stack.display()
        elif pilih == 5:
            print("Program selesai.")
        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()