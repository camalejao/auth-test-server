from flask import Blueprint, request
from auth.settings import basic_auth, digest_auth, token_auth

protocol_api = Blueprint('protocol_api', __name__)

@protocol_api.route('/protocol-none', methods=['POST'])
def protocol_none():
    return print_json_ok()

@protocol_api.route('/protocol-basic', methods=['POST'])
@basic_auth.login_required
def protocol_basic():
    return print_json_ok()

@protocol_api.route('/protocol-digest', methods=['POST'])
@digest_auth.login_required
def protocol_digest():
    return print_json_ok()

@protocol_api.route('/protocol-token', methods=['POST'])
@token_auth.login_required
def protocol_token():
    return print_json_ok()

def print_json_ok():
    data = request.get_json()
    print(data)
    return 'OK'
