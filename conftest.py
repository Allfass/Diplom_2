import pytest
import requests
from data import TestData
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
    payload = {
            "email": credentials["email"],
            "password": credentials['password'],
            "name": credentials['name']
        }
    responce = requests.post(TestData.CREATE_USER, data=payload, timeout=10)
    credentials["accessToken"] = responce.json()["accessToken"]
    credentials["refreshToken"] = responce.json()["refreshToken"]
    return credentials

@pytest.fixture
def logined_user(registered_user):
    payload = {
            "email": registered_user["email"],
            "password": registered_user['password']
        }
    header = {
            'Authorization': registered_user["accessToken"]
        }
    response = requests.post(TestData.LOGIN_USER, data=payload, headers=header, timeout=10)
    registered_user["accessToken"] = response.json()["accessToken"]
    registered_user["refreshToken"] = response.json()["refreshToken"]
    return registered_user

@pytest.fixture
def order(logined_user):
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
    logined_user["response"] = response.json()
    return logined_user