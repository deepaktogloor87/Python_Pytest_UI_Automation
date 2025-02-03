from selenium.webdriver.common.by import By

hardware_update_page_locators = [

    ("JBOD_C", (By.XPATH, '//*[@id="storage_group_action_20844290"]')),
    ("JBOD_D", (By.XPATH, '//*[@id="storage_group_action_20844392"]')),
    ("STORAGE_GROUP", (By.XPATH, '//*[@id="hardware_storagegroups_action_column"]')),
    ("JBOD_SSN", (By.XPATH, '//*[@id="storage_viewvolumegroupdetails_serialnumber"]')),
    ("JBOD_WWN", (By.XPATH, '//*[@id="storage_viewvolumegroupdetails_worldwidename"]')),
    ("CLICK_MAINTENANCE", (By.XPATH, '//*[@id="show_maintenance_form_link"]')),
    ("OTHER_CHECKBOX", (By.XPATH, '//*[@id="hardware_update_maintenanceentries_43_maintenancetypeid"]')),
    ("OTHER_TEXTBOX", (By.XPATH, '//*[@id="hardware_update_maintenanceentries_43_notes"]')),
    ("CONTINUE_BTN", (By.XPATH, '//*[@id="hardware_update_submit_row"]/input[@type="submit"]')),
    ("OTHER_MAINTENANCE_NOTES", (By.XPATH, '//*[contains(text(),"Other")]')),
    ("REMOTE_MGMT_CTRL", (By.XPATH, '//*[contains(text(),"Remote Management Control")]')),
    ("IPMI_REMOTE_MANAGEMENT_SUMMARY", (By.XPATH, '//*[@id="ui-id-1"]')),
    ("REDFISH_REMOTE_MANAGEMENT_SUMMARY", (By.XPATH, '//*[@id="ui-id-3"]')),
    ("REMOTE_MGMT_DROPDOWN", (By.XPATH, '//*[@id="remotemgmtcommands_names"]')),
    ("INITIATE_COMMAND", (By.XPATH, '/html/body/div[1]/table[3]/tbody/tr/td[3]/table[3]/tbody/tr/td/div/div[2]/form/input')),
    ("POWER_STATUS", (By.XPATH, '//*[@id="ui-id-4"]')),
    ("UIM_MANAGED_ASSET", (By.XPATH, '//*[@id="hardware_update_ngdcassetflag"]')),
    ("GENERAL_TAB_CONTINUE_BTN", (By.XPATH, '//*[@value="Continue"]')),
    # ... any other locators related to the Hardware update page
]