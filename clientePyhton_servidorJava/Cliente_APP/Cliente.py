#coding: utf-8

import socket
from Turma import Turma
from aluno import Aluno
import os
import json


host = '127.0.0.1'
porta = 1717



def enviarDados(dados):
    try:
        socketCliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        dest = (host, porta)
        socketCliente.connect(dest)
        socketCliente.send((str(dados)).encode('utf-8'))
        print("\nDados enviados com sucesso!")
        socketCliente.close()
    except ConnectionRefusedError:
        print("-> Servidor não está disponível.")


def cadastrarTurma():


    print("---- Cadastro de Turmas ----\n")
    print("Curso:")
    curso = input()

    print("\n")
    print("Ano:")
    ano = input()

    tr = Turma(ano, curso)

    opcao = 1
    while True:
        print("\n")
        print("-- Cadastrar Aluno da Turma ----\n")

        print("Nome do Aluno: ")
        nome = input()
        print("\n")

        print("Matriculado ? S - SIM || N - NÃO")
        op = input()
        matriculado = False
        if op == 'S':
            matriculado = True


        al = Aluno(tr.getId(), nome, matriculado)
        tr.addAluno(al)

        print("\n")
        print("Cadastrar um novo aluno para a turma? 1 - SIM || OUTRO VALOR - NÃO")
        opcao = input()

        if opcao == '1':
            continue
        else:
            break

    
    return tr

def formatarDados(dados):
    jsonTurma = {"Id":dados.getId(),
                 "Curso" : dados.getCurso(),
                 "Ano" : dados.getAno(),
                 "Alunos" : []}


    jsonAluno = {}
    alunos = dados.getAlunos()
    for al in alunos:
        jsonAluno = {"Id" : al.getId(),
                    "IdTurma" : al.getIdTurma(),
                    "Nome": al.getNome(),
                    "Matriculado" : al.getMatriculado()}
    
        jsonTurma['Alunos'].append(jsonAluno)

    return json.dumps(jsonTurma)


def main():
    dados = cadastrarTurma()
    dados = formatarDados(dados)
    enviarDados(dados)

if __name__ == '__main__':
    main()
