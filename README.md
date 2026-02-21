# SimplePrj

![CI](https://github.com/ggc4295/SimplePrj/actions/workflows/ci.yml/badge.svg)

A simple Python project for testing GitHub CI/CD functionality.

## Features

- Simple calculator module with basic math operations
- Unit tests with pytest
- GitHub Actions CI pipeline
- Code linting with flake8
- Code formatting check with black

## Project Structure

```
SimplePrj/
├── .github/
│   └── workflows/
│       └── ci.yml          # GitHub Actions CI workflow
├── src/
│   ├── __init__.py
│   ├── calculator.py       # Calculator module
│   └── utils.py            # Utility functions
├── tests/
│   ├── __init__.py
│   ├── test_calculator.py  # Calculator tests
│   └── test_utils.py       # Utility tests
├── .gitignore
├── requirements.txt
├── setup.py
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.9+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/<your-username>/SimplePrj.git
cd SimplePrj

# Install dependencies
pip install -r requirements.txt

# Install the package in development mode
pip install -e .
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src

# Run with verbose output
pytest -v
```

### Code Linting

```bash
# Run flake8
flake8 src/ tests/

# Check formatting with black
black --check src/ tests/
```

## CI Pipeline

The GitHub Actions CI pipeline runs on every push and pull request to `main` branch. It performs:

1. **Lint** - Code style checking with flake8 and black
2. **Test** - Run unit tests on multiple Python versions (3.9, 3.10, 3.11, 3.12)
3. **Build** - Verify package can be built successfully

## License

MIT License
