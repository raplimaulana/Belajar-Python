#not        *kebalikan
print("######### NOT ##########")
a = True
c = not a
print("data a = ",a)
print("---------- not ")
print("data c = ",c)

#or          *salah satu bernilai true, hasilnya true
print("######### OR ##########")
a = True
b = True
c = a or b
print(a," or",b," =",c)

a = True
b = False
c = a or b
print(a," or",b,"=",c)

a = False
b = True
c = a or b
print(a,"or",b," =",c)

a = False
b = False
c = a or b
print(a,"or",b,"=",c)

#and          *dua duanya harus bernilai true, hasilnya true
print("######### AND ##########")
a = True
b = True
c = a and b
print(a," and",b," =",c)

a = True
b = False
c = a and b
print(a," and",b,"=",c)

a = False
b = True
c = a and b
print(a,"and",b," =",c)

a = False
b = False
c = a and b
print(a,"and",b,"=",c)

#xor          *harus satu bernilai true, hasilnya true
print("######### XOR ##########")
a = True
b = True
c = a ^ b
print(a," xor",b," =",c)

a = True
b = False
c = a ^ b
print(a," xor",b,"=",c)

a = False
b = True
c = a ^ b
print(a,"xor",b," =",c)

a = False
b = False
c = a ^ b
print(a,"xor",b,"=",c)

