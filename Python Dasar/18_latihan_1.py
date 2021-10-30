print("MENU")
print("1. Menghitung luas dan keliling persegi panjang\n2. Menghitung luas dan keliling lingkaran\n3. Menghitung luas dan keliling segitiga")

pilihan = int(input("Masukan pilihan anda : "))

if pilihan == 1:
    a = float(input("Masukan nilai a : "))
    b = float(input("masukan nilai b :"))

    luas_persegi = a * b
    keliling_persegi = 2*(a + b)

    print("Keliling Persegi : ",keliling_persegi)
    print("Luas Persegi\t: ",luas_persegi)

elif pilihan == 2:
    r = float(input("Masukan Nilai r : "))

    luas_lingkaran = 22 / 7 * r ** 2
    keliling_lingkaran = 2 * 22 / 7 * r

    print("Keliling Lingkaran : ",keliling_lingkaran)
    print("Luas Lingkaran\t: ",luas_lingkaran)

elif pilihan == 3:
    a = float(input("Masukan Nilai a : "))
    t = float(input("Masukan Nilai t : "))

    luas_segitiga = 1 / 2 * a * t
    keliling_segitiga = 3 * a

    print("Keliling Segitiga : ",luas_segitiga)
    print("Luas Segitiga : ",keliling_segitiga)

else:
    print("Data tidak ditemukan, program dihentikan.....")
print("SELESAI")


