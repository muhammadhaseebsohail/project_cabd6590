Sure, here are some unit tests for the FastAPI endpoints:

```python
import pytest
from fastapi.testclient import TestClient
from main import app, User, PasswordResetRequest, PasswordReset

client = TestClient(app)

def test_password_reset_request_success():
    response = client.post(
        "/password-reset/request",
        json={"email": "user@example.com"},
    )
    assert response.status_code == 202
    assert response.json() == {"message": "Password reset email sent."}

def test_password_reset_request_no_email():
    response = client.post(
        "/password-reset/request",
        json={},
    )
    assert response.status_code == 422
    assert "email" in response.text

def test_password_reset_request_invalid_email():
    response = client.post(
        "/password-reset/request",
        json={"email": "invalid"},
    )
    assert response.status_code == 422
    assert "email" in response.text

def test_password_reset_confirm_success():
    response = client.post(
        "/password-reset/confirm",
        json={"password": "newPassword", "token": "validToken"},
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Password reset successfully."}

def test_password_reset_confirm_no_password():
    response = client.post(
        "/password-reset/confirm",
        json={"token": "validToken"},
    )
    assert response.status_code == 422
    assert "password" in response.text

def test_password_reset_confirm_no_token():
    response = client.post(
        "/password-reset/confirm",
        json={"password": "newPassword"},
    )
    assert response.status_code == 422
    assert "token" in response.text

def test_password_reset_confirm_invalid_token():
    response = client.post(
        "/password-reset/confirm",
        json={"password": "newPassword", "token": "invalidToken"},
    )
    assert response.status_code == 400
    assert "Invalid or expired password reset token." in response.text
```

In these tests, we are using the `TestClient` from FastAPI to send requests to our endpoints and make assertions based on the responses. We are testing for both success and error cases, as well as data validation.

Note: These tests assume that the `generate_reset_token`, `send_reset_email`, `verify_reset_token`, and `update_password` functions in the service layer return predictable results for the given inputs. In a real-world scenario, these functions would likely interact with a database or an email service, and you would need to use mocking to isolate your tests from these external dependencies.