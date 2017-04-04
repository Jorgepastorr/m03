#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from random import randint
os.system('clear')
#tirada de jugador
j1 = raw_input("Opciones a elegir /pa/pi/ti/la/sp: ")

#aleatorio maquina
maq = randint(1,5)

if maq == 1 :
	maq = "pa"
elif maq == 2 :
	maq = "pi"
elif maq == 3 :
	maq = "ti"
elif maq == 4 :
	maq = "la"
elif maq == 5 :
	maq = "sp"


# de 25 opciones descarto 5 igiales	
if j1 == maq :
	print "¡¡Empate!!"
else:
# de 20 opciones descarto 10 que puede ganar j1
	if (( j1 == "pa" and ( maq == "sp" or maq == "pi")) or
	    ( j1 == "pi" and ( maq == "ti" or maq == "la")) or
	    ( j1 == "ti" and ( maq == "pa" or maq == "la")) or
	    ( j1 == "la" and ( maq == "sp" or maq == "pa")) or
	    ( j1 == "sp" and ( maq == "pi" or maq == "ti")) 
	   ):
		   print "Tu",j1,"Maquina",maq,": ¡¡Ganas tu!!"
	else:
	# solo quedan las 10 opciones que ganaria maquina
		print "Tu",j1,"Maquina",maq,": ¡¡Pierdes!!!"

		
