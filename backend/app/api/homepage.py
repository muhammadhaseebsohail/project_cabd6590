```python
# Necessary imports
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
```

In the above code, we created a FastAPI instance and an endpoint `/homepage` which returns homepage data. We have used Pydantic's `BaseModel` to define how our response data should look like. The `get_homepage_data` function is a mock function. Replace it with the logic for retrieving actual data.

We have added error handling to raise an HTTP 404 error if the homepage data is not found. We have also added a docstring for OpenAPI documentation. The endpoint follows RESTful principles and does not require authentication/authorization as it is a public endpoint. The code is clean, modular, and follows FastAPI best practices.