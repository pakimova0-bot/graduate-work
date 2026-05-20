import requests
import allure

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer 3p3pq-pzoQb03hAIbZ3zGBqHQtQkKeORQY4VWKTCPEnQ-wmyHkrZxpfiuYHeZbMr",
}
base_url = "https://ru.yougile.com/api-v2/"


@allure.feature("Авторизация")
@allure.story("Успешная авторизация в системе")
def test_to_activation():
    with allure.step("Подготовка данных для авторизации"):
        payload = {"login": "p-akimova@mail.ru", "password": "inCanto720"}

    with allure.step("Отправка запроса на авторизацию"):
        response = requests.post(
            f"{base_url}auth/companies", headers=headers, json=payload
        )

    with allure.step("Проверка статуса ответа"):
        assert (
            response.status_code == 200
        ), f"Ожидался статус 200, получен {response.status_code}"


@allure.feature("Проекты")
@allure.story("Создание нового проекта")
def test_to_create():
    with allure.step("Подготовка данных для создания проекта"):
        payload = {"title": "Знания"}

    with allure.step("Отправка запроса на создание проекта"):
        response = requests.post(
            f"{base_url}projects", headers=headers, json=payload
        )

    with allure.step("Проверка статуса ответа"):
        assert (
            response.status_code == 201
        ), f"Ожидался статус 201, получен {response.status_code}"


@allure.feature("Проекты")
@allure.story("Редактирование проекта")
def test_to_change():
    old_title = "Новое задание"
    new_title = "Замена задания"

    with allure.step("Создание проекта для редактирования"):
        payload_create = {"title": old_title}
        response_create = requests.post(
            f"{base_url}projects", headers=headers, json=payload_create
        )
        assert response_create.status_code == 201
        project_data = response_create.json()
        project_id = project_data["id"]

    with allure.step(f"Редактирование проекта с ID {project_id}"):
        payload_update = {"title": new_title}
        response_update = requests.put(
            f"{base_url}projects/{project_id}",
            headers=headers,
            json=payload_update,
        )
        assert (
            response_update.status_code == 200
        ), f"Ожидался статус 200, получен {response_update.status_code}"

    with allure.step(f"Проверка обновлённых данных проекта с ID {project_id}"):
        response_get = requests.get(
            f"{base_url}projects/{project_id}", headers=headers
        )
        assert response_get.status_code == 200
        updated_data = response_get.json()
        assert (
            updated_data["title"] == new_title
        ), f"Заголовок не обновился: ожидалось '{new_title}', получено '{updated_data['title']}'"
