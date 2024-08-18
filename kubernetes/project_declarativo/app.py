# imports
import flask

from flask import Flask, render_template

# instanciando app
app = flask.Flask(__name__)

# app configs
app.config['DEBUG'] = True

# routes
@app.route('/')
def index():
    return render_template('index.html')

# execução
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port="5000")
