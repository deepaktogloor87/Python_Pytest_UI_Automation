from selenium.webdriver.common.by import By

service_inventory_report_page_locators = [

    ("ACCOUNT_ID",(By.XPATH,'//*[@id="searchfilter_0_data"]')),
    ("COMPANY_NAME",(By.XPATH,'//*[@id="searchfilter_2_data"]')),
    ("HOST_NAME",(By.XPATH,'//*[@id="searchfilter_4_data"]')),
    ("IP_ADDR",(By.XPATH,'//*[@id="searchfilter_6_data"]')),
    ("EVAULT_USERNAME",(By.XPATH,'//*[@id="searchfilter_5_data"]')),
    ("COMPANY_NAME_CHECKBOX",(By.XPATH,'//*[@id="searchfilter_2_method"]')),
    ("HOSTNAME_CHECKBOX",(By.XPATH,'//*[@id="searchfilter_4_method"]')),
    ("IP_ADDR_CHECKBOX",(By.XPATH,'//*[@id="searchfilter_6_method"]')),
    ("EVAULT_USERNAME_CHECKBOX",(By.XPATH,'//*[@id="searchfilter_5_method"]')),
    ("EVAULT_USERNAME_CHECKBOX",(By.XPATH,'//*[@name="data[SearchFilter][8][data]"]')),
    ("OBJECT_TYPE",(By.XPATH,'//*[@id="searchfilter_1_data" and @name="data[SearchFilter][1][data]"]')),
    ("OBJECT_STATUS",(By.XPATH,'//*[@id="searchfilter_3_data" and @name="data[SearchFilter][3][data]"]')),
    ("MANAGED_SERVER",(By.XPATH,'//*[@name="data[SearchFilter][7][data]"]')),
    ("SEARCH_BTN",(By.XPATH,'//*[@value="Search" and @class="submit_base"]')),
    # ... any other locators related to the Service Inventory Report Page

]