# SimplePrj

![CI](https://github.com/ggc4295/SimplePrj/actions/workflows/ci.yml/badge.svg)

A simple Python project demonstrating GitHub CI/CD best practices, including an interactive CLI calculator, utility math functions, multi-version testing, and automated packaging.

## Features

- **Interactive CLI calculator** — safe AST-based expression evaluator, no `eval`
- **Calculator module** — add, subtract, multiply, divide, power, modulo
- **Utility functions** — `is_even`, `is_positive`, `factorial`, `fibonacci`, `clamp`
- **Unit tests** with pytest and coverage reporting
- **GitHub Actions CI** — lint, test (Python 3.9–3.12), build, Windows EXE packaging
- **Code quality** — flake8 linting + black formatting (line length 120)
- **Fast dependency management** with [uv](https://docs.astral.sh/uv/)
- **GitHub Pages** project website

## Project Structure

```
SimplePrj/
├── .github/
│   └── workflows/
│       ├── ci.yml              # Lint / test / build / package (Windows EXE)
│       ├── code-review.yml     # Automated code review on PRs
│       ├── deploy-pages.yml    # Deploy web_site/ to GitHub Pages
│       ├── release.yml         # Release workflow
│       └── secret-scan.yml     # Secret scanning on push
├── src/
│   ├── __init__.py
│   ├── calculator.py           # Calculator class (6 operations)
│   ├── cli.py                  # Interactive CLI calculator
│   ├── main.py                 # Demo entry point (PyInstaller target)
│   └── utils.py                # Math utility functions
├── tests/
│   ├── __init__.py
│   ├── test_calculator.py      # Calculator tests
│   ├── test_cli.py             # CLI / safe_eval tests
│   └── test_utils.py           # Utility function tests
├── web_site/
│   ├── index.html              # Project website (GitHub Pages)
│   └── qa.html                 # Q&A page
├── .gitattributes
├── .gitignore
├── build_exe.py                # PyInstaller build script
├── CHANGELOG.md
├── pyproject.toml              # Project config & dependencies
├── README.md
└── simpleprj.spec              # PyInstaller spec file
```

## Getting Started

### Prerequisites

- Python 3.9+
- [uv](https://docs.astral.sh/uv/getting-started/installation/) — fast Python package manager

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Installation

```bash
git clone https://github.com/ggc4295/SimplePrj.git
cd SimplePrj

# Create virtual environment and install all dev dependencies
uv sync --extra dev
```

> `uv sync` automatically creates `.venv` and locks dependencies into `uv.lock`.

## CLI Calculator

```bash
# Install the package (registers the `calc` command)
uv pip install -e .

# Launch
calc
```

Example session:

```
SimplePrj Calculator — type an expression to evaluate
Supports: + - * / ** % and parentheses
Type 'help' for examples, 'quit' or 'exit' to quit.

calc> 2 + 3
  = 5
calc> (3 + 4) * 2
  = 14
calc> 10 / 4
  = 2.5
calc> 2 ** 8
  = 256
calc> 17 % 5
  = 2
calc> -3 + 10
  = 7
calc> help
  Examples:
    2 + 3           → 5
    10 / 4          → 2.5
    2 ** 8          → 256
    (3 + 4) * 2     → 14
    17 % 5          → 2
calc> quit
Bye!
```

Expression parsing uses Python's `ast` module — no `eval`, no code injection risk.

## Development

### Running Tests

```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=src --cov-report=term-missing

# Run a specific test file
uv run pytest tests/test_cli.py -v
```

### Code Linting & Formatting

```bash
# Lint with flake8
uv run flake8 src/ tests/ --max-line-length=120

# Check formatting
uv run black --check --line-length=120 src/ tests/

# Auto-format
uv run black --line-length=120 src/ tests/
```

## CI Pipeline

Runs on every push and pull request to `main`.

| Job | What it does |
|-----|-------------|
| **Lint** | flake8 + black check (Python 3.12) |
| **Test** | pytest + coverage on Python 3.9, 3.10, 3.11, 3.12 |
| **Build** | `uv build` — verify package builds cleanly |
| **Package** | PyInstaller Windows EXE (artifact only, not published) |

All CI steps use [`astral-sh/setup-uv`](https://github.com/astral-sh/setup-uv) with caching for fast installs.

## Release

Triggered by pushing a version tag (`v*`) or manually via `workflow_dispatch`.

1. Builds Windows EXE with PyInstaller
2. Extracts release notes from `CHANGELOG.md`
3. Publishes a GitHub Release with the EXE as a downloadable asset

To create a new release, push a tag:

```bash
git tag -a v1.0.0 -m "Release v1.0.0"
git push origin v1.0.0
```

Additional automated workflows:
- **Secret Scan** — detects accidentally committed secrets on every push
- **Code Review** — automated review comments on PRs
- **Deploy Pages** — publishes `web_site/` to GitHub Pages on push to `main`

All CI steps use [`astral-sh/setup-uv`](https://github.com/astral-sh/setup-uv) with caching for fast installs.

## License

MIT License
