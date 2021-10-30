count = 0

def faktorial(a):
    if a == 1:
        return 1
    else:
        return a * faktorial(a-1)

def permutasi():
    n = int(input("Nilai n : "))
    r = int(input("nilai r : "))
    hasil = faktorial(n)/faktorial((n-r))
    print(hasil)

def kombinasi():
    n = int(input("Nilai n : "))
    r = int(input("nilai r : "))
    hasil = faktorial(n)/faktorial(r)*faktorial(n-r)

while True:
    print(5*"#","Program Penghitung Permutasi dan Kombinasi",5*"#")
    print("1. Menghitung Permutasi\n2. Menghitung Kombinasi\n3. Keluar")
    pilihan = int(input("Masukan Pilihan Anda : "))
    count += 1

    if pilihan == 1:
        permutasi()
    elif pilihan == 2:
        kombinasi()
    elif pilihan == 3:
        break
    else:
        print("Inputan Salah !!!")
