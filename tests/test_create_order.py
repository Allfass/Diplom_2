import allure
import pytest
import requests
from data import TestData
from helper import TestHelper


class TestCreateOrder():
    
    def test_create_order_with_authorization_return_order(self, logined_user):
        payload = {
            "ingredients": [
                "61c0c5a71d1f82001bdaaa6d",
                "61c0c5a71d1f82001bdaaa73",
                "61c0c5a71d1f82001bdaaa77"]
        }
        header = {
            'Authorization': logined_user["accessToken"]
        }
        response = requests.post(TestData.CREATE_ORDER, headers=header, data=payload, timeout=10)
        expected = TestHelper.replace_fields_for_creating_order_test(TestData.EXPECTED_THREE_INGREDIENTS_SUITES[0], response, logined_user)
        assert response.status_code == 200 and\
               response.json() == expected
               
    def test_create_order_without_authorization_return_error(self):
        payload = {
            "ingredients": [
                "61c0c5a71d1f82001bdaaa6d",
                "61c0c5a71d1f82001bdaaa73",
                "61c0c5a71d1f82001bdaaa77"]
        }
        response = requests.post(TestData.CREATE_ORDER, data=payload, timeout=10)
        assert response.status_code == 200 and\
               response.json() == {
                    "success": True,
                    "name": "Фалленианский space флюоресцентный бургер",
                    "order": {
                        "number": response.json()["order"]["number"]
                    }
               }
    
    @pytest.mark.parametrize("rool,sauce,filling, expected", TestData.INGREDIENTS_HASH_AND_EXPECT_SUITES)
    def test_create_order_with_3_ingredients_return_success(self, logined_user, rool, sauce, filling, expected):
        payload = {
            "ingredients": [
                rool,
                sauce,
                filling]
        }
        header = {
            'Authorization': logined_user["accessToken"]
        }
        response = requests.post(TestData.CREATE_ORDER, headers=header, data=payload, timeout=10)
        expected = TestHelper.replace_fields_for_creating_order_test(expected, response, logined_user)
        
        assert response.status_code == 200 and\
               response.json() == expected
               
    def test_create_order_without_ingredients_return_400(self, logined_user):
        payload = {
            "ingredients": []
        }
        header = {
            'Authorization': logined_user["accessToken"]
        }
        response = requests.post(TestData.CREATE_ORDER, headers=header, data=payload, timeout=10)
        
        assert response.status_code == 400 and \
               response.json() == {
                   "success": False,
                   "message": "Ingredient ids must be provided"
               }
               
    def test_create_order_with_wrong_hash_ingredients_return_400(self, logined_user):
        payload = {
            "ingredients": [
                "61c0c5a71d1f82001bdaa111",
                "61c0c5a71d1f82001bdaa222",
                "61c0c5a71d1f82001bdaa333"]
        }
        header = {
            'Authorization': logined_user["accessToken"]
        }
        response = requests.post(TestData.CREATE_ORDER, headers=header, data=payload, timeout=10)
        
        assert response.status_code == 400 and \
               response.json() == {
                   "success": False,
                   "message": "One or more ids provided are incorrect"
               }
               
    def test_get_order_without_authorization_return_error(self):
        response = requests.get(TestData.CREATE_ORDER, timeout=10)
        assert response.status_code == 401 and \
            response.json() == {
                "success": False,
                "message": "You should be authorised"
            }
            
    def test_get_order_return_order(self, order):
        header = {
            'Authorization': order["accessToken"]
        }
        response = requests.get(TestData.CREATE_ORDER, headers=header, timeout=10)
        assert response.status_code == 200 and \
            response.json() == {
                "success": True,
                "orders": [
                    {
                        "_id": order["response"]["order"]["_id"],
                        "ingredients": [
                                order["response"]["order"]["ingredients"][0]["_id"],
                                order["response"]["order"]["ingredients"][1]["_id"],
                                order["response"]["order"]["ingredients"][2]["_id"]
                            ],
                        "status": "done",
                        "name": order["response"]["name"],
                        "createdAt": order["response"]["order"]["createdAt"],
                        "updatedAt": order["response"]["order"]["updatedAt"],
                        "number": order["response"]["order"]["number"]
                    }
                ],
                "total": response.json()["total"],
                "totalToday": response.json()["totalToday"]
            }