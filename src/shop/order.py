import decimal
import typing
from datetime import datetime

from src.shop import Customer
from src.shop.item import Item
from src.shop.rounding import round_value


class Order:
    def __init__(self, customer: Customer) -> None:
        self.items: typing.List[Item] = []
        self.date = datetime.now()
        self.customer = customer
        self.discount = customer.personal_discount / 100

    def add_item(self, item: Item) -> None:
        self.items.append(item)

    @property
    def value(self) -> decimal.Decimal:
        value = decimal.Decimal("0")
        for item in self.items:
            product_value = item.product.price - round_value(item.product.price * self.discount)
            value += product_value * item.quantity
        return value
