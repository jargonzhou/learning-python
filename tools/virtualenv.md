# virtualenv
* https://virtualenv.pypa.io/en/latest/index.html

> a tool to create isolated Python environments. Since Python 3.3, a subset of it has been integrated into the standard library under the `venv` module.

## Usage

```shell
✗ pip3 install virtualenv
✗ python3 -m virtualenv --help
```

example:

```shell
python -m virtualenv .venv
source .venv/Scripts/activate

# Windows
.venv/Scripts/pip install websockets
.venv/Scripts/pip install protobuf
.venv/Scripts/pip freeze > requirements.txt
.venv/Scripts/python main.py
```