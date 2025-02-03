from selenium.webdriver.common.by import By

hardware_component_search_page_locators = [

    ("SERIAL_NUMBER", (By.XPATH, '//*[@id="hardwarecomponent_search_serialnumbers"]')),
    ("SERIAL_NUMBER_ARROW", (By.XPATH, '//*[@id="hardwarecomponent_search_componentbyserialorid_action"]/img')),
    ("DISPLAY", (By.XPATH, '//*[@value="Display"]')),
    ("RESULT", (By.XPATH, '//*[@id="results_table_0"]')),
    ("COMPONENT_ID", (By.XPATH, '//*[@id="hardwarecomponent_search_id"]')),
    ("COMPONENTS_ATTACHED_TO_HARDWARE", (By.XPATH, '//*[@id="hardwarecomponent_search_attachedtohardware_action"]/img')),
    ("SOFTLAYER_SERIAL_NUMBER", (By.XPATH, '//*[@id="hardwarecomponent_search_hardware_serialnumbers"]')),
    ("MANUFACTURER_SERIAL_NUMBER", (By.XPATH, '//*[@id="hardwarecomponent_search_hardware_manufacturerserialnumbers"]')),
    ("HARDWARE_ID", (By.XPATH, '//*[@id="hardwarecomponent_search_hardware_id"]')),
    ("COMPONENT_DETAIL", (By.XPATH, '//*[@id="hardwarecomponent_search_componentdetail_action"]/img')),
    ("COMPONENT_STATUS", (By.XPATH, '//*[@id="hardwarecomponent_search_statuskeyname_"]')),
    ("LOT_NUMBER", (By.XPATH, '//*[@id="hardwarecomponent_search_lotnumber"]')),
    ("COMPONENTS_ATTACHED_TO_HARDWARE", (By.XPATH, '//*[@id="hardwarecomponent_search_attachedtohardware_action"]/img')),
    ("HARDWARE_STATUS", (By.XPATH, '//*[@id="hardwarecomponent_search_hardware_statuskeyname_"]')),
    ("ACCOUNT_ID", (By.XPATH, '//*[@id="hardwarecomponent_search_hardware_accountid"]')),
    ("HOSTNAME", (By.XPATH, '//*[@id="hardwarecomponent_search_hardware_hostname"]')),
    ("DOMAIN", (By.XPATH, '//*[@id="hardwarecomponent_search_hardware_domain"]')),
    ("FUNCTION_DROPDOWN", (By.XPATH, '//*[@id="hardwarecomponent_search_hardware_hardwarefunctioncode"]')),
    ("CHASSIS", (By.XPATH, '//*[@id="HardwareChassisSelect"]')),
    ("MAC_IPV4_IPV6", (By.XPATH, '//*[@id="hardwarecomponent_search_hardware_address"]')),
    ("EXPORT_CSV", (By.XPATH, '//*[@id="hardwarecomponent_search_form_submit"]')),
    ("EXPORT_EXCEL", (By.XPATH, '//*[@id="hardwarecomponent_search_form_submit"]')),
    ("SEND_AND_SHARE", (By.XPATH, '//*[@id="searchQueryUrlButton"]')),
    ("QUERY_URL", (By.XPATH, '//*[@id="inputField"]')),
    ("COMPONENT_EVENT", (By.XPATH, '//*[@id="hardwarecomponent_search_componentevents_action"]/img')),
    ("ACCOUNT_ID_DETAILS", (By.XPATH, '//*[@id="hardwarecomponent_search_eventaccountid"]')),
    ("HW_ID", (By.XPATH, '//*[@id="hardwarecomponent_search_eventhardwareid"]')),
    ("LOCATION_ELEMENT", (By.XPATH, '//*[@id="hardwarecomponent_search_eventlocationid_container"]/select')),
    ("ID_LINK", (By.XPATH, '//*[@id="results_table_0"]/tr/td[4]/a'))
    # ... any other locators related to the Hardware Component Search Page
]
