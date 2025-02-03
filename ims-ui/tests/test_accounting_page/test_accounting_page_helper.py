from pages.login_page.login_page import LoginPage
import allure
from allure_commons.types import AttachmentType
from utilities.read_properties import ReadConfig


class TestAccountingPageHelper:
    def login_to_app(self, driver, username, password, return_object, url=ReadConfig.get_application_url()):
        self.loginPage = LoginPage(driver, url)
        self.accounting = self.loginPage.do_login(username, password, return_object)

    def open_accounting_page(self, path, environment):
        url = self.url_builder(path, environment)
        self.accounting.navigate_to_accounting_page(url)

    def construct_url_with_branch_name(self, environment):
        base_url = ReadConfig.get_application_url()
        parts = base_url.split('.')
        parts[0] = 'https://' + environment
        modified_base_url = '.'.join(parts)
        return modified_base_url

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

    def check_if_links_are_clickable_and_working(self):
        is_clickable_and_workable = self.accounting.verify_links_clickability_and_workability()
        self.log.info(f"Is all the links under accounting page are working? {is_clickable_and_workable}")
        return is_clickable_and_workable

    @staticmethod
    def get_screenshot_on_error(driver, name):
        allure.attach(driver.get_screenshot_as_png(), name=name,
                      attachment_type=AttachmentType.PNG)

    def get_total_links_under_accounting_page(self):
        total_links = self.accounting.capture_links_under_accounting_page()
        return total_links
