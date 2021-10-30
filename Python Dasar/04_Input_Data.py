#data dimasukan pasti string
a = input("masukan data :")

print("data adalah : ",a)

#int
#jika kita ingin mengambil int, harus di casting terlebih dahulu
b = int(input("masukan data : "))

print("data adalah : ", b)

#boolean
#ubah ke integer, kemudian ke boolean
c = bool(int(input("masukan data : ")))
print("data adalah = ",c)