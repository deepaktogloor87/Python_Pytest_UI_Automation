import pytest
from selenium.common import TimeoutException
from tests.test_accounting_page.test_accounting_page_helper import TestAccountingPageHelper
from tests.test_base import BaseTest
from utilities.read_json import read_and_parse_json
from utilities.read_properties import ReadConfig


class TestAccountingPage(BaseTest, TestAccountingPageHelper):
    base_url = ReadConfig.get_application_url()
    username = ReadConfig.get_application_username()
    password = ReadConfig.get_application_password()

    @pytest.fixture(scope="function")
    def setup(self, logger):
        self.log = logger
        self.log.info("Setting up the test data file for use in the test")
        return read_and_parse_json(
            'tests/test_accounting_page/testdata/accounting_page_testdata.json')

    @pytest.mark.accounting
    def test_accounting_page_links_are_working_and_clickable(self, setup):
        """
                Test Case ID: TC_UI_AC_0001
                Jira ID     : r25074063
                Objective   : Verify that all the links under accounting page are working and clickable

                Precondition:
                - User have access to IMS qa environment

                Steps:
                - go the qa env url:
                   http://metal-5703.internal.qadal0901.softlayer.local/Accounting

                Expected Outcome:
                - Verify that all the links under accounting page are working and clickable
                - the url should give 200 OK response

        """
        tc_id = setup.get("tc_id_accounting_page_links_are_working_and_clickable", None)
        accounting_page_endpoint = setup.get("accounting_page_url", None)
        environment = setup.get("environment", None)

        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that all the links under accounting page are working and clickable")
            self.log.info("Precondition: User has access to IMS qa environment.")
            self.log.info(
                "Starting test: test_accounting_page_links_are_working_and_clickable")

            accounting_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, accounting_page, url)

            self.log.info("Opening the accounting page url")
            self.open_accounting_page(accounting_page_endpoint, environment)

            is_all_links_working = self.check_if_links_are_clickable_and_working()
            assert is_all_links_working, "All the accounting page links are not working"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.accounting
    def test_number_of_links_present_in_accounting_page(self, setup):
        """
                Test Case ID: TC_UI_AC_0002
                Jira ID     : r25074063
                Objective   : Verify the total no. of links present in accounting page

                Precondition:
                - User have access to IMS qa environment

                Steps:
                - go the qa env url:
                   http://metal-5703.internal.qadal0901.softlayer.local/Accounting

                Expected Outcome:
                - Verify the total no. of links present in accounting page is 30

        """
        tc_id = setup.get("tc_id_number_of_links_present_in_accounting_page", None)
        accounting_page_endpoint = setup.get("accounting_page_url", None)
        environment = setup.get("environment", None)
        no_of_links_under_the_page = setup.get("no_of_links_to_use_under_accounting_page", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify the total no. of links present in accounting page is 30")
            self.log.info("Precondition: User has access to IMS qa environment.")
            self.log.info(
                "Starting test: test_number_of_links_present_in_accounting_page")

            accounting_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, accounting_page, url)

            self.log.info("Opening the accounting page url")
            self.open_accounting_page(accounting_page_endpoint, environment)

            no_of_links = self.get_total_links_under_accounting_page()
            self.log.info(f"No. of links present in accounting page is {no_of_links}")
            assert str(no_of_links) == no_of_links_under_the_page, "All links are not available to use"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")
