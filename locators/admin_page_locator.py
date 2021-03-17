from selenium.webdriver.common.by import By


class AdminPageLocator:
    LOCATOR_ADMIN_PAGE_TITLE = (By.XPATH, '//h1[text()="Site administration"]')
    LOCATOR_LINK_ADD_GROUP = (By.XPATH, '//a[text()="Groups"]')
    LOCATOR_GROUPS_NAME = (By.CLASS_NAME, 'field-__str__')
    LOCATOR_LINK_ADD_USER = (By.XPATH, '//a[@href="/admin/auth/user/add/"]')
    LOCATOR_USERNAME = (By.CSS_SELECTOR, '[name="username"]')
    LOCATOR_PASSWORD = (By.CSS_SELECTOR, '[name="password1"]')
    LOCATOR_CONFIRM_PASSWORD = (By.CSS_SELECTOR, '[name="password2"]')
    LOCATOR_BUTTON_SAVE = (By.CSS_SELECTOR, '[name="_save"]')
    LOCATOR_FIELD_FIRST_NAME = (By.CSS_SELECTOR, '[name="first_name"]')
    LOCATOR_FIELD_LAST_NAME = (By.CSS_SELECTOR, '[name="last_name"]')
    LOCATOR_EMAIL_ADDRESS = (By.CSS_SELECTOR, '[name="email"]')
    LOCATOR_SUPERUSER_STATUS = (By.CSS_SELECTOR, '[name="is_superuser"]')
    LOCATOR_BUTTON_SAVE_IN_CHANGE_USER = (By.CSS_SELECTOR, '[value="Save"]')
    LOCATOR_ADD_USER_IN_GROUP_CHOOSE_ALL = (By.ID, "id_groups_add_all_link")
    LOCATOR_FIND_SELECT = (By.TAG_NAME, 'select')
    LOCATOR_ADD_USER_IN_GROUP = (By.CSS_SELECTOR, '[id="id_groups_add_link"]')
