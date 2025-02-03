from pages.login_page.login_page import LoginPage
import allure
from allure_commons.types import AttachmentType
from utilities.read_properties import ReadConfig


class TestDataVerificationToolPageHelper:
    def login_to_app(self, driver, username, password, return_object, url=ReadConfig.get_application_url()):
        self.loginPage = LoginPage(driver, url)
        self.dataverificationtool = self.loginPage.do_login(username, password, return_object)



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

    def open_data_verification_tool_page(self, path, environment):
        url = self.url_builder(path, environment)
        self.dataverificationtool.navigate_to_data_verification_tool_page(url)

    def run_address_test_button_display_check(self):
        status = self.dataverificationtool.capture_run_address_button_status()
        return status

    def run_location_test_button_display_check(self):
        status = self.dataverificationtool.capture_run_location_button_status()
        return status

    def run_pools_test_button_display_check(self):
        status = self.dataverificationtool.capture_run_pools_button_status()
        return status

    def run_power_test_button_display_check(self):
        status = self.dataverificationtool.capture_run_power_button_status()
        return status

    def run_checkin_test_button_display_check(self):
        status = self.dataverificationtool.capture_run_checkin_button_status()
        return status

    def run_scanin_test_button_display_check(self):
        status = self.dataverificationtool.capture_run_scanin_button_status()
        return status

    def verify_checkbox_option_for_datacenter_to_verify(self):
        options = self.dataverificationtool.get_the_options_for_datacenter_to_verify()
        return options

    def run_all_test_button_display_check(self):
        status = self.dataverificationtool.capture_run_all_button_status()
        return status

    def export_all_results_button_display_check(self):
        status = self.dataverificationtool.capture_export_all_results_button_status()
        return status
