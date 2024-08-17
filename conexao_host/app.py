# importando libs
import flask
import requests
import flask_mysqldb

from flask import request, json, jsonify
from flask_mysqldb import MySQL

# instanciando app
app = flask.Flask(__name__)

# configurações
app.config['DEBUG'] = True
# hot.docker.internal -> indical o host local para DOCKER
app.config['MYSQL_HOST'] = 'host.docker.internal'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'flask_host'

# instanciando mysql
mysql = MySQL(app)

# routes
@app.route('/', methods=['GET'])
def index():
    # API que retorna dados aleatorios de usuarios
    data = requests.get('https://randomuser.me/api')
    return data.json()

@app.route('/inserthost', methods=['POST'])
def inserthost():
    # Retorno de dados da API
    dados = requests.get('https://randomuser.me/api').json()
    # acessando indices dos dados (json)
    username = dados['results'][0]['name']['first']

    # criando conexao
    cur = mysql.connection.cursor()
    # executando query
    cur.execute(
        """
            INSERT INTO users(name) VALUES(%s)
        """,
        (username,)
    )
    # persistindo dados
    mysql.connection.commit()

    # fechando conexao
    cur.close()

    return username

# verificando acesso do app
if __name__ == '__main__':
    # execytando app
    app.run(host='0.0.0.0', debug=True, port='5000')
