import allure
import requests
from data import Data

class TestUserDataChanging:

    @allure.title('Изменение даных залогиненного пользователя')
    def test_user_data_changing_with_auth(self, generate_reg_data):
        user = generate_reg_data
        user_new_data = generate_reg_data
        requests.post(Data.REGISTER_URL, data=user)
        login = requests.post(Data.LOGIN_URL, data=user)
        id_user = login.json()["accessToken"]
        response = requests.get(Data.UPDATE_USER_DATA_URL, headers={"Authorization": id_user}, data=user_new_data)
        assert response.status_code == 200 and '"success": true'
        requests.delete(Data.DELETE_USER_URL, data=user_new_data)

    @allure.title('Изменение даных не залогиненного пользователя')
    def test_user_data_changing_without_auth(self, generate_reg_data):
        user = generate_reg_data
        user_new_data = generate_reg_data
        requests.post(Data.REGISTER_URL, data=user)
        response = requests.get(Data.UPDATE_USER_DATA_URL, data=user_new_data)
        assert response.status_code == 401 and '"success": false' and '"message": "You should be authorised"'
        requests.delete(Data.DELETE_USER_URL, data=user)