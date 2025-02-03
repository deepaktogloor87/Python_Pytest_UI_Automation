from pages.login_page.login_page import LoginPage
import allure
from allure_commons.types import AttachmentType
from utilities.read_properties import ReadConfig


class TestCancelVirtualProcessInstanceHelper:
    def login_to_app(self, driver, username, password, return_object, url=ReadConfig.get_application_url()):
        self.loginPage = LoginPage(driver, url)
        self.cancelvirtualprocessinstace = self.loginPage.do_login(username, password, return_object)

    @staticmethod
    def construct_url_with_branch_name(environment):
        base_url = ReadConfig.get_application_url()
        parts = base_url.split('.')
        parts[0] = 'https://' + environment
        modified_base_url = '.'.join(parts)
        return modified_base_url

    def open_cancel_virtual_process_instance_page(self, path, environment):
        url = self.url_builder(path, environment)
        self.cancelvirtualprocessinstace.navigate_to_cancel_virtual_process_instance_page(url)

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

    def cancel_virtual_process_instance_link_presence(self):
        is_present = self.cancelvirtualprocessinstace.capture_link_presence()
        return is_present

    def build_url_and_open_cancel_virtual_process_instance_page(self, path, environment):
        url = self.url_builder(path, environment)
        self.cancelvirtualprocessinstace.navigate_to_cancel_virtual_process_instance_page(url)
        self.cancelvirtualprocessinstace.click_on_to_cancel_virtual_process_instance_link()

    def check_for_instructions_presence(self):
        presence_status = self.cancelvirtualprocessinstace.instructions_display_check()
        return presence_status

    def check_for_process_instance_info(self, process_instance):
        self.cancelvirtualprocessinstace.enter_the_process_instance_and_click_on_view_button(process_instance)
        ps_presence = self.cancelvirtualprocessinstace.process_instance_information_status()
        return ps_presence

    def check_for_error_msg_provinding_incorrect_ps(self, incorrect_ps):
        self.cancelvirtualprocessinstace.enter_the_process_instance_and_click_on_view_button(incorrect_ps)
        err_presence = self.cancelvirtualprocessinstace.error_msg_presence()
        return err_presence

    def get_the_cancel_button_status(self, ps_instance):
        self.cancelvirtualprocessinstace.enter_the_process_instance_and_click_on_view_button(ps_instance)
        is_present = self.cancelvirtualprocessinstace.capture_cancel_button_status()
        return is_present
