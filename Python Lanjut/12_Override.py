#override = menimpa method super class
class Hero:
    def __init__(self,name,health):
        self.name = name
        self.health = health

    def ShowInfo(self):
        print("{} \nHP\t: {} \n".format(self.name,self.health))

class HeroTanker(Hero):
    def __init__(self,name):
        super().__init__(name,200)
        
    #override
    def ShowInfo(self):
        print("Print Menggunakan Override")
        print("{} \nHP\t: {} \nType : Hero Tanker\n".format(self.name,self.health))

class HeroCaryy(Hero):
    def __init__(self,name):
        super().__init__(name,150)


hero1 = HeroTanker("Ursa")
hero2 = HeroCaryy("Razor")

hero1.ShowInfo()
hero2.ShowInfo()