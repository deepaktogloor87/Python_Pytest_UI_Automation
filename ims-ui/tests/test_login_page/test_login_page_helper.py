from pages.login_page.login_page import LoginPage
import allure
from allure_commons.types import AttachmentType


class TestLoginPageHelper:

    def login_to_app(self, driver, username, password, return_object):
        self.loginPage = LoginPage(driver)
        self.loginPage.do_login(username, password, return_object)

    def get_title_of_the_app(self):
        return self.loginPage.get_page_title()

    def logout_from_app(self):
        self.loginPage.logout_user()

    def pull_logout_info(self):
        return self.loginPage.capture_logout_message()

    @staticmethod
    def get_screenshot_on_error(driver, name):
        allure.attach(driver.get_screenshot_as_png(), name=name,
                      attachment_type=AttachmentType.PNG)
