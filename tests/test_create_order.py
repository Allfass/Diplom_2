import allure
import pytest
import requests
from data import TestData



class TestCreateOrder():
    
    @pytest.mark.parametrize("rool,sauce,filling", TestData.INGREDIENTS_SUITES)
    def test_create_order_with_3_ingredients_return_success(self, logined_user, rool, sauce, filling):
        payload = {
            "ingredients": [
                rool,
                sauce,
                filling]
        }
        header = {
            'Authorization': logined_user["accessToken"]
        }
        response = requests.post(TestData.LOGIN_USER, data=payload, headers=header, timeout=10)