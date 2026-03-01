# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.2.0] - 2026-03-01

### Added
- `src/cli.py`: interactive CLI calculator (`calc` command)
  - Safe AST-based expression parser — no `eval`, no code injection risk
  - Supports `+`, `-`, `*`, `/`, `**`, `%` and parentheses
  - Continuous input loop with `quit`/`exit` to stop
  - Built-in `help` command with examples
  - Graceful error handling for division by zero and invalid input
- `tests/test_cli.py`: 23 unit tests covering `safe_eval` and `format_result`
- `pyproject.toml`: registered `calc` CLI entry point via `[project.scripts]`

### Changed
- README: comprehensive rewrite — accurate project structure, full CLI docs, CI table

---

## [0.1.0] - Initial Release

### Added
- Calculator module: `add`, `subtract`, `multiply`, `divide`, `power`, `modulo`
- Utils module: `is_even`, `is_positive`, `factorial`, `fibonacci`, `clamp`
- GitHub CI pipeline: lint, test (Python 3.9–3.12), build, PyInstaller EXE
- GitHub Pages project website (`web_site/`)
- Secret scanning and automated code review on PRs
