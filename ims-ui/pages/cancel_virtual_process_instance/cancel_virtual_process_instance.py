from pages.base_page import BasePage
from pages.cancel_virtual_process_instance.cancel_virtual_process_instance_locators import \
    cancel_virtual_process_instance_locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class CancelVirtualProcessInstancePage(BasePage):
    locators_dict = {name: locator for name, locator in cancel_virtual_process_instance_locators}

    """constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_cancel_virtual_process_instance_page(self, url):
        self.driver.get(url)

    def capture_link_presence(self):
        is_present = self.check_element_presence(self.locators_dict["CANCEL_VIRTUAL_PROCESS_INSTANCE"][1])
        return is_present

    def click_on_to_cancel_virtual_process_instance_link(self):
        self.do_click(self.locators_dict["CANCEL_VIRTUAL_PROCESS_INSTANCE"])

    def instructions_display_check(self):
        is_present = self.check_element_presence(self.locators_dict["INSTRUCTIONS"][1])
        return is_present

    def enter_the_process_instance_and_click_on_view_button(self, process_instance):
        ps_txt_box = self.driver.find_element(By.XPATH, self.locators_dict["PROCESS_INSTANCE_TEXT_BOX"][1])
        ps_txt_box.send_keys(process_instance)
        self.do_click(self.locators_dict["PROCESS_INSTANCE_VIEW_BUTTON"])

    def process_instance_information_status(self):
        ps_presence = self.check_element_presence(self.locators_dict["PROCESS_INSTANCE_INFORMATION"][1])
        return ps_presence

    def error_msg_presence(self):
        err_presence = self.check_element_presence(self.locators_dict["ERROR_MSG"][1])
        return err_presence

    def capture_cancel_button_status(self):
        is_present = self.check_if_element_is_displayed(self.locators_dict["CANCEL_BTN"])
        return is_present
