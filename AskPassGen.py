#!/usr/bin/env python3

import sys
import os
import time
import collections
import platform
import argparse

dadosvit = {}
args = [0,1,2]
lista = []
pontuacao = ["!","?",".","..","...","!!!","!.","!..","!...","?.","?..","?...","@!","+","-","*","**","***"]
semels = collections.OrderedDict([('i', '1'), ('s', '$'), ('n', 'm'), ('o', '0'), ('c', 'k'), ('w', 'u'), ('v','w')])
dectsemels = []
nsem = {i:k for i,k in enumerate(semels.keys())}
lsem = {k:i for i,k in enumerate(semels.keys())}

__interacoes__ = 10000

parser = argparse.ArgumentParser(description='AskPassGen - Made by @DarthSouza - Licensed under the MIT license.')
parser.add_argument('-l', action='store', dest='profd', help='Level of Depth', default=1, type=int)
parser.add_argument('-v', action='store', dest="verb", help='Level of Verbose', default=3, type=int)
parser.add_argument('-firstname', action='store', dest='firstname', help='Target - First Name', type=str)
parser.add_argument('-middlename', action='store', dest='middlename', help='Target - Middle Name', default="", type=str)
parser.add_argument('-lastname', action='store', dest='lastname', help='Target - Last Name', type=str)
parser.add_argument('-ddd', action='store', dest='ddd', help='Target - DDD of phone number', default="")
parser.add_argument('-phone', action='store', dest='phone', help='Target - Telephone Number', default="")
parser.add_argument('-username', action='store', dest='username', help='Target - Username', default="")
parser.add_argument('-firstrelation', action='store', dest='firstrelation', help='Target - First Relationship', default="", type=str)
parser.add_argument('-actualrelation', action='store', dest='actualrelation', help='Target - Actual Relationship', default="", type=str)
arglin = parser.parse_args()

def bannerq():
	if bool(arglin.firstname) == True and bool(arglin.lastname) == True:
		args[1] = arglin.profd
		args[2] = arglin.verb
		dadosvit['primeironome'] = arglin.firstname
		dadosvit['meionome'] = arglin.middlename
		dadosvit['sobrenome'] = arglin.lastname
		dadosvit['ddd'] = arglin.ddd
		dadosvit['celular'] = [arglin.phone]
		dadosvit['username'] = arglin.username
		dadosvit['pamor'] = arglin.firstrelation
		dadosvit['aamor'] = arglin.actualrelation
	else:
		print("########################################################")
		print("#----------------AskPassGen Beta v3--------------------#")
		print("#---------Desenvolvedor: Kevin Souza (@DarthSouza)-----#")
		print("#---------Criado em: 05/09/2015 - 07:05 AM-------------#")
		print("#---------Atualizado em: 06/11/2015 - 07:04 PM---------#")
		print("#---------Inspirado por: Mr.Robot (The Series)---------#")
		print("########################################################")
		print("")
		print("")
		args[1] = int(input("Level de profundidade (0,1,2,3): "))
		args[2] = int(input("Level de verbose (0,1,2,3,4): "))
		if args[1] == "" or args[1] == "0" or args[1] == 0:
			args[1] = arglin.profd
		if args[2] == "" or args[2] == "0" or args[2] == 0:
			args[2] = arglin.verb
		print("Digite as informacoes relevantes a vitima:")
		dadosvit['primeironome'] = input("Primeiro nome: ")
		dadosvit['meionome'] = input("Nome do meio: ")
		dadosvit['sobrenome'] = input("Sobrenome: ")
		dadosvit['qtmovel'] = input("Quantidade de disp. moveis: ")
		if dadosvit['qtmovel'] == '' or dadosvit['qtmovel'] == 0 or dadosvit['qtmovel'] == '0':
			dadosvit['qtmovel'] = 0
			dadosvit['ddd'] = '0'
		else:
			dadosvit['qtmovel'] = int(dadosvit['qtmovel'])
			dadosvit['ddd'] = input("DDD dos telefones: ")
			dadosvit['celular'] = []
			for quantidade in range(dadosvit['qtmovel']):
				dadosvit['celular'].append(input("Numero de celular #" + str(quantidade + 1) + ": ")) # sem DDD
		dadosvit['username'] = input("Nome de usuario: ")
		dadosvit['pamor'] = input("Nome do primeiro namoro/amor: ")
		dadosvit['aamor'] = input("Nome do atual namoro/amor: ")
	if checarinfo() <= 0:
		limpatela()
		print('Nenhuma informacao foi fornecida. Mano, ce tem demencia?')
		time.sleep(5)
		sys.exit(0)

