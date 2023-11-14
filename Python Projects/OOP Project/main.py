class Account:
    def __init__(self,id,amount):
        self.id = id
        self.amount = amount
        self.balance = 1000

    def withdraw(self,amount):
        self.balance = self.balance - amount

    def deposit(self,amount):
        self.balance = self.balance + amount

anis = Account(123,500)
anis.withdraw(500)
print(anis.balance)