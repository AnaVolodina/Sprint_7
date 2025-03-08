import requests
import random
import string
from endpoints import URL
from data import TestData


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string

# метод регистрации нового курьера возвращает список из логина и пароля
# если регистрация не удалась, возвращает пустой список
def register_new_courier_and_return_login_password():
    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    def generate_random_string_for_create_courier(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    # создаём список, чтобы метод мог его вернуть
    login_pass = []

    # генерируем логин, пароль и имя курьера
    login = generate_random_string_for_create_courier(10)
    password = generate_random_string_for_create_courier(10)
    first_name = generate_random_string_for_create_courier(10)

    # собираем тело запроса
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.post(URL.CREATE_COURIER, data=payload)

    # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    # возвращаем список
    return login_pass

def login_and_get_courier_id(payload):
    login_response = requests.post(URL.LOGIN_COURIER, json=payload)
    assert login_response.status_code == 200
    courier_id = login_response.json().get('id')
    assert courier_id is not None
    return courier_id

def delete_courier(courier_id):
    delete_response = requests.delete(f"{URL.CREATE_COURIER}/{courier_id}")
    assert delete_response.status_code == 200

def cancel_an_order(track):
    payload = {"track": track}
    response = requests.put(URL.CANCEL_AN_ORDER, json=payload)
    return response
