
from pages.login_page.login_page import LoginPage
import allure
from allure_commons.types import AttachmentType
from utilities.read_properties import ReadConfig


class TestHardwareChaasisListPageHelper:
    def login_to_app(self, driver, username, password, return_object, url=ReadConfig.get_application_url()):
        self.loginPage = LoginPage(driver, url)
        self.hardwarechaasislist = self.loginPage.do_login(username, password, return_object)

    def open_hardware_component_search_page(self, path, environment):
        url = self.url_builder(path, environment)
        self.hardwarechaasislist.navigate_to_hardware_chaasis_list_page(url)

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

    def click_on_the_edit_link(self):
        self.hardwarechaasislist.go_into_the_edit_link()

    def click_on_add_an_attribute(self):
        self.hardwarechaasislist.select_add_an_attribute()

    def select_raid_card_capacity_and_set_the_value_to_2(self):
        status = self.hardwarechaasislist.set_raid_card_capacity_to_2()
        return status

    def select_the_chaasis(self, chassis):
        self.hardwarechaasislist.choose_chaasis(chassis)

    def return_the_riser_card_rows(self):
        row_count = self.hardwarechaasislist.get_the_riser_card_rows()
        return row_count

    def type_the_description(self, template_description):
        self.hardwarechaasislist.send_description(template_description)

    def make_other_selection_and_save_the_page(self, PO):
        self.hardwarechaasislist.select_dropdowns_and_save_the_page(PO)

