#set (himpunan)
#data tidak berurutan dan data maksimal 1 (tidak ada data yg sama)

#membuat set 1
ganjil = {1,3,5,7,9}
genap = {2,4,6,8,10}

#menambah set
ganjil.add(11)

print(ganjil)
print(genap)

#membuat set 2
prima = set()

prima.add("dua")
prima.add(2)
prima.add(3)

print(prima,"\n")

#union (gabungan)
print("gabungan = ",ganjil.union(genap))

#intersection (irisan)
print("irisan = ",ganjil.intersection(prima))