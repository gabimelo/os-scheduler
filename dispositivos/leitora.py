from fila_de_jobs import *

class Leitora():
	def __init__(self, tempo_transferencia_palavra, tamanho_max_fila):
		self.tempo_transferencia_palavra = tempo_transferencia_palavra
		self.fila_espera = FilaDeJobs(tamanho_max_fila)
		self.ocupado = False