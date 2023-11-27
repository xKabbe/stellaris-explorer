# Contributing to Stellaris Explorer

Thank you for considering contributing to Stellaris Explorer! Follow the guidelines below to contribute effectively.

## How to Contribute

1. Fork the repository.
2. Clone your fork:
   ```bash
   git clone https://github.com/your-username/stellaris-explorer.git
3. Create a new branch for your contribution:
   ```bash
   git checkout -b feature-or-fix-name
4. Make your changes and commit:
   ```bash
   git add .
   git commit -m "Description of your changes"
5. Push your changes to your fork:
   ```bash
   git push origin feature-or-fix-name
6. Create a pull request (PR) on the main repository.

## File Header

Please ensure that each Python file in the project has a consistent file header.
The header should include the following information:

```python
"""
File: file name
Author: name
Description: ...

For more information, see: https://github.com/xKabbe/stellaris-explorer
"""
```

Replace `file name` with the actual name of the file, and `name` with your name.
Provide a brief description of the file's purpose in the `Description` section.

## Code Style

Follow [PEP 8](https://peps.python.org/pep-0008/) style guidelines for Python code.

## Testing

Ensure that your changes include appropriate tests. Run the existing tests using:

```bash
pytest
```

If you add new functionality, please add corresponding tests.
