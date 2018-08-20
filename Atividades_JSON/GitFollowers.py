#coding: utf-8

import json
import urllib2 as ur

urlModel = "https://api.github.com/users/"
urlFollowers = "https://api.github.com/users/{}/followers"
urlRepos = "https://api.github.com/users/"
urlReposComplemento = "/repos?type=owner"


def request(url):
    try:
        return ur.urlopen(url).read()
    except Exception as ex:
        print(ex)
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
        strReturn = str(jsonUser["name"])
        return strReturn.encode('utf-8')


def exibir_repositorios_user(loginUser):
    global urlRepos, urlReposComplemento

    url = urlRepos + loginUser + urlReposComplemento

    jsonRepos = []

    request = request(url)

    if request == None:
        return request
    else:
        jsonRepos = json.loads(request)
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

        print("\n%d Seguidores:\n" % len(jsonFollowers))
        for jObject in jsonFollowers:
            nome = ler_nome_completo_usuario(jObject["login"])
            print("\t{}:".format(nome))

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
