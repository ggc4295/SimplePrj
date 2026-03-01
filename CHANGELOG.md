# Changelog

All notable changes to this project will be documented in this file.

---

- **v0.2.0**
  - `src/cli.py`: interactive CLI calculator (`calc` command)
    - Safe AST-based expression parser — no `eval`, no code injection risk
    - Supports `+`, `-`, `*`, `/`, `**`, `%` and parentheses
    - Continuous input loop; `quit`/`exit` to stop; `help` for examples
    - Graceful error handling for division by zero and invalid input
  - `tests/test_cli.py`: 23 unit tests covering `safe_eval` and `format_result`
  - `pyproject.toml`: registered `calc` CLI entry point via `[project.scripts]`
  - README: comprehensive rewrite — accurate project structure, CLI docs, CI/Release table

- **v0.1.0**
  - Initial release of SimplePrj
  - Calculator module: `add`, `subtract`, `multiply`, `divide`, `power`, `modulo`
  - Utils module: `is_even`, `is_positive`, `factorial`, `fibonacci`, `clamp`
  - GitHub CI pipeline: lint, test (4 Python versions), build, PyInstaller EXE artifact
  - GitHub Pages project website (`web_site/`)
  - Secret scanning and automated code review on PRs
