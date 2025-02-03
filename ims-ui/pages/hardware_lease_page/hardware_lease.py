import os
import time

from selenium.common import StaleElementReferenceException

from pages.base_page import BasePage
from pages.hardware_lease_page.hardware_lease_locators import hardware_lease_page_locators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class HardwareLeasePage(BasePage):
    locators_dict = {name: locator for name, locator in hardware_lease_page_locators}

    """constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_hardware_lease_page(self, url):
        self.driver.get(url)

    def verify_department_dropdown_accessibility(self, department, department_value):
        time.sleep(10)
        self.check_if_element_is_clickable(self.locators_dict["DEPARTMENT"])
        element = self.driver.find_element(By.XPATH, self.locators_dict["DEPARTMENT"][1])
        select = Select(element)
        select.select_by_visible_text(department)
        time.sleep(5)
        if element.get_attribute('value') == department_value:
            return True
        else:
            return False

    def inspect_ship_to_add_value(self):
        self.check_if_element_is_displayed(self.locators_dict["SHIP_TO_ADDR"])
        ship_to = self.driver.find_element(By.XPATH, self.locators_dict["SHIP_TO_ADDR"][1])
        if ship_to.get_attribute('value') != None:
            return True
        else:
            return False

    def get_lead_time_length(self, ):
        element = self.driver.find_element(By.XPATH, self.locators_dict["LEAD_TIME"][1])
        maxlength = element.get_attribute("maxlength")
        return int(maxlength)

    def insert_lead_time(self, value):
        time.sleep(5)
        lead_time = self.driver.find_element(By.XPATH, self.locators_dict["LEAD_TIME"][1])
        lead_time.clear()
        self.do_send_keys(self.locators_dict["LEAD_TIME"], value)
        self.do_click(self.locators_dict["SAVE"])
        time.sleep(10)
        print("value", lead_time.text)

    def extract_status_value(self):
        status = self.driver.find_element(By.XPATH, self.locators_dict["STATUS"][1])
        if status.get_attribute("value") == "Ordered":
            return True
        else:
            return False

    def total_amount_status_check(self):
        total_amount = self.driver.find_element(By.XPATH, self.locators_dict["TOTAL_AMOUNT"][1])
        print("total amount", total_amount.get_attribute("value"))
        if total_amount.get_attribute("value") != None:
            return True
        else:
            return False

    def buyer_note_edit_status(self):
        result = self.check_if_element_is_editable(self.locators_dict["BUYER_NOTE"])
        return result

    def note_edit_status(self):
        result = self.check_if_element_is_editable(self.locators_dict["NOTES"])
        return result

    def save_button_working_status(self, notes):
        result = self.driver.find_element(By.XPATH, self.locators_dict["NOTES"][1])
        result.clear()
        self.do_send_keys(self.locators_dict["NOTES"], notes)
        self.do_click(self.locators_dict["SAVE"])
        time.sleep(10)
        result = self.driver.find_element(By.XPATH, self.locators_dict["NOTES"][1]).text
        return result

    def export_csv_button_working_status(self):
        self.do_click(self.locators_dict["EXPORT_CSV"])
        time.sleep(5)
        files = os.listdir("/Users/deepak/Desktop/Project/apollo3/iqe-ui-automation-apollo/ims-ui/downloads")
        csv_file = [f for f in files if f.endswith('.csv')]
        if csv_file:
            return True
        else:
            return False

    def export_excel_button_working_status(self):
        self.do_click(self.locators_dict["EXPORT_EXCEL"])
        time.sleep(5)
        files = os.listdir("/Users/deepak/Desktop/Project/apollo3/iqe-ui-automation-apollo/ims-ui/downloads")
        csv_file = [f for f in files if f.endswith('.xls') or f.endswith('.xlsx')]
        if csv_file:
            return True
        else:
            return False

    def export_xml_button_working_status(self):
        self.do_click(self.locators_dict["EXPORT_XML"])
        time.sleep(5)
        files = os.listdir("/Users/deepak/Desktop/Project/apollo3/iqe-ui-automation-apollo/ims-ui/downloads")
        csv_file = [f for f in files if f.endswith('.xml')]
        if csv_file:
            return True
        else:
            return False

    def vendor_name_default_status(self):
        vendor_name = self.driver.find_element(By.XPATH, self.locators_dict["VENDOR_NAME"][1])
        print("vendor name", vendor_name.get_attribute("value"))
        if vendor_name.get_attribute("value") != None:
            return True
        else:
            return False

    def ship_to_addr_disability_check(self):
        ship_to_dropdown = self.driver.find_element(By.CSS_SELECTOR, self.locators_dict["SHIP_TO_ADDR"][1])
        is_disabled = ship_to_dropdown.get_attribute("disabled") is not None
        return is_disabled

    def po_void_select_status(self):
        po_void_checkbox = self.driver.find_element(By.XPATH, self.locators_dict["PO_VOID"][1])
        if not po_void_checkbox.is_selected():
            self.do_click(self.locators_dict["PO_VOID"])
        if po_void_checkbox.is_selected():
            return True

    def po_void_unselect_status(self):
        po_void_checkbox = self.driver.find_element(By.XPATH, self.locators_dict["PO_VOID"][1])
        if po_void_checkbox.is_selected():
            self.do_click(self.locators_dict["PO_VOID"])
        if not po_void_checkbox.is_selected():
            return True

