import allure
import requests
from data import Data

class TestGetUserOrders:

    @allure.title('Получение списка заказов авторизованного пользователя')
    def test_get_auth_user_orders(self, generate_reg_data):
        user = generate_reg_data
        requests.post(Data.REGISTER_URL, data=user)
        login = requests.post(Data.LOGIN_URL, data=user)
        id_user = login.json()["accessToken"]
        response = requests.get(Data.GET_USER_ORDERS_URL, headers={"Authorization": id_user}, data=user)
        assert response.status_code == 200 and '"success": true'
        requests.delete(Data.DELETE_USER_URL, data=user)

    @allure.title('Получение списка заказов не авторизованного пользователя')
    def test_get_not_auth_user_orders(self, generate_reg_data):
        user = generate_reg_data
        requests.post(Data.REGISTER_URL, data=user)
        response = requests.get(Data.GET_USER_ORDERS_URL,data=user)
        assert response.status_code == 401 and '"success": false' and '"message": "You should be authorised"'
        requests.delete(Data.DELETE_USER_URL, data=user)