# example_app

Setup:
```shell
python -m virtualenv .venv
source .venv/Scripts/activate

.venv/Scripts/pip install flask
# Bootstrap
.venv/Scripts/pip install flask-bootstrap
# date and time
.venv/Scripts/pip install flask-moment
# web forms
.venv/Scripts/pip install flask-wtf
.venv/Scripts/pip install email-validator
# SqlAlchemy
.venv/Scripts/pip install flask-sqlalchemy
# Migration: Alemic
.venv/Scripts/pip install flask-migrate
# email
.venv/Scripts/pip install flask-mail
# login
.venv/Scripts/pip install flask-login
.venv/Scripts/pip install itsdangerous

# dependency
.venv/Scripts/pip freeze > requirements.txt
.venv/Scripts/pip install -r requirements.txt


export FLASK_APP=main.py
export FLASK_DEBUG=1

# Database migration
.venv/Scripts/flask.exe db init
.venv/Scripts/flask.exe db migrate
.venv/Scripts/flask.exe db upgrade

# test
.venv/Scripts/flask.exe test

# run
.venv/Scripts/flask.exe run --port 15000
```

## Dependencies

- [Flask-Bootstrap](https://pythonhosted.org/Flask-Bootstrap/)