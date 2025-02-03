from selenium.webdriver.common.by import By

reports_page_locators = [

    ("ACCOUNTING_TAB", (By.XPATH, '//*[@id="ui-id-1"]')),
    ("ACCOUNTING_LINK", (By.XPATH, '//*[@id="accounting_tab"]/ul/li[{i}]/a')),
    ("ALL_ACCOUNTING_LINK", (By.XPATH, '//*[@id="accounting_tab"]/ul/li/a')),
    ("SALES_TAB", (By.XPATH, '//*[@id="ui-id-2"]')),
    ("SALES_LINK", (By.XPATH, '//*[@id="sales_tab"]/ul/li[{i}]/a')),
    ("ALL_SALES_LINK", (By.XPATH, '//*[@id="sales_tab"]/ul/li/a')),
    ("DATACENTER_TAB", (By.XPATH, '//*[@id="ui-id-3"]')),
    ("DATACENTER_LINK", (By.XPATH, '//*[@id="datacenter_tab"]/ul/li[{i}]/a')),
    ("ALL_DATACENTER_LINK", (By.XPATH, '//*[@id="datacenter_tab"]/ul/li/a')),
    ("TICKETS_TAB", (By.XPATH, '//*[@id="ui-id-4"]')),
    ("TICKETS_LINK", (By.XPATH, '//*[@id="tickets_tab"]/ul/li[{i}]/a')),
    ("ALL_TICKETS_LINK", (By.XPATH, '//*[@id="tickets_tab"]/ul/li/a')),
    ("MISC_TAB", (By.XPATH, '//*[@id="ui-id-5"]')),
    ("MISC_LINK", (By.XPATH, '//*[@id="misc_tab"]/ul/li[{i}]/a')),
    ("ALL_MISC_LINK", (By.XPATH, '//*[@id="misc_tab"]/ul/li/a'))
    # ... any other locators related to the Reports Page

]
