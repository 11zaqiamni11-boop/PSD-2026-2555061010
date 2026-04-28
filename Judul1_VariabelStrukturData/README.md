A. Judul Program
PROGRAM PENCATATAN PENGELUARAN HARIAN

B. Deskripsi Singkat
Program tersebut berfungsi sebagai sistem sederhana untuk pencatatan pengeluaran harian.
Pengguna dapat menambahkan data pengeluaran dan nominalnya, melihat daftar catatan yang sudah dimasukkan, 
dan mengedit data pengeluaran yang ada. Program berjalan dalam loop hingga pengguna memilih untuk keluar dari program. 
Selain itu, program juga dilengkapi dengan validasi input untuk memastikan data yang dimasukkan sesuai dan tidak menimbulkan error. 
Struktur data yang digunakan dalam program ini adalah list 1 dimensi, yaitu variabel pengeluaran yang menyimpan kumpulan data dalam bentuk list. 
Setiap elemen dalam list tersebut berupa tuple (keterangan, nominal) yang menyimpan pasangan keterangan pengeluaran dan jumlah nominalnya.
Operasi yang dilakukan meliputi penambahan data menggunakan append, penelusuran data menggunakan perulangan for, serta pembaruan data berdasarkan indeks.
Judul program

C. Source Code
<img width="1902" height="1018" alt="image" src="https://github.com/user-attachments/assets/59e2ecc3-df5c-4a88-93b5-f336ecf772d0" />
<img width="1900" height="990" alt="image" src="https://github.com/user-attachments/assets/6a57c508-7e5c-459e-ba39-76f6a75282e5" />

Penjelasan kode per baris:

1.Membuat fungsi menu()

2.Mencetak menu pertama untuk memasukkan keterangan dan nominal pengeluaran

3.Mencetak menu kedua untuk menampilkan catatan pengeluaran

4.Mencetak menu ketiga untuk edit keterangan dan nominal pengeluaran

5.Mencetak menu keempat untuk keluar dari program

6.Membuat fungsi main() sebagai program utama

7.Membuat list variabel pengeluaran = [ ] yang masih berupa list kosong

8.Membuat variabel running yang bernilai boolean True agar program berjalan

9.Perulangan while yang membuat program terus berjalan selama kondisi True

10.Menampilkan fungsi menu()

11.Program akan mencoba (try)

12.Meminta user untuk input pilihan menu yang bernilai integer

13.Pengecualian (except) jika value yang diinputkan error

14.Program akan meminta user untuk memasukkan angka yang valid

15continue berfungsi untuk membuat program kembali ke looping awal

16.Pengondisian (if) jika user memilih menu 1

17.Program meminta user untuk input keterangan pengeluaran yang akan disimpan di variabel keterangan

18.Perulangan (while) saat kondisi True

19.Program akan mencoba (try)

20.Meminta user untuk input nominal pengeluaran yang akan disimpan pada variabel nominal

21.break berfungsi untuk mengeluarkan dari perulangan

22.Pengondisian (except) jika value yang diinputkan error

23.Program akan mencetak "Input tidak valid, silakan masukkan angka!" dan meminta untuk memasukkan angka lagi

24.Input keterangan pengeluaran dan nominal pengeluaran yang valid akan tersimpan di list pengeluaran menggunakan operasi append

25.Pengondisian (elif) jika user memilih menu 2

26.Kondisi (if not) jika variabel pengeluaran adalah list kosong

27.Program mencetak “Belum ada data pengeluaran, silakan input terlebih dahulu.”

28.else, kondisi jika list pengeluaran sudah terisi

29.Program akan menampilkan catatan pengeluaran

30.Mencetak garis pembatas

31.Perulangan for untuk melakukan iterasi dengan operasi enumerate, keterangan dan nominal yang ada pada list pengeluaran

32.Mencetak nomor pengeluaran, yaitu index ditambah satu, keterangan pengeluaran, dan jumlah nominalnya

33.Mencetak garis pembatas

34.Pengondisian (elif) jika user memilih menu 3

35.Kondisi (if not) jika variabel pengeluaran adalah list kosong

36.Program akan mencetak “Belum ada data pengeluaran, silakan input terlebih dahulu”

37.else, kondisi jika list pengeluaran sudah terisi

38.Program akan mencoba (try)

39.Meminta user untuk input nomor pengeluaran yang akan di edit dan disimpan pada variabel index (dikurangi 1 agar sesuai dengan index list)

40.Jika index ada di antara 0 dan jumlah karakter pada list pengeluaran

41.Program meminta user untuk input keterangan baru

42.Perulangan (while) jika kondisi True

43.Program akan mencoba (try)

44.Meminta user untuk input nominal baru yang bernilai integer

45.break berfungsi untuk mengeluarkan dari perulangan

46.Kondisi (except) jika value yang diinputkan error

47.Program mencetak “Input tidak valid, silakan masukkan angka!”

48.Keterangan pengeluaran dan nominal pengeluaran yang baru diedit akan terupdate di list pengeluaran sesuai posisi indexnya

49.else, kondisi jika nomor pengeluaran yang diinputkan user tidak ada di dalam list

50.Program akan mencetak "Nomor pengeluaran tidak valid."

51.Jika value error (except ValueError) saat user input nomor pengeluaran

52.Program mencetak “Input tidak valid, silakan masukkan angka!”

53.Pengondisian (elif) jika user input menu 4

54.Variabel running akan diubah menjadi False sehingga perulangan program berhenti

55.Mencetak “Program selesai.”

56.Kondisi (else) jika user menginputkan selain angka 1, 2, 3 dan 4

57.Program mencetak "Pilihan tidak valid!"

58.Entry point (if __name__ == "__main__":), agar program hanya berjalan saat file dijalankan langsung, dan jika diimport ke file lain program tidak otomatis berjalan.

D. Output Program
<img width="1382" height="645" alt="image" src="https://github.com/user-attachments/assets/a0e7b1fa-1215-48a0-8cb6-6a14d923d613" />
<img width="1141" height="440" alt="image" src="https://github.com/user-attachments/assets/33fd0721-d72a-48e0-bf8d-a936127c2147" />

Penjelasan Output: Program akan langsung menampilkan menu saat dijalankan dan meminta user untuk menginputkan pilihan menu yang diinginkan. 
Saat user memilih menu 1, program meminta user untuk menginputkan keterangan pengeluaran yang diisi “makan siang” dan menginputkan nominal pengeluaran yang diiisi 50000 oleh user.
Selanjutnya, program akan melakukan perulangan dengan menampilkan menu. Selanjutnya, user memilih menu 1 lagi dengan menginputkan bensin dengan nominalnya yang berjumlah 20000. 
Program akan mengulang dan menampilkan menu kembali. Tahap selanjutnya, user memilih menu 2. Program menampilkan data catatan pengeluaran yang sebelumnya sudah diinputkan oleh user.
Lalu, program akan kembali ke menu dan user menginputkan menu 3. Program akan meminta user untuk menginput nomor pengeluaran yang ingin diedit. User ingin mengedit pengeluaran nomor 2, yaitu bensin. 
User menginputkan keterangan baru, yaitu isi bensin motor. Lalu, user mengedit jumlah nominal isi bensin motor menjadi 25000.
Selanjutnya, user menginputkan menu 2 untuk menampilkan kembali data catatan pengeluaran setelah melakukan perubahan dan program pun menampilkan catatan pengeluaran yang sudah diupdate.
Selanjutnya, user memilih menu 4 dan program telah selesai dijalankan.

E. Link Youtube
