from Mahasiswa import *

count = 0
while True:
    print(8*"#","SIAM UB",8*"#")
    print("1. Daftar Mahasiswa \n2. Pilih Mata Kuliah \n3. Lihat Data Mahasiswa \n4. Keluar")
    pilihan = int(input("Masukan Pilihan Anda : "))
    count += 1
    if pilihan == 1:
        nama = input("Masukan Nama Anda\t: ")
        nim = input("Masukan Nim Anda\t: ")
        jurusan = input("Masukan Jurusan Anda\t: ")
        ip = int(input("Masukan IP Semester ini\t: "))

        m1 = Mahasiswa(nama,nim,jurusan,ip)

    elif pilihan == 2:
        count2 = 0
        while True:
            kode = int(input("Masukan Kode Mata Kuliah\t: "))
            namaMK = input("Masukan Nama Mata Kuliah\t: ")
            sks = int(input("Masukan Jumlah SKS\t: "))
            count2 += 1

            m1.mataKuliah = (kode,namaMK,sks)

            pilihan2 = input("Apakah Anda ingin Memilih Mata Kuliah Lagi? ")
            if pilihan2 not in ("ya","Ya","YA","y","Y"):
                break
    elif pilihan == 3:
        print(m1.info)
    elif pilihan == 4:
        break
    else:
        print("Pilihan Anda Salah")
#(pilihan2 == "ya" or "Ya" or "y" or "Y")










