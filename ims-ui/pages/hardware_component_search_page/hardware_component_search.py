import time
from pages.base_page import BasePage
from pages.hardware_component_search_page.hardware_component_search_locator import \
    hardware_component_search_page_locators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class HardwareComponentSearchPage(BasePage):
    locators_dict = {name: locator for name, locator in hardware_component_search_page_locators}

    """constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_hardware_component_search_page(self, url):
        self.driver.get(url)

    def input_serial_number(self, serial_number):
        self.do_click(self.locators_dict["SERIAL_NUMBER_ARROW"])
        self.do_send_keys(self.locators_dict["SERIAL_NUMBER"], serial_number)
        self.do_click(self.locators_dict["DISPLAY"])
        result = self.check_if_element_is_displayed(self.locators_dict["RESULT"])
        return result

    def input_component_id(self, component_id):
        self.do_click(self.locators_dict["SERIAL_NUMBER_ARROW"])
        self.do_send_keys(self.locators_dict["COMPONENT_ID"], component_id)
        self.do_click(self.locators_dict["DISPLAY"])
        result = self.check_if_element_is_displayed(self.locators_dict["RESULT"])
        return result

    def input_component_ids_newline(self, component_id1, component_id2):
        self.do_click(self.locators_dict["SERIAL_NUMBER_ARROW"])
        self.do_send_keys(self.locators_dict["COMPONENT_ID"], component_id1)
        self.press_enter(self.locators_dict["COMPONENT_ID"])
        self.do_send_keys(self.locators_dict["COMPONENT_ID"], component_id2)
        self.do_click(self.locators_dict["DISPLAY"])
        result = self.check_if_element_is_displayed(self.locators_dict["RESULT"])
        return result

    def input_serial_number_newline(self, serial_number1, serial_number2):
        self.do_click(self.locators_dict["SERIAL_NUMBER_ARROW"])
        self.do_send_keys(self.locators_dict["SERIAL_NUMBER"], serial_number1)
        self.press_enter(self.locators_dict["SERIAL_NUMBER"])
        self.do_send_keys(self.locators_dict["SERIAL_NUMBER"], serial_number2)
        self.do_click(self.locators_dict["DISPLAY"])
        result = self.check_if_element_is_displayed(self.locators_dict["RESULT"])
        return result

    def input_sl_serial_number(self, sl_serial_no):
        self.do_click(self.locators_dict["COMPONENTS_ATTACHED_TO_HARDWARE"])
        self.do_send_keys(self.locators_dict["SOFTLAYER_SERIAL_NUMBER"], sl_serial_no)
        self.do_click(self.locators_dict["DISPLAY"])
        result = self.check_if_element_is_displayed(self.locators_dict["RESULT"])
        return result

    def input_sl_serial_numbers_with_newline(self, sl_serial_1, sl_serial_2):
        self.do_click(self.locators_dict["COMPONENTS_ATTACHED_TO_HARDWARE"])
        self.do_send_keys(self.locators_dict["SOFTLAYER_SERIAL_NUMBER"], sl_serial_1)
        self.press_enter(self.locators_dict["SOFTLAYER_SERIAL_NUMBER"])
        self.do_send_keys(self.locators_dict["SOFTLAYER_SERIAL_NUMBER"], sl_serial_2)
        self.do_click(self.locators_dict["DISPLAY"])
        result = self.check_if_element_is_displayed(self.locators_dict["RESULT"])
        return result

    def input_manufacturer_sl_number(self, mf_serial_no):
        self.do_click(self.locators_dict["COMPONENTS_ATTACHED_TO_HARDWARE"])
        self.do_send_keys(self.locators_dict["MANUFACTURER_SERIAL_NUMBER"], mf_serial_no)
        self.do_click(self.locators_dict["DISPLAY"])
        result = self.check_if_element_is_displayed(self.locators_dict["RESULT"])
        return result

    def input_manufacturer_sl_number_with_newline(self, mf_sl_1, mf_sl_2):
        self.do_click(self.locators_dict["COMPONENTS_ATTACHED_TO_HARDWARE"])
        self.do_send_keys(self.locators_dict["MANUFACTURER_SERIAL_NUMBER"], mf_sl_1)
        self.press_enter(self.locators_dict["MANUFACTURER_SERIAL_NUMBER"])
        self.do_send_keys(self.locators_dict["MANUFACTURER_SERIAL_NUMBER"], mf_sl_2)
        self.do_click(self.locators_dict["DISPLAY"])
        result = self.check_if_element_is_displayed(self.locators_dict["RESULT"])
        return result

    def input_hardware_id(self, hw_id):
        self.do_click(self.locators_dict["COMPONENTS_ATTACHED_TO_HARDWARE"])
        self.do_send_keys(self.locators_dict["HARDWARE_ID"], hw_id)
        self.do_click(self.locators_dict["DISPLAY"])
        result = self.check_if_element_is_displayed(self.locators_dict["RESULT"])
        return result

    def input_hardware_id_with_newline(self, hw_id1, hw_id2):
        self.do_click(self.locators_dict["COMPONENTS_ATTACHED_TO_HARDWARE"])
        self.do_send_keys(self.locators_dict["HARDWARE_ID"], hw_id1)
        self.press_enter(self.locators_dict["HARDWARE_ID"])
        self.do_send_keys(self.locators_dict["HARDWARE_ID"], hw_id2)
        self.do_click(self.locators_dict["DISPLAY"])
        result = self.check_if_element_is_displayed(self.locators_dict["RESULT"])
        return result

    def choose_multiple_component_states(self):
        time.sleep(5)
        action = ActionChains(self.driver)
        self.do_click(self.locators_dict["COMPONENT_DETAIL"])
        time.sleep(5)
        element = self.driver.find_element(By.XPATH, self.locators_dict["COMPONENT_STATUS"][1])
        select = Select(element)
        option1 = select.select_by_visible_text("ADMIN_HOLD")
        option2 = select.select_by_visible_text("AUDIT")
        option3 = select.select_by_visible_text("CHECK_OUT")
        action.key_down(Keys.CONTROL).click(option1).click(option2).click(option3).key_up(Keys.CONTROL).perform()
        self.do_click(self.locators_dict["DISPLAY"])
        time.sleep(10)
        result = self.check_if_element_is_displayed(self.locators_dict["RESULT"])
        return result

    def input_lot_number(self, lot_number):
        time.sleep(5)
        action = ActionChains(self.driver)
        self.do_click(self.locators_dict["COMPONENT_DETAIL"])
        time.sleep(5)
        element = self.driver.find_element(By.XPATH, self.locators_dict["COMPONENT_STATUS"][1])
        select = Select(element)
        option1 = select.select_by_visible_text("ADMIN_HOLD")
        option2 = select.select_by_visible_text("AUDIT")
        option3 = select.select_by_visible_text("CHECK_OUT")
        action.key_down(Keys.CONTROL).click(option1).click(option2).click(option3).key_up(Keys.CONTROL).perform()
        self.do_send_keys(self.locators_dict["LOT_NUMBER"], lot_number)
        self.do_click(self.locators_dict["DISPLAY"])
        time.sleep(10)
        result = self.check_if_element_is_displayed(self.locators_dict["RESULT"])
        return result


    def choose_multiple_hardware_states(self):
        time.sleep(5)
        action = ActionChains(self.driver)
        self.do_click(self.locators_dict["COMPONENTS_ATTACHED_TO_HARDWARE"])
        time.sleep(10)
        element = self.driver.find_element(By.XPATH, self.locators_dict["HARDWARE_STATUS"][1])
        select = Select(element)
        option1 = select.select_by_visible_text("DISCONNECT")
        option2 = select.select_by_visible_text("FIRMWARE_WAIT")
        action.key_down(Keys.CONTROL).click(option1).click(option2).key_up(Keys.CONTROL).perform()
        self.do_click(self.locators_dict["DISPLAY"])
        time.sleep(10)
        result = self.check_if_element_is_displayed(self.locators_dict["RESULT"])
        return result

    def input_account_id(self, account_id):
        self.do_click(self.locators_dict["COMPONENTS_ATTACHED_TO_HARDWARE"])
        time.sleep(10)
        self.do_send_keys(self.locators_dict["ACCOUNT_ID"], account_id)
        self.do_click(self.locators_dict["DISPLAY"])
        time.sleep(10)
        result = self.check_if_element_is_displayed(self.locators_dict["RESULT"])
        return result

    def input_hostname(self, host, account_id):
        self.do_click(self.locators_dict["COMPONENTS_ATTACHED_TO_HARDWARE"])
        time.sleep(10)
        self.do_send_keys(self.locators_dict["ACCOUNT_ID"], account_id)
        self.do_send_keys(self.locators_dict["HOSTNAME"], host)
        self.do_click(self.locators_dict["DISPLAY"])
        time.sleep(10)
        result = self.check_if_element_is_displayed(self.locators_dict["RESULT"])
        return result

    def input_domain(self, domain, host, account_id):
        self.do_click(self.locators_dict["COMPONENTS_ATTACHED_TO_HARDWARE"])
        time.sleep(10)
        self.do_send_keys(self.locators_dict["ACCOUNT_ID"], account_id)
        self.do_send_keys(self.locators_dict["HOSTNAME"], host)
        self.do_send_keys(self.locators_dict["DOMAIN"], domain)
        self.do_click(self.locators_dict["DISPLAY"])
        time.sleep(10)
        result = self.check_if_element_is_displayed(self.locators_dict["RESULT"])
        return result

    def choose_from_function_dropdown(self, function_dropdown, domain, host, account_id):
        self.do_click(self.locators_dict["COMPONENTS_ATTACHED_TO_HARDWARE"])
        time.sleep(10)
        self.do_send_keys(self.locators_dict["ACCOUNT_ID"], account_id)
        self.do_send_keys(self.locators_dict["HOSTNAME"], host)
        self.do_send_keys(self.locators_dict["DOMAIN"], domain)
        element = self.driver.find_element(By.XPATH, self.locators_dict["FUNCTION_DROPDOWN"][1])
        select = Select(element)
        select.select_by_visible_text(function_dropdown)
        self.do_click(self.locators_dict["DISPLAY"])
        time.sleep(10)
        result = self.check_if_element_is_displayed(self.locators_dict["RESULT"])
        return result

    def choose_from_chassis(self, chassis, function_dropdown, domain, host, account_id):
        self.do_click(self.locators_dict["COMPONENTS_ATTACHED_TO_HARDWARE"])
        time.sleep(10)
        self.do_send_keys(self.locators_dict["ACCOUNT_ID"], account_id)
        self.do_send_keys(self.locators_dict["HOSTNAME"], host)
        self.do_send_keys(self.locators_dict["DOMAIN"], domain)
        function_element = self.driver.find_element(By.XPATH, self.locators_dict["FUNCTION_DROPDOWN"][1])
        function_select = Select(function_element)
        function_select.select_by_visible_text(function_dropdown)
        time.sleep(10)
        chassis_element = self.driver.find_element(By.XPATH, self.locators_dict["CHASSIS"][1])
        chassis_select = Select(chassis_element)
        chassis_select.select_by_visible_text(chassis)
        self.do_click(self.locators_dict["DISPLAY"])
        time.sleep(10)
        result = self.check_if_element_is_displayed(self.locators_dict["RESULT"])
        return result

    def input_mac_ipv4_ipv6(self, mac_ipv4_ipv6, chassis, function_dropdown, domain, host, account_id):
        self.do_click(self.locators_dict["COMPONENTS_ATTACHED_TO_HARDWARE"])
        time.sleep(10)
        self.do_send_keys(self.locators_dict["ACCOUNT_ID"], account_id)
        self.do_send_keys(self.locators_dict["HOSTNAME"], host)
        self.do_send_keys(self.locators_dict["DOMAIN"], domain)
        function_element = self.driver.find_element(By.XPATH, self.locators_dict["FUNCTION_DROPDOWN"][1])
        function_select = Select(function_element)
        function_select.select_by_visible_text(function_dropdown)
        time.sleep(10)
        chassis_element = self.driver.find_element(By.XPATH, self.locators_dict["CHASSIS"][1])
        chassis_select = Select(chassis_element)
        chassis_select.select_by_visible_text(chassis)
        self.do_send_keys(self.locators_dict["MAC_IPV4_IPV6"], mac_ipv4_ipv6)
        self.do_click(self.locators_dict["DISPLAY"])
        time.sleep(10)
        result = self.check_if_element_is_displayed(self.locators_dict["RESULT"])
        return result

    def click_on_export_csv_button(self):
        self.do_click(self.locators_dict["EXPORT_CSV"])
        time.sleep(10)

    def click_on_export_excel_button(self):
        self.do_click(self.locators_dict["EXPORT_EXCEL"])
        time.sleep(10)

    def click_query_button(self):
        self.do_click(self.locators_dict["SEND_AND_SHARE"])
        result = self.check_if_element_is_displayed(self.locators_dict["QUERY_URL"])
        return result

    def input_account_id_details(self, account_id):
        self.do_click(self.locators_dict["COMPONENT_EVENT"])
        self.do_send_keys(self.locators_dict["ACCOUNT_ID_DETAILS"], account_id)
        self.do_click(self.locators_dict["DISPLAY"])
        time.sleep(10)
        result = self.check_if_element_is_displayed(self.locators_dict["RESULT"])
        return result

    def input_hw_id_details(self, hw_id):
        self.do_click(self.locators_dict["COMPONENT_EVENT"])
        self.do_send_keys(self.locators_dict["HW_ID"], hw_id)
        self.do_click(self.locators_dict["DISPLAY"])
        time.sleep(10)
        result = self.check_if_element_is_displayed(self.locators_dict["RESULT"])
        return result

    def input_location_details(self, location, hw_id):
        self.do_click(self.locators_dict["COMPONENT_EVENT"])
        self.do_send_keys(self.locators_dict["HW_ID"], hw_id)
        location_element = self.driver.find_element(By.XPATH, self.locators_dict["LOCATION_ELEMENT"][1])
        location_select = Select(location_element)
        location_select.select_by_visible_text(location)
        self.do_click(self.locators_dict["DISPLAY"])
        time.sleep(10)
        result = self.check_if_element_is_displayed(self.locators_dict["RESULT"])
        return result

    def id_link_status_check(self):
        self.do_click(self.locators_dict["ID_LINK"])
        time.sleep(10)
        return self.driver.title

