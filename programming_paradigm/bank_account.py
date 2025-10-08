class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")

    def display_balance(self):
        print(f"Account owner: {self.owner}, Balance: {self.balance}")


# Example usage (you can comment this out if not required)
# account = BankAccount("Blessing", 500)
# account.deposit(200)
# account.withdraw(100)
# account.display_balance()
