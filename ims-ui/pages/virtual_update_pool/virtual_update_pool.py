from pages.base_page import BasePage
from pages.virtual_update_pool.virtual_update_pool_locator import virtual_update_pool_page_locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class VirtualUpdatePoolPage(BasePage):
    locators_dict = {name: locator for name, locator in virtual_update_pool_page_locators}

    """constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_update_pool_page(self, url):
        self.driver.get(url)

    def navigate_to_back_to_pool_page(self):
        self.do_click(self.locators_dict["BACK_TO_POOL"])

    def capture_the_content_from_pool_list_table_header(self):
        self.is_visible(self.locators_dict["BACK_TO_POOL_TABLE_HEADER"])
        captured_pool_table_header = self.get_element_text(self.locators_dict["BACK_TO_POOL_TABLE_HEADER"])
        return captured_pool_table_header

    def check_if_name_field_is_enabled_and_editable(self):
        element_editabiliy = self.check_if_element_is_editable(self.locators_dict["NAME_FIELD"])
        return element_editabiliy

    def check_if_description_field_is_enabled_and_editable(self):
        element_editability = self.check_if_element_is_editable(self.locators_dict["DESCRIPTION_FIELD"])
        return element_editability

    def visibility_of_pool_master_table(self):
        table_visibility = self.is_visible(self.locators_dict["POOL_MASTER_TABLE"])
        return table_visibility

    def check_for_hardware_presence_in_pool_master_table(self, hardware):
        pool_table = self.driver.find_element(By.XPATH, self.locators_dict["POOL_MASTER_TABLE"][1])
        hardware_visibility = False
        rows = pool_table.find_elements(By.TAG_NAME, 'tr')
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, 'td')
            for cell in cells:
                if hardware in str(cell.text):
                    hardware_visibility = True
                    break
                else:
                    continue
        return hardware_visibility

    def update_button_display_and_clickability_check(self):
        is_clickable = self.check_if_element_is_clickable(self.locators_dict["UPDATE_POOL_BUTTON"])
        is_displayed = self.check_if_form_is_displayed(self.locators_dict["UPDATE_POOL_BUTTON"])
        if is_clickable and is_displayed:
            return True
        else:
            return False

    def check_host_reservation_edit_display(self):
        is_displayed = self.check_if_element_is_displayed(self.locators_dict["HOST_RESERVATION"])
        is_editable = self.check_if_element_is_editable(self.locators_dict["HOST_RESERVATION"])
        if is_displayed and is_editable:
            return True
        else:
            return False

    def pool_brand_dropdown_status(self):
        element = self.driver.find_element(By.XPATH, self.locators_dict["POOL_BRAND"][1])
        pool_brand = True if element.tag_name.lower() == "select" else False
        return pool_brand

    def pool_brand_options_check(self):
        dropdown = self.driver.find_element(By.XPATH, self.locators_dict["POOL_BRAND"][1])

        select = Select(dropdown)
        dropdown_len = len(select.options)
        return dropdown_len

    def preferred_os_dropdown_status(self):
        element = self.driver.find_element(By.XPATH, self.locators_dict["PREFERRED_OS"][1])
        preferred_os = True if element.tag_name.lower() == "select" else False
        return preferred_os

    def reload_os_dropdown_status(self):
        element = self.driver.find_element(By.XPATH, self.locators_dict["RELOAD_OS"][1])
        preferred_os = True if element.tag_name.lower() == "select" else False
        return preferred_os

    def preferred_os_options_check(self):
        dropdown = self.driver.find_element(By.XPATH, self.locators_dict["PREFERRED_OS"][1])
        select = Select(dropdown)
        dropdown_len = len(select.options)
        return dropdown_len

    def reload_os_options_check(self):
        dropdown = self.driver.find_element(By.XPATH, self.locators_dict["RELOAD_OS"][1])
        select = Select(dropdown)
        dropdown_len = len(select.options)
        return dropdown_len

    def pool_type_dropdown_status(self):
        element = self.driver.find_element(By.XPATH, self.locators_dict["POOL_TYPE"][1])
        pool_type = True if element.tag_name.lower() == "select" else False
        return pool_type

    def capture_pool_type_options(self):
        element = self.driver.find_element(By.XPATH, self.locators_dict["POOL_TYPE"][1])
        dropdown = Select(element)
        option = dropdown.options
        pool_type = []
        for value in option:
            pool_type.append(value.text)
        return pool_type

    def check_if_host_reservation_is_enabled_and_editable(self):
        element_editable_status = self.check_if_element_is_editable(self.locators_dict["HOST_RESERVATION"])
        return element_editable_status

    def check_if_transient_cpu_limit_is_enabled_and_editable(self):
        element_editable_status = self.check_if_element_is_editable(self.locators_dict["TRANSIENT_CPU_LIMIT"])
        return element_editable_status

    def check_if_auto_migrate_pool_limit_is_enabled_and_editable(self):
        element_editable_status = self.check_if_element_is_editable(self.locators_dict["AUTO_MIGRATE_POOL_LIMIT"])
        return element_editable_status

    def use_host_with_preferred_os_status(self):
        element = self.driver.find_element(By.XPATH, self.locators_dict["ONLY_USE_HOSTS_WITH_PREFERRED_OS"][1])
        status = True if element.get_attribute("type") == "checkbox" and element.is_enabled() else False
        return status

    def enable_hosts_after_reload_status(self):
        element = self.driver.find_element(By.XPATH, self.locators_dict["ENABLE_HOSTS_AFTER_RELOADS"][1])
        status = True if element.get_attribute("type") == "checkbox" and element.is_enabled() else False
        return status

    def vlan_provisions_allowed_status(self):
        element = self.driver.find_element(By.XPATH, self.locators_dict["VLAN_PROVISIONS_ALLOWED"][1])
        status = True if element.get_attribute("type") == "checkbox" and element.is_enabled() else False
        return status

    def disable_host_auto_migration_allowed_status(self):
        element = self.driver.find_element(By.XPATH, self.locators_dict["DISABLE_HOST_AUTO_MIGRATION"][1])
        status = True if element.get_attribute("type") == "checkbox" and element.is_enabled() else False
        return status

    def get_the_no_of_checkboxes_for_pool_roles(self):
        td_elements = self.driver.find_element(By.XPATH,self.locators_dict["POOL_ROLES"][1])
        labels = td_elements.find_elements(By.XPATH,".//label")
        checkboxes = [label.text.strip() for label in labels if label.find_element(By.XPATH, ".//input[@type='checkbox']")]
        return len(checkboxes)
