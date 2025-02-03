from selenium.webdriver.common.by import By

cancel_virtual_process_instance_locators = [

    ("CANCEL_VIRTUAL_PROCESS_INSTANCE", (By.XPATH, '//a[contains(text(), "Cancel Virtual Process Instance")]')),
    ("INSTRUCTIONS", (By.XPATH,
                      '//p[contains(text(), "This tool should be used with caution as cancelling incomplete process instances may leave resources in an invalid state.")]')),
    ("PROCESS_INSTANCE_TEXT_BOX", (By.XPATH, '//*[@id="developmentvirtualtools_processinstanceid"]')),
    ("PROCESS_INSTANCE_VIEW_BUTTON",
     (By.XPATH, '//*[@id="_developmentvirtualtools_cancelprocessinstance_form_submit"]')),
    ("PROCESS_INSTANCE_INFORMATION",
     (By.XPATH, '//*[@id="_developmentvirtualtools_cancelprocessinstance_form"]/b/b/table/tbody')),
    ("ERROR_MSG", (By.XPATH, '//*[contains(text(), "An error has occurred")]')),
    ("CANCEL_BTN",
     (By.XPATH, '//input[contains(@id, "developmentvirtualtools_cancelprocessinstance") and @value="Cancel"]')),
    # ... any other locators related to the Cancel virtual process instance

]
