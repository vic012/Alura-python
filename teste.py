#A função que cria contas bancárias

def cria_conta(numero, titular, saldo, limite):
	conta = {
	'numero': numero,
	'titular': titular,
	'saldo': saldo,
	'limite': limite
	}
	return conta

def deposita(conta, valor):
	conta['saldo'] += valor

def saca(conta, valor):
	conta['saldo'] -= valor

def extrato(conta):
	print('O saldo da conta {} é de {}'.format(conta['numero'], conta['saldo']))
