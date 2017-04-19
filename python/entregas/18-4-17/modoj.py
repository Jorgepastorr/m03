#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
###############################################################
#				Que hace?
###############################################################

###############################################################
#				importaciones
###############################################################
import os
from random import randint

os.system('clear')
###############################################################
#				variables globales
###############################################################
credito = 100
rata = 0
salir2 = False
salir1 = False
salir3 = False

###############################################################
#				nivel 3
###############################################################
def condiciones():
	if apuesta == -1 or rata == 3 :
		global salir1
		salir1 = True
		global salir2
		salir2 = True
	
	elif apuesta > credito :
		print "¡¡No puedes apostar tanto!!"
		print ""
	
	elif apuesta < 10 :
		print "apuesa mínima es de 10"
		global rata
		rata = rata +1
	
	elif apuesta <= credito :		
		salir1 = True	

def cartaj1():
	global numeroj
	numeroj=j1num
	if (j1num==11):
		numeroj="J"
	if (j1num==12):
		numeroj="Q"
	if (j1num==13):
		numeroj="K"
	if (j1num==14):
		numeroj="A"
		
	global palj
	if (j1pal==1):
		palj="Picas"
	if (j1pal==2):
		palj="Treboles"
	if (j1pal==3):
		palj="Diamantes"
	if (j1pal==4):
		palj="Corazones"

	

def cartamaq():
	global numerom
	numerom=j2num
	if (j2num==11):
		numerom="J"
	if (j2num==12):
		numerom="Q"
	if (j2num==13):
		numerom="K"
	
	global palm
	if (j2pal==1):
		palm="Picas"
	if (j2pal==2):
		palm="Treboles"
	if (j2pal==3):
		palm="Diamantes"
	if (j2pal==4):
		palm="Corazones"

def condicion_entrada2():
	global salir3
	global salir1
	global salir2
	global rata
	
	print "Tienes",credito,"€"
	print "-1 Salir"
	apuesta = input("Cuanto quiere apostar: ")
	os.system('clear')

	if apuesta == -1 or rata == 3 :
		salir1 = True
		salir2 = True
		salir3 = True
	
	elif apuesta > credito :
		print "¡¡No puedes apostar tanto!!"
		print ""
	
	elif apuesta < 10 :
		print "apuesa mínima es de 10"
		rata = rata +1
	
	elif apuesta <= credito :		
		salir3 = True
###############################################################
#				nivel 2
###############################################################
def condicion_entrada():
	print "Tienes",credito,"€"
	print "-1 Salir"
	global apuesta
	apuesta = input("Cuanto quiere apostar:" )
	os.system('clear')

# condicióm de salida apuesta -1, sin credito o fallar 3 veces apuesta mínima				
	condiciones()
	

def jugada_j1():
	# Generem la tirada de jugador1 (agafa una carta aleatoria)
	global j1num
	j1num=randint(2,14)
	global j1pal
	j1pal=randint(1,4)
	
	cartaj1()
	print "Jugador 1 te: " , numeroj, "de " , palj
	
def jugada_j2():
	
	# Generem la tirada de jugador2 (agafa una carta aleatoria)
	global j2num
	j2num=randint(1,13)
	global j2pal
	j2pal=randint(1,4)
	
	cartamaq()
	print "Jugador 2 te: " , numerom, "de " , palm

def resultado():
	global credito

	if j1num==j2num :
		print "¡¡Empate!!"
		
	elif j1num>j2num :
	
		print "tu:",numeroj,palj,"Maquina:",numerom,palm," ¡¡Ganas tu!!"
		credito = credito + apuesta
					
	else:
		print "tu:",numeroj,palj,"Maquina:",numerom,palm," ¡¡Pierdes!!"
		credito = credito - apuesta		

def siguiente_apuesta():
	global salir3
	global salir1
	global salir2
	global rata
	
	if credito < 10 :
		print ("\033[;31m"+"Te quedaste sin pasta ¡¡Pringado!!"+"\033[0;m")
		print ""
		salir2 = True
	else:
		salir3 = False
		while salir3 == False:
			condicion_entrada2()
			
			
###############################################################
#				nivel 1
###############################################################

while salir1 == False:
	
	condicion_entrada()

while salir2 == False:
	
	jugada_j1()
	jugada_j2()

	
	resultado()
			
	siguiente_apuesta()	
	
