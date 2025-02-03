from pages.base_page import BasePage
from utilities.read_properties import ReadConfig
from pages.login_page.login_page_locators import login_page_locators
from pages.host_evacuation_type_page.host_evacuation import HostEvacuationPage
from pages.accounting_page.accounting import AccountingPage
from pages.virtual_update_pool.virtual_update_pool import VirtualUpdatePoolPage
from pages.cancel_virtual_process_instance.cancel_virtual_process_instance import CancelVirtualProcessInstancePage
from pages.data_verification_tool_page.data_verification_tool import DataVerificationToolPage
from pages.datacenter_checklist_tool_page.datacenter_checklist_tool import DatacenterChecklistToolPage
from pages.hardware_page.hardware import HardwarePage
from pages.hardware_transaction_page.hardware_transaction import HardwareTransactionPage
from pages.network_monitoring_page.network_monitoring import NetworkMonitoringPage
from pages.reports_page.reports import ReportsPage
from pages.network_firewall_page.network_firewall import NetworkFirewallPage
from pages.server_prebuild_page.server_prebuild import ServerPrebuildPage
from pages.service_inventory_report_page.service_inventory_report import ServiceInventoryReportPage
from pages.hardware_search_page.hardware_search import HardwareSearchPage
from pages.rma_ready_hardware_page.rma_ready_hardware import RMAReadyHardwarePage
from pages.hardware_component_search_page.hardware_component_search import HardwareComponentSearchPage
from pages.hardware_lease_page.hardware_lease import HardwareLeasePage
from pages.hardware_chaasis_list_page.hardware_chaasis_list import HardwareChaasisListPage
from pages.software_configuration_page.software_configuration import SoftwareConfigurationPage
from pages.hardware_update_page.hardware_update import HardwareUpdatePage
from pages.aggregate_group_page.aggregate_group import AggregateGroupPage
from pages.virtual_view_page.virtual_view_page import VirtualViewPage
from pages.hardware_view_edit_page.hardware_view_edit_page import HardwareViewEditPage


class LoginPage(BasePage):
    locators_dict = {name: locator for name, locator in login_page_locators}

    """constructor of the page class"""

    def __init__(self, driver, url):
        super().__init__(driver)
        self.driver.get(url)

    """Page Actions"""

    """"This is used to get page title"""

    def get_login_page_title(self, title):
        return self.get_title(title)

    """This is used to login to app"""

    def do_login(self, username, password, return_object):
        self.clear_element_text(self.locators_dict["USERNAME"])
        self.do_send_keys(self.locators_dict["USERNAME"], username)
        self.clear_element_text(self.locators_dict["PASSWORD"])
        self.do_send_keys(self.locators_dict["PASSWORD"], password)
        self.do_click(self.locators_dict["LOGIN_BUTTON"])
        if return_object == "Evacuation Type":
            return HostEvacuationPage(self.driver)
        if return_object == "Accounting Type":
            return AccountingPage(self.driver)
        if return_object == "Virtual Update Pool":
            return VirtualUpdatePoolPage(self.driver)
        if return_object == "Cancel Virtual Process Instance":
            return CancelVirtualProcessInstancePage(self.driver)
        if return_object == "Data Verification Tool":
            return DataVerificationToolPage(self.driver)
        if return_object == "Datacenter Checklist Tool":
            return DatacenterChecklistToolPage(self.driver)
        if return_object == "Hardware":
            return HardwarePage(self.driver)
        if return_object == "Hardware Transaction":
            return HardwareTransactionPage(self.driver)
        if return_object == "Network Monitoring":
            return NetworkMonitoringPage(self.driver)
        if return_object == "Reports":
            return ReportsPage(self.driver)
        if return_object == "Network Firewall":
            return NetworkFirewallPage(self.driver)
        if return_object == "Server Prebuild":
            return ServerPrebuildPage(self.driver)
        if return_object == "Service Inventory Report":
            return ServiceInventoryReportPage(self.driver)
        if return_object == "Hardware Search":
            return HardwareSearchPage(self.driver)
        if return_object == "RMA Ready Hardware":
            return RMAReadyHardwarePage(self.driver)
        if return_object == "Hardware Component Search":
            return HardwareComponentSearchPage(self.driver)
        if return_object == "Hardware Lease":
            return HardwareLeasePage(self.driver)
        if return_object == "Hardware Chaasis List":
            return HardwareChaasisListPage(self.driver)
        if return_object == "Software Configuration":
            return SoftwareConfigurationPage(self.driver)
        if return_object == "Hardware Update":
            return HardwareUpdatePage(self.driver)
        if return_object == "Aggregate Group":
            return AggregateGroupPage(self.driver)
        if return_object == "Virtual View Page":
            return VirtualViewPage(self.driver)
        if return_object == "Hardware View Edit Page":
            return HardwareViewEditPage(self.driver)

    def set_username(self, username):
        self.clear_element_text(self.locators_dict["USERNAME"])
        self.do_send_keys(self.locators_dict["USERNAME"], username)

    def set_password(self, password):
        self.clear_element_text(self.locators_dict["PASSWORD"])
        self.do_send_keys(self.locators_dict["PASSWORD"], password)

    def get_page_title(self):
        return self.driver.title

    def logout_user(self):
        self.do_click(self.locators_dict["LOGOUT_BUTTON"])

    def capture_logout_message(self):
        return self.get_element_text(self.locators_dict["LOGOUT_TEXT"])
