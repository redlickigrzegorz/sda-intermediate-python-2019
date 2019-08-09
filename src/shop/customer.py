import decimal


class Customer:
    def __init__(self, name: str, personal_discount: decimal.Decimal = decimal.Decimal("0.00")) -> None:
        self.name = name
        self.personal_discount = personal_discount

    def notify(self) -> None:
        print(f"Customer {self.name} has been notified!")
