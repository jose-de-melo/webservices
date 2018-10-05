# coding: utf-8

import json

from flask import Flask
from flask import request


app = Flask(__name__)

@app.route('/consulta/<int:valor>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def consulta(valor):
    if request.method == 'GET':
        return json.dumps({'valor' : valor})
    else:
        return json.dumps({'erro' : 'Método inválido!'})



if __name__ == "__main__":
    app.run(debug=True, port=8080)
