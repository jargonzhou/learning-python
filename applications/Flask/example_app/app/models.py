# 数据模型

from app import db

from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import UserMixin

from . import login_manager

# deprecated: https://itsdangerous.palletsprojects.com/en/stable/changes/
# from itsdangerous import TimedJSONWebSignatureSerializer as Serializer # JWT
from itsdangerous.url_safe import URLSafeTimedSerializer as Serializer
from flask import current_app

@login_manager.user_loader
def load_user(user_id):
  """登录管理器的加载用户函数"""
  return User.query.get(int(user_id))

class User(UserMixin, db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key=True)
  # 用户名
  username = db.Column(db.String(64), unique=True, nullable=False, index=True, default='')
  # 邮箱
  email = db.Column(db.String(64), unique=True, nullable=False, index=True, default='')
  # 密码
  password_hash = db.Column(db.String(128), nullable=False)
  # 是否已确认邮件
  confirmed = db.Column(db.Boolean, default=False, nullable=False)

  role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

  @property
  def password(self):
    raise AttributeError('password is not a readable attribute')
  
  @password.setter
  def password(self, password):
    """密码: 只写属性"""
    self.password_hash = generate_password_hash(password)

  def verify_password(self, password):
    """验证密码"""
    return check_password_hash(self.password_hash, password)

  def generate_confirmation_token(self, expiration=3600):
    """生成确认令牌"""
    s = Serializer(current_app.config['SECRET_KEY'])
    return s.dumps({'confirm': str(self.id)})
  
  def confirm(self, token):
    """确认用户"""
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
      data = s.loads(token)
    except Exception:
      return False
    if data.get('confirm') != self.id:
      return False
    self.confirmed = True
    db.session.add(self)
    return True

  def __repr__(self):
    return '<User %r>' % self.username
  

class Role(db.Model):
  __tablename__ = 'roles'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(64), unique=True, nullable=False)

  users = db.relationship('User', backref='role', lazy='dynamic')

  def __repr__(self):
    return '<Role %r>' % self.name