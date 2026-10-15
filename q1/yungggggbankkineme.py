class Account:
    name = ""
    number = ""
    __balance = 0
    def __init__ (self, name, number):
        self.name = name
        self.number = number
    def getBalance(self):
        return self. balance
    def deposit (self, amount):
        self.__balance += amount
    def withdraw(self, amount):
        if amount > self. balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
    def __str__(self):
        return self.name "["+ self.number +"] P" str(self.__balance)
    def del(self):
        print("Account", self.number, "closed")

class SavingsAccount (Account):
    __interest=0.05
    def addinterest(self):
        #sumtin
        interestToAdd = super().getBalance() * self.__interest
        super().deposit (interestToAdd)

class Bank:
    name = ""
    __accounts = []
    def __init__ (self, name):
        self.name = name
        print("Welcome to", self.name)
    def openAccount(self):
        print("Ready to open an account")
        acc_nam = input ("Account name: ")
        acc_num = input ("Account number: ")
        acc_typ input("Account type (savinge or checking): ")
        if acc_typ == "savings":
            account = SavingsAccount(acc_nam, acc_num)
        else:
            account = Account(acc_nam, acc_num)
        print ("Account created”)
        print (account)
        self.__accounts.append (account)
    def showAccounts (self):
        print ("Showing accounts")
        for a in self.__accounts:
        print (a)

    def addIntrest(self):
        print ("Adding interest to all saving accounts")
        for a in self.__accounts:
            if isistance(a, SavingsAccount)
            a.addInterest()
            print("Interest added to account", a.number)
            print(a)    
    def closeAccount(self):
        print("Ready to close an account")
        acc_num = input("Enter account number: ")
        for a in self.__accounts:
            if a.number == acc_num:
                self.__accounts.remove(a)
                del a
                print ("Account closed")
                
bank = Bank("Land Bank of the Philippines")
bank.openAccount()
bank.openAccount()
bank.showAccounts()
bank.deposit()
bank.deposit()
bank.addInterest()
bank.closeAccount()
del bank
