import pytest
import requests
from fixtures import *
from main import *

base_url = 'http://localhost:8000/users'


def test_add_valid_user(create_valid_user):
    response = requests.post(base_url, json=create_valid_user)
    print("Status code:", response.status_code)
    assert response.status_code == 200
    assert response.json()['status'] == 'Пользователь добавлен'


def test_add_invalid_user(create_invalid_user):
    response = requests.post(base_url, json=create_invalid_user)
    assert response.status_code == 400
    assert 'detail' in response.json()


def test_get_all_users(create_valid_user):
    print("create_valid_user:", create_valid_user)
    response_post = requests.post(base_url, json=create_valid_user)
    print("Status code:", response_post.status_code)

    assert response_post.status_code == 200

    response_get = requests.get(base_url)
    print("Response JSON:", response_get.json())
    print("create_valid_user:", create_valid_user)

    assert response_get.status_code == 200
    data = response_get.json()

    assert any(u['first_name'] == create_valid_user['first_name'] for u in data)


def test_find_by_first_name(create_valid_user):
    requests.post(base_url, json=create_valid_user)

    name = create_valid_user['first_name']
    response = requests.get(f'{base_url}/first_name/{name}')
    assert response.status_code == 200
    data = response.json()

    assert 'data' in data
    assert data['data'][0]['first_name'] == name


def test_find_by_address(create_valid_user):
    requests.post(base_url, json=create_valid_user)

    address = create_valid_user['address']
    response = requests.get(f'{base_url}/address/{address}')
    assert response.status_code == 200
    data = response.json()

    assert 'data' in data
    assert data['data'][0]['address'] == address

