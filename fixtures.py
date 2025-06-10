import pytest
from faker import Faker
import random
from main import user_data

base_url = 'http://localhost:8000/users'
fake = Faker('ru')

@pytest.fixture(autouse=True, scope="function")
def clear_user_data():
    user_data.clear()
    yield
    user_data.clear()

@pytest.fixture(scope='session')
def create_valid_user():
    return {
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'age': fake.random_int(min=18, max=99),
        'phone_number': fake.phone_number(),
        'address': fake.address(),
        'email': fake.email()
    }

@pytest.fixture(scope='session')
def create_invalid_user(create_valid_user):
    valid = create_valid_user
    invalid_cases = []

    case1 = valid.copy()
    case1['first_name'] = ''
    invalid_cases.append(case1)

    case2 = valid.copy()
    case2['age'] = fake.random_int(min=-100, max=0),
    invalid_cases.append(case2)


    case3 = valid.copy()
    case3['email'] = 'invalid_email'
    invalid_cases.append(case3)

    case4 = valid.copy()
    case4['phone_number'] = "234"
    invalid_cases.append(case4)

    case5 = valid.copy()
    case5['address'] = ''
    invalid_cases.append(case5)

    return random.choice(invalid_cases)




