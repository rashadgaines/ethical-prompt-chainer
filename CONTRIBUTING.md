# Contributing to Ethical Prompt Chainer

Thank you for your interest in contributing to Ethical Prompt Chainer! This document provides guidelines and instructions for contributing.

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment for everyone.

## Development Setup

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/yourusername/ethical-prompt-chainer.git
   cd ethical-prompt-chainer
   ```
3. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. Install development dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

## Development Workflow

1. Create a new branch for your feature/fix:
   ```bash
   git checkout -b feature/your-feature-name
   ```
2. Make your changes
3. Run tests:
   ```bash
   pytest
   ```
4. Format code:
   ```bash
   black .
   isort .
   ```
5. Type check:
   ```bash
   mypy .
   ```
6. Lint:
   ```bash
   flake8
   ```
7. Commit your changes with a descriptive message
8. Push to your fork
9. Create a pull request

## Pull Request Process

1. Update the README.md with details of changes if needed
2. Update the documentation if needed
3. Ensure all tests pass
4. The PR will be merged once you have the sign-off of at least one maintainer

## Adding New Features

When adding new features:

1. Add appropriate tests
2. Update documentation
3. Follow the existing code style
4. Add type hints
5. Consider backward compatibility

## Reporting Bugs

Please report bugs using the GitHub issue tracker. Include:

1. A clear description of the bug
2. Steps to reproduce
3. Expected behavior
4. Actual behavior
5. Environment details

## Documentation

When adding new features or making changes:

1. Update relevant documentation
2. Add docstrings to new functions/classes
3. Include examples where appropriate

## Testing

- Write tests for new features
- Ensure all tests pass
- Maintain or improve test coverage

## Code Style

- Follow PEP 8
- Use type hints
- Format code with black
- Sort imports with isort
- Run mypy for type checking
- Use flake8 for linting

## Questions?

Feel free to open an issue for any questions about contributing. 