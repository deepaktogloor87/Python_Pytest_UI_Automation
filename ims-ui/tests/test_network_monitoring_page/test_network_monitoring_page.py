import pytest
from selenium.common import TimeoutException
from tests.test_network_monitoring_page.test_network_monitoring_page_helper import TestNetworkMonitoringPageHelper
from tests.test_base import BaseTest
from utilities.read_json import read_and_parse_json
from utilities.read_properties import ReadConfig


class TestNetworkMonitoringPage(BaseTest, TestNetworkMonitoringPageHelper):
    base_url = ReadConfig.get_application_url()
    username = ReadConfig.get_application_username()
    password = ReadConfig.get_application_password()

    @pytest.fixture(scope="function")
    def setup(self, logger):
        self.log = logger
        self.log.info("Setting up the test data file for use in the test")
        return read_and_parse_json(
            'tests/test_network_monitoring_page/testdata/network_monitoring_page_testdata.json')

    @pytest.mark.networkmonitoring
    @pytest.mark.php8_1
    def test_links_of_networking_monitoring_are_working_and_clickable(self, setup):
        """
            Test Case ID: TC_UI_VSI_NM_0001
            Jira ID     : r25373860
            Objective   : Verify that all links under networking monitoring page are working and clickable

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - Verify that all links under networking monitoring page are working and clickable

        """
        tc_id = setup.get("test_links_of_networking_monitoring_are_working_and_clickable", None)
        networking_monitoring_url = setup.get("network_monitoring_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that all links under networking monitoring page are working and clickable")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_links_of_networking_monitoring_are_working_and_clickable")

            network_monitoring_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, network_monitoring_page, url)

            self.log.info("Opening network monitoring page")
            self.open_network_monitoring_page(networking_monitoring_url, environment)

            self.log.info("Getting the links of the network monitoring page")
            is_all_links_working = self.check_if_links_response_code_is_200()
            assert is_all_links_working, "all the links of network monitoring are not working"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.networkmonitoring
    @pytest.mark.php8_1
    def test_no_of_links_on_the_page_is_5(self, setup):
        """
            Test Case ID: TC_UI_VSI_NM_0002
            Jira ID     : r25373972
            Objective   : Verify that no. of links present on network monitoring page is 5

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - no. of links present on network monitoring page is 5

        """
        tc_id = setup.get("test_no_of_links_on_the_page_is_5", None)
        networking_monitoring_url = setup.get("network_monitoring_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: no. of links present on network monitoring page is 5")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_no_of_links_on_the_page_is_5")

            network_monitoring_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, network_monitoring_page, url)

            self.log.info("Opening network monitoring page")
            self.open_network_monitoring_page(networking_monitoring_url, environment)

            total_link_value = self.check_total_no_of_links_under_nw_monitoring_page()
            self.log.info(f"no of links under find heading {total_link_value}")
            assert total_link_value == 5, "no of links under find tab is not 5"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")
