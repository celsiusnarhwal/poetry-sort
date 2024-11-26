# poetry-sort

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/poetry-sort?logo=python&logoColor=white&style=for-the-badge)](https://pypi.org/project/poetry-sort)
[![PyPI](https://img.shields.io/pypi/v/poetry-sort?logo=pypi&color=green&logoColor=white&style=for-the-badge)](https://pypi.org/project/poetry-sort)
[![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/celsiusnarhwal/poetry-sort?logo=github&color=orange&logoColor=white&style=for-the-badge)](https://github.com/celsiusnarhwal/poetry-sort/releases)
[![PyPI - License](https://img.shields.io/pypi/l/poetry-sort?color=03cb98&style=for-the-badge)](https://github.com/celsiusnarhwal/poetry-sort/blob/main/LICENSE.md)
[![Code style: Black](https://aegis.celsiusnarhwal.dev/badge/black?style=for-the-badge)](https://github.com/psf/black)

poetry-sort is a [Poetry](https://python-poetry.org/) plugin that alphabetically sorts the dependencies in
your `pyproject.toml` file.

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

You can configure poetry-sort via the `tool.poetry-sort` section of `pyproject.toml`.

```toml
[tool.poetry-sort]
auto = true
case-sensitive = false
sort-python = false
format = true

```

The following options are available:

- `auto` (`bool`, default: `true`): Whether or not to automatically sort dependencies when running `poetry add`
  or `poetry init`. `poetry sort` can always be run manually, regardless of this setting.

- `case-sensitive` (`bool`, default: `false`): Whether to take case into account when sorting.

- `sort-python` (`bool`, default: `false`): Whether to also sort the `python` dependency. If `false`, the `python`
  dependency will be placed at the top of `tool.poetry.dependencies`; if `true`, it will be sorted alphebetically with
  everything else.

- `format` (`bool`, default: `true`): Whether to apply some basic formatting to `pyproject.toml` after sorting.
  If `true`, poetry-sort will :take all occurences of three or more consecutive newlines in `pyproject.toml` and
  replace them with two newlines.

## License

poetry-sort is licensed under the [MIT License](https://github.com/celsiusnarhwal/poetry-sort/blob/main/LICENSE.md).
