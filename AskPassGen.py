#!/usr/bin/env python3

# importacoes de bibilhotecas
import sys
import os
import time
import collections
import platform

# iniciando as variaveis
dadosvit = {}
args = [0,1,2]
lista = []
pontuacao = ["!","?",".","..","...","!!!","!.","!..","!...","?.","?..","?...","@!","+","-","*","**","***"]
semels = collections.OrderedDict([('i', '1'), ('s', '$'), ('n', 'm'), ('o', '0'), ('c', 'k'), ('w', 'u'), ('v','w')])
dectsemels = []
nsem = {i:k for i,k in enumerate(semels.keys())}
lsem = {k:i for i,k in enumerate(semels.keys())}

# variaveis globais do meu corasaum
# nao altere essa variavel se vc n manja dos paranaues, e mesmo se manjar, nao recomendo kk
__interacoes__ = 10000

# banner junto com a prinicipal parte do code
def bannerq():
	print("########################################################")
	print("#----------------AskPassGen Beta v1--------------------#")
	print("#-------------Desenvolvedor: Kevin Souza---------------#")
	print("#---------------Twitter: @DarthSouza-------------------#")
	print("#-----------Criado em: 05/09/2015 - 07:05 AM-----------#")
	print("#---------Atualizado em: 09/09/2015 - 03:53 AM---------#")
	print("#---------Inspirado por: Mr.Robot (The Series)---------#")
	print("########################################################")
	print("")
	print("")
	args[1] = int(input("Level de profundidade (0,1,2): "))
	args[2] = int(input("Level de verbose (0,1,2,3,4): "))
	print("Digite as informacoes relevantes a vitima:")
	dadosvit['primeironome'] = input("Primeiro nome: ")
	dadosvit['meionome'] = input("Nome do meio: ")
	dadosvit['sobrenome'] = input("Sobrenome: ")
	dadosvit['qtmovel'] = input("Quantidade de disp. moveis: ")
	if dadosvit['qtmovel'] == '' or dadosvit['qtmovel'] == 0:
		dadosvit['qtmovel'] = 0
		dadosvit['ddd'] = '0'
	else:
		dadosvit['qtmovel'] = int(dadosvit['qtmovel'])
		dadosvit['ddd'] = input("DDD dos telefones: ") 
	dadosvit['celular'] = []
	for quantidade in range(dadosvit['qtmovel']):
		dadosvit['celular'].append(input("Numero de celular #" + str(quantidade + 1) + ": ")) # sem DDD
	dadosvit['username'] = input("Nome de usuario: ") # em breve, fazer com seja possivel add mais de um
	dadosvit['pamor'] = input("Nome do primeiro namoro/amor: ") # pode parecer irrelevante, mas se tratando de senhas, nada e impossivel
	dadosvit['aamor'] = input("Nome do atual namoro/amor: ") # pode parecer irrelevante, mas se tratando de senhas, nada e impossivel
	if checarinfo() <= 0:
		print('Nenhuma informacao foi fornecida. Mano, ce tem demencia?')
		time.sleep(5)
		sys.exit(0)

def verbos(level,mensagem):
	if args[2] >= level and level != 0:
		print(mensagem)
	elif args[2] == level:
		print(mensagem)

# funcoes da zuera
def arquivar(nomedoarquivo,texto):
	name = nomedoarquivo +'.txt'

	try:
		file = open(name,'w+')
		file.writelines(texto)
		file.close()

	except:
		print('Deu merda berg... Corre vai explodir! -qq')
		time.sleep(3)
		sys.exit(0)

# vamos checar os parametros
def checarinfo():
	verbos(2,'Verificando informacoes fornecidas...')
	checagem = 0
	for potaria in dadosvit:
		if bool(dadosvit[potaria]) == True:
			checagem = checagem + 1
	return checagem

def semelnome(nome,letrosa,modo): # vai retornar o nome dado com as mudancas, tipo Kevin, ficaria Kevim
	nome = nome.lower()
	letra = letrosa
	nomenovo = nome
	# OLD STYLE
	# if (nomenovo.count('n') > 0) and (qtd = 1):
	#	nomenovo = nomenovo.replace('n','m')
	if (modo == 1):
		nomenovo = nomenovo.replace(nsem[lsem[letra]],semels[nsem[lsem[letra]]])
	else:
		for num in nsem:
			nomenovo = nomenovo.replace(nsem[num],semels[nsem[num]])
	nomenovo = nomenovo[0].upper() + nomenovo[1:len(nomenovo)]
	return nomenovo

