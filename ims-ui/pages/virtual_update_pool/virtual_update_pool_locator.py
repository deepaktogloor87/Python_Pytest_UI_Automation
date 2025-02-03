from selenium.webdriver.common.by import By

virtual_update_pool_page_locators = [

    ("ALL_ACCOUNTING_LINKS", (By.XPATH, '//*[@id="accounting_tab"]/ul/li[{i}]/a')),
    ("TOTAL_LINKS", (By.XPATH, "//*[@id='accounting_tab']//a")),
    ("BACK_TO_POOL", (By.XPATH, '//*[@title="Back to pool list"]')),
    ("BACK_TO_POOL_TABLE_HEADER",
     (By.XPATH, '//*[@id="virtual_host_pools_3_virtual_host_pool_list_3_pagination_table_caption"]/b')),
    ("NAME_FIELD", (By.XPATH, '//*[@id="pool_name"]')),
    ("POOL_MASTER_TABLE", (By.XPATH, '//table[contains(@id, "virtual_updatepool_")]')),
    ("DESCRIPTION_FIELD", (By.XPATH, '//*[@id="pool_description"]')),
    ("UPDATE_POOL_BUTTON", (By.XPATH, '//*[contains(@id,"_form_submit") and @value="Update pool"]')),
    ("HOST_RESERVATION", (By.XPATH, '//*[@id="pool_hostreservationpercent"]')),
    ("POOL_BRAND", (By.XPATH, '//*[@id="pool_brandid"]')),
    ("PREFERRED_OS", (By.XPATH, '//*[@id="pool_preferredhostoperatingsystemid"]')),
    ("RELOAD_OS", (By.XPATH, '//*[@id="pool_hostreloadsoperatingsystemid"]')),
    ("POOL_TYPE", (By.XPATH, '//*[@id="pool_typeid"]')),
    ("HOST_RESERVATION", (By.XPATH, '//*[@id="pool_hostreservationpercent"]')),
    ("TRANSIENT_CPU_LIMIT", (By.XPATH, '//*[@id="pool_transientcpulimitpercent"]')),
    ("AUTO_MIGRATE_POOL_LIMIT", (By.XPATH, '//*[@id="pool_maxautomigratelimit"]')),
    ("ONLY_USE_HOSTS_WITH_PREFERRED_OS", (By.XPATH, '//*[@id="pool_preferredhostoperatingsystemonly"]')),
    ("ENABLE_HOSTS_AFTER_RELOADS", (By.XPATH, '//*[@id="pool_enablehostsafterreloadsflag"]')),
    ("VLAN_PROVISIONS_ALLOWED", (By.XPATH, '//*[@id="pool_enablehostsafterreloadsflag"]')),
    ("DISABLE_HOST_AUTO_MIGRATION", (By.XPATH, '//*[@id="pool_disablehostautomigrationflag"]')),
    ("POOL_ROLES", (By.XPATH, '//*[@id="virtual_updatepool_3_details"]/tbody/tr[3]/td[2]'))
    # ... any other locators related to the Update PoolPage

]