def verbos(level,mensagem):
	if args[2] >= level and level != 0:
		print(mensagem)
	elif args[2] == level:
		print(mensagem)

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

def checarinfo():
	verbos(2,'Verificando informacoes fornecidas...')
	checagem = 0
	for potaria in dadosvit:
		if bool(dadosvit[potaria]) == True:
			checagem = checagem + 1
	return checagem

def semelnome(nome,letrosa,modo):
	nome = nome.lower()
	letra = letrosa
	nomenovo = nome
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
		verbos(3,'Ha ' + str(mudancas) + ' semelhancas entre letras no nome: ' + nome)
	return mudancas

def looploko(tipo,variavel,nomeamigavel):
	if tipo == 1: # tipo 1 seria para nomes em geral, sem numeros
		if variavel.isalpha() == True:
			verbos(1,"Gerando senhas a partir do " + nomeamigavel + " original...")
			for ponto in pontuacao:
				treta = variavel + ponto + "\n"
				lista.append(treta)
				verbos(4,'Senha gerada: ' + str(treta))
			for br in range(__interacoes__):
				treta = variavel + str(br) + "\n"
				lista.append(treta)
				verbos(4,'Senha gerada: ' + str(treta))
				if args[1] >= 2:
					treta = str(br) + variavel + "\n"
					lista.append(treta)
					verbos(4,'Senha gerada: ' + str(treta))
				if args[1] >= 1:
					for ponto in pontuacao:
						treta = variavel + str(br) + ponto + "\n"
						lista.append(treta)
						verbos(4,'Senha gerada: ' + str(treta))
						if args[1] >= 2:
							treta =  variavel + ponto + str(br) + "\n"
							lista.append(treta)
							verbos(4,'Senha gerada: ' + str(treta))
						if args[1] >= 3:
							treta = str(br) + variavel + ponto + "\n"
							lista.append(treta)
							verbos(4,'Senha gerada: ' + str(treta))
			verbos(2,"Gerando senhas a partir do " + nomeamigavel + " original com letras pequenas...")
			for ponto in pontuacao:
				treta = variavel.lower() + ponto + "\n"
				lista.append(treta)
				verbos(4,'Senha gerada: ' + str(treta))
			for br in range(__interacoes__):
				treta = variavel.lower() + str(br) + "\n"
				lista.append(treta)
				verbos(4,'Senha gerada: ' + str(treta))
				if args[1] >= 2:
					treta = str(br) + variavel.lower() + "\n"
					lista.append(treta)
					verbos(4,'Senha gerada: ' + str(treta))
				if args[1] >= 1:
					for ponto in pontuacao:
						treta = variavel.lower() + str(br) + ponto + "\n"
						lista.append(treta)
						verbos(4,'Senha gerada: ' + str(treta))
						if args[1] >= 2:
							treta = variavel.lower() + ponto + str(br) + "\n"
							lista.append(treta)
							verbos(4,'Senha gerada: ' + str(treta))
						if args[1] >= 3:
							treta = str(br) + variavel.lower() + ponto + "\n"
							lista.append(treta)
							verbos(4,'Senha gerada: ' + str(treta))
	if tipo == 2: #tipo 2 e pra similaridades
		if qtsemelnome(variavel) > 0 and variavel.isalpha() == True:
			verbos(1,"Gerando senhas a partir do " + nomeamigavel + " com similaridades consideradas...")
			nomesemel = semelnome(variavel, 0, 2)
			for algo in dectsemels:
				nomenovo = semelnome(variavel, algo, 1)
				for ponto in pontuacao:
					treta = nomenovo + ponto + "\n"
					lista.append(treta)
					verbos(4,'Senha gerada: ' + str(treta))
				for br in range(__interacoes__):
					treta = nomenovo + str(br) + "\n"
					lista.append(treta)
					verbos(4,'Senha gerada: ' + str(treta))
					if args[1] >= 2:
						treta = str(br) + nomenovo + "\n"
						lista.append(treta)
						verbos(4,'Senha gerada: ' + str(treta))
					if args[1] >= 1:
						for ponto in pontuacao:
							treta = nomenovo + str(br) + ponto + "\n"
							lista.append(treta)
							verbos(4,'Senha gerada: ' + str(treta))
							if args[1] >= 2:
								treta = nomenovo + ponto + str(br) + "\n"
								lista.append(treta)
								verbos(4,'Senha gerada: ' + str(treta))
							if args[1] >= 3:
								treta = str(br) + nomenovo + ponto + "\n"
								lista.append(treta)
								verbos(4,'Senha gerada: ' + str(treta))
				for ponto in pontuacao:
					treta = variavel.lower() + ponto + "\n"
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
					if args[1] >= 1:
						for ponto in pontuacao:
							treta = nomenovo.lower() + str(br) + ponto + "\n"
							lista.append(treta)
							verbos(4,'Senha gerada: ' + str(treta))
							if args[1] >= 2:
								treta = nomenovo.lower() + ponto + str(br) + "\n"
								lista.append(treta)
								verbos(4,'Senha gerada: ' + str(treta))
							if args[1] >= 3:
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
				if args[1] >= 1:
					for ponto in pontuacao:
						treta = nomesemel + str(br) + ponto + "\n"
						lista.append(treta)
						verbos(4,'Senha gerada: ' + str(treta))
						if args[1] >= 2:
							treta = nomesemel + ponto + str(br) + "\n"
							lista.append(treta)
							verbos(4,'Senha gerada: ' + str(treta))
						if args[1] >= 3:
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
				if args[1] >= 1:
					for ponto in pontuacao:
						treta = nomesemel.lower() + str(br) + ponto + "\n"
						lista.append(treta)
						verbos(4,'Senha gerada: ' + str(treta))
						if args[1] >= 2:
							treta = nomesemel.lower() + ponto + str(br) + "\n"
							lista.append(treta)
							verbos(4,'Senha gerada: ' + str(treta))
						if args[1] >= 3:
							treta = str(br) + nomesemel.lower() + ponto + "\n"
							lista.append(treta)
							verbos(4,'Senha gerada: ' + str(treta))

