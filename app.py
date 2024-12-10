from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth, HTTPDigestAuth, HTTPTokenAuth

app = Flask(__name__)
app.secret_key = "segredo"

basic_auth = HTTPBasicAuth()
digest_auth = HTTPDigestAuth()
token_auth = HTTPTokenAuth('Bearer')

users = {
    "joao": {
        "password": "123",
        "token": "t0k3n-joao",
        "secret": "aha"
    },
    "maria": {
        "password": "456",
        "token": "t0k3n-maria",
        "secret": "hoho"
    },
}

@basic_auth.verify_password
def verify_password(username, password):
    if username in users and password == users[username]["password"]:
        return username

@digest_auth.get_password
def get_password(username):
    if username in users.keys():
        p = users[username]["password"]
        return p

@token_auth.verify_token
def verify_token(token):
    for user in users.keys():
        if users[user]["token"] == token:
            return user

@app.route('/hello-basic')
@basic_auth.login_required
def hello():
    return 'Hello, %s!' % basic_auth.current_user()

@app.route('/hello-digest')
@digest_auth.login_required
def hello_digest():
    return 'Hello, %s!' % digest_auth.current_user()

@app.route('/hello-token')
@token_auth.login_required
def hello_token():
    return 'Hello, %s!' % token_auth.current_user()

@app.route('/oauth', methods=['POST'])
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

@app.route('/protocol-none', methods=['POST'])
def protocol_none():
    data = request.get_json()
    print(data)
    return 'OK'

@app.route('/protocol-basic', methods=['POST'])
@basic_auth.login_required
def protocol_basic():
    data = request.get_json()
    print(data)
    return 'OK'

@app.route('/protocol-digest', methods=['POST'])
@digest_auth.login_required
def protocol_digest():
    data = request.get_json()
    print(data)
    return 'OK'

@app.route('/protocol-token', methods=['POST'])
@token_auth.login_required
def protocol_token():
    data = request.get_json()
    print(data)
    return 'OK'

@app.route('/protocol-oauth', methods=['POST'])
@token_auth.login_required
def protocol_oauth():
    data = request.get_json()
    print(data)
    return 'OK'

@app.route('/')
def root():
    return 'Roots, bloody roots!'

if __name__ == '__main__':
    app.run(port=8080)
