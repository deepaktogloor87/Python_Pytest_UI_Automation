import time

from pages.login_page.login_page import LoginPage
import allure
from allure_commons.types import AttachmentType
from utilities.read_properties import ReadConfig


class TestRMAReadyHardwarePageHelper:
    def login_to_app(self, driver, username, password, return_object, url=ReadConfig.get_application_url()):
        self.loginPage = LoginPage(driver, url)
        self.rmahardwareready = self.loginPage.do_login(username, password, return_object)

    def open_rma_ready_hardware_page(self, path, environment):
        url = self.url_builder(path, environment)
        self.rmahardwareready.navigate_to_rma_ready_hardware_page(url)

    @staticmethod
    def url_builder(path, environment=None):
        if not environment:
            environment = "stable"

        base_url = ReadConfig.get_application_url()

        # Split the base URL into components
        parts = base_url.split('.')

        # Replace the environment part (assuming the environment is always the first subdomain)
        parts[0] = 'https://' + environment

        # Recreate the base_url with the new environment
        modified_base_url = '.'.join(parts)

        if not modified_base_url.endswith('/'):
            modified_base_url += '/'
        if path.startswith('/'):
            path = path[1:]
        if not path.endswith('/'):
            path += '/'

        full_url = modified_base_url + path

        return full_url

    @staticmethod
    def construct_url_with_branch_name(environment):
        base_url = ReadConfig.get_application_url()
        parts = base_url.split('.')
        parts[0] = 'https://' + environment
        modified_base_url = '.'.join(parts)
        return modified_base_url

    def serial_number_textbox_status(self):
        serial_number_details = self.rmahardwareready.get_the_details_of_serial_number_txt_box()
        return serial_number_details

    def location_dropbox_status(self):
        location_details = self.rmahardwareready.get_the_details_of_location_dropbox()
        return location_details

    def hardware_function_dropbox_status(self):
        hardware_function_details = self.rmahardwareready.get_the_details_of_hardware_function_dropbox()
        return hardware_function_details

    def rma_number_dropbox_status(self):
        rma_number_details = self.rmahardwareready.get_the_details_of_rma_number_dropbox()
        return rma_number_details

    def search_btn_status(self):
        search_btn_details = self.rmahardwareready.get_the_details_of_search_btn()
        return search_btn_details

    def assign_btn_status(self):
        assign_btn_details = self.rmahardwareready.get_the_details_of_assign_btn()
        return assign_btn_details

    def rma_ready_hardware_list_table_status(self):
        rma_ready_hardware_table_details = self.rmahardwareready.get_the_details_of_rma_ready_hardware_table_details()
        return rma_ready_hardware_table_details

    def pass_and_check_the_table_content(self):
        self.rmahardwareready.select_50_per_page_from_displaying_checkbox()
        time.sleep(10)
        rma_ready_hardware_table_details = self.rmahardwareready.get_the_details_of_rma_ready_hardware_table_details()
        return len(rma_ready_hardware_table_details)
    
