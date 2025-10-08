#!/usr/bin/python3
import sys
from bank_account import BankAccount

def main():
    account = BankAccount("Blessing", 0)  # Owner name and starting balance

    if len(sys.argv) < 2:
        print("Usage: python3 main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command_parts = sys.argv[1].split(':')
    command = command_parts[0]
    amount = float(command_parts[1]) if len(command_parts) > 1 else None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
    elif command == "withdraw" and amount is not None:
        account.withdraw(amount)
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
