# Testing

Testing is an essential part of ensuring the reliability and correctness of your project.
This document provides an overview of the testing structure and tools used in this project.

## Unit Testing

### Frontend

Frontend unit testing is crucial for validating the behavior of your [Dash](https://plotly.com/dash/) web application's user interface.
In this project, we leverage `pytest` along with `dash.testing` to streamline the testing process.

#### pytest

[pytest](https://docs.pytest.org/en/stable/) is a popular testing framework for Python that makes it easy to write simple unit tests and scalable functional tests.
It provides numerous features for efficient test discovery, test fixtures, and test parameterization.

#### dash.testing

[dash.testing](https://dash.plotly.com/testing) is a module within the Dash framework that facilitates testing Dash applications.
It provides tools like `DashComposite` and `DashDuo` for testing the frontend behavior of Dash apps.

To run frontend unit tests, execute the following command in your project's root directory:

```bash
pytest tests/test_app/test_frontend
```

or with full coverage reports:

```bash
pytest tests/test_app/test_frontend --cov=app/frontend --cov-report=html:coverage/frontend --template=html1/index.html --report=coverage/frontend/frontend-coverage-report.html --headless
```

### Backend

#### pytest

[pytest](https://docs.pytest.org/en/stable/) is used for backend unit testing as well.
It offers a flexible and easy-to-use framework for writing comprehensive backend tests.

To run backend unit tests, execute the following command in your project's root directory:

```bash
pytest tests/test_app/test_backend
```

or with full coverage reports:

```bash
pytest tests/test_app/test_backend --cov=app/backend --cov-report=html:coverage/backend --template=html1/index.html --report=coverage/backend/backend-coverage-report.html
```

## Integration Testing

In addition to unit tests, integration testing ensures that different components of your application work together seamlessly.
It involves testing interactions between frontend and backend components.

To run integration tests, execute the following command in your project's root directory:

```bash
pytest tests/test_integration
```

or with full coverage reports:

```bash
pytest tests/test_integration --template=html1/index.html --report=coverage/integration/integration-coverage-report.html
```

Feel free to explore the individual test files to gain insights into specific test cases and scenarios.

If you have any questions or need assistance with testing, refer to the project's documentation or reach out to me.

