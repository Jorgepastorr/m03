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
		
#############3
		
for fila in mi_rango(1,8,1):
	for columna in mi_rango(1,8,1):
		
		if ((fila%2==1 and columna%2==1 )or
			(fila%2==0 and columna%2==0 )):
			print "*",
		else:
			print " ",
		
			
	
	print " "
