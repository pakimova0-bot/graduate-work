# skypro_final_https://ru.yougile.com/
Ссылка на отчет https://p-akimova.yonote.ru/share/86921e2a-23c4-49b9-9b86-9b17a789e1a4

# Автоматизация UI- и API‑тестов для Юджил
Проект использует следующие технологии и синтаксис:

Python: Основной язык программирования для написания тестов.
Selenium: Библиотека для автоматизации взаимодействия с веб-браузером.
Pytest: Фреймворк для написания и запуска тестов.
Allure: Инструмент для генерации отчетов о выполнении тестов.
Проект содержит набор автоматизированных тестов для проверки функциональности веб‑сайта Юджил через UI и API.

### Структура проекта

DIPLOMA/
page
    main_pages.py # Методы для ui
test
    test_ui.py # UI‑тесты
    test_api.py # API‑тесты
requirements.txt # Зависимости
README.md # Эта документация
pytest.ini
.gitignore
conftest.py

# Запуск тестов
## Все тесты - bash
pytest
## Только UI‑тесты - bash
pytest -m ui 
## Только API‑тесты - bash
pytest -m api 
## С подробной информацией - bash
pytest -v 

# Запуск с Allure отчетом
pytest --alluredir=allure-results -v
allure serve allure-results 

# Особенности реализации
Page Object Model — для UI‑тестов используется шаблон Page Object (aythpage.py).
Allure‑отчёты — все тесты снабжены Allure‑разметкой для наглядных отчётов.
