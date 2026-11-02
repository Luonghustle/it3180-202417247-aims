import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_title


class TestSearchByTitle(unittest.TestCase):
    def test_search_by_title_is_case_insensitive(self):
        items = [DigitalVideoDisc("The Lion King"), DigitalVideoDisc("Star Wars")]
        self.assertEqual([d.title for d in search_by_title(items, "lion")], ["The Lion King"])
        self.assertEqual([d.title for d in search_by_title(items, "STAR")], ["Star Wars"])


if __name__ == "__main__":
    unittest.main()
