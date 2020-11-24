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
