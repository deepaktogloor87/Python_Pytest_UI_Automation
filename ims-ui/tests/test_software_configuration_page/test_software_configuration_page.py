import time

import pytest
from selenium.common import TimeoutException
from tests.test_software_configuration_page.test_software_configuration_page_helper import \
    TestSoftwareConfigurationPageHelper
from tests.test_base import BaseTest
from utilities.read_json import read_and_parse_json
from utilities.read_properties import ReadConfig


class TestSoftwareConfigurationPage(BaseTest, TestSoftwareConfigurationPageHelper):
    base_url = ReadConfig.get_application_url()
    username = ReadConfig.get_application_username()
    password = ReadConfig.get_application_password()

    @pytest.fixture(scope="function")
    def setup(self, logger):
        self.log = logger
        self.log.info("Setting up the test data file for use in the test")
        return read_and_parse_json(
            'tests/test_software_configuration_page/testdata/software_configuration_page_testdata.json')

    @pytest.mark.php8_1
    @pytest.mark.softwareconfiguration
    def test_fragment_can_be_added_to_assigned_fragments_list(self, setup):
        """
            Test Case ID: TC_UI_SC_0001
            Jira ID     : r25094694
            Objective   : Verify that fragments can be added to assigned fragments list without errors

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/HardwareComponent/search

            Expected Outcome:
            - Fragments can be added to assigned fragments list without errors

        """
        tc_id = setup.get("tc_id_fragment_can_be_added_to_assigned_fragments_list", None)
        software_configuration_url = setup.get("software_configuration_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify fragments can be added to assigned fragments list without errors")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_fragment_can_be_added_to_assigned_fragments_list")

            hardware_component_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_component_search_page, url)

            self.log.info("Opening the software configuration page")
            self.open_hardware_lease_page(software_configuration_url, environment)

            self.select_a_template()
            self.select_a_section()
            self.select_an_available_fragment()
            self.click_on_assigned_fragment_btn()
            result = self.check_if_fragment_is_assigned_to_assigned_fragment_list()
            assert result == "Assigned Fragments", "Fragment is not added to assigned fragment list"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")
