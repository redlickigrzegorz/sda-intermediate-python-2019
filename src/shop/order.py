from datetime import datetime

from src.shop import Customer
from src.shop.exceptions import ItemValueNotPositive
from src.shop.item import Item
from src.shop.rounding import round_value


class Order:
    def __init__(self, customer: Customer):
        self.items = []
        self.date = datetime.now()
        self.customer = customer
        self.discount = customer.personal_discount / 100

    def add_item(self, item: Item):
        if item.quantity > 0 and item.product.price > 0:
            self.items.append(item)
        else:
            raise ItemValueNotPositive()

    @property
    def value(self):
        value = 0
        for item in self.items:
            product_value = item.product.price - round_value(item.product.price * self.discount)
            value += product_value * item.quantity
        return value
