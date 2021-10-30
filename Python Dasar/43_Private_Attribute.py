#class
class Mahasiswa():
    __nilai = 0                                 #private
    jurusan = "Teknik informatika"              #public

    def __init__(self,input_nama,input_nim):
        self.nama = input_nama                  #public
        self.nim = input_nim                    #public

    def uts(self,input_nilai):
        self.__nilai += input_nilai

    def uas(self,input_nilai):
        self.__nilai += input_nilai

    def cek_status(self):
        if self.__nilai <= 100:
            print(self.nama,self.jurusan,"Tidak Lulus")
        else:
            print(self.nama,"Lulus")

#main program
x1 = Mahasiswa("Rapli levine",155150200111274)

#memanggil method pada class menggunakan argument
x1.uts(30)
x1.uas(50)

x1.cek_status()
