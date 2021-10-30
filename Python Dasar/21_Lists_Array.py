data1 = [1,4,9,16,25,36,49]
data2 = [10,20,30,40,50,60]

print(data1[3])
print("\n")

#list 1 dimensi
#mengakses list
subdata1 = data1[1]
subdata2 = data1[-1]
subdata3 = data1[0:4]
subdata4 = data1[4:] # ambil data semua ke kanan setelah list ke 4
subdata5 = data1[:4] # ambil data semua ke kiri sebelum list ke 4


print(subdata1)
print(subdata2)
print(subdata3)
print(subdata4)
print(subdata5,"\n")

#menambah list
data3 = data1 + data2

print(data3,"\n")

#mengubah isi list
print(data1)

data1[4] = 99

print(data1,"\n")

#copy data dari list
a = data1[:]
a[4] = 76

print(a,"\n")

#merubah data dengan menggunakan metode slice
data1[3:5] = [11,12]

print(data1,"\n")

#list dalam list
b = [data1,data2]

print(b,"\n")

#list 2 dimensi
x = b[0][3]
y = b[1][3]
print(x,y)
