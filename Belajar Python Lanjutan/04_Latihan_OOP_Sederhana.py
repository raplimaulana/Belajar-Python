class Hero:
    def __init__(self,name,health,attack,armor):
        self.name = name
        self.armor = armor
        self.health = health + armor
        self.attack = attack

  # def serang(self, Object Hero)
   #nama "Object Hero", dapat diganti dengan kata lain. berisi object yang sudah ada
    def serang(self,lawan):
        print(self.name,"menyerang",lawan.name)
        lawan.diserang(self,self.attack)

    def diserang(self,lawan,attack_penyerang):
        print(self.name,"diserang",lawan.name)
        sisa_health = self.health - attack_penyerang
        self.health = sisa_health
        print("Serangan terasa :",attack_penyerang,"\nSisa health",self.name, ":",self.health,"\n")

hero1 = Hero("ursa",100,30,20)
hero2 = Hero("razor",100,50,10)


hero1.serang(hero2)
hero1.serang(hero2)
hero1.serang(hero2)