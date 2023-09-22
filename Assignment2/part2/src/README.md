# JSONAPI Repository

## Overview
The `jsonapi` repository contains custom JSON encoding and decoding functionalities, focusing mainly on handling complex types like `range` and `complex` numbers. The implementation is housed under the `src` directory, with accompanying tests in the `tests` directory.

## Repository Structure
```
jsonapi/
│
├── src/
│   └── jsonapi.py          # Main module with JSON encoding and decoding functionalities
│
├── tests/
│   └── test_jsonapi.py     # Unit tests for the jsonapi module
│
├── setup.py                # Setup script for packaging
└── pyproject.toml          # Defines build system details
```

## Building the Project
To build the project, navigate to the project root directory and run the following command:
```sh
python -m build
```
Make sure to have the `build` module installed. If not, you can install it using pip:
```sh
pip install build
```

## Running Tests
To run the tests for the `jsonapi` module, navigate to the `tests` directory and execute the following command:
```sh
python3 test_jsonapi.py
```

## Usage
After building the project, you can use the functionalities provided by the `jsonapi` module by importing it into your Python scripts or projects.