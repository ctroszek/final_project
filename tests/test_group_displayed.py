from pages.main_page import MainPage
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.admin_page import AdminPage
from time import sleep
from conftest import group_add, group_delete


#SLEEPS DELETE!!!
def test_group_displayed(browser):

    group_add()

    base_page = BasePage(browser)
    base_page.open_base_page()
    main_page = MainPage(browser)

    main_page.open_login_page()
    login_page = LoginPage(browser)
    sleep(2)
    login_page.login('admin', 'password')
    admin_page = AdminPage(browser)
    sleep(2)

    admin_page.admin_page_is_present()
    admin_page.click_on_groups()
    sleep(2)
    admin_page.group_is_exist('postgres')

    group_delete()
