from flask_login import login_required
from flask_migrate import Migrate, upgrade
from app.models import Comment, Follow, Permission, Post, User, Role
from app import create_app, db, main
import os
import click
import sys

# 覆盖测试
COV = None
if os.environ.get('FLASK_COVERAGE'):
  import coverage
  COV = coverage.coverage(branch=True, include='app/*')
  COV.start()


# Flask应用实例
app = create_app(os.getenv('FLASK_CONFIG') or 'default')


@app.route("/secret")
@login_required
def secret():
  return "只有登录用户才能访问的秘密页面！"


# 数据迁移扩展
migrate = Migrate(app, db)


@app.shell_context_processor  # flash shell上下文处理器
def make_shell_context():
  return dict(db=db, User=User, Follow=Follow, Role=Role, Permission=Permission,
              Post=Post, Comment=Comment)


@app.cli.command()  # unit test launcher command: flask test
@click.option('--coverage/--no-coverage', default=False,
              help='Run tests under code coverage.')
@click.argument('test_names', nargs=-1)
def test(coverage, test_names):
  if coverage and not os.environ.get('FLASK_COVERAGE'):
    import subprocess
    os.environ['FLASK_COVERAGE'] = '1'
    sys.exit(subprocess.call(sys.argv))

  import unittest
  if test_names:
    tests = unittest.TestLoader().loadTestsFromNames(test_names)
  else:
    tests = unittest.TestLoader().discover('tests')
  unittest.TextTestRunner(verbosity=2).run(tests)

  if COV:
    COV.stop()
    COV.save()
    print('Coverage Summary:')
    COV.report()
    basedir = os.path.abspath(os.path.dirname(__file__))
    covdir = os.path.join(basedir, 'tmp/coverage')
    COV.html_report(directory=covdir)
    print('HTML version: file://%s/index.html' % covdir)
    COV.erase()


@app.cli.command()
def deploy():
  upgrade()

  Role.insert_roles()


@app.cli.command()
@click.option('--length', default=25,
              help='Number of functions to include in the profiler report.')
@click.option('--profile-dir', default=None,
              help='Directory where profiler data files are saved.')
# profile
def profile(length, profile_dir):
  """Start the application under the code profiler."""
  # https://werkzeug.palletsprojects.com/en/stable/middleware/profiler/
  from werkzeug.middleware.profiler import ProfilerMiddleware
  app.wsgi_app = ProfilerMiddleware(app.wsgi_app, restrictions=[length],
                                    profile_dir=profile_dir)

  # WARNING
  # Ignoring a call to 'app.run()' that would block the current 'flask' CLI command.
  #  Only call 'app.run()' in an 'if __name__ == "__main__"' guard.
  # https://github.com/pallets/flask/issues/2776
  del os.environ["FLASK_RUN_FROM_CLI"]
  app.run(port=15000)
