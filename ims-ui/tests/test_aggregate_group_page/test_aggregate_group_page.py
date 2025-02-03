import time

import pytest
from selenium.common import TimeoutException
from tests.test_aggregate_group_page.test_aggregate_group_page_helper import TestAggregateGroupPageHelper
from tests.test_base import BaseTest
from utilities.read_json import read_and_parse_json
from utilities.read_properties import ReadConfig


class TestAggregateGroupPage(BaseTest, TestAggregateGroupPageHelper):
    base_url = ReadConfig.get_application_url()
    username = ReadConfig.get_application_username()
    password = ReadConfig.get_application_password()

    @pytest.fixture(scope="function")
    def setup(self, logger):
        self.log = logger
        self.log.info("Setting up the test data file for use in the test")
        return read_and_parse_json(
            'tests/test_aggregate_group_page/testdata/aggregate_group_page_testdata.json')

    @pytest.mark.aggregategroup
    @pytest.mark.php8_1
    def test_user_is_able_to_create_aggregate_group(self, setup):
        """
            Test Case ID: TC_UI_AG_0001
            Jira ID     : r25444054
            Objective   : Verify that user is able to create aggregate group

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - User is able to create aggregate group

        """
        tc_id = setup.get("tc_id_user_is_able_to_create_aggregate_group", None)
        aggregate_group_url = setup.get("aggregate_group_url", None)
        new_group = setup.get("new_group", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that user is able to create aggregate group")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_user_is_able_to_create_aggregate_group")

            hardware_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_search_page, url)

            self.log.info("Opening the aggregate group page")
            self.open_aggregate_group_page(aggregate_group_url, environment)

            self.log.info("Creating a new aggregate group")
            status_msg  = self.create_a_new_aggregate_group(new_group)

            self.log.info(f"status msg: {status_msg}")
            assert status_msg == "Successfully created Aggregate Group", "Aggregate group is not created successfully"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")

    @pytest.mark.aggregategroup
    @pytest.mark.php8_1
    def test_user_is_able_to_delete_aggregate_group(self, setup):
        """
            Test Case ID: TC_UI_AG_0002
            Jira ID     : r25444054
            Objective   : Verify that user is able to delete aggregate group

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - User is able to delete aggregate group

        """
        tc_id = setup.get("tc_id_user_is_able_to_delete_aggregate_group", None)
        aggregate_group_url = setup.get("aggregate_group_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that user is able to delete aggregate group")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_user_is_able_to_delete_aggregate_group")

            hardware_search_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, hardware_search_page, url)

            self.log.info("Opening the aggregate group page")
            self.open_aggregate_group_page(aggregate_group_url, environment)

            self.log.info("Creating a new aggregate group")
            status_msg = self.delete_aggregate_group()

            self.log.info(f"status msg: {status_msg}")
            assert status_msg == "Deleted", "Aggregate group is not deleted successfully"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")
            