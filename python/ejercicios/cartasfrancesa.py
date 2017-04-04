#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
os.system('clear')
from random import randint

j1 = randint(1,13)
maq = randint(1,13)
tipo = randint(1,4)

# 11 a 13 de maquina
if maq == 11 :
	maq1 = "J"
elif maq == 12 :
	maq1 = "Q"
elif maq == 13 :
	maq1 = "K"

# 11 a 13 de jugador
if j1 == 11 :
	j11 = "J"
elif j1 == 12 :
	j11 = "Q"
elif j1 == 13 :
	j11 = "K"


# define tipos
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
	if j1 > 10 :
		j1 = j11
	if maq > 10 :
		maq = maq1
	print "tu:",j1,tipo,"Maquina:",maq,tipo," ¡¡Ganas tu!!"
else:
	if j1 > 10 :
		j1 = j11
	if maq > 10 :
		maq = maq1
	print "tu:",j1,tipo,"Maquina:",maq,tipo," ¡¡Pierdes!!"
