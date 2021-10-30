count = 0
data = [["No.","Jenis","Harga","Diskon","AC","Colokan"], ["1","Ekonomi","50.000","2 %","Tidak Ada","Tidak Ada"], ["2","Bisnis","100.000","5 %","Ada","Tidak Ada"], ["3","Eksekutif","150.000","7 %","Ada","Tidak Ada"], ["4","Pariwisata","200.000","10 %","Ada","Ada"]]
harga = [50000,100000,200000,300000]
diskon = []
for i in range(len(harga)):
    if i == 0:
        r_diskon = int(harga[i]*(2/100))
        diskon.append(r_diskon)
    elif i == 1:
        r_diskon = int(harga[i] * (5 / 100))
        diskon.append(r_diskon)
    elif i == 2:
        r_diskon = int(harga[i] * (7 / 100))
        diskon.append(r_diskon)
    elif i == 3:
        r_diskon = int(harga[i] * (10 / 100))
        diskon.append(r_diskon)

harga_akhir = [harga[0]-diskon[0],harga[1]-diskon[1],harga[2]-diskon[2],harga[3]-diskon[3]]
print(data[0][5])
while True:
    print("1. Melihat Daftar Kereta Api\n2. Melihat Daftar Kereta Api yang Ada AC\n3. Melihat Daftar Kereta Api yang Ada Colokan\n4. Memesan Tiket Kereta Api\n5. Melihat Pesanan Tiket\n6. Keluar")
    pilihan = int(input("Masukan Pilihan : "))
    count += 1
    print("=====================================")

    if pilihan == 1:
        for i in range(len(data)):
            for j in range(len(data)+1):
                if j == 0 or j == 1:
                    print(data[i][j],end = "\t\t")
            print("")
        print("=====================================\n")

    elif pilihan == 2:
        for i in range(len(data)):
            for j in range(len(data)+1):
                if j == 0 or j == 1 or j == 4:
                    print(data[i][j],end = "\t\t")
            print("")
        print("=====================================\n")

    elif pilihan == 3:
        for i in range(len(data)):
            for j in range(len(data)+1):
                if j == 0 or j == 1 or j == 5:
                    print(data[i][j],end = "\t\t")
            print("")
        print("=====================================\n")

    elif pilihan == 4:
        for i in range(len(data)):
            for j in range(len(data) + 1):
                if j == 0 or j == 1 or j == 2 or j == 3:
                    print(data[i][j], end="\t\t")
            print("")
        print("=====================================\n")

        kereta = int(input("Jenis Kereta : "))
        nama = input("Nama Calon Penumpang : ")
        tanggal = input("Keberangkatan (dd/mm/yyyy) : ")
        jumlah_tiket = int(input("Jumlah Tiket : "))
        if jumlah_tiket == 0:
            print("tidak boleh diisi '0'")
            jumlah_tiket = int(input("Jumlah Tiket : "))
            print("=====================================\n")

    elif pilihan == 5:
        print("=====================================")
        print("Nama : \t\t\t",nama)
        print("Tanggal Keberangkatan : \t",tanggal)
        print("Jenis Kereta : ",kereta)
        total = jumlah_tiket * harga_akhir[jumlah_tiket-1]
        print("Total Harga : ",total)
        print("=====================================\n")
    elif pilihan == 6:
        break
    else:
        print("Angka yang Anda Masukan Salah !!!")





