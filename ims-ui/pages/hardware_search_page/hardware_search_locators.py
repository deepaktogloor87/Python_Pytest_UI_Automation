from selenium.webdriver.common.by import By

hardware_search_page_locators = [

    ("LOCATION", (By.XPATH, '//*[@id="hardware_search_locationid_chooser"]')),
    ("HARDWARE_FUNCTION", (By.XPATH, '//*[@id="hardware_search_hardwarechassis_hardwarefunctioncode"]')),
    ("UIM_MANAGED_ASSET", (By.XPATH, '//*[@id="hardware_search_ngdcassetflag"]')),
    ("UIM_MANAGED_ASSET", (By.XPATH, '//*[@id="hardware_search_tags_tag_internal"]')),
    ("HARDWARE_POOL", (By.XPATH, '//*[@id="hardware_search_hardwarepoolid"]')),
    ("POOLED_SERVERS", (By.XPATH, '//*[@id="hardware_search_pooledservers"]')),
    ("HARDWARE_POOL_STATUS", (By.XPATH, '//*[@name="data[Hardware][search][hardwarePoolStatus]"]')),
    ("GENERIC_COMPONENT", (By.XPATH, '//*[@id="HardwareGenericComponentSelect"]')),
    ("SPECIFIC_COMPONENT", (By.XPATH, '//*[@id="HardwareGenericComponentSelect"]')),
    ("CHASSIS", (By.XPATH, '//*[@id="HardwareChassisSelect"]')),
    ("DISPLAY", (By.XPATH, '//*[@name="data[Hardware][search][output]" and @value="Display"]')),
    ("EXPORT_CSV", (By.XPATH, '//*[@name="data[Hardware][search][output]" and @value="Export CSV"]')),
    ("EXPORT_EXCEL", (By.XPATH, '//*[@name="data[Hardware][search][output]" and @value="Export Origin Certificates"]')),
    ("EXPORT_ORIGIN_CERTIFICATES", (By.XPATH, '//*[@id="HardwareChassisSelect"]')),
    ("SAVE_AND_SHARE_SEARCH_QUERY_URL", (By.XPATH, '//*[@id="searchQueryUrlButton"]')),
    ("HARDWARE_ID", (By.XPATH, '//*[@id="hardware_search_id"]')),
    ("VIRTUAL_HOST_ID", (By.XPATH, '//*[@id="hardware_search_virtualhostid"]')),
    ("MANUFACTURER_SERIAL_NUMBER", (By.XPATH, '//*[@id="hardware_search_manufacturerserialnumbers"]')),
    ("SOFTLAYER_SERIAL_NUMBER", (By.XPATH, '//*[@id="hardware_search_serialnumbers"]')),
    ("ACCOUNT_ID", (By.XPATH, '//*[@id="hardware_search_accountid"]')),
    ("CHASSIS_SCIP_ID", (By.XPATH, '//*[@id="hardware_search_hardwarechassis_scip"]')),
    ("HARDWARE_COMPONENT_MODEL_SCIP_ID",
     (By.XPATH, '//*[@id="hardware_search_components_hardwarecomponentmodel_scip"]')),
    ("MAC/IPV4/IPV6_ADDRESS", (By.XPATH, '//*[@id="hardware_search_address"]')),
    ("INTERNAL_NOTES", (By.XPATH, '//*[@id="hardware_search_internalnotes"]')),
    # ... any other locators related to the Hardware Search Page

]
