from pages.base_page import BasePage
from pages.virtual_view_page.virtual_view_page_locators import virtual_view_page_locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class VirtualViewPage(BasePage):
    locators_dict = {name: locator for name, locator in virtual_view_page_locators}

    """constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_virtual_view_page(self, url):
        self.driver.get(url)

    def check_for_password_link(self):
        password_link_presence = self.check_element_presence(self.locators_dict["VIEW_HARDWARE_CREDENTIALS"][1])
        return password_link_presence.text
