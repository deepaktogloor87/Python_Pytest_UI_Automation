from selenium.webdriver.common.by import By

host_evacuation_page_locators = [

    ("CREATE_TICKET_CHECKBOX",(By.XPATH,"//*[contains(@id,'virtual_choosehostevacuationtype')]")),
    ("CREATE_TICKET_FORM",(By.XPATH,"//*[contains(@id,'createhostevacuationnotification_content')]")),
    ("CREATE_TICKET_TITLE",(By.XPATH,"//*[contains(@id,'reatehostevacuationnotification_title')]")),
    ("TICKET_ACCOUNT_ID",(By.XPATH,"/html/body/div[1]/table[3]/tbody/tr/td[3]/table[3]/tbody/tr/td/div[7]/table[1]/tbody/tr[4]/td[3]/a")),
    ("TICKET_COMPANY_DETAILS",(By.XPATH,"//*[@id='layoutContentBody']/tbody/tr/td/div[7]/table[1]/tbody/tr[5]/td[3]")),
    ("TICKET_ACCOUNT_ID",(By.XPATH,"/html/body/div[1]/table[3]/tbody/tr/td[3]/table[3]/tbody/tr/td/div[7]/table[1]/tbody/tr[4]/td[3]/a")),
    ("TICKET_GROUP_INFO",(By.XPATH,"//*[@id='layoutContentBody']/tbody/tr/td/div[7]/table[1]/tbody/tr[15]/td[3]"))
    # ... any other locators related to the HostEvacuationTypePage

]