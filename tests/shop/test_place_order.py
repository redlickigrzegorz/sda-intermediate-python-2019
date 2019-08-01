import unittest

from src.shop import place_order
from src.shop.customer import Customer
from src.shop.item import Item
from src.shop.product import tv
from src.shop.product import iPhone
from src.shop.product import chocolate


class TestPlaceOrder(unittest.TestCase):

    def setUp(self):
        self.item_tv = Item(tv, 1)
        self.item_iPhone = Item(iPhone, 1)
        self.item_chocolate = Item(chocolate, 2)
        self.bob = Customer("Bob")

    def test_01(self):
        order = place_order(self.bob, self.item_tv, self.item_iPhone, self.item_chocolate)
        self.assertEqual(1510, order.value)

    def test_02(self):
        order = place_order(self.bob, self.item_tv, self.item_iPhone, self.item_chocolate)
        self.assertEqual(self.bob, order.customer)


