A. Judul Program

PROGRAM E-LIVESTOCK: MANAJEMEN KAWANAN SAPI PAKE STRUKTUR DATA BINARY SEARCH TREE (BST)

B. Deskripsi Singkat

Program ini dibikin untuk nyimulasiin sistem pencatatan sapi di peternakan (E-Livestock) pake nomor tag telinga bentuk angka. Penyimpanannya ini pake konsep Binary Search Tree (BST). Bayangin aja datanya itu kayak silsilah pohon yang bercabang ke bawah. Aturannya : kalau nomor tag sapi yang baru masuk angkanya lebih kecil dari posisi data saat ini, dia bakal ke cabang kiri. Sebaliknya, kalau lebih gede, masuk ke cabang kanan.

Kelebihan program ini itu kalau mau nge-insert data ternak baru atau nyari rekam jejak sapi. Fitur utamanya ada tambah nomor tag, cari status sapi di kandang, sampai ngecek info populasi seperti nyari nomor tag paling kecil (biasanya sapi paling tua atau awal masuk), paling gede (sapi atau anak sapi baru), dan ngitung total populasi sapi yang udah terdaftar. Biar kodingannya gak gampang error atau mati sendiri pas di-run gara-gara user salah ngetik huruf (padahal disuruhnya angka), di codenya udah ada pengaman try-except. Kinerja program ini buat nyari data lumayan sat set alias O(log n), soalnya bisa langsung motong jalur pencarian jadi setengah tanpa harus ngecek datanya satu-satu dari awal.

C. Source Code

<img width="1919" height="995" alt="image" src="https://github.com/user-attachments/assets/97b66b66-e58c-4310-9ecd-c56a4fd0d759" />
<img width="1919" height="834" alt="image" src="https://github.com/user-attachments/assets/9d88cced-b4d3-4549-a2aa-01c52d64536f" />
<img width="1919" height="864" alt="image" src="https://github.com/user-attachments/assets/bbd2cf8e-3c6b-4b72-b172-62c59c7513c0" />
<img width="1919" height="520" alt="image" src="https://github.com/user-attachments/assets/bd142def-4332-4276-bcd6-707d3377b2d1" />

Penjelasan kode per baris:

