class Data:
    BASE_URL = 'https://stellarburgers.nomoreparties.site'
    REGISTER_URL = f'{BASE_URL}/api/auth/register'
    DELETE_USER_URL = f'{BASE_URL}/api/auth/user'
    LOGIN_URL = f'{BASE_URL}/api/auth/login'
    UPDATE_USER_DATA_URL = f'{BASE_URL}/api/auth/user'
    CREATE_ORDER_URL = f'{BASE_URL}/api/orders'
    GET_USER_ORDERS_URL = f'{BASE_URL}/api/orders'

    CORRECT_BURGER = {'ingredients': ['61c0c5a71d1f82001bdaaa6d', '61c0c5a71d1f82001bdaaa70']}
    EMPTY_BURGER = {'ingredients': []}
    INVALID_BURGER = {'ingredients': ['61c0c5a71d1f82001bd6d', '61c0c5a71d1f82001bd33333']}