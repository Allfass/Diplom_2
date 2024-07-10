import allure
import pytest
import requests
from data import TestData



class TestLoginUser():
    
    def test_login_exist_user_return_success(self, registered_user):
        payload = {
            "email": registered_user["email"],
            "password": registered_user['password']
        }
        header = {
            'Authorization': registered_user["accessToken"]
        }
        response = requests.post(TestData.LOGIN_USER, data=payload, headers=header, timeout=10)
        assert response.status_code == 200 and \
               response.json()["success"] == True and \
               response.json()["user"] == {
                   "email":registered_user["email"],
                   "name":registered_user['name']} and \
               response.json()["accessToken"] and \
               response.json()["refreshToken"]
               
    @pytest.mark.parametrize("field",["email", "password"])
    def test_login_exist_user_without_required_field_return_401(self, registered_user, field):
        payload = {
            field: registered_user[field]
        }
        header = {
            'Authorization': registered_user["accessToken"]
        }
        response = requests.post(TestData.LOGIN_USER, data=payload, headers=header, timeout=10)
        assert response.status_code == 401 and \
               response.json() == {
                   "success": False,
                   "message": "email or password are incorrect"
               }
               