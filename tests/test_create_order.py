import allure
import requests
from data import Data

class TestCreateOrder:

    @allure.title('Создание заказа с авторизацией и ингредиентами')
    def test_create_order_with_auth(self, generate_reg_data):
        user = generate_reg_data
        requests.post(Data.REGISTER_URL, data=user)
        requests.post(Data.LOGIN_URL, data=user)
        response = requests.post(Data.CREATE_ORDER_URL, data=Data.CORRECT_BURGER)
        assert response.status_code == 200 and '"success": true'
        requests.delete(Data.DELETE_USER_URL, data=user)

    @allure.title('Создание заказа без авторизации и с ингредиентами')
    def test_create_order_without_auth(self, generate_reg_data):
        user = generate_reg_data
        requests.post(Data.REGISTER_URL, data=user)
        response = requests.post(Data.CREATE_ORDER_URL, data=Data.CORRECT_BURGER)
        assert response.status_code == 200 and '"success": true'
        requests.delete(Data.DELETE_USER_URL, data=user)

    @allure.title('Создание заказа без ингредиентов')
    def test_create_order_without_ingridients(self, generate_reg_data):
        user = generate_reg_data
        requests.post(Data.REGISTER_URL, data=user)
        response = requests.post(Data.CREATE_ORDER_URL, data=Data.EMPTY_BURGER)
        assert response.status_code == 400 and '"success": false' and '"message": "Ingredient ids must be provided"'
        requests.delete(Data.DELETE_USER_URL, data=user)

    @allure.title('Создание заказа с некорректным ингридиентом')
    def test_create_order_with_wrong_ingridient(self, generate_reg_data):
        user = generate_reg_data
        requests.post(Data.REGISTER_URL, data=user)
        response = requests.post(Data.CREATE_ORDER_URL, data=Data.INVALID_BURGER)
        assert response.status_code == 500 and '"success": false'
        requests.delete(Data.DELETE_USER_URL, data=user)