#coding: utf-8

import json
import urllib2 as ur
import os.path


urlModel = "https://api.github.com/users/"
urlFollowers = "https://api.github.com/users/{}/followers"
urlRepos = "https://api.github.com/users/"
urlReposComplemento = "/repos?type=owner"
caminhoCache = "cache/"
extensao = ".csh"


def request(url):
    urlFormatada = url.replace("/", "-")

    if os.path.exists(caminhoCache + urlFormatada + extensao):
        return open(caminhoCache + urlFormatada + extensao, 'r').read()

    else:
        try:
            conteudo = ur.urlopen(url).read()
            newCache = open(caminhoCache + urlFormatada + extensao, 'w')
            newCache.write(conteudo)
            return conteudo
        except Exception as ex:
            print('>> A requisição foi recusada recusada!')
            return None


def ler_nome_completo_usuario(loginUser):
    global urlModel

    url = urlModel + loginUser

    jsonUser = {}

    strRequest = request(url)

    if strRequest == None:
        return strRequest
    else:
        jsonUser = json.loads(strRequest)
        jUsername = jsonUser["name"]

        if jUsername != None:
            strReturn = str(jUsername.encode("utf-8"))
            return strReturn + '({})'.format(loginUser)
        else:
            return 'Sem nome completo ({})'.format(loginUser)


def exibir_repositorios_user(loginUser):
    global urlRepos, urlReposComplemento

    url = urlRepos + loginUser + urlReposComplemento

    jsonRepos = []

    requestSTR = request(url)

    if requestSTR == None:
        return requestSTR
    else:
        jsonRepos = json.loads(requestSTR)
        for jObj in jsonRepos:
            print("\t\t{}".format(jObj["name"]))



def ler_exibir_seguidores(loginUser):
    global urlFollowers
    urlFollowers = urlFollowers.format(loginUser)

    strRequest = request(urlFollowers)

    if strRequest == None:
        return strRequest
    else:
        jsonFollowers = json.loads(strRequest)

        print("\n%d Seguidor(es):\n" % len(jsonFollowers))
        for jObject in jsonFollowers:
            nome = ler_nome_completo_usuario(jObject["login"])
            if nome != None:
                print("\t{}:".format(nome))
                exibir_repositorios_user(jObject["login"])

def ler_user():
    user = raw_input("Forneça o nome do usuário:\n>>> ")
    return user


def main():
    print("--- Consultar Usuários - GitHub")
    loginUser = ler_user()
    nomeCompletoUsuario = ler_nome_completo_usuario(loginUser)

    if nomeCompletoUsuario != None:
        print("Usuário da Consulta: {}".format(nomeCompletoUsuario))
        ler_exibir_seguidores(loginUser)


if __name__ == '__main__':
    main()
