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
		
for i in mi_rango(2,9,3):
	print i







