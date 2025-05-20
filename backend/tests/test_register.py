Here is how you can write unit tests for the "/register" endpoint using pytest and FastAPI TestClient:

```python
from fastapi.testclient import TestClient
from main import app, UserCreate
import pytest

client = TestClient(app)

@pytest.fixture
def test_user():
    return UserCreate(username="testuser", email="testemail@example.com", password="password123")

# Success cases
def test_create_user(test_user):
    response = client.post("/register", json=test_user.dict())
    assert response.status_code == 201
    assert response.json() == {"username": "testuser", "email": "testemail@example.com"}

# Error cases
def test_create_user_without_username(test_user):
    test_user.username = None
    response = client.post("/register", json=test_user.dict())
    assert response.status_code == 422

def test_create_user_without_password(test_user):
    test_user.password = None
    response = client.post("/register", json=test_user.dict())
    assert response.status_code == 422

# Data validation
def test_create_user_with_invalid_email(test_user):
    test_user.email = "invalidemail"
    response = client.post("/register", json=test_user.dict())
    assert response.status_code == 422

# Edge cases
def test_create_user_with_empty_username(test_user):
    test_user.username = ""
    response = client.post("/register", json=test_user.dict())
    assert response.status_code == 422

def test_create_user_with_empty_password(test_user):
    test_user.password = ""
    response = client.post("/register", json=test_user.dict())
    assert response.status_code == 422

```
In the above tests:

- `test_create_user` tests a successful user creation operation.
- `test_create_user_without_username` and `test_create_user_without_password` test the error cases where a required field is missing.
- `test_create_user_with_invalid_email` tests the data validation logic when an invalid email is provided.
- `test_create_user_with_empty_username` and `test_create_user_with_empty_password` test edge cases where the username and password fields are empty strings.

Remember to replace "main" with the name of your actual Python file containing the FastAPI application.