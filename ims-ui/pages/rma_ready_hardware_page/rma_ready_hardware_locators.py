from selenium.webdriver.common.by import By

rma_ready_hardware_page_locators = [

    ("SERIAL_NUMBER", (By.XPATH, '//*[@id="rma_serialnumbers"]')),
    ("LOCATION", (By.XPATH, '//*[@name="data[Rma][locationId_chooser]"]')),
    ("HARDWARE_FUNCTION", (By.XPATH, '//*[@name="data[Rma][hardwareFunctionId]"]')),
    ("RMA_NUMBER", (By.XPATH, '//*[@id="rma_id"]')),
    ("SEARCH_BTN", (By.XPATH, '//*[@id="rma_rmareadyhardware_form_submit"]')),
    ("ASSIGN_BTN", (By.XPATH, '//*[@id="rma_attachitems_hardware_form_submit"]')),
    ("RMA_READY_HARDWARE_TABLE", (By.XPATH, '//*[@id="rma_rmareadyhardwarelist_0"]')),
    ("DISPLAYING_CHECKBOX",
     (By.XPATH, '//*[@id="rma_rma_ready_hardware_rma_rma_ready_hardware_list_pagination_limit_select"]')),
    # ... any other locators related to the RMA Ready Hardware Page

]
