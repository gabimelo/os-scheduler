from cpu import *
from memoria import *
from disco import *
from impressora import *
from leitora import *

class Sistema():
	def __init__(self, cpu, memoria, disco, impressora1, impressora2, leitora1, leitora2):
		self.cpu = cpu
		self.memoria = memoria
		self.disco = disco
		self.impressora1 = impressora1
		self.impressora2 = impressora2
		self.leitora1 = leitora1
		self.leitora2 = leitora2