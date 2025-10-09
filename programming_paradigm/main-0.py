import sys
from bank_account import BankAccount

def main():
    account = BankAccount(0)  # Start with 0 balance

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
        account.deposit(amount)
    elif command == "withdraw" and amount is not None:
        if not account.withdraw(amount):
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
