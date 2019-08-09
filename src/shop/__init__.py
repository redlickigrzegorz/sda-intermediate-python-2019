import typing

from src.shop.customer import Customer
from src.shop.exceptions import EmptyOrderError
from src.shop.item import Item
from src.shop.order import Order


def place_order(customer: Customer, *items: Item) -> Order:
    if not items:
        raise EmptyOrderError()

    order = Order(customer)
    for item in items:
        order.add_item(item)
    return order


def notify_everyone(orders: typing.List[Order]):
    for order in orders:
        order.customer.notify()


if __name__ == "__main__":
    bob = Customer("Bob")
    john = Customer("John")

    order_1 = Order(bob)
    order_2 = Order(john)

    notify_everyone([order_1, order_2])
