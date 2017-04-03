from fila_de_jobs import *

class Memoria():
	def __init__(self, tamanho, tamanho_max_fila):
		self.memoria_disponivel = tamanho
		self.fila_espera = FilaDeJobs(tamanho_max_fila)
		self.tempo_de_relocacao = 10