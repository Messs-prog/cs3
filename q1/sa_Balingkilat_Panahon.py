print ("Welcome to Metrobank!")
print ("\nReady to create account\n")
  
acc1= str(input("Account name: "))
acn1= str(input("Account number: "))
act1=str(input("Account type (savings or checking): "))

class Account:
    
    def __init__(self, nae, num, typ, amt):
        self.nae = nae
        self.num = num
        self.typ = typ
        self.amt = amt
        
    def deposit (self, amt):
        self.amt += amd
        print(f"{self.nae} has P{self.amt}")

def priNt(self):
    print (f"{self.nae} has {self.amt}!")

account1 = Account( acc1, acn1, act1, 0)
print (f"Account created \n {acc1} [{acn1}] P 0.")
print (f"\nReady to create account\n")

acc2= str(input("Account name: "))
acn2= str(input("Account number: "))
act2=str(input("Account type (savings or checking): "))

class Account:
    
    def __init__(self, name, num, typ, amt):
        self.name = name
        self.num = num
        self.typ = typ
        self.amt = amt
        
    def deposit (self, amt):
        self.amt += amd
        print(f"{self.name} has P{self.amt}")
        
account2 = Account( acc2, acn2, act2, 0)
print (f"Account created \n {acc2} [{acn2}] P 0.")

print (f"\nready to deposit amount\n") 
amd = float(input("Enter amount to deposit: "))
print (f"You are about to deposit P{amd}.")
ps = str(input("Enter account number: "))
if ps := acn1:
    account1.deposit(amd)
else:
    if ps := acn2:
        account2.deposit(amd)
    else:
        print("invalid")
