class BankAccount:

    # CLS METHOD
    accounts = []
    # CLS METHOD

    def __init__(self, balance, interest_rate):
        self.balance = balance
        self.interest_rate = interest_rate
        # CLS METHOD
        BankAccount.accounts.append(self)
        # CLS METHOD

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f'Your balance is up to ${self.balance}!')
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance-amount
            print(f'Your balance is down to ${self.balance}.')
        else:
            self.balance = self.balance - 5
            print('Insufficient Funds')
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}\nInterest Rate: {self.interest_rate}%")
        return self

    def yield_of_interest(self):
        if self.balance > 0:
            self.balance = self.balance * (self.interest_rate)
            print(f"After APY, your balance is {self.balance}.")
        else:
            print("Your account is negative")
        return self

# CLS METHOD
    @classmethod
    def display_all(cls):
        for account in cls.accounts:
            account.display_account_info()
# CLS METHOD

checking = BankAccount(5200, 1.045)
savings = BankAccount(105000, 1.02)

print(checking.balance, checking.interest_rate)
print(savings.balance, savings.interest_rate)


checking.deposit(675).deposit(1450).deposit(375).withdraw(1690).yield_of_interest().display_account_info()
savings.deposit(5770).deposit(1525).withdraw(70000).withdraw(10000).withdraw(2500).withdraw(2250).yield_of_interest().display_account_info()

# CLS METHOD -- this will print all values. 
BankAccount.display_all()
# CLS METHOD -- this happens because we create a global empty list, 
# then inside the constructor we append that empty list to our 
# CLASSNAME <=> Instance (BankAccount... <=list=> .append(self) )
# Then we create the @classmethod, and for every account in BankAccount,
# we display that accounts info..Lastly, we call the CLS function
