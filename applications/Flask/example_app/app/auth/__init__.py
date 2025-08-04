# 身份验证blueprint

from flask import Blueprint

auth = Blueprint('auth', __name__)

# autopep8: off
from . import views
# autopep8: on
