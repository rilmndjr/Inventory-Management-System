class BankAccount:
    def __init__(self, account_holder, account_number, balance=0):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited ${amount}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append(f"Withdrew ${amount}")
        else:
            print("Insufficient funds")

    def transfer(self, amount, recipient_account):
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append(f"Transferred ${amount} to {recipient_account}")
            recipient_account.deposit(amount)
        else:
            print("Insufficient funds")

    def print_statement(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: ${self.balance}")
        print("Transactions:")
        for transaction in self.transactions:
            print(transaction)

# Example usage:
account1 = BankAccount("John Doe", "123456789")
account2 = BankAccount("Jane Smith", "987654321")

account1.deposit(1000)
account1.withdraw(500)
account1.transfer(200, account2)

account1.print_statement()
print("\n")
account2.print_statement()
