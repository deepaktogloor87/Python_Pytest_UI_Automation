from selenium.webdriver.common.by import By

server_prebuild_page_locators = [

    ("HARDWARE_ID",(By.XPATH,'//*[@id="hardwareIdListField"]/input')),
    ("BASE_HARDWARE_ID",(By.XPATH,'//*[@id="serverprebuild_variables_0_baseserverid"]')),
    ("SOFTLAYER_TICKET_ID",(By.XPATH,'//*[@id="serverprebuild_variables_0_ticketid"]')),
    ("SEARCH_PREBUILD_JOBS",(By.XPATH,'//*[@id="ui-id-3"]')),
    ("SPJ_BASE_SERVER_ID",(By.XPATH,'//*[@id="serverprebuild_variables_0_serverid"]')),
    ("SPJ_SOFTLAYER_TICKET_ID",(By.XPATH,'//*[@id="serverprebuild_variables_0_softlayerticketid"]')),
    ("SPJ_PREBUILD_JOB_ID",(By.XPATH,'//*[@id="serverprebuild_variables_0_prebuildjobid"]')),
    ("SPJ_USER_ID",(By.XPATH,'//*[@id="serverprebuild_variables_0_userid"]')),
    ("CPJ_CREATE_BUTTON",(By.XPATH,'//*[@id="serverprebuild_submit"]')),
    ("CPJ_RESET_BUTTON",(By.XPATH,'//*[@id="serverprebuild_create_form_reset"]')),
    ("SPJ_SEARCH_BUTTON",(By.XPATH,'//*[@id="serverprebuild_submit" and @value="Search"]')),
    ("SPJ_ROP_BUTTON",(By.CSS_SELECTOR,'#serverprebuild_create_form_reset')),
    # ... any other locators related to the server prebuild Page

]