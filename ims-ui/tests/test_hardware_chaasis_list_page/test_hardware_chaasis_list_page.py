import pytest
from tests.test_hardware_chaasis_list_page.test_hardware_chaasis_list_page_helper import \
    TestHardwareChaasisListPageHelper
from tests.test_base import BaseTest
from utilities.read_json import read_and_parse_json
from utilities.read_properties import ReadConfig


class TestHardwareComponentSearchPage(BaseTest, TestHardwareChaasisListPageHelper):
    base_url = ReadConfig.get_application_url()
    username = ReadConfig.get_application_username()
    password = ReadConfig.get_application_password()

    @pytest.fixture(scope="function")
    def setup(self, logger):
        self.log = logger
        self.log.info("Setting up the test data file for use in the test")
        return read_and_parse_json(
            'tests/test_hardware_chaasis_list_page/testdata/hardware_chaasis_list_testdata.json')

    @pytest.mark.php8_1
    @pytest.mark.hardwarechaasislist
    def test_set_riser_card_capacity_to_any_value(self, setup):
        """
            Test Case ID: TC_UI_HCL_0001
            Jira ID     : r25094694
            Objective   : Verify that riser card capacity can be set to any value

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/HardwareComponent/search

            Expected Outcome:
            - Riser card capacity can be set to any value

        """
        tc_id = setup.get("tc_id_set_riser_card_capacity_to_any_value", None)
        hardware_chaasis_list_url = setup.get("hardware_chaasis_list_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: verify that riser card capacity can be set to any value")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_set_riser_card_capacity_to_any_value")

            hardware_component_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_component_search_page, url)

            self.log.info("Opening the hardware component search page")
            self.open_hardware_component_search_page(hardware_chaasis_list_url, environment)
            self.click_on_the_edit_link()
            self.click_on_add_an_attribute()
            result = self.select_raid_card_capacity_and_set_the_value_to_2()
            assert result, "Failed to get any result when serial number is inputed"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.php8_1
    @pytest.mark.hardwarechaasislist
    def test_ensure_that_2_riser_card_row_is_created(self, setup):
        """
            Test Case ID: TC_UI_HCL_0002
            Jira ID     : r25094694
            Objective   : Verify that riser card capacity rows on the page is 2

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/HardwareComponent/search

            Expected Outcome:
            - Riser card capacity rows on the page is 2

        """
        tc_id = setup.get("tc_id_ensure_that_2_riser_card_row_is_created", None)
        hardware_configuration_template_url = setup.get("hardware_configuration_template_url", None)
        chassis = setup.get("chassis", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: verify that riser card capacity rows on the page is 2")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_ensure_that_2_riser_card_row_is_created")

            hardware_component_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_component_search_page, url)

            self.log.info("Opening the hardware component search page")
            self.open_hardware_component_search_page(hardware_configuration_template_url, environment)
            self.select_the_chaasis(chassis)
            row_count = self.return_the_riser_card_rows()
            assert row_count == 2, "riser card capacity row count is not 2"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.php8_1
    @pytest.mark.hardwarechaasislist
    def test_hardware_template_can_be_saved_without_errors(self, setup):
        """
            Test Case ID: TC_UI_HCL_0003
            Jira ID     : r25094694
            Objective   : Verify that hardware configuration template can be saved without errors

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/HardwareComponent/search

            Expected Outcome:
            - Hardware configuration template can be saved without errors

        """
        tc_id = setup.get("tc_id_hardware_template_can_be_saved_without_errors", None)
        hardware_configuration_template_url = setup.get("hardware_configuration_template_url", None)
        chassis = setup.get("chassis", None)
        template_description = setup.get("template_description", None)
        PO = setup.get("PO", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: verify that that hardware configuration template can be saved without errors")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_hardware_template_can_be_saved_without_errors")

            hardware_component_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_component_search_page, url)

            self.log.info("Opening the hardware component search page")
            self.open_hardware_component_search_page(hardware_configuration_template_url, environment)
            self.type_the_description(template_description)
            self.select_the_chaasis(chassis)
            self.make_other_selection_and_save_the_page(PO)
            # row_count = self.return_the_riser_card_rows()
            # assert row_count == 2, "riser card capacity row count is not 2"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")
            
