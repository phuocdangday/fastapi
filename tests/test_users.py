from fastapi import status
from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_create_user():
    body = {
        'name': 'test create user'
    }
    response = client.post('/users', json=body)
    assert response.status_code == status.HTTP_201_CREATED


def test_get_user():
    response = client.get('/users/1')
    assert response.status_code == status.HTTP_200_OK


def test_get_user_not_exists():
    response = client.get('/users/2')
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_get_all_user():
    response = client.get('/users')
    assert response.status_code == status.HTTP_200_OK


def test_update_user():
    body = {
        'name': 'test update user'
    }
    response = client.put('/users/1', json=body)
    assert response.status_code == status.HTTP_200_OK


def test_update_user_not_exists():
    body = {
        'name': 'test update user not exists'
    }
    response = client.put('/users/2', json=body)
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_delete_user():
    response = client.delete('/users/1')
    assert response.status_code == status.HTTP_200_OK


def test_delete_user_not_exists():
    response = client.delete('/users/2')
    assert response.status_code == status.HTTP_404_NOT_FOUND
