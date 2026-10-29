#i hat u <3 - mesy
#i luv u 2 <3 - aubr
#im neauteral ab u <3 - lyre
#ur epikshon haz bin noted <3 - ben10

class Warrior:
    def special_move(self):
        print(f"Warrior swings a mighty sword!")

class Mage:
    def special_move(self):
        print(f"Mage casts a powerful spell!")
        
class Archer:
    def special_move(self):
        print(f"Archer shoots a precise arrow!")
        
def perform_move(character):
    character.special_move()
        
Zion = Warrior()
Retrixx = Mage()
Bob = Archer()

heroes = [Zion, Retrixx, Bob]
for c in heroes:
    perform_move(c)


    
