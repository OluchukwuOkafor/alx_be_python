class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited: ${amount}"
        return None

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds."
        elif amount <= 0:
            return "Insufficient funds."
        else:
            self.balance -= amount
            return f"Withdrew: ${amount}"

    def display_balance(self):
        return f"Current Balance: ${self.balance:.2f}"
