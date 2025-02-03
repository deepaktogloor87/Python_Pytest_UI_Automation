import time

import requests
from selenium.webdriver.support.select import Select
from utilities.logger import setup_logger
from pages.base_page import BasePage
from pages.hardware_update_page.hardware_update_locators import hardware_update_page_locators
from selenium.webdriver.common.by import By


class HardwareUpdatePage(BasePage):
    locators_dict = {name: locator for name, locator in hardware_update_page_locators}

    """constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)
        self.log = setup_logger('apollo')

    def navigate_to_hardware_update_page(self, url):
        self.driver.get(url)

    def choose_properties_from_checkbox(self):
        self.do_click(self.locators_dict["STORAGE_GROUP"])
        time.sleep(10)
        jbod_c_select = Select(self.driver.find_element(By.XPATH, self.locators_dict["JBOD_C"][1]))
        jbod_c_select.select_by_value("properties")
        time.sleep(10)

    def ssn_display_status(self):
        display_status = self.check_if_element_is_displayed(self.locators_dict["JBOD_SSN"])
        return display_status

    def ssn_editable_status(self):
        editable_status = self.check_if_element_is_editable(self.locators_dict["JBOD_SSN"])
        return editable_status

    def wwn_display_status(self):
        display_status = self.check_if_element_is_displayed(self.locators_dict["JBOD_WWN"])
        return display_status

    def wwn_editable_status(self):
        editable_status = self.check_if_element_is_editable(self.locators_dict["JBOD_WWN"])
        return editable_status

    def click_maintenance_link(self):
        time.sleep(25)
        self.do_click(self.locators_dict["CLICK_MAINTENANCE"])
        self.log.info("maintenance link clicked")
        # time.sleep(20)

    def click_on_others_checkbox(self):
        self.do_click(self.locators_dict["OTHER_CHECKBOX"])
        self.log.info("other checkbox clicked")

    def post_maintenance_notes(self, maintenance_notes):
        self.do_send_keys(self.locators_dict["OTHER_TEXTBOX"], maintenance_notes)
        self.log.info(f"{maintenance_notes} has been written to maintenance notes")

    def click_on_continue_btn(self):
        time.sleep(10)
        self.do_click(self.locators_dict["CONTINUE_BTN"])
        self.log.info("Continue button clicked")
        time.sleep(20)

    def maintenance_notes_visibility(self):
        visibility = self.check_element_presence(self.locators_dict["OTHER_MAINTENANCE_NOTES"][1])
        return visibility.text

    def get_remote_management_control_link_presence(self):
        presence = self.check_element_presence(self.locators_dict["REMOTE_MGMT_CTRL"][1])
        if presence:
            self.log.info("remote management control link is present on the page")
            self.log.info("checking if it is the link")
            element = self.driver.find_element(By.XPATH, self.locators_dict["REMOTE_MGMT_CTRL"][1])
            if element.tag_name == "a":
                return True
        return False

    def open_remote_management_control_link(self):
        self.do_click(self.locators_dict["REMOTE_MGMT_CTRL"])
        self.log.info("opening remote management control......")
        time.sleep(15)

    def get_ipmi_remote_management_summary_presence(self):
        self.log.info("checking the presence of ipmi remote management summary")
        presence = self.check_element_presence(self.locators_dict["IPMI_REMOTE_MANAGEMENT_SUMMARY"][1])
        return presence

    def get_redfish_remote_management_summary_presence(self):
        self.log.info("checking the presence of redfish remote management summary")
        presence = self.check_element_presence(self.locators_dict["IPMI_REMOTE_MANAGEMENT_SUMMARY"][1])
        return presence

    def remote_mgmt_summary_click(self):
        self.do_click(self.locators_dict["REDFISH_REMOTE_MANAGEMENT_SUMMARY"])
        self.log.info("clicked")

    def power_down_redfish(self):
        time.sleep(20)
        dropdown = Select(self.driver.find_element(By.XPATH, self.locators_dict["REMOTE_MGMT_DROPDOWN"][1]))
        dropdown.select_by_value("powerOff")
        self.log.info("power off option is selected")
        self.log.info("Initiating power off")
        self.do_click(self.locators_dict["INITIATE_COMMAND"])
        time.sleep(20)
        self.log.info("Refreshing the page")
        self.driver.refresh()
        time.sleep(20)
        self.remote_mgmt_summary_click()
        time.sleep(20)
        self.log.info("Getting the text")
        power_status = self.driver.find_element(By.XPATH, self.locators_dict["POWER_STATUS"][1])
        self.log.info(f"power status  of the redfish server is {power_status}")
        return power_status.text

    def power_on_redfish(self):
        time.sleep(20)
        dropdown = Select(self.driver.find_element(By.XPATH, self.locators_dict["REMOTE_MGMT_DROPDOWN"][1]))
        dropdown.select_by_value("powerOn")
        self.log.info("power on option is selected")
        self.log.info("Initiating power off")
        self.do_click(self.locators_dict["INITIATE_COMMAND"])
        time.sleep(20)
        self.log.info("Refreshing the page")
        self.driver.refresh()
        time.sleep(20)
        self.remote_mgmt_summary_click()
        time.sleep(20)
        self.log.info("Getting the text")
        power_status = self.driver.find_element(By.XPATH, self.locators_dict["POWER_STATUS"][1])
        self.log.info(f"power status  of the redfish server is {power_status}")
        return power_status.text

    def choose_yes_vpcng_from_dropdown(self):
        time.sleep(20)
        uim_managed_asset = self.driver.find_element(By.XPATH, self.locators_dict["UIM_MANAGED_ASSET"][1])
        uim_managed_asset_options = Select(uim_managed_asset)
        uim_managed_asset_options.select_by_value("vpcng")

    def get_the_uim_managed_asset_dropdown_value(self):
        uim_managed_asset = self.driver.find_element(By.XPATH, self.locators_dict["UIM_MANAGED_ASSET"][1])
        uim_managed_asset_options = Select(uim_managed_asset)
        selected_option = uim_managed_asset_options.first_selected_option
        select_option = selected_option.get_attribute("value")
        return select_option

    def click_on_general_tab_continue_btn(self):
        time.sleep(20)
        self.do_click(self.locators_dict["GENERAL_TAB_CONTINUE_BTN"])
        time.sleep(15)

    def choose_undercloud_from_dropdown(self):
        time.sleep(20)
        uim_managed_asset = self.driver.find_element(By.XPATH, self.locators_dict["UIM_MANAGED_ASSET"][1])
        uim_managed_asset_options = Select(uim_managed_asset)
        uim_managed_asset_options.select_by_value("undercloud")

    def choose_fedramp_from_dropdown(self):
        time.sleep(20)
        uim_managed_asset = self.driver.find_element(By.XPATH, self.locators_dict["UIM_MANAGED_ASSET"][1])
        uim_managed_asset_options = Select(uim_managed_asset)
        uim_managed_asset_options.select_by_value("fedramp")

    def choose_no_from_dropdown(self):
        time.sleep(20)
        uim_managed_asset = self.driver.find_element(By.XPATH, self.locators_dict["UIM_MANAGED_ASSET"][1])
        uim_managed_asset_options = Select(uim_managed_asset)
        uim_managed_asset_options.select_by_value("classic")
 