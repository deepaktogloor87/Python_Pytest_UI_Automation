from selenium.webdriver.common.by import By

hardware_lease_page_locators = [

    ("DEPARTMENT", (By.XPATH, '//*[@id="department_id"]')),
    ("SAVE", (By.XPATH, '//*[@id="hardwarelease_lineitems_form_submit"]')),
    ("SHIP_TO_ADDR", (By.XPATH, '//*[@id="hardwarelease_shipto"]')),
    ("LEAD_TIME", (By.XPATH, '//*[@id="hardwarelease_vendorleadtime"]')),
    ("STATUS", (By.XPATH, '//*[@id="hardwarelease_status"]')),
    ("TOTAL_AMOUNT", (By.XPATH, '//*[@id="hardwarelease_dollaramount"]')),
    ("BUYER_NOTE", (By.XPATH, '//*[@id="hardwarelease_buyersnote"]')),
    ("NOTES", (By.XPATH, '//*[@id="hardwarelease_notes"]')),
    ("EXPORT_CSV", (By.XPATH, '//*[@id="hardwarelease_lineitems_form_submit"][2]')),
    ("EXPORT_EXCEL", (By.XPATH, '//*[@id="hardwarelease_lineitems_form_submit"][3]')),
    ("EXPORT_XML", (By.XPATH, '//*[@id="hardwarelease_lineitems_form_submit"][4]')),
    ("VENDOR_NAME", (By.XPATH, '//*[@id="hardwarelease_vendorname"]')),
    ("SHIP_TO_ADDR", (By.CSS_SELECTOR, '#multiple_address_options')),
    ("PO_VOID", (By.XPATH, '//*[@id="hardwarelease_voidedflag"]'))
    # ... any other locators related to the Hardware Lease  Page
]
