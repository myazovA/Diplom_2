import allure
import requests
from data import Data

class TestCreateUser:

    @allure.title('Создание уникального пользователя')
    def test_create_unique_user(self, generate_reg_data):
        user = generate_reg_data
        response = requests.post(Data.REGISTER_URL, data=user)
        assert response.status_code == 200
        requests.delete(Data.DELETE_USER_URL, data=user)

    @allure.title('Повторное создание имеющегося пользователя')
    def test_create_registered_user(self, generate_reg_data):
        user = generate_reg_data
        requests.post(Data.REGISTER_URL, data=user)
        response = requests.post(Data.REGISTER_URL, data=user)
        assert response.status_code == 403 and '"success": false' and '"message": "User already exists"'
        requests.delete(Data.DELETE_USER_URL, data=user)

    @allure.title('Создание пользователя без пароля')
    def test_create_user_without_pass(self, generate_reg_data):
        user = generate_reg_data
        user['password'] = ''
        response = requests.post(Data.REGISTER_URL, data=user)
        assert response.status_code == 403 and '"success": false' \
               and '"message": "Email, password and name are required fields"'
        requests.delete(Data.DELETE_USER_URL, data=user)