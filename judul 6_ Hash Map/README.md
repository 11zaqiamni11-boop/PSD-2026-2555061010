A. Judul Program

PROGRAM E-LIVESTOCK: MANAJEMEN KAWANAN SAPI PAKE STRUKTUR DATA BINARY SEARCH TREE (BST)

B. Deskripsi Singkat

Program ini dibikin untuk nyimulasiin sistem pencatatan sapi di peternakan (E-Livestock) pake nomor tag telinga bentuk angka. Penyimpanannya ini pake konsep Binary Search Tree (BST). Bayangin aja datanya itu kayak silsilah pohon yang bercabang ke bawah. Aturannya : kalau nomor tag sapi yang baru masuk angkanya lebih kecil dari posisi data saat ini, dia bakal ke cabang kiri. Sebaliknya, kalau lebih gede, masuk ke cabang kanan.

Kelebihan program ini itu kalau mau nge-insert data ternak baru atau nyari rekam jejak sapi. Fitur utamanya ada tambah nomor tag, cari status sapi di kandang, sampai ngecek info populasi seperti nyari nomor tag paling kecil (biasanya sapi paling tua atau awal masuk), paling gede (sapi atau anak sapi baru), dan ngitung total populasi sapi yang udah terdaftar. Biar kodingannya gak gampang error atau mati sendiri pas di-run gara-gara user salah ngetik huruf (padahal disuruhnya angka), di codenya udah ada pengaman try-except. Kinerja program ini buat nyari data lumayan sat set alias O(log n), soalnya bisa langsung motong jalur pencarian jadi setengah tanpa harus ngecek datanya satu-satu dari awal.

C. Source Code

Penjelasan kode per baris:

