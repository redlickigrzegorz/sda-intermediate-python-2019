import typing

from src.shop.customer import Customer
from src.shop.order import Order
from src.shop.item import Item
from src.shop.product import *


def notify_everyone(orders: typing.List[Order]):
    for order in orders:
        order.customer.notify()

def place_order(customer, *items):
    '''
    # customer jako obiekt klasy, items jako lista [produkt, ilość"
    - nie umiem tego zapisać poprzez typowanie
    '''
    order = Order(customer)
    for i in items:
        order.add_item(Item(i[0], i[1]))
    return order


if __name__ == "__main__":
    bob = Customer("Bob")
    john = Customer("John")

    order_1 = Order(bob)
    order_2 = Order(john)

    notify_everyone([order_1, order_2])

if __name__ == '__main__':
    a = place_order(bob, [tv, 1], [iPhone, 1], [chocolate, 2])
    print(a.items)
