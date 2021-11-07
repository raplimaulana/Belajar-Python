class Team:
    def selfTeam(self,team):
        self.team = team

    def showTeam(self):
        print("Team ",self.team)

class TipeHero:
    def selfType(self,type):
        self.type = type

    def showType(self):
        print("Type :",self.type)

class Hero(Team,TipeHero):
    def __init__(self,name,health):
        self.name = name
        self.health = health


hero1 = Hero("Ursa",100)

hero1.selfTeam("Merah")
hero1.selfType("Tanker")

print(hero1.name)
hero1.showType()
hero1.showTeam()