from pages.base_page import BasePage
from pages.data_verification_tool_page.data_verification_tool_locator import data_verification_tool_page_locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class DataVerificationToolPage(BasePage):
    locators_dict = {name: locator for name, locator in data_verification_tool_page_locators}

    """constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_data_verification_tool_page(self, url):
        self.driver.get(url)

    def capture_run_address_button_status(self):
        is_displayed = self.check_if_element_is_displayed(self.locators_dict["RUN_ADDRESS_TEST_BUTTON"])
        return is_displayed

    def capture_run_location_button_status(self):
        is_displayed = self.check_if_element_is_displayed(self.locators_dict["RUN_LOCATION_TEST_BUTTON"])
        return is_displayed

    def capture_run_pools_button_status(self):
        is_displayed = self.check_if_element_is_displayed(self.locators_dict["RUN_POOLS_TEST_BUTTON"])
        return is_displayed

    def capture_run_power_button_status(self):
        is_displayed = self.check_if_element_is_displayed(self.locators_dict["RUN_POWER_TEST_BUTTON"])
        return is_displayed

    def capture_run_checkin_button_status(self):
        is_displayed = self.check_if_element_is_displayed(self.locators_dict["RUN_CHECKIN_TEST_BUTTON"])
        return is_displayed

    def capture_run_scanin_button_status(self):
        is_displayed = self.check_if_element_is_displayed(self.locators_dict["RUN_CHECKIN_TEST_BUTTON"])
        return is_displayed

    def get_the_options_for_datacenter_to_verify(self):
        dropdown = self.driver.find_element(By.XPATH, self.locators_dict["DATACENTER_TO_VERIFY"][1])
        select = Select(dropdown)
        options = select.options
        checkboxes = [option.text.strip() for option in options]
        return checkboxes

    def capture_run_all_button_status(self):
        is_displayed = self.check_if_element_is_displayed(self.locators_dict["RUN_ALL_TESTS"])
        return is_displayed

    def capture_export_all_results_button_status(self):
        is_displayed = self.check_if_element_is_displayed(self.locators_dict["EXPORT_TEST_RESULTS"])
        return is_displayed
