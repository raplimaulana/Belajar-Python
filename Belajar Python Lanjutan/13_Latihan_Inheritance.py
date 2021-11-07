class Hero:
    def __init__(self,name):
        self.__health_pool = [0,100,200,300,400,500]
        self.__attPower_pool = [0,10,20,30,40,50]
        self.__armor_pool = [0,1,2,3,4,5]
        self.__name = name
        self.__exp = 0
        self.__level = 0

    def showInfo(self):
        print("{} \n\tLEVEL\t : {} \n\thealth\t : {} \n\tattPower : {} \n\thealth\t : {}".format(self.__name,self.__level,self.__health,self.__attPower,self.__armor))

    @property
    def health_pool(self):
        pass

    @property
    def attPower_pool(self):
        pass

    @property
    def armor_pool(self):
        pass

    @property
    def gainExp(self):
        pass

    @property
    def levelUp(self):
        pass

    @health_pool.setter
    def health_pool(self,input):
        self.health_pool

    @attPower_pool.setter
    def attPower_pool(self, input):
        self.__attPower_pool = input

    @armor_pool.setter
    def armor_pool(self,input):
        self.__armor_pool = input

    @gainExp.setter
    def gainExp(self,input):
        self.__exp += input
        if self.__exp >= 100:
            self.levelUp = self.__exp//100
            self.__exp %= 100

    @levelUp.setter
    def levelUp(self,input):
        self.__level += input
        self.__health = self.__health_pool[self.__level]
        self.__attPower = self.__attPower_pool[self.__level]
        self.__armor = self.__armor_pool[self.__level]

class HeroTanker(Hero):
    def __init__(self,name):
        super().__init__(name)
        self.__health_pool = [0, 50, 100, 150, 200, 250]
        self.__attPower_pool = [0, 20, 40, 60, 80, 100]
        self.__armor_pool = [0, 2, 4, 6, 8, 10]
        self.levelUp = 1

class HeroCarry(Hero):
    def __init__(self,name):
        super().__init__(name)
        self.__health_pool = [0,50,100,150,200,250]
        self.__attPower_pool = [0,20,40,60,80,100]
        self.__armor_pool = [0,0.5,1,1.5,2,2.5]
        self.levelUp = 1

hero1 = HeroTanker("Ursa")
hero2 = HeroCarry("Razor")

hero1.showInfo()
hero2.showInfo()

hero1.gainExp = 350
hero2.gainExp = 100

hero1.showInfo()
hero2.showInfo()