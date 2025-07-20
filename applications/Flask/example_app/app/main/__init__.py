# main blueprints

from flask import Blueprint

# blueprint: 名称为main, 所在的模块或包为当前模块
main = Blueprint('main', __name__)

# 视图/路由, 错误处理器
from . import views, errors