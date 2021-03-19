#Começando OO
class Conta:
	#A função que inicia automaticamente
	#Chamamos de construtor
	def __init__(self, numero, titular, saldo, limite):
		#self é a própria referencia do objeto criado na memória
		self.numero = numero
		self.titular = titular
		self.saldo = saldo
		self.limite = limite

	def extrato(self):
		print("O saldo da conta de {} é de R$ {}".format(self.titular, self.saldo))

	def sacar(self, valor):
		self.saldo -= valor

	def depositar(self, valor):
		self.saldo += valor