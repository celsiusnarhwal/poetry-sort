# poetry-sort

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/poetry-sort?logo=python&logoColor=white&style=for-the-badge)](https://pypi.org/project/poetry-sort)
[![PyPI](https://img.shields.io/pypi/v/poetry-sort?logo=pypi&color=green&logoColor=white&style=for-the-badge)](https://pypi.org/project/poetry-sort)
[![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/celsiusnarhwal/poetry-sort?logo=github&color=orange&logoColor=white&style=for-the-badge)](https://github.com/celsiusnarhwal/poetry-sort/releases)
[![PyPI - License](https://img.shields.io/pypi/l/poetry-sort?color=03cb98&style=for-the-badge)](https://github.com/celsiusnarhwal/poetry-sort/blob/main/LICENSE)

poetry-sort is a [Poetry](https://python-poetry.org/) plugin that alphabetically sorts the dependencies in your `pyproject.toml` file.

## Installation

```bash
poetry self add poetry-sort
```

## Usage

```bash
poetry sort
```

`poetry sort` supports the `--with`, `--without`, and `--only` options, which function identically to `poetry install`.
For full usage information, run `poetry sort --help`.

poetry-sort runs automatically whenever you run `poetry add` or `poetry init` and will sort only the dependency
groups that were modified by the command.


## Configuration

poetry-sort can be configured via a `tool.sort.config` section in your `pyproject.toml` file.

```toml
[tool.sort.config]
sort-python = false
format = true
```

The following options are available:

- `sort-python`: Whether to also sort the `python` dependency. If `false`, the `python` dependency will be placed at
the top of `tool.poetry.dependencies`; if `true`, it will be sorted alphebetically with everything else.
Defaults to `false`.

- `format`: Whether to apply some basic formatting to `pyproject.toml` after sorting. If `true`, poetry-sort will
take all occurences of three or more consecutive newlines in `pyproject.toml` and replace them with two newlines.
If `false`, poetry-sort will not modify `pyproject.toml` beyond just sorting your dependencies. Defaults to `true`.


## License
poetry-sort is licensed udner the [MIT License](LICENSE.md).