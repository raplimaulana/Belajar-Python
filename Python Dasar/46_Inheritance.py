class Ojek():
    def __init__(self,nama,transmisi,daerah):
        self.nama = nama
        self.transmisi = transmisi
        self.daerah = daerah

    def CekId(self):
        print("Nama : ",self.nama,"\nMotor : ",self.transmisi,"\nDaerah : ",self.daerah,"\n")

class Gojek(Ojek):              #isi class gojek = isi class ojek (inheritance)
    pass

class Grab(Ojek):
    def CekId(self):            #menimpa / menambah method dari class induk (override)
        print("Cek ID Grab")

x1 = Ojek("Rapli","Honda","Subang")
x2 = Gojek("Maulana","Yamaha","Malang")

x1.CekId()
x2.CekId()