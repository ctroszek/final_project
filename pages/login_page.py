from pages.base_page import BasePage
from locators.login_page_locator import LoginPageLocator


class LoginPage(BasePage):

    def login(self, config):
        username_field = self.find_element(
            LoginPageLocator.LOCATOR_USERNAME_FIELD)
        username_field.send_keys(config['admin'])
        password_field = self.find_element(
            LoginPageLocator.LOCATOR_PASSWD_FIELD)
        password_field.send_keys(config['password'])
        button_log_in = self.find_element(
            LoginPageLocator.LOCATOR_BUTTON_LOG_IN)
        button_log_in.click()

    def login_form_is_present(self):
        auth_text = self.find_element(
            LoginPageLocator.LOCATOR_LOGIN_PAGE_TITLE).text
        assert auth_text == "Django administration"

