#Create a BankAccount class with attributes account_number, owner_name and balance. Add methods to deposit, withdraw, and check balance.

class BankAccount:
    def __init__(self, account_number, owner_name, balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        final_balance = self.balance + amount
        self.balance = final_balance
        print(f"{self.owner_name} Balance after deposit: {final_balance}")

    def withdraw(self, amount):
        final_balance = self.balance - amount
        self.balance = final_balance
        print(f"{self.owner_name} Balance after withdraw: {final_balance}")

    def check_balance(self):
        print(f"{self.owner_name} Balance : {self.balance}")

c1 = BankAccount(4677_8896, "Shree Kudande", 1000000000)
c2 = BankAccount(7564_4489, "Saurabh Nagawade", 100000)

print(c1.account_number, c1.owner_name, c1.balance )
print(c2.account_number, c2.owner_name, c2.balance )
        
c2.deposit(100000)
c1.withdraw(100000000)

c1.check_balance()
c2.check_balance()
