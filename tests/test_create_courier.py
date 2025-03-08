import allure
import requests
import pytest
from endpoints import URL
from helper import generate_random_string, delete_courier, login_and_get_courier_id
from data import TestData


class TestCreateCourier:
    @allure.title('Создание курьера')
    @allure.description('Проверка возможности создания курьера при заполнении всех полей валидными данными')
    def test_create_courier_account_created(self):
        payload = {'login': generate_random_string(10), 'password': generate_random_string(10), 'firstName': generate_random_string(10)}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(URL.CREATE_COURIER, json=payload, headers=headers)
        assert response.status_code == 201 and response.json() == TestData.OK_RESPONSE
        courier_id = login_and_get_courier_id(payload)
        delete_courier(courier_id)
    @allure.description('Проверка возможности создания курьера при заполнении обязательных полей валидными данными')
    def test_create_courier_required_fields_filled_account_created(self):
        payload = {'login': generate_random_string(10), 'password': generate_random_string(10)}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(URL.CREATE_COURIER, json=payload, headers=headers)
        assert response.status_code == 201 and response.json() == TestData.OK_RESPONSE
        courier_id = login_and_get_courier_id(payload)
        delete_courier(courier_id)

    @allure.description('Проверка появления сообщения об ошибке при попытке создания курьера с существующим логином')
    def test_create_courier_with_existing_login_error(self):
        payload = {'login': TestData.VALID_LOGIN, 'password': generate_random_string(10)}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(URL.CREATE_COURIER, json=payload, headers=headers)
        assert response.status_code == 409 and response.json() == TestData.MESSAGE_CONFLICT

    @allure.description('Проверка появления сообщения об ошибке при незаполненных обязательных полях')
    @pytest.mark.parametrize('login, password', [
        ('', generate_random_string(10)),
        (generate_random_string(10), ''),
        ('', '')
    ])
    def test_create_courier_required_fields_not_filled_error(self, login, password):
        payload = {'login': login, 'password': password}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(URL.CREATE_COURIER, json=payload, headers=headers)
        assert response.status_code == 400 and response.json() == TestData.MESSAGE_BAD_REQUEST_CREATE_ACCOUNT



