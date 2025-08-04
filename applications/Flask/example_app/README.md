# example_app

Code of 'Flask Web Development'.

Setup:
```shell
python -m virtualenv .venv
source .venv/Scripts/activate

pip install flask
# Bootstrap
pip install flask-bootstrap
# date and time
pip install flask-moment
# web forms
pip install flask-wtf
pip install email-validator
# SqlAlchemy
pip install flask-sqlalchemy
# Migration: Alemic
pip install flask-migrate
# email
pip install flask-mail
# login
pip install flask-login
pip install itsdangerous

# Markdown
pip install flask-pagedown markdown bleach

# HTTPAuth
pip install flask-httpauth

# dev
pip install faker

# test
pip install coverage
pip install playwright
playwright install # ~/AppData\Local\ms-playwright

# dependency
pip freeze > requirements.txt
pip install -r requirements.txt
# with common.txt, dev.txt
pip install -r requirements/dev.txt

export FLASK_APP=main.py
export FLASK_DEBUG=1

# Database migration
flask db init
flask db migrate
flask db upgrade

# test
flask test
flask test --coverage

# deploy
flask deploy

# run
flask run --port 15000
```

# Dependencies
- IDE: VSCode
- venv
- autopep8
- Flask-Bootstrap
- ...
- Flask-HTTPAuth

# Deployment

- development
  - [example_app.drawio](./doc/example_app.drawio)
```shell
# view SQLite datas
docker compose -f docker-compose.dev.yml up -d
```
- production
```shell
pip install gunicorn pymysql

docker compose build
docker compose up -d
```

# FAQ
- bootstrap, jquery resources loading in slow network: `app.config['BOOTSTRAP_SERVE_LOCAL'] = True`
