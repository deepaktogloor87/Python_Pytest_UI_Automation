from pages.login_page.login_page import LoginPage
import allure
from allure_commons.types import AttachmentType
from utilities.read_properties import ReadConfig


class TestHostEvacuationTypePageHelper:
    def login_to_app(self, driver, username, password, return_object, url=ReadConfig.get_application_url()):
        self.loginPage = LoginPage(driver, url)
        self.hostevacuation = self.loginPage.do_login(username, password, return_object)

    def is_create_tickets_to_notify_customers_checkbox_selected(self):
        return self.hostevacuation.check_create_ticket_checkbox_is_selected()

    def is_create_ticket_form_is_displayed(self):
        return self.hostevacuation.check_create_ticket_form_is_displayed()

    def uncheck_create_ticket_to_notify_customer_checkbox(self):
        self.hostevacuation.unselect_create_ticket_checkbox()

    def check_create_tickets_title_text_box_is_editable(self):
        return self.hostevacuation.verify_create_ticket_title_textbox_editibility()

    def check_create_tickets_form_text_box_is_editable(self):
        return self.hostevacuation.verify_create_ticket_form_textbox_editibility()

    @staticmethod
    def get_screenshot_on_error(driver, name):
        allure.attach(driver.get_screenshot_as_png(), name=name,
                      attachment_type=AttachmentType.PNG)

    def open_host_evacuation_ticket_page(self, path, host_id, environment):
        url = self.url_builder(path, host_id, environment)
        self.hostevacuation.open_ticket_page(url)

    def get_host_evacuation_ticket_page_account_id(self):
        account_id = self.hostevacuation.capture_account_id()
        return account_id

    def get_host_evacuation_ticket_page_company_details(self):
        company_details = self.hostevacuation.capture_company_details()
        return company_details

    def get_host_evacuation_ticket_page_group_field_info(self):
        group_info = self.hostevacuation.capture_group_info()
        return group_info

    def url_builder(self, path, host_id, environment=None):
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

        full_url = modified_base_url + path + str(host_id)

        return full_url

    def construct_url_with_branch_name(self, environment):
        base_url = ReadConfig.get_application_url()
        parts = base_url.split('.')
        parts[0] = 'https://' + environment
        modified_base_url = '.'.join(parts)
        return modified_base_url
