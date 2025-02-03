from pages.base_page import BasePage
from pages.host_evacuation_type_page.host_evacuation_locators import host_evacuation_page_locators


class HostEvacuationPage(BasePage):
    locators_dict = {name: locator for name, locator in host_evacuation_page_locators}

    """constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)

    def check_create_ticket_checkbox_is_selected(self):
        if_checkbox_selected = self.check_if_checkbox_is_selected(self.locators_dict["CREATE_TICKET_CHECKBOX"])
        return if_checkbox_selected

    def open_ticket_page(self, url):
        self.driver.get(url)

    def capture_account_id(self):
        account_id = self.get_element_text(self.locators_dict["TICKET_ACCOUNT_ID"])
        return account_id

    def capture_company_details(self):
        company_details = self.get_element_text(self.locators_dict["TICKET_COMPANY_DETAILS"])
        return company_details

    def check_create_ticket_form_is_displayed(self):
        if_form_displayed = self.check_if_form_is_displayed(self.locators_dict["CREATE_TICKET_FORM"])
        return if_form_displayed

    def unselect_create_ticket_checkbox(self):
        self.do_click(self.locators_dict["CREATE_TICKET_CHECKBOX"])

    def verify_create_ticket_title_textbox_editibility(self):
        return self.check_if_form_is_editable(self.locators_dict["CREATE_TICKET_TITLE"])

    def verify_create_ticket_form_textbox_editibility(self):
        return self.check_if_form_is_editable(self.locators_dict["CREATE_TICKET_FORM"])

    def capture_group_info(self):
        group_info = self.get_element_text(self.locators_dict["TICKET_GROUP_INFO"])
        return group_info
