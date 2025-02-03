from pages.login_page.login_page import LoginPage
import allure
from allure_commons.types import AttachmentType
from utilities.read_properties import ReadConfig


class TestServiceInventoryReportPageHelper:
    def login_to_app(self, driver, username, password, return_object, url=ReadConfig.get_application_url()):
        self.loginPage = LoginPage(driver, url)
        self.serviceinventorypage = self.loginPage.do_login(username, password, return_object)

    def open_service_inventory_report_page(self, path, environment):
        url = self.url_builder(path, environment)
        self.serviceinventorypage.navigate_to_service_inventory_report_page(url)

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

    def account_id_field_check(self):
        account_id_editable = self.serviceinventorypage.get_the_details_of_account_id()
        return account_id_editable

    def company_name_field_check(self):
        is_editable = self.serviceinventorypage.get_the_details_of_company_name()
        return is_editable

    def hostname_field_check(self):
        is_editable = self.serviceinventorypage.get_the_details_of_hostname()
        return is_editable

    def ip_address_field_check(self):
        is_editable = self.serviceinventorypage.get_the_details_of_ip_address()
        return is_editable

    def evault_username_field_check(self):
        is_editable = self.serviceinventorypage.get_the_details_of_evault_username()
        return is_editable

    def company_name_len_check(self):
        all_options_list =  self.serviceinventorypage.get_the_details_of_company_name_checkbox()
        return all_options_list

    def hostname_len_check(self):
        all_options_list = self.serviceinventorypage.get_the_details_of_hostname_checkbox()
        return all_options_list

    def ip_addr_len_check(self):
        all_options_list = self.serviceinventorypage.get_the_details_of_ip_addr_checkbox()
        return all_options_list

    def evault_username_len_check(self):
        all_options_list = self.serviceinventorypage.get_the_details_of_evault_username_checkbox()
        return all_options_list

    def show_with_evault_len_check(self):
        all_options_list = self.serviceinventorypage.get_the_details_of_show_with_evault_checkbox()
        return all_options_list

    def object_type_len_check(self):
        all_options_list = self.serviceinventorypage.get_the_details_of_object_type_checkbox()
        return all_options_list

    def object_status_len_check(self):
        all_options_list = self.serviceinventorypage.get_the_details_of_object_status_checkbox()
        return all_options_list

    def managed_server_len_check(self):
        all_options_list = self.serviceinventorypage.get_the_details_of_managed_server_checkbox()
        return all_options_list

    def search_btn_status_check(self):
        display_status = self.serviceinventorypage.get_the_details_of_search_button()
        return display_status
    
