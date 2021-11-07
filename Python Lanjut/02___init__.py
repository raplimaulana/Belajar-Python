class Hero:
    #class variable, variabel yang dimiliki oleh clas
    jumlah = 0

    def __init__(self,nama,darah):
        # instance variable, variabel ini hanya dimiliki oleh object yang di panggil.
        self.name = nama
        self.health = darah
        Hero.jumlah += 1


#object, berisi attribute
hero1 = Hero("Ursa",200)
hero2 = Hero("Razor",100)
hero3 = Hero("Dragon",1000)

#memanggil isi class
print(hero1.name)
print(hero2.health)
print(hero3.__dict__)

print("\njumlah hero adalah : ",Hero.jumlah)