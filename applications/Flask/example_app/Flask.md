# Flask Concepts

- app: `app = Flask(__name__)`
- route: `@app.route(...)`, `app.add_url_rule(...)`
  - dynamic route: `/<name>`
- development server: `flask run`, `app.run()`
- debug mode: reloader, debugger `FLASK_DEBUG=1`

## request-response cycle
context globals:
- 上下文: 线程中的全局变量
- 应用上下文
  - `current_app`: 活跃应用的应用实例 `from flask import current_app`
  - `g`: 用于处理请求的临时存储, 每个请求重置
  - 当应用上下文被`push()`后, `current_app`和`g`在线程中可用
- 请求上下文
  - `request`: 请求对象 `from flask import request`
  - `session`: 用户会话, 一个字典
- `app.app_context()`
```python
>>> from hello import app
>>> app_ctx = app.app_context()
>>> app_ctx.push()
>>> current_app.name
'hello'
>>> app_ctx.pop()
```

request dispatching: 
- `@app.route()` decorator
- `app.add_url_rule()` function
- `app.url_map`: route info

request object: context variable
- `form`, `args`, `headers`, `cookies`, `files`, ...

request hooks: code execute before or after each request is processed
- `@before_request`, `@before_first_request`, `@after_request`, `@teardown_request`
- `g`: share data between request hook functions and view functions

response: 
- `return <content>, <status code>, [headers]`
- `make_response(<content>, status code, [headers])`
- `redirect(<url>)`
- `abort(<status code>)`: raise an exception

extensions: database, user authentication 

## template: Jinja2

template for holding presentation logic.

variable: `{{ name }}`
- typed
- filters: `{{ name | lower}}`
  - `safe`, `captitalize`, ...

```python
render_template('<template-filename>', '<key-value-pairs>')
```

control structures
- `{% if %} {% else %} {% endif %}`
- `{% for ... in ... %} {% endfor %}`
- `{% macro %} {% endmacro %}`
- `{% import ... as ... %}`
- `{% include ... %}`
- template inheritance: 
  - `{% block ... %} {% endblock %}`, 
  - `{% extends %}`, `{{ super() }}`

Flask-Bootstrap
- base template: `bootstrap/base.html`
  - blocks: `doc`, `html_attribs`, ..

custom error pages
- `@app.errorhandler(<status code>)`, `404.html`, `500.html`

links: 
- `url_for(...)`: generate url from app URL map `app.url_map`

static files: `/static` folder

Flask-Moment: localization of data and times

## Web Forms
Flask-WTF extension: WTForms package 

`FlaskForm`

WTForms
- `*Field`
- validators: `DataRequired`, ...


```html
{% import "bootstrap/wtf.html" as wtf %}
{{ wtf.quick_form(form) }}
```

`form.validate_on_submit()`

`session["var-name"]`, `redirect(...)`


message flashing: 
- `flash(...)` in view functions
- `get_flashed_message()` in template

## Databases
- Flask-SQLAlchemy

database URL:
- MySQL mysql://username:password@hostname/database
- Postgres postgresql://username:password@hostname/database
- SQLite (Linux, macOS) sqlite:////absolute/path/to/database
- SQLite (Windows) sqlite:///c:/absolute/path/to/database

`SQLALCHEMY_DATABASE_URI`, `SQLALCHEMY_TRACK_MODIFICATIONS` in `app.config`

SQLAlchemy column types and options:
- `Integer`, ...
- `primary_key`, ...

relationship:
- one-to-many
```python
class Role(db.Model):
# ...
users = db.relationship('User', backref='role')
class User(db.Model):
# ...
role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
```
- one-to-one
- many-to-one
- many-to-many

relationship options:
- `backref`, `primaryjoin`, `lazy`, `uselist`, `order_by`, `secondary`, `secondaryjoin`

`flask shell`
```python
from hello import db
db.create_all()
db.drop_all()

# transaction
db.session.add(...)
db.session.add_all(...)
db.session.delete(...)
db.session.commit()
db.session.rollback()

# query
Role.query.all()
User.query.filter_by(xxx=yyy).all()
str(User.query.filter_by(xxx=yyy)) # native SQL
User.query.filter_by(xxx=yyy).first() # first
# more query filters: limit(), offset(), order_by(), group_by()

# query executor: all(), first(), first_or_404(), get(), get_or_404(), count(), paginate()
```

