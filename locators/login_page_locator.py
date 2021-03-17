from selenium.webdriver.common.by import By


class LoginPageLocator:
    LOCATOR_LOGIN_PAGE_TITLE = (By.XPATH, '//a[@href="/admin/"]')
    LOCATOR_USERNAME_FIELD = (By.XPATH, '//input[@id="id_username"]')
    LOCATOR_PASSWD_FIELD = (By.XPATH, '//*[@id="id_password"]')
    LOCATOR_BUTTON_LOG_IN = (By.XPATH, '//input[@type="submit"]')
