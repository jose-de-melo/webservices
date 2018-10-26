# coding: utf-8

import json

from flask import Flask
from flask import request
import os

## Bibliotecas para manipular XML
from xml.dom import minidom
from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement


diretorio_padrao = './arquivos'


app = Flask(__name__)

@app.route('/arquivos/<retorno>', methods=['GET'])
def nomes_arquivos(retorno):
    if retorno == 'json':
        lista_dir = os.listdir(diretorio_padrao)
        return json.dumps({'arquivos': lista_dir})
    elif retorno == 'xml':
        lista_dir = os.listdir(diretorio_padrao)

        root = Element('arquivos')

        for file in lista_dir:
            child = SubElement(root, 'arquivo', {'text':file})

        xmlStr = ElementTree.tostring(root, 'utf-8')
        reparsed = minidom.parseString(xmlStr)
        return reparsed.toprettyxml(indent=" ", newl="\n", encoding="UTF-8")
    else:
        return json.dumps({'erro': 'Tipo de retorno invalido!'})

@app.route('/arquivos/conteudo/<nome_arquivo>', methods=['GET'])
def conteudo_arquivo(nome_arquivo):
    try:
        arquivo = open('arquivos/' + nome_arquivo, 'r')
        conteudo = arquivo.read()
        return json.dumps({'status': 200, 'conteudo': conteudo})
    except:
        return json.dumps({'status': 771,'erro': 'O arquivo não existe!'})

@app.route('/arquivos', methods=['DELETE'])
def remover_todos_arquivos():
    lista_dir = os.listdir(diretorio_padrao)
    pathArquivo = ''
    for arq in lista_dir:
        pathArquivo = diretorio_padrao + '/' + arq
        if os.path.isfile(pathArquivo):
            os.remove(pathArquivo)

    return json.dumps({'status': 200})

@app.route('/arquivos/<nome_arquivo>', methods=['DELETE'])
def remover_arquivo(nome_arquivo):
    caminho_arquivo =  './arquivos/' + nome_arquivo
    print(caminho_arquivo)
    if os.path.exists(caminho_arquivo) == True:
        os.remove(caminho_arquivo)
        return json.dumps({'status': 200, 'mensagem': 'OK'})
    else:
        return json.dumps({'status': 771, 'mensagem': 'Arquivo não encontrado'})


@app.route('/arquivos/<nome_arquivo>', methods=['PUT'])
def atualizar_criar_arquivo(nome_arquivo):
    arquivo = diretorio_padrao + '/' + nome_arquivo
    arquivo = open(arquivo, 'w')
    conteudo = request.form['conteudo']
    arquivo.write(conteudo)
    arquivo.close()
    return json.dumps({'status':200})

if __name__ == "__main__":
    app.run(debug=True, port=8080)
