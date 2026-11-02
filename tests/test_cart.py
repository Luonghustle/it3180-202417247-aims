import unittest

from aims.cart import Cart, MAX_NUMBERS_ORDERED
from aims.dvd import DigitalVideoDisc


class TestCart(unittest.TestCase):
    def test_add_dvd_until_full(self):
        cart = Cart()
        for i in range(MAX_NUMBERS_ORDERED):
            self.assertTrue(cart.add_dvd(DigitalVideoDisc(f"DVD {i}", cost=1.0)))
        self.assertFalse(cart.add_dvd(DigitalVideoDisc("DVD 21", cost=1.0)))
        self.assertEqual(len(cart.items), MAX_NUMBERS_ORDERED)

    def test_total_cost(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("A", cost=19.95))
        cart.add_dvd(DigitalVideoDisc("B", cost=24.95))
        cart.add_dvd(DigitalVideoDisc("C", cost=18.99))
        self.assertAlmostEqual(cart.total_cost(), 63.89)


if __name__ == "__main__":
    unittest.main()
