import decimal
import unittest

from src.shop.customer import Customer
from src.shop.item import Item
from src.shop.order import Order
from src.shop.product import Product


class TestOrder(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.customer = Customer("John", decimal.Decimal("0.00"))  # type: ignore
        cls.customer_with_discard = Customer("Bob", decimal.Decimal("5.00"))  # type: ignore

        cls.game = Product("The Witcher III", "PS4 games", decimal.Decimal("199.90"))  # type: ignore
        cls.headphones = Product("Bose QuietComfort 35 II", "headphones", decimal.Decimal("1299.00"))  # type: ignore
        cls.computer = Product(  # type: ignore
            "Apple MacBook Air 2018", "notebook computer", decimal.Decimal("4999.00")
        )

    def test_should_add_products_into_order(self) -> None:
        # GIVEN
        order = Order(self.customer)  # type: ignore
        items = [Item(self.game, 1), Item(self.headphones, 2), Item(self.computer, 2)]  # type: ignore

        # WHEN
        order.add_item(items[0])
        order.add_item(items[1])
        order.add_item(items[2])

        # THEN
        self.assertListEqual(items, order.items)

    def test_should_calculate_order_value(self) -> None:
        # GIVEN
        order = Order(self.customer)  # type: ignore
        order.add_item(Item(self.game, 1))  # type: ignore
        order.add_item(Item(self.headphones, 2))  # type: ignore
        order.add_item(Item(self.computer, 2))  # type: ignore
        expected_order_value = decimal.Decimal("12795.90")

        # WHEN
        actual_order_value = order.value

        # THEN
        self.assertEqual(expected_order_value, actual_order_value)

    def test_should_calculate_order_value_with_personal_discount(self) -> None:
        # GIVEN
        order = Order(self.customer_with_discard)  # type: ignore
        order.add_item(Item(self.game, 1))  # type: ignore
        order.add_item(Item(self.headphones, 2))  # type: ignore
        order.add_item(Item(self.computer, 2))  # type: ignore
        expected_order_value = decimal.Decimal("12156.11")

        # WHEN
        actual_order_value = order.value

        # THEN
        self.assertEqual(expected_order_value, actual_order_value)


if __name__ == "__main__":
    unittest.main()
