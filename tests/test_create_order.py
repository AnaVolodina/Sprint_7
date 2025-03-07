import allure
import requests
import pytest
from endpoints import URL
from data import TestData


class TestCreateOrder:

    @allure.title('Проверка успешного создания заказа')
    @allure.description('Проверка успешного создания заказа при выборе в поле color одного цвета, двух цветов и без выбора цвета')
    @pytest.mark.parametrize('color', [
        TestData.ORDER_DATA_BLACK, TestData.ORDER_DATA_GREY,
        TestData.ORDER_DATA_MULTICOLOR, TestData.ORDER_DATA_NO_COLOR
    ])
    def test_create_order_with_filled_color_field_successful(self, color):
        payload = color
        response = requests.post(URL.CREATE_ORDER, json=payload)
        assert response.status_code == 201 and 'track' in response.json()