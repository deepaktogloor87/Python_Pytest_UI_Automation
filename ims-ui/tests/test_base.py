import pytest
from utilities.logger import setup_logger
from pages.login_page.login_page import LoginPage


@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass
