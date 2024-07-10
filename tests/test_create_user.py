import allure
import pytest
import requests
from data import TestData



class TestCreateUser():
    
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
               
    @pytest.mark.parametrize("payload", TestData.REQUIRED_REGISTRATION_FIELD_SUITES)           
    def test_create_user_without_required_field_return_403(self, payload):

        response = requests.post(TestData.CREATE_USER, data=payload, timeout=10)
        assert response.status_code == 403 and \
               response.json() == {
                   "success": False,
                   "message": "Email, password and name are required fields"
               }
