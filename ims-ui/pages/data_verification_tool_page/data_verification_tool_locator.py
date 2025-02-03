from selenium.webdriver.common.by import By

data_verification_tool_page_locators = [

    ("RUN_ADDRESS_TEST_BUTTON", (By.XPATH, '//*[@id="datacenterverificationtool_address_form_submit"]')),
    ("RUN_LOCATION_TEST_BUTTON", (By.XPATH, '//*[@id="datacenterverificationtool_location_form_submit"]')),
    ("RUN_POOLS_TEST_BUTTON", (By.XPATH, '//*[@id="datacenterverificationtool_pools_form_submit"]')),
    ("RUN_POWER_TEST_BUTTON", (By.XPATH, '//*[@id="datacenterverificationtool_power_form_submit"]')),
    ("RUN_CHECKIN_TEST_BUTTON", (By.XPATH, '//*[@id="datacenterverificationtool_checkin_form_submit"]')),
    ("RUN_CHECKIN_TEST_BUTTON", (By.XPATH, '//*[@id="datacenterverificationtool_scan_form_submit"]')),
    ("DATACENTER_TO_VERIFY", (By.XPATH, '//*[@id="location_id"]')),
    ("RUN_ALL_TESTS", (By.XPATH, '//*[@id="_submit" and @value="Run All Tests"]')),
    ("EXPORT_TEST_RESULTS", (By.XPATH, '//*[@id="_submit" and @value="Export Test Results"]')),
    # ... any other locators related to the data verification tool page
]
