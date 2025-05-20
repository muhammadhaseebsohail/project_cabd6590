The Pydantic models are already included in the provided code. They are used to validate the data sent to the API. Here they are again with their import statements:

```python
from pydantic import BaseModel

class UserBase(BaseModel):
    """
    This is the base User model which other User models will inherit from.
    It includes the username field which is required for all User models.
    """
    username: str

class UserCreate(UserBase):
    """
    This is the User model for creating a new user.
    It inherits from the base User model and includes the password field which is required for creating a new user.
    """
    password: str

class User(UserBase):
    """
    This is the User model for reading users from the database.
    It inherits from the base User model and includes the id and is_active fields which are not required when creating a new user but are included when reading a user from the database.
    """
    id: int
    is_active: bool

    class Config:
        orm_mode = True
```

These models are used in the endpoint for creating a new user. The UserCreate model is used as the request model and the User model is used as the response model:

```python
@app.post("/users/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    Create a new user
    """
    db_user = User(username=user.username)
    db_user.hash_password(user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
```

In this endpoint, FastAPI automatically validates the request data against the UserCreate model and returns an error if the data is not valid. After the new user is created in the database, the data is validated against the User model before it is returned in the response.