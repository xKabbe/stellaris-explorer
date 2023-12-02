# Stellaris Explorer

## Getting Started

### Prerequisites

Before you begin, ensure you have the following prerequisites installed:

- [Python 3.11](https://www.python.org/downloads/release/python-3110/) or higher
- [pip](https://pip.pypa.io/en/stable/) (Python package manager)

### Installation

1. Clone the repository to your local machine:

    ```shell
    git clone https://github.com/xKabbe/stellaris-explorer.git
    ```

2. Install the production dependencies:

    ```shell
    pip install -r requirements.txt
    ```

3. Install the development dependencies (for testing, code formatting, etc.):

    ```shell
    pip install -r requirements-dev.txt
    ```

## Usage

Coming soon...

### Unit Testing

[pytest](https://docs.pytest.org/en/7.4.x/) makes it easy to write small, readable tests, and can scale to support complex functional testing for applications and libraries.

| Command                          | Description                                                              |
|----------------------------------|--------------------------------------------------------------------------|
| `pytest`                         | Run all tests in the current directory and its subdirectories.           |
| `pytest test_module.py`          | Run tests in a specific module.                                          |
| `pytest test_module.py::test_fn` | Run a specific test function in a module.                                |
| `pytest -k expression`           | Run tests that match the given keyword expression.                       |
| `pytest -m marker`               | Run tests that have a specific marker.                                   |
| `pytest --fixtures`              | Show available fixtures.                                                 |
| `pytest --cov=your_module`       | Measure code coverage for your module. Requires the `pytest-cov` plugin. |
| `pytest --junitxml=result.xml`   | Generate JUnit-style XML reports.                                        |
| `pytest --html=report.html`      | Generate an interactive HTML report. Requires the `pytest-html` plugin.  |
| `pytest --durations=n`           | Show n slowest test durations.                                           |
| `pytest --markers`               | Show available markers.                                                  |
| `pytest -h`                      | Display help message and exit.                                           |


### MkDocs Documentation

[MkDocs](https://www.mkdocs.org) is a fast, simple, and widely used tool for creating documentation from Markdown files.
To view the project documentation locally and start a live-reloading server, follow these commands:

| Command        | Description                                                                                                                                                                                                                                   |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `mkdocs serve` | This command will start a local development server, and you can access the documentation at http://127.0.0.1:8000/. <br>As you make changes to the documentation files, MkDocs will automatically update the rendered content in your browser |
| `mkdocs build` | This command will build the documentation site                                                                                                                                                                                                |
| `mkdocs -h`    | This command will print the help message and exit                                                                                                                                                                                             |
