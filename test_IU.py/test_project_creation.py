import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import allure
from page.aythpage import AuthPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.feature("Авторизация")
@allure.story("Успешная авторизация с корректными данными")
def test_gud_login(driver):
    page = AuthPage(driver)
    LOGIN = "p-akimova@mail.ru"
    PASSWORD = "inCanto720"

    with allure.step("Открытие страницы авторизации"):
        page.open()

    with allure.step(f"Ввод логина: {LOGIN}"):
        page.enter_login(LOGIN)

    with allure.step(f"Ввод пароля: {PASSWORD}"):
        page.enter_password(PASSWORD)

    with allure.step("Нажатие кнопки входа"):
        page.submit_login()

    with allure.step("Проверка успешного входа"):
        assert page.is_login() is True, "Авторизация не прошла успешно"


@allure.feature("Авторизация")
@allure.story("Неуспешная авторизация с некорректными данными")
def test_nogud_login(driver):
    page = AuthPage(driver)
    LOGIN = "p-akimova@mail"
    PASSWORD = "inCant"

    with allure.step("Открытие страницы авторизации"):
        page.open()

    with allure.step(f"Ввод некорректного логина: {LOGIN}"):
        page.enter_login(LOGIN)

    with allure.step(f"Ввод некорректного пароля: {PASSWORD}"):
        page.enter_password(PASSWORD)

    with allure.step("Нажатие кнопки входа"):
        page.submit_login()

    with allure.step("Проверка неуспешного входа"):
        assert (
            page.is_login() is False
        ), "Авторизация прошла успешно, хотя должна была провалиться"
