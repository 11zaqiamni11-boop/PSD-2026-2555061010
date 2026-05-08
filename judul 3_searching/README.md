A. Judul Program
PROGRAM VERIFIKASI ID REGISTRASI SEMINAR MENGGUNAKAN BINARY SEARCH

B. Deskripsi Singkat
Program tersebut berfungsi sebagai sistem verifikasi untuk mengecek apakah ID peserta sudah terdaftar dalam sistem registrasi seminar menggunakan algoritma Binary Search. Pengguna pertama-tama menentukan jumlah data ID peserta yang ingin dimasukkan ke dalam sistem. Kemudian pengguna memasukkan ID peserta secara berurutan dari yang terkecil hingga terbesar (urut menaik) karena ini merupakan syarat mutlak agar Binary Search dapat bekerja. Program dilengkapi dengan validasi input (penanganan error) menggunakan *try-except* untuk memastikan pengguna tidak memasukkan huruf/simbol saat sistem meminta tipe data integer. Struktur data yang digunakan dalam program ini adalah list 1 dimensi. Operasi yang dilakukan meliputi penambahan data menggunakan *append*, serta pencarian data dengan cara membagi list menjadi dua bagian secara berulang (menentukan indeks batas kiri, batas kanan, dan median) hingga ID target ditemukan atau hingga disimpulkan bahwa ID tersebut tidak ada dalam sistem. Program ini memiliki tingkat efisiensi pencarian $O(\log n)$.

C. Source Code
<img width="1918" height="1002" alt="image" src="https://github.com/user-attachments/assets/0a3f4a1a-7ade-47b2-b86a-7ffba28725e2" />
<img width="1907" height="432" alt="image" src="https://github.com/user-attachments/assets/387fbc9b-72a6-4a04-92ef-b2b21f3c3ed6" />

