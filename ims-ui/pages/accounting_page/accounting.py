import requests
from pages.base_page import BasePage
from pages.accounting_page.accounting_locators import accounting_page_locators
from selenium.webdriver.common.by import By


class AccountingPage(BasePage):
    locators_dict = {name: locator for name, locator in accounting_page_locators}

    """constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_accounting_page(self, url):
        self.driver.get(url)

    def link_works(self, url):
        try:
            request_response = requests.head(url, allow_redirects=True, timeout= 10, verify=False)
            status_code = request_response.status_code
            return status_code == 200
        except requests.ConnectionError:
            return False

    def verify_links_clickability_and_workability(self):

        all_links_working = True
        for i in range(1,31):
            xpath_with_index = self.locators_dict["ALL_ACCOUNTING_LINKS"][1].replace('{i}', str(i))
            locator = (self.locators_dict["ALL_ACCOUNTING_LINKS"][0], xpath_with_index)

            link_element = self.wait_until_element_is_visible(xpath_with_index)
            href = link_element.get_attribute('href')

            if href and 'http' in href:
                # If either the link is not clickable or doesn't work, set the flag to False
                if not (self.is_clickable(link_element) and self.link_works(href)):
                    all_links_working = False
                    # break  # Optional: stop checking after the first failure
            else:
                # If the href is not valid, set the flag to False
                all_links_working = False
                # break  # Optional: stop checking after the first failure

        return all_links_working

    def capture_links_under_accounting_page(self):
        accounting_tab = self.driver.find_elements(By.XPATH, self.locators_dict["TOTAL_LINKS"][1])
        no_of_links_under_accounting_page = len(accounting_tab)
        return str(no_of_links_under_accounting_page)