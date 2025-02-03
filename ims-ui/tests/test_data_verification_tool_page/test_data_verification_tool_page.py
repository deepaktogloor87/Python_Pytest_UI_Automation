import pytest
from selenium.common import TimeoutException
from tests.test_data_verification_tool_page.test_data_verification_tool_helper import TestDataVerificationToolPageHelper
from tests.test_base import BaseTest
from utilities.read_json import read_and_parse_json
from utilities.read_properties import ReadConfig


class TestDataVerificationToolPage(BaseTest, TestDataVerificationToolPageHelper):
    base_url = ReadConfig.get_application_url()
    username = ReadConfig.get_application_username()
    password = ReadConfig.get_application_password()

    @pytest.fixture(scope="function")
    def setup(self, logger):
        self.log = logger
        self.log.info("Setting up the test data file for use in the test")
        return read_and_parse_json(
            'tests/test_data_verification_tool_page/testdata/data_verification_tool_page_testdata.json')

    @pytest.mark.dataverificationtool
    @pytest.mark.php8_1
    def test_run_address_test_button_is_displayed(self, setup):
        """
            Test Case ID: TC_UI_VSI_DVT_0001
            Jira ID     : r25282493
            Objective   : Verify run address test button is displayed

            Precondition:
            - User have access to IMS qa environment

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/chooseHostEvacuationType/1455135

            Expected Outcome:
            - run address test button is displayed

        """
        tc_id = setup.get("test_run_address_test_button_is_displayed", None)
        dvt_url = setup.get("data_verification_tool_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify run address test button is displayed")
            self.log.info("Precondition: User has access to IMS qa environment.")
            self.log.info(
                "Starting test: test_run_address_test_button_is_displayed")

            data_verification_tool_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login.")
            self.login_to_app(self.driver, self.username, self.password, data_verification_tool_page, url)

            self.log.info("Opening the host evacuation ticket url")
            self.open_data_verification_tool_page(dvt_url, environment)

            self.log.info("Checking if run address test button is displayed and enabled")
            run_address_test = self.run_address_test_button_display_check()

            self.log.info(f"is run address test displayed: {run_address_test}")
            assert run_address_test, "run address test button is not displayed"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.dataverificationtool
    @pytest.mark.php8_1
    def test_run_location_test_button_is_displayed(self, setup):
        """
            Test Case ID: TC_UI_VSI_DVT_0002
            Jira ID     : r25282502
            Objective   : Verify run location test button is displayed

            Precondition:
            - User have access to IMS qa environment

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/chooseHostEvacuationType/1455135

            Expected Outcome:
            - run location test button is displayed

        """
        tc_id = setup.get("test_run_location_test_button_is_displayed", None)
        dvt_url = setup.get("data_verification_tool_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify run location test button is displayed")
            self.log.info("Precondition: User has access to IMS qa environment.")
            self.log.info(
                "Starting test: test_run_location_test_button_is_displayed")

            data_verification_tool_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login.")
            self.login_to_app(self.driver, self.username, self.password, data_verification_tool_page, url)

            self.log.info("Opening the host evacuation ticket url")
            self.open_data_verification_tool_page(dvt_url, environment)

            self.log.info("Checking if run location test button is displayed and enabled")
            run_location_test = self.run_location_test_button_display_check()

            self.log.info(f"is run address test displayed: {run_location_test}")
            assert run_location_test, "run location test button is not displayed"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.dataverificationtool
    @pytest.mark.php8_1
    def test_run_pools_test_button_is_displayed(self, setup):
        """
            Test Case ID: TC_UI_VSI_DVT_0003
            Jira ID     : r25282505
            Objective   : Verify run pools test button is displayed

            Precondition:
            - User have access to IMS qa environment

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/chooseHostEvacuationType/1455135

            Expected Outcome:
            - run pools test button is displayed

        """
        tc_id = setup.get("test_run_pools_test_button_is_displayed", None)
        dvt_url = setup.get("data_verification_tool_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify run pools test button is displayed")
            self.log.info("Precondition: User has access to IMS qa environment.")
            self.log.info(
                "Starting test: test_run_pools_test_button_is_displayed")

            data_verification_tool_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login.")
            self.login_to_app(self.driver, self.username, self.password, data_verification_tool_page, url)

            self.log.info("Opening the host evacuation ticket url")
            self.open_data_verification_tool_page(dvt_url, environment)

            self.log.info("Checking if run pools test button is displayed and enabled")
            run_pools_test = self.run_pools_test_button_display_check()

            self.log.info(f"is run address test displayed: {run_pools_test}")
            assert run_pools_test, "run pools test button is not displayed"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.dataverificationtool
    @pytest.mark.php8_1
    def test_run_pools_test_button_is_displayed(self, setup):
        """
            Test Case ID: TC_UI_VSI_DVT_0003
            Jira ID     : r25282505
            Objective   : Verify run pools test button is displayed

            Precondition:
            - User have access to IMS qa environment

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/chooseHostEvacuationType/1455135

            Expected Outcome:
            - run pools test button is displayed

        """
        tc_id = setup.get("test_run_pools_test_button_is_displayed", None)
        dvt_url = setup.get("data_verification_tool_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify run pools test button is displayed")
            self.log.info("Precondition: User has access to IMS qa environment.")
            self.log.info(
                "Starting test: test_run_pools_test_button_is_displayed")

            data_verification_tool_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login.")
            self.login_to_app(self.driver, self.username, self.password, data_verification_tool_page, url)

            self.log.info("Opening the host evacuation ticket url")
            self.open_data_verification_tool_page(dvt_url, environment)

            self.log.info("Checking if run pools test button is displayed and enabled")
            run_pools_test = self.run_pools_test_button_display_check()

            self.log.info(f"is run address test displayed: {run_pools_test}")
            assert run_pools_test, "run pools test button is not displayed"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.dataverificationtool
    @pytest.mark.php8_1
    def test_run_power_test_button_is_displayed(self, setup):
        """
            Test Case ID: TC_UI_VSI_DVT_0004
            Jira ID     : r25305303
            Objective   : Verify run pools power button is displayed

            Precondition:
            - User have access to IMS qa environment

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/chooseHostEvacuationType/1455135

            Expected Outcome:
            - run power test button is displayed

        """
        tc_id = setup.get("test_run_power_test_button_is_displayed", None)
        dvt_url = setup.get("data_verification_tool_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify run pools power button is displayed")
            self.log.info("Precondition: User has access to IMS qa environment.")
            self.log.info(
                "Starting test: test_run_power_test_button_is_displayed")

            data_verification_tool_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login.")
            self.login_to_app(self.driver, self.username, self.password, data_verification_tool_page, url)

            self.log.info("Opening the host evacuation ticket url")
            self.open_data_verification_tool_page(dvt_url, environment)

            self.log.info("Checking if run power test button is displayed and enabled")
            run_power_test = self.run_power_test_button_display_check()

            self.log.info(f"is run power test displayed: {run_power_test}")
            assert run_power_test, "run power test button is not displayed"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.dataverificationtool
    @pytest.mark.php8_1
    def test_run_checkin_test_button_is_displayed(self, setup):
        """
            Test Case ID: TC_UI_VSI_DVT_0005
            Jira ID     : r25305304
            Objective   : Verify run checkin power button is displayed

            Precondition:
            - User have access to IMS qa environment

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/chooseHostEvacuationType/1455135

            Expected Outcome:
            - run checkin test button is displayed

        """
        tc_id = setup.get("test_run_checkin_test_button_is_displayed", None)
        dvt_url = setup.get("data_verification_tool_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify run checkin power button is displayed")
            self.log.info("Precondition: User has access to IMS qa environment.")
            self.log.info(
                "Starting test: test_run_checkin_test_button_is_displayed")

            data_verification_tool_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login.")
            self.login_to_app(self.driver, self.username, self.password, data_verification_tool_page, url)

            self.log.info("Opening the host evacuation ticket url")
            self.open_data_verification_tool_page(dvt_url, environment)

            self.log.info("Checking if run checkin test button is displayed and enabled")
            run_checkin_test = self.run_checkin_test_button_display_check()

            self.log.info(f"is run checkin test displayed: {run_checkin_test}")
            assert run_checkin_test, "run checkin test button is not displayed"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.dataverificationtool
    @pytest.mark.php8_1
    def test_run_scanin_test_button_is_displayed(self, setup):
        """
            Test Case ID: TC_UI_VSI_DVT_0006
            Jira ID     : r25305305
            Objective   : Verify run scanin power button is displayed

            Precondition:
            - User have access to IMS qa environment

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/chooseHostEvacuationType/1455135

            Expected Outcome:
            - run scanin test button is displayed

        """
        tc_id = setup.get("test_run_scanin_test_button_is_displayed", None)
        dvt_url = setup.get("data_verification_tool_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify run scanin power button is displayed")
            self.log.info("Precondition: User has access to IMS qa environment.")
            self.log.info(
                "Starting test: test_run_scanin_test_button_is_displayed")

            data_verification_tool_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login.")
            self.login_to_app(self.driver, self.username, self.password, data_verification_tool_page, url)

            self.log.info("Opening the host evacuation ticket url")
            self.open_data_verification_tool_page(dvt_url, environment)

            self.log.info("Checking if run scanin test button is displayed and enabled")
            run_scanin_test = self.run_scanin_test_button_display_check()

            self.log.info(f"is run scanin test displayed: {run_scanin_test}")
            assert run_scanin_test, "run scanin test button is not displayed"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.dataverificationtool
    @pytest.mark.php8_1
    def test_datacenter_to_verify_checkbox_options_are_displayed_properly(self, setup):
        """
            Test Case ID: TC_UI_VSI_DVT_0007
            Jira ID     : r25305322
            Objective   : Verify datacenter to verify checkbox options are displayed properly

            Precondition:
            - User have access to IMS qa environment

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/chooseHostEvacuationType/1455135

            Expected Outcome:
            - datacenter to verify checkbox options are displayed properly

        """
        tc_id = setup.get("test_datacenter_to_verify_checkbox_options_are_displayed_properly", None)
        dvt_url = setup.get("data_verification_tool_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify datacenter to verify checkbox options are displayed properly")
            self.log.info("Precondition: User has access to IMS qa environment.")
            self.log.info(
                "Starting test: test_datacenter_to_verify_checkbox_options_are_displayed_properly")

            data_verification_tool_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login.")
            self.login_to_app(self.driver, self.username, self.password, data_verification_tool_page, url)

            self.log.info("Opening the host evacuation ticket url")
            self.open_data_verification_tool_page(dvt_url, environment)

            self.log.info("getting the datacenter to verify options")
            datacenter_to_verify_options = self.verify_checkbox_option_for_datacenter_to_verify()

            self.log.info(f"datacenter to verify options: {datacenter_to_verify_options}")
            assert datacenter_to_verify_options, "datacenter to verify options are not properly displayed"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.dataverificationtool
    @pytest.mark.php8_1
    def test_run_all_tests_button_is_displayed(self, setup):
        """
            Test Case ID: TC_UI_VSI_DVT_0008
            Jira ID     : r25305324
            Objective   : Verify run all tests button is displayed

            Precondition:
            - User have access to IMS qa environment

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/chooseHostEvacuationType/1455135

            Expected Outcome:
            - run all tests button is displayed

        """
        tc_id = setup.get("test_run_all_tests_button_is_displayed", None)
        dvt_url = setup.get("data_verification_tool_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify run all tests button is displayed")
            self.log.info("Precondition: User has access to IMS qa environment.")
            self.log.info(
                "Starting test: test_run_all_tests_button_is_displayed")

            data_verification_tool_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login.")
            self.login_to_app(self.driver, self.username, self.password, data_verification_tool_page, url)

            self.log.info("Opening the host evacuation ticket url")
            self.open_data_verification_tool_page(dvt_url, environment)

            self.log.info("Checking if run scanin test button is displayed and enabled")
            run_all_test = self.run_all_test_button_display_check()

            self.log.info(f"is run all tests button displayed: {run_all_test}")
            assert run_all_test, "run all tests button is not displayed"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.dataverificationtool
    @pytest.mark.php8_1
    def test_export_test_results_button_is_displayed(self, setup):
        """
            Test Case ID: TC_UI_VSI_DVT_0009
            Jira ID     : r25305325
            Objective   : Verify export test results button is displayed

            Precondition:
            - User have access to IMS qa environment

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/chooseHostEvacuationType/1455135

            Expected Outcome:
            - export test results button is displayed

        """
        tc_id = setup.get("test_export_test_results_button_is_displayed", None)
        dvt_url = setup.get("data_verification_tool_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify export test results button is displayed")
            self.log.info("Precondition: User has access to IMS qa environment.")
            self.log.info(
                "Starting test: test_export_test_results_button_is_displayed")

            data_verification_tool_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login.")
            self.login_to_app(self.driver, self.username, self.password, data_verification_tool_page, url)

            self.log.info("Opening the host evacuation ticket url")
            self.open_data_verification_tool_page(dvt_url, environment)

            self.log.info("Checking if run export all results  button is displayed and enabled")
            export_all_results = self.export_all_results_button_display_check()

            self.log.info(f"is export all results button displayed: {export_all_results}")
            assert export_all_results, "export all results button is not displayed"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")
