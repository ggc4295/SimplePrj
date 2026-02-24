# SimplePrj

![CI](https://github.com/ggc4295/SimplePrj/actions/workflows/ci.yml/badge.svg)

A simple Python project for testing GitHub CI/CD functionality.

## Features

- Simple calculator module with basic math operations
- Unit tests with pytest
- GitHub Actions CI pipeline
- Code linting with flake8
- Code formatting check with black
- Fast dependency management with [uv](https://docs.astral.sh/uv/)

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
├── pyproject.toml          # Project config & dependencies
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.9+
- [uv](https://docs.astral.sh/uv/getting-started/installation/) — fast Python package manager

### Install uv

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Installation

```bash
# Clone the repository
git clone https://github.com/ggc4295/SimplePrj.git
cd SimplePrj

# Create virtual environment and install all dev dependencies
uv sync --extra dev
```

> `uv sync` will automatically create a `.venv` and lock dependencies into `uv.lock`.

### Running Tests

```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=src

# Run with verbose output
uv run pytest -v
```

### Code Linting

```bash
# Run flake8
uv run flake8 src/ tests/

# Check formatting with black
uv run black --check src/ tests/

# Auto-format with black
uv run black src/ tests/
```

## CI Pipeline

The GitHub Actions CI pipeline runs on every push and pull request to `main` branch. It performs:

1. **Lint** - Code style checking with flake8 and black
2. **Test** - Run unit tests on multiple Python versions (3.9, 3.10, 3.11, 3.12)
3. **Build** - Verify package can be built successfully with `uv build`

All CI steps use the official [`astral-sh/setup-uv`](https://github.com/astral-sh/setup-uv) action with caching enabled for fast installs.

## License

MIT License
