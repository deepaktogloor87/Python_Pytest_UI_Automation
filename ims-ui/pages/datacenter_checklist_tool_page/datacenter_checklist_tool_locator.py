from selenium.webdriver.common.by import By

datacenter_checklist_tool_page_locators = [

    ("START_NEW_DATACENTER_VERIFICATION_ARROW", (By.XPATH, '//*[@id="image_startverificationworkflow"]')),
    ("START_BTN", (By.XPATH, '//*[@id="datacenterchecklisttool_startverificationworkflow_form_submit"]')),
    ("SELECT_DATACENTER_DROPDOWN", (By.XPATH, '//*[@id="datacenterchecklisttool_startverificationworkflow_datacenterid"]')),
    ("CHECKLIST_HEADING", (By.CSS_SELECTOR, 'th.rotate > div > span')),
    ("LEGEND_TABLE", (By.CSS_SELECTOR, '#legend_table tr')),
    # ... any other locators related to the datacenter checklist tool page
]
