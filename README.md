# TUGAS_PERTEMUAN_9
_________________________________________________________________________________

Jadi pada pertemuan ini saya diberikan beberapa tugas oleh dosen saya yaitu diantaranya:

## LAB 4

![Latihan 1](https://github.com/HamdanAlWahidan/TUGAS_PERTEMUAN7/blob/main/Pertemuan7/latihan1.png) <br>

![Latihan 1.1](https://github.com/HamdanAlWahidan/TUGAS_PERTEMUAN7/blob/main/Pertemuan7/latihan1.png) <br>

Pada tugas LAB 4, saya diminta untuk membuat sebuah program menambahkan data ke sebuah list yang nantinya akan menghasilkan output seperti gambat diatas.
Untuk bisa dapat menghasilkan output tersebut maka saya memasukan script:

```
print("========Program Input Nilai =========")
data={}
tambahdata = 100
for i in range(tambahdata):
    while True:
        c = input("Tambah data (y/t)")
        if c.lower() == 'y':
            print("=======Tambah Data===")
            nama    =input("Nama                :  ")
            nim     =input("NIM                 :  ")
            tugas   =int(input("Masukan Nilai Tugas :  "))
            uts     =int(input("Masukan Nilai UTS   :  "))
            uas     =int(input("Masukan Nilai UAS   :  "))
            akhir   = (0.30 * tugas) + (0.35 * uts) + (0.35 * uas)
            data[nama] = nim ,tugas, uts, uas, akhir
            continue

        elif c.lower() == 't':
            if data.items():
                print("Daftar Nilai Mahasiswa")
                print("================================================================================================")
                print(" |NO   |     NAMA      |    NIM    |     TUGAS    |     UTS     |       UAS    |    AKHIR     | ")
                print("================================================================================================")
                i=0
                for x in data.items():
                    i+=1
                    print(" | {6:2}  |  {0:12s} | {1:9s} | {2:11}  | {3:11} | {4:11}  |  {5:11} |".format(x[0], x[1][0], x[1][1], x[1][2], x[1][3], x[1][4], i))
                    print("============================================================================================")

```
Jika sudah memasukan semua script diatas dan telah di run, maka kamu akan mendapatkan tampilan seperti gambar yang ada dibawah ini.

![Foto Lat1](https://github.com/HamdanAlWahidan/TUGAS_PERTEMUAN7/blob/main/Lab3/Lab3.1.png) <br>

Ini contoh gambaran program ini menggunakan Flowchart

![Foto Lat1](https://github.com/HamdanAlWahidan/TUGAS_PERTEMUAN7/blob/main/Lab3/Lab3.1.png) <br>

## TUGAS LAB 5

![Latihan 2.1](https://github.com/HamdanAlWahidan/TUGAS_PERTEMUAN7/blob/main/Pertemuan7/latihan2.png) <br>

![Latihan 2.2](https://github.com/HamdanAlWahidan/TUGAS_PERTEMUAN7/blob/main/Pertemuan7/latihan2.png) <br>

![Latihan 2.3](https://github.com/HamdanAlWahidan/TUGAS_PERTEMUAN7/blob/main/Pertemuan7/latihan2.png) <br>

Di tugas ke dua, saya diminta untuk membuat program sederhana yang akan menampilkan daftar nilai mahasiswa. Maka saya memasukan script di bawah ini:
```
print("========Program Input Nilai =========")
data={}
while True:
    print("")
    c =input("(L)lihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar : ")
    if c.lower() == 'k':
        print("Keluar")
        break

    elif c.lower() == 'l':
        if data.items():
            print("Daftar Nilai Mahasiswa")
            print("================================================================================================")
            print(" |NO   |     NAMA      |    NIM    |     TUGAS    |     UTS     |       UAS    |    AKHIR     | ")
            print("================================================================================================")
            i=0
            for x in data.items():
                i+=1
                print(" | {6:2}  |  {0:12s} | {1:9s} | {2:11}  | {3:11} | {4:11}  |  {5:11} |".format(x[0], x[1][0], x[1][1], x[1][2], x[1][3], x[1][4], i))
                print("============================================================================================")
        else:
            print("Daftar Nilai Mahasiswa")
            print("================================================================================================")
            print(" |NO   |     NAMA      |    NIM    |     TUGAS    |     UTS     |       UAS    |    AKHIR     | ")
            print("================================================================================================")
            print("|                                      TIDAK ADA DATA                                         |")
            print("===============================================================================================")

    elif c.lower() == 't':
        print("=======Tambah Data===")
        nama    =input("Nama               :  ")
        nim     =input("Nim                 :  ")
        tugas   =int(input("masukan nilai tugas :  "))
        uts     =int(input("masukan nilai uts   :  "))
        uas     =int(input("masukan nilai uas   :  "))
        akhir   = (0.30 * tugas) + (0.35 * uts) + (0.35 * uas)
        data[nama] = nim ,tugas, uts, uas, akhir

    elif c.lower() == 'u':
        print('=======Ubah Data Mahasiswa=======')
        nama = input('Nama                :  ')
        if nama in data.keys():
            nim     =input('Nim                 :  ')
            tugas   =int(input("masukan nilai tugas :  "))
            uts     =int(input("masukan nilai uts   :  "))
            uas     =int(input("masukan nilai uas   :  "))
            akhir   =(0.30 * tugas) + (0.35 * uts) + (0.35 * uas)
            data[nama] = nim, tugas, uts, uas, akhir
        else:
            print("Data Nilai Tidak Ada".format(nama))


    elif c.lower() == 'h':
        print("====hapus data mahasiswa====")
        nama=input("nama :  ")
        if nama in data.keys():
            del data[nama]
        else:
            print("Data Nilai Tidak Ada".format(nama))

    elif c.lower() == 'c':
        print("===cari data mahasiswa===")
        nama=input("Masukan Nama :  ")
        if nama in data.keys():
            print("Daftar Nilai Mahasiswa")
            print("================================================================================================")
            print(" |NO   |     NAMA      |    NIM    |     TUGAS    |     UTS     |       UAS    |    AKHIR     | ")
            print("================================================================================================")
            print("|    {0} |   {1} | ".format(nama, data[nama]))
            print("===============================================================================================")
        else:
            print("Datanya {0} Tidak Ada ".format(nama))
    else:
        print("Daftar Nilai Mahasiswa")
        print("================================================================================================")
        print(" |NO   |     NAMA      |    NIM    |     TUGAS    |     UTS     |       UAS    |    AKHIR     | ")
        print("================================================================================================")
        print("|                                      TIDAK ADA DATA                                         |")
        print("===============================================================================================")
else:
    print("Tidak Ada Apa Apa")

```

Jika sudah memasukan semua syntax diatas dan telah di run, maka kamu akan mendapatkan tampilan seperti gambar yang ada dibawah ini.

![Foto Lat2](https://github.com/HamdanAlWahidan/TUGAS_PERTEMUAN7/blob/main/Lab3/Lab3.png) <br>

Untuk fitur selebih nya bisa kalian coba sendiri menggunakan script di atas.
Ini contoh gambaran program ini menggunakan Flowchart

![Foto Lat3](https://github.com/HamdanAlWahidan/TUGAS_PERTEMUAN7/blob/main/Lab3/Lab3.1.png) <br>
___________________________________________________________________________________________________
