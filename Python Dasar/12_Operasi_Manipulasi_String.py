#menyambung string (concatenate)
nama_depan = "rapli"
nama_tengah = "maulana"
nama_belakang = "aji"

nama_lengkap = nama_depan+" "+nama_tengah+" "+nama_belakang
print(nama_lengkap,"\n")

#menghitung panjang string
panjang = len(nama_lengkap)
print(panjang)

print(len(nama_lengkap))

print("panjang dari "+ nama_lengkap +" adalah " + str(panjang))
print("panjang dari "+ nama_lengkap +" adalah " + str(len(nama_lengkap)),"\n")

#mengecek apakah ada komponen char atau string di string
x = "M"
y = "m"

status1 = x in nama_lengkap
status2 = y in nama_lengkap

print(x + " ada di " + nama_lengkap + " = " + str(status1))
print(y + " ada di " + nama_lengkap + " = " , status2,"\n")

#mengulang string
print("wk"*10)
print(10*"wk","\n")

#mengambil data dari string (indexing)
print("index ke-1 : " + nama_lengkap[1])        #berurut dari depan, mulai 0
print("index ke-(-1) : " + nama_lengkap[-1])    #berurut dari belakang, mulai -1

print("index ke-(0:3) : " + nama_lengkap[0:3])
print("index ke-(0:3) : " + nama_lengkap[0:4])
print("index ke-(0,2,4,8,10) : " + nama_lengkap[0:11:2],"\n")

#item paling kecil
print("paling kecil : ",min(nama_lengkap))

#item paling besar
print("paling besar : " + max(nama_lengkap))

#ascii code
ascii_code = ord(" ")
print("ascii codenya adalah : ",ascii_code)

data1 = 117
print("char untuk ascii code ",data1," adalah ",chr(data1))

#operator dalam bentuk method
data2 = "seblak merah hitam"
jumlah = data2.count("a")

print("jumlah a pada "+ data2 + " adalah " + str(jumlah))
print("jumlah h pada "+ data2 + " adalah", data2.count("h"))
