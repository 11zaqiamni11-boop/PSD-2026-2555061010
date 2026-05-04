A. Judul Program
PROGRAM PENGURUTAN STRUK BERDASARKAN TANGGAL TRANSAKSI MENGGUNAKAN INSERTION SORT

B. Deskripsi Singkat
Program tersebut berfungsi sebagai sistem sederhana untuk mencatat dan merapikan tumpukan struk atau nota berdasarkan tanggal transaksinya menggunakan algoritma Insertion Sort. Pengguna pertama-tama menentukan jumlah struk yang ingin dicatat, kemudian memasukkan nama/keterangan struk beserta angka tanggal transaksinya. Program dilengkapi dengan validasi input (penanganan error) untuk memastikan pengguna memasukkan format angka pada input yang membutuhkan tipe data integer. Struktur data yang digunakan dalam program ini adalah list 1 dimensi yang berisi elemen berupa dictionary (kamus). Setiap elemen dictionary tersebut menyimpan pasangan key-value untuk keterangan nama struk dan jumlah nominal tanggalnya. Operasi yang dilakukan meliputi penambahan data menggunakan append, penelusuran dan pencetakan data menggunakan perulangan for, serta pembandingan dan pergeseran data antar indeks di dalam list untuk menghasilkan urutan tanggal dari yang terkecil hingga terbesar.

C. Source Code
<img width="1919" height="1020" alt="image" src="https://github.com/user-attachments/assets/5c98c5b2-4aa6-4d64-8320-36ecd551f8a9" />

Penjelasan kode per baris:
1. #PROGRAM PENGURUTAN STRUK BERDASARKAN TANGGAL TRANSAKSI MENGGUNAKAN INSERTION SORT Merupakan baris komentar (ditandai dengan # ) yang berisi judul program. Baris ini tidak akan dieksekusi oleh Python dan hanya berfungsi sebagai catatan.

3. def insertion_sort_struk(arr, n): Mendefinisikan fungsi bernama insertion_sort_struk yang membutuhkan dua parameter: arr (list data) dan n (jumlah data).
 
5. for i in range(1, n): Memulai perulangan (looping) dari indeks 1 sampai batas n. Indeks 0 dilewati karena dianggap sudah berada di posisi yang benar.
 
7. temp = arr[i] Menyimpan elemen list pada indeks ke-i ke dalam variabel sementara bernama temp. Ini adalah data struk yang sedang dicarikan posisinya.
 
9. j = i - 1 Membuat variabel j untuk menunjuk ke indeks elemen yang berada tepat di sebelah kiri temp.
 
11. while j >= 0 and arr[j]['tanggal'] > temp['tanggal']: Memulai perulangan bersyarat. Looping berjalan selama masih ada elemen di sebelah kiri (j >= 0) DAN nilai tanggal dari elemen di sebelah kiri tersebut lebih besar dari nilai tanggal temp.
 
13. arr[j + 1] = arr[j] Jika kondisi terpenuhi, elemen di sebelah kiri yang lebih besar itu digeser satu posisi ke kanan untuk menyediakan ruang kosong.
 
15. j -= 1 Mengurangi nilai j dengan 1 agar program mengecek elemen yang posisinya lebih ke kiri lagi pada perulangan while berikutnya.
 
17. arr[j + 1] = temp Menyisipkan data yang ada di variabel temp ke dalam ruang kosong (j + 1) yang sudah ditemukan setelah perulangan while berhenti.
 
19. def main(): Mendefinisikan fungsi main yang akan menjadi alur utama berjalannya program.
 
21. try: Membuka blok error handling untuk menangkap potensi error saat pengguna memasukkan data awal.
 
23. n = int(input("Masukkan jumlah tumpukan struk/nota: ")) Meminta pengguna memasukkan jumlah struk, mengonversinya menjadi angka bulat (integer), dan menyimpannya di variabel n.
    
25. except ValueError: Blok penangkap error yang aktif jika pengguna memasukkan data selain angka (misal huruf/simbol).
    
27. print("Input tidak valid!") Mencetak pesan kesalahan ke layar karena input bukan angka.
    
29. return Menghentikan secara langsung fungsi main agar program tidak berlanjut dengan data yang salah.
    
31. arr = [] Mendeklarasikan sebuah list kosong bernama arr untuk menyimpan semua rincian struk.
    
33. print("Masukkan rincian struk:") Mencetak instruksi pengisian data ke layar.
    
35. for i in range(n): Melakukan perulangan sebanyak n kali untuk mengambil rincian data setiap struk.
    
