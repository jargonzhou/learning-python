# Quickstart

Flask依赖于
- Werkzeug: 路由, 调试, WSGI子系统.
- Jinja2: 模板.
- Click: 命令行集成.

- 应用
```python
app = Flask(__name__)
```
- 路由和视图
```python
# 方式1
@app.route('/')
def index():
  return '<h1>Hello World!</h1>'

# 方式2
def index():
  return '<h1>Hello World!</h1>'
app.add_url_rule('/', 'index', index) # rule, endpoint, 视图函数view_func
```
- 完整应用
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
  return '<h1>Hello World!</h1>'
```
- 开发服务器
使用`flask`命令
```shell
export FLASK_APP=hello.py
flask run
```
不使用`flask`命令:
```python
if __name__ == '__main__':
  app.run()
```
- 调试模式
```shell
export FLASK_DEBUG=1
```

- app: `app = Flask(__name__)`
- route: `@app.route(...)`, `app.add_url_rule(...)`
  - dynamic route: `/<name>`
- development server: `flask run`, `app.run()`
- debug mode: reloader, debugger `FLASK_DEBUG=1`

# 应用`Flask`

## 请求上下文
使用上下文, 在视图函数中临时可用一些全局访问的对象, 而不需要接受大量的参数. 这些对象是线程局部对象.
- 应用上下文
  - `current_app`: 活跃应用的应用实例
  - `g`: 用于处理请求的临时存储, 每个请求重置
  - 当应用上下文被`push()`后, `current_app`和`g`在线程中可用
- 请求上下文
  - `request`: 请求对象
  - `session`: 用户会话, 一个字典

```python
from flask import current_app
from flask import request

request.headers.get('User-Agent')
```

Flask在分发请求到应用之前, 激活或压入应用和请求上下文, 在处理完请求之后移除. 不在活跃应用或请求上下文中访问这些对象会抛出错误.
```python
>>> from hello import app
>>> app_ctx = app.app_context()
>>> app_ctx.push()
>>> current_app.name
'hello'
>>> app_ctx.pop()
```

## 请求, 响应, 会话
URL映射: `app.url_map`

请求对象`request`
- `form`, `args`, `headers`, `cookies`, `files`, ...

请求hook: 在请求被处理之前或之后执行的代码, 使用装饰器实现
- `@before_request`, `@before_first_request`, `@after_request`, `@teardown_request`
- 模式: 使用`g`在请求hook和视图函数之间共享数据.

响应`response`: 
- 视图函数中返回: `return <content>, <status code>, [headers]`
- 创建响应对象函数: `make_response(<content>, status code, [headers])`
- 重定向: `redirect(<url>)`
- 异常退出: `abort(<status code>)`
```python
from flask import make_response
from flask import redirect
from flask import abort
```

会话`session`
- 类似于Python字典方式访问
```python
from flask import session

session['name'] = form.name.data
session.get('name')
```

## 路由

TODO: 路由形式

# 模板: Jinja2
处理表示逻辑的模板.

变量: `{{ name }}`
- 有类型的
- 使用过滤器: `{{ name | lower}}`
  - `safe`, `captitalize`, ...

渲染模板
```python
from flask import render_template

render_template('<template-filename>', '<key-value-pairs>')
```

模板中的控制结构
- `{% if %} {% else %} {% endif %}`
- `{% for ... in ... %} {% endfor %}`
- 宏: `{% macro %} {% endmacro %}`
- 导入: `{% import ... as ... %}`
- 包含: `{% include ... %}`
- 模板继承: 
  - 父模板中: `{% block <name> %} {% endblock %}`, 
  - 子模板中: `{% extends <parent-template>%}`, `{% block <name> %} {{ super() }} {% endblock %}`

扩展Flask-Bootstrap: 集成Bootstrap: 
- 初始化
```python
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap(app)
```
- 基础模板: `bootstrap/base.html`
  - blocks: `doc`, `html_attribs`, ..., `scripts`

自定义异常页
```python
@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html'), 404
```

链接: 
- `url_for(...)`: 根据URL映射`app.url_map`生成链接
```python
from flask import url_for

