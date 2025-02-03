import pytest
from selenium.common import TimeoutException
from tests.test_host_evacuation_type_page.test_host_evacuation_type_helper import TestHostEvacuationTypePageHelper
from tests.test_base import BaseTest
from utilities.read_json import read_and_parse_json
from utilities.read_properties import ReadConfig


class TestHostEvacuationTypePage(BaseTest, TestHostEvacuationTypePageHelper):
    base_url = ReadConfig.get_application_url()
    username = ReadConfig.get_application_username()
    password = ReadConfig.get_application_password()

    @pytest.fixture(scope="function")
    def setup(self, logger):
        self.log = logger
        self.log.info("Setting up the test data file for use in the test")
        return read_and_parse_json(
            'tests/test_host_evacuation_type_page/testdata/host_evacuation_type_page_testdata.json')

    @pytest.mark.hostevacuation
    def test_evacuation_page_create_ticket_checkbox_is_selected_and_form_is_displayed(self, setup):
        """
                Test Case ID: TC_UI_VSI_HET_0001
                Jira ID     : r24741071
                Objective   : Verify that when "Create tickets to notify customers." checkbox is selected,
                              the create ticket form is displayed

                Precondition:
                - User have access to IMS qa environment

                Steps:
                - go the qa env url:
                   https://stable.internal.qadal0901.softlayer.local/Virtual/chooseHostEvacuationType/1455135

                Expected Outcome:
                - Verify that when "Create tickets to notify customers." checkbox is selected,
                  the create ticket form is displayed

                """
        tc_id = setup.get("tc_id_evacuation_page_create_ticket_checkbox_is_selected_and_form_is_displayed", None)
        he_url = setup.get("Host_evacuation_choose_host_url", None)
        host_id = setup.get("Host_evacuation_host_id", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that when Create tickets to notify customers checkbox is selected,"
                          "the create ticket form is displayed")
            self.log.info("Precondition: User has access to IMS qa environment.")
            self.log.info(
                "Starting test: test_evacuation_page_create_ticket_checkbox_is_selected_and_form_is_displayed")

            evacuation_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login.")
            self.login_to_app(self.driver, self.username, self.password, evacuation_page, url)

            self.log.info("Opening the host evacuation ticket url")
            self.open_host_evacuation_ticket_page(he_url, host_id, environment)

            self.log.info("Checking if create tickets to notify customers checkbox is selected")
            is_checkbox_selected = self.is_create_tickets_to_notify_customers_checkbox_selected()
            assert is_checkbox_selected, "Create tickets to notify customers checkbox is not selected"

            self.log.info("Checking if create tickets to notify customers checkbox is selected")
            is_form_displayed = self.is_create_ticket_form_is_displayed()
            assert is_form_displayed, "Create tickets to notify customers form is not displayed"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.hostevacuation
    def test_evacuation_page_create_ticket_checkbox_is_unselected_and_form_is_not_displayed(self, setup):
        """
            Test Case ID: TC_UI_VSI_HET_0002
            Jira ID     : r24741072
            Objective   : Verify that when "Create tickets to notify customers
                          checkbox is not selected, the create ticket form is not displayed

            Precondition:
            - User have access to IMS qa environment

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/chooseHostEvacuationType/1455135

            Expected Outcome:
            - Verify "Create tickets to notify customers" checkbox is not selected,
            - The create ticket form is not displayed

        """
        tc_id = setup.get("tc_id_evacuation_page_create_ticket_checkbox_is_unselected_and_form_is_not_displayed", None)
        he_url = setup.get("Host_evacuation_choose_host_url", None)
        host_id = setup.get("Host_evacuation_host_id", None)
        environment = setup.get("environment", None)

        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that when Create tickets to notify customers"
                          "checkbox is not selected, the create ticket form is not displayed")
            self.log.info("Precondition: User has access to IMS qa environment.")
            self.log.info(
                "Starting test: test_evacuation_page_create_ticket_checkbox_is_unselected_and_form_is_not_displayed")

            evacuation_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login.")
            self.login_to_app(self.driver, self.username, self.password, evacuation_page, url)

            self.log.info("Opening the host evacuation ticket url")
            self.open_host_evacuation_ticket_page(he_url, host_id, environment)

            self.log.info("Unchecking the create tickets to notify customer text box")
            self.uncheck_create_ticket_to_notify_customer_checkbox()
            is_checkbox_selected = self.is_create_tickets_to_notify_customers_checkbox_selected()
            assert not is_checkbox_selected, "Create tickets to notify customers checkbox is selected"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        with pytest.raises(TimeoutException):
            assert self.is_create_ticket_form_is_displayed(), "Create tickets to notify customers form is displayed"
        self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.hostevacuation
    def test_evacuation_page_create_ticket_title_textbox_is_editable(self, setup):
        """
            Test Case ID: TC_UI_VSI_HET_0003
            Jira ID     : r24741073
            Objective   : Verify that the "Title" field is an editable field


            Precondition:
            - User have access to IMS qa environment

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/chooseHostEvacuationType/1455135

            Expected Outcome:
            - Title text box should be editable

        """
        tc_id = setup.get("tc_id_evacuation_page_create_ticket_title_textbox_is_editable", None)
        he_url = setup.get("Host_evacuation_choose_host_url", None)
        host_id = setup.get("Host_evacuation_host_id", None)
        environment = setup.get("environment", None)

        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that the Title field is an editable field")
            self.log.info("Precondition: User has access to IMS qa environment.")
            self.log.info(
                "Starting test: test_evacuation_page_create_ticket_title_textbox_is_editable")

            evacuation_page = setup.get("return_object", None)

            url = self.construct_url_with_branch_name(environment)

            self.log.info(f"Logging into the application with username {self.username}")
            self.login_to_app(self.driver, self.username, self.password, evacuation_page, url)


            self.log.info("Opening the url")
            self.open_host_evacuation_ticket_page(he_url, host_id, environment)

            self.log.info("Check whether create tickets text box is editable")
            is_title_editable = self.check_create_tickets_title_text_box_is_editable()
            self.log.info(f"create ticket textbox editable? {is_title_editable}")
            assert is_title_editable, "Create tickets to notify customers title is not editable"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.hostevacuation
    def test_evacuation_page_create_ticket_form_textbox_is_editable(self, setup):
        """
            Test Case ID: TC_UI_VSI_HET_0004
            Jira ID     : r24741074
            Objective   : Verify that the "Content" field is an editable field


            Precondition:
            - User have access to IMS qa environment

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/chooseHostEvacuationType/1455135

            Expected Outcome:
            - Content text box should be editable

        """
        tc_id = setup.get("tc_id_evacuation_page_create_ticket_form_textbox_is_editable", None)
        he_url = setup.get("Host_evacuation_choose_host_url", None)
        host_id = setup.get("Host_evacuation_host_id", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that the Content field is an editable field")
            self.log.info("Precondition: User has access to IMS qa environment.")
            self.log.info(
                "Starting test: test_evacuation_page_create_ticket_form_textbox_is_editable")

            evacuation_page = setup.get("return_object", None)

            url = self.construct_url_with_branch_name(environment)

            self.log.info(f"Logging into the application with username: {self.username}")
            self.login_to_app(self.driver, self.username, self.password, evacuation_page, url)

            self.log.info("Opening the url")
            self.open_host_evacuation_ticket_page(he_url, host_id, environment)

            self.log.info("Checking whether create ticket form is editable")
            is_form_editable = self.check_create_tickets_form_text_box_is_editable()
            self.log.info(f"create ticket for editable? {is_form_editable}")

            assert is_form_editable, "Create tickets to notify customers title is not editable"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.hostevacuation
    def test_evacuation_page_ticket_has_proper_value_of_account_id_field(self, setup):
        """
            Test Case ID: TC_UI_VSI_HET_0015
            Jira ID     : r24741086
            Objective   : Verify that the ticket has the proper value on "Account ID" field


            Precondition:
            - User have access to IMS qa environment

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Ticket/ticketPreview/1455135

            Expected Outcome:
            - Account id should be not null and has numeric value

        """
        tc_id = setup.get("tc_id_evacuation_page_ticket_has_proper_value_of_account_id_field", None)
        he_url = setup.get("Host_evacuation_ticket_url", None)
        host_id = setup.get("Host_evacuation_host_id", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that the ticket has the proper value on 'Account ID' field")
            self.log.info("Precondition: User has access to IMS qa environment.")
            self.log.info(
                "Starting test: test_evacuation_page_ticket_has_proper_value_of_account_id_field")

            evacuation_page = setup.get("return_object", None)

            url = self.construct_url_with_branch_name(environment)

            self.log.info(f"Logging into the application with username: {self.username}")
            self.login_to_app(self.driver, self.username, self.password, evacuation_page, url)

            self.log.info("Opening the ticket url")
            self.open_host_evacuation_ticket_page(he_url, host_id, environment)
            self.log.info("Getting the account id from ticket page")
            account_id = int(self.get_host_evacuation_ticket_page_account_id())
            self.log.info(f"captured account id {account_id}")
            assert isinstance(account_id, int), "account id is null or non numeric"
        except ValueError as value_exec:
            self.log.error(f"Cant convert account id to numeric : {value_exec}")
            raise value_exec
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.hostevacuation
    def test_evacuation_page_ticket_has_proper_company_field(self, setup):
        """
            Test Case ID: TC_UI_VSI_HET_0016
            Jira ID     : r24741087
            Objective   : Verify that the ticket has the proper value on "Company" field


            Precondition:
            - User have access to IMS qa environment

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Ticket/ticketPreview/1455135

            Expected Outcome:
            - Account id should be not null and has numeric value

        """
        tc_id = setup.get("tc_id_evacuation_page_ticket_has_proper_company_field", None)
        he_url = setup.get("Host_evacuation_ticket_url", None)
        host_id = setup.get("Host_evacuation_host_id", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that the ticket has the proper value on 'Company' field")
            self.log.info("Precondition: User has access to IMS qa environment.")
            self.log.info(
                "Starting test: test_evacuation_page_ticket_has_proper_value_of_account_id_field")

            evacuation_page = setup.get("return_object", None)

            url = self.construct_url_with_branch_name(environment)

            self.log.info(f"Logging into the application with username: {self.username}")
            self.login_to_app(self.driver, self.username, self.password, evacuation_page, url)

            self.log.info("Opening the ticket url")
            self.open_host_evacuation_ticket_page(he_url, host_id, environment)

            self.log.info("Getting the company details from ticket page")
            company_details = self.get_host_evacuation_ticket_page_company_details()

            self.log.info(f"captured account id {company_details}")

            assert isinstance(company_details, str) and company_details.replace(" ", "").isalnum(), \
                "Company details are not displayed on the page"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.hostevacuation
    def test_evacuation_page_ticket_has_proper_value_of_group_field(self, setup):
        """
            Test Case ID: TC_UI_VSI_HET_0017
            Jira ID     : r24741088
            Objective   : Verify that the ticket has the proper value on "Group" field
            Precondition:
            - User have access to IMS qa environment
            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Ticket/ticketPreview/1455135
            Expected Outcome:
            - Group field should be not null and string
        """
        tc_id = setup.get("tc_id_evacuation_page_ticket_has_proper_value_of_group_field", None)
        he_url = setup.get("Host_evacuation_ticket_url", None)
        host_id = setup.get("Host_evacuation_host_id", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that the ticket has the proper value on 'Group' field")
            self.log.info("Precondition: User has access to IMS qa environment.")
            self.log.info(
                "Starting test: test_evacuation_page_ticket_has_proper_value_of_group_field")

            evacuation_page = setup.get("return_object", None)

            url = self.construct_url_with_branch_name(environment)

            self.log.info(f"Logging into the application with username: {self.username}")
            self.login_to_app(self.driver, self.username, self.password, evacuation_page, url)

            self.log.info("Opening the ticket url")
            self.open_host_evacuation_ticket_page(he_url, host_id, environment)

            self.log.info("Getting the info of group field from ticket page")
            group_field_info = self.get_host_evacuation_ticket_page_group_field_info()
            self.log.info(f"captured account id {group_field_info}")
            assert isinstance(group_field_info, str), "group info is null"
        except ValueError as value_exec:
            self.log.error(f"Cant convert account id to numeric : {value_exec}")
            raise value_exec
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")