* class Node ini cetakan awal buat bikin kotak data di tree.
* def init(self, key) ini fungsi bawaan buat ngatur nilai awal pas node baru dibuat.
* self.key = key ini buat nyimpen angka nomor tag sapi ke dalam kotaknya.
* self.left = None ini nyiapin dahan sebelah kiri yang awalnya dibikin kosong.
* self.right = None ini nyiapin dahan sebelah kanan yang awalnya juga kosong.
* class BSTDasar bikin class baru di sinilah semua fungsi buat ngatur tree dikumpulin.
* def init(self) ini fungsi setingan awal pas objek dari class BSTDasar dibikin pertama kali.
* self.root = None ngeset akar tree atau root nya jadi kosong pas program jalan awal.
* def insert_node(self, root, key) bikin fungsi buat nambahin node baru secara rekursif.
* if root is None dicek dulu nih kalau posisi yang lagi dicek ternyata masih kosong.
* return Node(key) maka dibikinlah node baru di posisi yang kosong itu.
* if key < root.key kalau angka yang mau dimasukin lebih kecil dari node saat ini.
* root.left = self.insert_node(root.left, key) datanya dilempar ke cabang kiri buat diproses lagi.
* elif key > root.key tapi kalau angkanya ternyata lebih gede dari node saat ini.
* root.right = self.insert_node(root.right, key) datanya dilempar ke cabang kanan buat diproses ke bawah.
* return root ngasih balik nilai root biar struktur tree nya tetap nyambung dari atas ke bawah.
* def insert(self, key) ini fungsi insert utama yang bakal dipanggil dari luar class biar simpel.
* self.root = self.insert_node(self.root, key) fungsi ini manggil fungsi rekursif di atas dan mulainya dari root.
* def search_node(self, root, key) bikin fungsi buat nyari data secara rekursif.
* if root is None kalau node yang lagi dicek ternyata kosong.
* return False berarti datanya emang gak ada jadi balikin nilai False.
* if root.key == key kalau angka di node saat ini sama persis kayak angka yang dicari.
* return True berarti datanya ketemu dan balikin nilai True.
* if key < root.key kalau angka yang dicari lebih kecil dari node saat ini.
* return self.search_node(root.left, key) lanjutin pencariannya ke cabang sebelah kiri.
* return self.search_node(root.right, key) kalau angkanya lebih gede lanjutin pencariannya ke cabang sebelah kanan.
* def search(self, key) fungsi search utama yang gampang dipanggil dari program tanpa parameter root.
* return self.search_node(self.root, key) tugasnya cuma manggil fungsi search node dari ujung akar.
* def inorder(self, root) bikin fungsi buat nampilin isi tree baca dari kiri cetak baru ke kanan.
* if root is None kalau node nya kosong.
* return keluar aja dari fungsi gak usah ngapa ngapain.
* self.inorder(root.left) telusuri dulu semua cabang sebelah kiri sampai mentok ke bawah.
* print(root.key, end=" ") terus cetak nilai node nya ke layar nyamping.
* self.inorder(root.right) habis itu baru telusuri cabang yang sebelah kanan.
* def preorder(self, root) bikin fungsi nampilin tree cetak atasnya dulu baru kiri terus kanan.
* if root is None cek kalau node nya kosong.
* return selesaiin fungsi kalau node gak ada isinya.
* print(root.key, end=" ") cetak dulu nilai node yang lagi dicek sekarang ke layar.
* self.preorder(root.left) baru deh telusuri cabang kirinya.
* self.preorder(root.right) terus lanjut telusuri cabang kanannya.
* def postorder(self, root) bikin fungsi nampilin tree telusuri kiri kanan baru cetak induknya.
* if root is None cek lagi kalau node nya kosong.
* return keluar dari fungsi kalau emang kosong.
* self.postorder(root.left) telusuri cabang kiri sampai mentok paling bawah.
* self.postorder(root.right) terus telusuri cabang kanannya.
* print(root.key, end=" ") terakhir baru cetak nilai node induknya ke layar.
* def find_min(self, root) bikin fungsi buat nyari angka paling kecil di dalam tree kita.
* if root is None cek dulu tree nya kosong apa nggak.
* return -1 kalau kosong balikin nilai min satu sebagai tanda datanya belum ada.
* current = root bikin variabel bantuan namanya current yang posisinya ditaruh di root.
* while current.left is not None looping selama cabang kiri masih ada isinya.
* current = current.left geser terus ke kiri soalnya nilai paling kecil ada di situ.
* return current.key kalau udah mentok gak ada kiri lagi balikin nilai yang ada di posisi itu.
* def find_max(self, root) bikin fungsi buat nyari angka paling gede di tree.
* if root is None cek kalau tree lagi kosong.
* return -1 balikin nilai min satu kalau beneran kosong.
* current = root set variabel current mulai dari posisi root.
* while current.right is not None looping selama cabang kanan masih ada isinya.
* current = current.right geser terus ke kanan karena nilai terbesar ngumpul di situ.
* return current.key balikin nilai posisinya kalau udah mentok di kanan.
* def count_nodes(self, root) bikin fungsi rekursif buat ngitung ada berapa total node di dalam tree.
* if root is None kalau node yang dicek kosong.
* return 0 ngasih nilai nol soalnya gak ada node buat dihitung.
* return 1 + self.count_nodes(root.left) + self.count_nodes(root.right) hitung satu untuk node saat ini terus tambahin total node kiri dan kanan.
* def sum_nodes(self, root) bikin fungsi buat ngejumlahin semua angka yang ada di tree.
* if root is None kalau node nya kosong.
* return 0 kasih nilai nol ke hitungan.
* return root.key + self.sum_nodes(root.left) + self.sum_nodes(root.right) tambahin nilai node sekarang dengan total angka cabang kiri dan kanan.
* def main() ini fungsi utama tempat aplikasi E-Livestock jalan pertama kali.
* peternakan = BSTDasar() kita bikin objek baru dari class BSTDasar dan disimpen ke variabel peternakan.
* pilih = 0 bikin variabel pilih buat nyimpen input menu diset nol dulu.
* while pilih != 4: looping terus terusan selama user belum milih angka empat buat keluar.
* print(=== E-Livestock: Manajemen Kawanan Sapi ===) cetak teks judul aplikasinya ke layar.
* print(1. Tambah Nomor Tag Sapi) cetak menu teks nomor satu buat nambah data sapi.
* print(2. Cari Nomor Tag Sapi) cetak menu teks nomor dua buat nyari data sapi.
* print(3. Tampilkan Info Populasi) cetak menu teks nomor tiga buat lihat info populasi.
* print(4. Keluar) cetak menu teks nomor empat buat keluar.
* try: mulai blok try except buat nangkep error kalau user masukin input selain angka.
* pilih = int(input(Pilih: )) minta user masukin pilihan menu dan dipaksa jadi integer.
* except ValueError: kalau ada error gara gara user masukin huruf.
* print(Input tidak valid! Masukkan angka.) cetak pesan peringatan ke user biar masukinnya bener.
* continue paksa program buat skip sisa kode di bawahnya dan balik lagi nampilin menu.
* if pilih == 1: kalau user ngetik angka satu milih menu tambah data.
* try: siapin jebakan error lagi khusus buat proses input nomor tag.
* x = int(input(Masukkan nomor tag sapi (angka): )) minta input nomor tag ke user disimpen di variabel x.
* peternakan.insert(x) panggil fungsi insert di objek peternakan buat masukin angkanya ke tree.
* print(Nomor tag sapi {x} berhasil dimasukkan ke sistem.) tunjukin pesan sukses.
* except ValueError: kalau user nginput huruf pas disuruh masukin nomor tag.
* print(Input tidak valid! Masukkan angka.) kasih pesan error ke layar.
* elif pilih == 2: kalau user milih menu nomor dua buat cari data sapi.
* try: siapin jebakan error lagi buat proses pencarian.
* x = int(input(Cari nomor tag sapi: )) minta user masukin angka tag sapi yang mau dicari.
* if peternakan.search(x): cek datanya pakai fungsi search kalau hasilnya True.
* print(Status: Sapi Terdaftar dan Ada di Kandang!) cetak pesan kalau sapinya beneran ada.
* else: kalau hasil search nya False.
* print(Status: Sapi Tidak Ditemukan dalam Data.) cetak pesan kalau sapinya emang gak ketemu.
* except ValueError: tangkep error kalau user masukin karakter selain angka pas nyari.
* print(Input tidak valid! Masukkan angka.) tunjukin pesan error.
* elif pilih == 3: kalau user milih menu nomor tiga buat lihat info populasi.
* print(Nomor tag terkecil (Paling Awal): {peternakan.find_min(peternakan.root)}) cetak teks info sapi paling lama dari tree.
* print(Nomor tag terbesar (Paling Baru): {peternakan.find_max(peternakan.root)}) cetak teks info sapi terbaru.
* print(Total populasi sapi di sistem: {peternakan.count_nodes(peternakan.root)}) cetak jumlah total populasi sapi.
* elif pilih == 4: kalau user milih menu empat buat keluar dari program.
* print(Program E-Livestock selesai.) cetak ucapan perpisahan karena program berhenti.
* else: kalau angka yang diketik user bukan satu dua tiga atau empat.
* print(Pilihan tidak valid!) kasih tau ke user kalau menu yang dipilih gak ada.
* if **name** == "**main**": baris standar python buat mastiin program dijalankan sebagai file utama.
* main() nah panggil fungsi main biar seluruh program kita mulai jalan.

