class BankAccount:
    def __init__(self):
        self.balance = 0
    
    def incoming(self,money):
        self.balance =+ money

    def outcoming(self,money):
        if money > self.balance:
            raise ValueError("There isn't enough to retire")
        else:
            self.balance -= money

class SavingsAccount(BankAccount):
    def __init__(self, balance,min_balance):
        self.balance = balance
        self.min_balance = min_balance
    
    def outcoming(self,money):
        if self.balance < self.min_balance:
            print("You can't retire money, the minimum balance is bigger than balance")
        else:
            self.balance -= money
            print("It was successful")

saving = SavingsAccount(1000,2000)
saving.outcoming(1000)
