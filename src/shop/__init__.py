import typing

from src.shop.customer import Customer
from src.shop.order import Order


def notify_everyone(orders: typing.List[Order]):
    for order in orders:
        order.customer.notify()


if __name__ == "__main__":
    bob = Customer("Bob")
    john = Customer("John")

    order_1 = Order(bob)
    order_2 = Order(john)

    notify_everyone([order_1, order_2])
