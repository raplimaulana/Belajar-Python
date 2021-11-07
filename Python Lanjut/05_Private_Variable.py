class Hero:

    #class variable
    jumlah = 0

    def __init__(self,name,health):
        self.name = name
        self.health = health
        self.jumlah += 1

        #instance variable, private
        self.__jurus = "Special Attack1"

        #instance variable, protected
        self._bonus = "Tidak Ada Bonus"


hero1 = Hero("Ursa",100)
hero2 = Hero("Razor",80)

#akses private variable
print(hero1.__dict__)
hero1.jurus = "jurus baru"
print(hero1.__dict__)
hero1.__jurus = "jurus terakhir"
print(hero1.__dict__)

#akses protected variable
print(hero2.__dict__)
hero2.bonus = "bonus uang"
print(hero2.__dict__)
hero2._bonus = "bonus health"
print(hero2.__dict__)
