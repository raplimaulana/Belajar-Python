class Hero:
    def __init__(self,name,health,armor):
        self.name = name
        self.__health = health
        self.__armor = armor

    @property
    def armor(self):
        pass

    @armor.getter
    def armor(self):
        return self.__armor

    @armor.setter
    def armor(self,input):
        self.__armor = input

    @armor.deleter
    def armor(self):
        print("armor di delete")
        self.__armor = None

hero1 = Hero("Ursa",100,50)

print(hero1.armor)
print(hero1.__dict__,"\n")

#hero1.armor(200)       --tidak digunakan, diganti menjadi seperti input/ubah variabel biasa
hero1.armor = 200
print(hero1.armor)
print(hero1.__dict__,"\n")

del hero1.armor
print(hero1.armor)
