#!/usr/bin/env python
# -*- coding: utf-8 -*-
########## random sin que se rtepitan los numeros nunca.
## cundo se acaban los números existentes sale.

from random import randint
import os
os.system("clear")

## lista bacia donde se ayadiran los números
li=[]

while True:
	num = randint(0,5)		# crea números
	
	if len(li) == 6 :       ## len indica cuantos números hay en la lista
		print "salir"		# si hay 6 en la lista sale del bucle
		break
	if not num in li :		### Si no existe número en la lista entra.
		print num			# muestra número
		li.insert(1,num)	# lo añade en la lista
		print li			# muestra la lista
							# y vuelve a empezar el bucle.
	
