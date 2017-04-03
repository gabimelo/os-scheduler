import sys
sys.path.insert(0, 'estruturas_de_dados')
sys.path.insert(0, 'dispositivos')

from motor import *
from sistema import *
from min_heap import *
from cpu import *
from disco import *
from impressora import *
from leitora import *
from memoria import *

def inicializa_sistema(arquivo):
	dados_sistema = le_especificacao_sistema("arquivos_entrada/sistema.txt")

	instante_inicial = dados_sistema[0]
	instante_final_max = dados_sistema[1]
	tamanho_max_fila_cpu = dados_sistema[2]
	duracao_time_slice = dados_sistema[3]
	tamanho_memoria = dados_sistema[4]
	tamanho_max_fila_memoria = dados_sistema[5]
	tempo_transferencia_disco = dados_sistema[6]
	tamanho_max_fila_disco = dados_sistema[7]
	tempo_transferencia_impressora1 = dados_sistema[8]
	tamanho_max_fila_impressora1 = dados_sistema[9]
	tempo_transferencia_impressora2 = dados_sistema[10]
	tamanho_max_fila_impressora2 = dados_sistema[11]
	tempo_transferencia_leitora1 = dados_sistema[12]
	tamanho_max_fila_leitora1 = dados_sistema[13]
	tempo_transferencia_leitora2 = dados_sistema[14]
	tamanho_max_fila_leitora2 = dados_sistema[15]

	cpu = CPU(tamanho_max_fila_cpu, duracao_time_slice)
	memoria = Memoria(tamanho_memoria, tamanho_max_fila_memoria)
	disco = Disco(tempo_transferencia_disco, tamanho_max_fila_disco)
	impressora1 = Impressora(tempo_transferencia_disco, tamanho_max_fila_disco)
	impressora2 = Impressora(tempo_transferencia_disco, tamanho_max_fila_disco)
	leitora1 = Leitora(tempo_transferencia_disco, tamanho_max_fila_disco)
	leitora2 = Leitora(tempo_transferencia_disco, tamanho_max_fila_disco)

	sistema = Sistema(cpu, memoria, disco, impressora1, impressora2, leitora1, leitora2)

	return instante_inicial, instante_final_max, sistema

def le_especificacao_sistema(arquivo):
	dados_sistema = []
	especificacao = open(arquivo, "r")
	for line in especificacao:
		if line[0] == "#":
			break
		dados = line.rstrip('\n')
		dados_sistema.append(dados)

	return dados_sistema

def prepara_lista_jobs(arquivo):
	lista_jobs = []
	dados_jobs = le_dados_jobs(arquivo)
	for job in dados_jobs:
		lista_jobs.append({"nome" :job[0],
			"prioridade" : job[1],
			"tempo_total_processamento" : job[2],
			"quantidade_memoria" : job[3],
			"quantidade_acessos_disco" : job[4],
			"tamanho_acessos_disco" : job[5],
			"quantidade_acessos_impressora1" : job[6],
			"tamanho_acessos_impressora1" : job[7],
			"quantidade_acessos_impressora2" : job[8],
			"tamanho_acessos_impressora2" : job[9],
			"quantidade_acessos_leitora1" : job[10],
			"tamanho_acessos_leitora1" : job[11],
			"quantidade_acessos_leitora2" : job[12],
			"tamanho_acessos_leitora2" : job[13]
		})

	return lista_jobs

def le_dados_jobs(arquivo):
	dados_jobs = []
	jobs = open(arquivo, "r")
	for line in jobs:
		if line[0] == "#":
			break
		dados = line.rstrip('\n').split(" ") 
		dados_jobs.append(dados)

	return dados_jobs

def prepara_lista_evento_inicial(instante_inicial, lista_jobs):
	lista_evento_inicial = MinHeap()
	evento = "CHEGADA_DE_JOB"
	instante = instante_inicial
	job = lista_jobs[0]
	lista_evento_inicial.append([int(instante), evento, job])
	return lista_evento_inicial

def main():
	instante_inicial, instante_final_max, sistema = inicializa_sistema("arquivos_entrada/sistema.txt")

	lista_jobs = prepara_lista_jobs("arquivos_entrada/jobs.txt")

	lista_evento_inicial = prepara_lista_evento_inicial(instante_inicial, lista_jobs)

	motor = Motor(instante_inicial, instante_final_max, lista_evento_inicial, lista_jobs, 1, sistema)
	motor.inicia()

if __name__ == "__main__":
	main()