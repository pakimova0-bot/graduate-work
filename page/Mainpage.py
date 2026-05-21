from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
import time

from selenium.webdriver.support.ui import WebDriverWait


class MainPage:

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_prodect(self):
        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//span[text()='Добавить проект с задачами']")
            )
        ).click()

    def add_prodect_title(self, title):
        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//input[@placeholder='Введите название проекта…']")
            )
        ).click()
        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//input[@placeholder='Введите название проекта…']")
            )
        ).send_keys(title)

    def prodect_button_click(self):
        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//div[text()='Добавить проект с задачами']")
            )
        ).click()

    def prodect_title_list(self):
        time.sleep(2)
        proj_cards = self.wait.until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, '[data-testid="project-title"]')
            )
        )
        return [card.text for card in proj_cards]

    def is_button_enabled(self, button_text="Добавить проект с задачами"):
        """
        Проверяет, активна ли кнопка.
        button_text: текст внутри кнопки для поиска.

        Returns:
        bool: True — кнопка активна, False — неактивна.
        """
        # Находим кнопку по тексту внутри вложенного div
        button = self.driver.find_element(
            By.XPATH,
            f'//div[@role="button" and .//div[text()="{button_text}"]]',
        )

        # Получаем значение атрибута class
        class_attribute = button.get_attribute("class")

        # Проверяем отсутствие класса pointer-events-none
        return "pointer-events-none" not in class_attribute

    def delete_project(self, title: str = None) -> None:
        """
        Удаляет созданный для теста проект.
        :param title: str — название проекта.
        """
        cards = self.wait.until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, '[data-testid="project-title"]')
            )
        )
        if title is not None:
            for card in cards:
                if title in card.text:
                    css = '[class="flex-none h-16 w-16 flex items-center justify-center"]'  # noqa
                    self.driver.find_element(By.CSS_SELECTOR, css).click()
                    self.wait.until(
                        EC.element_to_be_clickable(
                            (By.XPATH, "//div[text()='Удалить']")
                        )
                    ).click()
                    css = '[class="flex bg-action-attention-default text-invert px-16 py-12 plain-text-semibold hover:bg-action-attention-hover active:bg-action-attention-pressed rounded-8 w-fit cursor-pointer select-none"]'  # noqa
                    self.wait.until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, css))
                    ).click()
