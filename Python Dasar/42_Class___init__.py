#class
class Mahasiswa():
    nama = "nama"

    def __init__(self):
        print("__init__ akan selalu otomatis dipanggil pertama")

    def Belajar1(self):
        print("Saya Belajar")

    def Belajar2(self):
        print(self.nama,"Sedang Belajar")

    def Belajar3(self,a):
        print(self.nama,"Sedang Belajar",a)

#main program
x1 = Mahasiswa()
x2 = Mahasiswa()

x1.nama = "Rapli Levine"
x2.nama = "Adam Maulana"

#memanggil method pada class
x1.Belajar1()
x2.Belajar1()
print()

x1.Belajar2()
x2.Belajar2()
print()

#memanggil method pada class menggunakan argument
x1.Belajar3("Dengan Giat")
x2.Belajar3("Dengan Giat")
print()
