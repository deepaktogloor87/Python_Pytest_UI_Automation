from pages.base_page import BasePage
from pages.reports_page.reports_locators import reports_page_locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import requests


class ReportsPage(BasePage):
    locators_dict = {name: locator for name, locator in reports_page_locators}

    """constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_reports_page(self, url):
        self.driver.get(url)

    def click_on_accounting_tab(self):
        self.do_click(self.locators_dict["ACCOUNTING_TAB"])

    def click_on_sales_tab(self):
        self.do_click(self.locators_dict["SALES_TAB"])

    def click_on_datacenter_tab(self):
        self.do_click(self.locators_dict["DATACENTER_TAB"])

    def click_on_tickets_tab(self):
        self.do_click(self.locators_dict["TICKETS_TAB"])

    def click_on_misc_tab(self):
        self.do_click(self.locators_dict["MISC_TAB"])

    @staticmethod
    def link_works(url):
        try:
            request_response = requests.head(url, allow_redirects=True, timeout=10, verify=False)
            status_code = request_response.status_code
            return status_code == 200
        except requests.ConnectionError:
            return False

    def get_accounting_links_status(self):
        all_links_working = True
        for i in range(1, 15):
            xpath_with_index = self.locators_dict["ACCOUNTING_LINK"][1].replace('{i}', str(i))
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

    def get_sales_links_status(self):
        all_links_working = True
        for i in range(1,8):
            xpath_with_index = self.locators_dict["SALES_LINK"][1].replace('{i}', str(i))
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

    def get_datacenter_links_status(self):
        all_links_working = True
        for i in range(1,2):
            xpath_with_index = self.locators_dict["DATACENTER_LINK"][1].replace('{i}', str(i))
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

    def get_tickets_links_status(self):
        all_links_working = True
        for i in range(1,9):
            xpath_with_index = self.locators_dict["TICKETS_LINK"][1].replace('{i}', str(i))
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

    def get_misc_links_status(self):
        all_links_working = True
        for i in range(1,20):
            xpath_with_index = self.locators_dict["MISC_LINK"][1].replace('{i}', str(i))
            element_text = self.driver.find_element(By.XPATH, xpath_with_index)
            print("element", element_text.text)
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

    def get_the_total_no_of_links_under_accounting_tab(self):
        total_links = self.driver.find_elements(By.XPATH, self.locators_dict["ALL_ACCOUNTING_LINK"][1])
        return len(total_links)

    def get_the_total_no_of_links_under_sales_tab(self):
        total_links = self.driver.find_elements(By.XPATH, self.locators_dict["ALL_SALES_LINK"][1])
        return len(total_links)
    
    def get_the_total_no_of_links_under_datacenter_tab(self):
        total_links = self.driver.find_elements(By.XPATH, self.locators_dict["ALL_DATACENTER_LINK"][1])
        return len(total_links)

    def get_the_total_no_of_links_under_tickets_tab(self):
        total_links = self.driver.find_elements(By.XPATH, self.locators_dict["ALL_TICKETS_LINK"][1])
        return len(total_links)

    def get_the_total_no_of_links_under_misc_tab(self):
        total_links = self.driver.find_elements(By.XPATH, self.locators_dict["ALL_MISC_LINK"][1])
        return len(total_links)

