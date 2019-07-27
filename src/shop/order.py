from datetime import datetime

from src.shop.rounding import round_value


class Order:

    def __init__(self, customer):
        self.items = []
        self.date = datetime.now()
        self.customer = customer
        self.discount = customer.personal_discount / 100

    def add_item(self, item):
        self.items.append(item)

    @property
    def value(self):
        value = 0
        for item in self.items:
            product_value = item.product.price - round_value(item.product.price * self.discount)
            value += product_value * item.quantity
        return value
