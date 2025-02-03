from selenium.webdriver.common.by import By

network_monitoring_locators = [

    ("NETWORK_MONITORING_LINKS", (By.XPATH, '//*[@id="layoutContentBody"]/tbody/tr/td/p[{i}]/a')),
    ("TOTAL_LINKS_NETWORK_MONITORING",(By.XPATH,'//*[@id="layoutContentBody"]/tbody/tr/td/p//a'))
    # ... any other locators related to the Network Monitoring Page

]
