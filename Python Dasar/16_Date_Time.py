#date dan time
import datetime as dt

hari_ini = dt.date.today()

print("hari ini adalah",hari_ini)

tanggal = dt.date(2021,10,21)

print(tanggal,"\n")
#program
tanggal = int(input("masukan tanggal : "))
bulan = int(input("masukan bulan \t: "))
tahun = int(input("masukan tahun \t: "))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print("tanggal lahir anda adalah : ",tanggal_lahir)
print(f"harinya adalah : {tanggal_lahir:%A}")

umur_hari = hari_ini - tanggal_lahir #hasilnya akan hari
umur_tahun = umur_hari.days//365

print("umur anda adalah :",umur_tahun)


