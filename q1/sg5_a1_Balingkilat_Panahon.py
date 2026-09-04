#HERO's GAME
class hero:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def take_damage (self, hp):
        print(f"{self.name} takes 10 dmg!")
        self.hp -= hp


    def priNt(self):
        print (f"{self.name} has {self.hp}!")

hero1 = hero("Arthur", 100)
hero2 = hero("Morgona", 100)

hero1.take_damage(10)

hero1.priNt()
hero2.priNt()

