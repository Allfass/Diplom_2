import allure
import pytest
from tests.shared.request import Requests
from tests.shared.data import TestData



class TestLoginUser():
    @allure.title('Проверка авторизации зарегистрированного пользователя')
    @allure.description('При авторизации зарегистрированного пользователя, вернутся пользовательские данные и код 200')
    def test_login_exist_user_return_success(self, registered_user):
        test_request = Requests(
            TestData.LOGIN_USER_URL,
            {
                "email": registered_user["email"],
                "password": registered_user['password']
            },
            registered_user["accessToken"]
        )
        response = test_request.post()
        assert response.status_code == 200 and \
               response.json()["success"] == True and \
               response.json()["user"] == {
                   "email":registered_user["email"],
                   "name":registered_user['name']} and \
               response.json()["accessToken"] and \
               response.json()["refreshToken"]

    @allure.title('Проверка авторизации зарегистрированного пользователя без обязательного поля')
    @allure.description('При авторизации зарегистрированного пользователя без обязательного поля, вернётся ошибка и код 401')
    @pytest.mark.parametrize("field",["email", "password"])
    def test_login_exist_user_without_required_field_return_401(self, registered_user, field):
        test_request = Requests(
            TestData.LOGIN_USER_URL,
            {
                field: registered_user[field]
            },
            registered_user["accessToken"]
        )
        response = test_request.post()
        assert response.status_code == 401 and \
               response.json() == {
                   "success": False,
                   "message": "email or password are incorrect"
               }
               