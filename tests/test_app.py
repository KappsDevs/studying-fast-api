from http import HTTPStatus


def test_read_root(client):
    # Arrange

    response = client.get("/")  # Act

    assert response.status_code == HTTPStatus.OK  # 200
    assert response.json() == {"message": "Olar mundooo"}


def test_create_user(client):
    response = client.post(  # validar o userpublic
        "/user/",
        json={
            "username": "johndoe",
            "email": "aaa@aaa.com",
            "password": "123456",
        },
    )

    assert response.status_code == HTTPStatus.CREATED  # 200
    assert response.json() == {
        "id": 1,
        "username": "johndoe",
        "email": "aaa@aaa.com",
    }


def test_read_users(client):
    response = client.get("/user/")

    assert response.status_code == HTTPStatus.OK
    assert response.json == {
        "users": [{"email": "aaa@aaa.com", "id": 1, "username": "johndoe"}]
    }


def test_update_user(client):
    response = client.put(
        "/user/1",
        json={
            "id": 1,
            "username": "johndoe",
            "email": "aaa@aaa.com",
        },
    )

    assert response.json == {
        "id": 1,
        "username": "johndoe",
        "email": "aaa@aaa.com",
    }

def test_delete(client):
    response = client.delete("/user/1")

    assert response.json() == {'message': 'User deleted'}