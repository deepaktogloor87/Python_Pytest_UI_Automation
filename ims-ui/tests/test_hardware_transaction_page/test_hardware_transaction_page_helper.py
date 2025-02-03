from pages.login_page.login_page import LoginPage
import allure
from allure_commons.types import AttachmentType
from utilities.read_properties import ReadConfig


class TestHardwareTransactionPagePageHelper:
    def login_to_app(self, driver, username, password, return_object, url=ReadConfig.get_application_url()):
        self.loginPage = LoginPage(driver, url)
        self.hardwaretxn = self.loginPage.do_login(username, password, return_object)

    def open_hardware_txn_page(self, path, environment):
        url = self.url_builder(path, environment)
        self.hardwaretxn.navigate_to_hardware_txn_page(url)

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

    def extract_the_links_from_the_page(self):
        is_accessible = self.hardwaretxn.check_hardware_transaction_links_accessabilty()
        self.log.info(f"Is all the links under hardware transaction page are working? {is_accessible}")
        return is_accessible

    def get_the_no_of_links_from_page(self):
        no_of_links = self.hardwaretxn.capture_no_of_links_from_page()
        return no_of_links
