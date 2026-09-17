class Sauce:
  def
    __init__(self, name, taste):
    self.name = name
    self.taste = taste
    print(self.name, "sauce is ready and it tastes", self.taste)
  def __str__(self):
    return "Here is the " + self.taste + ""+ self.name

class Tusoktusok:
  def
    __init__(self, name, sauce):
    self.name = name
    self.sauce = sauce
    print(self.name, "dipped in", self.sauce.name)
  def eat(self):
    print("Eating", self.name, "with", self.sauce.name)
    def __del__(self):
    print("I threw the", self.name, "in the trash can")

vinegar = Sauce("vinegar", "sour")
fishball Tusoktusok("fishball", vinegar)
fishball.eat()
del fishball

