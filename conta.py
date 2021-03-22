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
		if (self.__pode_sacar(valor)):
			self.__saldo -= valor
		else:
			print('O valor {} passou do limite'.format(valor))

	#Método privado
	def __pode_sacar(self, valor_a_sacar):
		valor_disponivel = self.__saldo + self.__limite
		return valor_a_sacar <= valor_disponivel

	def depositar(self, valor):
		self.__saldo += valor

	def transferir(self, valor, destino):
		#Para usar esse método preciso ter duas contas cadastradas no mínimo

		'''Execução no CMD
		caixa = Conta(135, 'Zé', 50, 1000)
		inter = Conta(527, 'Asis', 200, 1000)

		caixa.transferir(50, caixa, inter)
		Aqui eu repeti caixa, vams melhorar isso

		caixa.extrato()
		O saldo da conta de Zé é de R$ 100
		inter.extrato()
		O saldo da conta de Asis é de R$ 150

		podemos deixa no atributo da seguinte forma:
		def transferir(self, valor, destino) em vez de
		def transferir(self, valor, origem, destino) 

		dessa forma, em vez de:

		origem.sacar(valor)
		destino.depositar(valor)

		Fica:'''

		self.sacar(valor)
		destino.depositar(valor)

	#Método Get, para retornar dados, isso pode ser ultil para relatórios
	def get_saldo(self):
		return self.__saldo

	def get_titular(self):
		return self.__titular

	@property
	def limite(self):
		return self.__limite

	#Método Set, para atualizar dados dentro do meu objeto
	#O set coloca um novo valor
	@limite.setter
	def limite(self, limite):
		self.__limite = limite