To create a secure database to store user information, we will use SQLAlchemy as our ORM (Object-Relational Mapper) and FastAPI's security utilities for password hashing. Here is the complete setup:

1. Database Setup:

```python
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"  # use your own database URL

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
```

2. User Model:

```python
from sqlalchemy import Boolean
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    def verify_password(self, password):
        return pwd_context.verify(password, self.hashed_password)

    def hash_password(self, password):
        self.hashed_password = pwd_context.hash(password)
```

3. Pydantic Models:

```python
from pydantic import BaseModel

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True
```

4. API Endpoints:

```python
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

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

5. Service Layer:

In this case the service layer is implemented within the User model class itself with the `verify_password` and `hash_password` methods.

Note: This code assumes that you have FastAPI, SQLAlchemy, Pydantic, and passlib installed in your environment. This is a very basic setup and does not include proper exception handling, logging, and different environments setup which would be needed for a production application.