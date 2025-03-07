import allure
import requests
import pytest
from endpoints import URL
from helper import register_new_courier_and_return_login_password, generate_random_string
from data import TestData


class TestLoginCourier:

    @allure.title('Проверка авторизации курьера')
    @allure.description('Проверка успешной авторизации при заполнении полей login и password валидными данными')
    def test_login_courier_required_fields_filled_successful(self):
        create_login = register_new_courier_and_return_login_password()
        login, password, first_name = create_login
        payload = {'login': login, 'password': password}
        response = requests.post(URL.LOGIN_COURIER, data=payload)
        assert response.status_code == 200 and 'id' in response.json()

    @allure.description('Проверка неуспешной авторизации при незаполненных обязательных полях')
    @pytest.mark.parametrize('login, password', [
        ('', TestData.VALID_PASSWORD),
        (TestData.VALID_LOGIN, ''),
        ('', '')
    ])
    def test_login_courier_required_fields_not_filled_failure(self, login, password):
        payload = {'login': login, 'password': password}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(URL.LOGIN_COURIER, json=payload, headers=headers)
        assert response.status_code == 400 and response.json() == TestData.MESSAGE_BAD_REQUEST_LOGIN

    @allure.description('Проверка неуспешной авторизации при некорректном заполнении обязательных полей')
    @pytest.mark.parametrize('login, password', [
        (generate_random_string(10), TestData.VALID_PASSWORD),
        (TestData.VALID_LOGIN, generate_random_string(10))
    ])
    def test_login_courier_with_invalid_data_failure(self, login, password):
        payload = {'login': login, 'password': password}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(URL.LOGIN_COURIER, json=payload, headers=headers)
        assert response.status_code == 404 and response.json() == TestData.MESSAGE_NOT_FOUND