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
		dadosvit['username'] = arglin.username
		dadosvit['pamor'] = arglin.firstrelation
		dadosvit['aamor'] = arglin.actualrelation
		dadosvit['qtmovel'] = 0
	else:
		print("########################################################")
		print("#----------------AskPassGen Beta v3--------------------#")
		print("#---------Developer: Kevin Souza (@DarthSouza)---------#")
		print("#---------Created on: 05/09/2015 - 07:05 AM------------#")
		print("#---------Updated on: 06/11/2015 - 07:04 PM------------#")
		print("#---------Inspired by: Mr.Robot (The Series)-----------#")
		print("########################################################")
		print("")
		print("")
		args[1] = int(input("Level of Depth (0,1,2,3): "))
		args[2] = int(input("Level of Verbose (0,1,2,3,4): "))
		if args[1] == "" or args[1] == "0" or args[1] == 0:
			args[1] = arglin.profd
		if args[2] == "" or args[2] == "0" or args[2] == 0:
			args[2] = arglin.verb
		print("Type the target available information:")
		dadosvit['primeironome'] = input("First Name: ")
		dadosvit['meionome'] = input("Middle Name: ")
		dadosvit['sobrenome'] = input("Last Name: ")
		dadosvit['qtmovel'] = input("Quantity of mobile devices: ")
		if dadosvit['qtmovel'] == '' or dadosvit['qtmovel'] == 0 or dadosvit['qtmovel'] == '0':
			dadosvit['qtmovel'] = 0
		else:
			dadosvit['qtmovel'] = int(dadosvit['qtmovel'])
			dadosvit['celular'] = []
			for quantidade in range(dadosvit['qtmovel']):
				dadosvit['celular'].append(input("Phone Number #" + str(quantidade + 1) + ": "))
		dadosvit['username'] = input("Username: ")
		dadosvit['pamor'] = input("First relationship partner's name: ")
		dadosvit['aamor'] = input("Actual relationship partner's name: ")
	if checarinfo() < 2:
		limpatela()
		print('Are you on drugs? You did not provided any information. Dumb ass.')
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
		print('Shit... RUN DUDE! its gonna explode -qq')
		time.sleep(3)
		sys.exit(0)

def checarinfo():
	verbos(2,'Verifying provided information...')
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
		verbos(3,'Detecting similar letters on the name: ' + nome)
		for num in nsem:
			if nomenovo.count(nsem[num]) == 1:
				dectsemels.append(nsem[num])
				mudancas = mudancas + 1
		verbos(3,'There is ' + str(mudancas) + ' similar letters on the name: ' + nome)
	return mudancas

