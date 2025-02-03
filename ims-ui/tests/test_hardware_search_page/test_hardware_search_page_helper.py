from pages.login_page.login_page import LoginPage
import allure
from allure_commons.types import AttachmentType
from utilities.read_properties import ReadConfig


class TestHardwareSearchPageHelper:
    def login_to_app(self, driver, username, password, return_object, url=ReadConfig.get_application_url()):
        self.loginPage = LoginPage(driver, url)
        self.hardwaresearch = self.loginPage.do_login(username, password, return_object)

    def open_hardware_search_page(self, path, environment):
        url = self.url_builder(path, environment)
        self.hardwaresearch.navigate_to_hardware_search_page(url)

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

    def location_checkbox_status(self):
        location_details = self.hardwaresearch.get_the_details_of_location_checkbox()
        return location_details

    def hardware_function_checkbox_status(self):
        hardware_function_details = self.hardwaresearch.get_the_details_of_hardware_func_checkbox()
        return hardware_function_details

    def uim_managed_asset_checkbox_status(self):
        uim_managed_asset_details = self.hardwaresearch.get_the_details_of_uim_managed_asset_checkbox()
        return uim_managed_asset_details

    def tag_checkbox_status(self):
        tag_details = self.hardwaresearch.get_the_details_of_tag_checkbox()
        return tag_details

    def hardware_pool_checkbox_status(self):
        hardware_pool_details = self.hardwaresearch.get_the_details_of_hardware_pool_checkbox()
        return hardware_pool_details

    def pooled_servers_checkbox_status(self):
        pooled_servers_details = self.hardwaresearch.get_the_details_of_pooled_servers_checkbox()
        return pooled_servers_details

    def hardware_pool_status_checkbox_status(self):
        hardware_pool_status_details = self.hardwaresearch.get_the_details_of_hardware_pool_status_checkbox()
        return hardware_pool_status_details

    def generic_component_checkbox_status(self):
        generic_components_details = self.hardwaresearch.get_the_details_of_generic_components_checkbox()
        return generic_components_details

    def specific_component_checkbox_status(self):
        specific_components_details = self.hardwaresearch.get_the_details_of_specific_components_checkbox()
        return specific_components_details

    def chassis_checkbox_status(self):
        chassis_details = self.hardwaresearch.get_the_details_of_chassis_checkbox()
        return chassis_details

    def display_btn_status(self):
        display_btn_details = self.hardwaresearch.get_the_details_of_display_btn()
        return display_btn_details

    def export_csv_btn_status(self):
        export_csv_btn_details = self.hardwaresearch.get_the_details_of_export_csv_btn()
        return export_csv_btn_details

    def export_excel_btn_status(self):
        export_excel_btn_details = self.hardwaresearch.get_the_details_of_export_excel_btn()
        return export_excel_btn_details

    def export_origin_certificate_btn_status(self):
        export_origin_cert_btn_details = self.hardwaresearch.get_the_details_of_export_origin_cert_btn()
        return export_origin_cert_btn_details

    def save_and_share_search_query_url_btn_status(self):
        save_and_share_search_query_url_btn_details = self.hardwaresearch.get_the_details_of_save_and_share_search_query_url_btn()
        return save_and_share_search_query_url_btn_details

    def hardware_id_txt_field_status(self):
        hardware_id_txt_field_details = self.hardwaresearch.get_the_details_of_hardware_id_txt_box()
        return hardware_id_txt_field_details

    def virtual_host_id_txt_field_status(self):
        virtual_host_id_txt_field_details = self.hardwaresearch.get_the_details_of_virtual_host_id_txt_box()
        return virtual_host_id_txt_field_details

    def manufacture_serial_number_txt_field_status(self):
        manufacture_serial_number_field_details = self.hardwaresearch.get_the_details_of_manufacture_serial_number_txt_box()
        return manufacture_serial_number_field_details

    def softlayer_serial_number_txt_field_status(self):
        softlayer_serial_number_field_details = self.hardwaresearch.get_the_details_of_softlayer_serial_number_txt_box()
        return softlayer_serial_number_field_details

    def account_id_txt_field_status(self):
        account_id_field_details = self.hardwaresearch.get_the_details_of_account_id_txt_box()
        return account_id_field_details

    def chassis_scip_id_txt_field_status(self):
        chassis_scip_id_field_details = self.hardwaresearch.get_the_details_of_chassis_scip_id_txt_box()
        return chassis_scip_id_field_details

    def hardware_component_model_scip_id_txt_field_status(self):
        hardware_component_model_scip_id_field_details = self.hardwaresearch.get_the_details_of_hardware_component_model_scip_id_txt_box()
        return hardware_component_model_scip_id_field_details

    def mac_ipv4_ipv6_txt_field_status(self):
        mac_ipv4_ipv6_field_details = self.hardwaresearch.get_the_details_of_mac_ipv4_ipv6_txt_box()
        return mac_ipv4_ipv6_field_details

    def internal_notes_txt_field_status(self):
        internal_notes_field_details = self.hardwaresearch.get_the_details_of_internal_notes_txt_box()
        return internal_notes_field_details
