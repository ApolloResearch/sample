# Sample project

This is a sample project that uses the engineering practices described in [Apollo Engineering Guide](https://docs.google.com/document/d/1O6qFI93XjZPIltSELs18v8jEIOclvOinQsRCQkmsD64/edit#heading=h.vznvxqme70zl).

If you wish to use this repository as a template for your project, copy the contents of this directory to your new repository and run

```bash
./setup_pkg.sh <name_of_your_package>
```

with the name of your package as the argument. This will rename the package and set up the pre-commit hooks. You should also provide your name and email address in `setup.py`. You may then wish to remove the files and content that you do not need for your project.

## Dislosure level

You must set the disclosure level of your repository in `ACCESS.md`, listing all parties that can access the project. See [disclosure levels](https://www.lesswrong.com/posts/Gs29k3beHiqWFZqnn/conjecture-internal-infohazard-policy) for more information.

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

This repository uses [pre-commit](https://pre-commit.com/) to run a series of checks on the code before committing. These are installed with the development dependencies above.

## Usage

### MNIST

To train an MLP on MNIST, define a config file (see `configs/mnist.yaml` for an example) and run

```bash
python scripts/train_mnist.py <path_to_config_file>
```

You may be asked to enter your wandb API key. You can find it in your [wandb account settings](https://wandb.ai/settings). Alternatively, to avoid entering your API key on program execution, you can set the environment variable `WANDB_API_KEY` to your API key.
