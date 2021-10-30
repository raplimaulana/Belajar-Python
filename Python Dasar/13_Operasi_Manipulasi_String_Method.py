#merubah ke huruf kapital (upper case)
data1 = "RaPlI MaULaNa"
kapital = data1.upper()

print(data1 + " jadi " + kapital)
print(data1 + " jadi " + data1.upper())

#merubah ke huruf kecil
kecil = data1.lower()

print(data1 + " jadi " + kecil)
print(data1 + " jadi " + data1.upper()+"\n")

##pengecekan isX method
#pengecekan lower dan upper case
data2 = "seblak merah"
apakah_lower = data2.islower()
apakah_upper = data2.isupper()

print(data2 + " is lower " + str(apakah_lower))
print(data2 + " is upper " + str(apakah_upper)+"\n")

# isalpha()     untuk mengecek semuanya huruf
# isalnum()     untuk mengecek huruf dan angka
# isdecimal()   untuk mengecek angka saja
# isspace()     untuk mengecek isi print kosong (cuma spasi,tab atau newline \n)
# istitle()     untuk mengecek untuk mengecek semua kata dimulai dengan huruf besar

#ngecek komponen
data3 = "rumahku idamanku".startswith("rumahku")
print("start : " + str(data3))

data4 = "house of targaryen"
end = data4.endswith("targaryen")
print("start : " + str(end)+"\n")

#penggabungan komponen join() dan split()
pisah1 = ["rapli","maulana","aji"]
gabungan1 = ",".join(pisah1)

print(gabungan1)

gabungan2 = "rapliokmaulanaokajiok"
pisah2 = gabungan2.split("ok")

print(pisah2)
print(gabungan2.split("ok"))

#alokasi karakter rjust() = rata kanan, ljust() = rata kiri, center() = rata tengah
data5 = "kanan"
rata_kanan = data5.rjust(10)

print("'" + rata_kanan + "'")

data6 = "kiri".ljust(10)
print("'" + data6 + "'")

data7 = "tengah".center(20,"-")
print("'" + data7 + "'")

