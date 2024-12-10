from flask import Blueprint
from auth.settings import basic_auth, digest_auth, token_auth

hello_api = Blueprint('hello_api', __name__)

@hello_api.route('/hello-basic')
@basic_auth.login_required
def hello():
    return 'Hello, %s!' % basic_auth.current_user()

@hello_api.route('/hello-digest')
@digest_auth.login_required
def hello_digest():
    return 'Hello, %s!' % digest_auth.current_user()

@hello_api.route('/hello-token')
@token_auth.login_required
def hello_token():
    return 'Hello, %s!' % token_auth.current_user()
