The Pydantic models needed for the code snippet you have provided would be:

```python
from pydantic import BaseModel, EmailStr, Field

class PasswordResetRequest(BaseModel):
    email: EmailStr = Field(..., description="The email of the user who has forgotten their password")

class PasswordReset(BaseModel):
    password: str = Field(..., description="The new password of the user")
    token: str = Field(..., description="The reset token")
```

Here we have two Pydantic models:

1. `PasswordResetRequest`: This is the request model for the password reset request endpoint. This model expects a valid email.

2. `PasswordReset`: This is the request model for the password reset endpoint. This model expects a new password and a valid reset token.

Additionally, you might want a response model for your endpoints, such as:

```python
class PasswordResetResponse(BaseModel):
    message: str = Field(..., description="The response message")
```

Here, `PasswordResetResponse` would be used to structure the response of both the password reset request and password reset endpoints.

Also, remember to include all necessary imports in your code. For instance, the `Field` class from `pydantic` is used to add metadata to the model fields, and `EmailStr` is a Pydantic type that checks that the field is a valid email address.