Penjelasan kode per baris:
1. `def binary_search(arr, n, target):` : Bikin fungsi bernama `binary_search` yang minta tiga parameter masukan: `arr` (list/array datanya), `n` (jumlah datanya), dan `target` (ID yang mau dicari).
2. `l = 0` : Deklarasi variabel `l` (left) diisi 0. Ini dipakai buat nandain batas pencarian paling kiri alias indeks pertama.
3. `r = n - 1` : Deklarasi variabel `r` (right) diisi `n - 1`. Ini buat nandain batas pencarian paling kanan alias indeks terakhir.
4. `pos = -1` : Bikin variabel `pos` (posisi) dan di-set -1. Ini nilai *default* yang bakal dikembaliin kalau ternyata datanya nggak ketemu.
5. `while l <= r:` : Buka perulangan `while` yang bakal jalan terus-menerus selama batas kiri belum ngelewati batas kanan.
6. `m = l + (r - l) // 2` : Ngitung indeks tengah (median) lalu disimpen ke variabel `m`. Rumus ini dipakai biar aman dan nggak kena *integer overflow* kalau datanya super banyak.
7. `print(f"Median: {m}, nilai: {arr[m]}")` : Nyetak info ke layar biar kita bisa lihat algoritma ini lagi ada di indeks median berapa dan nilainya apa.
8. `if arr[m] == target:` : Mengecek, apakah data di posisi tengah itu nilainya udah sama persis kayak `target` yang lagi dicari?
9. `pos = m` : Kalau kondisinya benar (sama), simpen nilai indeks tengah `m` itu ke dalam variabel `pos`.
10. `break` : Langsung hentiin paksa perulangan `while` karena datanya udah ketemu, jadi nggak perlu nyari lagi.
11. `elif arr[m] < target:` : Kalau ternyata salah, cek lagi apakah data di posisi tengah itu lebih kecil dari `target`?
12. `print("Mencari di kanan")` : Kalau iya, cetak teks ini buat ngasih tau pencarian geser ke belahan kanan array.
13. `l = m + 1` : Geser batas kiri jadi `m + 1`. Artinya, kita buang setengah data bagian kiri karena udah pasti target nggak ada di sana.
14. `else:` : Kondisi sisa kalau ternyata data di tengah lebih besar dari `target`.
15. `print("Mencari di kiri")` : Cetak teks ini buat ngasih tau pencarian geser ke belahan kiri array.
16. `r = m - 1` : Geser batas kanan jadi `m - 1`. Artinya, setengah data bagian kanan kita buang dari area pencarian.
17. `return pos` : Balikin nilai yang ada di variabel `pos` ke program utama yang manggil fungsi ini.
18. `def main():` : Bikin fungsi `main` yang bakal jadi kerangka utama alur berjalannya program kita.
19. `print("--- Sistem Verifikasi ID Registrasi Seminar ---")` : Nyetak judul program ke layar terminal.
20. `try:` : Buka blok *error handling* (penanganan error) buat ngejaga kalau-kalau user masukin data yang aneh.
21. `n = int(input("Masukkan jumlah elemen (peserta): "))` : Minta user nginput jumlah peserta, paksa ubah jadi integer (angka), terus simpen di variabel `n`.
22. `except ValueError:` : Blok ini bakal jalan cuma kalau terjadi error `ValueError` (misalnya user iseng masukin huruf pas disuruh masukin angka).
23. `print("Input tidak valid!")` : Nyetak pesan peringatan ke user kalau inputnya salah.
24. `return` : Menghentikan fungsi `main` sepenuhnya biar program langsung kelar saat itu juga.
25. `arr = []` : Deklarasiin variabel `arr` sebagai list kosong buat nampung semua ID peserta nanti.
26. `print("Masukkan elemen ID (urut menaik):")` : Nyetak instruksi ke layar biar user tahu mereka harus masukin ID satu-satu dan wajib urut.
27. `for i in range(n):` : Buka perulangan `for` yang bakal muter sebanyak `n` kali buat ngumpulin input ID.
28. `while True:` : Buka perulangan tak terbatas di dalam `for`. Gunanya biar kalau user ngetik huruf, programnya nggak *crash* tapi ngulang minta input di posisi yang sama.
29. `try:` : Buka blok penanganan error lagi, khusus buat inputan ID.
30. `nilai = int(input())` : Minta user ngetik ID, dipaksa jadi integer, dan disimpen ke variabel `nilai`.
31. `arr.append(nilai)` : Tambahin data ID yang ada di variabel `nilai` ke dalam barisan paling belakang list `arr`.
32. `break` : Keluar dari perulangan `while True` karena input ID-nya valid (berupa angka) dan udah masuk list.
33. `except ValueError:` : Nangkep error kalau user ngetik huruf atau simbol pas masukin ID.
34. `print("Input tidak valid, silakan masukkan angka!")` : Nyetak pesan teguran, habis ini otomatis bakal muter ke baris 29 lagi buat minta ID yang bener.
35. `print(f"Array: {arr}")` : Nampilin semua isi list `arr` ke layar biar user bisa ngecek datanya.
36. `while True:` : Buka perulangan tak terbatas lagi, sekarang buat proses input target pencarian.
37. `try:` : Buka blok penanganan error buat ngejaga input ID target.
38. `target = int(input("Masukkan ID peserta yang ingin dicari: "))` : Minta input ID yang mau dicari, jadikan integer, simpen di variabel `target`.
39. `break` : Berhentiin perulangan `while True` karena input targetnya sukses (berupa angka valid).
40. `except ValueError:` : Nangkep error kalau user malah ngetik huruf di input pencarian ini.
41. `print("Input tidak valid, silakan masukkan angka!")` : Nyetak teguran, terus ngulang lagi nanya input targetnya.
42. `pos = binary_search(arr, n, target)` : Manggil fungsi `binary_search` yang ada di atas, ngirim data `arr`, `n`, dan `target`, lalu hasil kembaliannya (indeks posisinya) disimpen ke variabel `pos`.
43. `if pos != -1:` : Bikin kondisi buat ngecek, apakah hasil `pos` bukan -1? (Artinya ID-nya berhasil ketemu).
44. `print(f"ID Valid! Ditemukan pada indeks ke-{pos}")` : Kalau benar, cetak keterangan kalau ID valid dan kasih tau ada di indeks ke berapa.
45. `else:` : Kondisi sebaliknya kalau nilai `pos` tetap -1 (artinya data emang nggak ada).
46. `print("ID Tidak ditemukan dalam sistem")` : Cetak informasi ke layar kalau ID tersebut nggak terdaftar.
47. `if __name__ == "__main__":` : Ini baris khusus di Python buat mastiin kode di bawahnya cuma jalan kalau file ini dieksekusi langsung (bukan numpang di-import sama file lain).
48. `main()` : Manggil fungsi `main()` buat mulai ngejalanin semua logika programnya dari awal.

D. Output Program
<img width="1918" height="580" alt="image" src="https://github.com/user-attachments/assets/8ca59cbd-830e-4d80-844f-af4963fc7874" />

Penjelasan Output: Saat program dijalankan, sistem pertama-tama mencetak judul "--- Sistem Verifikasi ID Registrasi Seminar ---" dan meminta user memasukkan jumlah elemen (peserta). Misalkan user menginputkan angka 5. Program kemudian akan mencetak instruksi untuk memasukkan 5 data ID secara berurutan (urut menaik). User memasukkan 101, 105, 110, 115, dan 120. (Apabila user mengetik huruf saat input ini, program akan mencetak pesan "Input tidak valid, silakan masukkan angka!" dan meminta angka diulang tanpa *crash*). Program kemudian menampilkan list utuhnya: `Array: [101, 105, 110, 115, 120]`. Selanjutnya, sistem meminta user memasukkan ID yang ingin dicari. Misal user mencari "115". Algoritma Binary Search mulai berjalan di latar belakang dan mencetak prosesnya ke layar. Pertama, algoritma mengecek nilai tengah (`Median: 2, nilai: 110`). Karena 110 lebih kecil dari 115, program mencetak `Mencari di kanan`. Algoritma menentukan median baru dari sisa area (`Median: 3, nilai: 115`). Karena nilai sekarang cocok dengan yang dicari, pencarian berhenti. Di akhir eksekusi, program akan mencetak hasil akhir: "ID Valid! Ditemukan pada indeks ke-3". Sebaliknya, jika user sedari awal memasukkan ID yang tidak terdaftar (misal 999), proses median akan terus bergeser hingga area pencarian habis dan pada akhirnya program akan mencetak "ID Tidak ditemukan dalam sistem".
