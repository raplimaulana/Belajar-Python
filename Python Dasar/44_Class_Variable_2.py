#class
class Mahasiswa:
    JumlahMahasiswa = 0
    def __init__(self,input_nama,input_nim):
        self.nama = input_nama
        self.input = input_nim
        Mahasiswa.JumlahMahasiswa += 1

#main program
x1 = Mahasiswa("Rapli levine",155150200111274)
x2 = Mahasiswa("Adam maulana",155152388267565)

print(Mahasiswa.JumlahMahasiswa)