url_for('index')
url_for('index', _external=True)
# 动态URL: 使用关键字参数
url_for('user', name='john', page=2, version=1)
# 静态资源: 默认/static目录
url_for('static', filename='css/styles.css', _external=True)
```

扩展Flask-Moment: 本地化日期和时间
- 依赖: jQuery.js, Moment.js
```python
from flask_moment import Moment
# 初始化
moment = Moment(app)
```
```html
<!-- 导入Momemnt.js库 -->
{{ moment.include_moment() }}
{{ moment.locale('es') }}

<!-- current_time: 传入模板的值 -->
{{ moment(current_time).fromNow(refresh=True) }}
```

# 页面表单
扩展Flask-WTF: WTForms package 

配置: 使用密钥避免CSRF攻击
```python
app.config['SECRET_KEY'] = 'hard to guess string'
```

表单类
```python
from flask_wtf import FlaskForm              # 表单类
from wtforms import StringField, SubmitField # 字段
from wtforms.validators import DataRequired  # 校验器

class NameForm(FlaskForm):
  name = StringField('What is your name?', validators=[DataRequired()])
  submit = SubmitField('Submit')
```

模板中使用
```html
<!-- 表单字段是可调用的 -->
<form method="POST">
  {{ form.hidden_tag() }} <!-- 隐藏字段 -->
  {{ form.name.label }} {{ form.name(id='my-text-field') }} <!-- 传递id, class属性 -->
  {{ form.submit() }}
</form>
```
```html
<!-- 使用Bootstrap预定义表单形式渲染整个表单 -->
{% import "bootstrap/wtf.html" as wtf %}
{{ wtf.quick_form(form) }}
```

视图函数中使用
```python
@app.route('/', methods=['GET', 'POST'])
def index():
  name = None
  form = NameForm()
  if form.validate_on_submit(): # 表单提交, 通过校验
    name = form.name.data # 表单中字段
    form.name.data = ''
  return render_template('index.html', form=form, name=name)
```

消息闪烁(message flashing)
```python
from flask import flask

# 视图函数中
flash('message')
``` 
```html
<!-- 模板中 -->
{% for message in get_flashed_messages() %}
  {{ message }}
{% endfor %}
```

# 数据库
扩展Flask-SQLAlchemy: 集成SQLAlchemy
- 数据库URL
```python
# MySQL 
mysql://username:password@hostname/database
# Postgres 
postgresql://username:password@hostname/database
# SQLite (Linux, macOS) 
sqlite:////absolute/path/to/database
# SQLite (Windows) 
sqlite:///c:/absolute/path/to/database
```
- 配置
```python
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@hostname/database'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
```

模型定义
```python
class Role(db.Model):                           # 模型类
  __tablename__ = 'roles'                       # 表名
  id = db.Column(db.Integer, primary_key=True)  # 字段: 类型, 选项
  name = db.Column(db.String(64), unique=True)
  
  users = db.relationship('User', backref='role')              # 关系

  def __repr__(self):
    return '<Role %r>' % self.name

class User(db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(64), unique=True, index=True)
  
  role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))    # 外键

  def __repr__(self):
    return '<User %r>' % self.username
```

关系:
- 类型: one-to-many, one-to-one, many-to-one, many-to-many
- 选项
  - `backref`: 定义关系的反方向, 例`backref='role'`在`User`模型中添加`role`属性
  - `primaryjoin`: 显示指定两个模型的联接条件.
  - `lazy`: 指定如何加载相关的项.
    - `select`: 第一次访问时加载项
    - `immediate`: 加载源对象时加载项
    - `subquery`: 使用子查询立即加载项
    - `noload`: 从不加载项
    - `dynamic`: 指定加载项的查询
  - `uselist`: 设置为`False`时使用标量而不是列表
  - `order_by`: 指定关系中项的排序
  - `secondary`: 指定多对多关系中使用的关联表的名称
  - `secondaryjoin`: 指定多对多关系中次要联接条件

数据库操作
- 使用`flask shell`
```python
from hello import db

# 创建表
db.create_all()
# 删除表
db.drop_all()

# 插入, 修改, 删除
db.session.add(...)
db.session.add_all(...)
db.session.delete(...)

# 事务
db.session.commit()
db.session.rollback()

