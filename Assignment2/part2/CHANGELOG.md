## [0.1.0] - 2023-09-21

### Added
- Created a new `jsonapi` module that:
  - Overrides the default encoder and decoder of the `json` package.
  - Can handle `range` and `complex` numbers, allowing them to be encoded to, and decoded from, JSON format.

- Implemented the basic package structure to support a build system:
  - Added a `pyproject.toml` file to specify build system requirements and backend.
  - Created a `setup.py` file to define package metadata and dependencies.
  - Included an `__init__.py` file to mark the directory as a Python package.

### Notes
- This release lays the foundation for the project's build system and extends the JSON handling capabilities of the Python standard library.

[0.1.0]: https://github.com/yourusername/yourrepository/releases/tag/v0.1.0