import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import allure
from page.aythpage import AuthPage
from page.Mainpage import MainPage


@allure.feature("Авторизация")
@allure.story("Успешная авторизация с корректными данными")
@pytest.mark.ui
def test_gud_login(driver):
    page = AuthPage(driver)

    with allure.step("Открытие страницы авторизации"):
        page.open()

    with allure.step(f"Ввод логина и пароля правильного"):
        page.make_login()

    with allure.step("Проверка успешного входа"):
        assert page.is_login() is True, "Авторизация не прошла успешно"


@allure.feature("Авторизация")
@allure.story("Неуспешная авторизация с некорректными данными")
@pytest.mark.ui
def test_nogud_login(driver):
    page = AuthPage(driver)
    LOGIN = "p-akimova@mail"
    PASSWORD = "inCant"

    with allure.step("Открытие страницы авторизации"):
        page.open()

    with allure.step(f"Ввод некорректного логина, пароля: {LOGIN} {PASSWORD}"):
        page.make_login(LOGIN, PASSWORD)

    with allure.step("Проверка неуспешного входа"):
        assert (
            page.is_login() is False
        ), "Авторизация прошла успешно, хотя должна была провалиться"


@allure.story("Создание проекта")
@allure.title("Создание проекта с валидным названием")
@allure.description(
    "Тест проверяет успешное создание нового проекта с корректным названием"
)
@pytest.mark.ui
def test_create(driver):
    page = AuthPage(driver)

    with allure.step("Открытие страницы авторизации"):
        page.open()

    with allure.step(f"Ввод логина и пароля правильного"):
        page.make_login()

    with allure.step("Проверка успешного входа"):
        assert page.is_login() is True, "Авторизация не прошла успешно"
    main = MainPage(driver)
    title = "Дипломная работа"
    with allure.step("Создание проекта"):
        main.add_prodect()
        main.add_prodect_title(title)
        main.prodect_button_click()
    with allure.step("Проверка наличия карточки проекта"):
        proj_card = main.prodect_title_list()
        assert title in proj_card


@allure.story("Создание проекта")
@allure.title("Создание проекта с пустым названием (негативный сценарий)")
@allure.description(
    "Тест проверяет, что нельзя создать проект с пустым названием"
)
@pytest.mark.ui
def test_create_emty_title(driver):
    page = AuthPage(driver)

    with allure.step("Открытие страницы авторизации"):
        page.open()

    with allure.step(f"Ввод логина и пароля правильного"):
        page.make_login()

    with allure.step("Проверка успешного входа"):
        assert page.is_login() is True, "Авторизация не прошла успешно"
    main = MainPage(driver)
    with allure.step("Создание карточки проекта с пустым названием"):
        title = ""
        main.add_prodect()
        main.add_prodect_title(title)
        assert main.is_button_enabled() == False


@allure.story("Удаление проекта")
@allure.title("Удаление существующего проекта")
@allure.description("Тест проверяет успешное удаление существующего проекта")
@pytest.mark.ui
def test_delete(driver):
    page = AuthPage(driver)

    with allure.step("Открытие страницы авторизации"):
        page.open()

    with allure.step(f"Ввод логина и пароля правильного"):
        page.make_login()

    with allure.step("Проверка успешного входа"):
        assert page.is_login() is True, "Авторизация не прошла успешно"
    main = MainPage(driver)
    with allure.step("Создание карторчки нового проекта"):
        title = "Акт"
        main.add_prodect()
        main.add_prodect_title(title)
        main.prodect_button_click()
    with allure.step("Проверка наличия карточки проекта"):
        proj_card = main.prodect_title_list()
        assert title in proj_card
    with allure.step("Удаление карточки проекта"):
        main.delete_project(title)
    with allure.step("Проверка успешного удаления карточки проекта"):
        proj_card = main.prodect_title_list()
        assert title not in proj_card
