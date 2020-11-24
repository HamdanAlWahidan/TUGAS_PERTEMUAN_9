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
