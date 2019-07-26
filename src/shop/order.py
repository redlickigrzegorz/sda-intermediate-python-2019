from datetime import datetime


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
            value += (item.product.price - item.product.price * self.discount) * item.quantity
        return value
