First off, let's create a Pydantic model for User and LoginPayload. The User model has two fields: username and password. The LoginPayload model has the same fields which will be used for login purposes.

```python
from pydantic import BaseModel, Field

class User(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    password: str = Field(..., min_length=5)

class LoginPayload(BaseModel):
    username: str
    password: str
```

Next, we need to create a helper function to authenticate users and generate JWT tokens.

```python
import jwt
from typing import Optional
from fastapi import HTTPException, status
from passlib.context import CryptContext

SECRET_KEY = "YOUR_SECRET_KEY"
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def authenticate_user(fake_db, username: str, password: str):
    user = fake_db.get(username)
    if not user:
        return False
    if not pwd_context.verify(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict):
    to_encode = data.copy()
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)
    return encoded_jwt
```

Now, let's create our login API endpoint.

```python
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.post("/token", response_model=Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    user = authenticate_user(fake_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
```

In this endpoint, we are getting form data using OAuth2PasswordRequestForm. We then authenticate the user using our helper function. If the user is not authenticated, we raise an HTTPException with a status code of 401. Otherwise, we create an access token and return it in a JSON response.

Please note that "fake_db" is a placeholder for your actual database or data source where you would verify the user details. Similarly, you should replace "YOUR_SECRET_KEY" with your actual secret key.