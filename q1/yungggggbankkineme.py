class SavingsAccount(Account):
    

class Bank:
    name = ""
    __accounts = []
    def __init__(self, name):
        self.name = name
        print("Welcome to",self.name)
    def openAccount(self):
        print("Ready to open an account")
        acc_nam = input("Account name: ")
        acc_num = input("Account number: ")
        acc_typ = input("Account type (savings or checking)")
        if acc_typ == "savings":
            account = SavingsAccount(acc_nam, acc_num)
        else:
            account = Account(acc_name, acc_num)
        print("Account created")
        print(account)
        self.__accounts.append(account)
    def showAccounts(self):
        print("Ready to deposit an amount")
        amount = float(input("Enter an amount to deposit: "))
        for a in self.__accounts:
            if a.number == acc_num:
                a.ddeposit(amount)
                print ("Deposit successful")
                print(a)
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