def qtsemelnome(nome):
	nomenovo = nome.lower()
	mudancas = 0
	if len(nome) >= 1 and nome.isalnum() == True:
		verbos(3,'Detectando semelhancas entre letras no nome: ' + nome)
		for num in nsem:
			if nomenovo.count(nsem[num]) == 1:
				dectsemels.append(nsem[num])
				mudancas = mudancas + 1
		# OLD STYLE
		#if nomenovo.count('n') > 0:
		#	mudancas = mudancas + 1
		verbos(3,'Ha ' + str(mudancas) + ' semelhancas entre letras no nome: ' + nome)
	return mudancas

def looploko(tipo,variavel,nomeamigavel):
	if tipo == 1: # tipo 1 seria para nomes em geral, sem numeros
		if variavel.isalpha() == True:
			verbos(1,"Gerando senhas a partir do " + nomeamigavel + " original...")
			for br in range(__interacoes__):
				treta = variavel + str(br) + "\n"
				lista.append(treta)
				verbos(4,'Senha gerada: ' + str(treta))
				if args[1] >= 2:
					treta = str(br) + variavel + "\n"
					lista.append(treta)
					verbos(4,'Senha gerada: ' + str(treta))
				# testanu algo
				if args[1] >= 1:
					for ponto in pontuacao:
						treta = variavel + str(br) + ponto + "\n"
						lista.append(treta)
						verbos(4,'Senha gerada: ' + str(treta))
						if args[1] >= 2:
							treta = str(br) + variavel + ponto + "\n"
							lista.append(treta)
							verbos(4,'Senha gerada: ' + str(treta))
			verbos(2,"Gerando senhas a partir do " + nomeamigavel + " original com letras pequenas...")
			for br in range(__interacoes__):
				treta = variavel.lower() + str(br) + "\n"
				lista.append(treta)
				verbos(4,'Senha gerada: ' + str(treta))
				if args[1] >= 2:
					treta = str(br) + variavel.lower() + "\n"
					lista.append(treta)
					verbos(4,'Senha gerada: ' + str(treta))
				# testanu algo
				if args[1] >= 1:
					for ponto in pontuacao:
						treta = variavel.lower() + str(br) + ponto + "\n"
						lista.append(treta)
						verbos(4,'Senha gerada: ' + str(treta))
						if args[1] >= 2:
							treta = str(br) + variavel.lower() + ponto + "\n"
							lista.append(treta)
							verbos(4,'Senha gerada: ' + str(treta))
	if tipo == 2: #tipo 2 e pra similaridades
		if qtsemelnome(variavel) > 0 and variavel.isalpha() == True:
			verbos(1,"Gerando senhas a partir do " + nomeamigavel + " com similaridades consideradas...")
			nomesemel = semelnome(variavel, 0, 2)
			for algo in dectsemels:
				nomenovo = semelnome(variavel, algo, 1)
				for br in range(__interacoes__):
					treta = nomenovo + str(br) + "\n"
					lista.append(treta)
					verbos(4,'Senha gerada: ' + str(treta))
					if args[1] >= 2:
						treta = str(br) + nomenovo + "\n"
						lista.append(treta)
						verbos(4,'Senha gerada: ' + str(treta))
					# testanu algo
					if args[1] >= 1:
						for ponto in pontuacao:
							treta = nomenovo + str(br) + ponto + "\n"
							lista.append(treta)
							verbos(4,'Senha gerada: ' + str(treta))
							if args[1] >= 2:
								treta = str(br) + nomenovo + ponto + "\n"
								lista.append(treta)
								verbos(4,'Senha gerada: ' + str(treta))
				for br in range(__interacoes__):
					treta = nomenovo.lower() + str(br) + "\n"
					lista.append(treta)
					verbos(4,'Senha gerada: ' + str(treta))
					if args[1] >= 2:
						treta = str(br) + nomenovo.lower() + "\n"
						lista.append(treta)
						verbos(4,'Senha gerada: ' + str(treta))
					# testanu algo
					if args[1] >= 1:
						for ponto in pontuacao:
							treta = nomenovo.lower() + str(br) + ponto + "\n"
							lista.append(treta)
							verbos(4,'Senha gerada: ' + str(treta))
							if args[1] >= 2:
								treta = str(br) + nomenovo.lower() + ponto + "\n"
								lista.append(treta)
								verbos(4,'Senha gerada: ' + str(treta))
			for br in range(__interacoes__):
				treta = nomesemel + str(br) + "\n"
				lista.append(treta)
				verbos(4,'Senha gerada: ' + str(treta))
				if args[1] >= 2:
					treta = str(br) + nomesemel + "\n"
					lista.append(treta)
					verbos(4,'Senha gerada: ' + str(treta))
				# testanu algo
				if args[1] >= 1:
					for ponto in pontuacao:
						treta = nomesemel + str(br) + ponto + "\n"
						lista.append(treta)
						verbos(4,'Senha gerada: ' + str(treta))
						if args[1] >= 2:
							treta = str(br) + nomesemel + ponto + "\n"
							lista.append(treta)
							verbos(4,'Senha gerada: ' + str(treta))
			for br in range(__interacoes__):
				treta = nomesemel.lower() + str(br) + "\n"
				lista.append(treta)
				verbos(4,'Senha gerada: ' + str(treta))
				if args[1] >= 2:
					treta = str(br) + nomesemel.lower() + "\n"
					lista.append(treta)
					verbos(4,'Senha gerada: ' + str(treta))
				# testanu algo
				if args[1] >= 1:
					for ponto in pontuacao:
						treta = nomesemel.lower() + str(br) + ponto + "\n"
						lista.append(treta)
						verbos(4,'Senha gerada: ' + str(treta))
						if args[1] >= 2:
							treta = str(br) + nomesemel.lower() + ponto + "\n"
							lista.append(treta)
							verbos(4,'Senha gerada: ' + str(treta))


