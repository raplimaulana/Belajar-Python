#contoh tidak menggunakan return value
def kuadrat_1(angka):
    hasil = angka**2
    print("Hasil pangkat",angka,"adalah",hasil)

kuadrat_1(3)

a = kuadrat_1(4)

print(a,"\n")
print(20*"#")

#contoh menggunakan return value (agar isinya, dapat digunakan variabel berikutnya)
def kuadrat_2(angka):
    hasil = angka**2
    print("Hasil pangkat",angka,"adalah",hasil)
    return hasil

kuadrat_2(3)

a = kuadrat_2(4)

print(a)
print(kuadrat_2(5))
print(20*"#")

#fungsi dengan return value multiple argument
def kali(argumen1,argumen2):
    hasil = argumen1 * argumen2
    return hasil

def tambah(argumen1,argumen2):
    hasil = argumen1 + argumen2
    return hasil

print(tambah(3,4),"\n")

a = tambah(2,4)
print("hasilnya adalah : ",a)

b = kali(2,a)
print("hasilnya adalah : ",b)

b = kali(2,tambah(2,4))
print("hasilnya adalah : ",b)