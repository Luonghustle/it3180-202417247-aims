import unittest

from aims.cart import Cart
from aims.dvd import DigitalVideoDisc


class TestSort(unittest.TestCase):
    def setUp(self):
        self.cart = Cart()
        for title, cost in [("Star Wars", 24.95), ("Aladdin", 18.99), ("The Lion King", 19.95), ("Aladdin", 25.0)]:
            self.cart.add_dvd(DigitalVideoDisc(title, cost=cost))

    def test_sort_by_title(self):
        result = [(d.title, d.cost) for d in self.cart.sort_by_title()]
        self.assertEqual(result, [("Aladdin", 25.0), ("Aladdin", 18.99), ("Star Wars", 24.95), ("The Lion King", 19.95)])

    def test_sort_by_cost(self):
        result = [d.cost for d in self.cart.sort_by_cost()]
        self.assertEqual(result, [25.0, 24.95, 19.95, 18.99])


if __name__ == "__main__":
    unittest.main()
