import allure
import requests
from data import Data

class TestLogin:

    @allure.title('Логин под существующим пользователем')
    def test_created_user_login(self, generate_reg_data):
        user = generate_reg_data
        requests.post(Data.REGISTER_URL, data=user)
        response = requests.post(Data.LOGIN_URL, data=user)
        assert response.status_code == 200 and '"success": true'
        requests.delete(Data.DELETE_USER_URL, data=user)

    @allure.title('Логин с неправильным логином и паролем')
    def test_wrong_login_and_pass_login(self, generate_reg_data):
        user = generate_reg_data
        user['email'] = 'sus'
        user['password'] = '222'
        requests.post(Data.REGISTER_URL, data=user)
        response = requests.post(Data.LOGIN_URL, data=user)
        assert response.status_code == 401 and '"success": false' and '"message": "email or password are incorrect"'
        requests.delete(Data.DELETE_USER_URL, data=user)