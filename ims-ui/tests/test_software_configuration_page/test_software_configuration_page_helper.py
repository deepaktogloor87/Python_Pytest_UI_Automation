import time

from pages.login_page.login_page import LoginPage
import allure
from allure_commons.types import AttachmentType
from utilities.read_properties import ReadConfig


class TestSoftwareConfigurationPageHelper:
    def login_to_app(self, driver, username, password, return_object, url=ReadConfig.get_application_url()):
        self.loginPage = LoginPage(driver, url)
        self.softwareconfiguration = self.loginPage.do_login(username, password, return_object)

    def open_hardware_lease_page(self, path, environment):
        url = self.url_builder(path, environment)
        self.softwareconfiguration.navigate_to_software_configuration_page(url)

    def url_builder(self, path, environment=None):
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

    def construct_url_with_branch_name(self, environment):
        base_url = ReadConfig.get_application_url()
        parts = base_url.split('.')
        parts[0] = 'https://' + environment
        modified_base_url = '.'.join(parts)
        return modified_base_url

    def select_a_template(self):
        self.softwareconfiguration.choose_a_template()

    def select_a_section(self):
        self.softwareconfiguration.choose_a_section()

    def select_an_available_fragment(self):
        self.softwareconfiguration.choose_an_avaliable_fragment()

    def check_if_fragment_is_assigned_to_assigned_fragment_list(self):
        result = self.softwareconfiguration.get_text()
        return result


    def click_on_assigned_fragment_btn(self):
        self.softwareconfiguration.select_assigned_fragment_btn()