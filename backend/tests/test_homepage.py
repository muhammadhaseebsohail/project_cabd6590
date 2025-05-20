```python
# Necessary imports
import pytest
from fastapi.testclient import TestClient
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

# Initialize the FastAPI instance
app = FastAPI(title="Homepage API", description="API to serve homepage data", version="1.0")

# Pydantic model for the response
class HomePageData(BaseModel):
    title: str
    description: Optional[str]
    content: str

# Service layer
def get_homepage_data():
    # This is a mock function. Replace it with actual data retrieval logic.
    return {
        "title": "Welcome to our Homepage!",
        "description": "This is a description of our homepage.",
        "content": "This is the main content of our homepage."
    }

# API endpoint
@app.get("/homepage", response_model=HomePageData)
async def homepage():
    """
    Get Homepage Data

    This endpoint provides data for the homepage. The data includes the title, description, and main content of the homepage.

    - **title**: The title of the homepage.
    - **description**: A brief description of the homepage.
    - **content**: The main content of the homepage.
    """
    data = get_homepage_data()
    if not data:
        raise HTTPException(status_code=404, detail="Homepage data not found")
    return data

# Test client
client = TestClient(app)

def test_get_homepage_data_success():
    response = client.get("/homepage")
    assert response.status_code == 200
    assert response.json() == {
        "title": "Welcome to our Homepage!",
        "description": "This is a description of our homepage.",
        "content": "This is the main content of our homepage."
    }

def test_get_homepage_data_not_found():
    # Mock the get_homepage_data function to return None
    app.dependency_overrides[get_homepage_data] = lambda: None
    response = client.get("/homepage")
    assert response.status_code == 404
    assert response.json() == {"detail": "Homepage data not found"}

def test_get_homepage_data_invalid_response():
    # Mock the get_homepage_data function to return invalid data
    app.dependency_overrides[get_homepage_data] = lambda: {"title": "Welcome to our Homepage!", "description": 123, "content": "This is the main content of our homepage."}
    response = client.get("/homepage")
    assert response.status_code == 422  # Unprocessable Entity

# For edge cases, since the function is a mock, creating edge cases would depend on the nature of the actual function implementation. 
# But this would typically involve testing with unexpected data types, extreme values, etc.
```

This unit test covers success cases, error cases and data validation. The `test_get_homepage_data_success` function tests a successful request. The `test_get_homepage_data_not_found` function tests the case where homepage data is not found. The `test_get_homepage_data_invalid_response` function tests the case where the response data is invalid. The `client` object is an instance of `TestClient` which is used to make requests to the FastAPI application.