# 查询
Role.query.all()
User.query.filter_by(xxx=yyy).all()
# 查看原始SQL
str(User.query.filter_by(xxx=yyy))
# 过滤器
User.query.filter_by(xxx=yyy).first() # first
# filter(), filter_by(), limit(), offset(), order_by(), group_by()
# 执行器
# all(), first(), first_or_404(), get(), get_or_404(), count(), paginate()
```

与Python shell集成: `flask shell`
```python
@app.shell_context_processor
def make_shell_context():
  # 传入自动导入的对象
  return dict(db=db, User=User, Role=Role)
```

## 数据库迁移
扩展Flask-Migrate: Alembic的封装。

初始化
```python
from flask_migrate import Migrate

migrate = Migrate(app, db)
```

`flask db`命令
```shell
# 初始化迁移: 创建migrations目录
flask db init

# 创建Alembic迁移脚本
# manually `revision`, automatically `migrate`
flask db migrate -m "initial migration"

# 执行迁移脚本
flask db upgrade
flask db downgrade
```

# 邮件
扩展Flask-Mail: 封装`smtplib`, SMTP(Simple Mail Transfer Protocol)

初始化
```python
from flask_mail import Mail

mail = Mail(app)
```

使用
```python
from flask_mail import Message

msg = Message('test email', sender='you@example.com', recipients=['you@example.com'])
msg.body = 'This is the plain text body'
msg.html = 'This is the <b>HTML</b> body'
with app.app_context():
  mail.send(msg)
```

# 大型应用结构

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
`-- tests                      测试
    |-- __init__.py
    `-- test_basics.py
```

- 配置选项: `Config`
- 应用包
  - 单脚本应用
  - blueprint: 类似于应用, 但可以定义路由和错误处理器. 需要注册到应用中.
```python
# app/main/__init__.py
from flask import Blueprint

main = Blueprint('main', __name__)

from . import views, errors

# app/__init__.py
def create_app(config_name): # 应用工厂
  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)

  return app

# app/main/views.py
@main.route('/') # blueprint中路由
def index():
  return render_template('index.html')
```
- 应用脚本`main.py`: 
  - 定义应用实例`app`
  - 定义数据迁移
  - 定义`flask shell`脚本上下文处理器: `@app.shell_context_processor`, 注入`db`等 
  - 定义命令行命令: `@app.cli.command()`, 例如执行单元测试`test`
```python
@app.shell_context_processor
def make_shell_context():
  return dict(db=db, User=User, Role=Role)
```
```shell
# 环境变量
export FLASK_APP=main.py
export FLASK_DEBUG=1
```
- 依赖
```shell
pip freeze >requirements.txt
```
- 单元测试: `unittest`
```python
# main.py
@app.cli.command() # 自定义命令
def test():
  """Run the unit tests."""
  import unittest
  tests = unittest.TestLoader().discover('tests')
  unittest.TextTestRunner(verbosity=2).run(tests)
```
```shell
flask test
```
- 数据库: 使用Flask-SQLAlchemy, Flask-Migrate
- 运行应用: 
```shell
flask run
```

# 示例应用: 社交博客

## 用户身份验证

Flask身份认证扩展:
- Flask-Login: 管理用户会话
- Werkzeug: 密码哈希和验证
- itsdangerous: 安全token生成和验证

`auth` blueprint

Flask-Login
- `UserMixin`: `class User(UserMixin, db.Model)`
  - `is_authenticated`
  - `is_active`
  - `is_anonymous`
  - `get_id()`
- `LoginManager`
  - `init_app(app)`: 初始化
  - `@login_manager.user_loader`: 加载用户
- `@login_required`: 保护路由
- `current_user`: 当前用户, 对视图和模板可用
- `login_user()`: 会话中标记为已登录
- `logout_user()`: 登出

初始化
```python
# app/__init__.py
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app(config_name):
  login_manager.init_app(app)
```

模型
```python
# app/models.py
from flask_login import UserMixin, AnonymousUserMixin
from . import login_manager

class User(UserMixin, db.Model):         # 用户
  ...

class AnonymousUser(AnonymousUserMixin): # 匿名用户
  ...

login_manager.anonymous_user = AnonymousUser

@login_manager.user_loader # 用户加载函数
def load_user(user_id):
  return User.query.get(int(user_id))
```

