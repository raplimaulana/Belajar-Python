counter = 0
while True:
    print(8 * "#", "PROGRAM PENGHITUNG GANJIL GENAP", 8 * "#")
    print("1. Bilangan Ganjil\n2. Bilangan Genap\n3. Selesai")
    pilihan = int(input("Masukan Pilihan : "))

    counter = + 1

    if pilihan == 1:
        a = int(input("Masukan nilai a : "))
        if a%2 == 1:
            print("Bilangan ini adalah ganjil")
        else:
            print("Bilangan salah")
    elif pilihan == 2:
        a = int(input("Masukan nilai a: "))
        if a%2 == 0:
            print("Bilangan ini adalah genap")
    elif pilihan == 3:
        break
    else:
        print("silahkan ulangi kembali")
print(8*"#","PROGRAM SELESAI",8*"#")