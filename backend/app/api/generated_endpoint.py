The task you're requesting does not involve creating an API endpoint, but rather the setup of a Continuous Integration/Continuous Deployment (CI/CD) process for a backend application built with FastAPI, as well as the proper handling of environment variables.

While I can't directly provide you with the complete code for this task, because it largely depends on the infrastructure and services you're using (like GitHub Actions, GitLab CI/CD, Jenkins, or others for the CI/CD setup; and local machine, Docker, or cloud services for environment variables), I can guide you on the general steps you need to follow.

1. **CI/CD setup:**

   - Create a `.yml` or `.yaml` file in your repository's root in a directory named `.github/workflows` if you are using GitHub Actions. If you're using GitLab, the file should be named `.gitlab-ci.yml` and be placed in the root of your repository. For Jenkins, you would use a `Jenkinsfile`. Here's a simple example for GitHub Actions:

```yaml
name: Python application

on:
  push:
    branches: [ main ]

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python 3.8
      uses: actions/setup-python@v2
      with:
        python-version: 3.8
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Run tests
      run: |
        pytest
```
This simple pipeline runs whenever you push to the main branch. It sets up Python 3.8, installs the dependencies from your `requirements.txt` file, and then runs all your tests using pytest.

2. **Proper Environment Variables:**

   - You should never hard code sensitive information like passwords, API keys or any configuration variable that might change between deployment environments. Instead, use environment variables. In FastAPI, you can use the `python-dotenv` package to load these variables from a `.env` file. 

```python
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.
```

You can then access these variables with `os.getenv('VAR_NAME')`. When deploying, make sure to set these environment variables on your server or in your CI/CD pipeline.

Remember that the `.env` file should not be committed to your repository. Instead, include an `.env.example` file that includes all the necessary environment variables to run the application without the actual values.