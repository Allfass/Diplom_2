import allure
import pytest
import requests
from data import TestData



class TestCreateUser():
    @allure.title('Проверка регистрации нового пользователя')
    @allure.description('При регистрации нового пользователя, вернутся пользовательские данные и код 200')
    def test_create_unique_user_return_success(self, credentials):

        payload = {
            "email": credentials["email"],
            "password": credentials['password'],
            "name": credentials['name']
        }
        response = requests.post(TestData.CREATE_USER, data=payload, timeout=10)
        assert response.status_code == 200 and \
               response.json()["success"] == True and \
               response.json()["user"] == {
                   "email":credentials["email"],
                   "name":credentials['name']} and \
               response.json()["accessToken"] and \
               response.json()["refreshToken"]

    @allure.title('Проверка регистрации уже существующего пользователя')
    @allure.description('При регистрации уже существующего пользователя, вернётся ошибка и код 403')
    def test_create_user_that_already_exist_return_403(self, credentials):

        payload = {
            "email": credentials["email"],
            "password": credentials['password'],
            "name": credentials['name']
        }
        response = requests.post(TestData.CREATE_USER, data=payload, timeout=10)
        response = requests.post(TestData.CREATE_USER, data=payload, timeout=10)
        assert response.status_code == 403 and \
               response.json() == {
                   "success": False,
                   "message": "User already exists"
               }

    @allure.title('Проверка регистрации нового пользователя без обязательного поля')
    @allure.description('При регистрации нового пользователя без обязательного поля, вернётся ошибка и код 403')
    @pytest.mark.parametrize("payload", TestData.REQUIRED_REGISTRATION_FIELD_SUITES)           
    def test_create_user_without_required_field_return_403(self, payload):

        response = requests.post(TestData.CREATE_USER, data=payload, timeout=10)
        assert response.status_code == 403 and \
               response.json() == {
                   "success": False,
                   "message": "Email, password and name are required fields"
               }
