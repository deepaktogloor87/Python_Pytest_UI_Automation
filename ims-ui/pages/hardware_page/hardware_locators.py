from selenium.webdriver.common.by import By

hardware_page_locators = [

    ("LINKS_UNDER_HARDWARE",(By.XPATH,'//*[@id="hardware_tab"]/ul[2]/li[{i}]/a')),
    ("LINKS_UNDER_FIND",(By.XPATH,'//*[@id="hardware_tab"]/ul/li[{i}]/a')),
    ("TOTAL_LINKS_FIND",(By.XPATH,'//*[@id="hardware_tab"]/ul[1]/*/a')),
    ("TOTAL_LINKS_HARDWARE",(By.XPATH,'//*[@id="hardware_tab"]/ul[2]//a'))
    # ... any other locators related to the Hardware Page
]