import time

import pytest
from selenium.common import TimeoutException
from tests.test_hardware_lease_page.test_hardware_lease_page_helper import TestHardwareLeasePageHelper
from tests.test_base import BaseTest
from utilities.read_json import read_and_parse_json
from utilities.read_properties import ReadConfig


class TestHardwareLeasePage(BaseTest, TestHardwareLeasePageHelper):
    base_url = ReadConfig.get_application_url()
    username = ReadConfig.get_application_username()
    password = ReadConfig.get_application_password()

    @pytest.fixture(scope="function")
    def setup(self, logger):
        self.log = logger
        self.log.info("Setting up the test data file for use in the test")
        return read_and_parse_json(
            'tests/test_hardware_lease_page/testdata/hardware_lease_page_testdata.json')

    @pytest.mark.php8_1
    @pytest.mark.hardwarelease
    def test_department_dropdown_is_clickable(self, setup):
        """
            Test Case ID: TC_UI_HL_0001
            Jira ID     : r25094694
            Objective   : Verify that department dropdown is clickable

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/HardwareComponent/search

            Expected Outcome:
            - department dropdown is clickable

        """
        tc_id = setup.get("tc_id_test_department_dropdown_is_clickable", None)
        hardware_lease_url = setup.get("hardware_lease_url", None)
        environment = setup.get("environment", None)
        department = setup.get("department", None)
        department_value = setup.get("department_value", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that department dropdown is clickable")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_department_dropdown_is_clickable")

            hardware_component_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_component_search_page, url)

            self.log.info("Opening the hardware component search page")
            self.open_hardware_lease_page(hardware_lease_url, environment)
            result = self.check_if_department_dropdown_is_clickable(department, department_value)
            assert result, "Department dropdown is not clickable"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.php8_1
    @pytest.mark.hardwarelease
    def test_ship_to_address_contains_a_default_value(self, setup):
        """
            Test Case ID: TC_UI_HL_0002
            Jira ID     : r25094694
            Objective   : Verify that ship to address contains a default value

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/HardwareComponent/search

            Expected Outcome:
            - ship to address contains a default value

        """
        tc_id = setup.get("tc_id_test_ship_to_address_contains_a_default_value", None)
        hardware_lease_url = setup.get("hardware_lease_url", None)
        environment = setup.get("environment", None)
        department = setup.get("department", None)
        department_value = setup.get("department_value", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that ship to address contains a default value")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_ship_to_address_contains_a_default_value")

            hardware_component_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_component_search_page, url)

            self.log.info("Opening the hardware component search page")
            self.open_hardware_lease_page(hardware_lease_url, environment)
            result = self.check_ship_to_address_default_value()
            assert result, "ship to address doesnt contain a default value"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.php8_1
    @pytest.mark.hardwarelease
    def test_lead_time_accepts_numeric_input_upto_3(self, setup):
        """
            Test Case ID: TC_UI_HL_0003
            Jira ID     : r25094694
            Objective   : Verify that lead time accepts numeric input upto 3

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/HardwareComponent/search

            Expected Outcome:
            - lead time accepts numeric input upto 3

        """
        tc_id = setup.get("tc_id_test_lead_time_accepts_numeric_input_upto_3", None)
        hardware_lease_url = setup.get("hardware_lease_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that lead time accepts numeric input upto 3")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_lead_time_accepts_numeric_input_upto_3")

            hardware_component_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_component_search_page, url)

            self.log.info("Opening the hardware component search page")
            self.open_hardware_lease_page(hardware_lease_url, environment)
            result = self.get_maxlength_lead_time()
            assert result == 3, "lead time does not have a maxlength of 3"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.php8_1
    @pytest.mark.xfail
    @pytest.mark.hardwarelease
    def test_lead_time_accepts_only_numeric_input(self, setup):
        """
            Test Case ID: TC_UI_HL_0004
            Jira ID     : r25094694
            Objective   : Verify that lead time accepts only numeric input

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/HardwareComponent/search

            Expected Outcome:
            - lead time accepts only numeric input

        """
        tc_id = setup.get("tc_id_test_lead_time_accepts_only_numeric_input", None)
        hardware_lease_url = setup.get("hardware_lease_url", None)
        environment = setup.get("environment", None)
        lead_time = setup.get("lead_time", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that lead time accepts only numeric input")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_lead_time_accepts_only_numeric_input")

            hardware_component_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_component_search_page, url)

            self.log.info("Opening the hardware component search page")
            self.open_hardware_lease_page(hardware_lease_url, environment)
            result = self.input_into_lead_time(lead_time)
            assert result, "lead time accepts value other than numeric"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.php8_1
    @pytest.mark.hardwarelease
    def test_status_field_have_ordered_by_default(self, setup):
        """
            Test Case ID: TC_UI_HL_0005
            Jira ID     : r25094694
            Objective   : Verify that status field have ordered by default

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/HardwareComponent/search

            Expected Outcome:
            - status field have ordered by default

        """
        tc_id = setup.get("tc_id_test_status_field_have_ordered_by_default", None)
        hardware_lease_url = setup.get("hardware_lease_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that status field have ordered by default")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_status_field_have_ordered_by_default")

            hardware_component_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_component_search_page, url)

            self.log.info("Opening the hardware component search page")
            self.open_hardware_lease_page(hardware_lease_url, environment)
            result = self.get_status_field_value()
            assert result, "status does not have ordered by default"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.php8_1
    @pytest.mark.hardwarelease
    def test_total_amount_textfield_has_default_value(self, setup):
        """
            Test Case ID: TC_UI_HL_0006
            Jira ID     : r25094694
            Objective   : Verify that total amount field has a default value

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/HardwareComponent/search

            Expected Outcome:
            - total amount field has a default value

        """
        tc_id = setup.get("tc_id_test_total_amount_textfield_has_default_value", None)
        hardware_lease_url = setup.get("hardware_lease_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that total amount field has a default value")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_total_amount_textfield_has_default_value")

            hardware_component_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_component_search_page, url)

            self.log.info("Opening the hardware component search page")
            self.open_hardware_lease_page(hardware_lease_url, environment)
            result = self.check_if_total_amount_has_default_value()
            assert result, "status does not have ordered by default"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.php8_1
    @pytest.mark.hardwarelease
    def test_buyer_note_is_editable(self, setup):
        """
            Test Case ID: TC_UI_HL_0007
            Jira ID     : r25094694
            Objective   : Verify that buyer note is editable

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/HardwareComponent/search

            Expected Outcome:
            - buyer note is editable

        """
        tc_id = setup.get("tc_id_test_buyer_note_is_editable", None)
        hardware_lease_url = setup.get("hardware_lease_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that buyer note is editable")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_buyer_note_is_editable")

            hardware_component_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_component_search_page, url)

            self.log.info("Opening the hardware component search page")
            self.open_hardware_lease_page(hardware_lease_url, environment)
            result = self.check_if_buyer_note_is_editable()
            assert result, "buyer note is not editable"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.php8_1
    @pytest.mark.hardwarelease
    def test_notes_is_editable(self, setup):
        """
            Test Case ID: TC_UI_HL_0008
            Jira ID     : r25094694
            Objective   : Verify that notes is editable

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/HardwareComponent/search

            Expected Outcome:
            - notes is editable

        """
        tc_id = setup.get("tc_id_test_notes_is_editable", None)
        hardware_lease_url = setup.get("hardware_lease_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that notes is editable")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_notes_is_editable")

            hardware_component_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_component_search_page, url)

            self.log.info("Opening the hardware component search page")
            self.open_hardware_lease_page(hardware_lease_url, environment)
            result = self.check_if_note_is_editable()
            assert result, "note text area is not editable"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.php8_1
    @pytest.mark.hardwarelease
    def test_save_button_is_working(self, setup):
        """
            Test Case ID: TC_UI_HL_0009
            Jira ID     : r25094694
            Objective   : Verify that save button functionality is working

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/HardwareComponent/search

            Expected Outcome:
            - Save button functionality is working

        """
        tc_id = setup.get("tc_id_test_save_button_is_working", None)
        hardware_lease_url = setup.get("hardware_lease_url", None)
        environment = setup.get("environment", None)
        notes = setup.get("notes", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that notes is editable")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_save_button_is_working")

            hardware_component_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_component_search_page, url)

            self.log.info("Opening the hardware component search page")
            self.open_hardware_lease_page(hardware_lease_url, environment)
            result = self.check_if_save_button_is_working(notes)
            assert result == notes, "Save button functionality is not working"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.php8_1
    @pytest.mark.hardwarelease
    def test_export_csv_button_is_working(self, setup):
        """
            Test Case ID: TC_UI_HL_0010
            Jira ID     : r25094694
            Objective   : Verify that export csv button functionality is working

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/HardwareComponent/search

            Expected Outcome:
            - export csv button functionality is working

        """
        tc_id = setup.get("tc_id_test_export_csv_button_is_working", None)
        hardware_lease_url = setup.get("hardware_lease_url", None)
        environment = setup.get("environment", None)
        notes = setup.get("notes", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that export csv button functionality is working")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_export_csv_button_is_working")

            hardware_component_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_component_search_page, url)

            self.log.info("Opening the hardware component search page")
            self.open_hardware_lease_page(hardware_lease_url, environment)
            result = self.check_if_export_csv_button_is_working()
            assert result, "export csv button functionality is not working"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.php8_1
    @pytest.mark.hardwarelease
    def test_export_excel_button_is_working(self, setup):
        """
            Test Case ID: TC_UI_HL_0011
            Jira ID     : r25094694
            Objective   : Verify that export excel button functionality is working

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/HardwareComponent/search

            Expected Outcome:
            - export excel button functionality is working

        """
        tc_id = setup.get("tc_id_test_export_excel_button_is_working", None)
        hardware_lease_url = setup.get("hardware_lease_url", None)
        environment = setup.get("environment", None)
        notes = setup.get("notes", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that export excel button functionality is working")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_export_excel_button_is_working")

            hardware_component_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_component_search_page, url)

            self.log.info("Opening the hardware component search page")
            self.open_hardware_lease_page(hardware_lease_url, environment)
            result = self.check_if_export_excel_button_is_working()
            assert result, "export excel button functionality is not working"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.php8_1
    @pytest.mark.hardwarelease
    def test_export_xml_button_is_working(self, setup):
        """
            Test Case ID: TC_UI_HL_0012
            Jira ID     : r25094694
            Objective   : Verify that export xml button functionality is working

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/HardwareComponent/search

            Expected Outcome:
            - export excel xml functionality is working

        """
        tc_id = setup.get("tc_id_test_export_xml_button_is_working", None)
        hardware_lease_url = setup.get("hardware_lease_url", None)
        environment = setup.get("environment", None)
        notes = setup.get("notes", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that export excel button functionality is working")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_export_xml_button_is_working")

            hardware_component_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_component_search_page, url)

            self.log.info("Opening the hardware component search page")
            self.open_hardware_lease_page(hardware_lease_url, environment)
            result = self.check_if_export_xml_button_is_working()
            assert result, "export xml button functionality is not working"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.php8_1
    @pytest.mark.hardwarelease
    def test_vendor_name_textfield_has_prefilled_value(self, setup):
        """
            Test Case ID: TC_UI_HL_0013
            Jira ID     : r25094694
            Objective   : Verify that vendor name has prefilled value

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/HardwareComponent/search

            Expected Outcome:
            - vendor name has prefilled value


        """
        tc_id = setup.get("tc_id_test_vendor_name_textfield_has_prefilled_value", None)
        hardware_lease_url = setup.get("hardware_lease_url", None)
        environment = setup.get("environment", None)
        notes = setup.get("notes", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that export excel button functionality is working")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_vendor_name_textfield_has_prefilled_value")

            hardware_component_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_component_search_page, url)

            self.log.info("Opening the hardware component search page")
            self.open_hardware_lease_page(hardware_lease_url, environment)
            result = self.check_if_vendor_name_have_default_value()
            assert result, "vendor name does not have prefilled value"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.php8_1
    @pytest.mark.hardwarelease
    def test_ship_to_address_is_disabled(self, setup):
        """
            Test Case ID: TC_UI_HL_0014
            Jira ID     : r25094694
            Objective   : Verify that ship to address is disabled

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/HardwareComponent/search

            Expected Outcome:
            - ship to address has a default option of select an address


        """
        tc_id = setup.get("tc_id_test_ship_to_address_is_disabled", None)
        hardware_lease_url = setup.get("hardware_lease_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that ship to address is disabled")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_ship_to_address_is_disabled")

            hardware_component_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_component_search_page, url)

            self.log.info("Opening the hardware component search page")
            self.open_hardware_lease_page(hardware_lease_url, environment)
            result = self.check_if_ship_to_address_disabled()
            assert result, "ship to address is not disabled"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.php8_1
    @pytest.mark.hardwarelease
    def test_po_void_checkbox_can_be_selected(self, setup):
        """
            Test Case ID: TC_UI_HL_0015
            Jira ID     : r25094694
            Objective   : Verify that PO void can be selected

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/HardwareComponent/search

            Expected Outcome:
            - PO void can be selected


        """
        tc_id = setup.get("tc_id_test_po_void_checkbox_can_be_selected", None)
        hardware_lease_url = setup.get("hardware_lease_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that PO void can be selected")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_po_void_checkbox_can_be_selected")

            hardware_component_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_component_search_page, url)

            self.log.info("Opening the hardware component search page")
            self.open_hardware_lease_page(hardware_lease_url, environment)
            is_selectable = self.check_if_po_void_can_be_selected()
            assert is_selectable, "po void cannot be selected"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.php8_1
    @pytest.mark.hardwarelease
    def test_po_void_checkbox_can_be_unselected(self, setup):
        """
            Test Case ID: TC_UI_HL_0016
            Jira ID     : r25094694
            Objective   : Verify that PO void can be unselected

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/HardwareComponent/search

            Expected Outcome:
            - PO void can be unselected


        """
        tc_id = setup.get("tc_id_test_po_void_checkbox_can_be_unselected", None)
        hardware_lease_url = setup.get("hardware_lease_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that PO void can be unselected")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_po_void_checkbox_can_be_unselected")

            hardware_component_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_component_search_page, url)

            self.log.info("Opening the hardware component search page")
            self.open_hardware_lease_page(hardware_lease_url, environment)
            is_unselectable = self.check_if_po_void_can_be_unselected()
            assert is_unselectable, "po void cannot be selected"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

