import decimal
import unittest

from src.shop.customer import Customer
from src.shop.item import Item
from src.shop.order import Order
from src.shop.product import game, headphones, computer


class TestOrder(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.customer = Customer("John", decimal.Decimal("0.00"))
        cls.customer_with_discard = Customer("Bob", decimal.Decimal("5.00"))

    def test_should_add_products_into_order(self):
        # GIVEN
        order = Order(self.customer)
        items = [Item(game, 1), Item(headphones, 2), Item(computer, 2)]

        # WHEN
        order.add_item(items[0])
        order.add_item(items[1])
        order.add_item(items[2])

        # THEN
        self.assertListEqual(items, order.items)

    def test_should_calculate_order_value(self):
        # GIVEN
        order = Order(self.customer)
        order.add_item(Item(game, 1))
        order.add_item(Item(headphones, 2))
        order.add_item(Item(computer, 2))
        expected_order_value = decimal.Decimal("12795.90")

        # WHEN
        actual_order_value = order.value

        # THEN
        self.assertEqual(expected_order_value, actual_order_value)

    def test_should_calculate_order_value_with_personal_discount(self):
        # GIVEN
        order = Order(self.customer_with_discard)
        order.add_item(Item(game, 1))
        order.add_item(Item(headphones, 2))
        order.add_item(Item(computer, 2))
        expected_order_value = decimal.Decimal("12156.11")

        # WHEN
        actual_order_value = order.value

        # THEN
        self.assertEqual(expected_order_value, actual_order_value)


if __name__ == "__main__":
    unittest.main()
