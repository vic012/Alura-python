#Usando propriedades
class Cliente:

	def __init__(self, nome):
		self.__nome = nome

	#Aqui se trata de uma propriedade
	@property
	def nome(self):
		print("Chamando @property nome()")
		return self.__nome.title()
	
	#Aqui se trata de uma atualização a propriedade (set)
	@nome.setter
	def nome(self, nome):
		print("Chamando setter nome()")
		self.__nome = nome
