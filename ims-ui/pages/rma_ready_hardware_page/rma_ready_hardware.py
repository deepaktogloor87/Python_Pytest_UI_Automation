import requests
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage
from pages.rma_ready_hardware_page.rma_ready_hardware_locators import rma_ready_hardware_page_locators
from selenium.webdriver.common.by import By


class RMAReadyHardwarePage(BasePage):
    locators_dict = {name: locator for name, locator in rma_ready_hardware_page_locators}

    """constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_rma_ready_hardware_page(self, url):
        self.driver.get(url)

    def get_the_details_of_checkbox(self, by_locator):
        element = self.driver.find_element(By.XPATH, by_locator)
        checkbox_options = Select(element)
        all_options = checkbox_options.options
        all_options_list = []
        for option in all_options:
            all_options_list.append(option.text)
        return all_options_list

    def get_the_details_of_serial_number_txt_box(self):
        is_displayed = self.check_if_element_is_displayed(self.locators_dict["SERIAL_NUMBER"])
        is_editable = self.check_if_element_is_editable(self.locators_dict["SERIAL_NUMBER"])
        return True if (is_displayed and is_editable) else False

    def get_the_details_of_location_dropbox(self):
        location_items = self.get_the_details_of_checkbox(self.locators_dict["LOCATION"][1])
        return location_items

    def get_the_details_of_hardware_function_dropbox(self):
        hardware_function_items = self.get_the_details_of_checkbox(self.locators_dict["HARDWARE_FUNCTION"][1])
        return hardware_function_items

    def get_the_details_of_rma_number_dropbox(self):
        rma_number_items = self.get_the_details_of_checkbox(self.locators_dict["RMA_NUMBER"][1])
        return rma_number_items

    def get_the_details_of_search_btn(self):
        search_btn_element = self.driver.find_element(By.XPATH, self.locators_dict["SEARCH_BTN"][1])
        is_clickable = self.is_clickable(search_btn_element)
        return is_clickable

    def get_the_details_of_assign_btn(self):
        assign_btn_element = self.driver.find_element(By.XPATH, self.locators_dict["ASSIGN_BTN"][1])
        is_clickable = self.is_clickable(assign_btn_element)
        return is_clickable

    def get_the_details_of_rma_ready_hardware_table_details(self):
        table = self.driver.find_element(By.XPATH, self.locators_dict["RMA_READY_HARDWARE_TABLE"][1])
        rows = table.find_elements(By.TAG_NAME, 'tr')
        table = []
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, 'td')
            row_data = []
            for cell in cells:
                if cell.is_displayed():
                    row_data.append(cell.text)
            table.append(row_data)
        return table

    def select_50_per_page_from_displaying_checkbox(self):
        displaying_element = self.driver.find_element(By.XPATH, self.locators_dict["DISPLAYING_CHECKBOX"][1])
        select = Select(displaying_element)
        select.select_by_visible_text("50 per page")
        
