# 视图/路由

from datetime import datetime
from sqlite3.dbapi2 import Timestamp
from flask import current_app, render_template, redirect, url_for, flash, request, abort
from flask_login import current_user, login_required

from ..decorators import admin_required, permission_required
from . import main  # blueprint
from .forms import EditProfileForm, NameForm, EditProfileAdminForm, PostForm, CommentForm
from .. import db
from ..models import Permission, User, Role, Post, Comment
from flask_sqlalchemy.record_queries import get_recorded_queries


@main.after_app_request
def after_request(response):  # 请求后处理器
  for query in get_recorded_queries():
    # if query.duration >= current_app.config['APP_SLOW_DB_QUERY_TIME']:
    current_app.logger.debug(
        'Query: %s\nParameters: %s\nDuration: %fs\nContext: %s\n'
        % (query.statement, query.parameters, query.duration,
           query.location))
  return response

# deprecated: https://github.com/pallets/werkzeug/issues/1752
#
# @main.route('/shutdown', methods=['GET'])
# def server_shutdown():  # 关闭服务
#   if not current_app.testing:
#     abort(404)
#   shutdown = request.environ.get('werkzeug.server.shutdown')
#   if not shutdown:
#     abort(500)
#   shutdown()
#   return 'Shutting down...'

################################################################################
# 帖子
################################################################################


@main.route('/', methods=['GET', 'POST'])  # 主页
def index():
  form = PostForm()
  if current_user.can(Permission.WRITE) and form.validate_on_submit():
    post = Post(body=form.body.data, author=current_user._get_current_object())
    db.session.add(post)
    db.session.commit()
    return redirect(url_for('.index'))
  # 分页
  page = request.args.get('page', 1, type=int)
  pagination = Post.query.order_by(Post.timestamp.desc()).paginate(
      page=page, per_page=current_app.config['APP_POSTS_PER_PAGE'],
      error_out=False)
  posts = pagination.items
  return render_template('index.html', form=form, posts=posts, pagination=pagination)


@main.route('/post/<int:id>', methods=['GET', 'POST'])  # 帖子, 评论表单
def post(id):
  post = Post.query.get_or_404(id)
  form = CommentForm()
  if form.validate_on_submit():
    comment = Comment(body=form.body.data,
                      post=post,
                      author=current_user._get_current_object())
    db.session.add(comment)
    db.session.commit()
    flash('Your comment has been published.')
    return redirect(url_for('.post', id=post.id, page=-1))
  page = request.args.get('page', 1, type=int)
  if page == -1:
    page = (post.comments.count() - 1) // \
        current_app.config['APP_COMMENTS_PER_PAGE'] + 1
  pagination = post.comments.order_by(Comment.timestamp.asc()).paginate(
      page=page, per_page=current_app.config['APP_COMMENTS_PER_PAGE'],
      error_out=False)
  comments = pagination.items
  return render_template('post.html', posts=[post], form=form,
                         comments=comments, pagination=pagination)


@main.route('/edit/<int:id>', methods=['GET', 'POST'])  # 编辑帖子
@login_required
def edit_post(id):
  post = Post.query.get_or_404(id)
  if current_user != post.author and \
          not current_user.can(Permission.ADMIN):
    abort(403)
  form = PostForm()
  if form.validate_on_submit():
    post.body = form.body.data
    db.session.add(post)
    db.session.commit()
    flash('The post has been updated.')
    return redirect(url_for('.post', id=post.id))
  form.body.data = post.body
  return render_template('edit_post.html', form=form)


@main.route('/moderate')  # 修改评论
@login_required
@permission_required(Permission.MODERATE)
def moderate():
  page = request.args.get('page', 1, type=int)
  pagination = Comment.query.order_by(Comment.timestamp.desc()).paginate(
      page=page, per_page=current_app.config['APP_COMMENTS_PER_PAGE'],
      error_out=False)
  comments = pagination.items
  return render_template('moderate.html', comments=comments,
                         pagination=pagination, page=page)


@main.route('/moderate/enable/<int:id>')  # 取消评论
@login_required
@permission_required(Permission.MODERATE)
def moderate_enable(id):
  comment = Comment.query.get_or_404(id)
  comment.disabled = False
  db.session.add(comment)
  db.session.commit()
  return redirect(url_for('.moderate', page=request.args.get('page', 1, type=int)))


@main.route('/moderate/disable/<int:id>')  # 开启评论
@login_required
@permission_required(Permission.MODERATE)
def moderate_disable(id):
  comment = Comment.query.get_or_404(id)
  comment.disabled = True
  db.session.add(comment)
  db.session.commit()
  return redirect(url_for('.moderate', page=request.args.get('page', 1, type=int)))


