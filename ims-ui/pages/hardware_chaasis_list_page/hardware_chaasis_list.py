import time
from pages.base_page import BasePage
from pages.hardware_chaasis_list_page.hardware_chaasis_list_locators import hardware_chaasis_list_locators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class HardwareChaasisListPage(BasePage):
    locators_dict = {name: locator for name, locator in hardware_chaasis_list_locators}

    """constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_hardware_chaasis_list_page(self, url):
        self.driver.get(url)

    def go_into_the_edit_link(self):
        self.do_click(self.locators_dict["EDIT"])
        time.sleep(5)

    def select_add_an_attribute(self):
        self.do_click(self.locators_dict["ADD_AN_ATTRIBUTE"])
        time.sleep(5)

    def set_raid_card_capacity_to_2(self):
        attribute = self.driver.find_element(By.XPATH, self.locators_dict["ATTRIBUTE"][1])
        select_attribute = Select(attribute)
        select_attribute.select_by_visible_text("Riser Card Capacity")
        self.do_send_keys(self.locators_dict["ATTRIBUTE_VALUE"], 2)
        self.driver.find_element(By.XPATH, self.locators_dict["CONTINUE_BTN"][1]).click()
        time.sleep(5)
        status = self.get_element_text(self.locators_dict["STATUS_MSG"])
        return status

    def choose_chaasis(self, chassis):
        chassis_dropdown = self.driver.find_element(By.XPATH, self.locators_dict["CHASSIS"][1])
        select_chassis = Select(chassis_dropdown)
        select_chassis.select_by_visible_text(chassis)

    def get_the_riser_card_rows(self):
        time.sleep(25)
        riser_card_rows = self.driver.find_elements(By.XPATH, self.locators_dict["RISER_CARD_ROWS"][1])
        riser_card_rows_count = len(riser_card_rows)
        return riser_card_rows_count

    def send_description(self, template_description):
        self.do_send_keys(self.locators_dict["DESCRIPTION"], template_description)

    def select_dropdowns_and_save_the_page(self, PO):
        """
            Please do not change the configuration as this will fail the testcase
        """
        time.sleep(25)
        # select usb device 1
        usb_dropdown = self.driver.find_element(By.XPATH, self.locators_dict["USB_DEVICE"][1])
        select_usb_device = Select(usb_dropdown)
        select_usb_device.select_by_index(1)


        #select riser card 1
        riser_card_1_dropdown = self.driver.find_element(By.XPATH, self.locators_dict["RISER_CARD_1"][1])
        riser_card_1_select = Select(riser_card_1_dropdown)
        riser_card_1_select.select_by_index(1)


        # select riser card 2
        riser_card_2_dropdown = self.driver.find_element(By.XPATH, self.locators_dict["RISER_CARD_2"][1])
        riser_card_2_select = Select(riser_card_2_dropdown)
        riser_card_2_select.select_by_index(1)


        # select motherboard
        motherboard_dropdown = self.driver.find_element(By.XPATH, self.locators_dict["MOTHERBOARD"][1])
        motherboard_select = Select(motherboard_dropdown)
        motherboard_select.select_by_index(2)
        time.sleep(25)


        # select Processor 1
        processor1_dropdown = self.driver.find_element(By.XPATH, self.locators_dict["PROCESSOR1"][1])
        processor1_select = Select(processor1_dropdown)
        processor1_select.select_by_index(1)

        # select Processor 1
        processor2_dropdown = self.driver.find_element(By.XPATH, self.locators_dict["PROCESSOR2"][1])
        processor2_select = Select(processor2_dropdown)
        processor2_select.select_by_index(1)

        # select Expansion Card 1
        expansion_card_dropdown = self.driver.find_element(By.XPATH, self.locators_dict["EXPANSION_CARD"][1])
        expansion_card_select = Select(expansion_card_dropdown)
        expansion_card_select.select_by_index(2)

        # select RAM
        # ram_dropdown = self.driver.find_element(By.XPATH, self.locators_dict["RAM"][1])
        # ram_select = Select(ram_dropdown)
        # ram_select.select_by_index(5)

        # select Drive Controller
        drive_controller_dropdown = self.driver.find_element(By.XPATH, self.locators_dict["DRIVE_CONTROLLER"][1])
        drive_controller_select = Select(drive_controller_dropdown)
        drive_controller_select.select_by_index(1)

        # select Battery
        battery_dropdown = self.driver.find_element(By.XPATH, self.locators_dict["BATTERY"][1])
        battery_select = Select(battery_dropdown)
        battery_select.select_by_index(1)

        # select Hard drive
        hd_dropdown = self.driver.find_element(By.XPATH, self.locators_dict["HARD_DRIVE"][1])
        hd_select = Select(hd_dropdown)
        hd_select.select_by_index(1)

        # select remote management card
        remote_mgmt_card_dropdown = self.driver.find_element(By.XPATH, self.locators_dict["REMOTE_MGMT_CARD"][1])
        remote_mgmt_card_select= Select(remote_mgmt_card_dropdown)
        remote_mgmt_card_select.select_by_index(1)

        # select network card
        network_card_dropdown = self.driver.find_element(By.XPATH, self.locators_dict["NETWORK_CARD"][1])
        network_card_select = Select(network_card_dropdown)
        network_card_select.select_by_index(1)

        # select network optic
        network_optic_dropdown = self.driver.find_element(By.XPATH, self.locators_dict["NETWORK_OPTIC"][1])
        network_optic_select = Select(network_optic_dropdown)
        network_optic_select.select_by_index(1)

        # select power supply
        power_supply_dropdown = self.driver.find_element(By.XPATH, self.locators_dict["POWER_SUPPLY"][1])
        power_supply_select = Select(power_supply_dropdown)
        power_supply_select.select_by_index(1)

        # select backplane
        backplane_dropdown = self.driver.find_element(By.XPATH, self.locators_dict["BACKPLANE"][1])
        backplane_select = Select(backplane_dropdown)
        backplane_select.select_by_index(1)

        # select fan
        fan_dropdown = self.driver.find_element(By.XPATH, self.locators_dict["FAN"][1])
        fan_select = Select(fan_dropdown)
        fan_select.select_by_index(1)

        # select video card
        video_card_dropdown = self.driver.find_element(By.XPATH, self.locators_dict["VIDEO_CARD"][1])
        video_card_select = Select(video_card_dropdown)
        video_card_select.select_by_index(1)

        # select gpu
        gpu_dropdown = self.driver.find_element(By.XPATH, self.locators_dict["GPU"][1])
        gpu_select = Select(gpu_dropdown)
        gpu_select.select_by_index(1)

        # select line card
        line_card_dropdown = self.driver.find_element(By.XPATH, self.locators_dict["LINE_CARD"][1])
        line_card_select = Select(line_card_dropdown)
        line_card_select.select_by_index(1)

        # select gpu
        security_device_dropdown = self.driver.find_element(By.XPATH, self.locators_dict["SECURITY_DEVICE"][1])
        security_device_select = Select(security_device_dropdown)
        security_device_select.select_by_index(1)

        # select checkbox
        self.do_click(self.locators_dict["INDEP_MGMT_PORT_CHECKBOX"])

        # enter PO number
        po_textbox = self.driver.find_element(By.XPATH, self.locators_dict["PO"][1])
        self.do_send_keys(self.locators_dict["PO"], PO)
        time.sleep(10)
        po_textbox.send_keys(Keys.DOWN)
        po_textbox.send_keys(Keys.ENTER)
        time.sleep(10)

        #save the template
        self.do_click(self.locators_dict["SAVE_TEMPLATE"])
        time.sleep(20)



