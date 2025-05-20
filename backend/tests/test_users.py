To test the FastAPI endpoint, we can use Pytest and FastAPI's TestClient. We will mock the database session to isolate the endpoint from the database layer.

First, install the necessary libraries:

```bash
pip install pytest pytest-mock fastapi[all]
```

Now, let's write the tests:

```python
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from unittest.mock import MagicMock

from main import app, User, UserCreate
import pytest

client = TestClient(app)

@pytest.fixture
def mock_db_session():
    session = Session()
    session.add = MagicMock()
    session.commit = MagicMock()
    session.refresh = MagicMock()
    return session

@pytest.fixture
def test_user():
    return User(id=1, username="testuser", hashed_password="hashedpassword", is_active=True)

def test_create_user_success(mock_db_session, test_user):
    """Test that a user can be created successfully"""
    mock_db_session.add.return_value = None
    mock_db_session.commit.return_value = None
    mock_db_session.refresh.return_value = None

    user_create = UserCreate(username="testuser", password="password")
    response = client.post("/users/", json=user_create.dict(), headers={"content-type": "application/json"})

    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "username": "testuser",
        "is_active": True
    }

def test_create_user_data_validation(mock_db_session):
    """Test that a request with invalid data is rejected"""
    user_create = UserCreate(username="testuser", password="")
    response = client.post("/users/", json=user_create.dict(), headers={"content-type": "application/json"})

    assert response.status_code == 422  # Unprocessable Entity
    assert "password" in response.json()["detail"][0]["loc"]

def test_create_user_edge_case(mock_db_session, test_user):
    """Test that a request with a username that already exists is rejected"""
    mock_db_session.query.return_value.filter_by.return_value.first.return_value = test_user

    user_create = UserCreate(username="testuser", password="password")
    response = client.post("/users/", json=user_create.dict(), headers={"content-type": "application/json"})

    assert response.status_code == 400  # Bad Request
    assert "User already exists" in response.json()["detail"]
```

Note that these tests are based on the assumption that the application checks for existing users before creating a new user, and that it returns a 400 Bad Request response with a "User already exists" message in the details when a user with the given username already exists. If your application does not do this, you will need to adjust the tests accordingly.