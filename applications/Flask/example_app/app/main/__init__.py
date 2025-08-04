# main blueprints

from flask import Blueprint
from ..models import Permission

# blueprint: 名称为main, 所在的模块或包为当前模块
main = Blueprint('main', __name__)

# autopep8: off

# 视图/路由, 错误处理器
from . import views, errors

# 将权限类添加到模板上下文
@main.app_context_processor
def inject_permissions():
  return dict(Permission=Permission)

# autopep8: on