import sys
sys.path.insert(0, 'estruturas_de_dados')
sys.path.insert(0, 'dispositivos')

from random import *

class Motor():
	def __init__(self, instante_inicial, instante_final, lista_evento_inicial, lista_jobs, prox_job, sistema):
		self.instante_atual = instante_inicial
		self.instante_inicial = instante_inicial
		self.instante_final = instante_final
		self.lista_eventos = lista_evento_inicial
		self.lista_jobs = lista_jobs
		self.prox_job = prox_job
		self.job_table = {}
		self.sistema = sistema
								
	def inicia(self):
		self.contador_eventos_processados = 0
		self.log_data = ""
		self.dados_estatisticos = ""
		fim = False

		while not fim:
			if self.lista_eventos.is_empty():
				fim = True
				self.log_data += "Todos os eventos foram processados \n"
				self.dados_estatisticos += "Todos os eventos foram processados \n"
			elif int(self.instante_atual) >= int(self.instante_final):
				fim = True
				self.log_data += "Nem todos os eventos foram processados, porém foi atingido tempo limite de simulação \n"
				self.dados_estatisticos += "Nem todos os eventos foram processados, porém foi atingido tempo limite de simulação \n"
			else:
				fim = self._processa_evento(self.lista_eventos.serve())

		self._gera_log()
		self._imprime_estatisticas()

	def _processa_evento(self, evento):
		fim = False
		self.contador_eventos_processados += 1
		self.instante_atual = evento[0]
		tipo_evento = evento[1]
		job = evento[2]

		if tipo_evento == "CHEGADA_DE_JOB":
			acao = " <chamada a rotina chegada_de_job> "
			resultado = self.chegada_de_job(job)
			self.log_data += str(self.instante_atual) + " chegada de job " + job["nome"] + acao + resultado
			
		elif tipo_evento == "REQUISICAO_MEMORIA":
			acao = " <chamada a rotina de requisicao de memoria> "
			resultado = self.requisicao_memoria(job)
			self.log_data += str(self.instante_atual) + " requisição de memória " + job["nome"] + acao + resultado
			
		elif tipo_evento == "REQUISICAO_CPU":
			acao = " <chamada a rotina de requisicao de cpu> "
			resultado = self.requisicao_cpu(job)
			self.log_data += str(self.instante_atual) + " requisição de cpu " + job["nome"] + acao + resultado
			
		elif tipo_evento == "DESALOCACAO_CPU_TIME_SLICE":
			acao = " <chamada a rotina de desalocacao de cpu por fim de time slice> "
			resultado = self.desalocacao_cpu_time_slice(job)
			self.log_data += str(self.instante_atual) + " desalocação de cpu por time slice " + job["nome"] + acao + resultado
			
		elif tipo_evento == "DESALOCACAO_CPU_E_S":
			acao = " <chamada a rotina de desalocacao de cpu por entrada ou saída> "
			resultado = self.desalocacao_cpu_e_s(job)
			self.log_data += str(self.instante_atual) + " desalocação de cpu por e ou s " + job["nome"] + acao + resultado

		elif tipo_evento == "REQUISICAO_DISCO":
			acao = " <chamada a rotina de requisicao de dipositivo, para o disco> "
			resultado = self.requisicao_dispositivo(job, self.sistema.disco, "disco", job["tamanho_acessos_disco"])
			self.log_data += str(self.instante_atual) + " alocação de disco " + job["nome"] + acao + resultado

		elif tipo_evento == "DESALOCACAO_DISCO":
			acao = " <chamada a rotina de desalocacao de dipositivo, para o disco> "
			resultado = self.desalocacao_dispositivo(job, self.sistema.disco, "disco")
			self.log_data += str(self.instante_atual) + " desalocação de disco " + job["nome"] + acao + resultado

		elif tipo_evento == "REQUISICAO_LEITORA1":
			acao = " <chamada a rotina de requisicao de dipositivo, para a leitora1> "
			resultado = self.requisicao_dispositivo(job, self.sistema.leitora1, "leitora1", job["tamanho_acessos_leitora1"])
			self.log_data += str(self.instante_atual) + " alocação de leitora1 " + job["nome"] + acao + resultado

		elif tipo_evento == "DESALOCACAO_LEITORA1":
			acao = " <chamada a rotina de desalocacao de dipositivo, para a leitora1> "
			resultado = self.desalocacao_dispositivo(job, self.sistema.leitora1, "leitora1")
			self.log_data += str(self.instante_atual) + " desalocação de leitora1 " + job["nome"] + acao + resultado

		elif tipo_evento == "REQUISICAO_LEITORA2":
			acao = " <chamada a rotina de requisicao de dipositivo, para a leitora2> "
			resultado = self.requisicao_dispositivo(job, self.sistema.leitora2, "leitora2", job["tamanho_acessos_leitora1"])
			self.log_data += str(self.instante_atual) + " alocação de leitora2 " + job["nome"] + acao + resultado

		elif tipo_evento == "DESALOCACAO_LEITORA2":
			acao = " <chamada a rotina de desalocacao de dipositivo, para a leitora2> "
			resultado = self.desalocacao_dispositivo(job, self.sistema.leitora2, "leitora2")
			self.log_data += str(self.instante_atual) + " desalocação de leitora2 " + job["nome"] + acao + resultado

		elif tipo_evento == "REQUISICAO_IMPRESSORA1":
			acao = " <chamada a rotina de requisicao de dipositivo, para a impressora1> "
			resultado = self.requisicao_dispositivo(job, self.sistema.impressora1, "impressora1", job["tamanho_acessos_impressora1"])
			self.log_data += str(self.instante_atual) + " alocação de impressora1 " + job["nome"] + acao + resultado

		elif tipo_evento == "DESALOCACAO_IMPRESSORA1":
			acao = " <chamada a rotina de desalocacao de dipositivo, para a impressora1> "
			resultado = self.desalocacao_dispositivo(job, self.sistema.impressora1, "impressora1")
			self.log_data += str(self.instante_atual) + " desalocação de impressora1 " + job["nome"] + acao + resultado

		elif tipo_evento == "REQUISICAO_IMPRESSORA2":
			acao = " <chamada a rotina de requisicao de dipositivo, para a impressora2> "
			resultado = self.requisicao_dispositivo(job, self.sistema.impressora2, "impressora2", job["tamanho_acessos_impressora2"])
			self.log_data += str(self.instante_atual) + " alocação de impressora2 " + job["nome"] + acao + resultado

		elif tipo_evento == "DESALOCACAO_IMPRESSORA2":
			acao = " <chamada a rotina de desalocacao de dipositivo, para a impressora2> "
			resultado = self.desalocacao_dispositivo(job, self.sistema.impressora2, "impressora2")
			self.log_data += str(self.instante_atual) + " desalocação de impressora2 " + job["nome"] + acao + resultado

		elif tipo_evento == "DESALOCACAO_CPU_E_MEMORIA":
			acao = " <chamada a rotina de desalocacao de cpu e memoria> "
			resultado = self.desalocacao_cpu_e_memoria(job)
			self.log_data += str(self.instante_atual) + " desalocação de cpu e memória " + job["nome"] + acao + resultado

		else:
			raise TypeError("Tipo inválido de evento")

		self.log_data += "\n"

		return fim

	def _gera_log(self):
		log = open("arquivos_saida/log.txt", "w")
		log.write(self.log_data)
		print('O log completo da execução encontra-se no arquivo "arquivos_saida/log.txt"')

	def _imprime_estatisticas(self):
		self.agrega_dados_estatisticos()
		estatisticas = open("arquivos_saida/estatisticas.txt", "w")
		estatisticas.write(self.dados_estatisticos)
		print('As estatísticas da execução encontram-se no arquivo "arquivos_saida/estatísticas.txt"')

	def chegada_de_job(self, job):		
		resultado = " <"
		self.inicializa_job_em_job_table(job)
		self.lista_eventos.append([self.instante_atual, "REQUISICAO_MEMORIA", job])
		instante_prox_chegada = int(self.instante_atual) + randint(0, 20)
		try: 
			self.lista_eventos.append([int(instante_prox_chegada), "CHEGADA_DE_JOB", self.lista_jobs[self.prox_job]])
			resultado += "inserido proxima chegada de job e "
		except IndexError:
			pass
		self.prox_job += 1
		return resultado + "feita requisicao de memoria para job atual> "

	def inicializa_job_em_job_table(self, job):
		lista_de_e_s = []
		for i in range(0, int(job["quantidade_acessos_disco"])):
			instante_prox_e_s = randint(0, 20)
			lista_de_e_s.append([instante_prox_e_s, "disco", job["tamanho_acessos_disco"]])
		for i in range(0, int(job["quantidade_acessos_impressora1"])):
			instante_prox_e_s = randint(0, 20)
			lista_de_e_s.append([instante_prox_e_s, "impressora1", job["tamanho_acessos_impressora1"]])
		for i in range(0, int(job["quantidade_acessos_impressora2"])):
			instante_prox_e_s = randint(0, 20)
			lista_de_e_s.append([instante_prox_e_s, "impressora2", job["tamanho_acessos_impressora2"]])
		for i in range(0, int(job["quantidade_acessos_leitora1"])):
			instante_prox_e_s = randint(0, 20)
			lista_de_e_s.append([instante_prox_e_s, "leitora1", job["tamanho_acessos_leitora1"]])
		for i in range(0, int(job["quantidade_acessos_leitora2"])):
			instante_prox_e_s = randint(0, 20)
			lista_de_e_s.append([instante_prox_e_s, "leitora2", job["tamanho_acessos_leitora2"]])
		self.job_table[job["nome"]] = {"prioridade" : job["prioridade"], "tempo_restante_processamento" : job["tempo_total_processamento"], "lista_de_e_s" : lista_de_e_s}
		
	def requisicao_memoria(self, job):
		if int(self.sistema.memoria.memoria_disponivel) < int(job["quantidade_memoria"]):
			self.sistema.memoria.fila_espera.append([job["prioridade"], job], self.instante_atual)
			resultado = " <não havia quantidade suficiente de memória disponível e o job foi colocado na fila de espera da memória> "
		else:
			TR = int(self.sistema.memoria.tempo_de_relocacao)
			self.sistema.memoria.memoria_disponivel = int(self.sistema.memoria.memoria_disponivel) - int(job["quantidade_memoria"])
			self.lista_eventos.append([int(self.instante_atual) + TR, "REQUISICAO_CPU", job])
			resultado = " <job foi alocado na memória> "
		return resultado

	def requisicao_cpu(self, job):
		if self.sistema.cpu.ocupada:
			self.sistema.cpu.fila_espera.append([job["prioridade"], job], self.instante_atual)
			resultado = "<job colocado na fila de espera da cpu>"
		else:
			self.sistema.cpu.ocupada = True
			if len(self.job_table[job["nome"]]["lista_de_e_s"]) == 0:
				if self.job_table[job["nome"]]["tempo_restante_processamento"] < 0:
					instante_saida = self.instante_atual
				else:
					instante_saida = self.instante_atual + self.job_table[job["nome"]]["tempo_restante_processamento"]
				self.lista_eventos.append([instante_saida, "DESALOCACAO_CPU_E_MEMORIA", job])
				self.job_table[job["nome"]]["tempo_restante_processamento"] = 0
				resultado = " <gerado evento de desalocacao de cpu e memoria> "
			else:
				prox_e_s = self.job_table[job["nome"]]["lista_de_e_s"][0]
				if prox_e_s[0] > int(self.sistema.cpu.time_slice):
					instante_prox_desalocacao_cpu = self.instante_atual + int(self.sistema.cpu.time_slice)
					resultado = " <gerado evento de desalocacao de cpu devido a fim de time slice> "
					self.lista_eventos.append([instante_prox_desalocacao_cpu, "DESALOCACAO_CPU_TIME_SLICE", job])
				else:
					instante_prox_desalocacao_cpu = self.instante_atual + prox_e_s[0]
					resultado = " <gerado evento de desalocacao de cpu devido a operação de entrada ou saída> "
					self.lista_eventos.append([instante_prox_desalocacao_cpu, "DESALOCACAO_CPU_E_S", job])
				self.job_table[job["nome"]]["tempo_restante_processamento"] = instante_prox_desalocacao_cpu - self.instante_atual
		return resultado

	def desalocacao_cpu_time_slice(self, job):
		self.sistema.cpu.ocupada = False
		resultado = " <"
		TO = self.sistema.cpu.tempo_de_overhead

		self.sistema.cpu.fila_espera.append([job["prioridade"], job], self.instante_atual)
		resultado += " job saiu da cpu devido ao fim de seu time slice e colocado na fila de espera da cpu"

		if not self.sistema.cpu.fila_espera.is_empty():
			proximo_job_para_cpu = self.sistema.cpu.fila_espera.serve(self.instante_atual)
			self.lista_eventos.append([self.instante_atual + TO, "REQUISICAO_CPU", proximo_job_para_cpu[1]])
			resultado += " a lista de espera da cpu foi avançada "

		return resultado + "> "

	def desalocacao_cpu_e_s(self, job):
		self.sistema.cpu.ocupada = False
		resultado = " <"
		TO = self.sistema.cpu.tempo_de_overhead

		e_s = self.job_table[job["nome"]]["lista_de_e_s"].pop(0)
		if e_s[1] == "disco":
			self.lista_eventos.append([self.instante_atual + TO, "REQUISICAO_DISCO", job])
			resultado += " job saiu da cpu e foi gerado evento de requisicao de disco "
		elif e_s[1] == "leitora1":
			self.lista_eventos.append([self.instante_atual + TO, "REQUISICAO_LEITORA1", job])
			resultado += " job saiu da cpu e foi gerado evento de requisicao de leitora1 "
		elif e_s[1] == "leitora2":
			self.lista_eventos.append([self.instante_atual + TO, "REQUISICAO_LEITORA2", job])
			resultado += " job saiu da cpu e foi gerado evento de requisicao de leitora2 "
		elif e_s[1] == "impressora1":
			self.lista_eventos.append([self.instante_atual + TO, "REQUISICAO_IMPRESSORA1", job])
			resultado += " job saiu da cpu e foi gerado evento de requisicao de impressora1 "
		elif e_s[1] == "impressora2":
			self.lista_eventos.append([self.instante_atual + TO, "REQUISICAO_IMPRESSORA2", job])
			resultado += " job saiu da cpu e foi gerado evento de requisicao de impressora2 "

		if not self.sistema.cpu.fila_espera.is_empty():
			proximo_job_para_cpu = self.sistema.cpu.fila_espera.serve(self.instante_atual)
			self.lista_eventos.append([self.instante_atual + TO, "REQUISICAO_CPU", proximo_job_para_cpu[1]])
			resultado += " a lista de espera da cpu foi avançada "

		return resultado + "> "

	def requisicao_dispositivo(self, job, dispositivo, tipo_dispositivo, tamanho_acesso):
		if dispositivo.ocupado:
			dispositivo.fila_espera.append([job["prioridade"], job], self.instante_atual)
			if tipo_dispositivo == "disco":
				resultado = " <job foi colocado na fila de espera para o disco> "
			elif tipo_dispositivo == "impressora1":
				resultado = " <job foi colocado na fila de espera para a impressora1> "
			elif tipo_dispositivo == "impressora2":
				resultado = " <job foi colocado na fila de espera para a impressora2> "
			elif tipo_dispositivo == "leitora1":
				resultado = " <job foi colocado na fila de espera para o leitora1> "
			else:
				resultado = " <job foi colocado na fila de espera para o leitora2> "
		else:
			dispositivo.ocupado = True
			TD = int(dispositivo.tempo_transferencia_palavra) * int(tamanho_acesso)
			if tipo_dispositivo == "disco":
				self.lista_eventos.append([self.instante_atual + TD, "DESALOCACAO_DISCO", job])
				resultado = " <disco foi alocado para o job> "
			elif tipo_dispositivo == "impressora1":
				self.lista_eventos.append([self.instante_atual + TD, "DESALOCACAO_IMPRESSORA1", job])
				resultado = " <impressora1 foi alocada para o job> "
			elif tipo_dispositivo == "impressora2":
				self.lista_eventos.append([self.instante_atual + TD, "DESALOCACAO_IMPRESSORA2", job])
				resultado = " <impressora2 foi alocada para o job> "
			elif tipo_dispositivo == "leitora1":
				self.lista_eventos.append([self.instante_atual + TD, "DESALOCACAO_LEITORA1", job])
				resultado = " <leitora1 foi alocada para o job> "
			else:
				self.lista_eventos.append([self.instante_atual + TD, "DESALOCACAO_LEITORA2", job])
				resultado = " <leitora2 foi alocada para o job> "

		return resultado

	def desalocacao_dispositivo(self, job, dispositivo, tipo_dispositivo):
		dispositivo.ocupado = False
		resultado = " <"

		if not dispositivo.fila_espera.is_empty():
			proximo_job_para_dispositivo = dispositivo.fila_espera.serve(self.instante_atual)
			if tipo_dispositivo == "disco":
				self.lista_eventos.append([self.instante_atual, "REQUISICAO_DISCO", proximo_job_para_dispositivo[1]])
				resultado += " a lista de espera do disco foi avançada"
			elif tipo_dispositivo == "impressora1":
				self.lista_eventos.append([self.instante_atual, "REQUISICAO_IMPRESSORA1", proximo_job_para_dispositivo[1]])
				resultado += " a lista de espera da impressora1 foi avançada "
			elif tipo_dispositivo == "impressora2":
				self.lista_eventos.append([self.instante_atual, "REQUISICAO_IMPRESSORA2", proximo_job_para_dispositivo[1]])
				resultado += " a lista de espera da impressora2 foi avançada "
			elif tipo_dispositivo == "leitora1":
				self.lista_eventos.append([self.instante_atual, "REQUISICAO_LEITORA1", proximo_job_para_dispositivo[1]])
				resultado += " a lista de espera da leitora1 foi avançada "
			else:
				self.lista_eventos.append([self.instante_atual, "REQUISICAO_LEITORA1", proximo_job_para_dispositivo[1]])
				resultado += " a lista de espera da leitora1 foi avançada "

		TO = self.sistema.cpu.tempo_de_overhead
		self.lista_eventos.append([self.instante_atual + TO, "REQUISICAO_CPU", job])
		resultado += " o job saiu do dispositivo e foi gerado evento de requisicao de cpu"

		return resultado + "> "

	def desalocacao_cpu_e_memoria(self, job):
		resultado = " <"

		self.sistema.cpu.ocupada = False
		
		TO = self.sistema.cpu.tempo_de_overhead
		if not self.sistema.cpu.fila_espera.is_empty():
			proximo_job_para_cpu = self.sistema.cpu.fila_espera.serve(self.instante_atual)
			self.lista_eventos.append([self.instante_atual + TO, "REQUISICAO_CPU", proximo_job_para_cpu[1]])
			resultado += " a lista de espera da cpu foi avançada, "
		
		self.sistema.memoria.memoria_disponivel += int(job["quantidade_memoria"])

		if not self.sistema.memoria.fila_espera.is_empty():
			proximo_job_para_memoria = self.sistema.memoria.fila_espera.serve(self.instante_atual)
			self.lista_eventos.append([self.instante_atual, "REQUISICAO_MEMORIA", proximo_job_para_memoria[1]])
			resultado += " a lista de espera da memoria foi avançada, "

		resultado += " o job saiu da memoria e cpu"

		del self.job_table[job["nome"]]

		return resultado + "> "

	def agrega_dados_estatisticos(self):
		self.dados_estatisticos += "Tempo total de processamento = " + str(self.instante_atual-int(self.instante_inicial)) + "\n"
		self.dados_estatisticos += "Quantidade de eventos processados = " + str(self.contador_eventos_processados) + "\n"
		self.dados_estatisticos += "Quantidades de inserções na fila da memória = " + str(self.sistema.memoria.fila_espera.quantidade_insercoes) + "\n"
		self.dados_estatisticos += "Quantidades de inserções na fila da cpu = " + str(self.sistema.cpu.fila_espera.quantidade_insercoes) + "\n"
		self.dados_estatisticos += "Quantidades de inserções na fila do disco = " + str(self.sistema.disco.fila_espera.quantidade_insercoes) + "\n"
		self.dados_estatisticos += "Quantidades de inserções na fila da impressora1 = " + str(self.sistema.impressora1.fila_espera.quantidade_insercoes) + "\n"
		self.dados_estatisticos += "Quantidades de inserções na fila da impressora2 = " + str(self.sistema.impressora2.fila_espera.quantidade_insercoes) + "\n"
		self.dados_estatisticos += "Quantidades de inserções na fila da leitora1 = " + str(self.sistema.leitora1.fila_espera.quantidade_insercoes) + "\n"
		self.dados_estatisticos += "Quantidades de inserções na fila da leitora2 = " + str(self.sistema.leitora2.fila_espera.quantidade_insercoes) + "\n"
		self.dados_estatisticos += "Última modificação na fila da memória = " + str(self.sistema.memoria.fila_espera.instante_ultima_modificacao) + "\n"
		self.dados_estatisticos += "Última modificação na fila da cpu = " + str(self.sistema.cpu.fila_espera.instante_ultima_modificacao) + "\n"
		self.dados_estatisticos += "Última modificação na fila do disco = " + str(self.sistema.disco.fila_espera.instante_ultima_modificacao) + "\n"
		self.dados_estatisticos += "Última modificação na fila da impressora1 = " + str(self.sistema.impressora1.fila_espera.instante_ultima_modificacao) + "\n"
		self.dados_estatisticos += "Última modificação na fila da impressora2 = " + str(self.sistema.impressora2.fila_espera.instante_ultima_modificacao) + "\n"
		self.dados_estatisticos += "Última modificação na fila da leitora1 = " + str(self.sistema.leitora1.fila_espera.instante_ultima_modificacao) + "\n"
		self.dados_estatisticos += "Última modificação na fila da leitora2 = " + str(self.sistema.leitora2.fila_espera.instante_ultima_modificacao) + "\n"