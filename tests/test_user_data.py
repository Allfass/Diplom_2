import allure
import pytest
from tests.shared.request import Requests
from tests.shared.data import TestData



class TestUserData():
    @allure.title('Проверка обновления данных пользователя')
    @allure.description('При обновлении данных пользователя, вернутся данные пользователя и код 200')
    @pytest.mark.parametrize("field, second_field",[
            ("email", "name"),
            ("name", "email")
        ])
    def test_update_user_data_with_auth_token_return_success(self, registered_user, field, second_field):
        test_request = Requests(
            TestData.USER_DATA_URL,
            {
                field: f"01{registered_user[field]}"
            },
            registered_user["accessToken"]
        )
        response = test_request.patch()
        assert response.status_code == 200 and \
               response.json() == {
                   "success": True,
                   "user": {
                       field: f"01{registered_user[field]}",
                       second_field:registered_user[second_field]
                   }
               }

    @allure.title('Проверка обновления данных пользователя без авторизации')
    @allure.description('При обновлении данных пользователя без авторизации, вернётся ошибка и код 401')
    @pytest.mark.parametrize("field",["email", "name"])           
    def test_update_user_data_without_auth_token_return_401(self, registered_user, field):
        test_request = Requests(
            TestData.USER_DATA_URL,
            {
                field: f"01{registered_user[field]}"
            })
        response = test_request.patch()
        assert response.status_code == 401 and \
               response.json() == {
                   "success": False,
                   "message": "You should be authorised"
               }
