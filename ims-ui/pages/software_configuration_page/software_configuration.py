import os
import time

from selenium.common import StaleElementReferenceException

from pages.base_page import BasePage
from pages.software_configuration_page.software_configuration_locators import software_configuration_page_locators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class SoftwareConfigurationPage(BasePage):
    locators_dict = {name: locator for name, locator in software_configuration_page_locators}

    """constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_software_configuration_page(self, url):
        self.driver.get(url)

    def choose_a_template(self):
        self.do_click(self.locators_dict["TEMPLATE"])
        time.sleep(15)

    def choose_a_section(self):
        self.do_click(self.locators_dict["SECTION"])
        time.sleep(15)

    def choose_an_avaliable_fragment(self):
        self.do_click(self.locators_dict["AVAILABLE_FRAGMENT"])
        time.sleep(10)

    def get_text(self):
        text = self.get_element_text(self.locators_dict["ASSIGNED_FRAGMENT"])
        print("hello got the text!!!", text)
        return text

    def select_assigned_fragment_btn(self):
        self.do_click(self.locators_dict["ASSIGN_FRAGMENT_BTN"])
        time.sleep(15)
