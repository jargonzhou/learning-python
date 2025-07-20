# 身份验证blueprint

from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views