A. Judul Program PROGRAM SITOSERBA: MANAJEMEN STOK PAKE STRUKTUR DATA BINARY SEARCH TREE (BST)

B. Deskripsi Singkat Program ini dibikin buat nyimulasiin sistem manajemen stok barang di toko (SiToserba) pake kode barang bentuk angka. Penyimpanannya ini pake konsep Binary Search Tree (BST). Bayangkan saja datanya itu kayak pohon yang bercabang ke bawah. Aturannya simpel: kalau kode barang yang baru masuk angkanya lebih kecil dari posisi data saat ini, dan bakal ke cabang kiri. Sebaliknya, kalau lebih gede, masuk ke cabang kanan.

Kelebihan program ini cepet bener kalau mau nge-insert data baru atau nyari barang. Fitur utamanya ada tambah kode barang, cari status barang, sampai ngecek info stok seperti nyari kode barang paling kecil, paling gede, dan ngitung total jenis barang yang udah disimpen. Biar kodingannya tidak gampang error atau mati sendiri pas di-run gara-gara user salah ngetik huruf (padahal disuruhnya angka), di dalamnya udah dipasangin pengaman try-except. Kinerja program ini buat nyari data lumayan wush-wush alias O(log n), soalnya bisa langsung motong jalur pencarian jadi setengah tanpa harus ngecek datanya satu-satu dari awal.

C. Source Code image image image image

Penjelasan kode per baris :

