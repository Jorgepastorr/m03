#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from random import randint

credito = 100
rata = 0

os.system('clear')

salir = False
while salir == False:
	print "Tienes",credito,"€"
	print "-1 Salir"
	apuesta = input("Cuanto quiere apostar: ")
	os.system('clear')
	
# condicióm de salida apuesta -1, sin credito o fallar 3 veces apuesta mínima	
	if apuesta == -1 or rata == 3 :
		salir = True
	elif apuesta > credito :
		print "¡¡No puedes apostar tanto!!"
		print ""
	
	elif apuesta < 10 :
		print "apuesa mínima es de 10"
		rata = rata +1
	
	else:
		if apuesta <= credito :		
						
			j1 = randint(2,14)
			maq = randint(2,14)
			tipo = randint(1,4)
	
			# 11 a 13 de maquina le asigna una letra
			if maq == 11 :
				maq1 = "J"
			elif maq == 12 :
				maq1 = "Q"
			elif maq == 13 :
				maq1 = "K"
			elif maq == 14 :
				maq1 = "A"
				
			# 11 a 13 de jugador le asigna una letra
			if j1 == 11 :
				j11 = "J"
			elif j1 == 12 :
				j11 = "Q"
			elif j1 == 13 :
				j11 = "K"
			elif j1 == 14 :
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
		
		
			if maq == j1 :
				print "¡¡Empate!!"
			elif j1 > maq :
			# gana jugador1 si elguna variable es mayor que 10 se le asigna la variable con catacter alfabetico.	
				if j1 > 10 :
					j1 = j11
				if maq > 10 :
					maq = maq1
				print "tu:",j1,tipo,"Maquina:",maq,tipo," ¡¡Ganas tu!!"
				credito = credito + apuesta
							
			else:
			# pierde jugador1 si elguna variable es mayor que 10 se le asigna la variable con catacter alfabetico.
				if j1 > 10 :
					j1 = j11
				if maq > 10 :
					maq = maq1
				print "tu:",j1,tipo,"Maquina:",maq,tipo," ¡¡Pierdes!!"
				credito = credito - apuesta				
			
			if credito < 10 :
				print ("\033[;31m"+"Te quedaste sin pasta ¡¡Pringado!!"+"\033[0;m")
				print ""
				salir = True
