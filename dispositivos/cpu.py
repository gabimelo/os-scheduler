from fila_de_jobs import *

class CPU():
	def __init__(self, tamanho_max_fila, time_slice):
		self.fila_espera = FilaDeJobs(tamanho_max_fila)
		self.time_slice = time_slice
		self.ocupada = False
		self.tempo_de_overhead = 5