def gerar():
	verbos(0,'Gerando senhas a partir dos dados fornecidos...')
	looploko(1,dadosvit['primeironome'],"primeiro nome")
	looploko(2,dadosvit['primeironome'],"primeiro nome")
	looploko(1,dadosvit['meionome'],"nome do meio")
	looploko(2,dadosvit['meionome'],"nome do meio")
	looploko(1,dadosvit['sobrenome'],"sobrenome")
	looploko(2,dadosvit['sobrenome'],"sobrenome")
	looploko(1,dadosvit['pamor'],"nome do primeiro amor")
	looploko(2,dadosvit['pamor'],"nome do primeiro amor")
	looploko(1,dadosvit['aamor'],"nome do atual amor")
	looploko(2,dadosvit['aamor'],"nome do atual amor")
	if dadosvit['username'].isalnum() == True:
		verbos(1,"Gerando senhas a partir do nome de usuario (username)...")
		for br in range(__interacoes__):
			treta = dadosvit['username'] + str(br) + "\n"
			lista.append(treta)
			verbos(4,'Senha gerada: ' + str(treta))
	if bool(dadosvit['qtmovel']) == True:
		verbos(2,"Gerando senhas a partir do(s) celular(s)/telefone(s)...")
		for dispmovel in dadosvit['celular']:
			indicecel = dadosvit['celular'].index(dispmovel)
			if dadosvit['celular'][indicecel].isnumeric() == True:
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

main()
