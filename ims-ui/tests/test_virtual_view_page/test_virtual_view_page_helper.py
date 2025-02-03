from pages.login_page.login_page import LoginPage
import allure
from allure_commons.types import AttachmentType
from utilities.read_properties import ReadConfig


class TestVirtualViewPageHelper:
    def login_to_app(self, driver, username, password, return_object, url=ReadConfig.get_application_url()):
        self.loginPage = LoginPage(driver, url)
        self.virtualviewpage = self.loginPage.do_login(username, password, return_object)

    def open_virtual_view_page(self, path, environment):
        url = self.url_builder(path, environment)
        self.virtualviewpage.navigate_to_virtual_view_page(url)

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

    def check_if_click_to_view_password_link_present(self):
        return self.virtualviewpage.check_for_password_link()
