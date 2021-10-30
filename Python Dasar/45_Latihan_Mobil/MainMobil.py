from Mobil import *

merk = input("Masukan merk mobil anda : ")
plat = input("Masukan plat nomor mobil anda : ")
warna = input("Masukan warna mobil anda : ")
kecepatan = input("masukan kecepatan mobil anda : ")
print()


m1 = Mobil(plat,warna,merk,kecepatan)

m1.DisplayMessage()