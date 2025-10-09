import sys
from bank_account import BankAccount

if __name__ == "__main__":
    account = BankAccount(250)

    if len(sys.argv) > 1:
        command = sys.argv[1]

        if command.startswith("deposit:"):
            amount = float(command.split(":")[1])
            account.deposit(amount)
        elif command.startswith("withdraw:"):
            amount = float(command.split(":")[1])
            account.withdraw(amount)
        elif command == "balance":
            account.display_balance()
        else:
            print("Invalid command.")
    else:
        print("No command provided.")