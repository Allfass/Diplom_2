import allure
import pytest
from tests.shared.request import TestRequests
from tests.shared.data import TestData
from tests.shared.helper import TestHelper


class TestCreateOrder():
    @allure.title('Проверка создания заказа')
    @allure.description('При создании заказа, вернётся состав заказа и код 200')
    def test_create_order_with_authorization_return_order(self, logined_user):
        test_request = TestRequests(
            TestData.CREATE_ORDER_URL, 
            TestData.CORRECT_INGREDIENT_PAYLOAD, 
            logined_user["accessToken"])
        response = test_request.post()
        expected = TestHelper.replace_fields_for_creating_order_test(
            TestData.EXPECTED_THREE_INGREDIENTS_SUITES[0], 
            response, 
            logined_user
        )
        assert response.status_code == 200 and\
               response.json() == expected

    @allure.title('Проверка создания заказа без авторизации')
    @allure.description('При создании заказа без авторизации, вернётся ошибка')
    def test_create_order_without_authorization_return_error(self):
        test_request = TestRequests(
            TestData.CREATE_ORDER_URL, 
            TestData.CORRECT_INGREDIENT_PAYLOAD)
        response = test_request.post()
        assert response.status_code == 200 and\
               response.json() == {
                    "success": True,
                    "name": "Фалленианский space флюоресцентный бургер",
                    "order": {
                        "number": response.json()["order"]["number"]
                    }
               }

    @allure.title('Проверка создания заказа с тремя ингредиентами')
    @allure.description('При создании заказа с тремя ингредиентами, вернётся состав заказа и код 200')
    @pytest.mark.parametrize("rool,sauce,filling, expected", TestData.INGREDIENTS_HASH_AND_EXPECT_SUITES)
    def test_create_order_with_3_ingredients_return_success(self, logined_user, rool, sauce, filling, expected):
        test_request = TestRequests(
            TestData.CREATE_ORDER_URL, 
            {
                "ingredients": [
                    rool,
                    sauce,
                    filling]
            }, 
            logined_user["accessToken"])
        response = test_request.post()
        expected = TestHelper.replace_fields_for_creating_order_test(expected, response, logined_user)
        assert response.status_code == 200 and\
               response.json() == expected

    @allure.title('Проверка создания заказа без ингредиентов')
    @allure.description('При создании заказа без ингредиентов, вернётся ошибка  и код 400')
    def test_create_order_without_ingredients_return_400(self, logined_user):
        test_request = TestRequests(
            TestData.CREATE_ORDER_URL, 
            {
                "ingredients": []
            }, 
            logined_user["accessToken"])
        response = test_request.post()
        assert response.status_code == 400 and \
               response.json() == {
                   "success": False,
                   "message": "Ingredient ids must be provided"
               }

    @allure.title('Проверка создания заказа с неправильным хэшем ингредиентов')
    @allure.description('При создании заказа с неправильным хэшем ингредиентов, вернётся ошибка  и код 400')
    def test_create_order_with_wrong_hash_ingredients_return_400(self, logined_user):
        test_request = TestRequests(
            TestData.CREATE_ORDER_URL,
            TestData.WRONG_INGREDIENT_HASH,
            logined_user["accessToken"])
        response = test_request.post()
        assert response.status_code == 400 and \
               response.json() == {
                   "success": False,
                   "message": "One or more ids provided are incorrect"
               }

    @allure.title('Проверка получения заказа без авторизации')
    @allure.description('При получении заказа без авторизации, вернётся ошибка  и код 401')
    def test_get_order_without_authorization_return_error(self):
        test_request = TestRequests(
            TestData.CREATE_ORDER_URL, 
            TestData.WRONG_INGREDIENT_HASH)
        response = test_request.get()
        assert response.status_code == 401 and \
            response.json() == {
                "success": False,
                "message": "You should be authorised"
            }

    @allure.title('Проверка получения заказа')
    @allure.description('При получении заказа, вернётся состав заказа  и код 200')
    def test_get_order_return_order(self, order):
        test_request = TestRequests(
            TestData.CREATE_ORDER_URL, 
            "",
            order["accessToken"])
        response = test_request.get_empty_body()
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