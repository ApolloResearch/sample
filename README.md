# Sample project

This is a sample project that uses the solid engineering practices described in [Apollo Engineering Guide](https://docs.google.com/document/d/1O6qFI93XjZPIltSELs18v8jEIOclvOinQsRCQkmsD64/edit#heading=h.vznvxqme70zl).

When making a new repository, copy the contents of this directory to your new repository. You will need to rename `mypkg` to the name of your package in the following places:

- The `mypkg` directory name
- `setup.py`
- `.github/workflows/checks.yaml`
- `pre-commit` (and subsequently your local `.git/hooks/pre-commit` file)

## Installation

From the root of the repository, run

```bash
pip install -e .
```

## Development

To install the development dependencies, run

```bash
pip install -e ".[dev]"
```

Suggested extensions and settings for VSCode are provided in `.vscode/`.

### Pre-commit hooks

To use the suggestion precommit hook copy the file `pre-commit` to `.git/hooks/` and make it executable (`chmod +x .git/hooks/pre-commit`).
