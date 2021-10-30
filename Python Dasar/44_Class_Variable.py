#class
class Mahasiswa():
    __nilai = 0                                #variable class
    jurusan = "Teknik informatika"             #variable class

    def __init__(self,input_nama,input_nim):
        self.nama = input_nama                 #variable main program
        self.nim = input_nim                   #variable main program

#main
x1 = Mahasiswa("Rapli levine",155150200111274)
x2 = Mahasiswa("Adam Maulana",152526727161441)

print(Mahasiswa.jurusan)
print(x1.jurusan)
print(x2.jurusan,"\n")

#mengganti variabel sendiri (override)
x1.jurusan = "ekonomi"

print(Mahasiswa.jurusan)
print(x1.jurusan)
print(x2.jurusan,"\n")

#ubah variable (semuanya)
Mahasiswa.jurusan = "fisika"

print(Mahasiswa.jurusan)
print(x1.jurusan)
print(x2.jurusan,"\n")

