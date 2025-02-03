import pytest
from selenium.common import TimeoutException
from tests.test_cancel_virtual_process_instance.test_cancel_virtual_process_instance_helper import \
    TestCancelVirtualProcessInstanceHelper
from tests.test_base import BaseTest
from utilities.read_json import read_and_parse_json
from utilities.read_properties import ReadConfig


class TestCancelVirtualProcessInstance(BaseTest, TestCancelVirtualProcessInstanceHelper):
    base_url = ReadConfig.get_application_url()
    username = ReadConfig.get_application_username()
    password = ReadConfig.get_application_password()

    @pytest.fixture(scope="function")
    def setup(self, logger):
        self.log = logger
        self.log.info("Setting up the test data file for use in the test")
        return read_and_parse_json(
            'tests/test_cancel_virtual_process_instance/testdata/cancel_virtual_process_instance_testdata.json')

    @pytest.mark.cancelvirtualprocessinstance
    def test_cancel_virtual_process_instance_link_present_on_the_page(self, setup):
        """
            Test Case ID: TC_UI_VSI_CVPI_0001
            Jira ID     : r25282465
            Objective   : Verify that cancel virtual process instance is a link and present on the page

            Precondition:
            - User have access to IMS qa environment

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/chooseHostEvacuationType/1455135

            Expected Outcome:
            - cancel virtual process instance is a link
            - cancel virtual process instance is displayed on the page

        """
        tc_id = setup.get("test_cancel_virtual_process_instance_link_present_on_the_page", None)
        cvpi_url = setup.get("cancel_virtual_process_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that Virtual process instance is a link and present on the page")
            self.log.info("Precondition: User has access to IMS qa environment.")
            self.log.info(
                "Starting test: test_cancel_virtual_process_instance_link_present_on_the_page")

            cancel_virtual_process_instance_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login.")
            self.login_to_app(self.driver, self.username, self.password, cancel_virtual_process_instance_page, url)

            self.log.info("Opening cancel virtual process instance page")
            self.open_cancel_virtual_process_instance_page(cvpi_url, environment)

            self.log.info("Checking if cancel virtual process instance is a link and present on the page")
            cancel_virtual_process_instance_status = self.cancel_virtual_process_instance_link_presence()

            self.log.info(f"is cancel vitual process instance link present: {cancel_virtual_process_instance_status}")
            assert cancel_virtual_process_instance_status, "cancel virtual process instance is not present on the page"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.cancelvirtualprocessinstance
    def test_cancel_virtual_process_instance_page_displays_proper_instruction_note(self, setup):
        """
            Test Case ID: TC_UI_VSI_CVPI_0002
            Jira ID     : r25282474
            Objective   : Verify that cancel virtual process instance displays proper instruction notes

            Precondition:
            - User have access to IMS qa environment

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/chooseHostEvacuationType/1455135

            Expected Outcome:
            - proper instructions are displayed on cancel virtual process instance

        """
        tc_id = setup.get("test_cancel_virtual_process_instance_page_displays_proper_instruction_note", None)
        cvpi_url = setup.get("cancel_virtual_process_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that cancel virtual process instance displays proper instruction notes")
            self.log.info("Precondition: User has access to IMS qa environment.")
            self.log.info(
                "Starting test: test_cancel_virtual_process_instance_page_displays_proper_instruction_note")

            cancel_virtual_process_instance_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login.")
            self.login_to_app(self.driver, self.username, self.password, cancel_virtual_process_instance_page, url)

            self.log.info("Opening cancel virtual process instance page")
            self.build_url_and_open_cancel_virtual_process_instance_page(cvpi_url, environment)

            self.log.info("Checking if proper instructions are present on the page")
            instruction_presence_status = self.check_for_instructions_presence()

            self.log.info(f"is cancel virtual process instance link present: {instruction_presence_status}")
            assert instruction_presence_status, "instructions are not present oncancel virtual process instance"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.cancelvirtualprocessinstance
    def test_info_of_process_instance_is_displayed_by_clicking_on_view_button(self, setup):
        """
            Test Case ID: TC_UI_VSI_CVPI_0003
            Jira ID     : r25282476
            Objective   : Verify that process instance information is displayed by clicking on view button

            Precondition:
            - User have access to IMS qa environment

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/chooseHostEvacuationType/1455135

            Expected Outcome:
            - process instance info is displayed properly

        """
        tc_id = setup.get("test_info_of_process_instance_is_displayed_by_clicking_on_view_button", None)
        cvpi_url = setup.get("cancel_virtual_process_url", None)
        process_instance = setup.get("process_instance", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that process instance information is displayed by clicking on view button")
            self.log.info("Precondition: User has access to IMS qa environment.")
            self.log.info(
                "Starting test: test_info_of_process_instance_is_displayed_by_clicking_on_view_button")

            cancel_virtual_process_instance_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login.")
            self.login_to_app(self.driver, self.username, self.password, cancel_virtual_process_instance_page, url)

            self.log.info("Opening cancel virtual process instance page")
            self.build_url_and_open_cancel_virtual_process_instance_page(cvpi_url, environment)

            self.log.info("Entering the process instance and clicking on view button")
            instance_info_presence_status = self.check_for_process_instance_info(process_instance)

            self.log.info(f"is process instance information present: {instance_info_presence_status}")
            assert instance_info_presence_status, "process instance information is not present " \
                                                  "by clicking on view button"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.cancelvirtualprocessinstance
    def test_providing_incorrect_process_id_gives_error(self, setup):
        """
            Test Case ID: TC_UI_VSI_CVPI_0004
            Jira ID     : r25282479
            Objective   : Verify that providing incorrect process_id gives error

            Precondition:
            - User have access to IMS qa environment

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/chooseHostEvacuationType/1455135

            Expected Outcome:
            - an incorrect process instance should give error

        """
        tc_id = setup.get("test_providing_incorrect_process_id_gives_error", None)
        cvpi_url = setup.get("cancel_virtual_process_url", None)
        incorrect_process_instance = setup.get("incorrect_process_instance", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that providing incorrect process_id gives error")
            self.log.info("Precondition: User has access to IMS qa environment.")
            self.log.info(
                "Starting test: test_providing_incorrect_process_id_gives_error")

            cancel_virtual_process_instance_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login.")
            self.login_to_app(self.driver, self.username, self.password, cancel_virtual_process_instance_page, url)

            self.log.info("Opening cancel virtual process instance page")
            self.build_url_and_open_cancel_virtual_process_instance_page(cvpi_url, environment)

            self.log.info("Entering incorrect process instance and clicking on view button")
            error_msg_status = self.check_for_error_msg_provinding_incorrect_ps(incorrect_process_instance)

            self.log.info(f"is error msg generated: {error_msg_status}")
            assert error_msg_status, "error message is not generated by providing incorrect process instance"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.cancelvirtualprocessinstance
    def test_cancel_button_is_displayed(self, setup):
        """
            Test Case ID: TC_UI_VSI_CVPI_0005
            Jira ID     : r25282481
            Objective   : Verify that cancel button is displayed

            Precondition:
            - User have access to IMS qa environment

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/chooseHostEvacuationType/1455135

            Expected Outcome:
            - an incorrect process instance should give error

        """
        tc_id = setup.get("test_cancel_button_is_displayed", None)
        cvpi_url = setup.get("cancel_virtual_process_url", None)
        process_instance = setup.get("process_instance", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that cancel button is displayed")
            self.log.info("Precondition: User has access to IMS qa environment.")
            self.log.info(
                "Starting test: test_cancel_button_is_displayed")

            cancel_virtual_process_instance_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login.")
            self.login_to_app(self.driver, self.username, self.password, cancel_virtual_process_instance_page, url)

            self.log.info("Opening cancel virtual process instance page")
            self.build_url_and_open_cancel_virtual_process_instance_page(cvpi_url, environment)

            self.log.info("Entering the process instance and clicking on view button")
            cancel_button_status = self.get_the_cancel_button_status(process_instance)

            self.log.info(f"is cancel button present: {cancel_button_status}")
            assert cancel_button_status, "Cancel button is not displayed"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")
