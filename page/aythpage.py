from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import WebDriverWait


class AuthPage:

    URL = "https://ru.yougile.com/team/"

    EMAIL_INPUT = (By.CSS_SELECTOR, '[type="email"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '[type="password"]')
    LOGIN_BUTTON = (By.XPATH, "//div[text()='Войти']")
    PROFILE_ICON = (By.CSS_SELECTOR, "img")
    LOGIN = "p-akimova@mail.ru"
    PASSWORD = "inCanto720"
    PRIF = (
        By.XPATH,
        '//div[@data-testid="left-sidebar"]//div[text()="Моя компания"]',
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        """Метод переходит на страницу"""
        self.driver.get(self.URL)

    def make_login(self, login=LOGIN, pas=PASSWORD) -> None:
        """Метод воодит логин и пароль"""
        self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, '//input[@placeholder="example@mail.ru"]')
            )
        ).send_keys(login)
        self.driver.find_element(
            By.XPATH, '//input[@type="password"]'
        ).send_keys(pas)
        self.driver.find_element(By.XPATH, '//div[text()="Войти"]').click()

    def is_login(self) -> bool:
        """Метод проверяет авторизацию"""
        try:
            self.wait.until(EC.presence_of_element_located(self.PRIF))
            return True
        except TimeoutException:
            return False
