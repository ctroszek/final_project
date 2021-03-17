from pages.base_page import BasePage
from locators.admin_page_locator import AdminPageLocator
from selenium.webdriver.support.ui import Select


class AdminPage(BasePage):

    def admin_page_is_present(self):
        title_text = self.find_element(
            AdminPageLocator.LOCATOR_ADMIN_PAGE_TITLE).text
        text = 'Site administration'
        assert title_text == text,\
            f'Title text {title_text} on admin page does not eq {text}'

    def click_on_groups(self):
        link_groups = self.find_element(AdminPageLocator.LOCATOR_LINK_ADD_GROUP)
        link_groups.click()

    def group_is_exist(self, group_name):
        group_list = self.find_elements(AdminPageLocator.LOCATOR_GROUPS_NAME)
        exist = False
        for i in group_list:
            if group_name in i.text:
                exist = True
        assert exist, f"group {group_name} not found"

    def click_on_add_user(self):
        link_add_user = self.find_element(
            AdminPageLocator.LOCATOR_LINK_ADD_USER
        )
        link_add_user.click()

    def add_user(self, username, password):
        user = self.find_element(AdminPageLocator.LOCATOR_USERNAME)
        user.send_keys(username)
        passwd = self.find_element(AdminPageLocator.LOCATOR_PASSWORD)
        passwd.send_keys(password)
        confirm_password = self.find_element(
            AdminPageLocator.LOCATOR_CONFIRM_PASSWORD
        )
        confirm_password.send_keys(password)
        button_save = self.find_element(AdminPageLocator.LOCATOR_BUTTON_SAVE)
        button_save.click()

    def change_user(self, firstname, lastname, email):
        first_name = self.find_element(
            AdminPageLocator.LOCATOR_FIELD_FIRST_NAME
        )
        first_name.send_keys(firstname)
        last_name = self.find_element(AdminPageLocator.LOCATOR_FIELD_LAST_NAME)
        last_name.send_keys(lastname)
        email_address = self.find_element(
            AdminPageLocator.LOCATOR_EMAIL_ADDRESS
        )
        email_address.send_keys(email)
        superuser_status = self.find_element(
            AdminPageLocator.LOCATOR_SUPERUSER_STATUS
        )
        superuser_status.click()

    def user_add_in_group(self):
        find_group = Select(self.find_element(AdminPageLocator.LOCATOR_FIND_SELECT))
        find_group.select_by_visible_text('postgres')
        group_add_link = self.find_element(
            AdminPageLocator.LOCATOR_ADD_USER_IN_GROUP
        )
        group_add_link.click()
        button_save = self.find_element(
            AdminPageLocator.LOCATOR_BUTTON_SAVE_IN_CHANGE_USER
        )
        button_save.click()

    # def user_in_db(self, username):

