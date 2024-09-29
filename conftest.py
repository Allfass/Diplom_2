import pytest
from tests.shared.data import TestData
from tests.shared.request import Requests
from faker import Faker


@pytest.fixture
def credentials():
    credentials = {}
    fake = Faker("en_US")
    credentials['email'] = fake.ascii_free_email()
    credentials['password'] = fake.password(length=12)
    credentials['name'] = fake.first_name()
    return credentials

@pytest.fixture
def registered_user(credentials):
    test_request = Requests(
        TestData.CREATE_USER_URL,
        {
            "email": credentials["email"],
            "password": credentials['password'],
            "name": credentials['name']
        }
    )
    responce = test_request.post()
    credentials["accessToken"] = responce.json()["accessToken"]
    credentials["refreshToken"] = responce.json()["refreshToken"]
    return credentials

@pytest.fixture
def logined_user(registered_user):
    test_request = Requests(
        TestData.LOGIN_USER_URL,
        {
            "email": registered_user["email"],
            "password": registered_user['password']
        },
        registered_user["accessToken"]
    )
    response = test_request.post()
    registered_user["accessToken"] = response.json()["accessToken"]
    registered_user["refreshToken"] = response.json()["refreshToken"]
    return registered_user

@pytest.fixture
def order(logined_user):
    test_request = Requests(
        TestData.CREATE_ORDER_URL,
        TestData.CORRECT_INGREDIENT_PAYLOAD,
        logined_user["accessToken"]
    )
    response = test_request.post()
    logined_user["response"] = response.json()
    return logined_user