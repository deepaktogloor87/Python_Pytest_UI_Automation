import time
import pytest
from selenium.common import TimeoutException
from tests.test_hardware_update_page.test_hardware_update_page_helper import TestHardwareUpdatePageHelper
from tests.test_base import BaseTest
from utilities.read_json import read_and_parse_json
from utilities.read_properties import ReadConfig


class TestHardwareUpdatePage(BaseTest, TestHardwareUpdatePageHelper):
    base_url = ReadConfig.get_application_url()
    username = ReadConfig.get_application_username()
    password = ReadConfig.get_application_password()

    @pytest.fixture(scope="function")
    def setup(self, logger):
        self.log = logger
        self.log.info("Setting up the test data file for use in the test")
        return read_and_parse_json(
            'tests/test_hardware_update_page/testdata/hardware_update_page_testdata.json')

    @pytest.mark.hardwareupdate
    @pytest.mark.php8_1
    def test_storage_group_sn_is_displayed_and_editable_for_jbod_c(self, setup):
        """
            Test Case ID: TC_UI_HU_0001
            Jira ID     : r25353534
            Objective   : Verify that storage group serial number is displayed and editable

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            -  Storage group serial number is displayed and editable

        """
        tc_id = setup.get("tc_id_storage_group_sn_is_displayed_and_editable_jbod_c", None)
        hardware_update_url = setup.get("hardware_update_url", None)
        hardware_id = setup.get("hardware_id", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that storage group serial number is displayed and editable")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_storage_group_sn_is_displayed_and_editable_jbod_c")

            update_pool_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, update_pool_page, url)

            self.log.info("Opening the hardware update page")
            self.open_hardware_update_page(hardware_update_url, hardware_id, environment)

            display_status = self.check_if_ssn_is_displayed()
            assert display_status, "ssn is not displayed"

            editable_status = self.check_if_ssn_is_editable()
            assert editable_status, "ssn is not editable"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.hardwareupdate
    @pytest.mark.php8_1
    def test_storage_group_wwn_is_displayed_and_editable_for_jbod_c(self, setup):
        """
            Test Case ID: TC_UI_HU_0002
            Jira ID     : r25353534
            Objective   : Verify that storage group world wide number is displayed and editable

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            -  Storage group serial number is displayed and editable

        """
        tc_id = setup.get("tc_id_storage_group_wwn_is_displayed_and_editable_for_jbod_cc", None)
        hardware_update_url = setup.get("hardware_update_url", None)
        hardware_id = setup.get("hardware_id", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: verify that storage group world wide number is displayed and editable")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_storage_group_wwn_is_displayed_and_editable_for_jbod_c")

            update_pool_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, update_pool_page, url)

            self.log.info("Opening the hardware update page")
            self.open_hardware_update_page(hardware_update_url, hardware_id, environment)

            display_status = self.check_if_wwn_is_displayed()
            assert display_status, "world wide number is not displayed"

            editable_status = self.check_if_wwn_is_editable()
            assert editable_status, "world wide number  is not editable"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.hardwareupdate
    @pytest.mark.php8_1
    def test_maintenance_notes_can_be_updated_successfully(self, setup):
        """
            Test Case ID: TC_UI_HU_0003
            Jira ID     : r25353534
            Objective   : Verify that maintenance notes can be updated

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            -  maintenance notes can be updated

        """
        tc_id = setup.get("tc_id_maintenance_notes_can_be_updated_successfully", None)
        hardware_update_url = setup.get("hardware_update_url", None)
        hardware_id = setup.get("hardware_id_test_03", None)
        maintenance_notes = setup.get("maintenance_notes", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: verify that maintenance notes can be updated")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_maintenance_notes_can_be_updated_successfully")

            update_pool_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, update_pool_page, url)

            self.log.info("Opening the hardware update page")
            self.open_hardware_update_page(hardware_update_url, hardware_id, environment)

            self.write_maintenance_notes(maintenance_notes)
            if_present = self.check_if_maintenance_notes_present()
            assert if_present == "Other", "Not able to update the maintenance notes"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.hardwareupdate
    @pytest.mark.php8_1
    def test_remote_management_control_link_is_present_for_redfish_enabled_hardware(self, setup):
        """
            Test Case ID: TC_UI_HU_0004
            Jira ID     : r25353534
            Objective   : Verify that remote management control link is present for redfish enabled server

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Hardware/update/3448722

            Expected Outcome:
            -  remote management control link is present for redfish enabled server

        """
        tc_id = setup.get("tc_id_remote_management_control_link_is_present_for_redfish_enabled_hardware", None)
        hardware_update_url = setup.get("hardware_update_url", None)
        redfish_enabled_server = setup.get("redfish_enabled_server", None)
        environment = "metal-6019"
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: verify that remote management control link is present for redfish enabled server")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_remote_management_control_link_is_present_for_redfish_enabled_hardware")

            update_pool_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, update_pool_page, url)

            self.log.info("Opening the hardware update page")
            self.open_hardware_update_page(hardware_update_url, redfish_enabled_server, environment)

            self.log.info(f"checking if remote management control link is present on {redfish_enabled_server}")
            is_present = self.check_presence_of_remote_management_link()
            self.log.info(f"remote management control link present?? {is_present}")

            assert is_present, "Remote management control link is not present"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.hardwareupdate
    @pytest.mark.php8_1
    def test_there_are_2_tabs_for_redfish_enabled_server(self, setup):
        """
            Test Case ID: TC_UI_HU_0005
            Jira ID     : r25353534
            Objective   : Verify that there are 2 tabs for redfish enabled server

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Hardware/update/3448722

            Expected Outcome:
            -  Verify that there are 2 tabs for redfish enabled server

        """
        tc_id = setup.get("tc_id_there_are_2_tabs_for_redfish_enabled_server", None)
        hardware_update_url = setup.get("hardware_update_url", None)
        redfish_enabled_server = setup.get("redfish_enabled_server", None)
        environment = "metal-6019"
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: verify that maintenance notes can be updated")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_remote_management_control_link_is_present_for_redfish_enabled_hardware")

            update_pool_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, update_pool_page, url)

            self.log.info("Opening the hardware update page")
            self.open_hardware_update_page(hardware_update_url, redfish_enabled_server, environment)

            self.log.info(f"checking if there are 2 tabs on {redfish_enabled_server}")
            self.click_on_remote_management_link()
            is_present = self.check_if_2_tabs_are_present()

            self.log.info(f"are 2 tabs present on remote management control page: {is_present}")
            assert is_present, "2 tabs are present on redfish enabled server"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.hardwareupdate
    @pytest.mark.php8_1
    @pytest.mark.staging_only
    def test_redfish_server_can_be_powered_off_successfully(self, setup):
        """
            Test Case ID: TC_UI_HU_0006
            Jira ID     : r25353534
            Objective   : Verify that redfish server can be powered off successfully

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Hardware/update/3448722

            Expected Outcome:
            -  Verify that redfish server can be powered off successfully

        """
        tc_id = setup.get("tc_id_redfish_server_can_be_powered_off_successfully", None)
        hardware_update_url = setup.get("hardware_update_url", None)
        redfish_enabled_server = setup.get("redfish_enabled_server", None)
        environment = "metal-6019"
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: verify that redfish server can be powered off successfully")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_redfish_server_can_be_powered_off_successfully")

            update_pool_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, update_pool_page, url)

            self.log.info("Opening the hardware update page")
            self.open_hardware_update_page(hardware_update_url, redfish_enabled_server, environment)

            self.log.info(f"clicking on remote control management link")
            self.click_on_remote_management_link()
            self.log.info(f"clicking on redfish remote control management summary tab")
            self.click_on_redfish_remote_management_summary()

            self.log.info("selecting power off option from checkbox")
            answer = self.select_power_off_option_from_dropdown()
            assert answer.__contains__("Power Status: on"), "Redfish server is not power off"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.hardwareupdate
    @pytest.mark.php8_1
    @pytest.mark.staging_only
    def test_redfish_server_can_be_powered_on_successfully(self, setup):
        """
            Test Case ID: TC_UI_HU_0007
            Jira ID     : r25353534
            Objective   : Verify that redfish server can be powered on successfully

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Hardware/update/3448722

            Expected Outcome:
            -  Verify that redfish server can be powered on successfully

        """
        tc_id = setup.get("tc_id_redfish_server_can_be_powered_on_successfully", None)
        hardware_update_url = setup.get("hardware_update_url", None)
        redfish_enabled_server = setup.get("redfish_enabled_server", None)
        environment = "metal-6019"
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: verify that redfish server can be powered on successfully")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_redfish_server_can_be_powered_on_successfully")

            update_pool_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, update_pool_page, url)

            self.log.info("Opening the hardware update page")
            self.open_hardware_update_page(hardware_update_url, redfish_enabled_server, environment)

            self.log.info(f"clicking on remote control management link")
            self.click_on_remote_management_link()
            self.log.info(f"clicking on redfish remote control management summary tab")
            self.click_on_redfish_remote_management_summary()

            self.log.info("selecting power off option from checkbox")
            answer = self.select_power_on_option_from_dropdown()
            assert answer.__contains__("Power Status: on"), "Redfish server is not power off"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.IO_Regression
    def test_uim_managed_flag_can_be_set_to_yes_vpcng_successfully(self, setup):
        """
            Test Case ID: TC_UI_HU_0008
            Jira ID     : r25353534
            Objective   : verify that uim managed flag can be set to yes-vpcng

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               http://stable.internal.qadal0901.softlayer.local/Hardware/update/1333199

            Expected Outcome:
            -  uim managed flag is set to yes-vpcng

        """
        tc_id = setup.get("tc_id_uim_managed_flag_can_be_set_to_yes_vpcng_successfully", None)
        hardware_update_url = setup.get("hardware_update_url", None)
        hardware_id = setup.get("test08_hardware", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: verify that uim managed flag can be set to yes-vpcng")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_uim_managed_flag_can_be_set_to_yes_vpcng_successfully")

            update_pool_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, update_pool_page, url)

            self.log.info("Opening the hardware update page")
            self.open_hardware_update_page(hardware_update_url, hardware_id, environment)

            self.log.info("select vpcng from the dropdowm")
            self.select_yes_vpcng_option_from_uim_managed_asset_dropdown()

            self.log.info("click on the continue button")
            uim_managed_asset_value = self.check_if_changes_are_saved_successfully()

            self.log.info(f"uim managed asset value set is {uim_managed_asset_value}")
            assert uim_managed_asset_value == "vpcng", "uim managed flag can be set to yes-vpcng"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.IO_Regression
    def test_uim_managed_flag_can_be_set_to_undercloud_successfully(self, setup):
        """
            Test Case ID: TC_UI_HU_0009
            Jira ID     : r25353534
            Objective   : verify that uim managed flag can be set to undercloud

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               http://stable.internal.qadal0901.softlayer.local/Hardware/update/1333199

            Expected Outcome:
            -   uim managed flag is set to undercloud

        """
        tc_id = setup.get("tc_id_uim_managed_flag_can_be_set_to_undercloud_successfully", None)
        hardware_update_url = setup.get("hardware_update_url", None)
        hardware_id = setup.get("test08_hardware", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: verify that uim managed flag can be set to undercloud")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_uim_managed_flag_can_be_set_to_undercloud_successfully")

            update_pool_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, update_pool_page, url)

            self.log.info("Opening the hardware update page")
            self.open_hardware_update_page(hardware_update_url, hardware_id, environment)

            self.log.info("select undercloud from the dropdowm")
            self.select_undercloud_option_from_uim_managed_asset_dropdown()

            self.log.info("click on the continue button")
            uim_managed_asset_value = self.check_if_changes_are_saved_successfully()

            self.log.info(f"uim managed asset value set is {uim_managed_asset_value}")
            assert uim_managed_asset_value == "undercloud", "uim managed flag can be set to undercloud"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.IO_Regression
    def test_uim_managed_flag_can_be_set_to_fedramp_successfully(self, setup):
        """
            Test Case ID: TC_UI_HU_0010
            Jira ID     : r25353534
            Objective   : verify that uim managed flag can be set to fedramp

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               http://stable.internal.qadal0901.softlayer.local/Hardware/update/1333199

            Expected Outcome:
            -   uim managed flag is set to fedramp

        """
        tc_id = setup.get("tc_id_uim_managed_flag_can_be_set_to_fedramp_successfully", None)
        hardware_update_url = setup.get("hardware_update_url", None)
        hardware_id = setup.get("test08_hardware", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: verify that uim managed flag can be set to fedramp")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_uim_managed_flag_can_be_set_to_fedramp_successfully")

            update_pool_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, update_pool_page, url)

            self.log.info("Opening the hardware update page")
            self.open_hardware_update_page(hardware_update_url, hardware_id, environment)

            self.log.info("select fedramp from the dropdowm")
            self.select_fedramp_option_from_uim_managed_asset_dropdown()

            self.log.info("click on the continue button")
            uim_managed_asset_value = self.check_if_changes_are_saved_successfully()

            self.log.info(f"uim managed asset value set is {uim_managed_asset_value}")
            assert uim_managed_asset_value == "fedramp", "uim managed flag can be set to fedramp"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.IO_Regression
    def test_uim_managed_flag_can_be_set_to_no_successfully(self, setup):
        """
            Test Case ID: TC_UI_HU_0011
            Jira ID     : r25353534
            Objective   : verify that uim managed flag can be set to no

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               http://stable.internal.qadal0901.softlayer.local/Hardware/update/1333199

            Expected Outcome:
            -   uim managed flag is set to no

        """
        tc_id = setup.get("tc_id_uim_managed_flag_can_be_set_to_no_successfully", None)
        hardware_update_url = setup.get("hardware_update_url", None)
        hardware_id = setup.get("test08_hardware", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: verify that uim managed flag can be set to fedramp")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_uim_managed_flag_can_be_set_to_no_successfully")

            update_pool_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, update_pool_page, url)

            self.log.info("Opening the hardware update page")
            self.open_hardware_update_page(hardware_update_url, hardware_id, environment)

            self.log.info("select no from the dropdowm")
            self.select_no_option_from_uim_managed_asset_dropdown()

            self.log.info("click on the continue button")
            uim_managed_asset_value = self.check_if_changes_are_saved_successfully()

            self.log.info(f"uim managed asset value set is {uim_managed_asset_value}")
            assert uim_managed_asset_value == "classic", "uim managed flag can be set to no"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")
