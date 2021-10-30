#input output
#mode file
"""
1. w = write mode (menulis/menghapus file lama. jika file tidak ada maka akan dibuat file baru )
2. r = read mode only (hanya bisa baca)
3. a = appending mode (menambahkan data di baris akhir)
4. r+ = write and read mode
"""

#membuat file
file = open("47_data.txt","w")

file.write("Ini adalah teks yang dibuat menggunakan python")
file.write("\nini baris kedua")
file.write("\nini baris ketiga")
file.write("\nini baris keempat")
file.close()        #harus di close, agar data tersimpan

#membaca file
file2 = open("47_data.txt","r")

#print(file2.read())
#print(file2.read(10))               #menampilkan 10 karakter pertama
print(file2.readline())              #menampilkan 1 baris saja
print(file2.readline())
file2.close()

#menambah data pada file
file3 = open("47_data.txt","a")

file3.write("\nbaris baru pake mode append")
file3.close()

