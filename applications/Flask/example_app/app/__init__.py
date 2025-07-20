from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from config import config

# 扩展实例
bootstrap = Bootstrap()
moment = Moment()
mail = Mail()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app(config_name):
  """Flask应用工厂函数"""
  app = Flask(__name__)
  # 加载配置
  app.config.from_object(config[config_name])

  # 扩展配置
  bootstrap.init_app(app)
  moment.init_app(app)
  mail.init_app(app)
  db.init_app(app)
  login_manager.init_app(app)

  # 注册blueprints
  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)
  from .auth import auth as auth_blueprint
  app.register_blueprint(auth_blueprint, url_prefix='/auth')

  return app