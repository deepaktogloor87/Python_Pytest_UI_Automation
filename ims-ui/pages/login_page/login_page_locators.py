from selenium.webdriver.common.by import By

login_page_locators = [


    ("USERNAME", (By.XPATH, "//*[@id='user_username'][@class='logintext']")),
    ("PASSWORD", (By.ID, "user_password")),
    ("LOGIN_BUTTON", (By.LINK_TEXT, "login")),
    ("LOGOUT_BUTTON", (By.LINK_TEXT, "Logout")),
    ("LOGOUT_TEXT", (By.XPATH, "//*[contains(text(),'You have logged out of the SoftLayer Internal Management Portal.')]"))
    # ... any other locators related to the LoginPage

]