37. print(f"\n Struk ke-{i+1} ") Mencetak penanda urutan struk (misal: "Struk ke-1"). Indeks ditambah 1 karena perulangan Python dimulai dari 0.
    
39. nama = input("Keterangan/Nama Struk (misal: Laundry, Makan): ") Meminta input teks dari pengguna untuk keterangan struk dan menyimpannya di variabel nama.
    
41. while True: Membuka perulangan tak terbatas agar program bisa terus meminta input tanggal jika pengguna salah memasukkan format.
    
43. try: Membuka blok error handling khusus untuk validasi input tanggal.
    
45. tanggal = int(input("Tanggal transaksi (1-31): ")) Meminta input tanggal, memaksanya menjadi integer, dan menyimpannya di variabel tanggal.
    
47. arr.append({'nama': nama, 'tanggal': tanggal}) Menggabungkan variabel nama dan tanggal menjadi satu dictionary, lalu menambahkannya ke dalam list arr.
    
49. break Menghentikan perulangan while True karena data tanggal sudah berhasil dan valid dimasukkan.
    
51. except ValueError: Menangkap error jika pengguna mengetikkan selain angka pada input tanggal.
    
53. print("Input tidak valid, silakan masukkan angka untuk tanggal!") Mencetak peringatan. Setelah ini, program otomatis mengulang ke baris 21 untuk menanyakan tanggal kembali.
 
55. print("Kondisi Tumpukan Struk SEBELUM diurutkan:") Mencetak teks judul untuk daftar struk acak.
 
57. for struk in arr: Melakukan iterasi untuk membaca setiap elemen dictionary di dalam list arr.
 
59. print(f"- {struk['nama']} (Tgl: {struk['tanggal']})") Mencetak nama dan tanggal struk ke layar. Pada titik ini, urutannya masih acak sesuai input pengguna.
 
61. insertion_sort_struk(arr, n) Memanggil fungsi algoritma Insertion Sort dengan membawa list arr dan jumlah n agar diproses menjadi berurutan.
 
63. print("Kondisi Tumpukan Struk SETELAH diurutkan (Insertion Sort):") Mencetak teks judul untuk daftar struk yang sudah rapi.
 
65. for struk in arr: Melakukan iterasi kembali pada list arr. Karena fungsi sort sudah dipanggil, isi list ini sekarang sudah berubah urutannya.
 
67. print(f"- {struk['nama']} (Tgl: {struk['tanggal']})") Mencetak hasil akhir nama dan tanggal struk ke layar, yang kini sudah terurut dari tanggal terkecil ke terbesar.
 
69. if __name__ == "__main__": Pengkondisian untuk memastikan bahwa kode di bawahnya hanya dieksekusi jika file ini dijalankan secara langsung (bukan saat di-import oleh file lain).
    
71. main() Memanggil fungsi main(), yang memicu seluruh alur program dari baris 10 hingga 34 untuk mulai berjalan.
    
D. Output Program
Penjelasan Output: Saat program dijalankan, sistem pertama-tama akan meminta user untuk memasukkan jumlah tumpukan struk yang ingin diproses. Misalkan user menginputkan angka 3. Program kemudian akan meminta user untuk melengkapi rincian 3 struk tersebut. Pada Struk ke-1, user memasukkan keterangan "Makan Siang" dan menginputkan tanggal transaksi bernilai 15. Pada Struk ke-2, user memasukkan keterangan "Laundry" dengan tanggal bernilai 5. Selanjutnya pada Struk ke-3, user menginputkan keterangan "Isi Bensin" dengan tanggal bernilai 10. (Jika pada saat memasukkan tanggal user tidak sengaja mengetikkan huruf, program tidak akan crash, melainkan memunculkan pesan peringatan dan meminta user mengulang input tanggal tersebut). Setelah ketiga data masuk, program akan langsung menampilkan "Kondisi Tumpukan Struk SEBELUM diurutkan", yang mencetak deretan struk persis sesuai riwayat input (Tgl 15, Tgl 5, dan Tgl 10). Setelah itu, algoritma Insertion Sort bekerja di latar belakang, membandingkan tanggal dan menyisipkan data ke posisi yang benar. Program kemudian memunculkan hasil akhirnya pada bagian "Kondisi Tumpukan Struk SETELAH diurutkan", di mana daftar struk tersebut sekarang tercetak rapi berdasarkan urutan kalender: diawali Laundry (Tgl: 5), lalu Isi Bensin (Tgl: 10), dan diakhiri Makan Siang (Tgl: 15). Setelah menampilkan hasil akhir ini, eksekusi program selesai.
