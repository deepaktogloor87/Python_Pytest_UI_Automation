import pytest
from selenium.common import TimeoutException
from tests.test_hardware_page.test_hardware_page_helper import TestHardwarePageHelper
from tests.test_base import BaseTest
from utilities.read_json import read_and_parse_json
from utilities.read_properties import ReadConfig


class TestHardwarePage(BaseTest, TestHardwarePageHelper):
    base_url = ReadConfig.get_application_url()
    username = ReadConfig.get_application_username()
    password = ReadConfig.get_application_password()

    @pytest.fixture(scope="function")
    def setup(self, logger):
        self.log = logger
        self.log.info("Setting up the test data file for use in the test")
        return read_and_parse_json(
            'tests/test_hardware_page/testdata/hardware_page_testdata.json')

    @pytest.mark.hardware
    @pytest.mark.php8_1
    def test_hardware_page_links_under_find_are_working_and_clickable(self, setup):
        """
                Test Case ID: TC_UI_AC_0001
                Jira ID     : r25316934
                Objective   : Verify that all the links under hardware page are working and clickable

                Precondition:
                - User have access to IMS qa environment

                Steps:
                - go the qa env url:
                   http://metal-5703.internal.qadal0901.softlayer.local/Accounting

                Expected Outcome:
                - All the hardware page links under find are working and clickable

        """
        tc_id = setup.get("test_hardware_page_links_under_find_are_working_and_clickable", None)
        hardware_endpoint = setup.get("hardware_page_url", None)
        environment = setup.get("environment", None)

        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that all the links under accounting page are working and clickable")
            self.log.info("Precondition: User has access to IMS qa environment.")
            self.log.info(
                "Starting test: test_hardware_page_links_under_find_are_working_and_clickable")

            hardware_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_page, url)

            self.log.info("Opening the hardware page url")
            self.open_hardware_page(hardware_endpoint, environment)

            is_all_links_working = self.check_if_links_response_code_is_200()
            assert is_all_links_working, "all the links under find of hardware page are not working"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.hardware
    @pytest.mark.php8_1
    def test_hardware_page_links_under_hardware_heading_are_working_and_clickable(self, setup):
        """
                Test Case ID: TC_UI_AC_0002
                Jira ID     : r25329706
                Objective   : Verify that all the links under hardware heading are working and clickable

                Precondition:
                - User have access to IMS qa environment

                Steps:
                - go the qa env url:
                   http://metal-5703.internal.qadal0901.softlayer.local/Accounting

                Expected Outcome:
                - All the hardware page links under hardware heading are working and clickable

        """
        tc_id = setup.get("test_hardware_page_links_under_hardware_heading_are_working_and_clickable", None)
        hardware_endpoint = setup.get("hardware_page_url", None)
        environment = setup.get("environment", None)

        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: All the hardware page links under hardware heading are working and clickable")
            self.log.info("Precondition: User has access to IMS qa environment.")
            self.log.info(
                "Starting test: test_hardware_page_links_under_hardware_heading_are_working_and_clickable")

            hardware_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_page, url)

            self.log.info("Opening the hardware page url")
            self.open_hardware_page(hardware_endpoint, environment)

            is_all_links_working = self.check_if_links_response_code_is_200_under_hardware_heading()
            self.log.info(f"working status of links under hardware heading {is_all_links_working}")
            assert is_all_links_working, "all the links under find of hardware page is not working are not working"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.hardware
    @pytest.mark.php8_1
    def test_total_links_under_find_heading_is_8(self, setup):
        """
                Test Case ID: TC_UI_AC_0003
                Jira ID     : r25346341
                Objective   : Verify that no. of links under find heading is 8

                Precondition:
                - User have access to IMS qa environment

                Steps:
                - go the qa env url:
                   http://metal-5703.internal.qadal0901.softlayer.local/Accounting

                Expected Outcome:
                - find heading link = 8

        """
        tc_id = setup.get("test_total_links_under_find_heading_is_8", None)
        hardware_endpoint = setup.get("hardware_page_url", None)
        environment = setup.get("environment", None)

        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: No. of links under find heading is 8")
            self.log.info("Precondition: User has access to IMS qa environment.")
            self.log.info(
                "Starting test: test_total_links_under_find_heading_is_8")

            hardware_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_page, url)

            self.log.info("Opening the hardware page url")
            self.open_hardware_page(hardware_endpoint, environment)

            total_link_value = self.check_total_no_of_links_under_find()
            self.log.info(f"no of links under find heading {total_link_value}")
            assert total_link_value == 8, "no of links under find tab is not 8"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.hardware
    @pytest.mark.php8_1
    def test_total_links_under_hardware_heading_is_25(self, setup):
        """
                Test Case ID: TC_UI_AC_0004
                Jira ID     : r25329706
                Objective   : Verify that no. of links under hardware heading is 24

                Precondition:
                - User have access to IMS qa environment

                Steps:
                - go the qa env url:
                   http://metal-5703.internal.qadal0901.softlayer.local/Accounting

                Expected Outcome:
                - find heading link = 8

        """
        tc_id = setup.get("test_total_links_under_hardware_heading_is_24", None)
        hardware_endpoint = setup.get("hardware_page_url", None)
        environment = setup.get("environment", None)

        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: No. of links under hardware heading is 24")
            self.log.info("Precondition: User has access to IMS qa environment.")
            self.log.info(
                "Starting test: test_total_links_under_hardware_heading_is_24")

            hardware_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_page, url)

            self.log.info("Opening the hardware page url")
            self.open_hardware_page(hardware_endpoint, environment)

            total_link_value = self.check_total_no_of_links_under_hardware()
            self.log.info(f"no of links under hardware heading {total_link_value}")
            assert total_link_value == 25, "no of links under hardware tab is not 8"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")
