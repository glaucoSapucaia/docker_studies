# importando libs
import flask
import requests

from flask import request, json, jsonify

# instanciando app
app = flask.Flask(__name__)
app.config['DEBUG'] = True

# routes
@app.route('/', methods=['GET'])
def index():
    # API que retorna dados aleatorios de usuarios
    data = requests.get('https://randomuser.me/api')
    return data.json()

# verificando acesso do app
if __name__ == '__main__':
    # execytando app
    app.run(host='0.0.0.0', debug=True, port='5000')
