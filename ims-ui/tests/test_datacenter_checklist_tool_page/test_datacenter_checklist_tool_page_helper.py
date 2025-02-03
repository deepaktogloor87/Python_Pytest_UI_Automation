from pages.login_page.login_page import LoginPage
import allure
from allure_commons.types import AttachmentType
from utilities.read_properties import ReadConfig


class TestDatacenterChecklistToolPageHelper:
    def login_to_app(self, driver, username, password, return_object, url=ReadConfig.get_application_url()):
        self.loginPage = LoginPage(driver, url)
        self.datacenterchecklist = self.loginPage.do_login(username, password, return_object)

    @staticmethod
    def construct_url_with_branch_name(environment):
        base_url = ReadConfig.get_application_url()
        parts = base_url.split('.')
        parts[0] = 'https://' + environment
        modified_base_url = '.'.join(parts)
        return modified_base_url

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

    def open_datacenter_checklist_page(self, path, environment):
        url = self.url_builder(path, environment)
        self.datacenterchecklist.navigate_to_datacenter_checklist_page(url)

    def start_button_display_status(self):
        self.datacenterchecklist.click_on_start_new_datacenter_verification_arrow()
        is_displayed_clickable = self.datacenterchecklist.get_start_button_status()
        return is_displayed_clickable

    def datacenter_dropdown_status(self):
        self.datacenterchecklist.click_on_start_new_datacenter_verification_arrow()
        datacenter_options = self.datacenterchecklist.get_the_dropdown_status()
        return datacenter_options

    def datacenter_heading_check(self):
        datacenter_headings = self.datacenterchecklist.get_datacenter_checklist_headings()
        return datacenter_headings

    def datacenter_rows_check(self):
        datacenter_rows = self.datacenterchecklist.get_datacenter_checklist_rows()
        return datacenter_rows

    def legend_table_instructions_display_check(self):
        legend_table_display = self.datacenterchecklist.get_the_legend_table_accessibility()
        return legend_table_display
