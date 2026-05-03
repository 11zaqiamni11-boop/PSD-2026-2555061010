**A. Judul Program**
PROGRAM PENGURUTAN STRUK BERDASARKAN TANGGAL TRANSAKSI MENGGUNAKAN INSERTION SORT

**B. Deskripsi Singkat**
Program tersebut berfungsi sebagai sistem sederhana untuk mencatat dan merapikan tumpukan struk atau nota berdasarkan tanggal transaksinya menggunakan algoritma Insertion Sort. Pengguna pertama-tama menentukan jumlah struk yang ingin dicatat, kemudian memasukkan nama/keterangan struk beserta angka tanggal transaksinya. Program dilengkapi dengan validasi input (penanganan *error*) untuk memastikan pengguna memasukkan format angka pada input yang membutuhkan tipe data *integer*. Struktur data yang digunakan dalam program ini adalah *list* 1 dimensi yang berisi elemen berupa *dictionary* (kamus). Setiap elemen *dictionary* tersebut menyimpan pasangan *key-value* untuk keterangan nama struk dan jumlah nominal tanggalnya. Operasi yang dilakukan meliputi penambahan data menggunakan *append*, penelusuran dan pencetakan data menggunakan perulangan *for*, serta pembandingan dan pergeseran data antar indeks di dalam *list* untuk menghasilkan urutan tanggal dari yang terkecil hingga terbesar.

**C. Source Code**
Penjelasan kode per baris:
1. Membuat fungsi `insertion_sort_struk(arr, n)` yang menerima parameter *list* `arr` dan jumlah elemen `n`.
2. Perulangan `for` untuk melakukan iterasi indeks `i` dari 1 sampai batas `n`, mengasumsikan elemen pertama (indeks 0) sudah berurutan.
3. Menyimpan elemen *list* pada indeks ke-`i` ke dalam variabel `temp` (sebagai elemen struk yang sedang dipegang dan akan disisipkan).
4. Membuat variabel `j` yang bernilai `i - 1` untuk mengecek elemen di sebelah kiri `temp`.
5. Perulangan `while` yang berjalan selama `j` bernilai lebih dari sama dengan 0 dan nilai parameter 'tanggal' pada indeks ke-`j` lebih besar dari nilai 'tanggal' pada variabel `temp`.
6. Memindahkan atau menggeser elemen yang lebih besar tersebut satu posisi ke kanan (`arr[j + 1] = arr[j]`) untuk membuat celah kosong.
7. Mengurangi nilai `j` sebesar 1 (`j -= 1`) agar program mengecek elemen di sebelah kirinya lagi.
8. Menyisipkan elemen dari variabel `temp` ke posisi celah yang tepat (`arr[j + 1] = temp`) setelah perulangan *while* berhenti.
9. Membuat fungsi `main()` sebagai program utama.
10. Program akan mencoba (`try`) mengeksekusi blok kode.
11. Meminta user untuk input jumlah tumpukan struk yang dikonversi ke tipe *integer* dan disimpan di variabel `n`.
12. Pengecualian (`except ValueError`) jika input yang dimasukkan user mengalami *error* (bukan angka).
13. Program akan mencetak "Input tidak valid!".
14. Perintah `return` untuk langsung menghentikan fungsi `main()` jika input di awal salah.
15. Membuat *list* `arr = []` yang masih kosong untuk menyimpan kumpulan data struk.
16. Mencetak perintah "Masukkan rincian struk:".
17. Perulangan `for` untuk menjalankan proses input data berulang kali sebanyak nilai `n`.
18. Mencetak nomor antrean struk yang sedang diinputkan.
19. Program meminta user untuk input nama/keterangan struk yang disimpan di variabel `nama` (bertipe *string*).
20. Perulangan `while True` agar program terus berjalan selama validasi input belum berhasil.
21. Program akan mencoba (`try`) mengeksekusi input tanggal.
22. Meminta user input tanggal transaksi yang dikonversi ke *integer* dan disimpan di variabel `tanggal`.
23. Menyimpan pasangan data `nama` dan `tanggal` ke dalam *list* `arr` dalam format *dictionary* menggunakan operasi `append`.
24. `break` berfungsi untuk menghentikan dan keluar dari perulangan `while` karena input tanggal sudah valid.
25. Pengecualian (`except ValueError`) jika *value* tanggal yang diinputkan *error* (berupa huruf atau simbol).
26. Program akan mencetak peringatan "Input tidak valid, silakan masukkan angka untuk tanggal!" dan meminta input kembali.
27. Mencetak garis pembatas dan teks awal tampilan hasil.
28. Mencetak teks "Kondisi Tumpukan Struk SEBELUM diurutkan:".
29. Perulangan `for` untuk melakukan iterasi pada elemen-elemen di dalam *list* `arr`.
30. Mencetak rincian nama dan tanggal setiap struk yang posisinya masih acak sesuai urutan saat user menginputnya.
31. Memanggil fungsi `insertion_sort_struk(arr, n)` untuk memproses algoritma pengurutan pada *list* `arr`.
32. Mencetak garis pembatas.
33. Mencetak teks "Kondisi Tumpukan Struk SETELAH diurutkan (Insertion Sort):".
34. Perulangan `for` kedua untuk melakukan iterasi ulang pada elemen *list* `arr` yang sudah diproses.
35. Mencetak rincian nama dan tanggal setiap struk yang sekarang posisinya sudah terurut dari tanggal awal hingga akhir.
36. *Entry point* (`if __name__ == "__main__":`), berfungsi agar program hanya berjalan saat *file* dieksekusi secara langsung.
37. Memanggil fungsi `main()` untuk menjalankan seluruh kode program di atasnya.

**D. Output Program**
Penjelasan Output: Saat program dijalankan, sistem pertama-tama akan meminta user untuk memasukkan jumlah tumpukan struk yang ingin diproses. Misalkan user menginputkan angka 3. Program kemudian akan meminta user untuk melengkapi rincian 3 struk tersebut. Pada Struk ke-1, user memasukkan keterangan "Makan Siang" dan menginputkan tanggal transaksi bernilai 15. Pada Struk ke-2, user memasukkan keterangan "Laundry" dengan tanggal bernilai 5. Selanjutnya pada Struk ke-3, user menginputkan keterangan "Isi Bensin" dengan tanggal bernilai 10. (Jika pada saat memasukkan tanggal user tidak sengaja mengetikkan huruf, program tidak akan *crash*, melainkan memunculkan pesan peringatan dan meminta user mengulang input tanggal tersebut). Setelah ketiga data masuk, program akan langsung menampilkan "Kondisi Tumpukan Struk SEBELUM diurutkan", yang mencetak deretan struk persis sesuai riwayat input (Tgl 15, Tgl 5, dan Tgl 10). Setelah itu, algoritma *Insertion Sort* bekerja di latar belakang, membandingkan tanggal dan menyisipkan data ke posisi yang benar. Program kemudian memunculkan hasil akhirnya pada bagian "Kondisi Tumpukan Struk SETELAH diurutkan", di mana daftar struk tersebut sekarang tercetak rapi berdasarkan urutan kalender: diawali Laundry (Tgl: 5), lalu Isi Bensin (Tgl: 10), dan diakhiri Makan Siang (Tgl: 15). Setelah menampilkan hasil akhir ini, eksekusi program selesai.
