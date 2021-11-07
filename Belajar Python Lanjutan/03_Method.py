class Hero:
    jumlah_hero = 0

    def __init__(self,nama,health,power,armor):
        self.nama = nama
        self.health = health
        self.power = power
        self.armor = armor
        Hero.jumlah_hero += 1

    # void return / method tanpa return dan argumen
    def Siapa(self):
        print("Namaku adalah :",self.nama)

    # method dengan argumen
    def HealthUp(self,up):
        self.health += up

    #method dengan return
    def getHealth(self):
        return self.health


hero1 = Hero("Ursa",200,30,50)
hero2 = Hero("Razor",100,70,50)

hero1.Siapa()
hero1.HealthUp(20)
#print("Health bar menjadi : ",hero1.health)
print("Health bar menjadi : ",hero1.getHealth())