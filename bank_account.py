
# Bank Account Program using OOP Concepts

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance   # Encapsulation

    def deposit(self, amount):
        self.__balance += amount
        print(f"{self.name} deposited ₹{amount}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"{self.name} withdraw ₹{amount}")
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance

    def show_balance(self):
        print(f"{self.name}'s balance: ₹{self.__balance}")


# Inheritance
class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        if self.get_balance() - amount >= 1000:
            super().withdraw(amount)
        else:
            print("Withdrawal denied! Maintain minimum balance of ₹1000")


# Creating objects
acc1 = BankAccount("Pavan", 5000)
acc2 = SavingsAccount("Kalyan", 8000)

# Simulating bank operations
acc1.deposit(2000)
acc1.withdraw(1000)
acc1.show_balance()

print("------------")

acc2.withdraw(7500)
acc2.show_balance()
