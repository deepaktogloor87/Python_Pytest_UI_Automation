from pages.login_page.login_page import LoginPage
import allure
from allure_commons.types import AttachmentType
from utilities.read_properties import ReadConfig


class TestVirtualUpdatePoolPageHelper:
    def login_to_app(self, driver, username, password, return_object, url=ReadConfig.get_application_url()):
        self.loginPage = LoginPage(driver, url)
        self.virtualupdatepool = self.loginPage.do_login(username, password, return_object)

    def open_update_pool_page(self, path, environment):
        url = self.url_builder(path, environment)
        self.virtualupdatepool.navigate_to_update_pool_page(url)

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

    def click_on_back_to_pool_list_link(self):
        self.virtualupdatepool.navigate_to_back_to_pool_page()
        self.log.info("Successfully opened back to pool list page")

    def extract_the_content_from_back_to_pool_list_page(self):
        captured_table_info = self.virtualupdatepool.capture_the_content_from_pool_list_table_header()
        self.log.info(f"Captured table header: {captured_table_info}")
        return captured_table_info

    def name_field_enabled_and_editable_check(self):
        name_editability = self.virtualupdatepool.check_if_name_field_is_enabled_and_editable()
        self.log.info(f"name field editability status: {name_editability}")
        return name_editability

    def description_field_enabled_and_editable_check(self):
        description_editability = self.virtualupdatepool.check_if_description_field_is_enabled_and_editable()
        self.log.info(f"name field editability status: {description_editability}")
        return description_editability

    def check_for_pool_master_table(self):
        table_visibility = self.virtualupdatepool.visibility_of_pool_master_table()
        self.log.info(f"Pool master table visibility: {table_visibility}")

    def check_for_hardware_availability_in_pool_master_table(self, hardware):
        hardware_visibility = self.virtualupdatepool.check_for_hardware_presence_in_pool_master_table(hardware)
        self.log.info(f"hardware display status in pool master table {hardware_visibility}")
        return hardware_visibility

    def check_whether_pool_button_is_displayed_and_clickable(self):
        is_displayed_and_clickable = self.virtualupdatepool.update_button_display_and_clickability_check()
        return is_displayed_and_clickable

    def host_reservation_editability_and_display_check(self):
        is_edit_display = self.virtualupdatepool.check_host_reservation_edit_display()
        return is_edit_display

    def pool_brand_tagname_check(self):
        is_dropdown = self.virtualupdatepool.pool_brand_dropdown_status()
        return is_dropdown

    def pool_brand_options_display_status(self):
        is_displayed = self.virtualupdatepool.pool_brand_options_check()
        return is_displayed

    def preferred_os_tagname_check(self):
        is_dropdown = self.virtualupdatepool.preferred_os_dropdown_status()
        return is_dropdown

    def reload_os_tagname_check(self):
        is_dropdown = self.virtualupdatepool.reload_os_dropdown_status()
        return is_dropdown

    def preferred_os_options_display_status(self):
        is_displayed = self.virtualupdatepool.preferred_os_options_check()
        return is_displayed

    def reload_os_options_display_status(self):
        is_displayed = self.virtualupdatepool.reload_os_options_check()
        return is_displayed

    def pool_type_dropdown_check(self):
        is_dropdown = self.virtualupdatepool.pool_type_dropdown_status()
        return is_dropdown

    def get_pool_type_dropdown_options(self):
        dropdown_options_list = self.virtualupdatepool.capture_pool_type_options()
        return dropdown_options_list

    def host_reservation_enable_and_editable_check(self):
        enabled_and_editable = self.virtualupdatepool.check_if_host_reservation_is_enabled_and_editable()
        return enabled_and_editable

    def transient_cpu_limit_enable_and_editable_check(self):
        enabled_and_editable = self.virtualupdatepool.check_if_transient_cpu_limit_is_enabled_and_editable()
        return enabled_and_editable

    def auto_migrate_pool_limit_enable_and_editable_check(self):
        enabled_and_editable = self.virtualupdatepool.check_if_auto_migrate_pool_limit_is_enabled_and_editable()
        return enabled_and_editable

    def use_host_with_preferred_os_input_type_and_enable_check(self):
        checkbox_and_enable_status = self.virtualupdatepool.use_host_with_preferred_os_status()
        return checkbox_and_enable_status

    def enable_host_after_reload_input_type_and_enable_check(self):
        checkbox_and_enable_status = self.virtualupdatepool.enable_hosts_after_reload_status()
        return checkbox_and_enable_status

    def vlan_provisions_allowed_input_type_and_enable_check(self):
        checkbox_and_enable_status = self.virtualupdatepool.vlan_provisions_allowed_status()
        return checkbox_and_enable_status

    def disable_host_auto_migration_input_type_and_enable_check(self):
        checkbox_and_enable_status = self.virtualupdatepool.disable_host_auto_migration_allowed_status()
        return checkbox_and_enable_status

    def verify_check_boxes_name_for_pool_roles(self):
        pool_roles_len = self.virtualupdatepool.get_the_no_of_checkboxes_for_pool_roles()
        return pool_roles_len
