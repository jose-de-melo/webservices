#coding: utf-8


class Turma:
	numeroDeObjetos = 0

	def __init__(self, ano, curso):
		self.__class__.numeroDeObjetos += 1
		self.id = self.__class__.numeroDeObjetos
		self.ano = ano
		self.curso = curso
		self.alunos = []

	def setId(self, id):
		self.id = id

	def getId(self):
		return self.id

	def setAno(self, ano):
		self.ano = ano

	def getAno(self):
		return self.ano

	def setCurso(self, curso):
		self.curso = curso

	def getCurso(self):
		return self.curso

	def setAlunos(self, alunos):
		self.alunos = alunos

	def getAlunos(self):
		return self.alunos

	def addAluno(self, aluno):
		self.alunos.append(aluno)

	def numeroDeAlunos(self):
		return len(alunos)
