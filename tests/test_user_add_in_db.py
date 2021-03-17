from pages.main_page import MainPage
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.admin_page import AdminPage
from time import sleep
from config import generate_password, generate_username, generate_email,\
    generate_first_last_name
from conftest import check_if_group_exist, group_delete, group_add


def test_add_user(browser):
    group_add()

    base_page = BasePage(browser)
    base_page.open_base_page()
    main_page = MainPage(browser)

    main_page.open_login_page()
    login_page = LoginPage(browser)
    sleep(2)
    login_page.login('admin', 'password')
    admin_page = AdminPage(browser)
    sleep(3)

    admin_page.admin_page_is_present()
    admin_page.click_on_add_user()
    sleep(3)

    username = generate_username(7)
    password = generate_password(10)
    admin_page.add_user(username, password)
    sleep(3)

    firstname = generate_first_last_name(6)
    lastname = generate_first_last_name(8)
    email = generate_email(8)
    sleep(4)
    admin_page.change_user(firstname, lastname, email)
    sleep(4)
    admin_page.user_add_in_group()
    sleep(1)

    