视图
```python
from flask_login import login_required, login_user, current_user

@app.route('/secret')
@login_required
def secret():
  return 'Only authenticated users are allowed!'

login_user(user, form.remember_me.data)
logout_user()
```

模板
```html
{% if current_user.is_authenticated %}
{% else %}
{% endif %}
```

## 用户角色

自定义权限检查装饰器:
```python
from functools import wraps
from flask import abort
from flask_login import current_user
from .models import Permission

def permission_required(permission):
  def decorator(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
      if not current_user.can(permission):
        abort(403)
      return f(*args, **kwargs)
    return decorated_function
  return decorator

def admin_required(f):
  return permission_required(Permission.ADMIN)(f)
```
使用:
```python
@main.route('/admin')
@login_required
@admin_required
def for_admins_only():
  return "For administrators!"

@main.route('/moderate')
@login_required
@permission_required(Permission.MODERATE)
def for_moderators_only():
  return "For comment moderators!"
```

应用上下文处理器
```python
# 例: 将对象传入模板, 避免每次给render_template()传入参数
# app/main/__init__.py
@main.app_context_processor
def inject_permissions():
  return dict(Permission=Permission)
```

## 用户信息

Avatars: [Gravatar](https://gravatar.com)

## 发布博客

依赖:
- Faker: 生成假信息
- Markdown支持
  - Flask-PageDown, PageDown: client-side markdown-to-html converter(JavaScript)
  - Markdown: server-side markdown-to-html converter(Python)
  - Bleach: HTML santitizer(Python)

Flask-SQLAlchemy分页: 
```python
# 返回Pagination
paginate(page, per_page, error_out)
```

定义Jinja2宏: 处理分页
```html
<!-- app/templates/_macros.html -->
{% macro pagination_widget(pagination, endpoint) %}
{% endmacro %}
```

扩展Flask-PageDown
- 初始化
```python
from flask_pagedown import PageDown

pagedown = PageDown()

def create_app(config_name):
  pagedown.init_app(app)
```
```html
<!-- 模板声明 -->
{{ pagedown.include_pagedown() }}
```

SQLAlchemy事件
```python
db.event.listen(Post.body, 'set', Post.on_changed_body)
```

## 关注

SQLAlchemy多对多关系例: 学生课程注册
```python
registrations = db.Table('registrations',                            # 中间表
  db.Column('student_id', db.Integer, db.ForeignKey('students.id')), # 外键
  db.Column('class_id', db.Integer, db.ForeignKey('classes.id')))

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

自引用关系:
```python
class Follow(db.Model):   # 关注关系
  __tablename__ = 'follows'
  follower_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True) # 关注人
  followed_id = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=True) # 被关注人
  timestamp = db.Column(db.DateTime, default=datetime.utcnow)

class User(db.Model):     # 用户
  # ...
  followed = db.relationship('Follow',               # 我关注的人
    foreign_keys=[Follow.follower_id],               # 外键: 我是关注人
    backref=db.backref('follower', lazy='joined'),   # 回引: 
                                  # joined: 联接时相关对象立即返回, 单个查询, 例user.followed().all()
                                  # select: 默认值, 第一次访问时, 独立的查询
    lazy='dynamic',                                  # 关系属性返回查询的对象而不是项
    cascade='all, delete-orphan')                    # 级联: 父对象上的动作如何传播到相关对象
                  # delete-orphan: 默认级联将相关对象的外键设置为NULL, 删除孤儿直接删除相关对象
                  # all: 除delete-orphan的所有级联选项
  
  followers = db.relationship('Follow',              # 关注我的人
    foreign_keys=[Follow.followed_id],               # 外键: 我是被关注人
    backref=db.backref('followed', lazy='joined'),
    lazy='dynamic',
    cascade='all, delete-orphan')
```

查询我关注的人的帖子: 联接join
```python
# in User
db.session.query(Post)                                # 查询帖子
  .select_from(Follow)                                # 查询关注关系
  .filter_by(follower_id=self.id)                       # 过滤: 用户是关注人
  .join(Post, Follow.followed_id == Post.author_id)   # 联接: 帖子的作者是被关注人

# 简化
Post.query                                            # 查询帖子
  .join(Follow, Follow.followed_id == Post.author_id) # 联接: 帖子的作者是被关注人
  .filter(Follow.follower_id == self.id)                # 过滤: 用户是关注人
