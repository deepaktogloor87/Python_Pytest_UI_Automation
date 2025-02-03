import time

from pages.login_page.login_page import LoginPage
import allure
from allure_commons.types import AttachmentType
from utilities.read_properties import ReadConfig


class TestHardwareLeasePageHelper:
    def login_to_app(self, driver, username, password, return_object, url=ReadConfig.get_application_url()):
        self.loginPage = LoginPage(driver, url)
        self.hardwarelease = self.loginPage.do_login(username, password, return_object)

    def open_hardware_lease_page(self, path, environment):
        url = self.url_builder(path, environment)
        self.hardwarelease.navigate_to_hardware_lease_page(url)

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

    def check_if_department_dropdown_is_clickable(self, department, department_value):
        result = self.hardwarelease.verify_department_dropdown_accessibility(department, department_value)
        return result

    def check_ship_to_address_default_value(self):
        result = self.hardwarelease.inspect_ship_to_add_value()
        return result

    def get_maxlength_lead_time(self, ):
        return self.hardwarelease.get_lead_time_length()

    def input_into_lead_time(self, value):
        result = self.hardwarelease.insert_lead_time(value)
        return result

    def get_status_field_value(self):
        result = self.hardwarelease.extract_status_value()
        return result

    def check_if_total_amount_has_default_value(self):
        result = self.hardwarelease.total_amount_status_check()
        return result

    def check_if_buyer_note_is_editable(self):
        result = self.hardwarelease.buyer_note_edit_status()
        return result

    def check_if_note_is_editable(self):
        result = self.hardwarelease.note_edit_status()
        return result

    def check_if_save_button_is_working(self, notes):
        result = self.hardwarelease.save_button_working_status(notes)
        return result

    def check_if_export_csv_button_is_working(self):
        result = self.hardwarelease.export_csv_button_working_status()
        return result

    def check_if_export_excel_button_is_working(self):
        result = self.hardwarelease.export_excel_button_working_status()
        return result

    def check_if_export_xml_button_is_working(self):
        result = self.hardwarelease.export_xml_button_working_status()
        return result

    def check_if_vendor_name_have_default_value(self):
        result = self.hardwarelease.vendor_name_default_status()
        return result

    def check_if_ship_to_address_disabled(self):
        result = self.hardwarelease.ship_to_addr_disability_check()
        return result

    def check_if_po_void_can_be_selected(self):
        result = self.hardwarelease.po_void_select_status()
        return result

    def check_if_po_void_can_be_unselected(self):
        result = self.hardwarelease.po_void_unselect_status()
        return result

