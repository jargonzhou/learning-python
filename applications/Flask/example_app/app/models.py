# 数据模型

import bleach
from markdown import markdown
from app import db

from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import UserMixin, AnonymousUserMixin

from . import login_manager, exceptions

# deprecated: https://itsdangerous.palletsprojects.com/en/stable/changes/
# from itsdangerous import TimedJSONWebSignatureSerializer as Serializer # JWT
from itsdangerous.url_safe import URLSafeTimedSerializer as Serializer
from flask import current_app, request, url_for

from datetime import datetime, timezone
import hashlib


################################################################################
# 用户, 角色, 权限
################################################################################

@login_manager.user_loader
def load_user(user_id):
  """登录管理器的加载用户函数"""
  return User.query.get(int(user_id))

#######
# 关注
#######


class Follow(db.Model):
  __tablename__ = 'follows'
  # follower关注followed
  # 关注人
  follower_id = db.Column(db.Integer, db.ForeignKey('users.id'),
                          primary_key=True)
  # 被关注人
  followed_id = db.Column(db.Integer, db.ForeignKey('users.id'),
                          primary_key=True)
  # 关注时间
  timestamp = db.Column(db.DateTime, default=datetime.now(timezone.utc))


class User(UserMixin, db.Model):
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key=True)
  # 用户名
  username = db.Column(db.String(64), unique=True,
                       nullable=False, index=True, default='')
  # 邮箱
  email = db.Column(db.String(64), unique=True,
                    nullable=False, index=True, default='')
  # 密码
  password_hash = db.Column(db.String(256), nullable=False)
  # 是否已确认邮件
  confirmed = db.Column(db.Boolean, default=False, nullable=False)

  # profile
  name = db.Column(db.String(64))
  location = db.Column(db.String(64))
  about_me = db.Column(db.Text())
  member_since = db.Column(db.DateTime(), default=datetime.now(timezone.utc))
  last_seen = db.Column(db.DateTime(), default=datetime.now(timezone.utc))

  # 头像
  avatar_hash = db.Column(db.String(32))

  # 角色外键
  role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

  # 帖子关联
  posts = db.relationship('Post', backref='author', lazy='dynamic')

  # 关注关系关联
  # 我关注的关注关系
  followed = db.relationship(
      'Follow',
      foreign_keys=[Follow.follower_id],  # 这里引用了Follow
      # joined: 联接时相关对象立即返回, 单个查询
      # select: 默认值, 第一次访问时, 独立的查询
      backref=db.backref('follower', lazy='joined'),
      # 关系属性返回查询的对象而不是项
      lazy='dynamic',
      # delete-orphan: 默认级联将相关对象的外键设置为NULL, 删除孤儿直接删除相关对象
      # all: 除delete-orphan的所有级联选项
      cascade='all, delete-orphan')
  # 关注我的关注关系
  followers = db.relationship(
      'Follow', foreign_keys=[Follow.followed_id],
      backref=db.backref('followed', lazy='joined'),
      lazy='dynamic',
      cascade='all, delete-orphan')

  # 帖子评论关联
  comments = db.relationship('Comment', backref='author', lazy='dynamic')

  def __init__(self, **kwargs):
    super(User, self).__init__(**kwargs)
    if self.role is None:
      if self.email == current_app.config['APP_ADMIN']:
        self.role = Role.query.filter_by(name='Administrator').first()
      if self.role is None:
        self.role = Role.query.filter_by(default=True).first()

    # 自己关注自己
    self.follow(self)

  @staticmethod
  def add_self_follows():
    for user in User.query.all():
      if not user.is_following(user):
        user.follow(user)
        db.session.add(user)
        db.session.commit()

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
    return s.dumps({'confirm': self.id})

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

  def do_confirm(self):  # 绕过邮件确认
    self.confirmed = True
    db.session.add(self)

  def can(self, perm):
    return self.role is not None and self.role.has_permission(perm)

  def is_administrator(self):
    return self.can(Permission.ADMIN)

  def ping(self):
    """refresh user's last visit time"""
    self.last_seen = datetime.now(timezone.utc)
    db.session.add(self)
    db.session.commit()

  def change_email(self, token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
      data = s.loads(token.encode('utf-8'))
    except:
      return False
    if data.get('change_email') != self.id:
      return False
    new_email = data.get('new_email')
    if new_email is None:
      return False
    if self.query.filter_by(email=new_email).first() is not None:
      return False
    self.email = new_email
    self.avatar_hash = self.gravatar_hash()
    db.session.add(self)
    return True

  def gravatar_hash(self):
    """根据邮箱生成头像hash"""
    return hashlib.md5(self.email.lower().encode('utf-8')).hexdigest()

  def gravatar(self, size=100, default='identicon', rating='g'):
    """头像"""
    if request.is_secure:
      url = 'https://secure.gravatar.com/avatar'
    else:
      url = 'http://www.gravatar.com/avatar'
    hash = self.avatar_hash or self.gravatar_hash()
    return '{url}/{hash}?s={size}&d={default}&r={rating}'.format(
        url=url, hash=hash, size=size, default=default, rating=rating)

  def is_following(self, user):
    """是否关注别人"""
    if user.id is None:
      return False
    # 我关注的关系中: 被关注者是别人
    return self.followed.filter_by(followed_id=user.id).first() is not None

  def is_followed_by(self, user):
    """是否被别人关注"""
    if user.id is None:
      return False
    # 关注我的关注关系中: 关注者是别人
    return self.followers.filter_by(follower_id=user.id).fist() is not None

  def follow(self, user):
    """关注别人"""
    if not self.is_following(user):
      f = Follow(follower=self, followed=user)
      db.session.add(f)

  def generate_auth_token(self, expiration):
    s = Serializer(current_app.config['SECRET_KEY'])
    return s.dumps({'id': self.id})  # .decode('utf-8')

  @staticmethod
  def verify_auth_token(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
      data = s.loads(token)
    except:
      return None
    return User.query.get(data['id'])

  def __repr__(self):
    return '<User %r>' % self.username

  def to_json(self):
    json_user = {
        'url': url_for('api.get_user', id=self.id),
        'username': self.username,
        'member_since': self.member_since,
        'last_seen': self.last_seen,
        'posts_url': url_for('api.get_user_posts', id=self.id),
        # 'followed_posts_url': url_for('api.get_user_followed_posts',
        #                               id=self.id),
        'post_count': self.posts.count()
    }
    return json_user


class AnonymousUser(AnonymousUserMixin):
  """匿名用户"""

  def can(self, permissions):
    return False

  def is_administrator(self):
    return False


# 指定匿名用户实现
login_manager.anonymous_user = AnonymousUser


class Role(db.Model):
  __tablename__ = 'roles'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(64), unique=True, nullable=False)
  # 是否默认
  default = db.Column(db.Boolean, default=False, index=True)
  # 角色的权限
  permissions = db.Column(db.Integer)

  users = db.relationship('User', backref='role', lazy='dynamic')

  @staticmethod
  def insert_roles():
    roles = {
        'User': [Permission.FOLLOW, Permission.COMMENT, Permission.WRITE],
        'Moderator': [Permission.FOLLOW, Permission.COMMENT,
                      Permission.WRITE, Permission.MODERATE],
        'Administrator': [Permission.FOLLOW, Permission.COMMENT,
                          Permission.WRITE, Permission.MODERATE,
                          Permission.ADMIN],
    }
    default_role = 'User'
    for r in roles:
      role = Role.query.filter_by(name=r).first()
      if role is None:
        role = Role(name=r)
      role.reset_permission()
      for perm in roles[r]:
        role.add_permission(perm)
      role.default = (role.name == default_role)
      db.session.add(role)
    db.session.commit()

  def __init__(self, **kwargs):
    super(Role, self).__init__(**kwargs)
    if self.permissions is None:
      self.permissions = 0

  def has_permission(self, perm):
    return self.permissions & perm == perm

  def add_permission(self, perm):
    if not self.has_permission(perm):
      self.permissions += perm

  def remove_permission(self, perm):
    if self.has_permission(perm):
      self.permissions -= perm

  def reset_permission(self):
    self.permissions = 0

  def __repr__(self):
    return '<Role %r>' % self.name


class Permission:
  FOLLOW = 1
  COMMENT = 2
  WRITE = 4
  MODERATE = 8
  ADMIN = 16

################################################################################
# 帖子
################################################################################


class Post(db.Model):
  __tablename__ = 'posts'
  id = db.Column(db.Integer, primary_key=True)
  body = db.Column(db.Text)
  body_html = db.Column(db.Text)  # markdown支持
  timestamp = db.Column(db.DateTime, index=True,
                        default=datetime.now(timezone.utc))

  # 作者外键
  author_id = db.Column(db.Integer, db.ForeignKey('users.id'))

  # 评论关联
  comments = db.relationship('Comment', backref='post', lazy='dynamic')

  @staticmethod
  def on_changed_body(target, value, oldvalue, initiator):
    allowed_tags = ['a', 'abbr', 'acronym', 'b', 'blockquote', 'code',
                    'em', 'i', 'li', 'ol', 'pre', 'strong', 'ul',
                    'h1', 'h2', 'h3', 'p']
    target.body_html = bleach.linkify(bleach.clean(
        markdown(value, output_format='html'),
        tags=allowed_tags, strip=True))

  def to_json(self):
    json_post = {
        'url': url_for('api.get_post', id=self.id),
        'body': self.body,
        'body_html': self.body_html,
        'timestamp': self.timestamp,
        'author_url': url_for('api.get_user', id=self.author_id),
        'comments_url': url_for('api.get_post_comments', id=self.id),
        'comment_count': self.comments.count()
    }
    return json_post

  @staticmethod
  def from_json(json_post):
    body = json_post.get('body')
    if body is None or body == '':
      raise exceptions.ValidationError('post does not have a body')
    return Post(body=body)


# 设置帖子body时更新body_html
db.event.listen(Post.body, 'set', Post.on_changed_body)


class Comment(db.Model):
  __tablename__ = 'comments'
  id = db.Column(db.Integer, primary_key=True)
  body = db.Column(db.Text)
  body_html = db.Column(db.Text)  # markdown支持
  timestamp = db.Column(db.DateTime, index=True,
                        default=datetime.now(timezone.utc))
  disabled = db.Column(db.Boolean)

  # 外键
  author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
  post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))

  @staticmethod
  def on_change_body(target, value, oldvalue, initiator):
    allowed_tags = ['a', 'abbr', 'acronym', 'b', 'code', 'em', 'i',
                    'strong']
    target.body_html = bleach.linkify(bleach.clean(
        markdown(value, output_format='html'),
        tags=allowed_tags, strip=True))

  def to_json(self):
    json_comment = {
        'url': url_for('api.get_comment', id=self.id),
        'post_url': url_for('api.get_post', id=self.post_id),
        'body': self.body,
        'body_html': self.body_html,
        'timestamp': self.timestamp,
        'author_url': url_for('api.get_user', id=self.author_id),
    }
    return json_comment

  @staticmethod
  def from_json(json_comment):
    body = json_comment.get('body')
    if body is None or body == '':
      raise exceptions.ValidationError('comment does not have a body')
    return Comment(body=body)


db.event.listen(Comment.body, 'set', Comment.on_change_body)
