 A. Judul Program
PROGRAM SITOSERBA: MANAJEMEN STOK PAKE STRUKTUR DATA BINARY SEARCH TREE (BST)

B. Deskripsi Singkat
Program ini dibikin buat nyimulasiin sistem manajemen stok barang di toko (SiToserba) pake kode barang bentuk angka. Penyimpanannya ini pake konsep Binary Search Tree (BST). Bayangin aja datanya itu kayak pohon yang bercabang ke bawah. Aturannya simpel: kalau kode barang yang baru masuk angkanya lebih kecil dari posisi data saat ini, dia bakal lari ke cabang kiri. Sebaliknya, kalau lebih gede, dia masuk ke cabang kanan.

Kelebihan pake program ini tuh cepet banget kalau kita mau nge-insert data baru atau nyari barang. Fitur utamanya ada tambah kode barang, cari status barang, sampai ngecek info stok kayak nyari kode barang paling kecil, paling gede, dan ngitung total jenis barang yang udah disimpen. Biar kodingannya nggak gampang error atau mati sendiri pas di-run gara-gara user salah ngetik huruf (padahal disuruhnya angka), di dalamnya udah dipasangin pengaman try-except. Kinerja program ini buat nyari data lumayan wush-wush alias O(log n), soalnya dia bisa langsung motong jalur pencarian jadi setengah tanpa harus ngecek datanya satu-satu dari awal.

C. Source Code Penjelasan kode per baris

