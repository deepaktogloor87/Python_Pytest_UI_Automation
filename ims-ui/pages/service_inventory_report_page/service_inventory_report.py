import requests
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage
from pages.service_inventory_report_page.service_inventory_report_locators import service_inventory_report_page_locators
from selenium.webdriver.common.by import By


class ServiceInventoryReportPage(BasePage):
    locators_dict = {name: locator for name, locator in service_inventory_report_page_locators}

    """constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_service_inventory_report_page(self, url):
        self.driver.get(url)

    def get_the_details_of_account_id(self):
        is_editable = self.check_if_element_is_editable(self.locators_dict["ACCOUNT_ID"])
        return is_editable

    def get_the_details_of_company_name(self):
        is_editable = self.check_if_element_is_editable(self.locators_dict["COMPANY_NAME"])
        return is_editable

    def get_the_details_of_hostname(self):
        is_editable = self.check_if_element_is_editable(self.locators_dict["HOST_NAME"])
        return is_editable

    def get_the_details_of_ip_address(self):
        is_editable = self.check_if_element_is_editable(self.locators_dict["IP_ADDR"])
        return is_editable

    def get_the_details_of_evault_username(self):
        is_editable = self.check_if_element_is_editable(self.locators_dict["EVAULT_USERNAME"])
        return is_editable

    def get_the_details_of_company_name_checkbox(self):
        element = self.driver.find_element(By.XPATH, self.locators_dict["COMPANY_NAME_CHECKBOX"][1])
        checkbox_options = Select(element)
        all_options = checkbox_options.options
        all_options_list = []
        for option in all_options:
            all_options_list.append(option.text)
        return all_options_list

    def get_the_details_of_hostname_checkbox(self):
        element = self.driver.find_element(By.XPATH, self.locators_dict["HOSTNAME_CHECKBOX"][1])
        checkbox_options = Select(element)
        all_options = checkbox_options.options
        all_options_list = []
        for option in all_options:
            all_options_list.append(option.text)
        return all_options_list

    def get_the_details_of_ip_addr_checkbox(self):
        element = self.driver.find_element(By.XPATH, self.locators_dict["IP_ADDR_CHECKBOX"][1])
        checkbox_options = Select(element)
        all_options = checkbox_options.options
        all_options_list = []
        for option in all_options:
            all_options_list.append(option.text)
        return all_options_list

    def get_the_details_of_evault_username_checkbox(self):
        element = self.driver.find_element(By.XPATH, self.locators_dict["EVAULT_USERNAME_CHECKBOX"][1])
        checkbox_options = Select(element)
        all_options = checkbox_options.options
        all_options_list = []
        for option in all_options:
            all_options_list.append(option.text)
        return all_options_list

    def get_the_details_of_show_with_evault_checkbox(self):
        element = self.driver.find_element(By.XPATH, self.locators_dict["EVAULT_USERNAME_CHECKBOX"][1])
        checkbox_options = Select(element)
        all_options = checkbox_options.options
        all_options_list = []
        for option in all_options:
            all_options_list.append(option.text)
        return all_options_list

    def get_the_details_of_object_type_checkbox(self):
        element = self.driver.find_element(By.XPATH, self.locators_dict["OBJECT_TYPE"][1])
        checkbox_options = Select(element)
        all_options = checkbox_options.options
        all_options_list = []
        for option in all_options:
            all_options_list.append(option.text)
        return all_options_list

    def get_the_details_of_object_status_checkbox(self):
        element = self.driver.find_element(By.XPATH, self.locators_dict["OBJECT_STATUS"][1])
        checkbox_options = Select(element)
        all_options = checkbox_options.options
        all_options_list = []
        for option in all_options:
            all_options_list.append(option.text)
        return all_options_list

    def get_the_details_of_managed_server_checkbox(self):
        element = self.driver.find_element(By.XPATH, self.locators_dict["MANAGED_SERVER"][1])
        checkbox_options = Select(element)
        all_options = checkbox_options.options
        all_options_list = []
        for option in all_options:
            all_options_list.append(option.text)
        return all_options_list

    def get_the_details_of_search_button(self):
        button = self.driver.find_element(By.XPATH, self.locators_dict["SEARCH_BTN"][1])
        clickable = self.is_clickable(button)
        return clickable
 
