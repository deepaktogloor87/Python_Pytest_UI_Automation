import pytest
from selenium.common import TimeoutException
from tests.test_datacenter_checklist_tool_page.test_datacenter_checklist_tool_page_helper import \
    TestDatacenterChecklistToolPageHelper
from tests.test_base import BaseTest
from utilities.read_json import read_and_parse_json
from utilities.read_properties import ReadConfig


class TestDatacenterChecklistToolPage(BaseTest, TestDatacenterChecklistToolPageHelper):
    base_url = ReadConfig.get_application_url()
    username = ReadConfig.get_application_username()
    password = ReadConfig.get_application_password()

    @pytest.fixture(scope="function")
    def setup(self, logger):
        self.log = logger
        self.log.info("Setting up the test data file for use in the test")
        return read_and_parse_json(
            'tests/test_datacenter_checklist_tool_page/testdata/datacenter_checklist_tool_page_testdata.json')

    @pytest.mark.datacenterchecklisttool
    @pytest.mark.php8_1
    def test_start_button_is_displayed_and_enabled(self, setup):
        """
                Test Case ID: TC_UI_VSI_DCCT_0001
                Jira ID     : r25316902
                Objective   : Verify that start button is displayed and enabled

                Precondition:
                - User have access to IMS qa environment

                Steps:
                - go the qa env url:
                   https://stable.internal.qadal0901.softlayer.local/Virtual/chooseHostEvacuationType/1455135

                Expected Outcome:
                - start button is displayed
                - start button is enabled

                """
        tc_id = setup.get("test_start_button_is_displayed_and_enabled", None)
        dvct_url = setup.get("data_verification_tool_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that start button is displayed and enabled")
            self.log.info("Precondition: User has access to IMS qa environment.")
            self.log.info(
                "Starting test: test_start_button_is_displayed_and_enabled")

            datacenter_checklist_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login.")
            self.login_to_app(self.driver, self.username, self.password, datacenter_checklist_page, url)

            self.log.info("Opening the datacenter checklist tool page url")
            self.open_datacenter_checklist_page(dvct_url, environment)

            self.log.info("Checking if start button is displayed and enabled")
            is_start_button_displayed_and_clickable = self.start_button_display_status()

            self.log.info(f"is start button displayed: {is_start_button_displayed_and_clickable}")
            assert is_start_button_displayed_and_clickable, "start button is not displayed and clickable on the page"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.datacenterchecklisttool
    @pytest.mark.php8_1
    def test_select_datacenter_dropdown_options_are_displayed_properly(self, setup):
        """
                Test Case ID: TC_UI_VSI_DCCT_0002
                Jira ID     : r25316902
                Objective   : Verify that select datacenter dropdown options are displayed properly on the page

                Precondition:
                - User have access to IMS qa environment

                Steps:
                - go the qa env url:
                   https://stable.internal.qadal0901.softlayer.local/Virtual/chooseHostEvacuationType/1455135

                Expected Outcome:
                - select datacenter dropdown options are displayed properly on the page

                """
        tc_id = setup.get("test_select_datacenter_dropdown_options_are_displayed_properly", None)
        dvct_url = setup.get("data_verification_tool_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that select datacenter dropdown options are displayed properly on the page")
            self.log.info("Precondition: User has access to IMS qa environment.")
            self.log.info(
                "Starting test: test_select_datacenter_dropdown_options_are_displayed_properly")

            datacenter_checklist_page = setup.get("return_object", None)
            self.log.info(
                f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login.")
            self.login_to_app(self.driver, self.username, self.password, datacenter_checklist_page, url)

            self.log.info("Opening the datacenter checklist tool page url")
            self.open_datacenter_checklist_page(dvct_url, environment)

            self.log.info("Checking if select datacenter dropdown options are visible")
            datacenter_dropdown_options = self.datacenter_dropdown_status()

            self.log.info(f"is select datacenter options are: {datacenter_dropdown_options}")
            assert datacenter_dropdown_options, "select dataceneter options on the page"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.datacenterchecklisttool
    @pytest.mark.php8_1
    def test_datacenter_checklist_heading_are_displayed_properly(self, setup):
        """
                Test Case ID: TC_UI_VSI_DCCT_0003
                Jira ID     : r25316902
                Objective   : Verify that select datacenter checklist heading are displayed properly on the page

                Precondition:
                - User have access to IMS qa environment

                Steps:
                - go the qa env url:
                   https://stable.internal.qadal0901.softlayer.local/Virtual/chooseHostEvacuationType/1455135

                Expected Outcome:
                - select datacenter dropdown options are displayed properly on the page

                """
        tc_id = setup.get("test_datacenter_checklist_heading_are_displayed_properly", None)
        dvct_url = setup.get("data_verification_tool_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info(
                "Objective: Verify that select datacenter checklist heading are displayed properly on the page")
            self.log.info("Precondition: User has access to IMS qa environment.")
            self.log.info(
                "Starting test: test_datacenter_checklist_heading_are_displayed_properly")

            datacenter_checklist_page = setup.get("return_object", None)
            self.log.info(
                f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login.")
            self.login_to_app(self.driver, self.username, self.password, datacenter_checklist_page, url)

            self.log.info("Opening the datacenter checklist tool page url")
            self.open_datacenter_checklist_page(dvct_url, environment)

            self.log.info("Checking if data center headings are displayed")
            datacenter_heading_status = self.datacenter_heading_check()

            self.log.info(f"select datacenter options are: {datacenter_heading_status}")
            assert datacenter_heading_status, "datacenter heading are not available on the page"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.datacenterchecklisttool
    @pytest.mark.php8_1
    def test_all_datacenter_rows_are_displayed_properly(self, setup):
        """
                Test Case ID: TC_UI_VSI_DCCT_0004
                Jira ID     : r25316921
                Objective   : Verify that all datacenter rows are displayed properly on the page

                Precondition:
                - User have access to IMS qa environment

                Steps:
                - go the qa env url:
                   https://stable.internal.qadal0901.softlayer.local/Virtual/chooseHostEvacuationType/1455135

                Expected Outcome:
                - select dall datacenter rows are displayed properly on the page

                """
        tc_id = setup.get("test_all_datacenter_rows_are_displayed_properly", None)
        dvct_url = setup.get("data_verification_tool_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info(
                "Objective: Verify that select datacenter checklist heading are displayed properly on the page")
            self.log.info("Precondition: User has access to IMS qa environment.")
            self.log.info(
                "Starting test: test_all_datacenter_rows_are_displayed_properly")

            datacenter_checklist_page = setup.get("return_object", None)
            self.log.info(
                f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login.")
            self.login_to_app(self.driver, self.username, self.password, datacenter_checklist_page, url)

            self.log.info("Opening the datacenter checklist tool page url")
            self.open_datacenter_checklist_page(dvct_url, environment)

            self.log.info("Checking if data center rows are displayed")
            datacenter_rows_status = self.datacenter_rows_check()

            self.log.info(f"datacenter displayed on the page are: {datacenter_rows_status}")
            assert datacenter_rows_status, "datacenter rows are not available on the page"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.datacenterchecklisttool
    @pytest.mark.php8_1
    def test_legend_table_instructions_displayed_properly(self, setup):
        """
                Test Case ID: TC_UI_VSI_DCCT_0005
                Jira ID     : r25316922
                Objective   : Verify that legend table instructions are displayed properly on the page

                Precondition:
                - User have access to IMS qa environment

                Steps:
                - go the qa env url:
                   https://stable.internal.qadal0901.softlayer.local/Virtual/chooseHostEvacuationType/1455135

                Expected Outcome:
                - select dall datacenter rows are displayed properly on the page

                """
        tc_id = setup.get("test_legend_table_instructions_displayed_properly", None)
        dvct_url = setup.get("data_verification_tool_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info(
                "Objective: VVerify that legend table instructions are displayed properly on the page")
            self.log.info("Precondition: User has access to IMS qa environment.")
            self.log.info(
                "Starting test: test_legend_table_instructions_displayed_properly")

            datacenter_checklist_page = setup.get("return_object", None)
            self.log.info(
                f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login.")
            self.login_to_app(self.driver, self.username, self.password, datacenter_checklist_page, url)

            self.log.info("Opening the datacenter checklist tool page url")
            self.open_datacenter_checklist_page(dvct_url, environment)

            self.log.info("Checking if legend table instructions are displayed")
            legend_table_status = self.legend_table_instructions_display_check()

            self.log.info(f"is legend table displayed: {legend_table_status}")
            assert legend_table_status, "legend table instructions are not available on the page"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")
