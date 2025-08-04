from flask import Blueprint
api = Blueprint('api', __name__)

# autopep8: off
from . import authentication, posts, users, comments, errors
# autopep8: on
