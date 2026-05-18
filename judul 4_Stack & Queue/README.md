A. Judul Program
PROGRAM SIMULASI PEMBUATAN ECOBRICK MENGGUNAKAN STRUKTUR DATA STACK (ARRAY)

B. Deskripsi Singkat
Program ini dibuat untuk menyimulasikan proses pemadatan sampah plastik dalam pembuatan ecobrick. Karena ecobrick pada dasarnya adalah botol yang diisi tumpukan sampah plastik lapis demi lapis, sistem penyimpanannya sangat cocok direpresentasikan dengan struktur data Stack yang punya prinsip LIFO (Last In, First Out). Artinya, sampah yang paling terakhir ditekan masuk ke botol bakal jadi sampah yang pertama kali bisa diambil kalau misalnya kita butuh membongkarnya.

Program ini menggunakan metode Array (pakai List bawaan Python) dan membatasi ukuran maksimalnya agar mirip kapasitas asli botol yang terbatas. Operasi intinya ada Push buat masukin sampah baru, Pop buat ngeluarin sampah yang paling atas (berguna banget kalau kita tidak sengaja masukin material yang salah seperti tisu basah/kotor), dan Peek untuk ngecek sampah apa yang posisinya ada di bawah leher botol banget. Biar aman dari crash saat dijalankan, program juga dikasih validasi try-except buat nge- handle kalau user iseng ngetik huruf pas disuruh milih menu angka. Tingkat efisiensi buat nambah atau ngambil data di program ini sangat cepat, yaitu konstan O(1), karena ini menggunakan indeks teratasnya saja tanpa perlu geser-geser data lain.

C. Source Code
<img width="1902" height="958" alt="Cuplikan layar 2026-05-18 194227" src="https://github.com/user-attachments/assets/bd83c681-ccee-427f-bac9-1592ef695d82" />
<img width="1918" height="838" alt="Cuplikan layar 2026-05-18 194256" src="https://github.com/user-attachments/assets/878d46d4-075f-407f-8e9e-86934827b51e" />
<img width="1918" height="183" alt="Cuplikan layar 2026-05-18 194350" src="https://github.com/user-attachments/assets/3ce424a3-cea4-4ae7-aa7b-ff1b11e89809" />

Penjelasan kode per baris:

Baris 1: class StackArray: - Deklarasi pembuatan cetakan (class) bernama StackArray untuk membangun struktur data stack.

Baris 2: def **init**(self, max_size=100): - Membuat fungsi inisialisasi awal (constructor) dengan parameter ukuran maksimal bawaan (default) 100.

Baris 3: self.MAX = max_size - Menyimpan nilai batas kapasitas maksimal botol tersebut ke dalam variabel memori self.MAX.

Baris 4: self.st = [None] * self.MAX - Membuat list bernama self.st berisi elemen kosong sebanyak kapasitas maksimal yang ditentukan untuk wadah tumpukan sampah.

Baris 5: self.top_idx = -1 - Menentukan penunjuk posisi tumpukan teratas di angka -1, tandanya botol (stack) masih benar-benar kosong.

Baris 7: def is_empty(self): - Deklarasi fungsi bantu untuk mengecek apakah stack dalam keadaan kosong.

Baris 8: return self.top_idx == -1 - Mengembalikan nilai True jika indeks teratas masih -1, dan False jika sudah ada isinya.

Baris 10: def is_full(self): - Deklarasi fungsi bantu untuk mengecek apakah kapasitas tumpukan di botol sudah penuh mentok.

Baris 11: return self.top_idx == self.MAX - 1 - Mengembalikan nilai True jika indeks teratas sudah menyentuh batas ujung dari ukuran list.

Baris 13: def push(self, x): - Deklarasi fungsi push untuk memasukkan data baru (sampah plastik) ke dalam tumpukan menggunakan parameter teks x.

Baris 14: if self.is_full(): - Memeriksa keamanan kapasitas botol apakah sudah penuh atau belum dengan memanggil fungsi is_full().

Baris 15: print("Stack penuh: Botol ecobrick sudah penuh!") - Jika kondisi penuh terpenuhi, program bakal mencetak peringatan ke layar.

Baris 16: return - Menghentikan paksa eksekusi fungsi push() saat itu juga agar program tidak error akibat kelebihan muatan.

Baris 17: self.top_idx += 1 - Jika masih muat, nilai indeks penunjuk posisi teratas (top_idx) dinaikkan 1 angka dulu ke slot kosong di atasnya.

Baris 18: self.st[self.top_idx] = x - Memasukkan data sampah x ke dalam slot list self.st tepat di posisi indeks teratas yang baru.

Baris 19: print(f"Push: '{x}' berhasil dipadatkan ke dalam botol.") - Mencetak konfirmasi sukses bahwa sampah sudah masuk botol.

