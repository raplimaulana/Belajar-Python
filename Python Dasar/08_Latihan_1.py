hasil1 = float(input("masukan angka yang bernilai kurang dari 3 atau lebih dari 10 : "))

kurangdari = (hasil1 < 3)
print("kurang dari 3 = ", kurangdari)

lebihdari = (hasil1 > 10)
print("lebih dari 10 = ", lebihdari)

cek = kurangdari or lebihdari
print("angka yang anda masukan = ",cek)