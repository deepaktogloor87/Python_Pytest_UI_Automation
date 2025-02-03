import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from utilities.logger import setup_logger
from datetime import datetime


@pytest.fixture(params=["chrome"], scope="function")
def init_driver(request):
    project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    download_dir = os.path.join(project_dir, 'downloads')
    os.makedirs(download_dir, exist_ok=True)
    # Create an instance of the driver based on the browser type.
    if request.param == "chrome":
        options = webdriver.ChromeOptions()
        # headless mode configuration
        # options.add_argument('--headless')
        # options.add_argument('--no-sandbox')
        # options.add_argument('--disable-dev-shm-usage')
        # headless mode configuration ends
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        options.add_experimental_option("prefs", {
            "download.default_directory": download_dir,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        })
        web_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    elif request.param == "firefox":
        web_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

    else:
        web_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    # This ensures the driver is accessible in the test method.

    request.cls.driver = web_driver

    # web_driver.implicitly_wait(10)

    yield

    # Capture screenshot after the test finishes but before the browser closes.
    # Use the test method name to name the screenshot for better traceability.
    screenshot_directory = "screenshots"
    if not os.path.exists(screenshot_directory):
        os.makedirs(screenshot_directory)

    # Get the current date and time
    current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

    # Get the method's name and prepend the current date and time to it
    screenshot_name = f"{current_time}_{request.node.function.__name__}.png"
    screenshot_path = os.path.join(screenshot_directory, screenshot_name)

    web_driver.save_screenshot(screenshot_path)

    # web_driver.save_screenshot(screenshot_path)
    web_driver.quit()


@pytest.fixture(scope='session')
def logger(request):
    log = setup_logger('apollo')
    return log


def pytest_runtest_protocol(item, nextitem):
    if item.function.__doc__:
        print("\n", item.function.__doc__.strip())
    return None
