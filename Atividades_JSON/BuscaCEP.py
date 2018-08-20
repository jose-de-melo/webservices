#coding: utf-8


import urllib2 as ur
import json

def lerCEP():
    print('\nForneça o CEP a ser consultado (sem hífen):')
    return input(">>> ")

def exibirDados(url):
    strCEP = ur.urlopen(url).read()
    jsonCEP = json.loads(strCEP)


    print("\n")
    print("CEP: {}".format(jsonCEP["cep"]))
    print("Logradouro: {}".format(jsonCEP["logradouro"].encode('utf-8')))
    print("Bairro: {}".format(jsonCEP["bairro"].encode('utf-8')))
    print("Localidade: {}".format(jsonCEP["localidade"].encode('utf-8')))
    print("UF: {}".format(jsonCEP["uf"].encode('utf-8')))
    print("IBGE: {}".format(jsonCEP["ibge"].encode('utf-8')))

    print("\nConsulta finalizada..")



def main():
    url = 'https://viacep.com.br/ws/'
    print("---- Consulta de CEP ----")
    cep = lerCEP()
    url += str(cep) + '/json'
    exibirDados(url)

if __name__ == '__main__':
    main()
