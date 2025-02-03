import pytest
from selenium.common import TimeoutException
from tests.test_virtual_update_pool_page.test_virtual_update_pool_page_helper import TestVirtualUpdatePoolPageHelper
from tests.test_base import BaseTest
from utilities.read_json import read_and_parse_json
from utilities.read_properties import ReadConfig


class TestVirtualUpdatePoolPage(BaseTest, TestVirtualUpdatePoolPageHelper):
    base_url = ReadConfig.get_application_url()
    username = ReadConfig.get_application_username()
    password = ReadConfig.get_application_password()

    @pytest.fixture(scope="function")
    def setup(self, logger):
        self.log = logger
        self.log.info("Setting up the test data file for use in the test")
        return read_and_parse_json(
            'tests/test_virtual_update_pool_page/testdata/update_pool_page_testdata.json')

    @pytest.mark.updatepool
    def test_back_to_pool_link_redirects_to_correct_page(self, setup):
        """
            Test Case ID: TC_UI_VSI_PU_0001
            Jira ID     : r25094694
            Objective   : Verify that back to pool link redirect to host pool page

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - Verify that back to pool link redirect to host pool page
            - Verify that the table header of back to pool list page is "CloudLayer Compute Instance Host Pools"

        """
        tc_id = setup.get("tc_id_back_to_pool_link_redirects_to_correct_page", None)
        virtual_update_pool_url = setup.get("virtual_update_pool_url", None)
        environment = setup.get("environment", None)
        table_header_pool_host = setup.get("back_to_pool_list_table_header", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that back to pool link redirect to host pool page")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_back_to_pool_link_redirects_to_correct_page")

            update_pool_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, update_pool_page, url)

            self.log.info("Opening the update pool page")
            self.open_update_pool_page(virtual_update_pool_url, environment)

            self.log.info("Clicking on the back to pool list link")
            self.click_on_back_to_pool_list_link()

            self.log.info("Getting the table header from back to pool list page")
            content_from_page = self.extract_the_content_from_back_to_pool_list_page()
            assert content_from_page == table_header_pool_host, "Failed to redirect to back to pool list page"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.updatepool
    def test_pool_master_table_displays_proper_data(self, setup):
        """
            Test Case ID: TC_UI_VSI_PU_0002
            Jira ID     : r25094696
            Objective   : Verify that pool master table is displayed

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - Verify that pool master table is displayed
            - Verify the hardware present in pool master table

        """
        tc_id = setup.get("tc_id_pool_master_table_displays_proper_data", None)
        virtual_update_pool_url = setup.get("virtual_update_pool_url", None)
        environment = setup.get("environment", None)
        hardware = setup.get("pool_master_hardware", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that pool master table is displayed")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_pool_master_table_displays_proper_data")

            update_pool_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, update_pool_page, url)

            self.log.info("Opening the update pool page")
            self.open_update_pool_page(virtual_update_pool_url, environment)

            self.log.info("Check whether pool master table is displayed")
            self.check_for_pool_master_table()

            hardware_availability_in_pool_master_table = self.check_for_hardware_availability_in_pool_master_table(
                hardware)
            assert hardware_availability_in_pool_master_table, "pool master table is not display or table is empty"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.updatepool
    def test_name_field_is_enabled_and_editable(self, setup):
        """
            Test Case ID: TC_UI_VSI_PU_0003
            Jira ID     : r25094709
            Objective   : Verify that name field is enabled and editable

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - the name field should be enabled
            - the name field should be editable

        """
        tc_id = setup.get("tc_id_name_field_is_enabled_and_editable", None)
        virtual_update_pool_url = setup.get("virtual_update_pool_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that name field is enabled and editable")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_name_field_is_enabled_and_editable")

            update_pool_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, update_pool_page, url)

            self.log.info("Opening the update pool page")
            self.open_update_pool_page(virtual_update_pool_url, environment)

            name_editability = self.name_field_enabled_and_editable_check()
            assert name_editability, "name field is not enabled or editable"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.updatepool
    def test_description_field_is_enabled_and_editable(self, setup):
        """
            Test Case ID: TC_UI_VSI_PU_0004
            Jira ID     : r25150822
            Objective   : Verify that description field is enabled and editable

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - the description field should be enabled
            - the description field should be editable

        """
        tc_id = setup.get("test_description_field_is_enabled_and_editable", None)
        virtual_update_pool_url = setup.get("virtual_update_pool_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that description field is enabled and editable")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_description_field_is_enabled_and_editable")

            update_pool_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, update_pool_page, url)

            self.log.info("Opening the update pool page")
            self.open_update_pool_page(virtual_update_pool_url, environment)

            description_editability = self.description_field_enabled_and_editable_check()
            assert description_editability, "description field is not enabled or editable"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.updatepool
    def test_update_pool_button_is_displayed_and_editable(self, setup):
        """
            Test Case ID: TC_UI_VSI_PU_0005
            Jira ID     : r25150825
            Objective   : Verify that update pool button is displayed and clickable

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - the update pool button should be displayed
            - the update pool button is clickable

        """
        tc_id = setup.get("test_update_pool_button_is_displayed_and_editable", None)
        virtual_update_pool_url = setup.get("virtual_update_pool_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that update pool button is displayed and clickable")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_update_pool_button_is_displayed_and_editable")

            update_pool_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, update_pool_page, url)

            self.log.info("Opening the update pool page")
            self.open_update_pool_page(virtual_update_pool_url, environment)

            self.log.info("Checking whether update pool button is displayed and clickable")
            update_pool_button_status = self.check_whether_pool_button_is_displayed_and_clickable()

            assert update_pool_button_status, "Update pool button is not displayed and clickable"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.updatepool
    def test_host_reservation_field_is_displayed_and_editable(self, setup):
        """
            Test Case ID: TC_UI_VSI_PU_0007
            Jira ID     : r25170289
            Objective   : Verify that host reservation is displayed and editable

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - the host reservation should be displayed
            - the host reservation button is clickable

        """
        tc_id = setup.get("test_host_reservation_field_is_displayed_and_editable", None)
        virtual_update_pool_url = setup.get("virtual_update_pool_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that host reservation is displayed and editable")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_update_pool_button_is_displayed_and_editable")

            update_pool_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, update_pool_page, url)

            self.log.info("Opening the update pool page")
            self.open_update_pool_page(virtual_update_pool_url, environment)

            host_reservation_status = self.host_reservation_editability_and_display_check()
            self.log.info(f"is host reservation field editable and displayed? {host_reservation_status}")
            assert host_reservation_status, "host reservation field is not editable or not displayed"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.updatepool
    def test_pool_brand_is_a_dropdown(self, setup):
        """
            Test Case ID: TC_UI_VSI_PU_0006
            Jira ID     : r25244532
            Objective   : Verify that pool brand is a dropdown

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - pool brand is a dropdown

        """
        tc_id = setup.get("test_pool_brand_is_a_dropdown", None)
        virtual_update_pool_url = setup.get("virtual_update_pool_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that pool brand is a dropdown")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_pool_brand_is_a_dropdown_options_are_displayed_properly")

            update_pool_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, update_pool_page, url)

            self.log.info("Opening the update pool page")
            self.open_update_pool_page(virtual_update_pool_url, environment)

            self.log.info("Checking if pool brand is a dropdown...")
            pool_brand_status = self.pool_brand_tagname_check()
            assert pool_brand_status, "pool brand is not a dropdown"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.updatepool
    def test_pool_brand_options_are_displayed_correctly(self, setup):
        """
            Test Case ID: TC_UI_VSI_PU_0008
            Jira ID     : r25244533
            Objective   : Verify that pool brand options are displayed correctly

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - pool brand options are displayed correctly

        """
        tc_id = setup.get("test_pool_brand_options_are_displayed_correctly", None)
        virtual_update_pool_url = setup.get("virtual_update_pool_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that pool brand options are displayed correctly")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_pool_brand_options_are_displayed_correctly")

            update_pool_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, update_pool_page, url)

            self.log.info("Opening the update pool page")
            self.open_update_pool_page(virtual_update_pool_url, environment)

            self.log.info("Checking if pool brand options are displayed properly...")
            display_status = self.pool_brand_options_display_status()
            assert display_status!=0,"pool brand options are displayed properly"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.updatepool
    def test_preferred_os_is_a_dropdown(self, setup):
        """
            Test Case ID: TC_UI_VSI_PU_0009
            Jira ID     : r25244534
            Objective   : Verify that Preferred os is a dropdown

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - preferred os is a dropdown

        """
        tc_id = setup.get("test_preferred_os_is_a_dropdown", None)
        virtual_update_pool_url = setup.get("virtual_update_pool_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that Preferred os is a dropdown")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_preferred_os_is_a_dropdown")

            update_pool_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, update_pool_page, url)

            self.log.info("Opening the update pool page")
            self.open_update_pool_page(virtual_update_pool_url, environment)

            self.log.info("Checking if pool brand is a dropdown...")
            preferred_os_status = self.preferred_os_tagname_check()
            assert preferred_os_status, "pool brand is not a dropdown"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.updatepool
    def test_reload_os_is_a_dropdown(self, setup):
        """
            Test Case ID: TC_UI_VSI_PU_0010
            Jira ID     : r25244535
            Objective   : Verify that reload os is a dropdown

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - reload os is a dropdown

        """
        tc_id = setup.get("test_reload_os_is_a_dropdown", None)
        virtual_update_pool_url = setup.get("virtual_update_pool_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that reload os is a dropdown")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_reload_os_is_a_dropdown")

            update_pool_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, update_pool_page, url)

            self.log.info("Opening the update pool page")
            self.open_update_pool_page(virtual_update_pool_url, environment)

            self.log.info("Checking if pool brand is a dropdown...")
            reload_os_status = self.reload_os_tagname_check()

            self.log.info(f"is reload os a dropdown? {reload_os_status}")
            assert reload_os_status, "pool brand is not a dropdown"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.updatepool
    def test_preferred_os_options_are_displayed_correctly(self, setup):
        """
            Test Case ID: TC_UI_VSI_PU_0011
            Jira ID     : r25244537
            Objective   : Verify that preferred os options are displayed correctly

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - preferred os options are displayed correctly

        """
        tc_id = setup.get("test_preferred_os_options_are_displayed_correctly", None)
        virtual_update_pool_url = setup.get("virtual_update_pool_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that preferred os options are displayed correctly")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_preferred_os_options_are_displayed_correctly")

            update_pool_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, update_pool_page, url)

            self.log.info("Opening the update pool page")
            self.open_update_pool_page(virtual_update_pool_url, environment)

            self.log.info("Checking if preferred os options are displayed properly...")
            display_status = self.preferred_os_options_display_status()
            assert display_status != 0, "pool brand options are displayed properly"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.updatepool
    def test_reload_os_options_are_displayed_correctly(self, setup):
        """
            Test Case ID: TC_UI_VSI_PU_0012
            Jira ID     : r25244538
            Objective   : Verify that reload os options are displayed correctly

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - preferred os options are displayed correctly

        """
        tc_id = setup.get("test_reload_os_options_are_displayed_correctly", None)
        virtual_update_pool_url = setup.get("virtual_update_pool_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that reload os options are displayed correctly")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_reload_os_options_are_displayed_correctly")

            update_pool_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, update_pool_page, url)

            self.log.info("Opening the update pool page")
            self.open_update_pool_page(virtual_update_pool_url, environment)

            self.log.info("Checking if reload os options are displayed properly...")
            display_status = self.reload_os_options_display_status()
            assert display_status != 0, "pool brand options are displayed properly"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.updatepool
    def test_pool_type_is_a_dropdown(self, setup):
        """
            Test Case ID: TC_UI_VSI_PU_0013
            Jira ID     : r25282445
            Objective   : Verify that pool type is a dropdown

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - pool type is a dropdown

        """
        tc_id = setup.get("test_pool_type_is_a_dropdown", None)
        virtual_update_pool_url = setup.get("virtual_update_pool_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that pool type is a dropdown")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_pool_type_is_a_dropdown")

            update_pool_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, update_pool_page, url)

            self.log.info("Opening the update pool page")
            self.open_update_pool_page(virtual_update_pool_url, environment)

            self.log.info("Checking if pool type is a dropdown...")
            pool_type_status = self.pool_type_dropdown_check()

            self.log.info(f"is pool type a dropdown? {pool_type_status}")
            assert pool_type_status, "pool brand is not a dropdown"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.updatepool
    def test_pool_type_dropdown_displays_correct_values(self, setup):
        """
            Test Case ID: TC_UI_VSI_PU_0014
            Jira ID     : r25282446
            Objective   : Verify that pool type dropdown displays correct value

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - pool type dropdown options are
                - Hypervisor Pool
                - Portal Pool
                - Standard Pool
                - OpenStack Pool
                - Internal Pool
                - Genesis Pool

        """
        tc_id = setup.get("test_pool_type_dropdown_displays_correct_values", None)
        virtual_update_pool_url = setup.get("virtual_update_pool_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that pool type is a dropdown")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_pool_type_dropdown_displays_correct_values")

            update_pool_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, update_pool_page, url)

            self.log.info("Opening the update pool page")
            self.open_update_pool_page(virtual_update_pool_url, environment)

            self.log.info("Getting pool type dropdown options")
            pool_type_options = self.get_pool_type_dropdown_options()

            self.log.info(f"pool type options list:  {pool_type_options}")
            assert pool_type_options is not None, "pool type options are not displayed properly"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.updatepool
    def test_host_reservation_is_enabled_and_editable(self, setup):
        """
            Test Case ID: TC_UI_VSI_PU_0015
            Jira ID     : r25282447
            Objective   : Verify that host reservation field is enabled and editable

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - the host reservation field should be enabled
            - the host reservation field should be editable

        """
        tc_id = setup.get("test_host_reservation_is_enabled_and_editable", None)
        virtual_update_pool_url = setup.get("virtual_update_pool_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that host reservation field is enabled and editable")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_host_reservation_is_enabled_and_editable")

            update_pool_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, update_pool_page, url)

            self.log.info("Opening the update pool page")
            self.open_update_pool_page(virtual_update_pool_url, environment)

            host_reservation_editable = self.host_reservation_enable_and_editable_check()
            self.log.info(f"is host reservation editable {host_reservation_editable}")
            assert host_reservation_editable, "host reservation is not enabled or editable"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.updatepool
    def test_transient_cpu_limit_is_enabled_and_editable(self, setup):
        """
            Test Case ID: TC_UI_VSI_PU_0016
            Jira ID     : r25282449
            Objective   : Verify that transient cpu limit field is enabled and editable

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - the transient cpu limit field should be enabled
            - the transient cpu limit field should be editable

        """
        tc_id = setup.get("test_transient_cpu_limit_is_enabled_and_editable", None)
        virtual_update_pool_url = setup.get("virtual_update_pool_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that transient cpu limit field is enabled and editable")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_transient_cpu_limit_is_enabled_and_editable")

            update_pool_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, update_pool_page, url)

            self.log.info("Opening the update pool page")
            self.open_update_pool_page(virtual_update_pool_url, environment)

            transient_cpu_limit_editable = self.transient_cpu_limit_enable_and_editable_check()
            self.log.info(f"is transient cpu limit editable {transient_cpu_limit_editable}")
            assert transient_cpu_limit_editable, "transient cpu is not enabled or editable"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.updatepool
    def test_auto_migrate_pool_limit_is_enabled_and_editable(self, setup):
        """
            Test Case ID: TC_UI_VSI_PU_0017
            Jira ID     : r25282450
            Objective   : Verify that auto migrate pool limit field is enabled and editable

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - auto migrate pool limit field should be enabled
            - auto migrate pool limit field should be editable

        """
        tc_id = setup.get("test_auto_migrate_pool_limit_is_enabled_and_editable", None)
        virtual_update_pool_url = setup.get("virtual_update_pool_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that auto migrate pool limit field is enabled and editable")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_auto_migrate_pool_limit_is_enabled_and_editable")

            update_pool_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, update_pool_page, url)

            self.log.info("Opening the update pool page")
            self.open_update_pool_page(virtual_update_pool_url, environment)

            auto_migrate_pool_limit_editable = self.auto_migrate_pool_limit_enable_and_editable_check()
            self.log.info(f"is auto migrate pool limit editable {auto_migrate_pool_limit_editable}")
            assert auto_migrate_pool_limit_editable, "auto migrate pool limit is not enabled or editable"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.updatepool
    def test_only_use_hosts_with_preferred_os_is_a_checkout_and_enabled(self, setup):
        """
            Test Case ID: TC_UI_VSI_PU_0018
            Jira ID     : r25282451
            Objective   : Verify that only use hosts with preferred os field is a checkbox and enabled

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - only use hosts with preferred os field is a checkbox
            - only use hosts with preferred os field is enabled

        """
        tc_id = setup.get("test_only_use_hosts_with_preferred_os_is_a_checkout_and_enabled", None)
        virtual_update_pool_url = setup.get("virtual_update_pool_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that only use hosts with preferred os field is a checkbox and enabled")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_only_use_hosts_with_preferred_os_is_a_checkout_and_enabled")

            update_pool_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, update_pool_page, url)

            self.log.info("Opening the update pool page")
            self.open_update_pool_page(virtual_update_pool_url, environment)

            self.log.info("Verifying if use hosts with preferred os is a checkbox and enabled...")
            use_host_with_preferred_os = self.use_host_with_preferred_os_input_type_and_enable_check()

            self.log.info(f"is use host with preferred os checkbox and enabled: {use_host_with_preferred_os}")
            assert use_host_with_preferred_os, "use host with preferred os is not a checkbox or not enabled"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.updatepool
    def test_enable_hosts_after_reload_is_a_checkout_and_enabled(self, setup):
        """
            Test Case ID: TC_UI_VSI_PU_0019
            Jira ID     : r25282452
            Objective   : Verify that enable hosts after reload field is a checkbox and enabled

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - enable hosts after reload field is a checkbox
            - enable hosts after reload field is enabled

        """
        tc_id = setup.get("test_enable_hosts_after_reload_is_a_checkout_and_enabled", None)
        virtual_update_pool_url = setup.get("virtual_update_pool_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that enable hosts after reload field is a checkbox and enabled")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_enable_hosts_after_reload_is_a_checkout_and_enabled")

            update_pool_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, update_pool_page, url)

            self.log.info("Opening the update pool page")
            self.open_update_pool_page(virtual_update_pool_url, environment)

            self.log.info("Verifying if enable hosts after reload is a checkbox and enabled")
            enable_hosts_after_reload = self.enable_host_after_reload_input_type_and_enable_check()

            self.log.info(f"is enable hosts after reload checkbox and enabled: {enable_hosts_after_reload}")
            assert enable_hosts_after_reload, "enable hosts after reload is not a checkbox or not enabled"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.updatepool
    def test_vlan_provisions_allowed_is_a_checkout_and_enabled(self, setup):
        """
            Test Case ID: TC_UI_VSI_PU_0020
            Jira ID     : r25282455
            Objective   : Verify that vlan provisions allowed field is a checkbox and enabled

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - vlan provisions allowed field is a checkbox
            - vlan provisions allowed field is enabled

        """
        tc_id = setup.get("test_vlan_provisions_allowed_is_a_checkout_and_enabled", None)
        virtual_update_pool_url = setup.get("virtual_update_pool_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that vlan provisions allowed field is a checkbox and enabled")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_vlan_provisions_allowed_is_a_checkout_and_enabled")

            update_pool_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, update_pool_page, url)

            self.log.info("Opening the update pool page")
            self.open_update_pool_page(virtual_update_pool_url, environment)

            self.log.info("Verifying if vlan provisions allowed  is a checkbox and enabled")
            vlan_provisions_allowed = self.vlan_provisions_allowed_input_type_and_enable_check()

            self.log.info(f"is vlan provisions allowed  checkbox and enabled: {vlan_provisions_allowed}")
            assert vlan_provisions_allowed, "vlan provisions allowed  is not a checkbox or not enabled"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.updatepool
    def test_disable_host_auto_migration_is_a_checkout_and_enabled(self, setup):
        """
            Test Case ID: TC_UI_VSI_PU_0021
            Jira ID     : r25282457
            Objective   : Verify that disable host auto migration field is a checkbox and enabled

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - disable host auto migration field is a checkbox
            - disable host auto migration field is enabled

        """
        tc_id = setup.get("test_disable_host_auto_migration_is_a_checkout_and_enabled", None)
        virtual_update_pool_url = setup.get("virtual_update_pool_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that disable host auto migration field is a checkbox and enabled")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_disable_host_auto_migration_is_a_checkout_and_enabled")

            update_pool_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, update_pool_page, url)

            self.log.info("Opening the update pool page")
            self.open_update_pool_page(virtual_update_pool_url, environment)

            self.log.info("Verifying if disable host auto migration is a checkbox and enabled")
            disable_host_auto_migration = self.disable_host_auto_migration_input_type_and_enable_check()

            self.log.info(f"is disable host auto migration checkbox and enabled: {disable_host_auto_migration}")
            assert disable_host_auto_migration, "disable host auto migration is not a checkbox or not enabled"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.updatepool
    def test_pool_roles_field_contains_6_checkbox_to_select(self, setup):
        """
            Test Case ID: TC_UI_VSI_PU_0022
            Jira ID     : r25282462
            Objective   : Verify that pool roles contains 6 checkbox

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - pool roles 6 checkboxes name
                - Local Pool
                - SAN Pool
                - Utility Pool
                - Customer Pool
                - GPU Pool
                - VPC

        """
        tc_id = setup.get("test_pool_roles_field_contains_6_checkbox_to_select", None)
        virtual_update_pool_url = setup.get("virtual_update_pool_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that pool roles contains 6 checkbox")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_pool_roles_field_contains_6_checkbox_to_select")

            update_pool_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, update_pool_page, url)

            self.log.info("Opening the update pool page")
            self.open_update_pool_page(virtual_update_pool_url, environment)

            self.log.info("Verifying no. of pool roles possible values...")
            pool_roles = self.verify_check_boxes_name_for_pool_roles()

            self.log.info(f"is pool roles possible values are : {pool_roles}")
            assert pool_roles == 6, "no. of pool roles possible values are not 6"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")
