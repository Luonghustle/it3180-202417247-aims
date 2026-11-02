import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_category


class TestSearchByCategory(unittest.TestCase):
    def test_search_by_category(self):
        items = [DigitalVideoDisc("The Lion King", "Animation"),
                 DigitalVideoDisc("Star Wars", "Science Fiction"),
                 DigitalVideoDisc("Aladdin", "Animation")]
        result = [d.title for d in search_by_category(items, "animation")]
        self.assertEqual(result, ["The Lion King", "Aladdin"])


if __name__ == "__main__":
    unittest.main()
