A. Judul Program
PROGRAM SIMULASI PEMBUATAN ECOBRICK MENGGUNAKAN STRUKTUR DATA STACK (ARRAY)

B. Deskripsi Singkat
Program ini dibuat untuk menyimulasikan proses pemadatan sampah plastik dalam pembuatan ecobrick. Karena ecobrick pada dasarnya adalah botol yang diisi tumpukan sampah plastik lapis demi lapis, sistem penyimpanannya sangat cocok direpresentasikan dengan struktur data Stack yang punya prinsip LIFO (Last In, First Out). Artinya, sampah yang paling terakhir ditekan masuk ke botol bakal jadi sampah yang pertama kali bisa diambil kalau misalnya kita butuh membongkarnya.

Program ini menggunakan metode Array (pakai List bawaan Python) dan membatasi ukuran maksimalnya agar mirip kapasitas asli botol yang terbatas. Operasi intinya ada Push buat masukin sampah baru, Pop buat ngeluarin sampah yang paling atas (berguna banget kalau kita tidak sengaja masukin material yang salah seperti tisu basah/kotor), dan Peek untuk ngecek sampah apa yang posisinya ada di bawah leher botol banget. Biar aman dari crash saat dijalankan, program juga dikasih validasi try-except buat nge- handle kalau user iseng ngetik huruf pas disuruh milih menu angka. Tingkat efisiensi buat nambah atau ngambil data di program ini sangat cepat, yaitu konstan O(1), karena ini menggunakan indeks teratasnya saja tanpa perlu geser-geser data lain.
