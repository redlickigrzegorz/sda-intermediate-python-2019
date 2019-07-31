import unittest

from src.shop.__init__ import *


class Place_order(unittest.TestCase):
    def test_01(self):
        bob = Customer("Bob")
        order = place_order(bob, [tv, 1], [iPhone, 1], [chocolate, 2])
        self.assertEqual(1510, order.value)

    def test_02(self):
        bob = Customer("Bob")
        order = place_order(bob, [tv, 1], [iPhone, 1], [chocolate, 2])
        self.assertEqual(bob, order.customer)


