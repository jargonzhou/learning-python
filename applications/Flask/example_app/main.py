# from flask import Flask, request, abort, current_app, jsonify
# # 全局上下文对象: current_app, g, request, session

# app = Flask(__name__)

# # 请求hook
# @app.before_request
# def before_request():
#     print("before request")

# @app.route("/")
# def hello_world():
#     user_agent = request.headers.get('User-Agent') # 请求头
#     return f"<p>Hello, World! - {user_agent}</p>"

# @app.route("/cookie")
# def set_cookie():
#     # make_response()
#     response = app.make_response("<h1>Cookie Set</h1>")
#     response.set_cookie('username', 'example_user', max_age=60*60*24)
#     return response

# @app.route("/error")
# def error():
#     # string, status code, headers
#     return "<h1>Bad Request</h1>", 400, {
#         'Content-Type': 'text/html',
#         'X-Error': 'Bad Request'
#     }

# # 重定向
# @app.route("/redirect")
# def redirect_example():
#     return app.redirect("/")

# # 错误处理
# @app.route("/abort")
# def abort_example():
#     abort(400, {'X-Error': 'Bad Request'})
# # 错误处理: JSON
# @app.errorhandler(400)
# def bad_request(e):
#     return jsonify({"error": "Bad Request", "message": str(e)}), 400

# # response with JSON
# @app.route("/user")
# def get_user():
#     return {
#         'name': 'Example User',
#         'age': 28
#     }


import os
from app import create_app, db
from app.models import User, Role
from flask_migrate import Migrate
from flask_login import login_required

# Flask应用实例
app = create_app(os.getenv('FLASK_CONFIG') or 'default')

@app.route("/secret")
@login_required
def secret():
    return "只有登录用户才能访问的秘密页面！"

# 数据迁移扩展
migrate = Migrate(app, db)

# flash shell上下文处理器
@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'User': User,
        'Role': Role
    }

# unit test launcher command: flask test
@app.cli.command()
def test():
    """运行单元测试"""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)