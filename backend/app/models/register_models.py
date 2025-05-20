The Pydantic models are already defined in the provided code. Here they are for clarity:

```python
from typing import Optional
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    """
    User Base model
    """
    email: Optional[EmailStr] = None
    username: str

class UserCreate(UserBase):
    """
    User Creation model
    """
    password: str
```

`UserBase` is a Pydantic model that includes the base properties for a User: `username` and an optional `email`.

`UserCreate` extends `UserBase` by adding a `password` field. This model is used when creating a new User.

These models are used in the API endpoint for user registration:

- The `UserCreate` model is used as the input model for the `/register` POST request. It validates the incoming data, ensuring that it contains a `username`, `email` (which can be optional), and a `password`.
- The `UserBase` model is used as the output model for the same `/register` POST request. This model ensures that the returned data contains the `username` and `email`.

Here is how these models are used in the endpoint:

```python
@app.post("/register", response_model=UserBase, status_code=201)
async def create_user(user: UserCreate):
    """
    Create a new user
    """
    password_hash = pwd_context.hash(user.password)
    # Here you would save the user to your database. 
    # As this is just an example, we'll skip that step.
    return UserBase(username=user.username, email=user.email)
```

In this function, `user: UserCreate` uses Pydantic to validate the incoming JSON request data, creating a new `UserCreate` object if the data is valid. The function then hashes the password, and returns a new `UserBase` object containing the username and email. The `response_model=UserBase` in the decorator ensures that the returned data matches the `UserBase` model.