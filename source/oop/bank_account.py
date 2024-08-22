from source.helpers import get_date


class BankAccount:

    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.balance = initial_balance
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            raise Exception("Invalid amount, amount must be greater than 0")

        self.balance += amount
        self.transactions.append(
            f"Deposited: {amount}. new balance: {self.balance} - Date: {get_date()}")

        return f"Deposited: {amount}"

    def withdraw(self, amount):
        if self.balance <= amount :
            raise Exception("Withdraw Cannot be Completed, insufficient balance")

        if self.balance > 0:
            self.balance -= amount
            self.transactions.append(
                f"Withdraw: {amount}. new balance: {self.balance} - Date: {get_date()}")

        return f"Withdraw: {amount}, Balance: {self.balance}"

    def check_balance(self):
        return f"Your current balance: {self.balance}"

    def account_info(self):
        return f"Account owner: {self.owner}\nCurrent balance: {self.balance}"

    def transaction_history(self):
        return "\n".join(self.transactions)
