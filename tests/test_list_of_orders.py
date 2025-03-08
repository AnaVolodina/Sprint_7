import allure
import requests
from endpoints import URL


class TestGetOrders:

    @allure.title('Проверка успешного получения списка заказов')
    def test_get_orders_list_successful(self):
        response = requests.get(URL.GET_LIST_OF_ORDERS)
        assert (type(response.json()['orders']) == list
                and response.status_code == 200
                and 'id' in response.json()['orders'][0])