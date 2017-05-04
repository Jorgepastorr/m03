#!/usr/bin/env python
# -*- coding: utf-8 -*-

def mi_rango(inicio,final,incremento):
	
	if inicio <= final :
		while inicio <= final :
			yield inicio
			inicio = inicio + incremento
	else:
		while inicio >= final :
			yield inicio
			inicio = inicio - incremento

#########################

#########################


for fila in mi_rango(1,5,1):
	print ""
	for columna in mi_rango(1,4,1):
		if fila == 1:			
			if columna == 2:
				print "A",
			elif columna == 3:
				print "B",
			elif columna == 4:
				print "C",
			else:
				print "-",
	
		elif columna == 1:
			print fila-1,
		else:
			print "-",





