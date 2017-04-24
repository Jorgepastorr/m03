#!/usr/bin/env python
# -*- coding: utf-8 -*-
##########################################################
#####				Que hace?
###	Juego de apuestas a la carta mas alta
##########################################################


##########################################################
#####				importaciones
##########################################################
import os
from random import randint
os.system('clear')
##########################################################
#####				varibales
##########################################################

credito = 100
rata = 0 ### Si falla al apostar
salir = False  ###  bucle juego  
salir1 = False  ### bucle apuestas
apuesta = 0
j1 = 0
j11=0
maq=0
maq1=0
tipo=0
tipo1=0
##########################################################
#####				level 3
##########################################################

##########################################################
#####				level 2
##########################################################

####
def apuesta_condicion_entrada(salir,apuesta,credito,rata):
	
	## despues de cada jugada mira que tengas mas de 10, si nno te hecha
	if credito < 10 :
		print ("\033[;31m"+"Te quedaste sin pasta ¡¡Pringado!!\n"+"\033[0;m")
		salir = True
	
	else:
		## Apuesta
		print "Tienes",credito,"€"
		print "-1 Salir"
		apuesta = input("Cuanto quiere apostar: ")
		os.system('clear')

		salir1 = False
		## condiciones de salida
		while salir1 == False:
			if apuesta == -1 or rata == 3 :
				salir = True
				salir1 = True
			
			elif apuesta >= 10 and apuesta <= credito:
				salir1 = True
				credito = credito - apuesta
			else:
				if apuesta < 10 :
					print "apuesa mínima es de 10"
					rata = rata +1
			
				if apuesta > credito:
					print "¡¡No puedes apostar tanto!!"
				
				## si fallas condicioners vuelves a apostar 	
				print "Tienes",credito,"€"
				print "-1 Salir"
				apuesta = input("Cuanto quiere apostar: ")
				os.system('clear')
	
	return salir,apuesta,credito,rata
######

def resultado(maq,j1,maq1,j11,tipo,tipo1,credito,apuesta):

	if maq == j1 :
		print "¡¡Empate!!"
	elif j1 > maq :
	# gana jugador1 
		print "tu:",j11,tipo,"Maquina:",maq1,tipo1," ¡¡Ganas tu!!"
		credito = credito + ( apuesta * 2 )					
	else:
	# pierde jugador1
		print "tu:",j11,tipo,"Maquina:",maq1,tipo1," ¡¡Pierdes!!"

	return credito,apuesta
	
#######

def jugada(salir,j1,maq,tipo,tipo1):	

	j1 = randint(2,14)
	maq = randint(2,14)
	tipo = randint(1,4)
	tipo1 = randint(1,4)
	
	# 11 a 13 de maquina le asigna una letra
	maq1 = maq 
	if maq1 == 11 :
		maq1 = "J"
	elif maq1 == 12 :
		maq1 = "Q"
	elif maq1 == 13 :
		maq1 = "K"
	elif maq1 == 14 :
		maq1 = "A"
		
	# 11 a 13 de jugador le asigna una letra
	j11 = j1
	if j11 == 11 :
		j11 = "J"
	elif j11 == 12 :
		j11 = "Q"
	elif j11 == 13 :
		j11 = "K"
	elif j11 == 14 :
		j11 = "A"

	# define tipos de cartas
	if tipo == 1 :
		tipo = "treboles"
	elif tipo == 2 :
		tipo = "picas"
	elif tipo == 3 :
		tipo = "corazones"
	elif tipo == 4 :
		tipo = "diamantes"
	
	if tipo1 == 1 :
		tipo1 = "treboles"
	elif tipo1 == 2 :
		tipo1 = "picas"
	elif tipo1 == 3 :
		tipo1 = "corazones"
	elif tipo1 == 4 :
		tipo1 = "diamantes"
		
	return salir,j1,j11,maq,maq1,tipo,tipo1

##########################################################
#####				level 1
##########################################################

# genera apuesta y condicion de salida
salir,apuesta,credito,rata = apuesta_condicion_entrada(salir,apuesta,credito,rata) 

# genera jugada
while salir == False:		
	salir,j1,j11,maq,maq1,tipo,tipo1 = jugada(salir,j1,maq,tipo,tipo1)
	
	## resultado de la jugada
	credito,apuesta = resultado(maq,j1,maq1,j11,tipo,tipo1,credito,apuesta)
	
	# genera apuesta y condicion de salida						
	salir,apuesta,credito,rata = apuesta_condicion_entrada(salir,apuesta,credito,rata) 