Baris 21: def pop(self): - Deklarasi fungsi pop untuk mengambil dan mengeluarkan data sampah yang posisinya berada di tumpukan paling atas.

Baris 22: if self.is_empty(): - Memeriksa keamanan tumpukan apakah botol kosong atau tidak menggunakan fungsi is_empty().

Baris 23: print("Stack kosong: Botol masih kosong, tidak ada yang bisa dikeluarkan.") - Cetak pesan penolakan jika dicoba pop tapi botolnya kosong.

Baris 24: return - Menghentikan eksekusi fungsi pop() seketika.

Baris 25: print(f"Pop: '{self.st[self.top_idx]}' berhasil dikeluarkan dari botol.") - Mencetak informasi nama elemen sampah teratas yang baru saja dikeluarkan dari botol.

Baris 26: self.top_idx -= 1 - Menurunkan indeks penunjuk teratas sebanyak 1 angka, sehingga data di atasnya otomatis diabaikan atau dianggap terhapus.

Baris 28: def peek(self): - Deklarasi fungsi peek buat sekadar mengintip sampah apa yang posisinya ada di paling atas tanpa mengubah isi tumpukan.

Baris 29: if self.is_empty(): - Mengecek kondisi apakah botol dalam keadaan kosong.

Baris 30: print("Stack kosong: Botol masih kosong.") - Mencetak pemberitahuan kalau tidak ada barang yang bisa diintip.

Baris 31: return - Langsung keluar dari fungsi peek().

Baris 32: print(f"Elemen teratas (di bawah leher botol): {self.st[self.top_idx]}") - Mencetak nama sampah yang posisinya paling atas di tumpukan saat ini.

Baris 34: def display(self): - Deklarasi fungsi display untuk menampilkan urutan seluruh isi tumpukan botol.

Baris 35: if self.is_empty(): - Mengecek kondisi apakah botolnya kosong atau tidak sebelum dicetak.

Baris 36: print("Stack kosong: Botol belum diisi.") - Memberitahu user jika memang tidak ada data sampah di dalamnya.

Baris 37: return - Keluar dari fungsi display().

Baris 38: print("\nIsi botol ecobrick (atas ke bawah):") - Mencetak teks pembuka sebelum barisan sampah ditampilkan.

Baris 39: for i in range(self.top_idx, -1, -1): - Perulangan for mundur dari indeks teratas (top_idx) berjalan turun ke indeks 0 agar urutan tampilnya dari atas ke bawah.

Baris 40: print(f"- Lapis {i+1}: {self.st[i]}") - Mencetak keterangan nomor lapis tumpukan beserta nama sampah pada posisi tersebut.

Baris 41: print() - Mencetak satu baris kosong tambahan agar jarak antar menu di terminal tidak terlalu rapat.

Baris 44: def main(): - Membuka kerangka fungsi utama main() yang bertindak sebagai motor jalannya program.

Baris 45: stack = StackArray(10) - Membuat objek bernama stack dari class StackArray dan menetapkan ukuran kapasitas botol uji cobanya hanya muat 10 lapis sampah.

Baris 46: pilih = 0 - Mendeklarasikan variabel pilih bernilai awal 0 sebagai pemancing agar program bisa masuk ke perulangan menu.

Baris 48: while pilih != 5: - Membuka perulangan while yang akan terus berputar menyajikan menu selama user belum memilih angka 5 (Keluar).

Baris 49: print("\n=== PEMBUATAN ECOBRICK (STACK) ===") - Mencetak judul antarmuka menu utama aplikasi.

Baris 50: print("1. Masukkan Sampah (Push)") - Mencetak pilihan menu nomor 1 ke layar terminal.

Baris 51: print("2. Keluarkan Sampah Teratas (Pop)") - Mencetak pilihan menu nomor 2 ke layar terminal.

Baris 52: print("3. Cek Sampah Paling Atas (Peek)") - Mencetak pilihan menu nomor 3 ke layar terminal.

Baris 53: print("4. Tampilkan Isi Botol") - Mencetak pilihan menu nomor 4 ke layar terminal.

Baris 54: print("5. Keluar") - Mencetak pilihan menu nomor 5 ke layar terminal.

Baris 56: try: - Membuka blok try (validasi error handling) buat nangkep jika ada kesalahan ketik dari sisi user.

Baris 57: pilih = int(input("Pilih: ")) - Menerima input pilihan menu dari user, dikonversi paksa menjadi angka (integer), lalu disimpan di variabel pilih.

Baris 58: except ValueError: - Blok penangkap jika terjadi error karena user tidak memasukkan angka (misalnya ngetik huruf/simbol).

Baris 59: print("Input tidak valid! Masukkan angka menu.") - Memberikan pesan teguran ke layar terminal bahwa inputnya salah.

