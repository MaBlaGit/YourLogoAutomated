from base.base_setup import BaseSetup
from pages.home_page import HomePage
import unittest


class SearchProductTest(BaseSetup, unittest.TestCase):

    def setUp(self):
        super(SearchProductTest, self).setUp()
        self.home_page = HomePage(self.driver)

    def test_search_product(self):
        self.home_page.search_product("Blouse")

    def tearDown(self):
        super(SearchProductTest, self).tearDown()


if __name__ == '__main__':
    unittest.main()
