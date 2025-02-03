import pytest
from selenium.common import TimeoutException
from tests.test_hardware_transaction_page.test_hardware_transaction_page_helper import \
    TestHardwareTransactionPagePageHelper
from tests.test_base import BaseTest
from utilities.read_json import read_and_parse_json
from utilities.read_properties import ReadConfig


class TestHardwareTransactionPage(BaseTest, TestHardwareTransactionPagePageHelper):
    base_url = ReadConfig.get_application_url()
    username = ReadConfig.get_application_username()
    password = ReadConfig.get_application_password()

    @pytest.fixture(scope="function")
    def setup(self, logger):
        self.log = logger
        self.log.info("Setting up the test data file for use in the test")
        return read_and_parse_json(
            'tests/test_hardware_transaction_page/testdata/hardware_transaction_page_testdata.json')

    @pytest.mark.hardwaretxn
    @pytest.mark.php8_1
    def test_links_under_transaction_page_are_accessible(self, setup):
        """
            Test Case ID: TC_UI_VSI_HT_0001
            Jira ID     : r25353534
            Objective   : Verify that links of hardware transaction page returns response code 200

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            -  links of hardware transaction page returns response code 200

        """
        tc_id = setup.get("test_links_under_transaction_page_are_accessible", None)
        hardware_txn_url = setup.get("hardware_transaction_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that links of hardware transaction page returns response code 200")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_links_under_transaction_page_are_accessible")

            update_pool_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, update_pool_page, url)

            self.log.info("Opening the update pool page")
            self.open_hardware_txn_page(hardware_txn_url, environment)

            self.log.info("Getting the links from hardware transactions page")
            is_accessible = self.extract_the_links_from_the_page()

            self.log.info(f"are all links accessible {is_accessible}")
            assert is_accessible, "all the links under transaction page are not accessible"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.hardwaretxn
    @pytest.mark.php8_1
    def test_total_no_of_links_under_transaction_page_is_8(self, setup):
        """
            Test Case ID: TC_UI_VSI_HT_0002
            Jira ID     : r25353535
            Objective   : Verify that no. of links of hardware transaction page is equal to 8
            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - no. of links of hardware transaction page is equal to 8

        """
        tc_id = setup.get("test_total_no_of_links_under_transaction_page_is_8", None)
        hardware_txn_url = setup.get("hardware_transaction_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that no. of links of hardware transaction page is equal to 8")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_total_no_of_links_under_transaction_page_is_8")

            update_pool_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, update_pool_page, url)

            self.log.info("Opening the update pool page")
            self.open_hardware_txn_page(hardware_txn_url, environment)

            self.log.info("Getting the no. of links from hardware transaction page")
            link_value = self.get_the_no_of_links_from_page()

            self.log.info(f"no.of links present on the page: {link_value}")
            assert link_value == 8, "total no. of links present on the page is not 8"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")
            