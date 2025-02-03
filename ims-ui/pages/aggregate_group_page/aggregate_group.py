import time

import requests
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage
from pages.aggregate_group_page.aggregate_group_locators import aggregate_group_page_locators
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class AggregateGroupPage(BasePage):
    locators_dict = {name: locator for name, locator in aggregate_group_page_locators}

    """constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_aggregate_group_page(self, url):
        self.driver.get(url)

    def new_group_creation(self, new_group):
        self.do_send_keys(self.locators_dict["DESCRIPTION"], new_group)
        self.do_click(self.locators_dict["SUBMIT"])
        time.sleep(10)
        status_msg = self.get_element_text(self.locators_dict["STATUS_MESSAGE"])
        return status_msg.strip()

    def group_deletion(self):
        self.do_click(self.locators_dict["CREATE_AGGREGATE_GRP_LINK"])
        time.sleep(5)
        self.do_click(self.locators_dict["DELETE"])
        alert = Alert(self.driver)
        alert.accept()
        time.sleep(5)
        self.driver.refresh()
        try:
            self.driver.find_element(By.XPATH, self.locators_dict["DELETE"][1])
        except NoSuchElementException:
            return "Deleted"
        return "not Deleted"
    