D. Output Program

Penjelasan Output:
Saat kodingan ini di-run, terminal bakal nampilin judul === E-Livestock: Manajemen Kawanan Sapi === sama 4 pilihan menu. Sistem bakal nunggu masukin angka. Misalnya, iseng masukin huruf A. Tapi udah ada try-except, jadi sistemnya nolak jadi nampilin: Input tidak valid! Masukkan angka. terus otomatis balik nampilin menu lagi tanpa error atau force close.

Terus, jalanin yang benernya. Pilih menu 1 (Tambah Nomor Tag Sapi), terus masukin angka 50 (misalnya anak sapi baru lahir atau sapi Limosin baru datang). Program nampilin: Nomor tag sapi 50 berhasil dimasukkan ke sistem. Terus ulang lagi cara ini dua kali berturut-turut buat masukin angka 30 dan 70. Di balik layar, sistem udah otomatis ngejadiin angka 50 sebagai akar atau root, angka 30 masuk ke cabang sebelah kiri karena lebih kecil, dan angka 70 ke cabang sebelah kanan karena lebih gede.

Buat ngebuktiin datanya beneran masuk, pilih menu 2 (Cari Nomor Tag Sapi) dan nyari angka 30. Sistem bakal nemuin dan nampilin tulisan: Status: Sapi Terdaftar dan Ada di Kandang!. Tapi misal iseng nyari angka 99 yang emang nggak pernah dimasukin, sistem langsung nampilin: Status: Sapi Tidak Ditemukan dalam Data.

Lanjut, kalau mau liat rekap datanya, tinggal pilih menu 3 (Tampilkan Info Populasi). Sistem bakal otomatis menuju ke cabang mentok kiri buat dapet nilai terkecil, cabang mentok kanan buat nilai terbesar, dan ngitung semua node yang ada. Hasilnya langsung keluar kalau tag sapi terkecilnya 30, terbesarnya 70, dan total populasinya ada 3 ekor.

Kalau udah selesai, tinggal pencet menu 4 (Keluar). Terminal bakal nampilin tulisan program selesai, perulangannya putus, dan aplikasinya berhenti dengan aman.
