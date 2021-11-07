class Hero:
    def __init__(self,name,health):
        self.name = name
        self.health = health

class HeroTanker(Hero):
    pass

class HeroCarry(Hero):
    pass

hero1 = Hero("Dragon",100)
hero2 = HeroTanker("Ursa",80)
hero3 = HeroCarry("Razor",60)