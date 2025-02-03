import requests

from pages.base_page import BasePage
from pages.hardware_page.hardware_locators import hardware_page_locators
from selenium.webdriver.common.by import By


class HardwarePage(BasePage):
    locators_dict = {name: locator for name, locator in hardware_page_locators}

    """constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_hardware_page(self, url):
        self.driver.get(url)

    @staticmethod
    def link_works(url):
        try:
            request_response = requests.head(url, allow_redirects=True, timeout=10, verify=False)
            status_code = request_response.status_code
            return status_code == 200
        except requests.ConnectionError:
            return False

    def verify_and_get_hardware_links_availability_and_workability(self):

        all_links_working = True
        for i in range(1, 9):
            xpath_with_index = self.locators_dict["LINKS_UNDER_HARDWARE"][1].replace('{i}', str(i))

            link_element = self.wait_until_element_is_visible(xpath_with_index)
            href = link_element.get_attribute('href')

            if href and 'http' in href:
                # If either the link is not clickable or doesn't work, set the flag to False
                if not (self.is_clickable(link_element) and self.link_works(href)):
                    all_links_working = False
                    break  # Optional: stop checking after the first failure
            else:
                all_links_working = False
        return all_links_working

    def verify_and_get_hardware_heading_links_availability_and_workability(self):

        all_links_working = True
        for i in range(1, 26):
            xpath_with_index = self.locators_dict["LINKS_UNDER_HARDWARE"][1].replace('{i}', str(i))

            link_element = self.wait_until_element_is_visible(xpath_with_index)
            href = link_element.get_attribute('href')

            if href and 'http' in href:
                # If either the link is not clickable or doesn't work, set the flag to False
                if not (self.is_clickable(link_element) and self.link_works(href)):
                    all_links_working = False
                    break  # Optional: stop checking after the first failure
            else:
                all_links_working = False
        return all_links_working

    def get_the_total_no_of_links_under_find(self):
        total_links = self.driver.find_elements(By.XPATH, self.locators_dict["TOTAL_LINKS_FIND"][1])
        return len(total_links)

    def get_the_total_no_of_links_under_hardware(self):
        total_links = self.driver.find_elements(By.XPATH, self.locators_dict["TOTAL_LINKS_HARDWARE"][1])
        return len(total_links)
