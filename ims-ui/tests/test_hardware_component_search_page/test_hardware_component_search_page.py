import time

import pytest
from selenium.common import TimeoutException
from tests.test_hardware_component_search_page.test_hardware_component_search_page_helper import \
    TestHardwareComponentSearchPageHelper
from tests.test_base import BaseTest
from utilities.read_json import read_and_parse_json
from utilities.read_properties import ReadConfig


class TestHardwareComponentSearchPage(BaseTest, TestHardwareComponentSearchPageHelper):
    base_url = ReadConfig.get_application_url()
    username = ReadConfig.get_application_username()
    password = ReadConfig.get_application_password()

    @pytest.fixture(scope="function")
    def setup(self, logger):
        self.log = logger
        self.log.info("Setting up the test data file for use in the test")
        return read_and_parse_json(
            'tests/test_hardware_component_search_page/testdata/hardware_component_search_testdata.json')

    @pytest.mark.php8_1
    @pytest.mark.hardwarecomponentsearch
    def test_search_hardware_component_using_serial_number(self, setup):
        """
            Test Case ID: TC_UI_HCS_0001
            Jira ID     : r25094694
            Objective   : Verify that hardware component can be searched using serial number

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/HardwareComponent/search

            Expected Outcome:
            - hardware component can be search using serial number

        """
        tc_id = setup.get("tc_id_search_hardware_component_using_serial_number", None)
        hardware_component_search_url = setup.get("hardware_component_search_url", None)
        environment = setup.get("environment", None)
        serial_number = setup.get("hardware_serial_number", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that hardware component can be searched using serial number")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_search_hardware_component_using_serial_number")

            hardware_component_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_component_search_page, url)

            self.log.info("Opening the hardware component search page")
            self.open_hardware_component_search_page(hardware_component_search_url, environment)
            result = self.enter_the_serial_number(serial_number)
            assert result, "Failed to get any result when serial number is inputed"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.php8_1
    @pytest.mark.hardwarecomponentsearch
    def test_search_hardware_component_using_component_id(self, setup):
        """
            Test Case ID: TC_UI_HCS_0002
            Jira ID     : r25094694
            Objective   : Verify that hardware component can be searched using component id

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/HardwareComponent/search

            Expected Outcome:
            - hardware component can be search using component id

        """
        tc_id = setup.get("tc_id_test_search_hardware_component_using_component_id", None)
        hardware_component_search_url = setup.get("hardware_component_search_url", None)
        environment = setup.get("environment", None)
        component_id = setup.get("hardware_component_id", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that hardware component can be searched using component id")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_search_hardware_component_using_component_id")

            hardware_component_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_component_search_page, url)

            self.log.info("Opening the hardware component search page")
            self.open_hardware_component_search_page(hardware_component_search_url, environment)
            result = self.enter_the_component_id(component_id)
            assert result, "Failed to get any result when component id is inputed"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.php8_1
    @pytest.mark.hardwarecomponentsearch
    def test_search_hardware_component_using_multiple_serial_number_with_spaces(self, setup):
        """
            Test Case ID: TC_UI_HCS_0003
            Jira ID     : r25094694
            Objective   : Verify that hardware component can be searched using multiple serial number

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/HardwareComponent/search

            Expected Outcome:
            - hardware component can be search using multiple serial number

        """
        tc_id = setup.get("tc_id_test_search_hardware_component_using_multiple_serial_number_with_spaces", None)
        hardware_component_search_url = setup.get("hardware_component_search_url", None)
        environment = setup.get("environment", None)
        multiple_serial_number_with_spaces = setup.get("multiple_serial_number_with_spaces", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that hardware component can be searched using serial number")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_search_hardware_component_using_multiple_serial_number_with_spaces")

            hardware_component_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_component_search_page, url)

            self.log.info("Opening the hardware component search page")
            self.open_hardware_component_search_page(hardware_component_search_url, environment)
            result = self.enter_the_serial_number(multiple_serial_number_with_spaces)
            assert result, "Failed to get any result when serial number is inputed"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.php8_1
    @pytest.mark.hardwarecomponentsearch
    def test_search_hardware_component_using_multiple_serial_number_with_commas(self, setup):
        """
            Test Case ID: TC_UI_HCS_0004
            Jira ID     : r25094694
            Objective   : Verify that hardware component can be searched using multiple serial number with commas

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/HardwareComponent/search

            Expected Outcome:
            - hardware component can be search using multiple serial number with commas

        """
        tc_id = setup.get("test_search_hardware_component_using_multiple_serial_number_with_commas", None)
        hardware_component_search_url = setup.get("hardware_component_search_url", None)
        environment = setup.get("environment", None)
        multiple_serial_number_with_commas = setup.get("multiple_serial_number_with_commas", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info(
                "Objective: Verify that hardware component can be searched using multiple serial number with commas")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_search_hardware_component_using_multiple_serial_number_with_commas")

            hardware_component_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_component_search_page, url)

            self.log.info("Opening the hardware component search page")
            self.open_hardware_component_search_page(hardware_component_search_url, environment)
            result = self.enter_the_serial_number(multiple_serial_number_with_commas)
            assert result, "Failed to get any result when serial number is inputed"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.php8_1
    @pytest.mark.hardwarecomponentsearch
    def test_search_hardware_component_using_component_id_with_spaces(self, setup):
        """
            Test Case ID: TC_UI_HCS_0005
            Jira ID     : r25094694
            Objective   : Verify that hardware component can be searched using component id with spaces

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/HardwareComponent/search

            Expected Outcome:
            - hardware component can be search using component id

        """
        tc_id = setup.get("tc_id_test_search_hardware_component_using_component_id_with_spaces", None)
        hardware_component_search_url = setup.get("hardware_component_search_url", None)
        environment = setup.get("environment", None)
        multiple_component_id_with_spaces = setup.get("multiple_component_id_with_spaces", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that hardware component can be searched using component id with spaces")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_search_hardware_component_using_component_id_with_spaces")

            hardware_component_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_component_search_page, url)

            self.log.info("Opening the hardware component search page")
            self.open_hardware_component_search_page(hardware_component_search_url, environment)
            result = self.enter_the_component_id(multiple_component_id_with_spaces)
            assert result, "Failed to get any result when component id is inputed"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.php8_1
    @pytest.mark.hardwarecomponentsearch
    def test_search_hardware_component_using_component_id_with_commas(self, setup):
        """
            Test Case ID: TC_UI_HCS_0006
            Jira ID     : r25094694
            Objective   : Verify that hardware component can be searched using component id with commas

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/HardwareComponent/search

            Expected Outcome:
            - hardware component can be search using component id

        """
        tc_id = setup.get("tc_id_test_search_hardware_component_using_component_id_with_commas", None)
        hardware_component_search_url = setup.get("hardware_component_search_url", None)
        environment = setup.get("environment", None)
        multiple_component_id_with_commas = setup.get("multiple_component_id_with_commas", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that hardware component can be searched using component id with commas")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_search_hardware_component_using_component_id_with_commas")

            hardware_component_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_component_search_page, url)

            self.log.info("Opening the hardware component search page")
            self.open_hardware_component_search_page(hardware_component_search_url, environment)
            result = self.enter_the_component_id(multiple_component_id_with_commas)
            assert result, "Failed to get any result when component id is inputed"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.php8_1
    @pytest.mark.hardwarecomponentsearch
    def test_search_hardware_component_using_multiple_component_id_with_newline(self, setup):
        """
            Test Case ID: TC_UI_HCS_0007
            Jira ID     : r25094694
            Objective   : Verify that hardware component can be searched using multiple component id with newline

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/HardwareComponent/search

            Expected Outcome:
            - hardware component can be search using component id

        """
        tc_id = setup.get("tc_id_test_search_hardware_component_using_multiple_component_id_with_newline", None)
        hardware_component_search_url = setup.get("hardware_component_search_url", None)
        environment = setup.get("environment", None)
        component_id1 = setup.get("hardware_component_id", None)
        component_id2 = setup.get("component_id1", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info(
                "Objective: Verify that hardware component can be searched using multiple component id with newline")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_search_hardware_component_using_multiple_component_id_with_newline")

            hardware_component_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_component_search_page, url)

            self.log.info("Opening the hardware component search page")
            self.open_hardware_component_search_page(hardware_component_search_url, environment)
            result = self.enter_component_ids_with_newline(component_id1, component_id2)
            assert result, "Failed to get any result when component id is inputed"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.php8_1
    @pytest.mark.hardwarecomponentsearch
    def test_search_hardware_component_using_multiple_serial_number_with_newline(self, setup):
        """
            Test Case ID: TC_UI_HCS_0008
            Jira ID     : r25094694
            Objective   : Verify that hardware component can be searched using multiple serial no. with newline

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/HardwareComponent/search

            Expected Outcome:
            - hardware component can be search using serial no.

        """
        tc_id = setup.get("tc_id_test_search_hardware_component_using_multiple_serial_number_with_newline", None)
        hardware_component_search_url = setup.get("hardware_component_search_url", None)
        environment = setup.get("environment", None)
        serial_number1 = setup.get("hardware_serial_number", None)
        serial_number2 = setup.get("hardware_serial_number2", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info(
                "Objective: Verify that hardware component can be searched using multiple component id with newline")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_search_hardware_component_using_multiple_serial_number_with_newline")

            hardware_component_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_component_search_page, url)

            self.log.info("Opening the hardware component search page")
            self.open_hardware_component_search_page(hardware_component_search_url, environment)
            result = self.enter_serial_numbers_with_newline(serial_number1, serial_number2)
            assert result, "Failed to get any result when serial no is inputed"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.php8_1
    @pytest.mark.hardwarecomponentsearch
    def test_functionality_of_softlayer_serial_number(self, setup):
        """
            Test Case ID: TC_UI_HCS_0009
            Jira ID     : r25094694
            Objective   : Verify that softlayer serial number functionality is working as expected

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/HardwareComponent/search

            Expected Outcome:
            - hardware component can be search using serial no.

        """
        tc_id = setup.get("tc_id_test_functionality_of_softlayer_serial_number", None)
        hardware_component_search_url = setup.get("hardware_component_search_url", None)
        environment = setup.get("environment", None)
        softlayer_serial_number = setup.get("softlayer_serial_number", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info(
                "Objective: Verify that softlayer serial number functionality is working as expected")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_functionality_of_softlayer_serial_number")

            hardware_component_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_component_search_page, url)

            self.log.info("Opening the hardware component search page")
            self.open_hardware_component_search_page(hardware_component_search_url, environment)
            result = self.enter_softlayer_serial_number(softlayer_serial_number)
            assert result, "Failed to get any result when softlayer serial number is inputed"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.php8_1
    @pytest.mark.hardwarecomponentsearch
    def test_functionality_of_multiple_softlayer_serial_number_with_spaces(self, setup):
        """
            Test Case ID: TC_UI_HCS_0010
            Jira ID     : r25094694
            Objective   : Verify that multiple softlayer serial number functionality with spaces is working as expected

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/HardwareComponent/search

            Expected Outcome:
            - hardware component can be search using serial no.

        """
        tc_id = setup.get("tc_id_test_functionality_of_multiple_softlayer_serial_number_with_spaces", None)
        hardware_component_search_url = setup.get("hardware_component_search_url", None)
        environment = setup.get("environment", None)
        softlayer_serial_number_with_spaces = setup.get("softlayer_serial_number_with_spaces", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info(
                "Objective: Verify that multiple softlayer serial number functionality with spaces is working as expected")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_functionality_of_multiple_softlayer_serial_number_with_spaces")

            hardware_component_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_component_search_page, url)

            self.log.info("Opening the hardware component search page")
            self.open_hardware_component_search_page(hardware_component_search_url, environment)
            result = self.enter_softlayer_serial_number(softlayer_serial_number_with_spaces)
            assert result, "Failed to get any result when softlayer serial number is inputed"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.php8_1
    @pytest.mark.hardwarecomponentsearch
    def test_functionality_of_multiple_softlayer_serial_number_with_commas(self, setup):
        """
            Test Case ID: TC_UI_HCS_0011
            Jira ID     : r25094694
            Objective   : Verify that multiple softlayer serial number functionality with commas is working as expected

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/HardwareComponent/search

            Expected Outcome:
            - hardware component can be search using serial no.

        """
        tc_id = setup.get("tc_id_test_functionality_of_multiple_softlayer_serial_number_with_commas", None)
        hardware_component_search_url = setup.get("hardware_component_search_url", None)
        environment = setup.get("environment", None)
        softlayer_serial_number_with_commas = setup.get("softlayer_serial_number_with_commas", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info(
                "Objective: Verify that multiple softlayer serial number functionality with commas is working as expected")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_functionality_of_multiple_softlayer_serial_number_with_commas")

            hardware_component_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_component_search_page, url)

            self.log.info("Opening the hardware component search page")
            self.open_hardware_component_search_page(hardware_component_search_url, environment)
            result = self.enter_softlayer_serial_number(softlayer_serial_number_with_commas)
            assert result, "Failed to get any result when softlayer serial number is inputed"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.php8_1
    @pytest.mark.hardwarecomponentsearch
    def test_functionality_of_multiple_softlayer_serial_number_with_newline(self, setup):
        """
            Test Case ID: TC_UI_HCS_0012
            Jira ID     : r25094694
            Objective   : Verify that multiple softlayer serial number functionality with newline is working as expected

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/HardwareComponent/search

            Expected Outcome:
            - hardware component can be search using serial no.

        """
        tc_id = setup.get("tc_id_test_functionality_of_multiple_softlayer_serial_number_with_newline", None)
        hardware_component_search_url = setup.get("hardware_component_search_url", None)
        environment = setup.get("environment", None)
        softlayer_serial_number1 = setup.get("softlayer_serial_number", None)
        softlayer_serial_number2 = setup.get("softlayer_serial_number2", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info(
                "Objective: Verify that multiple softlayer serial number functionality with newline is working as expected")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_functionality_of_multiple_softlayer_serial_number_with_newline")

            hardware_component_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_component_search_page, url)

            self.log.info("Opening the hardware component search page")
            self.open_hardware_component_search_page(hardware_component_search_url, environment)
            result = self.enter_softlayer_serial_number_with_newline(softlayer_serial_number1, softlayer_serial_number2)
            assert result, "Failed to get any result when softlayer serial number is inputed"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.php8_1
    @pytest.mark.hardwarecomponentsearch
    def test_functionality_of_manufacturer_serial_number(self, setup):
        """
            Test Case ID: TC_UI_HCS_0013
            Jira ID     : r25094694
            Objective   : Verify that manufacturer serial number functionality  is working as expected

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/HardwareComponent/search

            Expected Outcome:
            - hardware component can be search using manufacturer serial number

        """
        tc_id = setup.get("tc_id_test_functionality_of_manufacturer_serial_number", None)
        hardware_component_search_url = setup.get("hardware_component_search_url", None)
        environment = setup.get("environment", None)
        manufacturer_serial_number = setup.get("manufacturer_serial_number", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info(
                "Objective: Verify that manufacturer serial number functionality  is working as expected")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_functionality_of_manufacturer_serial_number")

            hardware_component_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_component_search_page, url)

            self.log.info("Opening the hardware component search page")
            self.open_hardware_component_search_page(hardware_component_search_url, environment)
            result = self.enter_manufacturer_serial_number(manufacturer_serial_number)
            assert result, "Failed to get any result when manufacturer serial number is inputed"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.php8_1
    @pytest.mark.hardwarecomponentsearch
    def test_functionality_of_multiple_manufacturer_serial_number_with_spaces(self, setup):
        """
            Test Case ID: TC_UI_HCS_0014
            Jira ID     : r25094694
            Objective   : Verify that multiple manufacturer serial number functionality with spaces is working as expected

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/HardwareComponent/search

            Expected Outcome:
            - hardware component can be search using manufacturer serial number

        """
        tc_id = setup.get("tc_id_test_functionality_of_multiple_manufacturer_serial_number_with_spaces", None)
        hardware_component_search_url = setup.get("hardware_component_search_url", None)
        environment = setup.get("environment", None)
        manufacturer_serial_number_with_spaces = setup.get("manufacturer_serial_number_with_spaces", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info(
                "Objective: Verify that multiple manufacturer serial number functionality with spaces is working as expected")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_functionality_of_multiple_manufacturer_serial_number_with_spaces")

            hardware_component_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_component_search_page, url)

            self.log.info("Opening the hardware component search page")
            self.open_hardware_component_search_page(hardware_component_search_url, environment)
            result = self.enter_manufacturer_serial_number(manufacturer_serial_number_with_spaces)
            assert result, "Failed to get any result when manufacturer serial number is inputed"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.php8_1
    @pytest.mark.hardwarecomponentsearch
    def test_functionality_of_multiple_manufacturer_serial_number_with_commas(self, setup):
        """
            Test Case ID: TC_UI_HCS_0015
            Jira ID     : r25094694
            Objective   : Verify that multiple manufacturer serial number functionality with commas is working as expected

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/HardwareComponent/search

            Expected Outcome:
            - hardware component can be search using manufacturer serial number

        """
        tc_id = setup.get("tc_id_test_functionality_of_multiple_manufacturer_serial_number_with_commas", None)
        hardware_component_search_url = setup.get("hardware_component_search_url", None)
        environment = setup.get("environment", None)
        manufacturer_serial_number_with_commas = setup.get("manufacturer_serial_number_with_commas", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info(
                "Objective: Verify that multiple manufacturer serial number functionality with commas is working as expected")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_functionality_of_multiple_manufacturer_serial_number_with_commas")

            hardware_component_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_component_search_page, url)

            self.log.info("Opening the hardware component search page")
            self.open_hardware_component_search_page(hardware_component_search_url, environment)
            result = self.enter_manufacturer_serial_number(manufacturer_serial_number_with_commas)
            assert result, "Failed to get any result when manufacturer serial number is inputed"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.php8_1
    @pytest.mark.hardwarecomponentsearch
    def test_functionality_of_multiple_manufacturer_serial_number_with_newline(self, setup):
        """
            Test Case ID: TC_UI_HCS_0016
            Jira ID     : r25094694
            Objective   : Verify that multiple manufacturer serial number functionality with newline is working as expected

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/HardwareComponent/search

            Expected Outcome:
            - hardware component can be search using manufacturer serial number

        """
        tc_id = setup.get("tc_id_test_functionality_of_multiple_manufacturer_serial_number_with_newline", None)
        hardware_component_search_url = setup.get("hardware_component_search_url", None)
        environment = setup.get("environment", None)
        manufacturer_serial_number1 = setup.get("manufacturer_serial_number", None)
        manufacturer_serial_number2 = setup.get("manufacturer_serial_number2", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info(
                "Objective: Verify that multiple manufacturer serial number functionality with newline is working as expected")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_functionality_of_multiple_manufacturer_serial_number_with_newline")

            hardware_component_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_component_search_page, url)

            self.log.info("Opening the hardware component search page")
            self.open_hardware_component_search_page(hardware_component_search_url, environment)
            result = self.enter_manufacturer_serial_number_with_newline(manufacturer_serial_number1, manufacturer_serial_number2)
            assert result, "Failed to get any result when manufacturer serial number is inputed"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.php8_1
    @pytest.mark.hardwarecomponentsearch
    def test_functionality_of_hardware_id(self, setup):
        """
            Test Case ID: TC_UI_HCS_0017
            Jira ID     : r25094694
            Objective   : Verify that hardware id functionality is working as expected

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/HardwareComponent/search

            Expected Outcome:
            - hardware component can be search using hardware id

        """
        tc_id = setup.get("tc_id_test_functionality_of_hardware_id", None)
        hardware_component_search_url = setup.get("hardware_component_search_url", None)
        environment = setup.get("environment", None)
        hardware_id = setup.get("hardware_id", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info(
                "Objective: Verify that hardware id functionality is working as expected")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_functionality_of_hardware_id")

            hardware_component_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_component_search_page, url)

            self.log.info("Opening the hardware component search page")
            self.open_hardware_component_search_page(hardware_component_search_url, environment)
            result = self.enter_hardware_id(hardware_id)
            assert result, "Failed to get any result when manufacturer serial number is inputed"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.php8_1
    @pytest.mark.hardwarecomponentsearch
    def test_functionality_of_multiple_hardware_id_with_spaces(self, setup):
        """
            Test Case ID: TC_UI_HCS_0018
            Jira ID     : r25094694
            Objective   : Verify that multiple hardware id functionality with spaces is working as expected

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/HardwareComponent/search

            Expected Outcome:
            - hardware component can be search using hardware id

        """
        tc_id = setup.get("tc_id_test_functionality_of_multiple_hardware_id_with_spaces", None)
        hardware_component_search_url = setup.get("hardware_component_search_url", None)
        environment = setup.get("environment", None)
        hardware_id_with_spaces = setup.get("hardware_id_with_spaces", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info(
                "Objective: Verify that multiple hardware id functionality with spaces is working as expected")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_functionality_of_multiple_hardware_id_with_spaces")

            hardware_component_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_component_search_page, url)

            self.log.info("Opening the hardware component search page")
            self.open_hardware_component_search_page(hardware_component_search_url, environment)
            result = self.enter_hardware_id(hardware_id_with_spaces)
            assert result, "Failed to get any result when manufacturer serial number is inputed"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.php8_1
    @pytest.mark.hardwarecomponentsearch
    def test_functionality_of_multiple_hardware_id_with_commas(self, setup):
        """
            Test Case ID: TC_UI_HCS_0019
            Jira ID     : r25094694
            Objective   : Verify that multiple hardware id functionality with commas is working as expected

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/HardwareComponent/search

            Expected Outcome:
            - hardware component can be search using hardware id

        """
        tc_id = setup.get("tc_id_test_functionality_of_multiple_hardware_id_with_commas", None)
        hardware_component_search_url = setup.get("hardware_component_search_url", None)
        environment = setup.get("environment", None)
        hardware_id_with_commas = setup.get("hardware_id_with_commas", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info(
                "Objective: Verify that multiple hardware id functionality with commas is working as expected")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_functionality_of_multiple_hardware_id_with_commas")

            hardware_component_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_component_search_page, url)

            self.log.info("Opening the hardware component search page")
            self.open_hardware_component_search_page(hardware_component_search_url, environment)
            result = self.enter_hardware_id(hardware_id_with_commas)
            assert result, "Failed to get any result when manufacturer serial number is inputed"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.php8_1
    @pytest.mark.hardwarecomponentsearch
    def test_functionality_of_multiple_hardware_id_with_newline(self, setup):
        """
            Test Case ID: TC_UI_HCS_0020
            Jira ID     : r25094694
            Objective   : Verify that multiple hardware id functionality with newline is working as expected

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/HardwareComponent/search

            Expected Outcome:
            - hardware component can be search using hardware id

        """
        tc_id = setup.get("tc_id_test_functionality_of_multiple_hardware_id_with_newline", None)
        hardware_component_search_url = setup.get("hardware_component_search_url", None)
        environment = setup.get("environment", None)
        hardware_id1 = setup.get("hardware_id", None)
        hardware_id2 = setup.get("hardware_id2", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info(
                "Objective: Verify that multiple hardware id functionality with newline is working as expected")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_functionality_of_multiple_hardware_id_with_newline")

            hardware_component_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_component_search_page, url)

            self.log.info("Opening the hardware component search page")
            self.open_hardware_component_search_page(hardware_component_search_url, environment)
            result = self.enter_hardware_id_with_newline(hardware_id1, hardware_id2)
            assert result, "Failed to get any result when manufacturer serial number is inputed"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.php8_1
    @pytest.mark.hardwarecomponentsearch
    def test_functionality_of_multiple_selection_of_component_status(self, setup):
        """
            Test Case ID: TC_UI_HCS_0021
            Jira ID     : r25094694
            Objective   : Verify that multiple selection of component status  is working as expected

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/HardwareComponent/search

            Expected Outcome:
            - hardware component can be search using component status

        """
        tc_id = setup.get("tc_id_test_functionality_of_multiple_selection_of_component_status", None)
        hardware_component_search_url = setup.get("hardware_component_search_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info(
                "Objective:Verify that multiple selection of component status  is working as expected")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_functionality_of_multiple_selection_of_component_status")

            hardware_component_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_component_search_page, url)

            self.log.info("Opening the hardware component search page")
            self.open_hardware_component_search_page(hardware_component_search_url, environment)
            result = self.select_multiple_component_status()
            assert result, "Failed to get any result when multiple component status is selected"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.php8_1
    @pytest.mark.hardwarecomponentsearch
    def test_functionality_of_lot_number(self, setup):
        """
            Test Case ID: TC_UI_HCS_0022
            Jira ID     : r25094694
            Objective   : Verify that lot number  is working as expected

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/HardwareComponent/search

            Expected Outcome:
            - hardware component can be search using lot number

        """
        tc_id = setup.get("tc_id_test_functionality_of_lot_number", None)
        hardware_component_search_url = setup.get("hardware_component_search_url", None)
        environment = setup.get("environment", None)
        lot_number = setup.get("lot_number", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info(
                "Objective:Verify that multiple selection of component status  is working as expected")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_functionality_of_lot_number")

            hardware_component_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_component_search_page, url)

            self.log.info("Opening the hardware component search page")
            self.open_hardware_component_search_page(hardware_component_search_url, environment)
            result = self.enter_lot_number(lot_number)
            assert result, "Failed to get any result when lot number is inputed"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.php8_1
    @pytest.mark.hardwarecomponentsearch
    def test_functionality_of_multiple_selection_of_hardware_status(self, setup):
        """
            Test Case ID: TC_UI_HCS_0023
            Jira ID     : r25094694
            Objective   : Verify that multiple selection of hardware status  is working as expected

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/HardwareComponent/search

            Expected Outcome:
            - hardware component can be search using hardware status

        """
        tc_id = setup.get("tc_id_test_functionality_of_multiple_selection_of_hardware_status", None)
        hardware_component_search_url = setup.get("hardware_component_search_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info(
                "Objective: Verify that multiple selection of hardware status  is working as expected")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_functionality_of_multiple_selection_of_hardware_status")

            hardware_component_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_component_search_page, url)

            self.log.info("Opening the hardware component search page")
            self.open_hardware_component_search_page(hardware_component_search_url, environment)
            result = self.select_multiple_hardware_status()
            assert result, "Failed to get any result when multiple hardware status is selected"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.php8_1
    @pytest.mark.hardwarecomponentsearch
    def test_functionality_of_account_id(self, setup):
        """
            Test Case ID: TC_UI_HCS_0024
            Jira ID     : r25094694
            Objective   : Verify that account id functionality is working as expected

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/HardwareComponent/search

            Expected Outcome:
            - hardware component can be search using account id

        """
        tc_id = setup.get("tc_id_test_functionality_of_account_id", None)
        hardware_component_search_url = setup.get("hardware_component_search_url", None)
        environment = setup.get("environment", None)
        account_id = setup.get("account_id", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info(
                "Objective: Verify that account id functionality is working as expected")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_functionality_of_account_id")

            hardware_component_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_component_search_page, url)

            self.log.info("Opening the hardware component search page")
            self.open_hardware_component_search_page(hardware_component_search_url, environment)
            result = self.enter_account_id(account_id)
            assert result, "Failed to get any result when account id is inputed"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.php8_1
    @pytest.mark.hardwarecomponentsearch
    def test_functionality_of_hostname(self, setup):
        """
            Test Case ID: TC_UI_HCS_0025
            Jira ID     : r25094694
            Objective   : Verify that hostname functionality is working as expected

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/HardwareComponent/search

            Expected Outcome:
            - hardware component can be search using account id

        """
        tc_id = setup.get("tc_id_test_functionality_of_hostname", None)
        hardware_component_search_url = setup.get("hardware_component_search_url", None)
        environment = setup.get("environment", None)
        account_id = setup.get("account_id", None)
        hostname = setup.get("hostname", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info(
                "Objective: Verify that hostname functionality is working as expected")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_functionality_of_hostname")

            hardware_component_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_component_search_page, url)

            self.log.info("Opening the hardware component search page")
            self.open_hardware_component_search_page(hardware_component_search_url, environment)
            result = self.enter_hostname(hostname, account_id)
            assert result, "Failed to get any result when hostname is inputed"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.php8_1
    @pytest.mark.hardwarecomponentsearch
    def test_functionality_of_domain(self, setup):
        """
            Test Case ID: TC_UI_HCS_0026
            Jira ID     : r25094694
            Objective   : Verify that domain functionality is working as expected

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/HardwareComponent/search

            Expected Outcome:
            - hardware component can be search using domain

        """
        tc_id = setup.get("tc_id_test_functionality_of_domain", None)
        hardware_component_search_url = setup.get("hardware_component_search_url", None)
        environment = setup.get("environment", None)
        account_id = setup.get("account_id", None)
        hostname = setup.get("hostname", None)
        domain = setup.get("domain", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info(
                "Objective: Verify that domain functionality is working as expected")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_functionality_of_domain")

            hardware_component_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_component_search_page, url)

            self.log.info("Opening the hardware component search page")
            self.open_hardware_component_search_page(hardware_component_search_url, environment)
            result = self.enter_domain(domain, hostname, account_id)
            assert result, "Failed to get any result when domain is inputed"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.php8_1
    @pytest.mark.hardwarecomponentsearch
    def test_functionality_of_function_dropdown(self, setup):
        """
            Test Case ID: TC_UI_HCS_0027
            Jira ID     : r25094694
            Objective   : Verify that function dropdown functionality is working as expected

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/HardwareComponent/search

            Expected Outcome:
            - hardware component can be search using function dropdown

        """
        tc_id = setup.get("tc_id_test_functionality_of_function_dropdown", None)
        hardware_component_search_url = setup.get("hardware_component_search_url", None)
        environment = setup.get("environment", None)
        account_id = setup.get("account_id", None)
        hostname = setup.get("hostname", None)
        domain = setup.get("domain", None)
        function_dropdown_element = setup.get("function_dropdown_element", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info(
                "Objective: Verify that domain functionality is working as expected")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_functionality_of_function_dropdown")

            hardware_component_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_component_search_page, url)

            self.log.info("Opening the hardware component search page")
            self.open_hardware_component_search_page(hardware_component_search_url, environment)
            result = self.select_function_dropdown(function_dropdown_element, domain, hostname, account_id)
            assert result, "Failed to get any result when element from function dropdown is selected"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.php8_1
    @pytest.mark.hardwarecomponentsearch
    def test_functionality_of_chassis(self, setup):
        """
            Test Case ID: TC_UI_HCS_0028
            Jira ID     : r25094694
            Objective   : Verify that chassis functionality is working as expected

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/HardwareComponent/search

            Expected Outcome:
            - hardware component can be search using chassis

        """
        tc_id = setup.get("tc_id_test_functionality_of_chassis", None)
        hardware_component_search_url = setup.get("hardware_component_search_url", None)
        environment = setup.get("environment", None)
        account_id = setup.get("account_id", None)
        hostname = setup.get("hostname", None)
        domain = setup.get("domain", None)
        chassis = setup.get("chassis", None)
        function_dropdown_element = setup.get("function_dropdown_element", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info(
                "Objective: Verify that chassis functionality is working as expected")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_functionality_of_chassis")

            hardware_component_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_component_search_page, url)

            self.log.info("Opening the hardware component search page")
            self.open_hardware_component_search_page(hardware_component_search_url, environment)
            result = self.select_chassis(chassis, function_dropdown_element, domain, hostname, account_id)
            assert result, "Failed to get any result when element from chassis is selected"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.php8_1
    @pytest.mark.hardwarecomponentsearch
    def test_functionality_of_mac_ipv4_ipv6(self, setup):
        """
            Test Case ID: TC_UI_HCS_0029
            Jira ID     : r25094694
            Objective   : Verify that mac ipv4 ipv6 functionality is working as expected

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/HardwareComponent/search

            Expected Outcome:
            - hardware component can be search using mac ipv4 ipv6

        """
        tc_id = setup.get("tc_id_test_functionality_of_mac_ipv4_ipv6", None)
        hardware_component_search_url = setup.get("hardware_component_search_url", None)
        environment = setup.get("environment", None)
        account_id = setup.get("account_id", None)
        hostname = setup.get("hostname", None)
        domain = setup.get("domain", None)
        chassis = setup.get("chassis", None)
        mac_ipv4_ipv6 = setup.get("mac_ipv4_ipv6", None)
        function_dropdown_element = setup.get("function_dropdown_element", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info(
                "Objective: Verify that mac ipv4 ipv6 functionality is working as expected")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_functionality_of_mac_ipv4_ipv6")

            hardware_component_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_component_search_page, url)

            self.log.info("Opening the hardware component search page")
            self.open_hardware_component_search_page(hardware_component_search_url, environment)
            result = self.enter_mac_ipv4_ipv6(mac_ipv4_ipv6, chassis, function_dropdown_element, domain, hostname, account_id)
            assert result, "Failed to get any result when mac ipv4 ipv6 is inputed"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.php8_1
    @pytest.mark.hardwarecomponentsearch
    def test_functionality_of_export_csv_button(self, setup):
        """
            Test Case ID: TC_UI_HCS_0030
            Jira ID     : r25094694
            Objective   : Verify that export csv button functionality is working as expected

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/HardwareComponent/search

            Expected Outcome:
            - hardware component can be downloaded from export csv button

        """
        tc_id = setup.get("tc_id_test_functionality_of_export_csv_button", None)
        hardware_component_search_url = setup.get("hardware_component_search_url", None)
        environment = setup.get("environment", None)
        account_id = setup.get("account_id", None)
        hostname = setup.get("hostname", None)
        domain = setup.get("domain", None)
        chassis = setup.get("chassis", None)
        mac_ipv4_ipv6 = setup.get("mac_ipv4_ipv6", None)
        function_dropdown_element = setup.get("function_dropdown_element", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info(
                "Objective: Verify that export csv button functionality is working as expected")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_functionality_of_export_csv_button")

            hardware_component_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_component_search_page, url)

            self.log.info("Opening the hardware component search page")
            self.open_hardware_component_search_page(hardware_component_search_url, environment)
            self.enter_mac_ipv4_ipv6(mac_ipv4_ipv6, chassis, function_dropdown_element, domain, hostname,
                                              account_id)
            result = self.download_csv_file()
            # assert result, "Csv file is not downloaded from export csv button"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.php8_1
    @pytest.mark.hardwarecomponentsearch
    def test_functionality_of_export_excel_button(self, setup):
        """
            Test Case ID: TC_UI_HCS_0031
            Jira ID     : r25094694
            Objective   : Verify that export excel button functionality is working as expected

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/HardwareComponent/search

            Expected Outcome:
            - hardware component can be downloaded from export excel button

        """
        tc_id = setup.get("tc_id_test_functionality_of_export_excel_button", None)
        hardware_component_search_url = setup.get("hardware_component_search_url", None)
        environment = setup.get("environment", None)
        account_id = setup.get("account_id", None)
        hostname = setup.get("hostname", None)
        domain = setup.get("domain", None)
        chassis = setup.get("chassis", None)
        mac_ipv4_ipv6 = setup.get("mac_ipv4_ipv6", None)
        function_dropdown_element = setup.get("function_dropdown_element", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info(
                "Objective: Verify that export excel button functionality is working as expected")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_functionality_of_export_excel_button")

            hardware_component_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_component_search_page, url)

            self.log.info("Opening the hardware component search page")
            self.open_hardware_component_search_page(hardware_component_search_url, environment)
            self.enter_mac_ipv4_ipv6(mac_ipv4_ipv6, chassis, function_dropdown_element, domain, hostname,
                                     account_id)
            result = self.download_excel_file()
            # assert result, "Csv file is not downloaded from export csv button"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.php8_1
    @pytest.mark.hardwarecomponentsearch
    def test_functionality_of_send_and_save_search_query_url(self, setup):
        """
            Test Case ID: TC_UI_HCS_0032
            Jira ID     : r25094694
            Objective   : Verify that send and save search query url functionality is working as expected

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/HardwareComponent/search

            Expected Outcome:
            - send and save search query url is working as expected

        """
        tc_id = setup.get("tc_id_test_functionality_of_send_and_save_search_query_url", None)
        hardware_component_search_url = setup.get("hardware_component_search_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info(
                "Objective: Verify that send and save search query url functionality is working as expected")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_functionality_of_send_and_save_search_query_url")

            hardware_component_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_component_search_page, url)

            self.log.info("Opening the hardware component search page")
            self.open_hardware_component_search_page(hardware_component_search_url, environment)
            result = self.click_on_send_and_share_button()
            assert result, "send and save search query url is not working as expected"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.php8_1
    @pytest.mark.hardwarecomponentsearch
    def test_functionality_of_filter_by_acccount_id(self, setup):
        """
            Test Case ID: TC_UI_HCS_0033
            Jira ID     : r25094694
            Objective   : Verify that filter by account id functionality is working as expected

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/HardwareComponent/search

            Expected Outcome:
            - hardware component can be search using account id

        """
        tc_id = setup.get("tc_id_test_functionality_of_filter_by_acccount_id", None)
        hardware_component_search_url = setup.get("hardware_component_search_url", None)
        environment = setup.get("environment", None)
        account_id_details = setup.get("account_id_details", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info(
                "Objective: Verify that filter by account id functionality is working as expected")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_functionality_of_filter_by_acccount_id")

            hardware_component_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_component_search_page, url)

            self.log.info("Opening the hardware component search page")
            self.open_hardware_component_search_page(hardware_component_search_url, environment)
            result = self.enter_account_id_details(account_id_details)
            assert result, "hardware component cannot be search using account id"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.php8_1
    @pytest.mark.hardwarecomponentsearch
    def test_functionality_of_filter_by_hw_id(self, setup):
        """
            Test Case ID: TC_UI_HCS_0034
            Jira ID     : r25094694
            Objective   : Verify that filter by hw id functionality is working as expected

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/HardwareComponent/search

            Expected Outcome:
            - hardware component can be search using hw id

        """
        tc_id = setup.get("tc_id_test_functionality_of_filter_by_hw_id", None)
        hardware_component_search_url = setup.get("hardware_component_search_url", None)
        environment = setup.get("environment", None)
        hw_id = setup.get("hw_id", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info(
                "Objective: Verify that filter by hw id functionality is working as expected")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_functionality_of_filter_by_hw_id")

            hardware_component_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_component_search_page, url)

            self.log.info("Opening the hardware component search page")
            self.open_hardware_component_search_page(hardware_component_search_url, environment)
            result = self.enter_hw_id_details(hw_id)
            assert result, "hardware component cannot be search using hw id"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.php8_1
    @pytest.mark.hardwarecomponentsearch
    def test_functionality_of_filter_by_location(self, setup):
        """
            Test Case ID: TC_UI_HCS_0035
            Jira ID     : r25094694
            Objective   : Verify that filter by hw id functionality is working as expected

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/HardwareComponent/search

            Expected Outcome:
            - hardware component can be search using hw id

        """
        tc_id = setup.get("tc_id_test_functionality_of_filter_by_location", None)
        hardware_component_search_url = setup.get("hardware_component_search_url", None)
        environment = setup.get("environment", None)
        hw_id = setup.get("hw_id", None)
        location = setup.get("location", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info(
                "Objective: Verify that filter by hw id functionality is working as expected")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_functionality_of_filter_by_location")

            hardware_component_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_component_search_page, url)

            self.log.info("Opening the hardware component search page")
            self.open_hardware_component_search_page(hardware_component_search_url, environment)
            result = self.select_location_details(location, hw_id)
            assert result, "hardware component cannot be search using hw id"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.php8_1
    @pytest.mark.hardwarecomponentsearch
    def test_click_id_link_opens_non_error_page(self, setup):
        """
            Test Case ID: TC_UI_HCS_0036
            Jira ID     : r25094694
            Objective   : Verify when id is clicked the page opens up without error

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/HardwareComponent/search

            Expected Outcome:
            - when id is clicked the page opens up without error

        """
        tc_id = setup.get("tc_id_test_click_id_link_opens_non_error_page", None)
        hardware_component_search_url = setup.get("hardware_component_search_url", None)
        environment = setup.get("environment", None)
        serial_number = setup.get("hardware_serial_number", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify when id is clicked the page opens up without error")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_click_id_link_opens_non_error_page")

            hardware_component_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_component_search_page, url)

            self.log.info("Opening the hardware component search page")
            self.open_hardware_component_search_page(hardware_component_search_url, environment)
            self.enter_the_serial_number(serial_number)
            result = self.check_if_id_link_working_status()
            assert result, "id link is broken"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

            