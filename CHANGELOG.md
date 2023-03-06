# Changelog[^1]

All notable changes to poetry-sort will be documented here. Breaking changes are marked with a 🚩.

poetry-sort adheres to [semantic versioning](https://semver.org/spec/v2.0.0.html).

## <a name="2-0-0">[2.0.0] - 2023-03-06</a>

### Added

- poetry-sort now keeps a proper changelog. You're reading it. Release notes from previous versions have been ported
  over to this changelog.

### Changed

- poetry-sort is now configured via the `tool.poetry-sort` section of `pyproject.toml` instead of `tool.sort.config`.
- The values for settings in `tool.poetry-sort` are no longer *strictly* required to be booleans as long as
  [Pydantic](https://docs.pydantic.dev) can coerce them to booleans.
- poetry-sort now supports Python 3.8 and later. It previously only supported Python 3.10 and later.

### Removed

- 🚩 Support for configuring poetry-sort via the `tool.sort.config` section of `pyproject.toml` has been removed.
- 🚩 Support for configuring poetry-sort globally via Poetry's `config.toml` file has been removed.

## <a name="1-2-0">[1.2.0] - 2022-12-25</a>

### Added

- `tool.sort.config` now supports an `auto` configuration option. By setting it to `false`, you can
  disable poetry-sort's automatic sorting of dependencies after running `poetry add` or `poetry init`.
- poetry-sort's settings can now be defined both on a per-project basis in `pyproject.toml` and globally
  in Poetry's `config.toml` file. Where the two files conflict, `pyproject.toml` will take precedence.

### Changed

- The values for settings in `tool.sort.config` are now strictly required to be booleans.

# <a name="1-1-0">[1.1.0] - 2022-12-25</a>

### Added

- You can now opt-in to case-sensitive sorting by setting the `case-sensitive` option to `true` in
  `tool.sort.config`.

# <a name="1-0-1">[1.0.1] - 2022-12-25</a>

### Fixed

- Fixed a bug where the sorting algorithm would act in a case-sensitive manner.

# <a name="1-0-0">[1.0.0] - 2022-12-25</a>

This is the initial release of poetry-sort.

[^1]: Based on version 1.0.0 of [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
