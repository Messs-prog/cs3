class Bill:
  amount = 0
  def __init__(self,amount):
    self.amount = amount
  def pay(self, Payment):
    self.amount -= Payment.amount
    print("Paying with ", Payment.mode)
    print("Balance: ", self.amount

class Payment:
  amount = o
  mode = "Cash"
  def __init_(self,amount):
    self.amount = amount

class Ewallet(Payment):
  sef __ini__(self, name, amount)
  self.mode = name
  self.amount = amount

bigBeautifulBill = Bill(1000)
bayad = Payment(900)
bigBeautifulBill.pay(bayad)

gcash = Ewallet("Gcash", 67)
bigBeautifulBill.pay(gcash)

ewallet = Ewallet("PisayCash", 33)
bigBeautifulBill.pay(ewallet)