Baris 1: class Node: - Bikin cetakan (class) namanya Node buat nyimpen satu data tunggal di pohonnya.
Baris 2: def **init**(self, key): - Ini constructor, semacam fungsi bawaan buat nyiapin node baru pas pertama kali dibikin, sekalian bawa parameter key alias kode barangnya.
Baris 3: self.key = key - Nyimpen nilai kode barang yang diinput user ke dalam memori node tersebut.
Baris 4: self.left = None - Setel cabang anak sebelah kiri jadi kosong dulu karena baru dibikin.
Baris 5: self.right = None - Setel cabang anak sebelah kanan jadi kosong juga.
Baris 7: class BSTDasar: - Bikin cetakan utama namanya BSTDasar buat ngebangun dan ngatur keseluruhan pohon BST-nya.
Baris 8: def **init**(self): - Fungsi inisialisasi awal buat pohon BST.
Baris 9: self.root = None - Setel akar pohon (root) ke kondisi kosong, tandanya pohon ini belum ada isinya sama sekali.
Baris 11: def insert_node(self, root, key): - Bikin fungsi rekursif (fungsi yang manggil dirinya sendiri) buat nyari posisi yang pas buat nyelipin node baru.
Baris 12: if root is None: - Ngecek, posisi cabang yang lagi dicek sekarang kosong nggak?
Baris 13: return Node(key) - Kalau kosong, langsung bikin node baru di situ dan balikin posisinya.
Baris 14: if key < root.key: - Ngecek apa kode barang yang mau dimasukin lebih kecil dari nilai node sekarang.
Baris 15: root.left = self.insert_node(root.left, key) - Kalau iya, lempar ke cabang kiri dan panggil fungsinya lagi buat nyari tempat kosong di sana.
Baris 16: elif key > root.key: - Ngecek kalau ternyata datanya lebih gede dari nilai node sekarang.
Baris 17: root.right = self.insert_node(root.right, key) - Lempar pencariannya ke cabang sebelah kanan.
Baris 18: return root - Balikin struktur pohon yang udah ke-update data baru.
Baris 20: def insert(self, key): - Fungsi pemicu buat mulai proses insert data dari posisi paling atas (root).
Baris 21: self.root = self.insert_node(self.root, key) - Eksekusi fungsi insert_node dengan titik start dari akar pohon.
Baris 23: def search_node(self, root, key): - Fungsi rekursif buat nyari kode barang tertentu di dalam pohon.
Baris 24: if root is None: - Kalau pencariannya udah mentok ujung tapi datanya nggak ada.
Baris 25: return False - Balikin nilai False, tandanya barang fix nggak ada.
Baris 26: if root.key == key: - Kalau kode barang di node pas banget sama yang lagi kita cari.
Baris 27: return True - Balikin nilai True, tandanya barang ketemu.
Baris 28: if key < root.key: - Kalau angka yang dicari lebih kecil dari posisi sekarang.
Baris 29: return self.search_node(root.left, key) - Lanjutin pencarian ke cabang kiri.
Baris 30: return self.search_node(root.right, key) - Kalau lebih gede, lanjutin pencarian nyusur ke cabang kanan.
Baris 32: def search(self, key): - Fungsi utama pemicu buat mulai pencarian barang, start-nya dari root.
Baris 33: return self.search_node(self.root, key) - Manggil fungsi search_node.
Baris 35 sampai 47: def inorder, preorder, postorder - Tiga blok fungsi ini disiapin buat nge-print isi pohon dengan urutan yang beda-beda. Walaupun belum dipake di menu utama, ini sengaja disiapin buat cadangan update fitur ke depannya.
Baris 49: def find_min(self, root): - Fungsi buat nyari kode barang paling kecil.
Baris 50: if root is None: - Ngecek dulu, pohonnya kosong nggak?
Baris 51: return -1 - Kalau kosong, balikin -1 aja sebagai tanda error atau datanya emang nggak ada.
Baris 52: current = root - Mulai penelusuran dari root.
Baris 53: while current.left is not None: - Selama cabang kirinya masih ada isinya, karena nilai paling kecil pasti posisinya mentok di kiri.
Baris 54: current = current.left - Terus geser ke bawah lewat jalur kiri.
Baris 55: return current.key - Kalau udah mentok, balikin angka di node terakhir itu.
Baris 57 sampai 63: def find_max(self, root): - Ini kebalikannya find_min. Dia bakal terus nyusur ke mentok cabang paling kanan buat dapet kode barang yang angkanya paling gede.
Baris 65: def count_nodes(self, root): - Fungsi buat ngitung ada berapa total variasi barang di sistem.
Baris 66: if root is None: - Kalau udah mentok ujung atau kosong.
Baris 67: return 0 - Balikin nilai 0.
Baris 68: return 1 + self.count_nodes(root.left) + self.count_nodes(root.right) - Hitung 1 buat node ini sendiri, terus tambahin jumlah node dari cabang kiri dan kanannya pake rekursif.
Baris 70 sampai 73: def sum_nodes(self, root): - Fungsi ini buat ngejumlahin total dari semua angka kode barang, ini juga buat cadangan fitur aja.
Baris 75: def main(): - Buka fungsi utama main yang jadi nyawa berjalannya program.
Baris 76: sitoserba = BSTDasar() - Bikin objek baru namanya sitoserba dari class BSTDasar. Ini bakal jadi mesin utamanya.
Baris 77: pilih = 0 - Deklarasi variabel pilih dikasih nilai 0 dulu buat mancing biar bisa masuk ke perulangan while.
Baris 79: while pilih != 4: - Bikin looping menu utama yang bakal muter terus selama kita belum milih menu nomor 4 atau keluar.
Baris 80 sampai 84: print - Nge-print antarmuka menu utama SiToserba di terminal.
Baris 86: try: - Pasang sabuk pengaman atau try-except biar kalau user typo ngetik huruf, programnya nggak langsung mati.
Baris 87: pilih = int(input("Pilih: ")) - Minta user milih menu, terus diubah paksa jadi integer.
Baris 88: except ValueError: - Nangkep error kalau ternyata user ngetik selain angka.
Baris 89: print("Input tidak valid! Masukkan angka.") - Ngasih tau user kalau inputnya salah.
Baris 90: continue - Langsung skip kode di bawahnya dan ngulang looping menu dari awal.
Baris 92: if pilih == 1: - Logika kalau user milih menu 1 (Tambah Kode Barang).
Baris 93: try: - Pasang pengaman lagi khusus buat input kodenya.
Baris 94: x = int(input("Masukkan kode barang (angka): ")) - Minta user masukin angka kode barang barunya.
Baris 95: sitoserba.insert(x) - Masukin data tadi ke dalam pohon.
Baris 96: print(f"Kode barang x berhasil dimasukkan...") - Nge-print info kalau datanya sukses masuk.
Baris 97 sampai 98: except ValueError - Sama kayak tadi, nangkep error kalau user masukin huruf.
Baris 100: elif pilih == 2: - Logika kalau user milih menu 2 (Cari Kode Barang).
Baris 102: x = int(input("Cari kode barang: ")) - Minta angka kode yang mau dicari.
Baris 103: if sitoserba.search(x): - Jalanin fungsi search, kalau hasilnya ketemu.
Baris 104: print("Status: Barang Ditemukan di Toko!") - Nampilin info kalau barangnya ada.
Baris 105 sampai 106: else: - Kalau nggak ketemu, print Barang Tidak Ada.
Baris 111: elif pilih == 3: - Logika kalau user milih menu 3 (Tampilkan Info Stok).
Baris 112: print - Manggil find_min buat nampilin kode barang paling kecil.
Baris 113: print - Manggil find_max buat nampilin kode barang paling gede.
Baris 114: print - Manggil count_nodes buat nampilin ada berapa barang yang udah kedaftar.
Baris 116: elif pilih == 4: - Logika kalau user milih menu 4 (Keluar).
Baris 117: print("Program SiToserba selesai.") - Nampilin teks penutup.
Baris 118 sampai 119: else: - Kalau user iseng masukin angka di luar menu, bakal nampil Pilihan tidak valid.
Baris 121 sampai 122: if **name** == "**main**": - Ini sintaks wajib di Python biar fungsi main cuma jalan kalau file ini dieksekusi langsung.

