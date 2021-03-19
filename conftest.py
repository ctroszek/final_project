import pytest
from selenium import webdriver
from connect import DB_URL
import json
from postgres.db__base_actions import DBActions
from random import randint
import time
from selenium.webdriver.chrome.options import Options

db_actions = DBActions(DB_URL)


@pytest.fixture
def setup_teardown():
    json_string = open('json_files/for_user_add.json', 'r').read()
    config = json.loads(json_string)

    group_name = 'gr-' + str(time.time())
    username = 'user-' + str(time.time())
    password = 'pass' + str(randint(100000, 999999))

    db_actions.group_creation(group_name)
    yield group_name, username, password, config

    db_actions.user_group_delete(group_name, username)
    db_actions.group_delete(group_name)
    db_actions.user_delete(username)


@pytest.fixture
def browser():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
#     chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    browser = webdriver.Chrome(options=chrome_options)
    # browser.maximize_window()
    browser.implicitly_wait(5)
    yield browser
    browser.quit()


@pytest.fixture
def api_setting():
    json_file = open('json_files/for_pet_data.json', 'r').read()
    user_data = json.loads(json_file)
    yield user_data


@pytest.fixture
def user_setting():
    json_file = open('json_files/for_user_add.json', 'r').read()
    admin_data = json.loads(json_file)
    return admin_data


@pytest.fixture
def json_bd_actions():
    json_file = open('postgres/data_for_db.json', 'r').read()
    data = json.loads(json_file)
    return data
