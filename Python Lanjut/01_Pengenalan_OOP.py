class Hero():           #template
    pass


hero1 = Hero()          #object
hero2 = Hero()          #object
hero3 = Hero()          #object


hero1.name = "Ursa"
hero1.health = 200

hero2.name = "Razor"
hero2.health = 100

hero3.name = "Dragon"
hero3.health = 1000

print(hero1)
print(hero1.__dict__)

