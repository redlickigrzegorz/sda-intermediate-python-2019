import typing

from src.shop.customer import Customer
from src.shop.order import Order
from src.shop.item import Item
from src.shop.product import Product


def notify_everyone(orders: typing.List[Order]):
    for order in orders:
        order.customer.notify()

def place_order(customer: Customer, *items: typing.Tuple[Product, int]) -> Order:
    user_order = Order(customer)
    # print(f'{customer.name} bought:', end=" ")
    for i in items:
        user_order.add_item(i)
    return user_order


if __name__ == "__main__":

    bob = Customer("Bob")
    john = Customer("John")

    order_1 = Order(bob)
    order_2 = Order(john)

    notify_everyone([order_1, order_2])

    # ========
    consola1 = Product('PS4', 'Consola', 300)
    book1 = Product('Cars', 'Book', 30)

    item1 = Item(consola1, 2)
    item2 = Item(book1, 1)

    print(place_order(bob, item1, item2).items)
    print(place_order(bob, item1, item2).value)



