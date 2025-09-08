class BankAcc:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Withdrawn {amount}. Remaining balance: {self.balance}")


# Usage
acc = BankAcc("John", 1000)
print(acc.name)      # John
print(acc.balance)   # 1000

acc.deposit(1000)    # Deposited 1000. New balance: 2000
print(acc.balance)   # 2000

acc.withdraw(10000)  
print(acc.balance)   
