import time
import requests
from pages.base_page import BasePage
from pages.server_prebuild_page.server_prebuild_locators import server_prebuild_page_locators
from selenium.webdriver.common.by import By


class ServerPrebuildPage(BasePage):
    locators_dict = {name: locator for name, locator in server_prebuild_page_locators}

    """constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_server_prebuild_page(self, url):
        self.driver.get(url)

    def get_editable_status_of_hardware_id(self):
        is_editable = self.check_if_form_is_editable(self.locators_dict["HARDWARE_ID"])
        return is_editable

    def get_editable_status_of_base_server_id(self):
        is_editable = self.check_if_form_is_editable(self.locators_dict["BASE_HARDWARE_ID"])
        return is_editable

    def get_editable_status_of_softlayer_ticket_id(self):
        is_editable = self.check_if_form_is_editable(self.locators_dict["SOFTLAYER_TICKET_ID"])
        return is_editable

    def click_on_server_prebuild_job_tab(self):
        self.do_click(self.locators_dict["SEARCH_PREBUILD_JOBS"])

    def get_editable_status_of_spj_base_server_id(self):
        is_editable = self.check_if_form_is_editable(self.locators_dict["SPJ_BASE_SERVER_ID"])
        return is_editable

    def get_editable_status_of_spj_softlayer_ticket_id(self):
        is_editable = self.check_if_form_is_editable(self.locators_dict["SPJ_SOFTLAYER_TICKET_ID"])
        return is_editable

    def get_editable_status_of_spj_prebuild_job_id(self):
        is_editable = self.check_if_form_is_editable(self.locators_dict["SPJ_PREBUILD_JOB_ID"])
        return is_editable

    def get_editable_status_of_spj_user_id(self):
        is_editable = self.check_if_form_is_editable(self.locators_dict["SPJ_USER_ID"])
        return is_editable

    def get_details_of_create_button_cpj(self):
        is_displayed = self.check_if_element_is_displayed(self.locators_dict["CPJ_CREATE_BUTTON"])
        is_clickable = self.is_clickable(self.driver.find_element(By.XPATH, self.locators_dict["CPJ_CREATE_BUTTON"][1]))
        return True if (is_displayed and is_clickable) else False

    def get_details_of_reset_button_cpj(self):
        is_displayed = self.check_if_element_is_displayed(self.locators_dict["CPJ_RESET_BUTTON"])
        is_clickable = self.is_clickable(self.driver.find_element(By.XPATH, self.locators_dict["CPJ_RESET_BUTTON"][1]))
        return True if (is_displayed and is_clickable) else False

    def get_details_of_search_button_spj(self):
        is_displayed = self.check_if_element_is_displayed(self.locators_dict["SPJ_SEARCH_BUTTON"])
        is_clickable = self.is_clickable(self.driver.find_element(By.XPATH, self.locators_dict["SPJ_SEARCH_BUTTON"][1]))
        return True if (is_displayed and is_clickable) else False

    def get_details_of_reset_button_spj(self):
        is_displayed = self.check_if_element_is_displayed(self.locators_dict["SPJ_ROP_BUTTON"])
        is_clickable = self.is_clickable(self.driver.find_element(By.CSS_SELECTOR, self.locators_dict["SPJ_ROP_BUTTON"][1]))
        return True if (is_displayed and is_clickable) else False

