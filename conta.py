#Começando OO
class Conta:
	#A função que inicia automaticamente
	#Chamamos de construtor
	def __init__(self, numero, titular, saldo, limite):
		#self é a própria referencia do objeto criado na memória

		#Atributos privados
		self.__numero = numero
		self.__titular = titular
		self.__saldo = saldo
		self.__limite = limite

	def extrato(self):
		print("O saldo da conta de {} é de R$ {}".format(self.__titular, self.__saldo))

	def sacar(self, valor):
		self.__saldo -= valor

	def depositar(self, valor):
		self.__saldo += valor