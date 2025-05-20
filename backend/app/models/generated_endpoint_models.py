The task does not correspond to the request of creating an API endpoint with FastAPI and Pydantic models. The context given is about setting up a CI/CD process and managing environment variables for a FastAPI application.

However, to answer your request, let's imagine an endpoint for creating a user. Here's how you would define the FastAPI endpoint, the Pydantic models, and a service layer.

1. **Pydantic Models:**
```python
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: EmailStr
    name: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    class Config:
        orm_mode = True
```

Here we have three models:
- `UserBase` which includes the common attributes
- `UserCreate` which is used when creating a new user and includes a password
- `User` which is used for reading and includes the user id

2. **Service Layer:**
```python
from sqlalchemy.orm import Session
from . import models, schemas

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
```
Here we have two service functions:
- `get_user` which retrieves a user by id
- `create_user` which creates a new user

3. **FastAPI Endpoints:**
```python
from typing import List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, services
from .database import SessionLocal, engine

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = services.get_user(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return services.create_user(db=db, user=user)
```
We have a single endpoint `/users/` that accepts a POST request. It uses a Pydantic model to parse and validate the request body, communicates with the database to create the user and returns the new user data.