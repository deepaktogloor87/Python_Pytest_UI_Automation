import time

import pytest
from selenium.common import TimeoutException
from tests.test_hardware_search_page.test_hardware_search_page_helper import TestHardwareSearchPageHelper
from tests.test_base import BaseTest
from utilities.read_json import read_and_parse_json
from utilities.read_properties import ReadConfig


class TestHardwareSearchPage(BaseTest, TestHardwareSearchPageHelper):
    base_url = ReadConfig.get_application_url()
    username = ReadConfig.get_application_username()
    password = ReadConfig.get_application_password()

    @pytest.fixture(scope="function")
    def setup(self, logger):
        self.log = logger
        self.log.info("Setting up the test data file for use in the test")
        return read_and_parse_json(
            'tests/test_hardware_search_page/testdata/hardware_search_page_testdata.json')

    @pytest.mark.hardwaresearch
    @pytest.mark.php8_1
    def test_location_checkbox_has_data_to_select(self, setup):
        """
            Test Case ID: TC_UI_VSI_HS_0001
            Jira ID     : r25444054
            Objective   : Verify that location checkbox has data to select

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - location checkbox has data to select and display

        """
        tc_id = setup.get("test_location_checkbox_has_data_to_select", None)
        hardware_search_url = setup.get("hardware_search_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that location checkbox has data to select")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_location_checkbox_has_data_to_select")

            hardware_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_search_page, url)

            self.log.info("Opening the hardware search page")
            self.open_hardware_search_page(hardware_search_url, environment)

            self.log.info("Checking the hardware search location checkbox status")
            location_box = self.location_checkbox_status()

            self.log.info(f"the items in the location checkbox are {location_box}")
            assert location_box, "There is no items in location checkbox"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.hardwaresearch
    @pytest.mark.php8_1
    def test_hardware_function_has_data_to_select(self, setup):
        """
            Test Case ID: TC_UI_VSI_HS_0002
            Jira ID     : r25444055
            Objective   : Verify that hardware function checkbox is not empty

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - hardware function has data to select and display

        """
        tc_id = setup.get("test_hardware_function_has_data_to_select", None)
        hardware_search_url = setup.get("hardware_search_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that hardware function checkbox is not empty")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_hardware_function_has_data_to_select")

            hardware_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_search_page, url)

            self.log.info("Opening the hardware search page")
            self.open_hardware_search_page(hardware_search_url, environment)

            self.log.info("Checking the hardware search hardware function checkbox status")
            hardware_function_box = self.hardware_function_checkbox_status()

            self.log.info(f"the items in the hardware function are {hardware_function_box}")
            assert hardware_function_box, "There is no items in hardware function checkbox"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.hardwaresearch
    @pytest.mark.php8_1
    def test_uim_managed_asset_has_data_to_select(self, setup):
        """
            Test Case ID: TC_UI_VSI_HS_0003
            Jira ID     : r25444056
            Objective   : Verify that uim managed asset checkbox is not empty

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - uim managed asset has data to select and display

        """
        tc_id = setup.get("test_uim_managed_assest_has_data_to_select", None)
        hardware_search_url = setup.get("hardware_search_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that uim managed asset checkbox is not empty")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_uim_managed_asset_has_data_to_select")

            hardware_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_search_page, url)

            self.log.info("Opening the hardware search page")
            self.open_hardware_search_page(hardware_search_url, environment)

            self.log.info("Checking the hardware search uim managed asset checkbox status")
            uim_managed_asset_box = self.uim_managed_asset_checkbox_status()

            self.log.info(f"the items in the uim managed asset are {uim_managed_asset_box}")
            assert uim_managed_asset_box, "There is no items in uim managed asset checkbox"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.hardwaresearch
    @pytest.mark.php8_1
    def test_tag_checkbox_has_data_to_select(self, setup):
        """
            Test Case ID: TC_UI_VSI_HS_0004
            Jira ID     : r25444057
            Objective   : Verify that tag checkbox is not empty

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - tag has data to select and display

        """
        tc_id = setup.get("test_tag_checkbox_has_data_to_select", None)
        hardware_search_url = setup.get("hardware_search_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that tag checkbox is not empty")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_tag_checkbox_has_data_to_select")

            hardware_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_search_page, url)

            self.log.info("Opening the hardware search page")
            self.open_hardware_search_page(hardware_search_url, environment)

            self.log.info("Checking the hardware search tag checkbox status")
            tag_box = self.tag_checkbox_status()

            self.log.info(f"the items in the tag are {tag_box}")
            assert tag_box, "There is no items in tag checkbox"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.hardwaresearch
    @pytest.mark.php8_1
    def test_hardware_pool_checkbox_has_data_to_select(self, setup):
        """
            Test Case ID: TC_UI_VSI_HS_0005
            Jira ID     : r25444059
            Objective   : Verify that hardware pool checkbox is not empty

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - hardware pool has data to select and display

        """
        tc_id = setup.get("test_hardware_pool_checkbox_has_data_to_select", None)
        hardware_search_url = setup.get("hardware_search_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that hardware pool checkbox is not empty")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_hardware_pool_checkbox_has_data_to_select")

            hardware_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_search_page, url)

            self.log.info("Opening the hardware search page")
            self.open_hardware_search_page(hardware_search_url, environment)

            self.log.info("Checking the hardware search page's hardware pool checkbox status")
            hardware_pool_box = self.hardware_pool_checkbox_status()

            self.log.info(f"the items in the hardware pool are {hardware_pool_box}")
            assert hardware_pool_box, "There is no items in hardware pool checkbox"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.hardwaresearch
    @pytest.mark.php8_1
    def test_pooled_servers_checkbox_has_data_to_select(self, setup):
        """
            Test Case ID: TC_UI_VSI_HS_0006
            Jira ID     : r25444058
            Objective   : Verify that pooled servers checkbox is not empty

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - pooled servers has data to select and display

        """
        tc_id = setup.get("test_pooled_servers_checkbox_has_data_to_select", None)
        hardware_search_url = setup.get("hardware_search_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that pooled servers checkbox is not empty")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_pooled_servers_checkbox_has_data_to_select")

            hardware_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_search_page, url)

            self.log.info("Opening the hardware search page")
            self.open_hardware_search_page(hardware_search_url, environment)

            self.log.info("Checking the hardware search page's pooled servers checkbox status")
            pooled_servers_box = self.pooled_servers_checkbox_status()

            self.log.info(f"the items in the pooled servers are {pooled_servers_box}")
            assert pooled_servers_box, "There is no items in pooled servers checkbox"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.hardwaresearch
    @pytest.mark.php8_1
    def test_hardware_pool_status_checkbox_has_data_to_select(self, setup):
        """
            Test Case ID: TC_UI_VSI_HS_0007
            Jira ID     : r25444060
            Objective   : Verify that hardware pool status checkbox is not empty

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - hardware pool status has data to select and display

        """
        tc_id = setup.get("test_hardware_pool_status_checkbox_has_data_to_select", None)
        hardware_search_url = setup.get("hardware_search_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that pooled servers checkbox is not empty")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_hardware_pool_status_checkbox_has_data_to_select")

            hardware_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_search_page, url)

            self.log.info("Opening the hardware search page")
            self.open_hardware_search_page(hardware_search_url, environment)

            self.log.info("Checking the hardware search page's hardware pool status checkbox status")
            hardware_pool_status_box = self.hardware_pool_status_checkbox_status()

            self.log.info(f"the items in the hardware pool status are {hardware_pool_status_box}")
            assert hardware_pool_status_box, "There is no items in hardware pool status checkbox"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.hardwaresearch
    @pytest.mark.php8_1
    def test_generic_component_checkbox_has_data_to_select(self, setup):
        """
            Test Case ID: TC_UI_VSI_HS_0008
            Jira ID     : r25444061
            Objective   : Verify that generic component checkbox is not empty

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - generic component has data to select and display

        """
        tc_id = setup.get("test_generic_component_checkbox_has_data_to_select", None)
        hardware_search_url = setup.get("hardware_search_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that generic component checkbox is not empty")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_generic_component_checkbox_has_data_to_select")

            hardware_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_search_page, url)

            self.log.info("Opening the hardware search page")
            self.open_hardware_search_page(hardware_search_url, environment)

            self.log.info("Checking the hardware search page's generic component checkbox status")
            generic_component_box = self.generic_component_checkbox_status()

            self.log.info(f"the items in the generic component are {generic_component_box}")
            assert generic_component_box, "There is no items in generic component checkbox"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.hardwaresearch
    @pytest.mark.php8_1
    def test_specific_component_checkbox_has_data_to_select(self, setup):
        """
            Test Case ID: TC_UI_VSI_HS_0009
            Jira ID     : r25444062
            Objective   : Verify that specific component checkbox is not empty

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - specific component has data to select and display

        """
        tc_id = setup.get("test_specific_component_checkbox_has_data_to_select", None)
        hardware_search_url = setup.get("hardware_search_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that specific component checkbox is not empty")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_specific_component_checkbox_has_data_to_select")

            hardware_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_search_page, url)

            self.log.info("Opening the hardware search page")
            self.open_hardware_search_page(hardware_search_url, environment)

            time.sleep(10)
            self.log.info("Checking the hardware search page's specific component checkbox status")
            specific_component_box = self.specific_component_checkbox_status()

            self.log.info(f"the items in the specific component are {specific_component_box}")
            assert specific_component_box, "There is no items in specific component checkbox"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.hardwaresearch
    @pytest.mark.php8_1
    def test_chassis_checkbox_has_data_to_select(self, setup):
        """
            Test Case ID: TC_UI_VSI_HS_0010
            Jira ID     : r25444063
            Objective   : Verify that chassis checkbox is not empty

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - chassis has data to select and display

        """
        tc_id = setup.get("test_chassis_checkbox_has_data_to_select", None)
        hardware_search_url = setup.get("hardware_search_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that chassis checkbox is not empty")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_chassis_checkbox_has_data_to_select")

            hardware_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_search_page, url)

            self.log.info("Opening the hardware search page")
            self.open_hardware_search_page(hardware_search_url, environment)

            time.sleep(10) #time taken to load the paga
            self.log.info("Checking the hardware search page's chassis checkbox status")
            chassis_box = self.chassis_checkbox_status()

            self.log.info(f"the items in the specific component are {chassis_box}")
            assert chassis_box, "There is no items in chassis checkbox"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.hardwaresearch
    @pytest.mark.php8_1
    def test_display_btn_is_enabled(self, setup):
        """
            Test Case ID: TC_UI_VSI_HS_0011
            Jira ID     : r25447941
            Objective   : Verify that display button is enabled

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - display button is enabled

        """
        tc_id = setup.get("test_display_btn_is_enabled", None)
        hardware_search_url = setup.get("hardware_search_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that display button is enabled")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_display_btn_is_enabled")

            hardware_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_search_page, url)

            self.log.info("Opening the hardware search page")
            self.open_hardware_search_page(hardware_search_url, environment)

            self.log.info("Checking the hardware search page's display button status")
            display_btn = self.display_btn_status()

            self.log.info(f"is display button clickable {display_btn}")
            assert display_btn, "display button is not clickable"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.hardwaresearch
    @pytest.mark.php8_1
    def test_export_csv_btn_is_enabled(self, setup):
        """
            Test Case ID: TC_UI_VSI_HS_0012
            Jira ID     : r25447942
            Objective   : Verify that export csv button is enabled

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - export csv button is enabled

        """
        tc_id = setup.get("test_export_csv_btn_is_enabled", None)
        hardware_search_url = setup.get("hardware_search_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that export csv button is enabled")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_export_csv_btn_is_enabled")

            hardware_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_search_page, url)

            self.log.info("Opening the hardware search page")
            self.open_hardware_search_page(hardware_search_url, environment)

            self.log.info("Checking the hardware search page's export csv button status")
            export_csv_btn = self.export_csv_btn_status()

            self.log.info(f"is export csv button clickable {export_csv_btn}")
            assert export_csv_btn, "export csv button is not clickable"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.hardwaresearch
    @pytest.mark.php8_1
    def test_export_excel_btn_is_enabled(self, setup):
        """
            Test Case ID: TC_UI_VSI_HS_0013
            Jira ID     : r25447943
            Objective   : Verify that export excel button is enabled

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - export excel button is enabled

        """
        tc_id = setup.get("test_export_excel_btn_is_enabled", None)
        hardware_search_url = setup.get("hardware_search_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that export csv button is enabled")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_export_excel_btn_is_enabled")

            hardware_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_search_page, url)

            self.log.info("Opening the hardware search page")
            self.open_hardware_search_page(hardware_search_url, environment)

            self.log.info("Checking the hardware search page's export excel button status")
            export_excel_btn = self.export_excel_btn_status()

            self.log.info(f"is export excel button clickable {export_excel_btn}")
            assert export_excel_btn, "export excel button is not clickable"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.hardwaresearch
    @pytest.mark.php8_1
    def test_export_origin_certificates_btn_is_enabled(self, setup):
        """
            Test Case ID: TC_UI_VSI_HS_0014
            Jira ID     : r25447944
            Objective   : Verify that export origin certificate button is enabled

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - export origin certificate button is enabled

        """
        tc_id = setup.get("test_export_origin_certificates_btn_is_enabled", None)
        hardware_search_url = setup.get("hardware_search_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that export csv button is enabled")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_export_origin_certificates_btn_is_enabled")

            hardware_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_search_page, url)

            self.log.info("Opening the hardware search page")
            self.open_hardware_search_page(hardware_search_url, environment)

            self.log.info("Checking the hardware search page's export origin certificate button status")
            export_origin_certificate_btn = self.export_origin_certificate_btn_status()

            self.log.info(f"is export origin certificate button clickable {export_origin_certificate_btn}")
            assert export_origin_certificate_btn, "export origin certificate button is not clickable"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.hardwaresearch
    @pytest.mark.php8_1
    def test_save_and_share_search_query_url_btn_is_enabled(self, setup):
        """
            Test Case ID: TC_UI_VSI_HS_0015
            Jira ID     : r25447945
            Objective   : Verify that save and share search query url button is enabled

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - save and share search query url button is enabled

        """
        tc_id = setup.get("test_save_and_share_search_query_url_btn_is_enabled", None)
        hardware_search_url = setup.get("hardware_search_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that save and share search query url button is enabled")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_save_and_share_search_query_url_btn_is_enabled")

            hardware_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_search_page, url)

            self.log.info("Opening the hardware search page")
            self.open_hardware_search_page(hardware_search_url, environment)

            self.log.info("Checking the hardware search page's save and share search query url button status")
            save_and_share_search_query_url_btn = self.save_and_share_search_query_url_btn_status()

            self.log.info(f"is save and share search query url button clickable {save_and_share_search_query_url_btn}")
            assert save_and_share_search_query_url_btn, "save and share search query url button is not clickable"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.hardwaresearch
    @pytest.mark.php8_1
    def test_hardware_id_is_textfield_and_editable(self, setup):
        """
            Test Case ID: TC_UI_VSI_HS_0016
            Jira ID     : r25447951
            Objective   : Verify that hardware id is an editable field

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - hardware id is an editable field

        """
        tc_id = setup.get("test_hardware_id_is_textfield_and_editable", None)
        hardware_search_url = setup.get("hardware_search_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that hardware id is an editable field")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_hardware_id_is_textfield_and_editable")

            hardware_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_search_page, url)

            self.log.info("Opening the hardware search page")
            self.open_hardware_search_page(hardware_search_url, environment)

            self.log.info("Checking the hardware search page's hardware id textbox status")
            hardware_id_txt_field = self.hardware_id_txt_field_status()

            self.log.info(f"is hardware id txt field editable {hardware_id_txt_field}")
            assert hardware_id_txt_field, "hardware id txt field editable is not editable"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.hardwaresearch
    @pytest.mark.php8_1
    def test_virtual_host_id_is_textfield_and_editable(self, setup):
        """
            Test Case ID: TC_UI_VSI_HS_0016
            Jira ID     : r25447995
            Objective   : Verify that virtual host id is an editable field

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - virtual host id is an editable field

        """
        tc_id = setup.get("test_virtual_host_id_is_textfield_and_editable", None)
        hardware_search_url = setup.get("hardware_search_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that virtual host id is an editable field")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_virtual_host_id_is_textfield_and_editable")

            hardware_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_search_page, url)

            self.log.info("Opening the hardware search page")
            self.open_hardware_search_page(hardware_search_url, environment)

            self.log.info("Checking the hardware search page's virtual host id textbox status")
            virtual_host_id_txt_field = self.virtual_host_id_txt_field_status()

            self.log.info(f"is virtual host id txt field editable {virtual_host_id_txt_field}")
            assert virtual_host_id_txt_field, "virtual host id txt field editable is not editable"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.hardwaresearch
    @pytest.mark.php8_1
    def test_manufacture_serial_number_is_textfield_and_editable(self, setup):
        """
            Test Case ID: TC_UI_VSI_HS_0018
            Jira ID     : r25447996
            Objective   : Verify that manufacture serial number is an editable field

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - manufacture serial number is an editable field

        """
        tc_id = setup.get("test_manufacture_serial_number_is_textfield_and_editable", None)
        hardware_search_url = setup.get("hardware_search_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that manufacture serial number is an editable field")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_manufacture_serial_number_is_textfield_and_editable")

            hardware_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_search_page, url)

            self.log.info("Opening the hardware search page")
            self.open_hardware_search_page(hardware_search_url, environment)

            self.log.info("Checking the hardware search page's manufacture serial number textbox status")
            manufacture_serial_number_txt_field = self.manufacture_serial_number_txt_field_status()

            self.log.info(f"is manufacture serial number txt field editable {manufacture_serial_number_txt_field}")
            assert manufacture_serial_number_txt_field, "manufacture serial number txt field editable is not editable"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.hardwaresearch
    @pytest.mark.php8_1
    def test_softlayer_serial_number_is_textfield_and_editable(self, setup):
        """
            Test Case ID: TC_UI_VSI_HS_0019
            Jira ID     : r25447997
            Objective   : Verify that softlayer serial number is an editable field

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - softlayer serial number is an editable field

        """
        tc_id = setup.get("test_softlayer_serial_number_is_textfield_and_editable", None)
        hardware_search_url = setup.get("hardware_search_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that manufacture serial number is an editable field")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_softlayer_serial_number_is_textfield_and_editable")

            hardware_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_search_page, url)

            self.log.info("Opening the hardware search page")
            self.open_hardware_search_page(hardware_search_url, environment)

            self.log.info("Checking the hardware search page's softlayer serial number textbox status")
            softlayer_serial_number_txt_field = self.softlayer_serial_number_txt_field_status()

            self.log.info(f"is softlayer serial number txt field editable {softlayer_serial_number_txt_field}")
            assert softlayer_serial_number_txt_field, "softlayer serial number txt field editable is not editable"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.hardwaresearch
    @pytest.mark.php8_1
    def test_account_id_is_textfield_and_editable(self, setup):
        """
            Test Case ID: TC_UI_VSI_HS_0020
            Jira ID     : r25447998
            Objective   : Verify that account id is an editable field

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - account id is an editable field

        """
        tc_id = setup.get("test_account_id_is_textfield_and_editable", None)
        hardware_search_url = setup.get("hardware_search_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that account id is an editable field")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_account_id_is_textfield_and_editable")

            hardware_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_search_page, url)

            self.log.info("Opening the hardware search page")
            self.open_hardware_search_page(hardware_search_url, environment)

            self.log.info("Checking the hardware search page's account id textbox status")
            account_id_txt_field = self.account_id_txt_field_status()

            self.log.info(f"is account id txt field editable {account_id_txt_field}")
            assert account_id_txt_field, "account id txt field editable is not editable"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.hardwaresearch
    @pytest.mark.php8_1
    def test_chassis_scip_id_is_textfield_and_editable(self, setup):
        """
            Test Case ID: TC_UI_VSI_HS_0021
            Jira ID     : r25447999
            Objective   : Verify that chassis scip id is an editable field

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - chassis scip id is an editable field

        """
        tc_id = setup.get("test_chassis_scip_id_is_textfield_and_editable", None)
        hardware_search_url = setup.get("hardware_search_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that account id is an editable field")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_chassis_scip_id_is_textfield_and_editable")

            hardware_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_search_page, url)

            self.log.info("Opening the hardware search page")
            self.open_hardware_search_page(hardware_search_url, environment)

            self.log.info("Checking the hardware search page's chassis scip id textbox status")
            chassis_scip_id_txt_field = self.chassis_scip_id_txt_field_status()

            self.log.info(f"is chassis scip id txt field editable {chassis_scip_id_txt_field}")
            assert chassis_scip_id_txt_field, "chassis scip id txt field editable is not editable"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.hardwaresearch
    @pytest.mark.php8_1
    def test_hardware_component_model_scip_id_is_textfield_and_editable(self, setup):
        """
            Test Case ID: TC_UI_VSI_HS_0022
            Jira ID     : r25448000
            Objective   : Verify that Hardware Component Model SCIP ID is an editable field

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            -  Hardware Component Model SCIP ID is an editable field

        """
        tc_id = setup.get("test_hardware_component_model_scip_id_is_textfield_and_editable", None)
        hardware_search_url = setup.get("hardware_search_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that Hardware Component Model SCIP ID is an editable field")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_hardware_component_model_scip_id_is_textfield_and_editable")

            hardware_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_search_page, url)

            self.log.info("Opening the hardware search page")
            self.open_hardware_search_page(hardware_search_url, environment)

            self.log.info("Checking the hardware search page's hardware component model scip id textbox status")
            hardware_component_model_scip_id_txt_field = self.hardware_component_model_scip_id_txt_field_status()

            self.log.info(
                f"is hardware component model scip id txt field editable {hardware_component_model_scip_id_txt_field}")
            assert hardware_component_model_scip_id_txt_field, "hardware component model scip id txt field editable is not editable"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.hardwaresearch
    @pytest.mark.php8_1
    def test_mac_ipv4_ipv6_is_textfield_and_editable(self, setup):
        """
            Test Case ID: TC_UI_VSI_HS_0022
            Jira ID     : r25448001
            Objective   : Verify that MAC/IPv4/IPv6  is an editable field

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            -  MAC/IPv4/IPv6  is an editable field

        """
        tc_id = setup.get("test_mac_ipv4_ipv6_is_textfield_and_editable", None)
        hardware_search_url = setup.get("hardware_search_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that MAC/IPv4/IPv6  is an editable field")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_mac_ipv4_ipv6_is_textfield_and_editable")

            hardware_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_search_page, url)

            self.log.info("Opening the hardware search page")
            self.open_hardware_search_page(hardware_search_url, environment)

            self.log.info("Checking the hardware search page's MAC/IPv4/IPv6 textbox status")
            mac_ipv4_ipv6_txt_field = self.mac_ipv4_ipv6_txt_field_status()

            self.log.info(
                f"is MAC/IPv4/IPv6  field editable {mac_ipv4_ipv6_txt_field}")
            assert mac_ipv4_ipv6_txt_field, "MAC/IPv4/IPv6  txt field editable is not editable"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.hardwaresearch
    @pytest.mark.php8_1
    def test_internal_notes_is_textfield_and_editable(self, setup):
        """
            Test Case ID: TC_UI_VSI_HS_0024
            Jira ID     : r25448002
            Objective   : Verify that internal notes  is an editable field

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            -  internal notes is an editable field

        """
        tc_id = setup.get("test_internal_notes_is_textfield_and_editable", None)
        hardware_search_url = setup.get("hardware_search_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that internal notes  is an editable field")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_internal_notes_is_textfield_and_editable")

            hardware_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_search_page, url)

            self.log.info("Opening the hardware search page")
            self.open_hardware_search_page(hardware_search_url, environment)

            self.log.info("Checking the hardware search page's internal notes textbox status")
            internal_notes_field = self.internal_notes_txt_field_status()

            self.log.info(
                f"is internal notes  field editable {internal_notes_field}")
            assert internal_notes_field, "internal notes txt field editable is not editable"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")
            