1. class Node: Mendefinisikan kelas Node sebagai representasi dasar dari sebuah simpul (titik data) di dalam struktur pohon.
2. def init(self, key): Konstruktor kelas Node untuk menginisialisasi atribut pada saat objek simpul baru dibuat.
3. self.key = key: Menyimpan nilai nomor identifikasi (tag) sapi ke dalam atribut key pada simpul tersebut.
4. self.left = None: Menginisialisasi penunjuk (pointer) cabang kiri dengan nilai None atau kosong.
5. self.right = None: Menginisialisasi penunjuk (pointer) cabang kanan dengan nilai None atau kosong.
6. class BSTDasar: Mendefinisikan kelas utama BSTDasar yang memuat seluruh logika dan operasi algoritma Binary Search Tree.
7. def init(self): Konstruktor untuk menginisialisasi struktur pohon pencarian biner saat pertama kali diinstansiasi.
8. self.root = None: Menetapkan akar (root) pohon dengan nilai None, yang menandakan bahwa struktur pohon masih dalam keadaan kosong.
9. def insert_node(self, root, key): Metode rekursif untuk menambahkan simpul baru ke dalam posisi yang tepat di dalam hierarki pohon.
10. if root is None: Mengevaluasi kondisi batas (base case) di mana posisi simpul yang sedang diperiksa saat ini kosong.
11. return Node(key): Mengembalikan objek Node baru yang berisi data nomor tag apabila kondisi posisi kosong terpenuhi.
12. if key < root.key: Mengevaluasi apakah nilai yang akan dimasukkan lebih kecil dari nilai pada simpul saat ini.
13. root.left = self.insert_node(root.left, key): Memanggil metode secara rekursif untuk menempatkan data pada percabangan sebelah kiri.
14. elif key > root.key: Mengevaluasi apakah nilai yang akan dimasukkan lebih besar dari nilai pada simpul saat ini.
15. root.right = self.insert_node(root.right, key): Memanggil metode secara rekursif untuk menempatkan data pada percabangan sebelah kanan.
16. return root: Mengembalikan nilai referensi simpul saat ini untuk mempertahankan struktur referensi hierarki pohon.
17. def insert(self, key): Metode antarmuka (interface) publik untuk menyederhanakan pemanggilan operasi penambahan data.
18. self.root = self.insert_node(self.root, key): Memulai proses penambahan simpul dengan memanggil metode rekursif dari posisi akar pohon.
19. def search_node(self, root, key): Metode rekursif untuk melakukan pencarian nilai tertentu di dalam struktur pohon secara efisien.
20. if root is None: Mengevaluasi kondisi batas apabila penelusuran telah mencapai ujung pohon yang kosong.
21. return False: Mengembalikan nilai boolean False yang mengindikasikan bahwa data tidak ditemukan di dalam struktur.
22. if root.key == key: Mengevaluasi apakah nilai simpul saat ini sama persis dengan nilai yang sedang dicari.
23. return True: Mengembalikan nilai boolean True yang mengindikasikan bahwa proses pencarian berhasil menemukan data.
24. if key < root.key: Mengevaluasi apakah target nilai pencarian lebih kecil dari nilai simpul saat ini.
25. return self.search_node(root.left, key): Mengarahkan penelusuran pencarian secara rekursif ke percabangan sebelah kiri.
26. return self.search_node(root.right, key): Mengarahkan penelusuran pencarian secara rekursif ke percabangan sebelah kanan apabila nilainya lebih besar.
27. def search(self, key): Metode antarmuka publik untuk memudahkan proses pencarian data tanpa parameter akar eksternal.
28. return self.search_node(self.root, key): Memulai inisialisasi proses pencarian data mulai dari akar pohon.
29. def inorder(self, root): Metode penelusuran (traversal) memori pohon menggunakan kaidah Inorder (Kiri, Induk, Kanan).
30. if root is None: Memeriksa apakah simpul bernilai kosong untuk mencegah eksekusi berlebih pada fungsi rekursif.
31. return: Menghentikan eksekusi prosedur pada tingkat rekursi saat ini tanpa mengembalikan nilai pengembalian.
32. self.inorder(root.left): Menelusuri seluruh simpul yang berada pada sisi cabang kiri secara rekursif hingga batas terdalam.
33. print(root.key, end= ): Mencetak nilai memori simpul saat ini ke layar secara horizontal.
34. self.inorder(root.right): Melanjutkan penelusuran terhadap seluruh simpul yang berada pada cabang sebelah kanan.
35. def preorder(self, root): Metode penelusuran memori pohon menggunakan standar algoritma Preorder (Induk, Kiri, Kanan).
36. if root is None: Melakukan validasi eksistensi simpul untuk menghindari kesalahan komputasi pada memori kosong.
37. return: Menginstruksikan metode untuk berhenti mengeksekusi baris kode berikutnya pada cabang kosong.
38. print(root.key, end= ): Mencetak luaran nilai simpul induk terlebih dahulu sebelum melanjutkan penelusuran.
39. self.preorder(root.left): Meneruskan penelusuran secara menyeluruh pada sisi kiri simpul anak.
40. self.preorder(root.right): Meneruskan tahap penelusuran struktur pada bagian kanan simpul.
41. def postorder(self, root): Metode komputasi penelusuran pohon menggunakan pendekatan algoritma Postorder (Kiri, Kanan, Induk).
42. if root is None: Melakukan inspeksi keamanan untuk memastikan simpul saat ini berisi nilai referensi memori yang sah.
43. return: Melakukan penghentian komputasi pada pemanggilan rekursif saat berhadapan dengan memori yang nihil.
44. self.postorder(root.left): Memerintahkan sistem untuk melakukan penjelajahan penuh hingga ujung terdalam cabang kiri.
45. self.postorder(root.right): Melakukan penjelajahan ekuivalen pada struktur cabang anak sisi kanan.
46. print(root.key, end= ): Mencetak identitas memori induk setelah seluruh simpul anaknya selesai diproses.
47. def find_min(self, root): Metode ekstraksi untuk mendapatkan nilai memori paling kecil (minimum) dalam struktur memori pohon.
48. if root is None: Memvalidasi kondisi inisial untuk menjamin bahwa struktur pohon tidak dalam kondisi kosong sepenuhnya.
49. return -1: Menghasilkan kode luaran negatif (-1) sebagai indikator galat yang menyatakan ketiadaan data.
50. current = root: Mendeklarasikan variabel referensi current untuk melacak posisi simpul mulai dari tingkat akar.
51. while current.left is not None: Memulai siklus perulangan terstruktur selama penunjuk bagian kiri masih memiliki referensi isi memori.
52. current = current.left: Merelokasi titik evaluasi terus-menerus mengikuti rute penunjuk arah kiri.
53. return current.key: Menghasilkan pemulangan nilai atribut simpul paling kiri yang merepresentasikan angka minimum data.
54. def find_max(self, root): Fungsi struktural pencarian angka paling besar (maksimum) dari sekumpulan simpul dalam pohon data.
55. if root is None: Menginstruksikan pemeriksaan eksistensi akar demi menjaga keandalan evaluasi data selanjutnya.
56. return -1: Menyajikan kode resolusi galat -1 yang merepresentasikan entitas pohon dalam keadaan kosong.
57. current = root: Menetapkan deklarasi pelacakan titik simpul awal di bagian puncak memori akar.
58. while current.right is not None: Melangsungkan pengulangan pencarian sisi ekstrem selama dahan anak bagian kanan sah secara komputasional.
59. current = current.right: Memigrasikan pemeriksaan data operasional menuju arah dahan ekstrem kanan secara persisten.
60. return current.key: Mengekstraksi angka pengenal memori simpul posisi terkanan untuk menampilkan rekor nilai maksimum.
61. def count_nodes(self, root): Prosedur analitik berbasis rekursi komputasi guna menghitung keseluruhan akumulasi simpul penyusun jaringan memori pohon.
62. if root is None: Menerapkan mekanisme proteksi penelusuran untuk mengidentifikasi keberadaan memori referensi hampa pada pohon.
63. return 0: Mengembalikan hasil evaluasi kuantitatif dasar bernilai nol dikarenakan ketiadaan penambahan simpul.
64. return 1 + self.count_nodes(root.left) + self.count_nodes(root.right): Mengalkulasikan simpul komputasi saat ini ditambah pengumpulan rekursif kuantitas anak kiri dan sisi kanan.
65. def sum_nodes(self, root): Modul operasi agragasi yang bertujuan merekapitulasi beban seluruh isi konstanta tiap node data.
66. if root is None: Menegakkan uji awal agar algoritma tak terjebak melakukan ekstraksi kuantifikasi terhadap kekosongan node memori.
67. return 0: Menyudahi penjumlahan bagian tersebut dengan menginjeksikan indeks nol demi melindungi total akumulasi hitungan.
68. return root.key + self.sum_nodes(root.left) + self.sum_nodes(root.right): Mentotal akumulasi parameter isi node dengan penjumlahan berantai ke simpul sebelah kiri serta turunannya ke ujung kanan.
69. def main(): Pendeklarasian fungsi pusat (main method) yang menjadi entitas inisialisasi titik mula eksekusi modul operasi ini.
70. peternakan = BSTDasar(): Penginisialisasian (instansiasi) referensi kelas logis ke wujud memori aktual objek di variabel kerja.
71. pilih = 0: Penyediaan penampung variabel alur logika yang diberikan beban awal nilai nol untuk persiapan perulangan sistem pilihan.
72. while pilih != 4: Deklarasi penugasan berantai guna mewajibkan perputaran antarmuka konsol sebelum masukan akhir (4) divalidasi.
73. print( E-Livestock: Manajemen Kawanan Sapi ): Mengeksekusi penulisan keterangan tajuk program operasional menuju media antarmuka.
74. print(1. Tambah Nomor Tag Sapi): Mendesain tampilan referensi interaksi pengguna untuk perintah masukan input nomor individu baru.
75. print(2. Cari Nomor Tag Sapi): Menampilkan parameter instruksional di bagian menu pelacakan identitas subjek tertentu di pangkalan memori.
76. print(3. Tampilkan Info Populasi): Menyediakan menu tampilan analitik agregasi rangkuman status hierarki kumpulan data hewan komputasional.
77. print(4. Keluar): Memberikan tampilan antarmuka interupsi memori untuk terminasi fungsional aplikasi tersebut secara normal.
78. try: Mengawali area penjagaan lingkungan rentan masalah akibat masukan yang tidak menaati protokol operasi (eksepsi tipe memori).
79. pilih = int(input(Pilih: )): Memanggil konsol guna penyerapan karakter angka yang nantinya akan dikonversi ke mode variabel bilangan asli.
80. except ValueError: Mempertemukan lingkungan tangkapan jenis kegagalan pembacaan apabila format sandi angka tak sejalan.
81. print(Input tidak valid! Masukkan angka.): Melahirkan pesan verifikasi teknis sebagai pedoman perbaikan ketidaksesuaian input pemakai instrumen.
82. continue: Merestorasi pergerakan pengontrol siklus kembali menjangkau blok awal verifikasi tanpa membuat mesin program gagal (crash).
83. if pilih == 1: Mengeksekusi filter komputasional terhadap permintaan pilihan modul satu untuk penambahan identitas data.
84. try: Menjalankan perlindungan pemrosesan dari kesalahan tipe karakter ketika konsol meminta atribut numerik nomor hewan.
85. x = int(input(Masukkan nomor tag sapi (angka): )): Melakukan inisiasi fungsi pemasukan terminal, lalu segera melakukan konversi identitas masukan menjadi jenis integer.
86. peternakan.insert(x): Menerapkan fungsi prosedur penyisipan modul agar pangkalan data BST menyerap referensi integer ke dalam struktur memori.
87. print(Nomor tag sapi {x} berhasil dimasukkan ke sistem.): Mentransmisikan umpan balik positif pencetakan tanda keberhasilan pencatatan.
88. except ValueError: Melakukan pemonitoran atas indikasi penyimpangan format teks huruf agar modul algoritma terhindar dari pemaksaan numerik.
89. print(Input tidak valid! Masukkan angka.): Memberitahu pengguna bahwasanya konversi sistem tertunda dikarenakan parameter instruksi berupa angka tidak dipenuhi.
90. elif pilih == 2: Menangani seleksi logika alternatif tatkala entitas sistem pengguna menargetkan akses nomor dua sebagai langkah interaksi berikutnya.
91. try: Melingkupi baris sensitif operasional penelusuran supaya interupsi sintaks non-angka otomatis diredam oleh kurungan parameter pengaman.
92. x = int(input(Cari nomor tag sapi: )): Memproses ekstraksi identitas variabel angka tujuan investigasi berdasarkan interaksi karakter konsol dari sistem klien.
93. if peternakan.search(x): Memvalidasi respons sistem sesudah mekanisme penyisiran tereksekusi pada variabel numerik acuan dengan indikator luaran True.
94. print(Status: Sapi Terdaftar dan Ada di Kandang!): Mendistribusikan penegasan pesan teknis jika hasil uji logis mengonfirmasi validitas posisi node termaksud.
95. else: Menganalisis lintasan pemrograman seandainya instrumen logika search merespons status data numerik sebagai nilai mutlak False (negatif).
96. print(Status: Sapi Tidak Ditemukan dalam Data.): Mencetak pernyataan keterangan tidak hadirnya indikator referensi identifikasi tersebut dari kolektibilitas struktur pohon hierarki.
97. except ValueError: Memonitor peluang munculnya eror akibat pengalihan interupsi tipe nilai data yang luput dari identifikasi karakter masukan bilangan bulat numerik.
98. print(Input tidak valid! Masukkan angka.): Menyuguhkan peringatan komputasional guna menyesuaikan tipe data karakter agar sejalan dengan kriteria pencarian operasi algoritma sistem memori terstruktur.
99. elif pilih == 3: Mengimplementasikan penyaringan instruksi ketika kondisi bernilai absolut menunjukkan arah penelusuran operasi rekapitulasi data (seleksi menu 3).
100. print(Nomor tag terkecil (Paling Awal): {peternakan.find_min(peternakan.root)}): Merangkai penggabungan perintah pemanggilan metode nilai atribut terkecil serta membingkai hasil keluarannya pada konsol.
101. print(Nomor tag terbesar (Paling Baru): {peternakan.find_max(peternakan.root)}): Menginisiasi instruksi untuk menyerap nilai luaran batas puncak simpul referensi maksimal lalu diekstraksi ke antarmuka layar pengguna.
102. print(Total populasi sapi di sistem: {peternakan.count_nodes(peternakan.root)}): Menyalurkan parameter instruksional prosedur penotalan seluruh atribut titik memori dan ditranskripsikan ke dalam visual rekapitulasi total keseluruhan sapi.
103. elif pilih == 4: Melakukan proses inspeksi bersyarat pada perintah rute keempat sebagai representasi terminasi lingkungan kerja.
104. print(Program E-Livestock selesai.): Merilis respons penutupan aktivitas pemrosesan guna menginformasikan kepada pengguna bahwa rutinitas sistem secara aman telah direduksi untuk berhenti.
105. else: Melingkupi penanganan penyimpangan di segala kondisi numerik apabila opsi input gagal mencocokkan rentang menu rasional operasi pilihan.
106. print(Pilihan tidak valid!): Mentransmisikan instruksi penegasan kepada pengguna mengenai batasan akses fungsionalitas ketika karakter di luar matriks ketentuan menu operasi diterapkan.
107. if name == main: Blok instruksi kondisional terstandar pada bahasa pemrograman Python guna memverifikasi bahwasanya file instruksi sedang dijalankan independen, bukan proses pemanggilan (import) pustaka.
108. main(): Menyelesaikan rangkaian operasi dengan mengaktifkan resolusi blok kode fungsi mula, membangkitkan eksekusi fungsionalitas skrip pengolahan program dari titik referensi utama.

