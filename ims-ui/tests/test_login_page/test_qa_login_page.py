from pages.login_page.login_page import LoginPage
from tests.test_base import BaseTest
from utilities.read_properties import ReadConfig
import pytest
from utilities.read_json import read_and_parse_json
from tests.test_login_page.test_login_page_helper import TestLoginPageHelper


class TestLoginPage(BaseTest, TestLoginPageHelper):
    base_url = ReadConfig.get_application_url()
    username = ReadConfig.get_application_username()
    password = ReadConfig.get_application_password()

    @pytest.fixture(scope="function")
    def setup(self, logger):
        self.log = logger
        self.log.info("Setting up the test data file for use in the test")
        return read_and_parse_json('tests/test_login_page/testdata/login_page_testdata.json')

    @pytest.mark.jira(id="2389")
    @pytest.mark.loginpage
    def test_user_login_session(self, setup):
        """
        Test Case ID:
        Objective: Verify the user registered with IMS can login successfully

        Precondition:
        - User have access to IMS qa environment

        Steps:
        1. go the qa env url: http://stable.internal.qadal0901.softlayer.local/
        2. Type in the username and password
        3. Click on login button

        Expected Outcome:
        - User is redirected to the dashboard
        - Verify Title "SoftLayer - Ticket Search"
        """
        tc_id = setup.get("tc_id_user_login_session", None)
        self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
        self.log.info("Objective: Verify the user registered with IMS can login successfully.")
        self.log.info("Precondition: User has access to IMS qa environment.")
        self.log.info("Starting test: test_user_login_session")

        login_page = setup.get("return_object", None)
        qa_env_page_title = setup.get("page_title_qa", None)
        try:
            self.log.info("Navigating to qa environment URL: http://stable.internal.qadal0901.softlayer.local/")

            self.log.info("Entering username and password for login.")
            self.login_to_app(self.driver, self.username, self.password, login_page)

            self.log.info("Clicked login button, waiting for redirection.")
            self.log.info("Login successful, retrieving the page title.")

            title = self.get_title_of_the_app()
            self.log.info(f"the title of the page is: {title}")
            assert qa_env_page_title == title, "Login Failed"
        except KeyError as e:
            self.log.error("KeyError: 'page_title_qa' not found in setup")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        except AssertionError as e:
            self.log.error(f"Assertion Error: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id}===")

    @pytest.mark.jira(id="2389")
    @pytest.mark.loginpage
    def test_user_logout_session(self, setup):
        """
        Test Case ID:
        Objective: Verify the user registered with IMS can login successfully

        Precondition:
        - User have access to IMS qa environment

        Steps:
        1. go the qa env url: http://stable.internal.qadal0901.softlayer.local/
        2. Type in the username and password
        3. Click on login button
        4. Click on the logout link

        Expected Outcome:
        - User is redirected to the dashboard
        - Verify Logout message is You have logged out of the SoftLayer Internal Management Portal.
        """

        tc_id = setup.get("tc_id_user_logout_session", None)
        self.log.info(f"=== TEST CASE ID: [{tc_id}] ===")
        self.log.info("Objective: Verify the user registered with IMS can logout successfully.")
        self.log.info("Precondition: User has access to IMS qa environment.")
        self.log.info("Starting test: test_user_logout_session")

        login_page = setup.get("return_object", None)
        logout_text_captured = None
        logout_message = setup.get("logout_text", None)  # Using get() to avoid KeyError
        try:
            self.log.info("Navigating to qa environment URL: http://stable.internal.qadal0901.softlayer.local/")

            self.log.info("Entering username and password for login.")
            self.login_to_app(self.driver, self.username, self.password, login_page)

            self.log.info("Clicked login button, waiting for redirection.")
            self.log.info("Login successful, attempting to logout.")

            self.logout_from_app()
            self.log.info("Logout initiated.")

            logout_text_captured = self.pull_logout_info()
            self.log.info(f"Captured logout message: {logout_text_captured}.")

            assert logout_message == logout_text_captured
        except AssertionError as e:
            self.log.error(
                f"Assertion Error: {e}. Expected logout message: '{logout_message}',"
                f" but got: '{logout_text_captured}'.")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        except Exception as e:
            self.log.error(f"An error occurred: {e}")
            self.get_screenshot_on_error(self.driver, name=tc_id)
            raise e
        finally:
            self.log.info(f"=== END OF TEST CASE {tc_id}===")