################################################################################
# 用户的profile页面
################################################################################

@main.route('/user/<username>')  # 按用户名称查询用户
def user(username):
  user = User.query.filter_by(username=username).first_or_404()
  page = request.args.get('page', 1, type=int)
  pagination = user.posts.order_by(Post.timestamp.desc()).paginate(
      page=page, per_page=current_app.config['APP_POSTS_PER_PAGE'],
      error_out=False)
  posts = pagination.items
  return render_template('user.html', user=user, posts=posts, pagination=pagination)


@main.route('/edit-profile', methods=['GET', 'POST'])  # profile表单
@login_required
def edit_profile():
  form = EditProfileForm()
  if form.validate_on_submit():
    current_user.name = form.name.data
    current_user.location = form.location.data
    current_user.about_me = form.about_me.data
    db.session.add(current_user._get_current_object())
    db.session.commit()
    flash('Your profile has been update.')
    return redirect(url_for('.user', username=current_user.username))
  form.name.data = current_user.name
  form.location.data = current_user.location
  form.about_me.data = current_user.about_me
  return render_template('edit_profile.html', form=form)


@main.route('/edit-profile/<int:id>', methods=['GET', 'POST'])  # 编辑某个profile
@login_required
@admin_required
def edit_profile_admin(id):
  user = User.query.get_or_404(id)
  form = EditProfileAdminForm(user=user)
  if form.validate_on_submit():
    user.email = form.email.data
    user.username = form.username.data
    user.confirmed = form.confirmed.data
    user.role = Role.query.get(form.role.data)
    user.name = form.name.data
    user.location = form.location.data
    user.about_me = form.about_me.data
    db.session.add(user)
    db.session.commit()
    flash('The profile has been updated.')
    return redirect(url_for('.user', username=user.username))
  form.email.data = user.email
  form.username.data = user.username
  form.confirmed.data = user.confirmed
  form.role.data = user.role_id
  form.name.data = user.name
  form.location.data = user.location
  form.about_me.data = user.about_me
  return render_template('edit_profile.html', form=form, user=user)


################################################################################
# 关注
################################################################################
@main.route('/follow/<username>')  # 关注
@login_required
@permission_required(Permission.FOLLOW)
def follow(username):
  user = User.query.filter_by(username=username).first()
  if user is None:
    flash('Invalid user.')
  if current_user.is_following(user):
    flash('You are already following this user.')
    return redirect(url_for('.user', username=username))
  current_user.follow(user)
  db.session.commit()
  flash('You are now following %s.' % username)
  return redirect(url_for('.user', username=username))


@main.route('/unfollow/<username>')  # 取消关注
@login_required
@permission_required(Permission.FOLLOW)
def unfollow(username):
  user = User.query.filter_by(username=username).first()
  if user is None:
    flash('Invalid user.')
    return redirect(url_for('.index'))
  if not current_user.is_following(user):
    flash('You are not following this user.')
    return redirect(url_for('.user', username=username))
  current_user.unfollow(user)
  db.session.commit()
  flash('You are not following %s anymore.' % username)
  return redirect(url_for('.user', username=username))


@main.route('/followers/<username>')  # 关注xxx的
def followers(username):
  user = User.query.filter_by(username=username).first()
  if user is None:
    flash('Invalid user.')
    return redirect(url_for('.index'))
  page = request.args.get('page', 1, type=int)
  pagination = user.followers.paginate(
      page=page, per_page=current_app.config['APP_FOLLOWERS_PERPAGE'], error_out=False)
  follows = [{'user': item.follower, 'timestamp': item.timestamp}
             for item in pagination.items]
  return render_template('followers.html', user=user, title='Followers of',
                         endpoint='.followers', pagination=pagination,
                         follows=follows)


@main.route('/followed_by/<username>')  # xxx关注的
def followed_by(username):
  user = User.query.filter_by(username=username).first()
  if user is None:
    flash('Invalid user.')
    return redirect(url_for('.index'))
  page = request.args.get('page', 1, type=int)
  pagination = user.followed.paginate(
      page=page, per_page=current_app.config['APP_FOLLOWERS_PERPAGE'],
      error_out=False)
  follows = [{'user': item.followed, 'timestamp': item.timestamp}
             for item in pagination.items]
  return render_template('followers.html', user=user, title="Followed by",
                         endpoint='.followed_by', pagination=pagination,
                         follows=follows)