class Node ini cetakan awal buat bikin kotak data di tree.
def init self key ini fungsi bawaan buat ngatur nilai awal pas node baru dibuat.
self key sama dengan key ini buat nyimpen angka kode barang ke dalam kotaknya.
self left sama dengan None ini nyiapin dahan sebelah kiri yang awalnya dibikin kosong.
self right sama dengan None ini nyiapin dahan sebelah kanan yang awalnya juga kosong.
class BSTDasar bikin class baru di sinilah semua fungsi buat ngatur tree dikumpulin.
def init self ini fungsi setingan awal pas objek dari class BSTDasar dibikin pertama kali.
self root sama dengan None ngeset akar tree atau root nya jadi kosong pas program jalan awal.
def insert node self root key bikin fungsi buat nambahin node baru secara rekursif.
if root is None dicek dulu nih kalau posisi yang lagi dicek ternyata masih kosong.
return Node key maka dibikinlah node baru di posisi yang kosong itu.
if key lebih kecil root key kalau angka yang mau dimasukin lebih kecil dari node saat ini.
root left sama dengan self insert node root left key datanya dilempar ke cabang kiri buat diproses lagi.
elif key lebih besar root key tapi kalau angkanya ternyata lebih gede dari node saat ini.
root right sama dengan self insert node root right key datanya dilempar ke cabang kanan buat diproses ke bawah.
return root ngasih balik nilai root biar struktur tree nya tetap nyambung dari atas ke bawah.
def insert self key ini fungsi insert utama yang bakal dipanggil dari luar class biar simpel.
self root sama dengan self insert node self root key fungsi ini manggil fungsi rekursif di atas dan mulainya dari root.
def search node self root key bikin fungsi buat nyari data secara rekursif.
if root is None kalau node yang lagi dicek ternyata kosong.
return False berarti datanya emang gak ada jadi balikin nilai False.
if root key sama dengan sama dengan key kalau angka di node saat ini sama persis kayak angka yang dicari.
return True berarti datanya ketemu dan balikin nilai True.
if key lebih kecil root key kalau angka yang dicari lebih kecil dari node saat ini.
return self search node root left key lanjutin pencariannya ke cabang sebelah kiri.
return self search node root right key kalau angkanya lebih gede lanjutin pencariannya ke cabang sebelah kanan.
def search self key fungsi search utama yang gampang dipanggil dari program tanpa parameter root.
return self search node self root key tugasnya cuma manggil fungsi search node dari ujung akar.
def inorder self root bikin fungsi buat nampilin isi tree baca dari kiri cetak baru ke kanan.
if root is None kalau node nya kosong.
return keluar aja dari fungsi gak usah ngapa ngapain.
self inorder root left telusuri dulu semua cabang sebelah kiri sampai mentok ke bawah.
print root key end spasi terus cetak nilai node nya ke layar nyamping.
self inorder root right habis itu baru telusuri cabang yang sebelah kanan.
def preorder self root bikin fungsi nampilin tree cetak atasnya dulu baru kiri terus kanan.
if root is None cek kalau node nya kosong.
return selesaiin fungsi kalau node gak ada isinya.
print root key end spasi cetak dulu nilai node yang lagi dicek sekarang ke layar.
self preorder root left baru deh telusuri cabang kirinya.
self preorder root right terus lanjut telusuri cabang kanannya.
def postorder self root bikin fungsi nampilin tree telusuri kiri kanan baru cetak induknya.
if root is None cek lagi kalau node nya kosong.
return keluar dari fungsi kalau emang kosong.
self postorder root left telusuri cabang kiri sampai mentok paling bawah.
self postorder root right terus telusuri cabang kanannya.
print root key end spasi terakhir baru cetak nilai node induknya ke layar.
def find min self root bikin fungsi buat nyari angka paling kecil di dalam tree kita.
if root is None cek dulu tree nya kosong apa nggak.
return min satu kalau kosong balikin nilai min satu sebagai tanda datanya belum ada.
current sama dengan root bikin variabel bantuan namanya current yang posisinya ditaruh di root.
while current left is not None looping selama cabang kiri masih ada isinya.
current sama dengan current left geser terus ke kiri soalnya nilai paling kecil ada di situ.
return current key kalau udah mentok gak ada kiri lagi balikin nilai yang ada di posisi itu.
def find max self root bikin fungsi buat nyari angka paling gede di tree.
if root is None cek kalau tree lagi kosong.
return min satu balikin nilai min satu kalau beneran kosong.
current sama dengan root set variabel current mulai dari posisi root.
while current right is not None looping selama cabang kanan masih ada isinya.
current sama dengan current right geser terus ke kanan karena nilai terbesar ngumpul di situ.
return current key balikin nilai posisinya kalau udah mentok di kanan.
def count nodes self root bikin fungsi rekursif buat ngitung ada berapa total node di dalam tree.
if root is None kalau node yang dicek kosong.
return nol ngasih nilai nol soalnya gak ada node buat dihitung.
return satu tambah self count nodes root left tambah self count nodes root right hitung satu untuk node saat ini terus tambahin total node kiri dan kanan.
def sum nodes self root bikin fungsi buat ngejumlahin semua angka yang ada di tree.
if root is None kalau node nya kosong.
return nol kasih nilai nol ke hitungan.
return root key tambah self sum nodes root left tambah self sum nodes root right tambahin nilai node sekarang dengan total angka cabang kiri dan kanan.
def main ini fungsi utama tempat aplikasi SiToserba jalan pertama kali.
sitoserba sama dengan BSTDasar kita bikin objek baru dari class BSTDasar dan disimpen ke variabel sitoserba.
pilih sama dengan nol bikin variabel pilih buat nyimpen input menu diset nol dulu.
while pilih tidak sama dengan empat looping terus terusan selama user belum milih angka empat buat keluar.
print SiToserba Manajemen Stok cetak teks judul aplikasinya ke layar.
print satu Tambah Kode Barang cetak menu teks nomor satu buat nambah barang.
print dua Cari Kode Barang cetak menu teks nomor dua buat nyari barang.
print tiga Tampilkan Info Stok cetak menu teks nomor tiga buat lihat info stok.
print empat Keluar cetak menu teks nomor empat buat keluar.
try mulai blok try except buat nangkep error kalau user masukin input selain angka.
pilih sama dengan int input Pilih minta user masukin pilihan menu dan dipaksa jadi integer.
except ValueError kalau ada error gara gara user masukin huruf.
print Input tidak valid Masukkan angka cetak pesan peringatan ke user biar masukinnya bener.
continue paksa program buat skip sisa kode di bawahnya dan balik lagi nampilin menu.
if pilih sama dengan satu kalau user ngetik angka satu milih menu tambah barang.
try siapin jebakan error lagi khusus buat proses input kode barang.
x sama dengan int input Masukkan kode barang angka minta input kode barang ke user disimpen di variabel x.
sitoserba insert x panggil fungsi insert di objek sitoserba buat masukin angkanya ke tree.
print Kode barang x berhasil dimasukkan ke sistem tunjukin pesan sukses.
except ValueError kalau user nginput huruf pas disuruh masukin kode barang.
print Input tidak valid Masukkan angka kasih pesan error ke layar.
elif pilih sama dengan dua kalau user milih menu nomor dua buat cari kode barang.
try siapin jebakan error lagi buat proses pencarian barang.
x sama dengan int input Cari kode barang minta user masukin angka kode barang yang mau dicari.
if sitoserba search x cek datanya pakai fungsi search kalau hasilnya True.
print Status Barang Ditemukan di Toko cetak pesan kalau barangnya beneran ada.
else kalau hasil search nya False.
print Status Barang Tidak Ada cetak pesan kalau barangnya emang gak ketemu.
except ValueError tangkep error kalau user masukin karakter selain angka pas nyari.
print Input tidak valid Masukkan angka tunjukin pesan error.
elif pilih sama dengan tiga kalau user milih menu nomor tiga buat lihat info stok.
print Kode barang terkecil sitoserba find min cetak teks info kode barang terkecil dari tree.
print Kode barang terbesar sitoserba find max cetak teks info kode barang terbesar.
print Total variasi barang di sistem sitoserba count nodes cetak jumlah total jenis barang.
elif pilih sama dengan empat kalau user milih menu empat buat keluar dari program.
print Program SiToserba selesai cetak ucapan perpisahan karena program berhenti.
else kalau angka yang diketik user bukan satu dua tiga atau empat.
print Pilihan tidak valid kasih tau ke user kalau menu yang dipilih gak ada.
if name sama dengan main baris standar python buat mastiin program dijalankan sebagai file utama.
main nah panggil fungsi main biar seluruh program kita mulai jalan.
D. Output Program image image

