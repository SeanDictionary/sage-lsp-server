# SageMath LSP Server (Forked from [Python LSP Server](https://github.com/python-lsp/python-lsp-server))

See original readme [here](./pylsp-README.md) or orginal repo [here](https://github.com/python-lsp/python-lsp-server)

![Release](https://img.shields.io/github/v/release/SeanDictionary/sage-lsp-server) ![Platform](https://img.shields.io/badge/platform-Linux-green) ![License](https://img.shields.io/github/license/SeanDictionary/sage-lsp-server) ![GitHub repo size](https://img.shields.io/github/repo-size/SeanDictionary/sage-lsp-server) ![GitHub last commit](https://img.shields.io/github/last-commit/SeanDictionary/sage-lsp-server) ![Python](https://img.shields.io/badge/python-3.9%2B-blue)

This is a fork of the [Python LSP Server](https://github.com/python-lsp/python-lsp-server) that costomizes it for use with [SageMath](https://www.sagemath.org/). It adds support for Sage-specific syntax sugar and constructs, making it easier to work with Sage code in editors that support the Language Server Protocol (LSP).

## Features

-   [Rope](https://github.com/python-rope/rope) for Completions and renaming
-   [Pyflakes](https://github.com/PyCQA/pyflakes) linter to detect various errors
-   [McCabe](https://github.com/PyCQA/mccabe) linter for complexity checking
-   [pycodestyle](https://github.com/PyCQA/pycodestyle) linter for style checking
-   [pydocstyle](https://github.com/PyCQA/pydocstyle) linter for docstring style checking (disabled by default)
-   [autopep8](https://github.com/hhatto/autopep8) for code formatting
-   [YAPF](https://github.com/google/yapf) for code formatting (disabled by default)
-   [flake8](https://github.com/pycqa/flake8) for error checking (disabled by default)
-   [pylint](https://github.com/PyCQA/pylint) for code linting (disabled by default)

## Differences

-   Support Sage synatx sugar. (e.g. `^^`, `R.<x,y> = ...`, etc.)
-   Linter to check for Sage-specific grammar
-   Formatters for Sage synatx sugar

## Change Logs

See [CHANGELOG.md](./CHANGELOG.md)

See [original CHANGELOG.md](./pylsp-CHANGELOG.md) for original changelogs.

## Others

Others are the same as the original Python LSP Server. You can see the original [CONTRIBUTING.md](./CONTRIBUTING.md)
