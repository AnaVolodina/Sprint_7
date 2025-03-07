
class TestData:
    VALID_LOGIN = 'lucky'
    VALID_PASSWORD = '2233'
    VALID_NAME = 'Parker'

    MESSAGE_CONFLICT = {'code': 409, "message": "Этот логин уже используется. Попробуйте другой."}
    MESSAGE_BAD_REQUEST_CREATE_ACCOUNT = {'code': 400, "message": "Недостаточно данных для создания учетной записи"}
    MESSAGE_NOT_FOUND = {'code': 404, "message": "Учетная запись не найдена"}
    MESSAGE_BAD_REQUEST_LOGIN = {'code': 400, "message": "Недостаточно данных для входа"}

    ORDER_DATA_BLACK = {
        "firstName": "John",
        "lastName": "Bing",
        "address": "Cafe",
        "metroStation": 1,
        "phone": "+7 800 123 45 67",
        "rentTime": 2,
        "deliveryDate": "2025-03-15",
        "comment": "Call me",
        "color": [
            "BLACK"
        ]
    }

    ORDER_DATA_GREY = {
        "firstName": "John",
        "lastName": "Bing",
        "address": "Cafe",
        "metroStation": 1,
        "phone": "+7 800 123 45 67",
        "rentTime": 2,
        "deliveryDate": "2025-03-15",
        "comment": "Call me",
        "color": [
            "GREY"
        ]
    }

    ORDER_DATA_MULTICOLOR = {
        "firstName": "John",
        "lastName": "Bing",
        "address": "Cafe",
        "metroStation": 1,
        "phone": "+7 800 123 45 67",
        "rentTime": 2,
        "deliveryDate": "2025-03-15",
        "comment": "Call me",
        "color": [
            "BLACK", "GREY"
        ]
    }

    ORDER_DATA_NO_COLOR = {
        "firstName": "John",
        "lastName": "Bing",
        "address": "Cafe",
        "metroStation": 1,
        "phone": "+7 800 123 45 67",
        "rentTime": 2,
        "deliveryDate": "2025-03-15",
        "comment": "Call me",
        "color": []
    }