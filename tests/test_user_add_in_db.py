from pages.main_page import MainPage
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.admin_page import AdminPage
from time import sleep
from conftest import db_actions


def test_add_user(browser, setup_teardown):
    group_name, username, password, config = setup_teardown

    base_page = BasePage(browser)
    base_page.open_base_page()
    main_page = MainPage(browser)

    main_page.open_login_page()
    login_page = LoginPage(browser)
    sleep(1)
    login_page.login(config)
    admin_page = AdminPage(browser)
    admin_page.admin_page_is_present()
    admin_page.click_on_add_user()
    sleep(1)
    admin_page.add_user(username, password)
    admin_page.user_add_in_group(group_name)
    db_actions.get_user_in_group(group_name, username)
