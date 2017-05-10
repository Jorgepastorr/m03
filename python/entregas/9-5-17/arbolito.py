#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

def mi_rango(inicio,final,incremento):
	
	if inicio <= final :
		while inicio <= final :
			yield inicio
			inicio = inicio + incremento
	else:
		while inicio >= final :
			yield inicio
			inicio = inicio - incremento
		
#############3
		
for fila in mi_rango(1,6,1):
	for columna in mi_rango(1,5,1):
		
		if  (fila == 1 and columna == 3 ):
			print "*",
		
		elif ((fila == 2 and columna == 3 )or
			 ( fila == 3 and ( columna >= 2 and columna <= 4 )) or
			 ( fila == 4 ) ):
			 print "A",
		
		elif ( columna == 3 ):
			print "N",
		else:
			print " ",
	
	print " "
