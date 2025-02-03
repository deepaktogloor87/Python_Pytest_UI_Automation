from selenium.webdriver.common.by import By

hardware_chaasis_list_locators = [

    ("EDIT", (By.XPATH, '//*[@id="hardwarechassis_addchassis"]/tbody/tr[6]/td[6]/a')),
    ("ADD_AN_ATTRIBUTE", (By.XPATH, '//*[@id="addHardwareChassisAttributeRow"]/td/a')),
    ("ATTRIBUTE", (By.XPATH, '//*[@id="hardwarechassis_update_attributes_0_typeid"]')),
    ("ATTRIBUTE_VALUE", (By.XPATH, '//*[@id="hardwarechassis_update_attributes_0_value"]')),
    ("STATUS_MSG", (By.XPATH, '//*[@id="status_messages"]/span')),
    ("CONTINUE_BTN", (By.XPATH, '//*[@name="continueButton"]')),
    ("CHASSIS", (By.XPATH, '//*[@id="hardwareconfigurationtemplate_template_hardwarechassisid"]')),
    ("RISER_CARD_ROWS", (By.XPATH, '//*[contains(@id,"riser_card_row")]')),
    ("DESCRIPTION", (By.XPATH, '//*[@id="hardwareconfigurationtemplate_template_description"]')),
    ("USB_DEVICE", (By.XPATH, '//*[@id="hardwareconfigurationtemplate_template_32_0"]')),
    ("RISER_CARD_1", (By.XPATH, '//*[@id="hardwareconfigurationtemplate_template_33_0"]')),
    ("RISER_CARD_2", (By.XPATH, '//*[@id="hardwareconfigurationtemplate_template_33_1"]')),
    ("MOTHERBOARD", (By.XPATH, '//*[@id="hardwareconfigurationtemplate_template_3_0"]')),
    ("PROCESSOR1", (By.XPATH, '//*[@id="hardwareconfigurationtemplate_template_2_0"]')),
    ("PROCESSOR2", (By.XPATH, '//*[@id="hardwareconfigurationtemplate_template_2_1"]')),
    ("EXPANSION_CARD", (By.XPATH, '//*[@id="hardwareconfigurationtemplate_template_29_0"]')),
    ("RAM", (By.XPATH, '//*[@id="hardwareconfigurationtemplate_template_4_0"]')),
    ("DRIVE_CONTROLLER", (By.XPATH, '//*[@id="hardwareconfigurationtemplate_template_5_0"]')),
    ("BATTERY", (By.XPATH, '//*[@id="hardwareconfigurationtemplate_template_13_0"]')),
    ("HARD_DRIVE", (By.XPATH, '//*[@id="hardwareconfigurationtemplate_template_1_0"]')),
    ("REMOTE_MGMT_CARD", (By.XPATH, '//*[@id="hardwareconfigurationtemplate_template_14_0"]')),
    ("NETWORK_CARD", (By.XPATH, '//*[@id="hardwareconfigurationtemplate_template_16_0"]')),
    ("NETWORK_OPTIC", (By.XPATH, '//*[@id="hardwareconfigurationtemplate_template_28_0"]')),
    ("POWER_SUPPLY", (By.XPATH, '//*[@id="hardwareconfigurationtemplate_template_19_0"]')),
    ("BACKPLANE", (By.XPATH, '//*[@id="hardwareconfigurationtemplate_template_18_0"]')),
    ("FAN", (By.XPATH, '//*[@id="hardwareconfigurationtemplate_template_24_0"]')),
    ("VIDEO_CARD", (By.XPATH, '//*[@id="hardwareconfigurationtemplate_template_12_0"]')),
    ("GPU", (By.XPATH, '//*[@id="hardwareconfigurationtemplate_template_20_0"]')),
    ("LINE_CARD", (By.XPATH, '//*[@id="hardwareconfigurationtemplate_template_21_0"]')),
    ("SECURITY_DEVICE", (By.XPATH, '//*[@id="hardwareconfigurationtemplate_template_26_0"]')),
    ("INDEP_MGMT_PORT_CHECKBOX", (By.XPATH, '//*[@id="hardwareconfigurationtemplate_template_managementportflag"]')),
    ("PO", (By.XPATH, '//*[@id="hardwareconfigurationtemplate_template_hardwareleaseid_textField"]')),
    ("SAVE_TEMPLATE", (By.XPATH, '//*[@id="hardwareconfigurationtemplate_template_templatesave"]'))
    # ... any other locators related to the Hardware Chaasis List Page
]