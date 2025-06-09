import pytest
import requests
from fixtures import *
from main import *

base_url = 'http://localhost:8000/users'


def test_add_valid_user(create_valid_user):
    response = requests.post(base_url, json=create_valid_user)
    assert response.status_code == 200
    assert response.json()['status'] == 'Пользователь добавлен'
    assert create_valid_user in user_data


def test_add_invalid_user(create_invalid_user):
    with pytest.raises(ValueError):
        response = requests.post(base_url, json=create_invalid_user)
        assert response.status_code == 400


def test_get_all_users(create_valid_user):
    requests.post(base_url, json=create_valid_user)
    response = requests.get(base_url)
    assert response.status_code == 200
    data = response.json()
    assert any(i['first_name'] == create_valid_user['first_name'] for i in data)


def test_find_by_first_name(create_valid_user):
    requests.post(base_url, json=create_valid_user)

    name = create_valid_user['first_name']
    response = requests.get(f'{base_url}/name/{name}')
    assert response.status_code == 200
    data = response.json()

    assert 'data' in data
    assert data['data'][0]['first_name'] == name


def test_find_by_city(create_valid_user):
    requests.post(base_url, json=create_valid_user)

    city = create_valid_user['city']
    response = requests.get(f'{base_url}/city/{city}')
    assert response.status_code == 200
    data = response.json()

    assert 'data' in data
    assert data['data'][0]['city'] == city

