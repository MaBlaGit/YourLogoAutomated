from base.base_setup import BaseSetup
from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.shopping_cart_page import ShoppingCartPage
from utilities import data_provider
import unittest


class SearchProductTest(BaseSetup, unittest.TestCase):

    def setUp(self):
        super(SearchProductTest, self).setUp()
        self.home_page = HomePage(self.driver)
        self.product_page = ProductPage(self.driver)
        self.shopping_cart_page = ShoppingCartPage(self.driver)
        self.data = data_provider.test_data_provider()

    def test_check_if_product_was_added_th_the_cart(self):
        self.home_page.search_product(self.data.get("search_item"))
        self.home_page.search_button()
        self.product_page.select_product()
        self.product_page.continue_shopping_button()
        self.home_page.cart_button()
        self.shopping_cart_page.cart_products()
        self.assertEqual(self.shopping_cart_page.cart_products()[-1].text, "Blouse")

    def tearDown(self):
        super(SearchProductTest, self).tearDown()


if __name__ == '__main__':
    unittest.main()
