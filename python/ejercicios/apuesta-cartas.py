#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
os.system('clear')
from random import randint
credito = 100

salir = False
while salir == False:
	print "Tienes",credito,"€"
	apuesta = input("Cuanto quiere apostar tienes : ")
	os.system('clear')
	
# condicióm de salida apuesta 0 o sin credito
	
	if apuesta == 0 :
		salir = True
	elif apuesta > credito :
		print "¡¡No puedes apostar tanto!!"
		print ""
	else:
		if apuesta <= credito :
		
			j1 = randint(1,13)
			maq = randint(1,13)
			tipo = randint(1,4)

			# 11 a 13 de maquina le asigna una letra
			if maq == 11 :
				maq1 = "J"
			elif maq == 12 :
				maq1 = "Q"
			elif maq == 13 :
				maq1 = "K"

			# 11 a 13 de jugador le asigna una letra
			if j1 == 11 :
				j11 = "J"
			elif j1 == 12 :
				j11 = "Q"
			elif j1 == 13 :
				j11 = "K"

			# define tipos de cartas
			if tipo == 1 :
				tipo = "treboles"
			elif tipo == 2 :
				tipo = "picas"
			elif tipo == 3 :
				tipo = "corazones"
			elif tipo == 4 :
				tipo = "diamantes"

			# gana jugador1 si elguna variable es mayor que 10 se le asigna la variable con catacter alfabetico.
			if maq == j1 :
				print "¡¡Empate!!"
			elif j1 > maq :
				if j1 > 10 :
					j1 = j11
				if maq > 10 :
					maq = maq1
				print "tu:",j1,tipo,"Maquina:",maq,tipo," ¡¡Ganas tu!!"
				credito = credito + apuesta
			# pierde jugador1 si elguna variable es mayor que 10 se le asigna la variable con catacter alfabetico.
			else:
				if j1 > 10 :
					j1 = j11
				if maq > 10 :
					maq = maq1
				print "tu:",j1,tipo,"Maquina:",maq,tipo," ¡¡Pierdes!!"
				credito = credito - apuesta
			
			if credito <= 0 :
				print ("\033[;31m"+"Te quedaste sin pasta ¡¡Pringado!!"+"\033[0;m")
				print ""
				salir = True
