from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_pagedown import PageDown


from config import config

# 扩展实例
bootstrap = Bootstrap()
moment = Moment()
mail = Mail()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
pagedown = PageDown()


def create_app(config_name):
  """Flask应用工厂函数"""
  app = Flask(__name__)
  # 加载配置
  conf = config[config_name]
  app.config.from_object(conf)
  conf.init_app(app)

  # 扩展配置
  # app.config['BOOTSTRAP_SERVE_LOCAL'] = True  # bootstrap使用本地资源

  bootstrap.init_app(app)
  moment.init_app(app)
  mail.init_app(app)
  db.init_app(app)
  login_manager.init_app(app)
  pagedown.init_app(app)

  # 注册blueprints
  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)
  from .auth import auth as auth_blueprint
  app.register_blueprint(auth_blueprint, url_prefix='/auth')
  from .api import api as api_blueprint
  app.register_blueprint(api_blueprint, url_prefix='/api/v1')

  return app
