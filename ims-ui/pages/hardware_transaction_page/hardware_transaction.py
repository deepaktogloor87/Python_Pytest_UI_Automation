import requests

from pages.base_page import BasePage
from pages.hardware_transaction_page.hardware_transaction_locators import hardware_transaction_page_locators
from selenium.webdriver.common.by import By


class HardwareTransactionPage(BasePage):
    locators_dict = {name: locator for name, locator in hardware_transaction_page_locators}

    """constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_hardware_txn_page(self, url):
        self.driver.get(url)

    @staticmethod
    def link_works(url):
        try:
            request_response = requests.head(url, allow_redirects=True, timeout=10, verify=False)
            status_code = request_response.status_code
            return status_code == 200
        except requests.ConnectionError:
            return False

    def check_hardware_transaction_links_accessabilty(self):
        all_links_working = True
        link_list = []
        for i in range(1, 9):
            xpath_with_index = self.locators_dict["ALL_HD_TXN_LINKS"][1].replace('{i}', str(i))

            link_element = self.wait_until_element_is_visible(xpath_with_index)
            text_value = self.driver.find_element(By.XPATH, xpath_with_index).text
            link_list.append(text_value)
            href = link_element.get_attribute('href')

            if href and 'http' in href:
                # If either the link is not clickable or doesn't work, set the flag to False
                if not (self.is_clickable(link_element) and self.link_works(href)):
                    all_links_working = False
                    break  # Optional: stop checking after the first failure
            else:
                all_links_working = False
        return all_links_working

    def capture_no_of_links_from_page(self):
        no_of_link_elements = self.driver.find_elements(By.XPATH, self.locators_dict["TOTAL_LINKS"][1])
        return len(no_of_link_elements)
