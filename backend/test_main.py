from fastapi.testclient import TestClient

from main import *

client = TestClient(app)


def test_get_user():
    response = client.get('/user/id/1')

    assert response.status_code == 200
    assert response.json() == {
        "email": "test@email.com",
        "full_name": "Test User",
        "gender": "Male",
        "password": "(^*^(^%$*(*(*%&%$%$^#@",
        "role": "user"
    }


def test_add_user():
    response = client.post('/create_user', json={



            "email": "something@emal.com",
            "full_name": "Pytest",
            "gender": "other",
            "password": "string",
            "email_verified": False,
            "disabled": True,
            "role": "user",


    })

    assert response.status_code == 200
    assert response.json() == {
        "ser":        {
            "user_id": 24,
            "email": "something@emal.com",
            "full_name": "Pytest",
            "gender": "other",
            "password": "string",
            "email_verified": False,
            "disabled": True,
            "role": "user",
        }


    }
