# autopep8
* https://pypi.org/project/autopep8/

> autopep8 automatically formats Python code to conform to the PEP 8 style guide. It uses the *pycodestyle* utility to determine what parts of the code needs to be formatted. autopep8 is capable of fixing most of the formatting issues that can be reported by pycodestyle.

```shell
$ pip install autopep8
```


disabling line-by-line:
```python
# autopep8: off
# autopep8: on
```
or
```python
# fmt: off
# fmt: on
```

# VSCode

user settings:
```json
{
  "[python]": {
        "editor.defaultFormatter": "ms-python.autopep8",
        "editor.formatOnSave": true,
    },
    "autopep8.args": [
        "--indent-size=2"
    ],
    "autopep8.interpreter": [
        "D:\\software\\miniconda3\\python.exe"
    ],
}
```

workspace settings: with venv
```json
{
// autopep8
  "autopep8.args": [
    "--indent-size=2"
  ],
  "autopep8.importStrategy": "fromEnvironment",
  "autopep8.interpreter": []
}
```