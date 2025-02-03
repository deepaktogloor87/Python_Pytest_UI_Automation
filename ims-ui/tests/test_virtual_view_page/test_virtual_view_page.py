import time

import pytest
from selenium.common import TimeoutException
from tests.test_virtual_view_page.test_virtual_view_page_helper import TestVirtualViewPageHelper
from tests.test_base import BaseTest
from utilities.read_json import read_and_parse_json
from utilities.read_properties import ReadConfig


class TestVirtualViewPage(BaseTest, TestVirtualViewPageHelper):
    base_url = ReadConfig.get_application_url()
    username = ReadConfig.get_application_username()
    password = ReadConfig.get_application_password()

    @pytest.fixture(scope="function")
    def setup(self, logger):
        self.log = logger
        self.log.info("Setting up the test data file for use in the test")
        return read_and_parse_json(
            'tests/test_virtual_view_page/testdata/virtual_view_page_test_data.json')

    @pytest.mark.virtualview
    def test_reveal_the_virtual_view_guest_password(self, setup):
        """
            Test Case ID: TC_UI_VV_0001
            Jira ID     : r25094694
            Objective   : Verify that password is masked by "click to display" link

            Precondition:
            - User have access to IMS qa environment stable branch

            Steps:
            - go the qa env url:
               https://stable.internal.qadal0901.softlayer.local/Virtual/updatePool/3/856795

            Expected Outcome:
            - When user clicks on click to display link the password details are shown


        """
        tc_id = setup.get("tc_id_reveal_the_virtual_view_guest_password", None)
        virtual_view_url = setup.get("virtual_view_url", None)
        environment = setup.get("environment", None)
        try:
            self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
            self.log.info("Objective: Verify that password is masked by \"click to display\" link")
            self.log.info("Precondition: User has access to IMS qa environment stable branch")
            self.log.info(
                "Starting test: test_reveal_the_virtual_view_guest_password")

            update_pool_page = setup.get("return_object", None)
            self.log.info(f"Navigating to qa environment URL: http://{environment}.internal.qadal0901.softlayer.local/")

            url = self.construct_url_with_branch_name(environment)

            self.log.info("Entering username and password for login")
            self.login_to_app(self.driver, self.username, self.password, update_pool_page, url)

            self.log.info("Opening the virtual view page")
            self.open_virtual_view_page(virtual_view_url, environment)

            self.log.info("Checking the password mask link name")
            password_mask_link = self.check_if_click_to_view_password_link_present()

            self.log.info(f"the password mask link name is {password_mask_link}")
            assert password_mask_link == "Click to View Password", "The password mask link is not present"
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id} ===")