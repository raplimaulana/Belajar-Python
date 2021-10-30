barang = ["kunci","ember","jaket","ban","mobil"]
print(barang,"\n")

#menambah data ke dalam list
barang.append("sepeda")
print(barang,"\n")

#menambah data per karakter ke dalam list
barang.extend("dompet")
print(barang,"\n")

#menambah data dengan posisi spesifik
barang.insert(3,"sepeda")
print(barang,"\n")

#menghitung anggota list
print("Jumlah sepeda adalah : ",barang.count("sepeda"))

#menghapus data (yg ketemu pertama kali dari kiri)
barang.remove("sepeda")
print(barang,"\n")

#membalik data
barang.reverse()
print(barang,"\n")
print(20*"#")

#mencopy data dari list
stuff_1 = barang
stuff_1.append("panci")

print(stuff_1)
print(barang,"\n")

stuff_2 = barang.copy()
stuff_2.append("panci")

print(stuff_2)
print(barang)