import requests

from pages.base_page import BasePage
from pages.network_firewall_page.network_firewall_locators import network_firewall_page_locators
from selenium.webdriver.common.by import By


class NetworkFirewallPage(BasePage):
    locators_dict = {name: locator for name, locator in network_firewall_page_locators}

    """constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_network_firewall_page(self, url):
        self.driver.get(url)

    @staticmethod
    def link_works(url):
        try:
            request_response = requests.head(url, allow_redirects=True, timeout=10, verify=False)
            status_code = request_response.status_code
            return status_code == 200
        except requests.ConnectionError:
            return False

    def check_network_firewall_links_accessabilty(self):
        all_links_working = True
        for i in range(1, 14):
            xpath_with_index = self.locators_dict["ALL_NETWORK_FIREWALL_LINKS"][1].replace('{i}', str(i))
            element_text = self.driver.find_element(By.XPATH, xpath_with_index)
            # print("element", element_text.text)
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

    def get_the_total_no_of_links_under_the_nw_firewall_page(self):
        total_links = self.driver.find_elements(By.XPATH, self.locators_dict["TOTAL_LINKS"][1])
        return len(total_links)
    