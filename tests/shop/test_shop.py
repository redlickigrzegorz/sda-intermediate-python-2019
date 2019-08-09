import decimal
import unittest

from src.shop import Customer, place_order, Item
from src.shop.exceptions import EmptyOrderError
from src.shop.product import game, headphones, computer


class TestShop(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.customer = Customer("John", decimal.Decimal("0.00"))

    def test_should_place_order_with_one_item(self) -> None:
        item_to_buy = Item(game, 3)
        expected_items = [item_to_buy]

        actual_order = place_order(self.customer, item_to_buy)

        self.assertListEqual(expected_items, actual_order.items)

    def test_should_place_order_with_more_items(self) -> None:
        item_to_buy_1 = Item(game, 3)
        item_to_buy_2 = Item(headphones, 2)
        item_to_buy_3 = Item(computer, 1)
        expected_items = [item_to_buy_1, item_to_buy_2, item_to_buy_3]

        actual_order = place_order(self.customer, item_to_buy_1, item_to_buy_2, item_to_buy_3)

        self.assertListEqual(expected_items, actual_order.items)

    def test_should_not_allow_place_order_without_items(self) -> None:
        with self.assertRaises(EmptyOrderError):
            place_order(self.customer)


if __name__ == '__main__':
    unittest.main()
