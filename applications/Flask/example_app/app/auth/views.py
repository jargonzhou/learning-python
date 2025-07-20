from flask import render_template, url_for, request, redirect, flash
from flask_login import login_user, logout_user, login_required, current_user

from . import auth  # auth blueprint
from .forms import LoginForm, RegisterForm

from ..models import User
from .. import db

from ..email import send_email

################################################################################
# 注册
################################################################################


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        # flash('注册成功，请登录！')

        token = user.generate_confirmation_token()
        send_email(recipient=user.email, subject='确认您的账户',
                   template='auth/email/confirm',
                   user=user, token=token)
        flash('注册成功，请检查您的邮箱以确认账户。')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)


@auth.route('/confirm/<token>')
@login_required
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for('main.index'))
    if current_user.confirm(token):
        db.session.commit()
        flash('您的账户已成功确认！')
    else:
        flash('无效或过期的确认令牌。')
    return redirect(url_for('main.index'))


@auth.route('/resend_confirmation')
@login_required
def resend_confirmation():
    """重新发送确认邮件"""
    if current_user.confirmed:
        flash('您的账户已确认，无需再次确认。')
        return redirect(url_for('main.index'))
    token = current_user.generate_confirmation_token()
    send_email(recipient=current_user.email, subject='重新确认您的账户',
               template='auth/email/confirm',
               user=current_user, token=token)
    flash('确认邮件已重新发送，请检查您的邮箱。')
    return redirect(url_for('main.index'))

################################################################################
# 登录
################################################################################


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('main.index')
            return redirect(next)
        flash('无效的用户名或密码')
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('您已成功登出')
    return redirect(url_for('main.index'))

################################################################################
# 过滤器
################################################################################


@auth.before_app_request
def before_request():
    """在每个请求前执行"""
    if current_user.is_authenticated \
        and not current_user.confirmed \
            and request.blueprint != 'auth' \
            and request.endpoint != 'static':
        return redirect(url_for('auth.unconfirmed'))


@auth.route('/unconfirmed')
def unconfirmed():
    """未确认账户页面"""
    if current_user.is_authenticated and current_user.confirmed:
        return redirect(url_for('main.index'))
    return render_template('auth/unconfirmed.html')
