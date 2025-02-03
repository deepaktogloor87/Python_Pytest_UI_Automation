from selenium.webdriver.common.by import By

network_firewall_page_locators = [

    ("ALL_NETWORK_FIREWALL_LINKS",(By.XPATH,'//*[@id="layoutContentBody"]/tbody/tr/td/a[{i}]')),
    ("TOTAL_LINKS",(By.XPATH,"//*[@id='layoutContentBody']/tbody/tr/td/a"))
    # ... any other locators related to the network firewall Page

]