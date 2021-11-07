class Hero:
    def __init__(self,name,health):
        self.name = name
        self.health = health

    def showInfo(self):
        print("{}\t: {} hp".format(self.name,self.health))

class HeroTanker(Hero):
    def __init__(self,name):
        #Hero.__init__(self,name,200)
        super().__init__(name,200)
        super().showInfo()

class HeroCarry(Hero):
    def __init__(self,name):
        super().__init__(name,100)
        super().showInfo()

hero1 = HeroTanker("Ursa")
hero2 = HeroCarry("Razor")