def gerar():
	verbos(0,'Gerando senhas a partir dos dados fornecidos...')
	# para o primeiro nome normal
	looploko(1,dadosvit['primeironome'],"primeiro nome")
	looploko(2,dadosvit['primeironome'],"primeiro nome")
	# para o nome do meio
	looploko(1,dadosvit['meionome'],"nome do meio")
	looploko(2,dadosvit['meionome'],"nome do meio")
	# para o sobrenome
	looploko(1,dadosvit['sobrenome'],"sobrenome")
	looploko(2,dadosvit['sobrenome'],"sobrenome")
	# para o nome do primeiro amor
	looploko(1,dadosvit['pamor'],"nome do primeiro amor")
	looploko(2,dadosvit['pamor'],"nome do primeiro amor")
	# para o nome do atual amor
	looploko(1,dadosvit['aamor'],"nome do atual amor")
	looploko(2,dadosvit['aamor'],"nome do atual amor")
	# para o nome de usuario.. precisa ser complementado, eu acho
	if dadosvit['username'].isalnum() == True:
		verbos(1,"Gerando senhas a partir do nome de usuario (username)...")
		for br in range(__interacoes__):
			treta = dadosvit['username'] + str(br) + "\n"
			lista.append(treta)
			verbos(4,'Senha gerada: ' + str(treta))
	# para o celular e telefone
	if dadosvit['ddd'].isnumeric() == True and int(dadosvit['ddd']) != 0:
		verbos(2,"Gerando senhas a partir do(s) celular(s)/telefone(s)...")
		for dispmovel in dadosvit['celular']:
			indicecel = dadosvit['celular'].index(dispmovel)
			if dadosvit['celular'][indicecel].isnumeric() == True:
				treta = dadosvit['ddd'] + dadosvit['celular'][indicecel] + "\n"
				lista.append(treta)
				verbos(4,'Senha gerada: ' + str(treta))
				treta = dadosvit['celular'][indicecel] + "\n"
				lista.append(treta)
				verbos(4,'Senha gerada: ' + str(treta))
	if dadosvit['primeironome'].isalpha() == True:
		verbos(3,'Gerando nome do arquivo...')
		nomefile = dadosvit['primeironome'].lower()
		if dadosvit['sobrenome'].isalpha() == True:
			nomefile = nomefile + "_" + dadosvit['sobrenome'].lower()
	verbos(0,"Arquivando as senhas geradas...")
	verbos(1,"Arquivando as senhas geradas...")
	arquivar(nomefile,lista)
	verbos(1,"Senhas geradas arquivadas em: " + nomefile + ".txt")

def limpatela():
	if platform.system() == 'Windows':
		nada = os.system('cls')
	else:
		nada = os.system('clear')

def main():
	limpatela()
	bannerq()
	limpatela()
	gerar()
	print("Tudo feito. Vlws Flws.")

main() # inicie essa bagaca
