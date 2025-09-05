# Code of 'Fluent Python'

- Part I. Data Structures: 1 - 6
- Part II. Functions as Objects: 7 - 10
- Part III. Classes and Protocols: 11 - 16
- Part IV. Control Flow: 17 - 21
- Part V. Metaprogramming: 22 - 24

# Depedencies

| Dependency | Install                           | Description                                                            |
| :--------- | :-------------------------------- | :--------------------------------------------------------------------- |
| Poetry     | `poetry new fluent-python`        | `poetry env activate` `source .venv/Scripts/activate`                  |
| unittest   | -                                 |                                                                        |
| Mypy       | `poetry add mypy --group dev`     | `poetry run mypy tests/function_as_objects/test_function_type_hint.py` |
| autopep8   | `poetry add autopep8 --group dev` |                                                                        |
| pylint     | `poetry add pylint --group dev`   |                                                                        |
| NumPy      | `poetry add numpy`                |                                                                        |

* unittest: `test_str.py`
```shell
# discover and run all
$ poetry run python -m unittest discover
$ poetry run python -m unittest
# run specific module
$ poetry run python -m unittest tests.test_str
$ poetry run python tests/test_str.py
# run specific test class
$ poetry run python -m unittest tests.test_str.TestStringMethods
# run specific test method
$ poetry run python -m unittest tests.test_str.TestStringMethods.test_upper
```