D. Output Program Penjelasan Output

Pas kodingan ini baru di-run, terminal bakal langsung nampilin judul "=== SiToserba: Manajemen Stok ===" sama 4 pilihan menu. Sistem bakal nunggu kita masukin angka. Misalnya nih, kita iseng masukin huruf A. Untungnya udah ada try-except, jadi sistemnya nolak halus dan bilang: "Input tidak valid! Masukkan angka." terus otomatis balik nampilin menu lagi tanpa error apalagi force close.

Terus, kita coba jalanin yang bener. Kita pilih menu 1 (Tambah Kode Barang), terus masukin angka 50. Program jawab: "Kode barang 50 berhasil dimasukkan ke sistem." Kita ulang lagi cara ini dua kali berturut-turut buat masukin angka 30 dan 70. Di balik layar, sistem udah otomatis ngejadiin angka 50 sebagai akar atau root, angka 30 masuk ke cabang sebelah kiri karena lebih kecil, dan angka 70 ke cabang sebelah kanan karena lebih gede.

Buat ngebuktiin datanya beneran masuk, kita pilih menu 2 (Cari Kode Barang) dan nyari angka 30. Sistem bakal cepet banget nemuin dan nampilin tulisan: "Status: Barang Ditemukan di Toko!". Tapi pas kita iseng nyari angka 99 yang emang nggak pernah dimasukin, sistem langsung jawab: "Status: Barang Tidak Ada."

Selanjutnya, kalau mau liat rekap datanya, tinggal pilih menu 3 (Tampilkan Info Stok). Sistem bakal otomatis meluncur ke cabang mentok kiri buat dapet nilai terkecil, cabang mentok kanan buat nilai terbesar, dan ngitung semua node yang ada. Hasilnya langsung keluar kalau barang terkecilnya 30, terbesarnya 70, dan total jenis barangnya ada 3.

Kalau udah kelar nyoba-nyoba, tinggal pencet menu 4 (Keluar). Terminal bakal nampilin tulisan program selesai, perulangannya putus, dan aplikasinya berhenti dengan aman.
