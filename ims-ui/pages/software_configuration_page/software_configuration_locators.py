from selenium.webdriver.common.by import By

software_configuration_page_locators = [

    ("TEMPLATE", (By.XPATH, '//*[contains(@id,"template_details")][1]/td[1]/a')),
    ("SECTION", (By.XPATH, '//*[@id="template_98_section_190_details_action"]/img')),
    ("AVAILABLE_FRAGMENT", (By.XPATH, '//*[@id="fragment_add_"]')),
    ("ASSIGN_FRAGMENT_BTN", (By.XPATH, '//*[@id="softwareconfiguration_assignfragments_190_form_submit"]')),
    # ("ASSIGNED_FRAGMENT", (By.XPATH, '//*[contains(text(), "Preeseed Header")]/../../../..')),
    ("ASSIGNED_FRAGMENT", (By.XPATH, '//*[contains(text(), "NIX Software")]/../../../..')),
    # ... any other locators related to the Software Configuration Page
]
