import pytest
from selenium.common import TimeoutException
from tests.test_service_inventory_report_page.test_service_inventory_report_page_helper import \
    TestServiceInventoryReportPageHelper
from tests.test_base import BaseTest
from utilities.read_json import read_and_parse_json
from utilities.read_properties import ReadConfig


class TestServiceInventoryReportPage(BaseTest, TestServiceInventoryReportPageHelper):
    base_url = ReadConfig.get_application_url()
    username = ReadConfig.get_application_username()
    password = ReadConfig.get_application_password()

    @pytest.fixture(scope="function")
    def setup(self, logger):
        self.log = logger
        self.log.info("Setting up the test data file for use in the test")
        return read_and_parse_json(
            'tests/test_service_inventory_report_page/testdata/service_inventory_report_testdata.json')

    @pytest.mark.serviceinventoryreport
    @pytest.mark.php8_1
    def test_account_id_is_an_editable_field(self, setup):
        """
            Test Case ID: TC_UI_VSI_SIR_0001
            Jira ID     : r25437477
            Objective   : Verify that account id is an editable field


            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - account id is an editable field

        """
        tc_id = setup.get("test_account_id_is_an_editable_field", None)
        service_inventory_report_url = setup.get("service_inventory_report_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that account id is an editable field")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_account_id_is_an_editable_field")

            update_pool_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, update_pool_page, url)

            self.log.info("Opening the service inventory report page")
            self.open_service_inventory_report_page(service_inventory_report_url, environment)

            self.log.info("Checking the details of account id field")
            account_id = self.account_id_field_check()

            self.log.info(f"is account id editable {account_id}")
            assert account_id , "account id is not an editable field"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.serviceinventoryreport
    @pytest.mark.php8_1
    def test_company_name_is_an_editable_field(self, setup):
        """
            Test Case ID: TC_UI_VSI_SIR_0002
            Jira ID     : r25437481
            Objective   : Verify that company name is an editable field


            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - company name is an editable field

        """
        tc_id = setup.get("test_company_name_is_an_editable_field", None)
        service_inventory_report_url = setup.get("service_inventory_report_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that company name is an editable field")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_company_name_is_an_editable_field")

            update_pool_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, update_pool_page, url)

            self.log.info("Opening the service inventory report page")
            self.open_service_inventory_report_page(service_inventory_report_url, environment)

            self.log.info("Checking the details of company name field")
            company_name = self.company_name_field_check()

            self.log.info(f"is company name editable {company_name}")
            assert company_name, "company name is not an editable field"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.serviceinventoryreport
    @pytest.mark.php8_1
    def test_hostname_is_an_editable_field(self, setup):
        """
            Test Case ID: TC_UI_VSI_SIR_0003
            Jira ID     : r25437483
            Objective   : Verify that hostname is an editable field


            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - hostname is an editable field

        """
        tc_id = setup.get("test_hostname_is_an_editable_field", None)
        service_inventory_report_url = setup.get("service_inventory_report_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that hostname is an editable field")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_hostname_is_an_editable_field")

            update_pool_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, update_pool_page, url)

            self.log.info("Opening the service inventory report page")
            self.open_service_inventory_report_page(service_inventory_report_url, environment)

            self.log.info("Checking the details of hostname field")
            hostname = self.hostname_field_check()

            self.log.info(f"is hostname editable {hostname}")
            assert hostname, "hostname is not an editable field"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.serviceinventoryreport
    @pytest.mark.php8_1
    def test_ip_address_is_an_editable_field(self, setup):
        """
            Test Case ID: TC_UI_VSI_SIR_0004
            Jira ID     : r25437485
            Objective   : Verify that ip address is an editable field


            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - ip address is an editable field

        """
        tc_id = setup.get("test_ip_address_is_an_editable_field", None)
        service_inventory_report_url = setup.get("service_inventory_report_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that hostname is an editable field")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_ip_address_is_an_editable_field")

            update_pool_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, update_pool_page, url)

            self.log.info("Opening the service inventory report page")
            self.open_service_inventory_report_page(service_inventory_report_url, environment)

            self.log.info("Checking the details of ip address field")
            ip_addr = self.ip_address_field_check()

            self.log.info(f"is ip address editable {ip_addr}")
            assert ip_addr, "ip address is not an editable field"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.serviceinventoryreport
    @pytest.mark.php8_1
    def test_evault_username_is_an_editable_field(self, setup):
        """
            Test Case ID: TC_UI_VSI_SIR_0005
            Jira ID     : r25437493
            Objective   : Verify that evault username is an editable field


            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - evault username is an editable field

        """
        tc_id = setup.get("test_evault_username_is_an_editable_field", None)
        service_inventory_report_url = setup.get("service_inventory_report_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that evault username is an editable field")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_evault_username_is_an_editable_field")

            update_pool_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, update_pool_page, url)

            self.log.info("Opening the service inventory report page")
            self.open_service_inventory_report_page(service_inventory_report_url, environment)

            self.log.info("Checking the details of evault username field")
            evault_username = self.evault_username_field_check()

            self.log.info(f"is evault username editable {evault_username}")
            assert evault_username, "evault username is not an editable field"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.serviceinventoryreport
    @pytest.mark.php8_1
    def test_company_name_checkbox_has_len_4(self, setup):
        """
            Test Case ID: TC_UI_VSI_SIR_0006
            Jira ID     : r25437498
            Objective   : Verify that company name checkbox has length of 4


            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - company name checkbox has length of 4

        """
        tc_id = setup.get("test_company_name_checkbox_has_len_4", None)
        service_inventory_report_url = setup.get("service_inventory_report_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that company name checkbox has length of 4")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_company_name_checkbox_has_len_4")

            update_pool_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, update_pool_page, url)

            self.log.info("Opening the service inventory report page")
            self.open_service_inventory_report_page(service_inventory_report_url, environment)

            self.log.info("Checking the options of company name field")
            options = self.company_name_len_check()

            self.log.info(f"options available to company name are {options}")
            assert len(options) == 4, "options available to company name is not 4"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.serviceinventoryreport
    @pytest.mark.php8_1
    def test_hostname_checkbox_has_len_4(self, setup):
        """
            Test Case ID: TC_UI_VSI_SIR_0007
            Jira ID     : r25437500
            Objective   : Verify that host name checkbox has length of 4


            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - host name checkbox has length of 4

        """
        tc_id = setup.get("test_hostname_checkbox_has_len_4", None)
        service_inventory_report_url = setup.get("service_inventory_report_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that host name checkbox has length of 4")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_hostname_checkbox_has_len_4")

            update_pool_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, update_pool_page, url)

            self.log.info("Opening the service inventory report page")
            self.open_service_inventory_report_page(service_inventory_report_url, environment)

            self.log.info("Checking the options of hostname field")
            options = self.hostname_len_check()

            self.log.info(f"options available to hostname are {options}")
            assert len(options) == 4, "options available to hostname is not 4"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.serviceinventoryreport
    @pytest.mark.php8_1
    def test_ip_addr_checkbox_has_len_4(self, setup):
        """
            Test Case ID: TC_UI_VSI_SIR_0008
            Jira ID     : r25437501
            Objective   : Verify that ip address checkbox has length of 4


            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - ip address checkbox has length of 4

        """
        tc_id = setup.get("test_ip_addr_checkbox_has_len_4", None)
        service_inventory_report_url = setup.get("service_inventory_report_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that ip address checkbox has length of 4")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_ip_addr_checkbox_has_len_4")

            update_pool_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, update_pool_page, url)

            self.log.info("Opening the service inventory report page")
            self.open_service_inventory_report_page(service_inventory_report_url, environment)

            self.log.info("Checking the options of ip address field")
            options = self.ip_addr_len_check()

            self.log.info(f"options available to hostname are {options}")
            assert len(options) == 4, "options available to ip address is not 4"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.serviceinventoryreport
    @pytest.mark.php8_1
    def test_evault_username_checkbox_has_len_4(self, setup):
        """
            Test Case ID: TC_UI_VSI_SIR_0009
            Jira ID     : r25437506
            Objective   : Verify that evault username checkbox has length of 4


            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - evault username checkbox has length of 4

        """
        tc_id = setup.get("test_evault_username_checkbox_has_len_4", None)
        service_inventory_report_url = setup.get("service_inventory_report_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that evault username checkbox has length of 4")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_evault_username_checkbox_has_len_4")

            update_pool_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, update_pool_page, url)

            self.log.info("Opening the service inventory report page")
            self.open_service_inventory_report_page(service_inventory_report_url, environment)

            self.log.info("Checking the options of evault username field")
            options = self.evault_username_len_check()

            self.log.info(f"options available to evault username are {options}")
            assert len(options) == 4, "options available to evault username is not 4"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.serviceinventoryreport
    @pytest.mark.php8_1
    def test_show_with_evault_checkbox_has_len_2(self, setup):
        """
            Test Case ID: TC_UI_VSI_SIR_0010
            Jira ID     : r25437510
            Objective   : Verify that show with evault checkbox has length of 2


            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - show with evault username checkbox has length of 2

        """
        tc_id = setup.get("test_show_with_evault_checkbox_has_len_2", None)
        service_inventory_report_url = setup.get("service_inventory_report_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that evault username checkbox has length of 4")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_show_with_evault_checkbox_has_len_2")

            update_pool_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, update_pool_page, url)

            self.log.info("Opening the service inventory report page")
            self.open_service_inventory_report_page(service_inventory_report_url, environment)

            self.log.info("Checking the options of show with evault field")
            options = self.show_with_evault_len_check()

            self.log.info(f"options available to show with evault are {options}")
            assert len(options) == 2, "options available to show with evault is not 2"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.serviceinventoryreport
    @pytest.mark.php8_1
    def test_object_type_checkbox_has_len_2(self, setup):
        """
            Test Case ID: TC_UI_VSI_SIR_0011
            Jira ID     : r25437534
            Objective   : Verify that object type checkbox has length of 2


            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - object type checkbox has length of 2

        """
        tc_id = setup.get("test_object_type_checkbox_has_len_2", None)
        service_inventory_report_url = setup.get("service_inventory_report_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that object type checkbox has length of 2")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_object_type_checkbox_has_len_2")

            update_pool_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, update_pool_page, url)

            self.log.info("Opening the service inventory report page")
            self.open_service_inventory_report_page(service_inventory_report_url, environment)

            self.log.info("Checking the options of object type field")
            options = self.object_type_len_check()

            self.log.info(f"options available to object type are {options}")
            assert len(options) == 2, "options available to object type is not 2"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.serviceinventoryreport
    @pytest.mark.php8_1
    def test_object_status_checkbox_has_len_2(self, setup):
        """
            Test Case ID: TC_UI_VSI_SIR_0012
            Jira ID     : r25437535
            Objective   : Verify that object status checkbox has length of 2


            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - object status checkbox has length of 2

        """
        tc_id = setup.get("test_object_status_checkbox_has_len_2", None)
        service_inventory_report_url = setup.get("service_inventory_report_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that object status checkbox has length of 2")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_object_status_checkbox_has_len_2")

            update_pool_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, update_pool_page, url)

            self.log.info("Opening the service inventory report page")
            self.open_service_inventory_report_page(service_inventory_report_url, environment)

            self.log.info("Checking the options of object status field")
            options = self.object_status_len_check()

            self.log.info(f"options available to object type are {options}")
            assert len(options) == 2, "options available to object status is not 2"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.serviceinventoryreport
    @pytest.mark.php8_1
    def test_managed_server_checkbox_has_len_1(self, setup):
        """
            Test Case ID: TC_UI_VSI_SIR_0013
            Jira ID     : r25437536
            Objective   : Verify that managed server checkbox has length of 1


            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - managed server checkbox has length of 1

        """
        tc_id = setup.get("test_managed_server_checkbox_has_len_1", None)
        service_inventory_report_url = setup.get("service_inventory_report_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that object status checkbox has length of 2")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_managed_server_checkbox_has_len_1")

            update_pool_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, update_pool_page, url)

            self.log.info("Opening the service inventory report page")
            self.open_service_inventory_report_page(service_inventory_report_url, environment)

            self.log.info("Checking the options of managed server field")
            options = self.managed_server_len_check()

            self.log.info(f"options available to managed server are {options}")
            assert len(options) == 2, "options available to managed server is not 2"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.serviceinventoryreport
    @pytest.mark.php8_1
    def test_search_button_is_displayed_and_enabled(self, setup):
        """
            Test Case ID: TC_UI_VSI_SIR_0014
            Jira ID     : r25444046
            Objective   : Verify that Search button is displayed and enabled


            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - search button is displayed and enabled

        """
        tc_id = setup.get("test_search_button_is_displayed_and_enabled", None)
        service_inventory_report_url = setup.get("service_inventory_report_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that object status checkbox has length of 2")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_search_button_is_displayed_and_enabled")

            update_pool_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, update_pool_page, url)

            self.log.info("Opening the service inventory report page")
            self.open_service_inventory_report_page(service_inventory_report_url, environment)

            self.log.info("Checking the status of search button")
            search_btn = self.search_btn_status_check()

            self.log.info(f"is search button displayed and enabled {search_btn}")
            assert search_btn, "search button is not displayed or enabled"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")
            