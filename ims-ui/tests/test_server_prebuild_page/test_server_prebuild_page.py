import pytest
from selenium.common import TimeoutException
from tests.test_server_prebuild_page.test_server_prebuild_test_helper import TestServerPrebuildPageHelper
from tests.test_base import BaseTest
from utilities.read_json import read_and_parse_json
from utilities.read_properties import ReadConfig


class TestServerPrebuildPage(BaseTest, TestServerPrebuildPageHelper):
    base_url = ReadConfig.get_application_url()
    username = ReadConfig.get_application_username()
    password = ReadConfig.get_application_password()

    @pytest.fixture(scope="function")
    def setup(self, logger):
        self.log = logger
        self.log.info("Setting up the test data file for use in the test")
        return read_and_parse_json(
            'tests/test_server_prebuild_page/testdata/server_prebuild_testdata.json')

    @pytest.mark.serverprebuild
    @pytest.mark.php8_1
    def test_hardware_id_field_is_enabled_and_editable(self, setup):
        """
            Test Case ID: TC_UI_VSI_SP_0001
            Jira ID     : r25403942
            Objective   : Verify that hardware id field is enabled and editable

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - hardware id field is enabled and editable

        """
        tc_id = setup.get("test_hardware_id_field_is_enabled_and_editable", None)
        server_prebuild_url = setup.get("server_prebuild_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that hardware id field is enabled and editable")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_hardware_id_field_is_enabled_and_editable")

            network_monitoring_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, network_monitoring_page, url)

            self.log.info("Opening server prebuild page")
            self.open_server_prebuild_page(server_prebuild_url, environment)

            self.log.info("checking hardware id is editable")
            editability_check = self.check_if_hardware_id_is_editable()

            self.log.info(f"hardware id editable status {editability_check}")
            assert editability_check, "Hardware id is not an editable field"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.serverprebuild
    @pytest.mark.php8_1
    def test_base_server_id_field_is_enabled_and_editable(self, setup):
        """
            Test Case ID: TC_UI_VSI_SP_0002
            Jira ID     : r25403945
            Objective   : Verify that base server id field is enabled and editable

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - base server id field is enabled and editable

        """
        tc_id = setup.get("test_base_server_id_field_is_enabled_and_editable", None)
        server_prebuild_url = setup.get("server_prebuild_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that base server id field is enabled and editable")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_base_server_id_field_is_enabled_and_editable")

            network_monitoring_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, network_monitoring_page, url)

            self.log.info("Opening server prebuild page")
            self.open_server_prebuild_page(server_prebuild_url, environment)

            self.log.info("checking base server id is editable")
            editability_check = self.check_if_base_server_id_is_editable()

            self.log.info(f"Base server id editable status {editability_check}")
            assert editability_check, "Base server id is not an editable field"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.serverprebuild
    @pytest.mark.php8_1
    def test_softlayer_ticket_id_field_is_enabled_and_editable(self, setup):
        """
            Test Case ID: TC_UI_VSI_SP_0003
            Jira ID     : r25415302
            Objective   : Verify that softlayer ticket id textbox is enabled and editable

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - softlayer ticket id textbox is enabled and editable

        """
        tc_id = setup.get("test_softlayer_ticket_id_field_is_enabled_and_editable", None)
        server_prebuild_url = setup.get("server_prebuild_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that softlayer ticket id textbox is enabled and editable")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_softlayer_ticket_id_field_is_enabled_and_editable")

            network_monitoring_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, network_monitoring_page, url)

            self.log.info("Opening server prebuild page")
            self.open_server_prebuild_page(server_prebuild_url, environment)

            self.log.info("checking softlayer ticket id is editable")
            softlayer_ticket_id = self.check_if_softlayer_ticket_id_is_editable()

            self.log.info(f"softlayer ticket id editable status {softlayer_ticket_id}")
            assert softlayer_ticket_id, "softlayer ticket id is not an editable field"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.serverprebuild
    @pytest.mark.php8_1
    def test_server_prebuild_job_base_server_id_field_is_enabled_and_editable(self, setup):
        """
            Test Case ID: TC_UI_VSI_SP_0004
            Jira ID     : r25415303
            Objective   : Verify that base server id textbox of server prebuild job tab is enabled and editable

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - base server id textbox of server prebuild job tab is enabled and editable

        """
        tc_id = setup.get("test_server_prebuild_job_base_server_id_field_is_enabled_and_editable", None)
        server_prebuild_url = setup.get("server_prebuild_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that softlayer ticket id textbox is enabled and editable")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_server_prebuild_job_base_server_id_field_is_enabled_and_editable")

            network_monitoring_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, network_monitoring_page, url)

            self.log.info("Opening server prebuild page")
            self.open_server_prebuild_page(server_prebuild_url, environment)
            self.navigate_to_server_prebuild_job_tab()

            self.log.info("checking base server id is editable")
            base_server_id = self.check_if_spj_base_server_id_is_editable()

            self.log.info(f"base server id editable status {base_server_id}")
            assert base_server_id, "base server id is not an editable field"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.php8_1
    @pytest.mark.serverprebuild
    def test_server_prebuild_job_softlayer_ticket_id_field_is_enabled_and_editable(self, setup):
        """
            Test Case ID: TC_UI_VSI_SP_0005
            Jira ID     : r25415310
            Objective   : Verify that softlayer ticket id textbox of server prebuild job tab is enabled and editable

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - softlayer ticket id textbox of server prebuild job tab is enabled and editable

        """
        tc_id = setup.get("test_server_prebuild_job_softlayer_ticket_id_field_is_enabled_and_editable", None)
        server_prebuild_url = setup.get("server_prebuild_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that softlayer id textbox of server prebuild job tab is enabled and editable")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_server_prebuild_job_softlayer_ticket_id_field_is_enabled_and_editable")

            network_monitoring_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, network_monitoring_page, url)

            self.log.info("Opening server prebuild page")
            self.open_server_prebuild_page(server_prebuild_url, environment)
            self.navigate_to_server_prebuild_job_tab()

            self.log.info("checking softlayer ticket id is editable")
            softlayer_ticket_id = self.check_if_spj_softlayer_ticket_id_is_editable()

            self.log.info(f"softlayer ticket id editable status {softlayer_ticket_id}")
            assert softlayer_ticket_id, "softlayer ticket id is not an editable field"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.serverprebuild
    @pytest.mark.php8_1
    def test_spj_prebuild_job_id_is_enabled_and_editable(self, setup):
        """
            Test Case ID: TC_UI_VSI_SP_0006
            Jira ID     : r25415312
            Objective   : Verify that prebuild job id textbox of server prebuild job tab is enabled and editable

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - prebuild job id textbox of server prebuild job tab is enabled and editable

        """
        tc_id = setup.get("test_spj_prebuild_job_id_is_enabled_and_editable", None)
        server_prebuild_url = setup.get("server_prebuild_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that prebuild job id textbox of server prebuild job tab is enabled and editable")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_spj_prebuild_job_id_is_enabled_and_editable")

            network_monitoring_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, network_monitoring_page, url)

            self.log.info("Opening server prebuild page")
            self.open_server_prebuild_page(server_prebuild_url, environment)
            self.navigate_to_server_prebuild_job_tab()

            self.log.info("checking if prebuild job id is editable")
            prebuild_job_id = self.check_if_spj_prebuild_job_id_is_editable()

            self.log.info(f"prebuild job id editable status {prebuild_job_id}")
            assert prebuild_job_id, "prebuild job id is not an editable field"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.serverprebuild
    @pytest.mark.php8_1
    def test_spj_user_id_is_enabled_and_editable(self, setup):
        """
            Test Case ID: TC_UI_VSI_SP_0007
            Jira ID     : r25415312
            Objective   : Verify that user id textbox of server prebuild job tab is enabled and editable

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - user id textbox of server prebuild job tab is enabled and editable

        """
        tc_id = setup.get("test_spj_user_id_is_enabled_and_editable", None)
        server_prebuild_url = setup.get("server_prebuild_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info(
                "Objective: Verify that user id textbox of server prebuild job tab is enabled and editable")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_spj_user_id_is_enabled_and_editable")

            network_monitoring_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, network_monitoring_page, url)

            self.log.info("Opening server prebuild page")
            self.open_server_prebuild_page(server_prebuild_url, environment)
            self.navigate_to_server_prebuild_job_tab()

            self.log.info("checking if prebuild job id is editable")
            user_id = self.check_if_spj_user_id_is_editable()

            self.log.info(f"user id editable status {user_id}")
            assert user_id, "user id is not an editable field"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.serverprebuild
    @pytest.mark.php8_1
    def test_create_button_of_cpj_is_displayed_and_enabled(self, setup):
        """
            Test Case ID: TC_UI_VSI_SP_0008
            Jira ID     : r25437462
            Objective   : Verify that create button of create prebuild job tab is displayed and enabled

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - create button of create prebuild job tab is displayed and enabled

        """
        tc_id = setup.get("test_create_button_of_cpj_is_displayed_and_enabled", None)
        server_prebuild_url = setup.get("server_prebuild_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info(
                "Objective: Verify that create button of create prebuild job tab is displayed and enabled")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_create_button_of_cpj_is_displayed_and_enabled")

            network_monitoring_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, network_monitoring_page, url)

            self.log.info("Opening server prebuild page")
            self.open_server_prebuild_page(server_prebuild_url, environment)

            self.log.info("Getting the details of create button")
            button_status = self.create_button_cpj_display_check()

            self.log.info(f"is create button displayed and clickable {button_status}")
            assert button_status, "create button is not displayed or clickable"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.serverprebuild
    @pytest.mark.php8_1
    def test_reset_button_of_cpj_is_displayed_and_enabled(self, setup):
        """
            Test Case ID: TC_UI_VSI_SP_0009
            Jira ID     : r25437468
            Objective   : Verify that reset button of create prebuild job tab is displayed and enabled

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - create button of reset prebuild job tab is displayed and enabled

        """
        tc_id = setup.get("test_reset_button_of_cpj_is_displayed_and_enabled", None)
        server_prebuild_url = setup.get("server_prebuild_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info(
                "Objective: Verify that reset button of create prebuild job tab is displayed and enabled")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_reset_button_of_cpj_is_displayed_and_enabled")

            network_monitoring_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, network_monitoring_page, url)

            self.log.info("Opening server prebuild page")
            self.open_server_prebuild_page(server_prebuild_url, environment)

            self.log.info("Getting the details of reset button")
            button_status = self.reset_button_cpj_display_check()

            self.log.info(f"is reset button displayed and clickable {button_status}")
            assert button_status, "reset button is not displayed or clickable"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.serverprebuild
    @pytest.mark.php8_1
    def test_search_button_of_spj_is_displayed_and_enabled(self, setup):
        """
            Test Case ID: TC_UI_VSI_SP_0010
            Jira ID     : r25437469
            Objective   : Verify that search button of search prebuild job tab is displayed and enabled

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - search button of search prebuild job tab is displayed and enabled

        """
        tc_id = setup.get("test_search_button_of_spj_is_displayed_and_enabled", None)
        server_prebuild_url = setup.get("server_prebuild_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info(
                "Objective: Verify that search button of create search job tab is displayed and enabled")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_search_button_of_spj_is_displayed_and_enabled")

            network_monitoring_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, network_monitoring_page, url)

            self.log.info("Opening server prebuild page")
            self.open_server_prebuild_page(server_prebuild_url, environment)
            self.navigate_to_server_prebuild_job_tab()

            self.log.info("Getting the details of search button")
            button_status = self.search_button_spj_display_check()

            self.log.info(f"is search button displayed and clickable {button_status}")
            assert button_status, "search button is not displayed or clickable"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.serverprebuild
    @pytest.mark.php8_1
    @pytest.mark.xfail
    def test_reset_button_of_spj_is_displayed_and_enabled(self, setup):
        """
            Test Case ID: TC_UI_VSI_SP_0011
            Jira ID     : r25437470

            Objective   : Verify that reset button of search prebuild job tab is displayed and enabled

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - reset button of search prebuild job tab is displayed and enabled

        """
        tc_id = setup.get("test_reset_button_of_spj_is_displayed_and_enabled", None)
        server_prebuild_url = setup.get("server_prebuild_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info(
                "Objective: Verify that reset button of search prebuild job tab is displayed and enabled")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_reset_button_of_spj_is_displayed_and_enabled")

            network_monitoring_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, network_monitoring_page, url)

            self.log.info("Opening server prebuild page")
            self.open_server_prebuild_page(server_prebuild_url, environment)
            self.navigate_to_server_prebuild_job_tab()

            self.log.info("Getting the details of reset button")
            button_status = self.reset_button_spj_display_check()

            self.log.info(f"is reset button displayed and clickable {button_status}")
            assert button_status, "reset button is not displayed or clickable"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")
       
