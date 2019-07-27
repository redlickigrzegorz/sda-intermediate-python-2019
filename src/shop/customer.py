import decimal


class Customer:
    def __init__(self, name, personal_discount=decimal.Decimal("0.00")):
        self.name = name
        self.personal_discount = personal_discount

    def notify(self):
        print(f"Customer {self.name} has been notified!")
