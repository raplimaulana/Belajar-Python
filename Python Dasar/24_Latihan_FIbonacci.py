counter = 0
a = 0
while True:
    print(8*"#","BILANGAN FIBONACCI",8*"#")
    print("1. Non rekursif\n2. Def\n3. Rekursif\n4. Keluar\n")

    pilihan = int(input("Masukan pilihan anda : "))
    counter += 1

    if pilihan == 1:
        b = int(input("Masukan nilai awal : "))
        panjang = int(input("masukan batas bilangan : "))

        for i in range(panjang):
            hasil = a + b
            print(hasil,end = " ")
            a = b
            b = hasil
        else:
            print(" ")

    elif pilihan == 4:
        break
    else:
        print("pilihan salah!!!")