from selenium.webdriver.common.by import By

accounting_page_locators = [

    ("ALL_ACCOUNTING_LINKS",(By.XPATH,'//*[@id="accounting_tab"]/ul/li[{i}]/a')),
    ("TOTAL_LINKS",(By.XPATH,"//*[@id='accounting_tab']//a"))
    # ... any other locators related to the AccountingPage

]