from pages.base_page import BasePage
from locators.main_page_locator import MainPageLocators


class MainPage(BasePage):

    def open_login_page(self):
        button = self.find_element(MainPageLocators.LOCATOR_GO_TO_ADMIN_BUTTON)
        button.click()