D. Output Program

<img width="1919" height="997" alt="image" src="https://github.com/user-attachments/assets/06447154-99ce-4638-aba6-e790e8093225" />
<img width="1919" height="707" alt="image" src="https://github.com/user-attachments/assets/1e7c2d96-1aeb-4512-baec-decbfb2a88c4" />

Penjelasan Output:
Saat kodingan ini di-run, terminal bakal nampilin judul E-Livestock: Manajemen Kawanan Sapi sama 4 pilihan menu. Sistem bakal nunggu masukin angka. Misalnya, iseng masukin huruf A. Tapi udah ada try-except, jadi sistemnya nolak jadi nampilin: Input tidak valid! Masukkan angka. terus otomatis balik nampilin menu lagi tanpa error atau force close.

Terus, jalanin yang benernya. Pilih menu 1 (Tambah Nomor Tag Sapi), terus masukin angka 50 (misalnya anak sapi baru lahir atau sapi Limosin baru datang). Program nampilin: Nomor tag sapi 50 berhasil dimasukkan ke sistem. Terus ulang lagi cara ini dua kali berturut-turut buat masukin angka 30 dan 70. Di balik layar, sistem udah otomatis ngejadiin angka 50 sebagai akar atau root, angka 30 masuk ke cabang sebelah kiri karena lebih kecil, dan angka 70 ke cabang sebelah kanan karena lebih gede.

Buat ngebuktiin datanya beneran masuk, pilih menu 2 (Cari Nomor Tag Sapi) dan nyari angka 30. Sistem bakal nemuin dan nampilin tulisan: Status: Sapi Terdaftar dan Ada di Kandang!. Tapi misal iseng nyari angka 99 yang emang nggak pernah dimasukin, sistem langsung nampilin: Status: Sapi Tidak Ditemukan dalam Data.

Lanjut, kalau mau liat rekap datanya, tinggal pilih menu 3 (Tampilkan Info Populasi). Sistem bakal otomatis menuju ke cabang mentok kiri buat dapet nilai terkecil, cabang mentok kanan buat nilai terbesar, dan ngitung semua node yang ada. Hasilnya langsung keluar kalau tag sapi terkecilnya 30, terbesarnya 70, dan total populasinya ada 3 ekor.

Kalau udah selesai, tinggal pencet menu 4 (Keluar). Terminal bakal nampilin tulisan program selesai, perulangannya putus, dan aplikasinya berhenti dengan aman.