```

## 博客评论

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

Jinja2的`set`指令
```html
<!-- app/templates/moderate.html -->
{% set moderate = True %}
{% include '_comments.html' %} <!-- moderate在_comments.html中可用 -->
```

# RESTful API

API版本:
- `/api/v1/posts`
- `/api/v2/posts`

in Flask:
- `request.get_json()`
- `jsonify()`
- `request.accept_mimetypes.accept_json`

`api` blueprint
- 初始化
```python
# app/api/__init__.py
from flask import Blueprint

api = Blueprint('api', __name__)

from . import authentication, posts, users, comments, errors
```
- 注册
```python
# app/__init__.py
def create_app(config_name):
  # ...
  from .api import api as api_blueprint
  app.register_blueprint(api_blueprint, url_prefix='/api/v1')
```

JSON
```python
# 判断请求是否接受JSON
request.accept_mimetypes.accept_json

from flask import jsonify
jsonify()

# 序列化/反序列化
class Post(db.Model):
  # ...
  def to_json(self):
    pass
  
  @staticmethod
  def from_json(json_post):
    pass
```

扩展: Flask-HTTPAuth
- 初始化
```python
# app/api/authentication.py
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth() # HTTP Basic认证

# 验证回调
@auth.verify_password
def verify_password(email, password):
  if email == '':
    return False
  user = User.query.filter_by(email = email).first()
  if not user:
    return False
  g.current_user = user
  return user.verify_password(password)
```

TODO: Swagger文档

测试: HTTPie

# 测试

覆盖测试: `coverage`

Flask测试客户端
```python
app.test_client(use_cookies=True)
  # GET
  .get('/')
  # POST
  .post('/auth/register', headers={}, data={}, follow_redirects=True)

# 规避Flask-WTF的CSRF保护
WTF_CSRF_ENABLED = False

# JSON响应
import json
json.loads(response.get_data(as_text=True))
```

端到端测试: Selenium, Playwright
```python
# 已废弃
shutdown = request.environ.get('werkzeug.server.shutdown')
# 改为使用daemon线程
```

# 性能

记录慢查询
```python
# app/main/views.py
from flask_sqlalchemy.record_queries import get_recorded_queries # Debug模式默认开启

@main.after_app_request
def after_request(response):  
  for query in get_recorded_queries():
    current_app.logger.debug(
        'Query: %s\nParameters: %s\nDuration: %fs\nContext: %s\n'
        % (query.statement, query.parameters, query.duration,
           query.location))
  return response

# 生产环境中记录查询
SQLALCHEMY_RECORD_QUERIES = True
```

源码profiling
```python
# Werkzeug对每个请求开启Python profiler
from werkzeug.middleware.profiler import ProfilerMiddleware
app.wsgi_app = ProfilerMiddleware(app.wsgi_app, restrictions=[length],
                                    profile_dir=profile_dir)
```

# 部署

- 部署命令
- 日志: `logging` `app.logger.addHandler(...)`, JSON格式`python-json-logger`
- 云部署, 例: Heroku
- 扩展: Flask-SSLify, 将HTTP请求重定向到HTTPS请求
```python
from flask_sslify import SSLify

sslify = SSLify(app)
```
- 处理反向代理
```python
# https://flask.palletsprojects.com/en/stable/deploying/proxy_fix/
from werkzeug.middleware.proxy_fix import ProxyFix

app.wsgi_app = ProxyFix(
    app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1
)
```
- 生产级Web服务器: Gunicorn, uWSGI
- 进程监控工具: Supervisor
- 处理环境变量: `.env`, `python-dotenv`


# 扩展
* https://flask.palletsprojects.com/en/stable/extensions/

- Flask-Babel: Internationalization and localization support
- Marshmallow: Serialization and deserialization of Python objects, useful for API resource representations
- Celery: Task queue for processing background jobs
- Frozen-Flask: Conversion of a Flask application to a static website
- Flask-DebugToolbar: In-browser debugging tools
- Flask-Assets: Merging, minifying, and compiling of CSS and JavaScript assets
- Flask-Session: Alternative implementation of user sessions that use server-side storage
- Flask-SocketIO: Socket.IO server implementation with support for WebSocket and long-polling