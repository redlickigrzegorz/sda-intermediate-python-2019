import unittest

from src.shop import Item, Customer, place_order, Product, Order


class TestPlaceOrder(unittest.TestCase):

    def setUp(self) -> None:
        """
        Creating items and customers
        :return:
        """
        self.cust1 = Customer('Marek')

        self.consola1 = Product('PS4', 'Consola', 300)
        self.book1 = Product('Cars', 'Book', 30)
        self.book2 = Product('Star Wars', 'Book', 20)

        self.item1 = Item(self.consola1, 1)
        self.item2 = Item(self.book1, 2)
        self.item3 = Item(self.book2, 3)



    def test_01_calculate_order_value(self):
        order = place_order(self.cust1, self.item1, self.item2, self.item3)
        self.assertEqual(420, order.value)

    def test_02_does_class_is_correct(self):
        order = place_order(self.cust1, self.item1, self.item2, self.item3)
        self.assertIsInstance(self.cust1, Customer)
        self.assertIsInstance(order, Order)

    