integrate with Python shell `flask shell`
```python
@app.shell_context_processor
def make_shell_context():
return dict(db=db, User=User, Role=Role)
```

Flask-Migrate: wrapper on Alembic
- migration script
- functions: `upgrade()`, `downgrade()`
- command: manually `revision`, automatically `migrate`
- apply command: `upgrade`

```python
from flask_migrate import Migrate
migrate = Migrate(app, db)
```

```shell
flask db init

# manually `revision`, automatically `migrate`
flask db migrate -m "initial migration"

flask db upgrade
flask db downgrade
```

## Flask-Mail
- `smtplib`: SMTP(Simple Mail Transfer Protocol)
- `Mail`, `Message`

config key:
- `MAIL_SERVER`, `MAIL_PORT`, ...

## example_app

- 配置选项: `Config`
- 应用包: 应用工厂`create_app(config_name)`
  - 单脚本应用
  - blueprint: 类似于应用, 但可以定义路由和错误处理器. 需要注册到应用中.
- 应用脚本: 
  - 定义应用实例`app`
  - 定义数据迁移
  - 定义`flask shell`脚本上下文处理器: `@app.shell_context_processor`, 注入`db`等 
  - 定义命令行命令: `@app.cli.command()`, 例如执行单元测试`test`
- 单元测试: `unittest` 
- 数据库设置: 使用Flask-Migrate
- 运行应用: `flask run`

features:
- user authentication
- user roles
- user profiles
- blog posts
- followers
- user commments

### program structure
P.85

```shell
|-- README.md
|-- app                       应用目录
|   |-- __init__.py
|   |-- email.py              邮件工具
|   |-- main                  main blueprint
|   |   |-- __init__.py       
|   |   |-- errors.py           错误处理器
|   |   |-- forms.py            表单
|   |   `-- views.py            视图/路由
|   |-- models.py             模型
|   |-- static                静态资源
|   |   |-- favicon.ico
|   |   `-- style.css
|   `-- templates             模板
|       |-- 404.html
|       |-- base.html
|       |-- index.html
|       `-- user.html
|-- config.py                  配置
|-- data-dev.sqlite            sqlite文件
|-- main.py                    入口
|-- migrations                 数据库迁移脚本目录
|-- requirements.txt
`-- tests                      单元测试
    |-- __init__.py
    `-- test_basics.py
```

### user authentication

