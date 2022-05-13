
class bankAccount:
    
    def __init__(self, name, email, account, interest_rate=0.1):
        self.name = name
        self.emai = email
        self.account = account
        self.account_balance = 0
        self.interest_ratet = interest_rate=0.1
        

    def make_deposit(self, amount):
        self.account_balance += amount
        return self


    def make_withdraw(self, amount):
        self.account_balance -= amount
        return self


    def display_user_bal(self):
        print(f"{self.name}, balance: {self.account_balance}")
        return self


    def yield_interest(self):
        self.balanace = self.account_balance * self.interest_rate +self.account_balance
        return self

bankaccount = bankAccount

user1 = bankAccount("Tim", "Tim@dojo.com", interest_rate=0.1)
user2 = bankAccount("Jim", "Jim@dojo.com", interest_rate= 0.1)


