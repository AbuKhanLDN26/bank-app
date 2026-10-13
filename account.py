class Account:
    def __init__(self, owner: str, balance: float = 0) -> None:
        if balance < 0:
            raise ValueError("Minimum balance of a new account is 0")
        self.owner = owner
        self.balance = balance
        self.history: list[tuple[str, float]] = []

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit must be greater than 0")
        self.balance += amount
        self.history.append(("Deposit", amount))

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Invalid Withdrawal Amount")
        elif amount > self.balance:
            raise ValueError("Insufficient Funds")
        self.balance -= amount
        self.history.append(("Withdraw", amount))

    def __str__(self) -> str:
        return f"{self.owner}: £{self.balance:,.2f}"

    def transaction_history(self) -> tuple[tuple[str, float], ...]:
        return tuple(self.history)