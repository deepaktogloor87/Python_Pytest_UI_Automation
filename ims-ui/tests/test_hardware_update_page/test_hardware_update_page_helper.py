from _curses_panel import panel

from pages.login_page.login_page import LoginPage
import allure
from allure_commons.types import AttachmentType
from utilities.read_properties import ReadConfig


class TestHardwareUpdatePageHelper:
    def login_to_app(self, driver, username, password, return_object, url=ReadConfig.get_application_url()):
        self.loginPage = LoginPage(driver, url)
        self.hardwareupdate = self.loginPage.do_login(username, password, return_object)

    # def open_hardware_update_page(self, path, environment):
    #     url = self.url_builder(path, environment)
    #     self.hardwareupdate.navigate_to_hardware_update_page(url)

    def open_hardware_update_page(self, path, hardware_id, environment):
        url = self.url_builder(path, hardware_id, environment)
        self.hardwareupdate.navigate_to_hardware_update_page(url)

    def url_builder(self, path, hardware_id, environment=None):
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

        full_url = modified_base_url + path + str(hardware_id)

        return full_url

    def construct_url_with_branch_name(self, environment):
        base_url = ReadConfig.get_application_url()
        parts = base_url.split('.')
        parts[0] = 'https://' + environment
        modified_base_url = '.'.join(parts)
        return modified_base_url

    def check_if_ssn_is_displayed(self):
        self.hardwareupdate.choose_properties_from_checkbox()
        display_status = self.hardwareupdate.ssn_display_status()
        return display_status

    def check_if_ssn_is_editable(self):
        editable_status = self.hardwareupdate.ssn_editable_status()
        return editable_status

    def check_if_wwn_is_displayed(self):
        self.hardwareupdate.choose_properties_from_checkbox()
        display_status = self.hardwareupdate.wwn_display_status()
        return display_status

    def check_if_wwn_is_editable(self):
        editable_status = self.hardwareupdate.wwn_editable_status()
        return editable_status

    def write_maintenance_notes(self, maintenance_notes):
        self.log.info("clicking on maintenance link")
        self.hardwareupdate.click_maintenance_link()
        self.log.info("clicking on other checkbox")
        self.hardwareupdate.click_on_others_checkbox()
        self.log.info("write the maintenance notes")
        self.hardwareupdate.post_maintenance_notes(maintenance_notes)
        self.log.info("clicking continue button")
        self.hardwareupdate.click_on_continue_btn()

    def check_if_maintenance_notes_present(self):
        self.log.info("Checking for the availability of the maintenance notes")
        return self.hardwareupdate.maintenance_notes_visibility()

    def check_presence_of_remote_management_link(self):
        result = self.hardwareupdate.get_remote_management_control_link_presence()
        return result

    def click_on_remote_management_link(self):
        self.hardwareupdate.open_remote_management_control_link()

    def check_if_2_tabs_are_present(self):
        tab_1 = self.hardwareupdate.get_ipmi_remote_management_summary_presence()
        tab_2 = self.hardwareupdate.get_redfish_remote_management_summary_presence()
        if tab_1 and tab_2:
            return True

    def click_on_redfish_remote_management_summary(self):
        self.hardwareupdate.remote_mgmt_summary_click()

    def select_power_off_option_from_dropdown(self):
        result = self.hardwareupdate.power_down_redfish()
        return result

    def select_power_on_option_from_dropdown(self):
        result = self.hardwareupdate.power_on_redfish()
        return result

    def select_yes_vpcng_option_from_uim_managed_asset_dropdown(self):
        self.hardwareupdate.choose_yes_vpcng_from_dropdown()

    def check_if_changes_are_saved_successfully(self):
        self.hardwareupdate.click_on_general_tab_continue_btn()
        uim_managed_asset_value = self.hardwareupdate.get_the_uim_managed_asset_dropdown_value()
        return uim_managed_asset_value

    def select_undercloud_option_from_uim_managed_asset_dropdown(self):
        self.hardwareupdate.choose_undercloud_from_dropdown()

    def select_fedramp_option_from_uim_managed_asset_dropdown(self):
        self.hardwareupdate.choose_fedramp_from_dropdown()

    def select_no_option_from_uim_managed_asset_dropdown(self):
        self.hardwareupdate.choose_no_from_dropdown()
