import typing

from src.shop.customer import Customer
from src.shop.order import Order
from src.shop.item import Item
from src.shop.product import *


def notify_everyone(orders: typing.List[Order]):
    for order in orders:
        order.customer.notify()

def place_order(customer: Customer, *items: typing.Tuple[Product, int]) -> Order:
    order = Order(customer)
    for i in items:
        order.add_item(i)
    return order


if __name__ == "__main__":
    bob = Customer("Bob")
    john = Customer("John")

    order_1 = Order(bob)
    order_2 = Order(john)

    notify_everyone([order_1, order_2])

    #homework
    item_tv = Item(tv, 1)
    item_iPhone = Item(iPhone, 1)
    item_chocolate = Item(chocolate, 2)
    a = place_order(bob, item_tv, item_iPhone, item_chocolate)
    print(a.items)
