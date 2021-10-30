class Mobil():
    counter = 0
    def __init__(self):
        self.counter =+ 1

    def noPlat(self,a):
        self.noPlatMobil = a
        return self.noPlatMobil

    def Warna(self,a):
        self.WarnaMobil = a
        return self.WarnaMobil

    def kaka(self,a):
        self.ManufakturMobil = a
        return self.ManufakturMobil

    def Kecepatan(self,a):
        self.KecepatanMobil = a
        return self.KecepatanMobil

    def DisplayMessage(self):
        print("Mobil anda bermerk",self.kaka())
        print("Mempunyai nomor plat",noPlat())
        print("Serta memiliki warna",Warna())
        print("dan mampu menempuh kecepatan",Kecepatan())

merk = "Toyota" #input("Masukan merk mobil anda : ")
plat = "B 1627 A" #input("Masukan plat nomor mobil anda : ")
warna = "Merah" #input("Masukan warna mobil anda : ")
kecepatan = "100 KM/Jam" #input("masukan kecepatan mobil anda : ")



m1 = Mobil()

m1.noPlat(plat)
m1.Warna(warna)
print(m1.kaka(merk))
m1.Kecepatan(kecepatan)

#print(m1.kaka())
m1.DisplayMessage()