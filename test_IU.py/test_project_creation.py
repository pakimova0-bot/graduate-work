import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from page.aythpage import AuthPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_gud_login(driver):
    page = AuthPage(driver)
    LOGIN = "p-akimova@mail.ru"
    PASSWORD = "inCanto720"
    # Открытие страницы
    page.open()

    # ввести логин и пароль
    page.make_login()
    assert page.is_login() is True

def test_nogud_login(driver):
    page = AuthPage(driver)
    LOGIN = "p-akimova@mail"
    PASSWORD = "inCant"
    # Открытие страницы
    page.open()

    # ввести логин и пароль
    page.make_login(login = LOGIN, pas = PASSWORD)
    assert page.is_login() is False