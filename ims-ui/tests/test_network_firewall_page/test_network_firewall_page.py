import pytest
from selenium.common import TimeoutException
from tests.test_network_firewall_page.test_network_firewall_page_helper import TestNetworkFirewallPagePageHelper
from tests.test_base import BaseTest
from utilities.read_json import read_and_parse_json
from utilities.read_properties import ReadConfig


class TestNetworkFirewallPage(BaseTest, TestNetworkFirewallPagePageHelper):
    base_url = ReadConfig.get_application_url()
    username = ReadConfig.get_application_username()
    password = ReadConfig.get_application_password()

    @pytest.fixture(scope="function")
    def setup(self, logger):
        self.log = logger
        self.log.info("Setting up the test data file for use in the test")
        return read_and_parse_json(
            'tests/test_network_firewall_page/testdata/network_firewall_testdata.json')

    @pytest.mark.networkfirewall
    @pytest.mark.php8_1
    def test_links_under_network_firewall_page_are_accessible(self, setup):
        """
            Test Case ID: TC_UI_VSI_NF_0001
            Jira ID     : r25374037
            Objective   : Verify that links of network firewall page returns response code 200

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            -  links of network firewall page returns response code 200

        """
        tc_id = setup.get("test_links_under_network_firewall_page_are_accessible", None)
        network_firewall_url = setup.get("network_firewall_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that links of network firewall page returns response code 200")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_links_under_network_firewall_page_are_accessible")

            network_firewall_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, network_firewall_page, url)

            self.log.info("Opening the network firewall page")
            self.open_network_firewall_page(network_firewall_url, environment)

            self.log.info("Getting the links from network firewall page")
            is_accessible = self.extract_the_links_from_the_page()

            self.log.info(f"are all links accessible {is_accessible}")
            assert is_accessible, "all the links under network firewall are not accessible"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.networkfirewall
    @pytest.mark.php8_1
    def test_no_of_links_on_the_page_is_13(self, setup):
        """
            Test Case ID: TC_UI_VSI_NF_0002
            Jira ID     : r25396640
            Objective   : Verify that no. of links present on network firewall page is 13

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - no. of links present on network firewall page is 13

        """
        tc_id = setup.get("test_no_of_links_on_the_page_is_13", None)
        network_firewall_url = setup.get("network_firewall_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that links of network firewall page returns response code 200")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_no_of_links_on_the_page_is_13")

            network_firewall_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, network_firewall_page, url)

            self.log.info("Opening the network firewall page")
            self.open_network_firewall_page(network_firewall_url, environment)

            total_link_value = self.check_total_no_of_links_under_nw_firewall_page()
            self.log.info(f"no of links under network firewall: {total_link_value}")
            assert total_link_value == 13, "no of links under network firewall is not 13"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")