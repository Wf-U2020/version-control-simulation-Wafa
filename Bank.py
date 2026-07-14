class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")

        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds.")

        self.balance -= amount
        return self.balance

    def __str__(self):
        return (f"Account {self.account_number} - "
                f"Owner: {self.owner}, "
                f"Balance: ${self.balance:.2f}")
    
    #Test code
if __name__ == "__main__":
    # Create an account
    account = BankAccount("12345", "Alice", 500)

    print("Initial account:")
    print(account)

    # Successful deposit
    try:
        account.deposit(200)
        print("\nAfter depositing $200:")
        print(account)
    except ValueError as e:
        print("Deposit Error:", e)

    # Successful withdrawal
    try:
        account.withdraw(100)
        print("\nAfter withdrawing $100:")
        print(account)
    except ValueError as e:
        print("Withdrawal Error:", e)
# Withdrawal that exceeds balance
    try:
        account.withdraw(1000)
    except ValueError as e:
        print("\nWithdrawal Error:", e)