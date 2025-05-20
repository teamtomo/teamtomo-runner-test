# torch-test

[![License](https://img.shields.io/pypi/l/torch-test.svg?color=green)](https://github.com/tlambert03/torch-test/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/torch-test.svg?color=green)](https://pypi.org/project/torch-test)
[![Python Version](https://img.shields.io/pypi/pyversions/torch-test.svg?color=green)](https://python.org)
[![CI](https://github.com/tlambert03/torch-test/actions/workflows/ci.yml/badge.svg)](https://github.com/tlambert03/torch-test/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/tlambert03/torch-test/branch/main/graph/badge.svg)](https://codecov.io/gh/tlambert03/torch-test)

Package description.

## Development

The easiest way to get started is to use the [github cli](https://cli.github.com)
and [uv](https://docs.astral.sh/uv/getting-started/installation/):

```sh
gh repo fork tlambert03/torch-test --clone
# or just
# gh repo clone tlambert03/torch-test
cd torch-test
uv sync
```

Run tests:

```sh
uv run pytest
```

Lint files:

```sh
uv run pre-commit run --all-files
```
