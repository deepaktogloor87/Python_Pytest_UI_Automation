import pytest
from selenium.common import TimeoutException
from tests.test_reports_page.tests_reports_page_helper import TestReportsPagePageHelper
from tests.test_base import BaseTest
from utilities.read_json import read_and_parse_json
from utilities.read_properties import ReadConfig


class TestReportsPage(BaseTest, TestReportsPagePageHelper):
    base_url = ReadConfig.get_application_url()
    username = ReadConfig.get_application_username()
    password = ReadConfig.get_application_password()

    @pytest.fixture(scope="function")
    def setup(self, logger):
        self.log = logger
        self.log.info("Setting up the test data file for use in the test")
        return read_and_parse_json(
            'tests/test_reports_page/testdata/reports_testdata.json')

    @pytest.mark.reports
    @pytest.mark.php8_1
    def test_links_of_accounting_tab_are_working_and_clickable(self, setup):
        """
            Test Case ID: TC_UI_VSI_RA_0001
            Jira ID     : r25374007
            Objective   : Verify that all the links of accounting tab are working and clickable

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - All the links of accounting tab are working and clickable

        """
        tc_id = setup.get("test_links_of_accounting_tab_are_working_and_clickable", None)
        reports_url = setup.get("reports_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that all the links of accounting tab are working and clickable")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_links_of_accounting_tab_are_working_and_clickable")

            reports_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, reports_page, url)

            self.log.info("Opening reports page")
            self.open_reports_page(reports_url, environment)

            self.log.info("Getting the working status of accounting tab links")
            is_all_links_working = self.check_if_accounting_links_response_code_is_200()
            assert is_all_links_working, "all the links of accounting tab are not working"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.reports
    @pytest.mark.php8_1
    def test_links_of_sales_tab_are_working_and_clickable(self, setup):
        """
            Test Case ID: TC_UI_VSI_RA_0002
            Jira ID     : r25374009
            Objective   : Verify that all the links of sales tab are working and clickable

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - All the links of sales tab are working and clickable

        """
        tc_id = setup.get("test_links_of_sales_tab_are_working_and_clickable", None)
        reports_url = setup.get("reports_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that all the links of sales tab are working and clickable")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_links_of_sales_tab_are_working_and_clickable")

            reports_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, reports_page, url)

            self.log.info("Opening reports page")
            self.open_reports_page(reports_url, environment)

            self.log.info("Getting the working status of sales tab links")
            is_all_links_working = self.check_if_sales_links_response_code_is_200()
            assert is_all_links_working, "all the links of sales tab are not working"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.reports
    @pytest.mark.php8_1
    def test_links_of_datacenter_tab_are_working_and_clickable(self, setup):
        """
            Test Case ID: TC_UI_VSI_RA_0003
            Jira ID     : r25374010
            Objective   : Verify that all the links of datacenter tab are working and clickable

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - All the links of datacenter tab are working and clickable

        """
        tc_id = setup.get("test_links_of_datacenter_tab_are_working_and_clickable", None)
        reports_url = setup.get("reports_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that all the links of datacenter tab are working and clickable")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_links_of_datacenter_tab_are_working_and_clickable")

            reports_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, reports_page, url)

            self.log.info("Opening reports page")
            self.open_reports_page(reports_url, environment)

            self.log.info("Getting the working status of datacenter tab links")
            is_all_links_working = self.check_if_datacenter_links_response_code_is_200()
            assert is_all_links_working, "all the links of datacenter tab are not working"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.reports
    @pytest.mark.php8_1
    def test_links_of_tickets_tab_are_working_and_clickable(self, setup):
        """
            Test Case ID: TC_UI_VSI_RA_0004
            Jira ID     : r25374011
            Objective   : Verify that all the links of tickets tab are working and clickable

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - All the links of tickets tab are working and clickable

        """
        tc_id = setup.get("test_links_of_tickets_tab_are_working_and_clickable", None)
        reports_url = setup.get("reports_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that all the links of tickets tab are working and clickable")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_links_of_tickets_tab_are_working_and_clickable")

            reports_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, reports_page, url)

            self.log.info("Opening reports page")
            self.open_reports_page(reports_url, environment)

            self.log.info("Getting the working status of tickets tab links")
            is_all_links_working = self.check_if_tickets_links_response_code_is_200()
            assert is_all_links_working, "all the links of tickets tab are not working"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.reports
    @pytest.mark.php8_1
    def test_links_of_misc_tab_are_working_and_clickable(self, setup):
        """
            Test Case ID: TC_UI_VSI_RA_0005
            Jira ID     : r25374012
            Objective   : Verify that all the links of misc tab are working and clickable

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - All the links of misc tab are working and clickable

        """
        tc_id = setup.get("test_links_of_misc_tab_are_working_and_clickable", None)
        reports_url = setup.get("reports_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that all the links of misc tab are working and clickable")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_links_of_misc_tab_are_working_and_clickable")

            reports_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, reports_page, url)

            self.log.info("Opening reports page")
            self.open_reports_page(reports_url, environment)

            self.log.info("Getting the working status of misc tab links")
            is_all_links_working = self.check_if_misc_links_response_code_is_200()
            assert is_all_links_working, "all the links of misc tab are not working"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.reports
    @pytest.mark.php8_1
    def test_no_of_accounting_links_on_the_page_is_14(self, setup):
        """
            Test Case ID: TC_UI_VSI_RA_0006
            Jira ID     : r25374014
            Objective   : Verify that no. of links present on accounting tab is 14

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - no. of links present on accounting tab is 14

        """
        tc_id = setup.get("test_no_of_accounting_links_on_the_page_is_14", None)
        reports_url = setup.get("reports_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that no. of links present on accounting tab is 14")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_no_of_accounting_links_on_the_page_is_14")

            reports_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, reports_page, url)

            self.log.info("Opening reports page")
            self.open_reports_page(reports_url, environment)

            total_link_value = self.check_total_no_of_links_under_accounting_tab()
            self.log.info(f"no of links under accounting tab {total_link_value}")
            assert total_link_value == 14, "no of links under accounting tab is not 14"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.reports
    @pytest.mark.php8_1
    def test_no_of_sales_links_on_the_page_is_8(self, setup):
        """
            Test Case ID: TC_UI_VSI_RA_0007
            Jira ID     : r25374015
            Objective   : Verify that no. of links present on sales tab is 8

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - no. of links present on sales tab is 8

        """
        tc_id = setup.get("test_no_of_sales_links_on_the_page_is_8", None)
        reports_url = setup.get("reports_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that no. of links present on accounting tab is 14")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_no_of_sales_links_on_the_page_is_8")

            reports_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, reports_page, url)

            self.log.info("Opening reports page")
            self.open_reports_page(reports_url, environment)

            total_link_value = self.check_total_no_of_links_under_sales_tab()
            self.log.info(f"no of links under sales tab {total_link_value}")
            assert total_link_value == 8, "no of links under sales tab is not 8"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.reports
    @pytest.mark.php8_1
    def test_no_of_datacenter_links_on_the_page_is_1(self, setup):
        """
            Test Case ID: TC_UI_VSI_RA_0008
            Jira ID     : r25374016
            Objective   : Verify that no. of links present on datacenter tab is 1

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - no. of links present on datacenter tab is 1

        """
        tc_id = setup.get("test_no_of_datacenter_links_on_the_page_is_1", None)
        reports_url = setup.get("reports_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that no. of links present on datacenter tab is 1")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_no_of_datacenter_links_on_the_page_is_1")

            reports_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, reports_page, url)

            self.log.info("Opening reports page")
            self.open_reports_page(reports_url, environment)

            total_link_value = self.check_total_no_of_links_under_datacenter_tab()
            self.log.info(f"no of links under datacenter tab {total_link_value}")
            assert total_link_value == 1, "no of links under datacenter tab is not 1"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.reports
    @pytest.mark.php8_1
    def test_no_of_tickets_links_on_the_page_is_8(self, setup):
        """
            Test Case ID: TC_UI_VSI_RA_0009
            Jira ID     : r25374030
            Objective   : Verify that no. of links present on tickets tab is 8

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - no. of links present on tickets tab is 8

        """
        tc_id = setup.get("test_no_of_tickets_links_on_the_page_is_8", None)
        reports_url = setup.get("reports_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that no. of links present on tickets tab is 8")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_no_of_tickets_links_on_the_page_is_8")

            reports_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, reports_page, url)

            self.log.info("Opening reports page")
            self.open_reports_page(reports_url, environment)

            total_link_value = self.check_total_no_of_links_under_tickets_tab()
            self.log.info(f"no of links under tickets tab {total_link_value}")
            assert total_link_value == 8, "no of links under tickets tab is not 8"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.reports
    @pytest.mark.php8_1
    def test_no_of_misc_links_on_the_page_is_19(self, setup):
        """
            Test Case ID: TC_UI_VSI_RA_0010
            Jira ID     : r25374031
            Objective   : Verify that no. of links present on misc tab is 19

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - no. of links present on misc tab is 19

        """
        tc_id = setup.get("test_no_of_misc_links_on_the_page_is_19", None)
        reports_url = setup.get("reports_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that no. of links present on tickets tab is 8")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_no_of_misc_links_on_the_page_is_19")

            reports_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, reports_page, url)

            self.log.info("Opening reports page")
            self.open_reports_page(reports_url, environment)

            total_link_value = self.check_total_no_of_links_under_misc_tab()
            self.log.info(f"no of links under misc tab {total_link_value}")
            assert total_link_value == 19, "no of links under misc tab is not 19"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")
            