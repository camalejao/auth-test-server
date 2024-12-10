from flask import Blueprint, request, jsonify
from auth.users import users

auth_api = Blueprint('auth_api', __name__)

@auth_api.route('/oauth', methods=['POST'])
def oauth():
    grant_type = request.form.get('grant_type')
    if grant_type != 'client_credentials':
        return jsonify({'error': 'unsupported_grant_type'}), 401

    client_id = request.form.get('client_id')
    client_secret = request.form.get('client_secret')

    if client_id in users.keys() and client_secret == users[client_id]["secret"]:
        return jsonify({
            'access_token': users[client_id]["token"],
            'token_type': 'Bearer'
        })
