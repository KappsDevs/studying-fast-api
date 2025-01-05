from http import HTTPStatus
from fastapi.testclient import TestClient
from src.app import app


def test_read_root():
    client = TestClient(app) #Arrange

    response = client.get('/') #Act

    assert response.status_code == HTTPStatus.OK #200
    assert response.json() == {"message": "Olar mundooo"}