from pages.login_page.login_page import LoginPage
import allure
from allure_commons.types import AttachmentType
from utilities.read_properties import ReadConfig


class TestServerPrebuildPageHelper:
    def login_to_app(self, driver, username, password, return_object, url=ReadConfig.get_application_url()):
        self.loginPage = LoginPage(driver, url)
        self.serverprebuild = self.loginPage.do_login(username, password, return_object)

    def open_server_prebuild_page(self, path, environment):
        url = self.url_builder(path, environment)
        self.serverprebuild.navigate_to_server_prebuild_page(url)

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

    def check_if_hardware_id_is_editable(self):
        editable_status = self.serverprebuild.get_editable_status_of_hardware_id()
        return editable_status

    def check_if_base_server_id_is_editable(self):
        editable_status = self.serverprebuild.get_editable_status_of_base_server_id()
        return editable_status

    def check_if_softlayer_ticket_id_is_editable(self):
        editable_status = self.serverprebuild.get_editable_status_of_softlayer_ticket_id()
        return editable_status

    def navigate_to_server_prebuild_job_tab(self):
        self.serverprebuild.click_on_server_prebuild_job_tab()

    def check_if_spj_base_server_id_is_editable(self):
        editable_status = self.serverprebuild.get_editable_status_of_spj_base_server_id()
        return editable_status

    def check_if_spj_softlayer_ticket_id_is_editable(self):
        editable_status = self.serverprebuild.get_editable_status_of_spj_softlayer_ticket_id()
        return editable_status

    def check_if_spj_prebuild_job_id_is_editable(self):
        editable_status = self.serverprebuild.get_editable_status_of_spj_prebuild_job_id()
        return editable_status

    def check_if_spj_user_id_is_editable(self):
        editable_status = self.serverprebuild.get_editable_status_of_spj_user_id()
        return editable_status

    def create_button_cpj_display_check(self):
        is_displayed_clickable = self.serverprebuild.get_details_of_create_button_cpj()
        return is_displayed_clickable

    def reset_button_cpj_display_check(self):
        is_displayed_clickable = self.serverprebuild.get_details_of_reset_button_cpj()
        return is_displayed_clickable

    def search_button_spj_display_check(self):
        is_displayed_clickable = self.serverprebuild.get_details_of_search_button_spj()
        return is_displayed_clickable

    def reset_button_spj_display_check(self):
        is_displayed_clickable = self.serverprebuild.get_details_of_reset_button_spj()
        return is_displayed_clickable

