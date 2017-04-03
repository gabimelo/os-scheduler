from min_heap import *

class FilaDeJobs():
	def __init__(self, tamanho_max_fila):
		self.tempo_max_espera = 100 
		self.fila_espera = MinHeap()
		self.acumulador_tempo_espera = 0
		self.tamanho_max_fila = tamanho_max_fila
		self.instante_ultima_modificacao = None
		self.quantidade_insercoes = 0

	def append(self, item, instante_insercao):
		self.fila_espera.append(item)
		self.quantidade_insercoes += 1
		self.instante_ultima_modificacao = instante_insercao

	def peek(self):
		return self.fila_espera.peek()

	def is_empty(self):
		return self.fila_espera.is_empty()

	def serve(self, instante_remocao):
		self.instante_ultima_modificacao = instante_remocao
		return self.fila_espera.serve()
		