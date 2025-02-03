from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

"""This is the parent of all pages"""
"""It contains all the generic methods and utilities for all the pages"""


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator)).send_keys(text)

    def press_enter(self, by_locator):
        WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator)).send_keys(Keys.ENTER)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
        return element.text

    def clear_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
        element.clear()

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(ec.title_is(title))
        return self.driver.title

    def check_if_element_is_editable(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
        is_editable = element.is_enabled() and not element.get_attribute('readonly')
        return is_editable

    def check_if_element_is_displayed(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
        return element.is_displayed()

    def check_element_presence(self, by_locator):
        presence = WebDriverWait(self.driver, 10).until(
            ec.presence_of_element_located((By.XPATH, by_locator))
        )

        return presence

    def wait_until_element_is_visible(self, by_locator):
        wait = WebDriverWait(self.driver, 10)
        element_presence = wait.until(ec.presence_of_element_located((By.XPATH, by_locator)))
        return element_presence

    def is_clickable(self, element):
        return element.is_displayed() and element.is_enabled()

    def check_if_form_is_displayed(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
        return element.is_displayed()

    def check_if_checkbox_is_selected(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
        return element.is_selected()

    def check_if_form_is_editable(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator))
        is_editable = element.is_enabled() and not element.get_attribute('readonly')
        return is_editable

    def check_if_element_is_clickable(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(by_locator))
        return element

    def wait_for_new_window_to_open(self):
        WebDriverWait(self.driver, 20).until(ec.number_of_windows_to_be(2))
        
