import pytest
from faker import Faker


@pytest.fixture
def credentials():
    credentials = {}
    fake = Faker("en_US")
    credentials['email'] = fake.ascii_free_email()
    credentials['password'] = fake.password(length=12)
    credentials['name'] = fake.first_name()
    return credentials