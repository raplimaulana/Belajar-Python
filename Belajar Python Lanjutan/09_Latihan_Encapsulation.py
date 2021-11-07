class Hero:
    __jumlah = 0
    def __init__(self,name,health,attPower,armor):
        self.__name = name
        self.__healthBase = health
        self.__attPowerBase = attPower
        self.__armorBase = armor
        self.__level = 1
        self.__experience = 0
        self.__exp = 0

        self.__healthMax = self.__healthBase * self.__level
        self.__attPower = self.__attPowerBase * self.__level
        self.__armor = self.__armorBase * self.__level

        self.__health = self.__healthMax

        Hero.__jumlah += 1

    @property
    def info(self):
        return "{} LEVEL {} \nhealth\t = {}/{} \nattack\t : {} \narmor\t : {}".format(self.__name,self.__level,self.__health,self.__healthMax,self.__attPower,self.__armor)

    @property
    def gainExp(self):
        pass

    @gainExp.setter
    def gainExp(self,addExp):
        self.__exp += addExp
        if (self.__exp >= 100):
            print(self.__name,"LEVEL UP!")
            self.__level += 1
            self.__exp -= 100

            self.__healthMax = self.__healthBase * self.__level
            self.__attPower = self.__attPowerBase * self.__level
            self.__armor = self.__armorBase * self.__level

    def attack(self,lawan):
        self.gainExp = 50


x1 = Hero("Ursa",1000,200,100)
x2 = Hero("Razor",1000,200,100)

print(x1.info,"\n")
x1.attack(x2)
x1.attack(x2)
x1.attack(x2)

print(x1.info,"\n")


