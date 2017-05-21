#!/usr/bin/env python
# -*- coding: utf-8 -*-

def mi_rango(inicio,final,incremento):

	while inicio <= final :
		yield inicio
		inicio = inicio + incremento

resultado= 0
final= 0

binario=input("inserte binario de 8 numeros: ")

for vuelta in mi_rango(0,7,1):
	if vuelta == 0:
		if binario%10==1 :
			final = 2**vuelta
		
		resultado = binario // 10 
	
	else:
		if resultado%10==1 :
			final= final+2**vuelta
			
		resultado = resultado // 10 
			
print final
