from flask_httpauth import HTTPBasicAuth, HTTPDigestAuth, HTTPTokenAuth
from auth.users import users

basic_auth = HTTPBasicAuth()
digest_auth = HTTPDigestAuth()
token_auth = HTTPTokenAuth('Bearer')

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