Baris 60: continue - Memaksa program melompat langsung kembali ke awal perulangan while untuk memunculkan menu lagi tanpa bikin aplikasi mati atau crash.

Baris 62: if pilih == 1: - Kondisi percabangan jika user memilih angka menu 1.

Baris 63: val = input("Masukkan jenis sampah plastik: ") - Meminta input nama sampah berupa teks biasa (string) lalu menyimpannya ke variabel val.

Baris 64: stack.push(val) - Memanggil fungsi push untuk memasukkan string nama sampah dari variabel val tadi ke dalam botol.

Baris 65: elif pilih == 2: - Kondisi percabangan jika user memilih angka menu 2.

Baris 66: stack.pop() - Mengeksekusi fungsi pop() untuk membuang elemen tumpukan teratas botol.

Baris 67: elif pilih == 3: - Kondisi percabangan jika user memilih angka menu 3.

Baris 68: stack.peek() - Mengeksekusi fungsi peek() untuk mengintip data teratas botol.

Baris 69: elif pilih == 4: - Kondisi percabangan jika user memilih angka menu 4.

Baris 70: stack.display() - Mengeksekusi fungsi display() untuk menjabarkan semua isi botol.

Baris 71: elif pilih == 5: - Kondisi percabangan jika user memilih angka menu 5.

Baris 72: print("Program selesai.") - Mencetak pesan penutup karena proses simulasi selesai dilakukan.

Baris 73: else: - Kondisi alternatif sisa jika user mengetikkan angka selain dari pilihan 1 sampai 5 (misal angka 8).

Baris 74: print("Pilihan tidak valid!") - Menampilkan informasi bahwa nomor menu tersebut tidak tersedia di sistem.

Baris 77: if **name** == "**main**": - Sintaks pengaman di Python untuk memastikan bahwa blok kode di bawahnya hanya akan dieksekusi kalau file ini dijalankan secara langsung.

Baris 78: main() - Memanggil fungsi main() untuk mentrigger jalannya seluruh sistem aplikasi dari awal.

D. Output Program
<img width="1793" height="908" alt="Cuplikan layar 2026-05-18 200542" src="https://github.com/user-attachments/assets/ad909211-f974-4218-b845-d4cd980307a3" />
<img width="1782" height="907" alt="Cuplikan layar 2026-05-18 200605" src="https://github.com/user-attachments/assets/f9bb925a-e397-48b6-b30d-1260491baa85" />
<img width="1882" height="245" alt="Cuplikan layar 2026-05-18 200646" src="https://github.com/user-attachments/assets/e89bae02-3ef9-4937-8334-41641a140c6e" />

Penjelasan Output:
Saat program baru pertama kali dijalankan, layar terminal langsung menampilkan === PEMBUATAN ECOBRICK (STACK) === beserta 5 pilihan menu. Sistem akan menunggu umtuk memasukkan angka.
Misalnya nyoba melihat isi botol sebelum diisi apa-apa dengan memilih menu 4 (Tampilkan Isi Botol). Sistem akan langsung menolak dan mencetak: "Stack kosong: Botol belum diisi." karena memang datanya masih kosong (indeks masih -1).
Setelah itu, baru beroperasi dengan benar. pilih menu 1 (Masukkan Sampah), lalu mengetik "Plastik kemasan deterjen". Program merespons: "Push: Plastik kemasan deterjen berhasil dipadatkan ke dalam botol."
Lalu pilih menu 1 lagi dua kali berturut-turut buat masukian "Bungkus kopi sachet" dan "Potongan sedotan plastik".
Untuk mastiin tumpukan teratas saat ini, kita memilih menu 3 (Cek Sampah Paling Atas). Program hanya akan melihat tanpa menghapus data, lalu mencetak: "Elemen teratas (di bawah botol): Potongan sedotan plastik".
lalu,ternyata potongan sedotannya kurang kecil dan malah bikin botol susah padat. Jadi, harus membuangnya dengan memilih menu 2 (Keluarkan Sampah Teratas). Sistem otomatis membuang sedotan tersebut dan merespons: "Pop: Potongan sedotan plastik berhasil dikeluarkan dari botol."
Sebagai gantinya, pilih menu 1 lagi dan memasukkan sampah baru berupa "Bungkus permen".
Untuk melihat susunan akhir botol saat ini, pilih menu 4. Program akan melakukan perulangan mundur dan mencetak hasilnya dari tumpukan teratas ke dasar botol 
Karena proses pemadatan dirasa sudah cukup untuk simulasi ini, terakhir memilih menu 5 (Keluar). Sistem akan mencetak "Program selesai." lalu perulangan while terputus dan program otomatis tertutup sepenuhnya.

