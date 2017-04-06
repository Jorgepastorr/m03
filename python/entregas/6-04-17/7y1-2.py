#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
os.system('clear')
from random import randint

tipo=randint(1,4)
maq = randint(1,7)
j1 = randint(1,10)
d={1:'oros',2:'espadas',3:'bastos',4:'copas'}

if j1 > 7:
	if j1 == 8 :
		j1 = 0.5
		print j1,'sota',d[tipo]
	if j1 == 9 :
		j1 = 0.5
		print j1,'caballo',d[tipo]
	if j1 == 10 :
		j1 = 0.5
		print j1,'rey',d[tipo]
		
else:
	print j1,d[tipo]

salir = False
while salir == False :
		
	if j1 > 7.5 :
		print 'Te as pasado'
		salir = True
	else:	
		op=raw_input('Quieres otra carta? s/n: ')
		if op == 'n':
			if j1 == maq :
				print 'empate tu',j1,'maquina',maq
				salir = True
			elif j1 > maq :
				print 'ganas',j1,'mayor',maq
				salir = True
				
			elif j1 < maq :
				print 'pierdes',j1,'menor',maq
				salir = True
		if op == 's':
			fi = randint(1,10)
			if fi > 7:
				if fi == 8 :
					print 'sota',d[tipo]
					fi = 0.5
				if fi == 9 :
					print 'caballo',d[tipo]
					fi = 0.5
				if fi == 10 :
					print 'rey',d[tipo]
					fi = 0.5
				j1 = fi + j1
				print 'Tienes: ',j1
			else:
				print fi,d[tipo]
				j1 = fi + j1
				print 'Tienes: ',j1
