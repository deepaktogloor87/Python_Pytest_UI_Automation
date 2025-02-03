from pages.login_page.login_page import LoginPage
import allure
from allure_commons.types import AttachmentType
from utilities.read_properties import ReadConfig


class TestHardwarePageHelper:
    def login_to_app(self, driver, username, password, return_object, url=ReadConfig.get_application_url()):
        self.loginPage = LoginPage(driver, url)
        self.hardware = self.loginPage.do_login(username, password, return_object)

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

    def open_hardware_page(self, path, environment):
        url = self.url_builder(path, environment)
        self.hardware.navigate_to_hardware_page(url)

    def check_if_links_response_code_is_200(self):
        is_clickable_and_workable = self.hardware.verify_and_get_hardware_links_availability_and_workability()
        self.log.info(f"Is all the links under hardware page are working? {is_clickable_and_workable}")
        return is_clickable_and_workable

    def check_if_links_response_code_is_200_under_hardware_heading(self):
        is_clickable_and_workable = self.hardware.verify_and_get_hardware_heading_links_availability_and_workability()
        self.log.info(f"Is all the links under hardware page are working? {is_clickable_and_workable}")
        return is_clickable_and_workable

    def check_total_no_of_links_under_find(self):
        total_links = self.hardware.get_the_total_no_of_links_under_find()
        return total_links

    def check_total_no_of_links_under_hardware(self):
        total_links = self.hardware.get_the_total_no_of_links_under_hardware()
        return total_links
