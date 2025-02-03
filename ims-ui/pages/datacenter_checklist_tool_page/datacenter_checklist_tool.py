from pages.base_page import BasePage
from pages.datacenter_checklist_tool_page.datacenter_checklist_tool_locator import \
    datacenter_checklist_tool_page_locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class DatacenterChecklistToolPage(BasePage):
    locators_dict = {name: locator for name, locator in datacenter_checklist_tool_page_locators}

    """constructor of the page class"""

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_datacenter_checklist_page(self, url):
        self.driver.get(url)

    def click_on_start_new_datacenter_verification_arrow(self):
        self.do_click(self.locators_dict["START_NEW_DATACENTER_VERIFICATION_ARROW"])

    def get_start_button_status(self):
        element = self.driver.find_element(By.XPATH, self.locators_dict["START_BTN"][1])
        is_clickable = self.is_clickable(element)
        return is_clickable

    def get_the_dropdown_status(self):
        element = self.driver.find_element(By.XPATH, self.locators_dict["SELECT_DATACENTER_DROPDOWN"][1])
        select = Select(element)
        options = select.options
        checkboxes = [option.text.strip() for option in options]
        return checkboxes

    def get_datacenter_checklist_headings(self):
        spans = self.driver.find_elements(By.CSS_SELECTOR, self.locators_dict["CHECKLIST_HEADING"][1])
        headings = [span.text for span in spans]
        return headings

    def get_datacenter_checklist_rows(self):
        location_element = self.driver.find_elements(By.TAG_NAME, 'em')
        datacenter = [location.text.strip() for location in location_element]
        return datacenter

    def get_the_legend_table_accessibility(self):
        rows = self.driver.find_elements(By.CSS_SELECTOR,self.locators_dict["LEGEND_TABLE"][1])
        cell_status = []
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, 'td')
            if len(cells) ==2 and all(cell.is_displayed() for cell in cells):
                cell_status.append(True)
            else:
                cell_status.append(False)
        return True if all(cell_status) else False
