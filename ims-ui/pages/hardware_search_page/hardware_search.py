import time

import requests
from selenium.webdriver.support.select import Select

from pages.base_page import BasePage
from pages.hardware_search_page.hardware_search_locators import hardware_search_page_locators
from selenium.webdriver.common.by import By


class HardwareSearchPage(BasePage):
    locators_dict = {name: locator for name, locator in hardware_search_page_locators}

    """constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_hardware_search_page(self, url):
        self.driver.get(url)

    def get_the_details_of_checkbox(self, by_locator):
        element = self.driver.find_element(By.XPATH, by_locator)
        checkbox_options = Select(element)
        all_options = checkbox_options.options
        all_options_list = []
        for option in all_options:
            all_options_list.append(option.text)
        return all_options_list

    def get_the_details_of_location_checkbox(self):
        location_items = self.get_the_details_of_checkbox(self.locators_dict["LOCATION"][1])
        return location_items

    def get_the_details_of_hardware_func_checkbox(self):
        hardware_func_items = self.get_the_details_of_checkbox(self.locators_dict["HARDWARE_FUNCTION"][1])
        return hardware_func_items

    def get_the_details_of_uim_managed_asset_checkbox(self):
        uim_managed_asset_items = self.get_the_details_of_checkbox(self.locators_dict["UIM_MANAGED_ASSET"][1])
        return uim_managed_asset_items

    def get_the_details_of_tag_checkbox(self):
        tag_items = self.get_the_details_of_checkbox(self.locators_dict["UIM_MANAGED_ASSET"][1])
        return tag_items

    def get_the_details_of_hardware_pool_checkbox(self):
        hardware_pool_items = self.get_the_details_of_checkbox(self.locators_dict["HARDWARE_POOL"][1])
        return hardware_pool_items

    def get_the_details_of_pooled_servers_checkbox(self):
        pooled_servers_items = self.get_the_details_of_checkbox(self.locators_dict["POOLED_SERVERS"][1])
        return pooled_servers_items

    def get_the_details_of_hardware_pool_status_checkbox(self):
        hardware_pool_status_items = self.get_the_details_of_checkbox(self.locators_dict["HARDWARE_POOL_STATUS"][1])
        return hardware_pool_status_items

    def get_the_details_of_generic_components_checkbox(self):
        generic_components_items = self.get_the_details_of_checkbox(self.locators_dict["GENERIC_COMPONENT"][1])
        return generic_components_items

    def get_the_details_of_specific_components_checkbox(self):
        specific_components_items = self.get_the_details_of_checkbox(self.locators_dict["SPECIFIC_COMPONENT"][1])
        return specific_components_items

    def get_the_details_of_chassis_checkbox(self):
        chassis_items = self.get_the_details_of_checkbox(self.locators_dict["CHASSIS"][1])
        return chassis_items

    def get_the_details_of_display_btn(self):
        display_btn_element = self.driver.find_element(By.XPATH, self.locators_dict["DISPLAY"][1])
        is_clickable = self.is_clickable(display_btn_element)
        return is_clickable

    def get_the_details_of_export_csv_btn(self):
        export_csv_btn_element = self.driver.find_element(By.XPATH, self.locators_dict["EXPORT_CSV"][1])
        is_clickable = self.is_clickable(export_csv_btn_element)
        return is_clickable

    def get_the_details_of_save_and_share_search_query_url_btn(self):
        save_and_share_search_query_url_btn_element = self.driver.find_element(By.XPATH, self.locators_dict[
            "SAVE_AND_SHARE_SEARCH_QUERY_URL"][1])
        is_clickable = self.is_clickable(save_and_share_search_query_url_btn_element)
        return is_clickable

    def get_the_details_of_export_excel_btn(self):
        export_excel_btn_element = self.driver.find_element(By.XPATH, self.locators_dict["EXPORT_EXCEL"][1])
        is_clickable = self.is_clickable(export_excel_btn_element)
        return is_clickable

    def get_the_details_of_export_origin_cert_btn(self):
        export_origin_cert_element = self.driver.find_element(By.XPATH,
                                                              self.locators_dict["EXPORT_ORIGIN_CERTIFICATES"][1])
        is_clickable = self.is_clickable(export_origin_cert_element)
        return is_clickable

    def get_the_details_of_hardware_id_txt_box(self):
        is_displayed = self.check_if_element_is_displayed(self.locators_dict["HARDWARE_ID"])
        is_editable = self.check_if_element_is_editable(self.locators_dict["HARDWARE_ID"])
        return True if (is_displayed and is_editable) else False

    def get_the_details_of_virtual_host_id_txt_box(self):
        is_displayed = self.check_if_element_is_displayed(self.locators_dict["VIRTUAL_HOST_ID"])
        is_editable = self.check_if_element_is_editable(self.locators_dict["VIRTUAL_HOST_ID"])
        return True if (is_displayed and is_editable) else False

    def get_the_details_of_manufacture_serial_number_txt_box(self):
        is_displayed = self.check_if_element_is_displayed(self.locators_dict["MANUFACTURER_SERIAL_NUMBER"])
        is_editable = self.check_if_element_is_editable(self.locators_dict["MANUFACTURER_SERIAL_NUMBER"])
        return True if (is_displayed and is_editable) else False

    def get_the_details_of_softlayer_serial_number_txt_box(self):
        is_displayed = self.check_if_element_is_displayed(self.locators_dict["SOFTLAYER_SERIAL_NUMBER"])
        is_editable = self.check_if_element_is_editable(self.locators_dict["SOFTLAYER_SERIAL_NUMBER"])
        return True if (is_displayed and is_editable) else False

    def get_the_details_of_account_id_txt_box(self):
        is_displayed = self.check_if_element_is_displayed(self.locators_dict["ACCOUNT_ID"])
        is_editable = self.check_if_element_is_editable(self.locators_dict["ACCOUNT_ID"])
        return True if (is_displayed and is_editable) else False

    def get_the_details_of_chassis_scip_id_txt_box(self):
        is_displayed = self.check_if_element_is_displayed(self.locators_dict["CHASSIS_SCIP_ID"])
        is_editable = self.check_if_element_is_editable(self.locators_dict["CHASSIS_SCIP_ID"])
        return True if (is_displayed and is_editable) else False

    def get_the_details_of_hardware_component_model_scip_id_txt_box(self):
        is_displayed = self.check_if_element_is_displayed(self.locators_dict["HARDWARE_COMPONENT_MODEL_SCIP_ID"])
        is_editable = self.check_if_element_is_editable(self.locators_dict["HARDWARE_COMPONENT_MODEL_SCIP_ID"])
        return True if (is_displayed and is_editable) else False

    def get_the_details_of_mac_ipv4_ipv6_txt_box(self):
        is_displayed = self.check_if_element_is_displayed(self.locators_dict["MAC/IPV4/IPV6_ADDRESS"])
        is_editable = self.check_if_element_is_editable(self.locators_dict["MAC/IPV4/IPV6_ADDRESS"])
        return True if (is_displayed and is_editable) else False

    def get_the_details_of_internal_notes_txt_box(self):
        is_displayed = self.check_if_element_is_displayed(self.locators_dict["INTERNAL_NOTES"])
        is_editable = self.check_if_element_is_editable(self.locators_dict["INTERNAL_NOTES"])
        return True if (is_displayed and is_editable) else False
