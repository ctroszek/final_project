import pytest
from selenium import webdriver
import psycopg2
import select


# @pytest.fixture()
# def browser():
#     driver = webdriver.Chrome()
#     yield driver
#     driver.quit()


@pytest.fixture()
def browser():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


def group_add():
    connection = psycopg2.connect(user="postgres",
                                  password="postgres",
                                  host="localhost",
                                  port="5432",
                                  database="postgres")

    cursor = connection.cursor()
    insert_query = """
    INSERT INTO public.auth_group (name) VALUES ('postgres')
    """
    cursor.execute(insert_query)
    connection.commit()
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")


def group_delete():
    connection = psycopg2.connect(user="postgres",
                                  password="postgres",
                                  host="localhost",
                                  port="5432",
                                  database="postgres")

    cursor = connection.cursor()
    delete_query = """
        DELETE FROM public.auth_group WHERE name='postgres'
        """
    cursor.execute(delete_query)
    connection.commit()


def check_if_group_exist():
    connection = psycopg2.connect(user="postgres",
                                  password="postgres",
                                  host="localhost",
                                  port="5432",
                                  database="postgres")

    cursor = connection.cursor()
    exist_or_no = """
            SELECT * FROM public.auth_group WHERE name='postgres'
            """
    cursor.execute(exist_or_no)
    result = cursor.fetchall()
    print(result)

# def check_if_user_in_group():






