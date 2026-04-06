---
name: python
description: Comprehensive Python skill covering package management with uv, modern 3.10+ syntax and typing, and ecosystem best practices including Ruff, FastAPI, Loguru, and async programming.
---

# Python

## Package and Environment Management (uv)

Always use `uv` for all package management and script execution tasks.

- Use `uv add <package>` to install dependencies.
- Use `uv remove <package>` to uninstall dependencies.
- Use `uv sync` to install dependencies from lockfiles or requirements.
- Use `uv venv` to manage virtual environments automatically.
- Execute all Python scripts using `uv run <script.py>`.
- Execute tools (like pytest, ruff, mypy) using `uv run <tool>`.
- Never use `pip`, `poetry`, `pip-tools`, or `virtualenv` commands directly.

## Type Annotations

Always explicitly annotate function return types, including `-> None`.

Import from `typing` only for advanced features not available in built-ins (e.g., `Any`, `Callable`, `Self`, `Literal`, `overload`).

### Built-in Collections

Use built-in lowercase types for hints (`list[int]`, `dict[str, int]`, `tuple[str, int]`, `type[MyClass]`). Do not use `typing.List`, `typing.Dict`, `typing.Tuple`, or `typing.Type`.

### Unions and Optionals

Use the pipe operator `|` for unions and optionals (e.g., `int | None`, `str | int`) instead of `typing.Union` or `typing.Optional`.

### Type Aliases (3.12+)

Use the `type` keyword for type aliases (e.g., `type UserID = int`).

## Modern Syntax (3.10+)

### File System Interactions

Use `pathlib.Path` for all file system interactions. Avoid `os.path` and `os.walk`.

### Structural Pattern Matching

Use `match` and `case` statements over complex `if/elif/else` chains or `isinstance` checks.

### String Formatting

Use f-strings for all string formatting. Avoid `%` formatting and `.format()`.

### Assignment Expressions

Use the walrus operator `:=` for assignment expressions inside conditions.

### Classes and Data Structures

Use `@dataclass` (with `slots=True` when possible) for classes that primarily store data. Use `enum.StrEnum` or `enum.IntEnum` for constant enumerations.

## Best Practices

### Code Quality

Assume the use of Ruff for linting and formatting. Write code that complies with standard Ruff rules (sorted imports, standard whitespace).

### Documentation

Use Google-style docstrings for all complex functions and classes.

### Library Selections

- **Web APIs**: Use `FastAPI`. Avoid Flask or Django for new projects.
- **Logging**: Use `loguru` instead of the built-in `logging` module.

### Performance and Architecture

- Use `async` and `await` for I/O-bound operations. Use `asyncio.run()` for entry points.
- Manage resources (files, sockets, locks) using `with` statements (context managers).
- Prefer generators and iterators over creating large lists in memory for data processing.
