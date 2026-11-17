class BankAccount:

    def __init__(self, balance=0):
        self._validate_initial_balance(balance)
        self.balance = balance

    def _validate_initial_balance(self, balance):
        if not isinstance(balance, (int, float)):
            raise TypeError("Initial balance must be numeric")
        if balance < 0:
            raise ValueError("Initial balance cannot be negative")

    def _validate(self, amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be numeric")
        if amount <= 0:
            raise ValueError("Amount must be positive")

    def deposit(self, amount):
        self._validate(amount)
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self._validate(amount)
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return self.balance

    def transfer(self, target_account, amount):
        if not isinstance(target_account, BankAccount):
            raise TypeError("Target must be a BankAccount instance")
        self.withdraw(amount)
        target_account.deposit(amount)
        return self.balance