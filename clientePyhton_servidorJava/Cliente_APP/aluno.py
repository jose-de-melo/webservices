#coding: utf-8

class Aluno:
    numeroDeObjetos = 0

    def __init__(self, idTurma, nome, matriculado):
        self.__class__.numeroDeObjetos += 1
        self.id = self.__class__.numeroDeObjetos
        self.idTurma = idTurma
        self.nome = nome
        self.matriculado = matriculado

    def setId(self, id):
        self.id = id

    def getId(self):
	    return self.id

    def setIdTurma(self, idTurma):
        self.id = idTurma

    def getIdTurma(self):
        return self.idTurma

    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def setMatriculado(self, matriculado):
        self.matriculado = matriculado

    def getMatriculado(self):
        return self.matriculado
