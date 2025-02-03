from pages.base_page import BasePage
from pages.hardware_view_edit_page.hardware_view_edit_page_locators import hardware_view_edit_page_locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class HardwareViewEditPage(BasePage):
    locators_dict = {name: locator for name, locator in hardware_view_edit_page_locators}

    """constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_hardware_view_page(self, url):
        self.driver.get(url)

    def check_for_mask_password_link(self):
        password_link_presence = self.check_element_presence(self.locators_dict["VIEW_HARDWARE_CREDENTIALS_LINK"][1])
        return password_link_presence.text
