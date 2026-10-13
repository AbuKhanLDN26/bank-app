class Account:
    def __init__(self, owner: str, balance: float = 0) -> None:
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit must be greater than 0")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if self.balance - amount >= 0:
            self.balance -= amount
        elif amount<=0:
                raise ValueError("Invalid Withdrawal Amount")
        elif self.balance - amount <0:
            raise ValueError("Insufficient Funds")

    def __str__(self) -> str:
        return (f"{self.owner}: £{self.balance:,.2f}")