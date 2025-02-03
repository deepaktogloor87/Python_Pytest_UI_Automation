import pytest
from selenium.common import TimeoutException
from tests.test_rma_ready_hardware_page.test_rma_ready_hardware_page_helper import TestRMAReadyHardwarePageHelper
from tests.test_base import BaseTest
from utilities.read_json import read_and_parse_json
from utilities.read_properties import ReadConfig


class TestRMAReadyHardwarePage(BaseTest, TestRMAReadyHardwarePageHelper):
    base_url = ReadConfig.get_application_url()
    username = ReadConfig.get_application_username()
    password = ReadConfig.get_application_password()

    @pytest.fixture(scope="function")
    def setup(self, logger):
        self.log = logger
        self.log.info("Setting up the test data file for use in the test")
        return read_and_parse_json(
            'tests/test_rma_ready_hardware_page/testdata/rma_ready_hardware_testdata.json')

    @pytest.mark.rmareadyhardware
    @pytest.mark.php8_1
    def test_serial_number_is_a_editable_field(self, setup):
        """
            Test Case ID: TC_UI_VSI_RMA_0001
            Jira ID     : r25448011
            Objective   : Verify that Serial Number is editable

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - Serial Number is editable

        """
        tc_id = setup.get("test_serial_number_is_a_editable_field", None)
        rma_ready_hardware_url = setup.get("rma_ready_hardware_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that back to pool link redirect to host pool page")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_serial_number_is_a_editable_field")

            rma_ready_hardware_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, rma_ready_hardware_page, url)

            self.log.info("Opening the rma ready hardware page")
            self.open_rma_ready_hardware_page(rma_ready_hardware_url, environment)

            self.log.info("Checking if serial number is editable")
            serial_number_textbox = self.serial_number_textbox_status()

            self.log.info(f"is serial number field editable {serial_number_textbox}")
            assert serial_number_textbox, "serial number is not an editable field"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.rmareadyhardware
    @pytest.mark.php8_1
    def test_location_dropbox_is_not_empty(self, setup):
        """
            Test Case ID: TC_UI_VSI_RMA_0002
            Jira ID     : r25448012
            Objective   : Verify that location dropbox is not empty

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - location dropbox is not empty

        """
        tc_id = setup.get("test_location_dropbox_is_not_empty", None)
        rma_ready_hardware_url = setup.get("rma_ready_hardware_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that location dropbox is not empty")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_location_dropbox_is_not_empty")

            rma_ready_hardware_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, rma_ready_hardware_page, url)

            self.log.info("Opening the rma ready hardware page")
            self.open_rma_ready_hardware_page(rma_ready_hardware_url, environment)

            self.log.info("Checking if location dropbox has data to display")
            location_dropbox = self.location_dropbox_status()

            self.log.info(f"the items in the location are {location_dropbox}")
            assert location_dropbox, "There is no items in location dropbox"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.rmareadyhardware
    @pytest.mark.php8_1
    def test_hardware_function_dropbox_is_not_empty(self, setup):
        """
            Test Case ID: TC_UI_VSI_RMA_0003
            Jira ID     : r25448013
            Objective   : Verify that hardware function dropbox is not empty

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - hardware function dropbox is not empty

        """
        tc_id = setup.get("test_hardware_function_dropbox_is_not_empty", None)
        rma_ready_hardware_url = setup.get("rma_ready_hardware_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that hardware function dropbox is not empty")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_hardware_function_dropbox_is_not_empty")

            rma_ready_hardware_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, rma_ready_hardware_page, url)

            self.log.info("Opening the rma ready hardware page")
            self.open_rma_ready_hardware_page(rma_ready_hardware_url, environment)

            self.log.info("Checking if hardware function dropbox has data to display")
            hardware_function_dropbox = self.hardware_function_dropbox_status()

            self.log.info(f"the items in the hardware function are {hardware_function_dropbox}")
            assert hardware_function_dropbox, "There is no items in hardware function dropbox"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.rmareadyhardware
    @pytest.mark.php8_1
    def test_rma_number_dropbox_is_not_empty(self, setup):
        """
            Test Case ID: TC_UI_VSI_RMA_0006
            Jira ID     : r25456557
            Objective   : Verify that RMA Number dropbox is not empty

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - RMA Number dropbox is not empty

        """
        tc_id = setup.get("test_rma_number_dropbox_is_not_empty", None)
        rma_ready_hardware_url = setup.get("rma_ready_hardware_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that RMA Number dropbox is not empty")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_rma_number_dropbox_is_not_empty")

            rma_ready_hardware_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, rma_ready_hardware_page, url)

            self.log.info("Opening the rma ready hardware page")
            self.open_rma_ready_hardware_page(rma_ready_hardware_url, environment)

            self.log.info("Checking if rma number dropbox has data to display")
            rma_number_dropbox = self.rma_number_dropbox_status()

            self.log.info(f"the items in the rma number are {rma_number_dropbox}")
            assert rma_number_dropbox, "There is no items in rma number dropbox"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.rmareadyhardware
    @pytest.mark.php8_1
    def test_search_btn_is_enabled(self, setup):
        """
            Test Case ID: TC_UI_VSI_RMA_0004
            Jira ID     : r25448014
            Objective   : Verify that Search button is enabled and clickable

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - Search button is enabled and clickable

        """
        tc_id = setup.get("test_search_btn_is_enabled", None)
        rma_ready_hardware_url = setup.get("rma_ready_hardware_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that Search button is enabled and clickable")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_search_btn_is_enabled")

            rma_ready_hardware_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, rma_ready_hardware_page, url)

            self.log.info("Opening the rma ready hardware page")
            self.open_rma_ready_hardware_page(rma_ready_hardware_url, environment)

            self.log.info("Checking if Search button status")
            search_btn = self.search_btn_status()

            self.log.info(f"is search button clickable {search_btn}")
            assert search_btn, "search button is not clickable"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.rmareadyhardware
    @pytest.mark.php8_1
    def test_assign_btn_is_enabled(self, setup):
        """
            Test Case ID: TC_UI_VSI_RMA_0005
            Jira ID     : r25448015
            Objective   : Verify that assign button is enabled and clickable

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - assign button is enabled and clickable

        """
        tc_id = setup.get("test_assign_btn_is_enabled", None)
        rma_ready_hardware_url = setup.get("rma_ready_hardware_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that assign button is enabled and clickable")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_assign_btn_is_enabled")

            rma_ready_hardware_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, rma_ready_hardware_page, url)

            self.log.info("Opening the rma ready hardware page")
            self.open_rma_ready_hardware_page(rma_ready_hardware_url, environment)

            self.log.info("Checking if assign button status")
            assign_btn = self.assign_btn_status()

            self.log.info(f"is assign button clickable {assign_btn}")
            assert assign_btn, "assign button is not clickable"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.rmareadyhardware
    @pytest.mark.php8_1
    def test_rma_ready_hardware_list_table_is_displayed(self, setup):
        """
            Test Case ID: TC_UI_VSI_RMA_0007
            Jira ID     : r25456558
            Objective   : Verify that rma ready hardware list table is displayed

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - rma ready hardware list table is displayed

        """
        tc_id = setup.get("test_rma_ready_hardware_list_table_is_displayed", None)
        rma_ready_hardware_url = setup.get("rma_ready_hardware_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that rma ready hardware list table is displayed")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_rma_ready_hardware_list_table_is_displayed")

            rma_ready_hardware_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, rma_ready_hardware_page, url)

            self.log.info("Opening the rma ready hardware page")
            self.open_rma_ready_hardware_page(rma_ready_hardware_url, environment)

            self.log.info("Checking rma ready hardware list table status")
            rma_ready_hardware_table = self.rma_ready_hardware_list_table_status()

            self.log.info(f"the items in the rma ready table are : {rma_ready_hardware_table}")
            assert rma_ready_hardware_table, "assign button is not clickable"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.rmareadyhardware
    @pytest.mark.php8_1
    def test_selecting_50_in_displaying_check_box_displays_50_element_in_the_table(self, setup):
        """
            Test Case ID: TC_UI_VSI_RMA_0008
            Jira ID     : r25456561
            Objective   : Verify that selecting 50 in displaying textbox displays 50 element in the table

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - passing 50 in go to page textbox displays 50 element in the table

        """
        tc_id = setup.get("test_passing_50_in_go_to_page_textbox_displays_50_element_in_the_table", None)
        rma_ready_hardware_url = setup.get("rma_ready_hardware_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that selecting 50 in displaying textbox displays 50 element in the table")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_passing_50_in_go_to_page_textbox_displays_50_element_in_the_table")

            rma_ready_hardware_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, rma_ready_hardware_page, url)

            self.log.info("Opening the rma ready hardware page")
            self.open_rma_ready_hardware_page(rma_ready_hardware_url, environment)

            self.log.info("Checking the table length after passing the parameter")
            table_length = self.pass_and_check_the_table_content()

            self.log.info(f"the length of the table captured is : {table_length}")
            assert table_length - 1 == 50, "table length is not 50"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")
