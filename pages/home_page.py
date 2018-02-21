from base.base_setup import BaseSetup
from base.webdriver_custom_class import WebDriverCustomClass
from utilities.ui_map import home_page


class HomePage(BaseSetup, WebDriverCustomClass):

    def search_product(self, searched_product):
        self.send_keys_to(home_page.get("searchFieldByID"), searched_product)