def looploko(tipo,variavel,nomeamigavel):
	if tipo == 1:
		if variavel.isalpha() == True:
			verbos(1,"Generating passwords from the " + nomeamigavel + " original...")
			for ponto in pontuacao:
				treta = variavel + ponto + "\n"
				lista.append(treta)
				verbos(4,'Generated password: ' + str(treta))
			for br in range(__interacoes__):
				treta = variavel + str(br) + "\n"
				lista.append(treta)
				verbos(4,'Generated password: ' + str(treta))
				if args[1] >= 2:
					treta = str(br) + variavel + "\n"
					lista.append(treta)
					verbos(4,'Generated password: ' + str(treta))
				if args[1] >= 1:
					for ponto in pontuacao:
						treta = variavel + str(br) + ponto + "\n"
						lista.append(treta)
						verbos(4,'Generated password: ' + str(treta))
						if args[1] >= 2:
							treta =  variavel + ponto + str(br) + "\n"
							lista.append(treta)
							verbos(4,'Generated password: ' + str(treta))
						if args[1] >= 3:
							treta = str(br) + variavel + ponto + "\n"
							lista.append(treta)
							verbos(4,'Generated password: ' + str(treta))
			verbos(2,"Generating passwords from the " + nomeamigavel + " original with lowercase letters...")
			for ponto in pontuacao:
				treta = variavel.lower() + ponto + "\n"
				lista.append(treta)
				verbos(4,'Generated password: ' + str(treta))
			for br in range(__interacoes__):
				treta = variavel.lower() + str(br) + "\n"
				lista.append(treta)
				verbos(4,'Generated password: ' + str(treta))
				if args[1] >= 2:
					treta = str(br) + variavel.lower() + "\n"
					lista.append(treta)
					verbos(4,'Generated password: ' + str(treta))
				if args[1] >= 1:
					for ponto in pontuacao:
						treta = variavel.lower() + str(br) + ponto + "\n"
						lista.append(treta)
						verbos(4,'Generated password: ' + str(treta))
						if args[1] >= 2:
							treta = variavel.lower() + ponto + str(br) + "\n"
							lista.append(treta)
							verbos(4,'Generated password: ' + str(treta))
						if args[1] >= 3:
							treta = str(br) + variavel.lower() + ponto + "\n"
							lista.append(treta)
							verbos(4,'Generated password: ' + str(treta))
	if tipo == 2: #tipo 2 e pra similaridades
		if qtsemelnome(variavel) > 0 and variavel.isalpha() == True:
			verbos(1,"Generating passwords from the " + nomeamigavel + " with the similar letters replaced...")
			nomesemel = semelnome(variavel, 0, 2)
			for algo in dectsemels:
				nomenovo = semelnome(variavel, algo, 1)
				for ponto in pontuacao:
					treta = nomenovo + ponto + "\n"
					lista.append(treta)
					verbos(4,'Generated password: ' + str(treta))
				for br in range(__interacoes__):
					treta = nomenovo + str(br) + "\n"
					lista.append(treta)
					verbos(4,'Generated password: ' + str(treta))
					if args[1] >= 2:
						treta = str(br) + nomenovo + "\n"
						lista.append(treta)
						verbos(4,'Generated password: ' + str(treta))
					if args[1] >= 1:
						for ponto in pontuacao:
							treta = nomenovo + str(br) + ponto + "\n"
							lista.append(treta)
							verbos(4,'Generated password: ' + str(treta))
							if args[1] >= 2:
								treta = nomenovo + ponto + str(br) + "\n"
								lista.append(treta)
								verbos(4,'Generated password: ' + str(treta))
							if args[1] >= 3:
								treta = str(br) + nomenovo + ponto + "\n"
								lista.append(treta)
								verbos(4,'Generated password: ' + str(treta))
				for ponto in pontuacao:
					treta = variavel.lower() + ponto + "\n"
					lista.append(treta)
					verbos(4,'Generated password: ' + str(treta))
				for br in range(__interacoes__):
					treta = nomenovo.lower() + str(br) + "\n"
					lista.append(treta)
					verbos(4,'Generated password: ' + str(treta))
					if args[1] >= 2:
						treta = str(br) + nomenovo.lower() + "\n"
						lista.append(treta)
						verbos(4,'Generated password: ' + str(treta))
					if args[1] >= 1:
						for ponto in pontuacao:
							treta = nomenovo.lower() + str(br) + ponto + "\n"
							lista.append(treta)
							verbos(4,'Generated password: ' + str(treta))
							if args[1] >= 2:
								treta = nomenovo.lower() + ponto + str(br) + "\n"
								lista.append(treta)
								verbos(4,'Generated password: ' + str(treta))
							if args[1] >= 3:
								treta = str(br) + nomenovo.lower() + ponto + "\n"
								lista.append(treta)
								verbos(4,'Generated password: ' + str(treta))
			for br in range(__interacoes__):
				treta = nomesemel + str(br) + "\n"
				lista.append(treta)
				verbos(4,'Generated password: ' + str(treta))
				if args[1] >= 2:
					treta = str(br) + nomesemel + "\n"
					lista.append(treta)
					verbos(4,'Generated password: ' + str(treta))
				if args[1] >= 1:
					for ponto in pontuacao:
						treta = nomesemel + str(br) + ponto + "\n"
						lista.append(treta)
						verbos(4,'Generated password: ' + str(treta))
						if args[1] >= 2:
							treta = nomesemel + ponto + str(br) + "\n"
							lista.append(treta)
							verbos(4,'Generated password: ' + str(treta))
						if args[1] >= 3:
							treta = str(br) + nomesemel + ponto + "\n"
							lista.append(treta)
							verbos(4,'Generated password: ' + str(treta))
			for br in range(__interacoes__):
				treta = nomesemel.lower() + str(br) + "\n"
				lista.append(treta)
				verbos(4,'Generated password: ' + str(treta))
				if args[1] >= 2:
					treta = str(br) + nomesemel.lower() + "\n"
					lista.append(treta)
					verbos(4,'Generated password: ' + str(treta))
				if args[1] >= 1:
					for ponto in pontuacao:
						treta = nomesemel.lower() + str(br) + ponto + "\n"
						lista.append(treta)
						verbos(4,'Generated password: ' + str(treta))
						if args[1] >= 2:
							treta = nomesemel.lower() + ponto + str(br) + "\n"
							lista.append(treta)
							verbos(4,'Generated password: ' + str(treta))
						if args[1] >= 3:
							treta = str(br) + nomesemel.lower() + ponto + "\n"
							lista.append(treta)
							verbos(4,'Generated password: ' + str(treta))


def gerar():
	verbos(0,'Generating passwords based on the information provided...')
	looploko(1,dadosvit['primeironome'],"first name")
	looploko(2,dadosvit['primeironome'],"first name")
	looploko(1,dadosvit['meionome'],"middle name")
	looploko(2,dadosvit['meionome'],"middle name")
	looploko(1,dadosvit['sobrenome'],"last name")
	looploko(2,dadosvit['sobrenome'],"last name")
	looploko(1,dadosvit['pamor'],"first relationship partner's name")
	looploko(2,dadosvit['pamor'],"first relationship partner's name")
	looploko(1,dadosvit['aamor'],"actual relationship partner's name")
	looploko(2,dadosvit['aamor'],"actual relationship partner's name")
	if dadosvit['username'].isalnum() == True:
		verbos(1,"Generating passwords from the username...")
		for br in range(__interacoes__):
			treta = dadosvit['username'] + str(br) + "\n"
			lista.append(treta)
			verbos(4,'Generated password: ' + str(treta))
	if dadosvit['qtmovel'] >= 1:
		verbos(2,"Generating passwords based on the phone's numbers...")
		for dispmovel in dadosvit['celular']:
			indicecel = dadosvit['celular'].index(dispmovel)
			if dadosvit['celular'][indicecel].isnumeric() == True:
				treta = dadosvit['celular'][indicecel] + "\n"
				lista.append(treta)
				verbos(4,'Generated password: ' + str(treta))
	if dadosvit['primeironome'].isalpha() == True:
		verbos(3,"Generating passwords file's name...")
		nomefile = dadosvit['primeironome'].lower()
		if dadosvit['sobrenome'].isalpha() == True:
			nomefile = nomefile + "_" + dadosvit['sobrenome'].lower()
	verbos(0,"Storing the generated passwords...")
	verbos(1,"Storing the generated passwords...")
	arquivar(nomefile,lista)
	verbos(1,"Generated passwords saved on: " + nomefile + ".txt")

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
	print("Job Done! See ya.")

main()
