#coding: utf-8

import requests
import os
import json

url = 'http://127.0.0.1:8080/arquivos'


def listar_arquivos():
    print('Arquivos do diretório /arquivos:\n')

    response = requests.get(url + '/json')
    
    jsonResponse = json.loads(response.text)
    for s in jsonResponse['arquivos']:
        print('>> ' + s + '\n')


def exibir_arquivo():
    nomeArq = input('Nome do Arquivo: ')

    response = requests.get(url + '/conteudo/' + nomeArq)

    jsonResponse = json.loads(response.text)

    if jsonResponse['status'] == 771:
        print(jsonResponse['erro'])
    else:
        print('\nConteúdo arquivo %s:' % nomeArq)
        print(jsonResponse['conteudo'])

def remover_arquivo():
    nomeArq = input('Nome do Arquivo: ')

    response = requests.delete(url + '/' + nomeArq)

    jsonResponse = json.loads(response.text)

    if jsonResponse['status'] == 200:
        print('Arquivo removido.')
    else:
        print(jsonResponse['mensagem'])

def remover_todos_arquivos():
    response = requests.delete(url)

    jsonResponse = json.loads(response.text)

    if jsonResponse['status'] == 200:
        print('Os arquivos foram removidos.')

def criar_arquivo():
    nomeArq = input('Nome do arquivo: ')

    response = requests.put(url + '/' + nomeArq, data={'conteudo': ''})

    jsonResponse = json.loads(response.text)

    if jsonResponse['status'] == 200:
        print('Arquivo criado com sucesso.')
    else:
        print('Ocorreu um erro ao tentar criar o arquivo.')

def atualizar_arquivo():
    nomeArq = input('Nome do arquivo: ')
    print('\n')
    conteudo = input('Novo conteúdo do arquivo:\n')

    response = requests.put(url + '/' + nomeArq, data={'conteudo': conteudo})

    jsonResponse = json.loads(response.text)

    if jsonResponse['status'] == 200:
        print('\nArquivo atualizado com sucesso.')
    else:
        print('\nOcorreu um erro ao tentar atualizar o arquivo.')


def requisicoes():
    funcoes = [listar_arquivos, exibir_arquivo, remover_arquivo, remover_todos_arquivos, criar_arquivo, atualizar_arquivo]
    
    while(True):
        os.system('clear')

        print('FileAPI - Escolha uma opção\n\n')
        op = int(input('1.Listar Arquivos\n2. Exibir Arquivo\n3. Remover Arquivo\n4. Remover Todos os Arquivos\n5. Criar Arquivo\n6. Atualizar Arquivo\n7. Sair\n\n\nOpção: '))

        if op == 7:
            break

        funcoes[op -1]()
        input('\nPressione ENTER para continuar...')
    

if __name__ == "__main__":
    try:
        requisicoes()
    except:
        print('\n')






