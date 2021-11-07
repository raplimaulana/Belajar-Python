class Hero:
    def __init__(self,name,health,attack_power):
        self.__name = name
        self.__health = health
        self.__attack_power = attack_power

    #getter
    def getName(self):
        return self.__name
    def getHealth(self):
        return self.__health

    #setter
    def diserang(self,attack_lawan):
        self.__health -= attack_lawan

#awal dari game
hero1 = Hero("Ursa",100,20)
print(hero1.__dict__)

#game berjalan
#print(hero1.__name)            *akan error, agar variabel private dapat diambil bisa menggunakan get
print(hero1.getName())

hero1.diserang(30)
print(hero1.getHealth())