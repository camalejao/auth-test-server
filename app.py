from flask import Flask
from api import hello_api, protocol_api, auth_api

app = Flask(__name__)
app.secret_key = "segredo"

app.register_blueprint(hello_api)
app.register_blueprint(protocol_api)
app.register_blueprint(auth_api)

@app.route('/')
def root():
    return 'Roots, bloody roots!'

if __name__ == '__main__':
    app.run(port=8080)
