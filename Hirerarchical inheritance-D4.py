# Parent Class
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient Balance")

    def display_balance(self):
        print("Balance:", self.balance)


# Child Class 1
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance, interest_rate):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print("Interest Added:", interest)


# Child Class 2
class CurrentAccount(BankAccount):
    def __init__(self, account_holder, balance, overdraft_limit):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw_with_overdraft(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print("Withdrawn using overdraft:", amount)
        else:
            print("Overdraft limit exceeded")


# Object Creation
save_acc = SavingsAccount("John", 10000, 5)
curr_acc = CurrentAccount("Jane", 5000, 2000)

# Testing Savings Account
save_acc.deposit(1000)
save_acc.add_interest()
save_acc.display_balance()

# Testing Current Account
curr_acc.withdraw_with_overdraft(6000)
curr_acc.display_balance()
