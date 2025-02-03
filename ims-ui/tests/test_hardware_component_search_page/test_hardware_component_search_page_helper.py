import time

from pages.login_page.login_page import LoginPage
import allure
from allure_commons.types import AttachmentType
from utilities.read_properties import ReadConfig


class TestHardwareComponentSearchPageHelper:
    def login_to_app(self, driver, username, password, return_object, url=ReadConfig.get_application_url()):
        self.loginPage = LoginPage(driver, url)
        self.hardwarecomponentsearch = self.loginPage.do_login(username, password, return_object)

    def open_hardware_component_search_page(self, path, environment):
        url = self.url_builder(path, environment)
        self.hardwarecomponentsearch.navigate_to_hardware_component_search_page(url)

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

    def enter_the_serial_number(self, serial_number):
        time.sleep(5)
        result = self.hardwarecomponentsearch.input_serial_number(serial_number)
        return result

    def enter_the_component_id(self, component_id):
        time.sleep(5)
        result = self.hardwarecomponentsearch.input_component_id(component_id)
        return result

    def enter_component_ids_with_newline(self, component_id1, component_id2):
        time.sleep(5)
        result = self.hardwarecomponentsearch.input_component_ids_newline(component_id1, component_id2)
        return result

    def enter_serial_numbers_with_newline(self, serial_number1, serial_number2):
        time.sleep(5)
        result = self.hardwarecomponentsearch.input_serial_number_newline(serial_number1, serial_number2)
        return result

    def enter_softlayer_serial_number(self, sl_serial_no):
        time.sleep(5)
        result = self.hardwarecomponentsearch.input_sl_serial_number(sl_serial_no)
        return result

    def enter_softlayer_serial_number_with_newline(self, sl_serial_1, sl_serial_2):
        time.sleep(5)
        result = self.hardwarecomponentsearch.input_sl_serial_numbers_with_newline(sl_serial_1, sl_serial_2)
        return result

    def enter_manufacturer_serial_number(self, manufacturer_sl_no):
        time.sleep(5)
        result = self.hardwarecomponentsearch.input_manufacturer_sl_number(manufacturer_sl_no)
        return result

    def enter_manufacturer_serial_number_with_newline(self, mf_sl_1, mf_sl_2):
        time.sleep(5)
        result = self.hardwarecomponentsearch.input_manufacturer_sl_number_with_newline(mf_sl_1, mf_sl_2)
        return result

    def enter_hardware_id(self, hw_id):
        time.sleep(5)
        result = self.hardwarecomponentsearch.input_hardware_id(hw_id)
        return result

    def enter_hardware_id_with_newline(self, hw_id1, hw_id2):
        time.sleep(5)
        result = self.hardwarecomponentsearch.input_hardware_id_with_newline(hw_id1, hw_id2)
        return result

    def select_multiple_component_status(self):
        time.sleep(5)
        result = self.hardwarecomponentsearch.choose_multiple_component_states()
        return result

    def enter_lot_number(self, lot_number):
        time.sleep(5)
        result = self.hardwarecomponentsearch.input_lot_number(lot_number)
        return result

    def select_multiple_hardware_status(self):
        time.sleep(5)
        result = self.hardwarecomponentsearch.choose_multiple_hardware_states()
        return result

    def enter_account_id(self, account_id):
        time.sleep(5)
        result = self.hardwarecomponentsearch.input_account_id(account_id)
        return result

    def enter_hostname(self, hostname, acc_id):
        time.sleep(5)
        result = self.hardwarecomponentsearch.input_hostname(hostname, acc_id)
        return result

    def enter_domain(self, domain, hostname, acc_id):
        time.sleep(5)
        result = self.hardwarecomponentsearch.input_domain(domain, hostname, acc_id)
        return result

    def select_function_dropdown(self, function_dropdown_element, domain, hostname, acc_id):
        time.sleep(5)
        result = self.hardwarecomponentsearch.choose_from_function_dropdown(function_dropdown_element, domain, hostname,
                                                                            acc_id)
        return result

    def select_chassis(self, chassis, function_dropdown_element, domain, hostname, acc_id):
        time.sleep(5)
        result = self.hardwarecomponentsearch.choose_from_chassis(chassis, function_dropdown_element, domain, hostname,
                                                                  acc_id)
        return result

    def enter_mac_ipv4_ipv6(self, mac_ipv4_ipv6, chassis, function_dropdown_element, domain, hostname, acc_id):
        time.sleep(5)
        result = self.hardwarecomponentsearch.input_mac_ipv4_ipv6(mac_ipv4_ipv6, chassis, function_dropdown_element,
                                                                  domain, hostname,
                                                                  acc_id)
        return result

    def download_csv_file(self):
        result = self.hardwarecomponentsearch.click_on_export_csv_button()
        return result

    def download_excel_file(self):
        result = self.hardwarecomponentsearch.click_on_export_excel_button()
        return result

    def click_on_send_and_share_button(self):
        result = self.hardwarecomponentsearch.click_query_button()
        return result

    def enter_account_id_details(self, acc_id):
        result = self.hardwarecomponentsearch.input_account_id_details(acc_id)
        return result

    def enter_hw_id_details(self, hw_id):
        result = self.hardwarecomponentsearch.input_hw_id_details(hw_id)
        return result

    def select_location_details(self, location, hw_id):
        result = self.hardwarecomponentsearch.input_location_details(location, hw_id)
        return result

    def check_if_id_link_working_status(self):
        result = self.hardwarecomponentsearch.id_link_status_check()
        return result
    
