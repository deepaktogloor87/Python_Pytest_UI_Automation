from selenium.webdriver.common.by import By

hardware_transaction_page_locators = [

    ("ALL_HD_TXN_LINKS", (By.XPATH, '//*[@id="layoutContentBody"]/tbody/tr/td/a[{i}]')),
    ("TOTAL_LINKS", (By.XPATH, "//*[@id='layoutContentBody']/tbody/tr/td/a"))
    # ... any other locators related to the Hardware Transaction page

]