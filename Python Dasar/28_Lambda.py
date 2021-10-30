#menggunakan function biasa
def jumlah(a,b):
    hasil = a + b
    return hasil

a = jumlah(2,3)

print(a)

#menggunakan anonymus function lambda
kali = lambda a,b: a*b

a = kali(2,3)

print(a)