Penjelasan Output:

Saat kodingan ini di run, terminal bakal langsung nampilin judul "=== SiToserba: Manajemen Stok ===" sama 4 pilihan menu. Sistem bakal nunggu masukin angka. Misalnya , iseng masukin huruf A. Tapi udah ada try-except, jadi sistemnya nolak jadi nampilin: "Input tidak valid! Masukkan angka." terus otomatis balik nampilin menu lagi tanpa error atau force close.

Terus, jalanin yang benernya. Pilih menu 1 (Tambah Kode Barang), terus masukin angka 50. Program nampilin: "Kode barang 50 berhasil dimasukkan ke sistem." Terus ulang lagi cara ini dua kali berturut-turut buat masukin angka 30 dan 70. Di balik layar, sistem udah otomatis ngejadiin angka 50 sebagai akar atau root, angka 30 masuk ke cabang sebelah kiri karena lebih kecil, dan angka 70 ke cabang sebelah kanan karena lebih gede.

Buat ngebuktiin datanya beneran masuk, kita pilih menu 2 (Cari Kode Barang) dan nyari angka 30. Sistem bakal cepet banget nemuin dan nampilin tulisan: "Status: Barang Ditemukan di Toko!". Tapi misal iseng nyari angka 99 yang emang nggak pernah dimasukin, sistem langsung jawab: "Status: Barang Tidak Ada."

Selanjutnya, kalau mau liat rekap datanya, tinggal pilih menu 3 (Tampilkan Info Stok). Sistem bakal otomatis meluncur ke cabang mentok kiri buat dapet nilai terkecil, cabang mentok kanan buat nilai terbesar, dan ngitung semua node yang ada. Hasilnya langsung keluar kalau barang terkecilnya 30, terbesarnya 70, dan total jenis barangnya ada 3.

Kalau udah kelar , tinggal pencet menu 4 (Keluar). Terminal bakal nampilin tulisan program selesai, perulangannya putus, dan aplikasinya berhenti dengan aman.
