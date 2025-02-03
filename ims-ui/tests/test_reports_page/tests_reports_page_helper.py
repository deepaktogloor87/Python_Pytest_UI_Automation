from pages.login_page.login_page import LoginPage
import allure
from allure_commons.types import AttachmentType
from utilities.read_properties import ReadConfig


class TestReportsPagePageHelper:
    def login_to_app(self, driver, username, password, return_object, url=ReadConfig.get_application_url()):
        self.loginPage = LoginPage(driver, url)
        self.reports  = self.loginPage.do_login(username, password, return_object)

    def open_reports_page(self, path, environment):
        url = self.url_builder(path, environment)
        self.reports.navigate_to_reports_page(url)

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

    def check_if_accounting_links_response_code_is_200(self):
        self.reports.click_on_accounting_tab()
        is_working = self.reports.get_accounting_links_status()
        return is_working

    def check_if_sales_links_response_code_is_200(self):
        self.reports.click_on_sales_tab()
        is_working = self.reports.get_sales_links_status()
        return is_working

    def check_if_datacenter_links_response_code_is_200(self):
        self.reports.click_on_datacenter_tab()
        is_working = self.reports.get_datacenter_links_status()
        return is_working

    def check_if_tickets_links_response_code_is_200(self):
        self.reports.click_on_tickets_tab()
        is_working = self.reports.get_tickets_links_status()
        return is_working

    def check_if_misc_links_response_code_is_200(self):
        self.reports.click_on_misc_tab()
        is_working = self.reports.get_misc_links_status()
        return is_working

    def check_total_no_of_links_under_accounting_tab(self):
        total_links = self.reports.get_the_total_no_of_links_under_accounting_tab()
        return total_links

    def check_total_no_of_links_under_sales_tab(self):
        self.reports.click_on_sales_tab()
        total_links = self.reports.get_the_total_no_of_links_under_sales_tab()
        return total_links

    def check_total_no_of_links_under_datacenter_tab(self):
        self.reports.click_on_datacenter_tab()
        total_links = self.reports.get_the_total_no_of_links_under_datacenter_tab()
        return total_links

    def check_total_no_of_links_under_tickets_tab(self):
        self.reports.click_on_tickets_tab()
        total_links = self.reports.get_the_total_no_of_links_under_tickets_tab()
        return total_links

    def check_total_no_of_links_under_misc_tab(self):
        self.reports.click_on_misc_tab()
        total_links = self.reports.get_the_total_no_of_links_under_misc_tab()
        return total_links