Flask authentication extension:
- Flask-Login                                                    <-- 管理用户会话
- [Werkzeug](https://werkzeug.palletsprojects.com/)              <-- 密码哈希和验证
- itsdangerous                                                   <-- 安全token生成和验证

> Werkzeug is a comprehensive WSGI web application library. It began as a simple collection of various utilities for WSGI applications and has become one of the most advanced WSGI utility libraries.
>
> Werkzeug doesn’t enforce any dependencies. It is up to the developer to choose a template engine, database adapter, and even how to handle requests.


`auth` blueprint

模拟创建用户
```shell
$ flask shell
Python 3.12.3 | packaged by conda-forge | (main, Apr 15 2024, 18:20:11) [MSC v.1938 64 bit (AMD64)] on win32
App: app
Instance: D:\workspace\github\workbench\Python\applications\Flask\example_app\instance
>>> u = User(email='a@example.com', username='john', password='123')
>>> db.session.add(u)
>>> db.session.commit()
>>> User.query.filter_by(email='a@example.com').first()
<User 'john'>
```

Flask-Login
- `UserMixin`
- `LoginManager`
  - `init_app(app)`: 初始化
  - `@login_manager.user_loader`: 加载用户
- `@login_required`: 保护路由
- `current_user`: 当前用户
- `login_user()`: 会话中标记为已登录
- `logout_user()`: 登出

新用户注册

账户确认邮件

### user roles

### user profiles

### blog posts

### followers

SQLAlchemy many-to-many example: 学生课程注册
```python
registrations = db.Table('registrations',                            # 中间表
  db.Column('student_id', db.Integer, db.ForeignKey('students.id')), # 外键
  db.Column('class_id', db.Integer, db.ForeignKey('classes.id'))
)

class Student(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String)
  classes = db.relationship('Class',                # 1对多的1端
    secondary=registrations,                        # 使用中间表
    backref=db.backref('students', lazy='dynamic'), # 回引
    lazy='dynamic')

class Class(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String)
```

自引用关系: users, followers
```python
class Follow(db.Model):
  __tablename__ = 'follows'
  follower_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True) # 关注人
  followed_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True) # 被关注人
  timestamp = db.Column(db.DateTime, default=datetime.utcnow)

class User(UserMixin, db.Model):
  # ...
  followed = db.relationship('Follow',               # 我关注的人
    foreign_keys=[Follow.follower_id],               # 外键: 关注人
    backref=db.backref('follower', lazy='joined'),   # 回引: 
                                  # joined: 联接时相关对象立即返回, 单个查询, 例user.followed().all()
                                  # select: 默认值, 第一次访问时, 独立的查询
    lazy='dynamic',                                  # 关系属性返回查询的对象而不是项
    cascade='all, delete-orphan')                    # 级联: 父对象上的动作如何传播到相关对象
                  # delete-orphan: 默认级联将相关对象的外键设置为NULL, 删除孤儿直接删除相关对象
                  # all: 除delete-orphan的所有级联选项
  followers = db.relationship('Follow',              # 关注我的人
    foreign_keys=[Follow.followed_id],               # 外键: 被关注人
    backref=db.backref('followed', lazy='joined'),
    lazy='dynamic',
    cascade='all, delete-orphan')
```

查询我关注的人的帖子: 联接join
```python
db.session.query(Post).select_from(Follow).\       # 查询帖子, 我关注的
  filter_by(follower_id=self.id).\
  join(Post, Follow.followed_id == Post.author_id) # 联接: 帖子

# 简化
Post.query.join(Follow, Follow.followed_id == Post.author_id)\ # 联接
  .filter(Follow.follower_id == self.id)
```

### user commments

```python
class Comment(db.Model):
  __tablename__ = 'comments'
  id = db.Column(db.Integer, primary_key=True)
  body = db.Column(db.Text)
  body_html = db.Column(db.Text)
  timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
  disabled = db.Column(db.Boolean)
  author_id = db.Column(db.Integer, db.ForeignKey('users.id'))           # 外键: 用户
  post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))             # 外键: 帖子

  db.event.listen(Comment.body, 'set', Comment.on_changed_body)

class User(db.Model):
  # ...
  comments = db.relationship('Comment', backref='author', lazy='dynamic') # 用户的评论

class Post(db.Model):
  # ...
  comments = db.relationship('Comment', backref='post', lazy='dynamic')   # 帖子的评论
```

# API
REST

versioning:
- `/api/v1/posts`
- `/api/v2/posts`

in Flask:
- `request.get_json()`
- `jsonify()`
- `request.accept_mimetypes.accept_json`

API blueprint: folder `app/api`

Flask-HTTPAuth

token-based authentication

serialization with JSON: `to_json`, `from_json`

resource endpoint: `jsonify()`

HTTPie

# Ops

testing
- `coverage`

HTTPS: Flask-SSLify

production-ready web server: Gunicorn, uWSGI

process-monitoring utility: Supervisor

environment variables: `.env`, `python-dotenv`

logging:
- `import logging`
- `app.logger`

# Resources

more extensions:
- Flask-Babel: Internationalization and localization support
- Marshmallow: Serialization and deserialization of Python objects, useful for API resource representations
- Celery: Task queue for processing background jobs
- Frozen-Flask: Conversion of a Flask application to a static website
- Flask-DebugToolbar: In-browser debugging tools
- Flask-Assets: Merging, minifying, and compiling of CSS and JavaScript assets
- Flask-Session: Alternative implementation of user sessions that use server-side storage
- Flask-SocketIO: Socket.IO server implementation with support for WebSocket and long-polling