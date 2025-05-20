First, let's create a Pydantic model for the token response.

```python
from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str
```

Now, the unit test code for the endpoint can be as follows:

```python
from fastapi.testclient import TestClient
import pytest
from main import app, User, authenticate_user, create_access_token

client = TestClient(app)

def test_login_success():
    response = client.post(
        "/token",
        data={
            "username": "testuser",
            "password": "testpass"
        }
    )
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"

def test_login_incorrect_password():
    response = client.post(
        "/token",
        data={
            "username": "testuser",
            "password": "wrongpass"
        }
    )
    assert response.status_code == 401
    assert response.json() == {"detail": "Incorrect username or password"}

def test_login_nonexistent_user():
    response = client.post(
        "/token",
        data={
            "username": "nonexistent",
            "password": "testpass"
        }
    )
    assert response.status_code == 401
    assert response.json() == {"detail": "Incorrect username or password"}

def test_login_validation():
    response = client.post(
        "/token",
        data={
            "username": "te",
            "password": "pa"
        }
    )
    assert response.status_code == 422  # Unprocessable Entity

def test_login_edge_case():
    response = client.post(
        "/token",
        data={
            "username": "testuser"*10,
            "password": "testpass"
        }
    )
    assert response.status_code == 422  # Unprocessable Entity
    assert "value_error.str" in response.json()["detail"][0]["type"]
```

In these tests, we are covering various cases:
- The login_success test checks a valid login.
- The login_incorrect_password and login_nonexistent_user tests check for incorrect credentials.
- The login_validation test checks Pydantic validation.
- The login_edge_case test checks for a username that exceeds the maximum length. 

Make sure to replace the "testuser" and "testpass" values with valid test data for your database in the login_success test.

Note that these tests require a running instance of your database as the `authenticate_user` function is trying to fetch users from it. If you want to avoid this, you could mock the `authenticate_user` function to simulate its behavior without hitting the database.