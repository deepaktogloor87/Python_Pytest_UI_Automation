from selenium.webdriver.common.by import By

aggregate_group_page_locators = [

    ("DESCRIPTION", (By.XPATH, '//*[@id="hardwarecomponentmodelgenericaggregategroup_description"]')),
    ("STATUS_MESSAGE", (By.XPATH, '//*[@id="status_messages"]/span')),
    ("SUBMIT", (By.XPATH, '//*[@id="hardwarecomponentmodelgenericaggregategroup_submit"]')),
    ("CREATE_AGGREGATE_GRP_LINK", (By.XPATH, '//*[@id="layoutContentBody"]/tbody/tr/td/a')),
    ("DELETE", (By.XPATH, '//td[contains(text(), "Creating a new group for automation")]/following-sibling::*[5]/a[2]')),
    # ... any other locators related to the Aggregate group page

]