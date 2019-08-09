import decimal
from dataclasses import dataclass, field


@dataclass
class Customer:
    name: str
    personal_discount: decimal.Decimal = field(default=decimal.Decimal("0.00"))

    def notify(self):
        print(f"Customer {self.name} has been notified!")
