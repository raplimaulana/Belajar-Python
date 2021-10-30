counter = 0

while True:
    print(8*"#","BILANGAN PRIMA",8*("#"))
    print("1. Cek bilangan prima\n2. Keluar")
    pilihan = int(input("Masukan pilihan anda : "))
    counter += 1

    if pilihan == 1:
        a = int(input("Masukan nilai a : "))

        for i in range(2,a+1):
            if a%i == 0 and i < a:
                print("Bukan bilangan prima, karena bisa dibagi dengan",i)
                break
            elif a%i == 0 and i <= a:
                print("Bilangan prima")
    elif pilihan == 2:
        break
    else:
        print("Pilihan salah !!!")
print(8*"#","PROGRAM SELESAI",8*"#")