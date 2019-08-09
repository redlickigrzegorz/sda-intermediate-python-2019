import decimal
import typing
from dataclasses import dataclass, field
from datetime import datetime

from src.shop import Customer, Item
from src.shop.rounding import round_value


@dataclass
class Order:
    customer: Customer
    items: typing.List[Item] = field(default_factory=list)
    date: datetime = field(default_factory=datetime.now)

    @property
    def discount(self) -> decimal.Decimal:
        return self.customer.personal_discount / 100

    @property
    def value(self):
        value = 0
        for item in self.items:
            product_value = item.product.price - round_value(item.product.price * self.discount)
            value += product_value * item.quantity
        return value

    def add_item(self, item):
        self.items.append(item)
