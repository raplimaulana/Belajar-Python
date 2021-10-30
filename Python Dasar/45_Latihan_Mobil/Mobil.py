class Mobil():
    counter = 0
    def __init__(self,noPlat,warna,manufaktur,kecepatan):
        self.noPlatMobil = noPlat
        self.WarnaMobil = warna
        self.ManufakturMobil = manufaktur
        self.KecepatanMobil = kecepatan
        self.counter =+ 1

    def noPlat(self):
        return self.noPlatMobil

    def Warna(self):
        return self.WarnaMobil

    def Manufaktur(self):
        return self.ManufakturMobil

    def Kecepatan(self):
        return self.KecepatanMobil

    def DisplayMessage(self):
        print("Mobil anda bermerk",self.Manufaktur())
        print("Mempunyai nomor plat",self.noPlat())
        print("Serta memiliki warna",self.Warna())
        print("dan mampu menempuh kecepatan",self.Kecepatan())

